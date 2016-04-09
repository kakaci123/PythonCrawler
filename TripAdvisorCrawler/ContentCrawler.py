import urllib.request
import re
from bs4 import BeautifulSoup


class ContentElement:
    def __init__(self, _ReviewId, _ReviewTitle, _ReviewRating, _RatingDate, _ReviewContent, _ReviewHelpfulvotes):
        self.ReviewId = _ReviewId
        self.ReviewTitle = _ReviewTitle
        self.ReviewRating = _ReviewRating
        self.RatingDate = _RatingDate
        self.Partial = 'not yet'
        self.ReviewContent = _ReviewContent
        self.ReviewHelpfulvotes = _ReviewHelpfulvotes


def content_crawler(url, UserId):
    req = urllib.request.urlopen(url)
    content = req.read().decode(req.info().get_content_charset())
    soup = BeautifulSoup(content, "html.parser")
    getId = soup.findAll('div', attrs={'class': 'memberOverlayLink'})

    if len(getId) == 0:
        Check_UId = '-1'
        Check_RId = re.findall('reviews=(.*)', url)[0]
    else:
        check = re.findall('UID_(.*?)-SRC_(.*?)$', getId[0].get('id'))
        Check_UId = check[0][0]
        Check_RId = check[0][1]

    if UserId == Check_UId and Check_RId in url:

        Temp_Element = soup.find('span', attrs={'class': 'noQuotes'})
        if Temp_Element is not None:
            title = Temp_Element.text
        else:
            title = '-1'

        Temp_Element = soup.select('.reviewItemInline > span > img')
        if len(Temp_Element) != 0:
            rating = re.findall('(.*?) of 5 stars', soup.select('.reviewItemInline > span > img')[0]['alt'])[0]
        else:
            rating = '-1'

        Temp_Element = soup.find('span', attrs={'class': 'ratingDate'})
        if Temp_Element is not None:
            if Temp_Element.get('title') is not None:
                TempDate = Temp_Element.get('title')
            else:
                TempDate = Temp_Element.contents[0].replace('Reviewed ', '').replace('\n', '')
        else:
            TempDate = '-1'

        year = TempDate.split(',')[1].replace(' ', '')
        monthandday = TempDate.split(',')[0]
        month = monthandday.split(' ')[0].replace(' ', '')

        if month == 'January':
            month = '1'
        elif month == 'February':
            month = '2'
        elif month == 'March':
            month = '3'
        elif month == 'April':
            month = '4'
        elif month == 'May':
            month = '5'
        elif month == 'June':
            month = '6'
        elif month == 'July':
            month = '7'
        elif month == 'August':
            month = '8'
        elif month == 'September':
            month = '9'
        elif month == 'October':
            month = '10'
        elif month == 'November':
            month = '11'
        elif month == 'December':
            month = '12'

        day = monthandday.split(' ')[1].replace(' ', '')
        date = year + '-' + month + '-' + day

        Temp_Element = soup.find('div', attrs={'class': 'entry'})
        if Temp_Element is not None:
            content = Temp_Element.text.replace('\n', '').replace('"', '')
        else:
            content = '-1'

        Temp_Element = soup.select('.numHlp')
        if len(Temp_Element) != 0:
            helpfulvote = Temp_Element[0].text.replace('\n', '')
        else:
            helpfulvote = '0'

        Temp_Info = ContentElement(Check_RId, title, rating, date, content, helpfulvote)
        return Temp_Info
    else:
        print('Can not find the review')
