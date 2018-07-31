# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

명령행 인자에 명시된 파일을 읽고, split() 합시다. (공백으로 쪼개기)
line by line 으로 읽어서 쪼개려고 하지 말고, 전체를 한번에 읽고 쪼갭시다

"mimic"이란 dict를 만들고 단어들을 파일 안에서 단어의 직후에 따라오는 
모든 단어들로(리스트로 만들어야겠죠) 매핑합시다. 

  ex) {"and": ["then", "best", "then", "after", ...], ...}

' ' (공백) 문자열을 파일의 첫 번째 단어 앞에 오도록 합시다
  ex) The가 첫 시작이면 -> {" ": ["The"], ...}

"mimic" dict를 이용하면, 랜덤한 문자열을 쉽게 생성할 수 있습니다
첫 단어를 print 한 뒤 다음으로 올수 있는 word를 dict에서 찾고, 
random하게 골라서 print 합니다. 그 다음도 마찬가지 입니다.
빈 문자열을 첫번째 단어로 사용합시다. 그리고 문장을 이어가다가 
다음 단어가 없는 문자열을 만나면, 다시 공백문자열로 돌아갑시다.

note: 파이썬 표준 모듈인 random.choice(list) 는 리스트에서 임의의
요소를 선택합니다

최대 70문자를 출력하고 줄바꿈을 해주면 보기가 좋아집니다
"""

import random
import sys
import requests
from bs4 import BeautifulSoup


# 구글클래스 원 문제는 함수로 작성하는 건데, 우린 클래스로 해봅시다
class Mimic(object):
  m_dict = {}
  def mimic_dict(self, url):
    """입력된 url의 텍스트 영역을 읽어 단어를 추출하고 멤버변수인 m_dict에 저장한다"""
    # +++your code here+++
    for x in url.content:      
      self.m_dict = {}
    return

  def print_mimic(self, word):
    """입력된 word로 문장을 시작하고 이어지는 단어를 랜덤하게 선택해가면서 word를 출력하자. 
      word 200개를 출력하고 종료한다
      적절한 예외 처리를 통해 에러에 대비하자.
    """
    # +++your code here+++
    return


if __name__ == '__main__':
  start_url = 'https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC'
  res = requests.get(start_url)
  
  m = Mimic()
  m.mimic_dict(res.split(' '))

