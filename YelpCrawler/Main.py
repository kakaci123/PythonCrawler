import Function
import Business
import ReviewContent
import MemberProfileCrawler
from random import randint
from time import sleep


def Start_RestaurantInfoCrawler(list):
    rlt = Business.run_program(list)
    for index in rlt:
        print(':::Starting Insert to Database:::')
        try:
            cursor.execute(
                "INSERT INTO RestaurantMain(RestaurantId, rRating,rCategoriesNum,rCategoriesText,rReviewNum,TimeStamp) values ('" + str(
                    index.RestaurantId) + "', '" + str(index.Rating) + "','" + str(
                    index.CategoriesCnt) + "','" + str(
                    index.CategoriesText) + "','" + str(
                    index.ReviewCount) + "','"
                + SystemTime + "')")
            cursor.commit()
            print(':::Insert to database successfully:::')
        except:
            print(':::Insert failed, please check!')

'''
Main Program
'''

SystemTime = Function.GetTimeStamp()
cursor = Function.DatabaseConnectionBuilder()

cursor.execute("SELECT RestaurantId,RestaurantHref FROM RestaurantList")
RestaurantList = cursor.fetchall()

print('[=Notification=] RestaurantInfoCrawler is Start')
Start_RestaurantInfoCrawler(RestaurantList)
print('[=Notification=] RestaurantInfoCrawler is finished')

print('[=Notification=] RestaurantReviewCrawler is Start')
for index in RestaurantList:

    sleep(randint(3, 8))
    TempRlt = ReviewContent.run_program(index, SystemTime)

    OverviewRlt = TempRlt[0]
    print('[System]Review Count=' + str(len(OverviewRlt)))
    for index in OverviewRlt:
        _RestaurantId = index.RestaurantId
        _ReviewId = index.ReviewId
        _UserId = index.UserId
        _AtPage = index.AtPage
        _OrderNumOfPage = index.OrderNumOfPage
        _ReviewDate = index.ReviewDate

        cursor.execute(
            "INSERT INTO ReviewOverview(RestaurantId, ReviewId, UserId, AtPage, OrderNumOfPage, ReviewDate,TimeStamp) values ('" + str(
                _RestaurantId) + "', '" + str(_ReviewId) + "','" + str(_UserId) + "','" + str(_AtPage) + "','" + str(
                _OrderNumOfPage) + "','" + str(_ReviewDate) + "','" + SystemTime + "')")
        cursor.commit()

    ScoreRlt = TempRlt[1]
    for index in ScoreRlt:
        _ReviewId = index.ReviewId
        _ReviewRating = index.ReviewRating
        _Useful = index.Useful
        _Funny = index.Funny
        _Cool = index.Cool

        cursor.execute(
            "INSERT INTO ReviewScore(ReviewId, ReviewRating, Useful, Funny, Cool,TimeStamp) values ('" + str(
                _ReviewId) + "', '" + str(_ReviewRating) + "','" + str(_Useful) + "','" + str(_Funny) + "','" + str(
                _Cool) + "','" + SystemTime + "')")
        cursor.commit()

    DetailRlt = TempRlt[2]
    for index in DetailRlt:
        _ReviewId = index.ReviewId
        _ReviewContent = index.ReviewContent
        _PhotoCnt = index.PhotoCnt
        if index.MorePhoto:
            _MorePhoto = '1'
        else:
            _MorePhoto = '0'

        cursor.execute(
            "INSERT INTO ReviewDetail(ReviewId, ReviewContent, PhotoCnt, MorePhoto,TimeStamp) values ('" + str(
                _ReviewId) + "', '" + str(_ReviewContent) + "','" + str(_PhotoCnt) + "','" + str(
                _MorePhoto) + "','" + SystemTime + "')")
        cursor.commit()
print('[=Notification=] RestaurantReviewCrawler is finished')

sleep(300)

print('[=Notification=] RestaurantReviewCrawler is Start')

cursor.execute("SELECT DISTINCT UserId FROM ReviewOverview")
UserIdList = cursor.fetchall()
TempRlt = MemberProfileCrawler.run_program(UserIdList)
RltInfoList = TempRlt[0]
RltScoreList = TempRlt[1]

if len(RltInfoList) == len(RltScoreList):
    for index in RltInfoList:
        _UserId = str(index.UserId)
        _TotalHelpfulVotes = str(index.TotalHelpfulVotes).replace(',', '@[CMA]').replace("'", "''").replace('"', '')
        _Name = str(index.Name).replace(',', '@[CMA]').replace("'", "''")
        _Since = str(index.Since).replace(',', '@[CMA]').replace("'", "''")
        _Location = str(index.Location).replace(',', '@[CMA]').replace("'", "''")
        _ThingsLove = str(index.ThingsLove).replace(',', '@[CMA]').replace("'", "''")

        cursor.execute(
            "SELECT * FROM MemberInfo WHERE UserId='" + _UserId + "' AND TotalHelpfulVote='" + _TotalHelpfulVotes + "' AND Name='" + _Name + "' AND Since='" + _Since + "' AND Location='" + _Location + "' AND ThingsLove='" + _ThingsLove + "'")
        CheckQuery = cursor.fetchall()

        if len(CheckQuery) == 0 or CheckQuery is None:
            cursor.execute(
                "INSERT INTO MemberInfo(UserId,TotalHelpfulVote,Name,Since,Location,ThingsLove,TimeStamp) values ('" +
                _UserId + "', '" + _TotalHelpfulVotes + "', '" + _Name + "','" + _Since + "','" + _Location + "','" + _ThingsLove + "','" + SystemTime + "')")
            cursor.commit()

    for index2 in RltScoreList:
        _UserId = index2.UserId
        _RD5 = str(index2.RD5)
        _RD4 = str(index2.RD4)
        _RD3 = str(index2.RD3)
        _RD2 = str(index2.RD2)
        _RD1 = str(index2.RD1)
        _Useful = str(index2.Useful)
        _Funny = str(index2.Funny)
        _Cool = str(index2.Cool)
        _Friends = str(index2.Friends)
        _Reviews = str(index2.Reviews)
        _Photos = str(index2.Photos)

        cursor.execute(
            "SELECT * FROM MemberScore WHERE UserId='" + _UserId + "' AND RD5='" + _RD5 + "' AND RD4='" + _RD4 + "' AND RD3='" + _RD3 + "' AND RD2='" + _RD2 + "' AND RD1='" + _RD1 + "' AND Useful='" + _Useful + "' AND Funny='" + _Funny + "' AND Cool='" + _Cool + "' AND Friends='" + _Friends + "' AND Reviews='" + _Reviews + "' AND Photos='" + _Photos + "'")
        CheckQuery = cursor.fetchall()

        if len(CheckQuery) == 0 or CheckQuery is None:
            cursor.execute(
                "INSERT INTO MemberScore(UserId,RD5,RD4,RD3,RD2,RD1,Useful,Funny,Cool,Friends,Reviews,Photos,TimeStamp) values ('" + _UserId + "', '" + _RD5 + "', '" + _RD4 + "','" + _RD3 + "','" + _RD2 + "','" + _RD1 + "', '" + _Useful + "','" + _Funny + "','" + _Cool + "','" + _Friends + "','" + _Reviews + "', '" + _Photos + "','" + SystemTime + "')")
            cursor.commit()

else:
    print('[System] Something wrong!')

print('[=Notification=] RestaurantReviewCrawler is finished')
