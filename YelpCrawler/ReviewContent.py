import urllib.request
import urllib
import re
import Function
from bs4 import BeautifulSoup
from datetime import datetime


class ReviewElement:
    def __init__(self, _RestaurantId, _ReviewId, _UserId, _AtPage, _OrderNumOfPage, _ReviewDate):
        self.RestaurantId = _RestaurantId
        self.ReviewId = _ReviewId
        self.UserId = _UserId
        self.AtPage = _AtPage
        self.OrderNumOfPage = _OrderNumOfPage
        self.ReviewDate = _ReviewDate


class ReviewScoreElement:
    def __init__(self, _ReviewId, _ReviewRating, _Useful, _Funny, _Cool):
        self.ReviewId = _ReviewId
        self.ReviewRating = _ReviewRating
        self.Useful = _Useful
        self.Funny = _Funny
        self.Cool = _Cool


class ReviewDetailElement:
    def __init__(self, _ReviewId, _ReviewContent, _PhotoCnt, _MorePhoto):
        self.ReviewId = _ReviewId
        self.ReviewContent = _ReviewContent
        self.PhotoCnt = _PhotoCnt
        self.MorePhoto = _MorePhoto


def run_program(index, SystemTime):
    OverviewList.clear()
    ScoreList.clear()
    DetailList.clear()

    rId = index[0]
    url = index[1]

    print('[System]Now is ' + rId + ' running')

    cursor = Function.DatabaseConnectionBuilder()
    req = urllib.request.urlopen(url)
    content = req.read().decode(req.info().get_content_charset()).replace("\n", "")

    soup = BeautifulSoup(content, "html.parser")
    star = soup.select(".histogram_count")
    cursor.execute(
        "INSERT INTO RestaurantDetail(RestaurantId,Star5, Star4,Star3,Star2,Star1,TimeStamp) values ('" + str(
            index[0]) + "', '" + str(star[0].text) + "','" + str(star[1].text) + "','" + str(
            star[2].text) + "','" + str(
            star[3].text) + "','" + str(star[4].text) + "','" + SystemTime + "')")
    cursor.commit()

    TotalPage = int(re.findall("Page 1 of (.*?) ", re.sub('\s+', ' ', soup.select(".page-of-pages")[0].text))[0])

    tag = soup.select(".review--with-sidebar")

    if 'Start your review' in tag[0].text or 'Select your rating' in tag[0].text:
        del tag[0]

    OrderNum = 1
    for index in tag:
        soup2 = BeautifulSoup(index.prettify(), "html.parser")
        date = soup2.select(".rating-qualifier > meta")
        if len(date) == 0:
            print('problem')

        date = datetime.strptime(date[0]['content'], "%Y-%m-%d").date()
        if date <= datetime.strptime('2016-3-28', "%Y-%m-%d").date():
            return OverviewList, ScoreList, DetailList

        _ReviewId = index['data-review-id']
        _UserId = index['data-signup-object'].replace('user_id:', '')

        temp = soup2.select(".vote-item")
        useful = temp[0].text.replace('\n', '').replace(' ', '').replace('Useful', '')
        funny = temp[1].text.replace('\n', '').replace(' ', '').replace('Funny', '')
        cool = temp[2].text.replace('\n', '').replace(' ', '').replace('Cool', '')

        if len(useful) > 0:
            useful = int(useful)
        else:
            useful = 0

        if len(funny) > 0:
            funny = int(funny)
        else:
            funny = 0

        if len(cool) > 0:
            cool = int(cool)
        else:
            cool = 0

        rating = soup2.select(".rating-very-large > meta")[0].get('content')
        ReviewContent = soup2.select("p")[0].text.replace('\n', '').strip()
        ReviewContent = re.sub('\s+', ' ', ReviewContent).replace(',', '@[CMA]').replace("'", "''")
        PhotoCnt = soup2.select(".photo-box-grid > li")
        PhotoCnt = len(PhotoCnt)

        if (PhotoCnt > 3):
            MorePhoto = True
        else:
            MorePhoto = False

        OverviewList.append(ReviewElement(rId, _ReviewId, _UserId, '1', OrderNum, date))
        ScoreList.append(ReviewScoreElement(_ReviewId, rating, useful, funny, cool))
        DetailList.append(ReviewDetailElement(_ReviewId, ReviewContent, PhotoCnt, MorePhoto))

        OrderNum += 1

    for i in range(2, TotalPage, 1):

        req = urllib.request.urlopen(url + '?sort_by=date_desc&start=' + str((i - 1) * 20))
        content = req.read().decode(req.info().get_content_charset()).replace("\n", "")
        soup = BeautifulSoup(content, "html.parser")
        tag = soup.select(".review--with-sidebar")

        if 'Start your review' in tag[0].text:
            del tag[0]
        OrderNum = 1
        for index in tag:
            soup2 = BeautifulSoup(index.prettify(), "html.parser")
            date = soup2.select(".rating-qualifier > meta")
            if len(date) == 0:
                print('problem')

            date = datetime.strptime(date[0]['content'], "%Y-%m-%d").date()
            if date <= datetime.strptime('2016-3-28', "%Y-%m-%d").date():
                return OverviewList, ScoreList, DetailList

            _ReviewId = index['data-review-id']
            _UserId = index['data-signup-object'].replace('user_id:', '')

            temp = soup2.select(".vote-item")
            useful = temp[0].text.replace('\n', '').replace(' ', '').replace('Useful', '')
            funny = temp[1].text.replace('\n', '').replace(' ', '').replace('Funny', '')
            cool = temp[2].text.replace('\n', '').replace(' ', '').replace('Cool', '')

            if len(useful) > 0:
                useful = int(useful)
            else:
                useful = 0

            if len(funny) > 0:
                funny = int(funny)
            else:
                funny = 0

            if len(cool) > 0:
                cool = int(cool)
            else:
                cool = 0

            rating = soup2.select(".rating-very-large > meta")[0].get('content')
            ReviewContent = soup2.select("p")[0].text.replace('\n', '').strip()
            ReviewContent = re.sub('\s+', ' ', ReviewContent).replace(',', '@[CMA]').replace("'", "''")
            PhotoCnt = soup2.select(".photo-box-grid > li")
            PhotoCnt = len(PhotoCnt)

            if (PhotoCnt > 3):
                MorePhoto = True
            else:
                MorePhoto = False

            OverviewList.append(ReviewElement(rId, _ReviewId, _UserId, '1', OrderNum, date))
            ScoreList.append(ReviewScoreElement(_ReviewId, rating, useful, funny, cool))
            DetailList.append(ReviewDetailElement(_ReviewId, ReviewContent, PhotoCnt, MorePhoto))

            OrderNum += 1
            
    return OverviewList, ScoreList, DetailList


OverviewList = []
ScoreList = []
DetailList = []
