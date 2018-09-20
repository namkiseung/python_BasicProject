# -*- coding: utf-8 -*-



""" 문자열을 입력받고,
사용된 word의 수를 카운트해
dict로 반환하는 함수 word_count를 작성하자

    sample in/out:
        word_count('the quick brown fox jumps over the lazy dog') 
            -> {'brown':1, 'lazy':1, 'over':1, 'fox':1, 'dog':1, 'quick':1, 'the':2, 'jumps':1}
        word_count('forensic data analysis (fda) is a branch of digital forensic') 
            -> {'a':1, 'of':1, 'is':1, 'forensic':2, 'analysis':1, 'branch':1, 'digital':1, 'data':1, '(fda)':1}
"""
def word_count(str_ba):
    tmp={}    
    cnt=0
    g=list()
    last=list()
    for x in str_ba.split():
        if x in tmp:            
            tmp[x]+=1
            g.append([x, tmp[x]])
        else:
            tmp[x]=1
            g.append([x, tmp[x]])
    
    
    for y in g:        
        tmp[y[0]]=y[1]        
    return tmp

if __name__ == "__main__":
    print(word_count('the quick brown fox jumps over the lazy dog'))
            #-> {'brown':1, 'lazy':1, 'over':1, 'fox':1, 'dog':1, 'quick':1, 'the':2, 'jumps':1}
    print(word_count('forensic data analysis (fda) is a branch of digital forensic')) 
            #-> {'a':1, 'of':1, 'is':1, 'forensic':2, 'analysis':1, 'branch':1, 'digital':1, 'data':1, '(fda)':1}
    pass

