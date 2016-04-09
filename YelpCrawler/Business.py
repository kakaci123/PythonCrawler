import Function


class BusinessElemet:
    def __init__(self, _RestaurantId, _Rating, _CategoriesCnt, _CategoriesText, _ReviewCount):
        self.RestaurantId = _RestaurantId
        self.Rating = _Rating
        self.CategoriesCnt = _CategoriesCnt
        self.CategoriesText = _CategoriesText
        self.ReviewCount = _ReviewCount


def run_program(list):
    rlt = []
    client = Function.GetAuthAndClient()
    for rName in list:
        print('[' + rName[0] + ']')
        CategoriesText = ''
        response = client.get_business(rName[0]).business
        Rating = response.rating
        for temp in response.categories:
            CategoriesText = CategoriesText + temp.name + ';'
        CategoriesCnt = len(response.categories)
        ReviewCount = response.review_count
        rlt.append(BusinessElemet(rName[0], Rating, CategoriesCnt, CategoriesText, ReviewCount))
    return rlt
