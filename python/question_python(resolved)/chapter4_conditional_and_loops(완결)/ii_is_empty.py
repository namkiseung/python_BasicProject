# -*- coding: utf-8 -*-


def is_empty(input_list):
    """ 사전들이 담긴 리스트를 전달받아서, 모든 사전이 비어있는지 검사하고, 비어있으면 True를, 아니면 False를 반환하는 함수를 작성하자

    sample in/out:
        is_empty([{},{},{}]) -> True
        is_empty([{1,2},{},{}]) -> False
    """
    # 여기 작성    
    #리스트의 인덱스 안에 값이 비어있나? true or False
        #(리스트는 사전으로 이루어짐)
        #리스트 인덱스 0번에 dict이 있는지 비교하는 방법?  -> 리스트에 지원하는 함수가 없음
        #그렇다면 다른 방법으로 0번에 
    c='no data'          
    for x in range(len(input_list)):
        #print 'x ?',x
        if not input_list[x]:                                    
            c = 'true'    
            continue             
        else:
            c = 'false'              
            break     
    return c    

if __name__ == "__main__":
    sample=[{},{},{}]
    sample2=[{1,2},{},{}]
    sample3=[{},{},{},{},{},{},1]
    sample4=[1,2,3,4,5,6,7,8]
    sample5=[{},{},{},{},{},{},{},{},{},{},{},{'a':1}]
    sample6=[{},{},{},{},{},{},{},{},{},{},{},{}]
    sample7=[]
    print is_empty(sample)
    print is_empty(sample2)
    print is_empty(sample3)
    print is_empty(sample4)
    print is_empty(sample5)
    print is_empty(sample6)
    pass

