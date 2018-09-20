# -*- coding: utf-8 -*-


""" 정수 두개를 가진 튜플들을 가진 리스트를 전달받아,
두 수의 차가 가장 작은 튜플을 반환하는 함수 get_min를 작성하자
    
    sample in/out:
        get_min([(1,2), (3,5), (100, 10)]) -> (1, 2)
        get_min([(1,10), (3,5), (100, 10)]) -> (3, 5)
"""
def get_min(li):
    x = abs(li[0][0]-li[0][1])       
    res=0
    for i in range(1, len(li)):                
        if abs(li[i][0]-li[i][1]) <= x:
            x = abs(li[i][0]-li[i][1])
            res = i        
    return li[res]

if __name__ == "__main__":
    print(get_min([(1,2), (3,5), (100, 10)]))# -> (1, 2)
    print(get_min([(1,10), (3,5), (100, 10)]))# -> (3, 5)
    pass

