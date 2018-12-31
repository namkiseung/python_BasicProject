import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
 
#중고나라 자체 url에서 Network에서 받아올 수 있는 기본 url로 바꾸어주었다.
list_url = 'https://m.cafe.naver.com/ArticleAllListAjax.nhn'
 
#인자들을 params로 받는다.
params = {
    'search.clubid' : '10050146',#중고나라id 
    'search.menuid' : '1768',    #가방/모자/장갑 게시판
    'search.boardtype' : 'L',    #여기서 boardtype(L), questionTab(A), totalCount(201)는 없어도 된다.
    'search.questionTab' : 'A',  #url을 가져올 때 몇가지를 없애보고 가능하다면 최소한으로 들고 오는게 좋다.
    'search.totalCount' : '201',
    'search.page' : 1,           #가방/모자/장갑 게시판 1페이지
}
 
 
html = requests.get(list_url, params = params).text
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
#soup를 확인해보면 li태그안에 각 상품의 내용이 있으므로, li태그를 각각 받는다.
 
for tag in soup.select('li'):
    article_url = urljoin(list_url,tag.find('a')['href']) #맨 처음에 있는 a항목을 가져온다.
    article_title = tag.find(class_='tit').text.strip()
    print(article_title, article_url)
 
    html2 = requests.get(article_url).text
    article_soup = BeautifulSoup(html2, 'html.parser')
 
    # 어떤 물품들을 로그인을 해야지 가격정보를 알려준다.
    # 가격이 없어 에러나는 부분은 None으로 처리했다.
    try:
        price = article_soup.select('.product_name .price')[0].text
    except IndexError:
        price = None
 
    print(price)

