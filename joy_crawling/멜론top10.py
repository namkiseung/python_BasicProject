import re
import requests
from bs4 import BeautifulSoup
#2007년대 노래 시대별차트
#https://www.melon.com/chart/age/list.htm?idx=1&chartType=YE&chartGenre=POP&chartDate=2007&moved=Y
headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
 
age_url ="https://www.melon.com/chart/age/list.htm"
 
params = {
    'idx':'1',
    'chartType':'YE',    #10년 단위로 검색하는 부분과 연관, AG로 표현된다.
    'chartGenre':'KPOP', #시대별 차트에서 가요 -> POP으로 변경해서 나오는 곡들은 KPOP 대신 POP을 넣으면 나타난다.
    'chartDate':'2007',
    'moved':'Y',
}
response = requests.get(age_url, params=params, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')
 
#enumerate를 넣어서 각 tag의 index값을 같이 가져온다. 
#맨 뒤에 1을 사용한 건 1부터 시작하겠다는 뜻이다. 없으면 0부터 시작한다.
#a태그가 많이 있는데 그 중에서 href요소 내부 값에 playSong문자를 포함하는 a태그만 가져온다.
for i, tag in enumerate(soup.select('a[href*=playSong]'),1):
    title = tag.text    
    js = tag['href']
    #시대별차트는 TOP100 크롤링과는 달리 songId부분이 ''홑따움표로 이루어져있다.
    #따라서 정규표현식을 그에 맟줘서 수정해줘야 한다.
    matched = re.search(r",'(\d+)'",js)
    #print(matched.group(1))
    
    if matched:
        #group(1)으로 괄호친 부부만 가져온다. group(0)는 홑따움표 전체를 들고 온다.
        song_Id = matched.group(1)
        song_url = 'https://www.melon.com/song/detail.htm?songId=' + song_Id
        print(i,title, song_url)


