import HotelInfoCrawler  # step 1
import HotelReviewCrawler  # step 2
import MemberProfileCrawler  # step 3
import Function
import re


# Step 1
# =================================================================================================================================================================
def Start_HotelInfoCrawler(list):
    HotelInfoList = HotelInfoCrawler.run_program(list)

    # Insert to Database
    for index in HotelInfoList:
        _HotelId = index.Id.replace(',', '')
        _hRank = int(index.hRank.replace(',', ''))
        _hRating = float(index.hRating.replace(',', ''))
        _hStarClass = float(index.hStarClass.replace(',', ''))
        _hRoomNum = int(index.hRoomNum.replace(',', ''))
        _hReviewNum = int(index.hReviewNum.replace(',', ''))

        print(':::Starting Insert to HotelMain:::')
        try:
            cursor.execute(
                "INSERT INTO HotelMain(HotelId, hRank,hRating,hStarClass,hRoomNum,hReviewNum,TimeStamp) values ('" + str(
                    _HotelId) + "', '" + str(_hRank) + "','" + str(_hRating) + "','" + str(
                    _hStarClass) + "','" + str(_hRoomNum) + "','" + str(
                    _hReviewNum) + "','" + SystemTime + "')")
            cursor.commit()
            print(':::Insert to database successfully:::')
        except:
            print(':::Insert failed, please check!')

        '''
        cursor.execute("SELECT * FROM HotelMain WHERE HotelId='" + index.Id + "' order by TimeStamp")
        CheckQuery = cursor.fetchall()
        if len(CheckQuery) != 0:
            CheckTemp = CheckQuery[len(CheckQuery) - 1]
            if CheckTemp[1] == _HotelId and CheckTemp[2] == _hRank and CheckTemp[3] == _hRating and CheckTemp[
                4] == _hStarClass and CheckTemp[5] == _hRoomNum and CheckTemp[6] == _hReviewNum:
                print('main same')
            else:
                print(':::Starting Insert to Database:::')
                try:
                    cursor.execute(
                        "INSERT INTO HotelMain(HotelId, hRank,hRating,hStarClass,hRoomNum,hReviewNum,TimeStamp) values ('" + str(
                            _HotelId) + "', '" + str(_hRank) + "','" + str(_hRating) + "','" + str(
                            _hStarClass) + "','" + str(_hRoomNum) + "','" + str(
                            _hReviewNum) + "','" + SystemTime + "')")
                    cursor.commit()
                    print(':::Insert to database successfully:::')
                except:
                    print(':::Insert failed, please check!')
        else:
            print(':::Starting Insert to Database:::')
            try:
                cursor.execute(
                    "INSERT INTO HotelMain(HotelId, hRank,hRating,hStarClass,hRoomNum,hReviewNum,TimeStamp) values ('" + str(
                        _HotelId) + "', '" + str(_hRank) + "','" + str(_hRating) + "','" + str(
                        _hStarClass) + "','" + str(
                        _hRoomNum) + "','" + str(_hReviewNum) + "','" + SystemTime + "')")
                cursor.commit()
                print(':::Insert to database successfully:::')
            except:
                print(':::Insert failed, please check!')
        '''

        _excellent = int(index.excellent.replace(',', ''))
        _verygood = int(index.verygood.replace(',', ''))
        _average = int(index.average.replace(',', ''))
        _poor = int(index.poor.replace(',', ''))
        _terrible = int(index.terrible.replace(',', ''))
        _hFamilies = int(index.hFamilies.replace(',', ''))
        _hCouples = int(index.hCouples.replace(',', ''))
        _hSolo = int(index.hSolo.replace(',', ''))
        _hBusiness = int(index.hBusiness.replace(',', ''))
        _hFrineds = int(index.hFrineds.replace(',', ''))
        _hMarMay = int(index.hMarMay.replace(',', ''))
        _hJunAug = int(index.hJunAug.replace(',', ''))
        _hSepNov = int(index.hSepNov.replace(',', ''))
        _hDecFeb = int(index.hDecFeb.replace(',', ''))

        print(':::Starting Insert to HotelDetail:::')
        try:
            cursor.execute(
                "INSERT INTO HotelDetail(HotelId,excellent,verygood,average,poor,terrible,hFamilies,hCouples,hSolo,hBusiness,hFrineds,hMarMay,hJunAug,hSepNov,hDecFeb,TimeStamp) values ('" + _HotelId + "', '" + str(
                    _excellent) + "','" + str(_verygood) + "','" + str(_average) + "','" + str(_poor) + "','" + str(
                    _terrible) + "','" + str(_hFamilies) + "','" + str(_hCouples) + "','" + str(
                    _hSolo) + "','" + str(
                    _hBusiness) + "','" + str(_hFrineds) + "','" + str(_hMarMay) + "','" + str(
                    _hJunAug) + "','" + str(
                    _hSepNov) + "','" + str(_hDecFeb) + "','" + SystemTime + "')")
            cursor.commit()
            print(':::Insert to database successfully:::')
        except:
            print(':::Insert failed, please check!')
        '''
        cursor.execute("SELECT * FROM HotelDetail WHERE HotelId='" + index.Id + "' order by TimeStamp")
        CheckQuery = cursor.fetchall()

        if len(CheckQuery) != 0:
            CheckTemp = CheckQuery[len(CheckQuery) - 1]
            if (CheckTemp[2] == _excellent and CheckTemp[3] == _verygood and
                        CheckTemp[4] == _average and CheckTemp[5] == _poor and CheckTemp[6] == _terrible and CheckTemp[
                7] == _hFamilies and
                        CheckTemp[8] == _hCouples and CheckTemp[9] == _hSolo and
                        CheckTemp[10] == _hBusiness and CheckTemp[11] == _hFrineds and
                        CheckTemp[12] == _hMarMay and CheckTemp[13] == _hJunAug and
                        CheckTemp[14] == _hSepNov and CheckTemp[15] == _hDecFeb):
                print('detail same')
            else:
                print(':::Starting Insert to Database:::')
                try:
                    cursor.execute(
                        "INSERT INTO HotelDetail(HotelId,excellent,verygood,average,poor,terrible,hFamilies,hCouples,hSolo,hBusiness,hFrineds,hMarMay,hJunAug,hSepNov,hDecFeb,TimeStamp) values ('" + _HotelId + "', '" + str(
                            _excellent) + "','" + str(_verygood) + "','" + str(_average) + "','" + str(
                            _poor) + "','" + str(
                            _terrible) + "','" + str(_hFamilies) + "','" + str(_hCouples) + "','" + str(
                            _hSolo) + "','" + str(_hBusiness) + "','" + str(_hFrineds) + "','" + str(
                            _hMarMay) + "','" + str(_hJunAug) + "','" + str(_hSepNov) + "','" + str(
                            _hDecFeb) + "','" + SystemTime + "')")
                    cursor.commit()
                    print(':::Insert to database successfully:::')
                except:
                    print(':::Insert failed, please check!')
        else:
            print(':::Starting Insert to Database:::')
            try:
                cursor.execute(
                    "INSERT INTO HotelDetail(HotelId,excellent,verygood,average,poor,terrible,hFamilies,hCouples,hSolo,hBusiness,hFrineds,hMarMay,hJunAug,hSepNov,hDecFeb,TimeStamp) values ('" + _HotelId + "', '" + str(
                        _excellent) + "','" + str(_verygood) + "','" + str(_average) + "','" + str(_poor) + "','" + str(
                        _terrible) + "','" + str(_hFamilies) + "','" + str(_hCouples) + "','" + str(
                        _hSolo) + "','" + str(
                        _hBusiness) + "','" + str(_hFrineds) + "','" + str(_hMarMay) + "','" + str(
                        _hJunAug) + "','" + str(
                        _hSepNov) + "','" + str(_hDecFeb) + "','" + SystemTime + "')")
                cursor.commit()
                print(':::Insert to database successfully:::')
            except:
                print(':::Insert failed, please check!')
        '''

    HotelInfoList.clear()
    # =================================================================================================================================================================


