from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=top_sly.hst&fbm=1&acr=6&ie=utf8&query=%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC+%EC%88%9C%EC%9C%84"
f = urlopen(url)

bs_obj = BeautifulSoup(f, "html.parser")

ol = bs_obj.find("ol", {"class":"thumb_list"})
ol2 = bs_obj.find("ol", {"start":"6"})

for i in ol.find_all("img"):
    print(i.get('alt'))

for i in ol2.find_all("img"):
    print(i.get('alt'))
