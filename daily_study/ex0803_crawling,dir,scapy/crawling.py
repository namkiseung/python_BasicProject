# -*- coding: utf-8 -*-
from requests.compat import urljoin
import requests

from bs4 import BeautifulSoup

url = "https://www.boannews.com/search/news_list.asp"
res = requests.get(url)

#print res.status_code
#print res.content[:200]
#requests.메서드(url, GET이면(params={}), POST이면(data={}))
soup = BeautifulSoup(res.content, "html.parser")
#print soup
news_list = soup.find_all("div", attrs={"class":"news_list"})

dict_tmp={}
for news in news_list:
    title = news.find("span").get_text()
    link = urljoin(url, news.find('a').get('href'))
    writer_name = news.find("span", attrs={"class":"news_writer"}).get_text()[:4]
    writer_time = news.find("span", attrs={"class":"news_writer"}).get_text()[9:]
    #a = news.select(".news_writer")[0].get_text().split(" | ")
    #Q.추출한 데이터를 dict자료형에 넣어보자
    
    #print title
    #print link
    dict_tmp[writer_name]=writer_time
    
for x,y in dict_tmp.items():
    print x,y+"\n"




