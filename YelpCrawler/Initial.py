import Function


class RestaurantElement:
    def __init__(self, _AreaId, _RestaurantId, _RestaurantName, _RestaurantHref, _ReviewCnt):
        self.AreaId = _AreaId
        self.RestaurantId = _RestaurantId
        self.RestaurantName = _RestaurantName
        self.RestaurantHref = _RestaurantHref
        self.ReviewCnt = _ReviewCnt


params = {
    'term': 'Restaurants',
    'limit': 20,
    'offset': 0,
    'sort': 0,
}

CrawlerList = [
    {'name': 'New York, NY', 'areaid': 1},
    {'name': 'Las Vegas, VN', 'areaid': 2},
    {'name': 'Orlando, FL', 'areaid': 3},
    {'name': 'Chicago, IL', 'areaid': 6},
    {'name': 'San Francisco, CA', 'areaid': 9}]

client = Function.GetAuthAndClient()
cursor = Function.DatabaseConnectionBuilder()
CrawlerResult = []
SQLInsertList = []
print('[System]Intial Start')

for city in CrawlerList:
    print('[System]Now is ' + city['name'] + ' crawlering')
    for i in range(0, 49, 1):
        response = client.search(city['name'], **params)
        for index in response.businesses:
            if index.review_count > 500:
                CrawlerResult.append(
                    RestaurantElement(city['areaid'], index.id, index.name, index.url, index.review_count))

        params['offset'] = params['offset'] + 20

    RestaurantList = sorted(CrawlerResult, key=lambda RestaurantElement: RestaurantElement.ReviewCnt, reverse=True)
    for j in range(0, 10, 1):
        SQLInsertList.append(RestaurantList[j])

    params['offset'] = 0
    RestaurantList.clear()
    CrawlerResult.clear()

for index2 in SQLInsertList:
    _AreaId = str(index2.AreaId)
    _RestaurantId = index2.RestaurantId
    _RestaurantName = index2.RestaurantName.replace(',', '@[CMA]').replace("'", "''")
    _RestaurantHref = index2.RestaurantHref

    cursor.execute(
        "INSERT INTO RestaurantList(AreaId,RestaurantId,RestaurantName,RestaurantHref) values ('" + _AreaId + "','" + _RestaurantId + "','" + _RestaurantName + "','" + _RestaurantHref + "')")
    cursor.commit()

print('[System]Intial End')
