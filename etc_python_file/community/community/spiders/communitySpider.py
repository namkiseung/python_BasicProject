# -*- coding: utf-8 -*-
#__author__ = 'onecue'
import scrapy

class CommunitySpider(scrapy.Spider):  #CommunitySpider클래스는 scrapy.Spider를 상속하게끔
	name = "communityCrawler"  #스파이더의 이름을 정의

	#start_urls = [] #클롤링할 사이트 주소들
	def start_requests(self):
		