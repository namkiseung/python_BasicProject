# -*- coding: utf-8 -*-
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise - Google's Python class

main 함수는 이미 아래쪽에 정의되어 있고, 
당신이 작성할 print_words 함수와 
print_top 함수를 호출하도록 되어 있습니다.
"""

import sys

# 여기 작성
# print_words(filename)과 print_top(filename) 함수를 작성하세요
# 파일을 열고, 단어를 세서 dict로 반환하는 헬퍼 함수를 정의해도 됩니다
# print_words 함수와 print_top 함수에서 헬퍼 함수를 호출하면 됩니다

###
'''
    1. --count 플래그가 설정되면, print_words(filename) 함수를 실행합니다. 
    이 함수는 파일을 읽고 각 단어가 몇번 사용됐는지 카운트하고 출력하는 함수입니다.

    예)
    and 5
    the 10
    ...
    단어 기준으로 정렬합니다(a가 먼저 나오도록) (구두점이 포함될텐데 그건 신경쓰지 맙시다).
    모든 단어는 소문자로 저장합시다. 예를 들어 The 와 the를 같이 카운트합니다.
    '''
def print_words(name_file):
  
  dic = {}
  with open(name_file, 'r') as f:
    data = f.read().split()      
    tmp = set(data)
  
  for x in tmp:       # 중복 제거된 리스트
    xx=x.lower()
    dic[xx.ljust(10)] = 0  

  for y in data:        #모든 리스트
    yy=y.lower()
    dic[yy.ljust(10)] = dic[yy.ljust(10)] + 1
  '''
  dic = {}

  for list_name in remove_overlap:
      dic[list_name] = 0

  for list_count in list_example:
      dic[list_count] = dic[list_count] + 1
  '''
  return dic
  
  '''
    2. --topcount 플래그가 설정되면, print_top(filename) 함수가 실행합니다. 이 함수는 
    print_words 함수와 비슷하지만, 가장 많은 count의 20 단어만 출력합니다(정렬 필요). 
    많이 등장한 단어 순으로 출력.

    Workflow: 코드를 한번에 완벽하게 작성하려고 하지 말고, 내가 의도한대로 코드가 동작하는지
    데이터를 화면에 출력하고, sys.exit() 함수를 이용해 프로그램을 종료합시다.
    제대로 동작한다면, 다음 코드를 작성합시다.

    Optional: print_words 함수와 print_top 함수가 중복되는 것을 막기 위해 
    헬퍼 함수를 만들어도 됩니다.
    '''
def print_top(name_file):
  return

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'    
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]

  if option == '--count':
    print_words(filename)

    
  elif option == '--topcount':
    print_top(filename)
    

  else:
    print 'unknown option: ' + option
    sys.exit(1)

def sort_func(x):
  return x[0]



if __name__ == '__main__':     
  print print_words("attachments/sample.txt") 
  #main()