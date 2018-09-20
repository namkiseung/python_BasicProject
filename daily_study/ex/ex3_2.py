# -*- coding:cp949 -*-
"""
<반복할 횟수 정하고, 알파벳 입력할때마다 (아스키 숫자) 뽑기 게임>
1. 처음에 몇 개를 입력받을지 숫자를 받자
2. 입력받은 숫자를 roof_num 으로 정하자.
3. roof_num의 개수 만큼 반복해서 '문자'를 입력가능하다
4. 문자를 입력 받으면 value_list라는 곳에 차곡차곡 쌓아두자
5. roof_num의 번째까지 꽉찰 경우 가지고 있는 데이터를 모두 꺼내자
"""
roof_num = input('반복횟수 : ')
for a in range(roof_num):
    value_list = raw_input()
    print ord(value_list)

"""
def input_alpha(value):    
    print ord(value)

value=raw_input()
input_alpha(value)
"""




