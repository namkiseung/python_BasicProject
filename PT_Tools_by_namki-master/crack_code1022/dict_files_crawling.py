# -*- coding : utf-8 -*-
import requests, os
from bs4 import BeautifulSoup
url = "http://phenoelit.org/dpl/dpl.html"
get_page=requests.get(url)
bs=BeautifulSoup(get_page.text, "html.parser")
res = bs.select("body > center > table > tbody > tr > td")
for x in res:
    if res != "" or res != "(none)":
        print x.text

