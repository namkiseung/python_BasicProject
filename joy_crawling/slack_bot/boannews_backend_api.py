# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url_origin = "http://www.boannews.com/media/news_rss.xml"
url_action = "http://www.boannews.com/media/news_rss.xml?kind=1"
hacknew_feed = "https://feeds.feedburner.com/TheHackersNews"
thehackernews_vuln = "https://thehackernews.com/search/label/Vulnerability"
thehackernews_data_breach = "https://thehackernews.com/search/label/data%20breach"
thehackernews_cyber_attack = "https://thehackernews.com/search/label/Cyber%20Attack"
thehackernews_malware = "https://thehackernews.com/search/label/Malware"

def get_obj_parserd(url):
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
    res = requests.get(url, headers=request_headers)
    print(res.status_code)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup

def get_boannews(obj):
    res_list = list()
    for x in obj.findAll('title'):
        res_list.append("○ {}".format(x.text))
    return res_list

if __name__=="__main__":
    boannews_url_lists = [url_action, url_origin]
    for url_item in boannews_url_lists:
        origin_obj=get_obj_parserd(url_item)
        print(get_boannews(origin_obj))
