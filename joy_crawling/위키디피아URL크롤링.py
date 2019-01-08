#-*- coding: utf-8 -*-
'''
*단일 페이지 내의 이동과 여러 페이지
*여러 사이트를 이동하는 부분을 다뤄보자
url은 위키 피디아(이 사이트는 하나의 페이지에 관련된 여러 링크가 존재)
'''
import re, requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Kevin_Bacon").text, "html.parser")

#for link in soup.findAll("a"): #a태그 전부가져오기
    #a태그전부 가져오는데, (조건 : href속성이 있는)
    #if 'href' in link.attrs: 
        #print(link)  

#찾고자하는조건(id가 bodyContent인 div안에 / URL에 세미콜론 포함X / URL은 '/wiki/'로 시작)
for link in soup.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs: 
        print(link.attrs['href'])  
'''
########### README.md #####################################################
전체 사이트 크롤링 - 위키 피디아 전체 사이트의 데이터 수집
역시 가장 먼저 해야할일은 사이트의 페이지 몇 개를 살펴보며 패턴을 찾는 일입니다. 위키 백과의 사이트는 아래와 같은 패턴이 있음을 확인할 수 있었습니다 (아래에서 '#' 뒤에는 'id'를 의미합니다)

제목은 항상 h1 태그 안에 있으며, 페이지당 하나만 존재합니다.
바디 텍스트는 div#bodyContent 태그에 들어 있습니다.
첫 번째 문단의 택스트만 선택하려면 div#mw-content-text->p만 선택합니다
편집 링크는 항목 페이지에만 존재합니다. 존재한다면 li#ca-edit -> span -> a로 찾을 수 있습니다.
############## SOURCE CODE ##################################################
pages = set() # 애초에 set은 중복을 허용하지 않음
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    soup = BeautifulSoup(html, "html.parser")

    try:
        print("Title : " + soup.h1.get_text())
        print("First paragraph : " + soup.find(id='mw-content-text').findAll('p')[0].get_text())
        print("Edit page link : " + soup.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("This page is mission something!")


    for link in soup.findAll("a", href = re.compile("^(/wiki)")):
        if 'href' in link.attrs: # 위에서 찾은 link에 href 속성이 있는지 확인
            if link.attrs['href'] not in pages: # 새로운 페이지인지 확인
                newPage = link.attrs['href']
                print("--\nNew Page : "  + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")
'''
#참고 : https://jungwoon.github.io/python/crawling/2018/04/12/Crawling-2/