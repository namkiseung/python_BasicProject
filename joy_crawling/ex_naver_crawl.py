import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%9D%BC%EC%A3%BC%EC%9D%BC%EB%82%A0%EC%94%A8&oquery=%EC%A3%BC%EA%B0%84+%EC%98%88%EB%B3%B4&tqi=UuDaalpySEKssvfyyiNsssssttZ-233515&acq=%EC%9D%BC%EC%A3%BC%EC%9D%BC%EB%82%A0&acr=1&qdt=0"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

result="" #결과값 변수
for x in soup.select("div > div > div > div > div > ul > li > dl > dd > span")[33:65]:
   result+=x.text
print(result)
    