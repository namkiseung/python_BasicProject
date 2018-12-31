# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
#from flask import Flask, render_template
# app=Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/news")
# def hello():
#     boannews_url_lists = [url_action, url_origin]
#     hacknews_url_lists = [thehackernews_vuln, thehackernews_data_breach, thehackernews_cyber_attack, thehackernews_malware]
#     main_list=list()
#     for url_item in boannews_url_lists:
#         origin_obj=get_obj_parserd(url_item)
#         main_list.append(get_boannews(origin_obj))
    
#     for url_item in hacknews_url_lists:
#         origin_obj=get_obj_parserd(url_item)
#         print("")
#         #print("length : %d, article-title : %s"%(len(get_thehacknews(origin_obj)), url_item))
#         print("")
#         main_list.append(get_thehacknews(origin_obj))
#     return render_template("news.html", main_data = main_list)
'''
boannews : https://www.boannews.com/custom/news_rss.asp
rss_hacknews : https://feeds.feedburner.com/TheHackersNews
origin_hacknews : https://thehackernews.com/ 
'''
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
    
def get_thehacknews(obj):
    res_list = list()
    for x in obj.findAll('h2',{'class':'home-title'}):
        res_list.append("○ {}".format(x.text))
    return res_list

def get_feed_hacknews(obj):
    res_list = list()
    for x in obj.select(".timetitle"):
        print(x)
    pass

if __name__=="__main__":
    boannews_url_lists = [url_action, url_origin]
    hacknews_url_lists = [thehackernews_vuln, thehackernews_data_breach, thehackernews_cyber_attack, thehackernews_malware]
    for url_item in boannews_url_lists:
        origin_obj=get_obj_parserd(url_item)
        print(get_boannews(origin_obj))
    
    for url_item in hacknews_url_lists:
        origin_obj=get_obj_parserd(url_item)
        print("")
        print("length : %d, article-title : %s"%(len(get_thehacknews(origin_obj)), url_item))
        print("")
        print(get_thehacknews(origin_obj))
    
    #res = get_obj_parserd(hacknew_feed)
    #print("")
    #print("length : %d, article-title : %s"%(len(get_feed_hacknews(res)), hacknew_feed))
    #print(res.findAll('li'))
    #print(get_feed_hacknews(res))

    #app.run(debug=True, host="0.0.0.0", port=3131)
    