# -*- coding: utf-8 -*-



msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def tran(char, num):
    """ 문자열과, 정수를 전달받고, 문자열의 문자를 각각 num 만큼 shift시킨 문자열을 반환하는 함수를 작성하자.
          (만약, shift 결과가 알파벳 마지막(z)을 넘어가면 다시 a부터 시작한다)
        hint: 시져 암호, ord, chr

        sample in/out:
            tran("abc", 1) -> "bcd"
            tran("abc", 3) -> "def"
            tran("xyz", 2) -> "zab"
    """
    # 여기 작성
    #<시나리오>      a부터 z까지 (97번 ~ 122번)
        #.1 한글자씩 shift하기
            #1-1. 입력받은 char를  아스키 숫자로 구함
            #1-2. 아스키 숫자에 + num을 더한다
            #1-3. 다시 chr(num)으로 문자로 변환시킨다

        #print chr(ord(char[0])+num)
        #print chr(ord(char[1])+num)
        #print chr(ord(char[2])+num)
        
        #2. 여러글짜 shift 하기
            #2-1 글자 수만큼 반복하자
            #2-2 

        # ord('a')    ->    숫자로 나온다.
        # chr(100)      ->    문자로 나온다.
    n=''
    for x in range(len(char)):
        if ord(char[x])+num > 122:            
            n += chr(ord(char[x])-24)    # 바꿔야할 문자에 알파벳 문자를 초기화 할 수 있는 값을 빼는걸 <반복>
        else:
            n += chr(ord(char[x])+num)   #단어의 한 문자를 ASC로 바꾸고 +3(num) 해서  다시 chr로 문자로 변환하자
        
        #만약에 x가 122 초과다 그러면 x를 97로 

        #s = 'apple copyright'
        #예제1) n = s.translate({ ord('a'): '@', ord('c'): '©', ord('p'): '℗', ord('r'): '®' })
        #예제2) n = s.translate({ ord(x): y for (x, y) in zip(oldChars, newChars) })    
    return n

# 함수 작성이 끝나면, msg 변수의 내용을 해독해보자

if __name__ == "__main__":
    print tran("abc", 1) #-> "bcd"
    print tran("abc", 3) #-> "def"
    print tran("xyz", 2) #-> "zab"
    pass