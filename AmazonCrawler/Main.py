from amazon.api import AmazonAPI

amazon = AmazonAPI('AKIAJHZQBNLMX725DQFA', '90iFRqaxfgfmwLtKY3xZy7VgVJDHWItTSjYa2PwV', 'hansel.hu-20')
#product = amazon.lookup(ItemId='B0051QVF7A')
products = amazon.search(Keywords='kindle', SearchIndex='All')
for i, product in enumerate(products):
    print "{0}. '{1}'".format(i, product.reviews[1])