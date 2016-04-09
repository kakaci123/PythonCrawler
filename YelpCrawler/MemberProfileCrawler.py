import urllib.request
import urllib
import re
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from random import randint


class MemberInfo:
    def __init__(self, _UserId, _Name, _TotalHelpfulVotes, _Since, _Location, _ThingsLove):
        self.UserId = _UserId
        self.TotalHelpfulVotes = _TotalHelpfulVotes
        self.Name = _Name
        self.Since = _Since
        self.Location = _Location
        self.ThingsLove = _ThingsLove


class MemberScore:
    def __init__(self, _UserId, _RD5, _RD4, _RD3, _RD2, _RD1, _Useful, _Funny, _Cool, _Friends, _Reviews, _Photos):
        self.UserId = _UserId
        self.RD5 = _RD5
        self.RD4 = _RD4
        self.RD3 = _RD3
        self.RD2 = _RD2
        self.RD1 = _RD1
        self.Useful = _Useful
        self.Funny = _Funny
        self.Cool = _Cool
        self.Friends = _Friends
        self.Reviews = _Reviews
        self.Photos = _Photos


def run_program(list):

    for index in list:
        sleep(randint(2, 5))
        UserId = index[0]
        print('[' + UserId + ']')

        req = urllib.request.urlopen(url + UserId)
        content = req.read().decode(req.info().get_content_charset()).replace("\n", "")
        soup = BeautifulSoup(content, "html.parser")

        RatingDistribution = soup.select('.histogram_count')
        if len(RatingDistribution) == 0:
            RD5 = '-1'
            RD4 = '-1'
            RD3 = '-1'
            RD2 = '-1'
            RD1 = '-1'

        else:
            RD5 = RatingDistribution[0].text
            RD4 = RatingDistribution[1].text
            RD3 = RatingDistribution[2].text
            RD2 = RatingDistribution[3].text
            RD1 = RatingDistribution[4].text

        ReviewVote = soup.select('.ysection > ul[class~=ylist--condensed] > li')

        Useful = -1
        Funny = -1
        Cool = -1

        if len(ReviewVote) != 0:
            for temp in ReviewVote:
                if 'Useful' in temp.text:
                    Useful = int(re.sub('\s+', ' ', temp.text).replace('Useful', ''))
                elif 'Funny' in temp.text:
                    Funny = int(re.sub('\s+', ' ', temp.text).replace('Funny', ''))
                elif 'Cool' in temp.text:
                    Cool = int(re.sub('\s+', ' ', temp.text).replace('Cool', ''))

        Profile = soup.select('ul[class=ylist] > li')
        try:
            Location = Profile[1].text.replace('Location', '').strip()
        except:
            Location = '-1'
        try:
            Since = datetime.strptime(Profile[2].text.replace('Yelping Since', '').strip(), "%B %Y").date()
        except:
            Since = '-1'
        try:
            ThingsLove = Profile[3].text.replace('Things I Love', '').strip()
        except:
            ThingsLove = '-1'

        UserName = soup.select('div[class~=user-profile_info] > h1')[0].text
        UserTemp = soup.select('div[class~=user-profile_info] > .clearfix > ul[class=user-passport-stats] > li')

        Friends = int(re.sub('\s+', ' ', UserTemp[0].text).replace('Friends', '').replace('Friend', ''))
        Reviews = int(re.sub('\s+', ' ', UserTemp[1].text).replace('Reviews', '').replace('Review', ''))
        Photos = int(re.sub('\s+', ' ', UserTemp[2].text).replace('Photos', '').replace('Photo', ''))

        MemberInfoList.append(MemberInfo(UserId, UserName, str(Useful), str(Since), Location, ThingsLove))
        MemberScoreList.append(
            MemberScore(UserId, RD5, RD4, RD3, RD2, RD1, Useful, Funny, Cool, Friends,
                        Reviews, Photos))
    return MemberInfoList, MemberScoreList


url = 'https://www.yelp.com/user_details?userid='
MemberInfoList = []
MemberScoreList = []