# Step 2
# =================================================================================================================================================================
def Start_HotelReviewCrawler(list):
    for index, i in enumerate(list):

        _HotelId = i[2]
        _HotelUrl = i[4]

        print('The hotel = ' + i[3])
        print('The url = ' + _HotelUrl)
        '''
        _YesterdayReviewNum = []
        _TodayReviewNum = []

        cursor.execute(
            "SELECT hReviewNum FROM HotelMain WHERE HotelId='" + _HotelId + "' AND TimeStamp='" + Yesterday + "'")
        CheckQuery = cursor.fetchall()
        if len(CheckQuery) != 0:
            _YesterdayReviewNum = CheckQuery[0]

        cursor.execute(
            "SELECT hReviewNum FROM HotelMain WHERE HotelId='" + _HotelId + "' AND TimeStamp='" + SystemTime + "'")
        CheckQuery = cursor.fetchall()
        if len(CheckQuery) != 0:
            _TodayReviewNum = CheckQuery[0]

        if len(_YesterdayReviewNum) != 0:
            DeltaReviewNum = _TodayReviewNum[0] - _YesterdayReviewNum[0]
        else:
            DeltaReviewNum = _TodayReviewNum[0]
        print(DeltaReviewNum)
        '''
        DeltaReviewNum = -1

        TempList = HotelReviewCrawler.run_program(_HotelUrl, _HotelId, AreaId, SystemTime, DeltaReviewNum)

        ReviewList = TempList[0]
        ContentList = TempList[1]
        # Insert to Database
        '''
        cursor.execute(
            "SELECT * FROM ReviewOverview WHERE HotelId='" + _HotelId + "' AND TimeStamp='" + Yesterday + "'")
        CheckQuery = cursor.fetchall()
        if len(CheckQuery) != 0:
            for indexYesterday in CheckQuery:
                _ReviewIdYes = indexYesterday[2]
                _UserIdYes = indexYesterday[3]
                _AtPageYes = str(indexYesterday[4])
                _OrderOfPageYes = str(indexYesterday[5])
                _ReviewDateYes = indexYesterday[6]
                countTemp = int(_OrderOfPageYes) + DeltaReviewNum

                if countTemp > 10:
                    _AtPageYes = str(int(_AtPageYes) + int(countTemp / 10))
                    if countTemp % 10 == 0:
                        _AtPageYes = str(int(_AtPageYes) - 1)
                        _OrderOfPageYes = '10'
                    else:
                        _OrderOfPageYes = str(countTemp % 10)
                else:
                    _OrderOfPageYes = str(countTemp)
                cursor.execute(
                    "INSERT INTO ReviewOverview(HotelId, ReviewId,UserId,AtPage,OrderNumOfPage,ReviewDate,TimeStamp) values ('" + _HotelId + "', '" + _ReviewIdYes + "','" + _UserIdYes + "','" + _AtPageYes + "','" + _OrderOfPageYes + "','" + _ReviewDateYes + "','" + SystemTime + "')")
                cursor.commit()

        cursor.execute(
            "SELECT * FROM ReviewScore WHERE HotelId='" + _HotelId + "' AND TimeStamp='" + Yesterday + "'")
        CheckQuery = cursor.fetchall()
        if len(CheckQuery) != 0:
            for indexYesterday in CheckQuery:
                _ReviewId = indexYesterday[2]
                _ReviewRatingYes = str(indexYesterday[3])
                _ReviewHelpfulvotesYes = str(indexYesterday[4])
                cursor.execute(
                    "INSERT INTO ReviewScore(HotelId,ReviewId, ReviewRating,ReviewHelpfulvotes,TimeStamp) values ('" + _HotelId + "', '" + _ReviewId + "', '" + _ReviewRatingYes + "','" + _ReviewHelpfulvotesYes + "','" + SystemTime + "')")
                cursor.commit()
        '''
        if len(ReviewList) != 0 and len(ContentList) != 0:
            print(':::Starting Insert to Database:::')

            for index in ReviewList:
                _ReviewId = index.ReviewId
                _UserId = index.UserId
                _AtPage = index.AtPage
                _OrderOfPage = str(index.OrderOfPage)
                _ReviewDate = index.ReviewDate

                cursor.execute(
                    "INSERT INTO ReviewOverview(HotelId, ReviewId,UserId,AtPage,OrderNumOfPage,ReviewDate,TimeStamp) values ('" + _HotelId + "','" + _ReviewId + "','" + _UserId + "','" + _AtPage + "','" + _OrderOfPage + "','" + _ReviewDate + "','" + SystemTime + "')")
                cursor.commit()

            for index in ContentList:
                _ReviewRating = index.ReviewRating.replace(',', '')
                _ReviewHelpfulvotes = index.ReviewHelpfulvotes.replace(',', '')

                cursor.execute(
                    "INSERT INTO ReviewScore(HotelId,ReviewId, ReviewRating,ReviewHelpfulvotes,TimeStamp) values ('" + _HotelId + "','" + _ReviewId + "','" + _ReviewRating + "','" + _ReviewHelpfulvotes + "','" + SystemTime + "')")
                cursor.commit()

                _ReviewId = index.ReviewId
                _ReviewTitle = index.ReviewTitle.replace(',', '@[CMA]').replace("'", "''")
                _ReviewContent = index.ReviewContent.replace(',', '@[CMA]').replace("'", "''")
                _Partial = index.Partial.replace(',', '@[CMA]').replace("'", "''").strip()

                emoji_pattern = re.compile("["
                                           u"\U0001F600-\U0001F64F"  # emoticons
                                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                           "]+", flags=re.UNICODE)
                _ReviewContent = emoji_pattern.sub(r'', _ReviewContent)
                _Partial = emoji_pattern.sub(r'', _Partial)

                cursor.execute(
                    "SELECT * FROM ReviewDetail WHERE ReviewId='" + _ReviewId + "' AND ReviewTitle='" + _ReviewTitle + "' AND ReviewContent='" + _ReviewContent + "' AND ParitalContent='" + _Partial + "'")
                CheckQuery = cursor.fetchall()

                if len(CheckQuery) == 0 or CheckQuery is None:
                    cursor.execute(
                        "INSERT INTO ReviewDetail(ReviewId, ReviewTitle,ParitalContent,ReviewContent,TimeStamp) values ('" + _ReviewId + "', '" + _ReviewTitle + "','" + _Partial + "','" + _ReviewContent + "','" + SystemTime + "')")
                    cursor.commit()

            print(':::Insert Process is finished:::')


