# -*- coding: utf-8 -*-

from collections import Counter

def word_histogram(filename):
    """ 파일을 읽어 단어 수를 세고, 히스토그램을 문자열로 만들어 반환하는 함수를 작성하자
        (반환되는 문자열이 다음과 같은 형태로 출력되면 된다 
          (각 라인이 '\n'로 끝나야 함, 앞에 공백 개수는 신경쓰지 마세요))
        hint: from collections import Counter                

        example:
            the            :**********
            of             :*******
            German         :****
            Unity          :***
            Day            :***
            in             :**
            ...
    """
    a = ''
    b = ''
    with open(filename) as f:
        data = f.read().split()
        
    #for x in data:
    #    a += x+":"+str(len(x)*'*')+'\n'
    

    for x in Counter(data):        
        b += x.ljust(20)+" : " +str(len(x)*'*') + '\n'
    return b


if __name__ == "__main__":
    inf = "attachments\\sample.txt"
    print word_histogram(inf)