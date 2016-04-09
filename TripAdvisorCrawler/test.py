import urllib.request
import re
from bs4 import BeautifulSoup


url='https://www.tripadvisor.com/ExpandedUserReviews-g45963-d91844?target=360847363&context=1&reviews=360847363'


req = urllib.request.urlopen(url)
content = req.read().decode(req.info().get_content_charset())
soup = BeautifulSoup(content,"html.parser")

temp = soup.select('.reviewItemInline > span > img')[0]['alt']

print('123')