# =================================================================================================================================================================

# step 3
# =================================================================================================================================================================

def Start_MemberProfileCrawler():
    # UserId='7EC2CD53AB6787D4C94E08F185E05483'
    # ReviewId='327918536'
    cursor.execute(
        "SELECT UserId,ReviewId FROM ReviewOverview WHERE TimeStamp='" + SystemTime + "'")
    QueryArray = cursor.fetchall()
    MemberProfileCrawler.run_program(QueryArray, SystemTime)


# *****************Main Program****************

SystemTime = Function.GetTimeStamp()
Yesterday = Function.GetYesterdayTimeStamp()

try:
    cursor = Function.DatabaseConnectionBuilder()
    print('[=Notification=] Database connection is built')
except:
    print('[=Notification=] Database connection occurs exception')
    SystemExit(0)

# Step 1 (Get Hotel List From Current Area)

NY = 'http://www.tripadvisor.com/Hotels-g60763-New_York_City_New_York-Hotels.html'  # no.1
LV = 'http://www.tripadvisor.com/Hotels-g45963-Las_Vegas_Nevada-Hotels.html'  # no.2
OF = 'http://www.tripadvisor.com/Hotels-g34515-Orlando_Florida-Hotels.html'  # no.3
CI = 'http://www.tripadvisor.com/Hotels-g35805-Chicago_Illinois-Hotels.html'  # no.4
SF = 'https://www.tripadvisor.com/Hotels-g60713-San_Francisco_California-Hotels.html'  # no.5
#
CityArray = [('New York City, New York', NY), ('Las Vagas, Nevada', LV), ('Orlando, Florida', OF),
             ('Chicago, Illinois', CI), ('San Francisco, California', SF)]

for CityElement in CityArray:
    # [Query Result]row=(1, 'New York', '60763')
    cursor.execute("SELECT * FROM AreaList WHERE AreaName='" + CityElement[0] + "'")

    row = cursor.fetchone()
    AreaId = str(row[0])
    CityName = CityElement[0]
    CityUrl = CityElement[1]

    print("[=Notification=] Now is [" + CityName + "] running")

    cursor.execute("SELECT * FROM HotelList WHERE AreaId='" + AreaId + "'")
    HotelList = cursor.fetchall()

    print('[=Notification=] HotelInfoCrawler is Start')
    Start_HotelInfoCrawler(HotelList)
    print('[=Notification=] HotelInfoCrawler is finished')

    print('[=Notification=] HotelReviewCrawler is Start')
    Start_HotelReviewCrawler(HotelList)
    print('[=Notification=] HotelReviewCrawler is finished')

print('[=Notification=] MemberProfileCrawler is Start')
Start_MemberProfileCrawler()
print('[=Notification=] MemberProfileCrawler is finished')

cursor.close()
print('===Connection is closed===')
