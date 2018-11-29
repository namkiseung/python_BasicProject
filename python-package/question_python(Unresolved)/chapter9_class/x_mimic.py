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
import time
from bs4 import BeautifulSoup


# 구글클래스 원 문제는 함수로 작성하는 건데, 우린 클래스로 해봅시다
class Mimic(object):
  m_dict = {}
  
  def mimic_dict(self, url):
    """입력된 url의 텍스트 영역을 읽어 단어를 추출하고 멤버변수인 m_dict에 저장한다"""
    # +++your code here+++        
    bin_list = url.split() #빈 리스트 생성 "최종 딕셔너리의 값에 리스트형태로 넣기위해서"
    self.m_dict={} #빈 딕셔너리 생성 "지금 생성한 딕셔너리를 리턴할것이기 때문"
    #빈 딕셔너리의 처음 '키'는 공백
    #[약속] 나열된 단어가 있을때,
   
    local_binlist=[]
    bin_word=' '       #비어있는 단어를 만들자
    for i in bin_list:            
      if bin_word in self.m_dict.keys():      
        self.m_dict[bin_word].append(i)        
      else:
        self.m_dict[bin_word] = [i]
      bin_word = i #(bin) 단어에다가 한번 사용한 i 단어를 넣어주어 업데이트 하고, 이 단어는 이제 값이 될것이다.             
    
    #중복되는 키가 존재할때, 
    #if 새로추가하려는키 in 딕트의 키:
      #dict[새로추가하려는키].append(새로추가하려는키)
    
    return self.m_dict

  def print_mimic(self, word):
    """입력된 word로 문장을 시작하고 이어지는 단어를 랜덤하게 선택해가면서 word를 출력하자. 
    word 200개를 출력하고 종료한다
    적절한 예외 처리를 통해 에러에 대비하자.

    "mimic" dict를 이용하면, 랜덤한 문자열을 쉽게 생성할 수 있습니다
    첫 단어를 print 한 뒤 다음으로 올수 있는 word를 dict에서 찾고, 
    random하게 골라서 print 합니다. 그 다음도 마찬가지 입니다.
    빈 문자열을 첫번째 단어로 사용합시다. 그리고 문장을 이어가다가 
    다음 단어가 없는 문자열을 만나면, 다시 공백문자열로 돌아갑시다.

    note: 파이썬 표준 모듈인 random.choice(list) 는 리스트에서 임의의
    요소를 선택합니다

    최대 70문자를 출력하고 줄바꿈을 해주면 보기가 좋아집니다
    200개를 출력한다.
    그 위에서 dict를 만들었다
    처음 빈 문자열의 벨류가 this다.
    """
    
    # +++your code here+++    
    for i in range(200):
      #dict의 키하나 준다.
      #나온 벨류를 다시 다음 키값으로 넣자            
      single_word=self.m_dict.keys()
      words = random.choice(single_word)      
      #print words,           
    return ""
  

if __name__ == '__main__':
  #start_url = 'https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC'
  #res = requests.get(start_url)
  with open("tmp.txt", "r") as f:
      con=f.read() 
  #res.status_code 이것이 웹 응답 확인방법  
  #m.mimic_dict(res.split(' '))
  m = Mimic()
  print m.print_mimic(con)
  #print m.mimic_dict(con)  

