# -*- coding: utf-8 -*-
from requests.compat import urljoin
import requests

from bs4 import BeautifulSoup


url = "http://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_key=40210%2C40232&panel_type=&search_optional_item=n"
res = requests.get(url)

    #print res.status_code
    #print res.content[:200]

    #requests.메서드(url, GET이면(params={}), POST이면(data={}))
soup = BeautifulSoup(res.content, "html.parser")
recruit_list = soup.select("#default_list_wrap > table > tbody > tr") #이 id다  -> 그 태그 아래에 table -> 그 안에 tr들 추출

for recruit in recruit_list:
    sector = recruit.select(".job_sector")[0].get_text().strip()
    if u"보안" not in sector:
        continue
    company = recruit.select("span")[1].get_text().strip()
    #print recruit.find_all('span')[1].get_text()
    print u"{:<40} {:<20}".format(company, sector)
    
     




