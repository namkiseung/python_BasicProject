# -*- coding: utf-8 -*-


""" 정수 두개를 가진 튜플들을 가진 리스트를 전달받아,
두 수의 차가 가장 작은 튜플을 반환하는 함수 get_min를 작성하자
    
    sample in/out:
        get_min([(1,2), (3,5), (100, 10)]) -> (1, 2)
        get_min([(1,10), (3,5), (100, 10)]) -> (3, 5)
"""
def get_min(tu):
##    tu[0][0] tu[0][1]
##    tu[1][0] tu[1][1]
##    tu[2][0] tu[2][1]
##    tu[3][0] tu[3][1]
##    tu[4][0] tu[4][1]
    #x=[]
    cnt=0
    tmp=tu[0][0]-tu[0][1]
    for i in tu:
        if i[cnt][0]-i[cnt][1] < tmp:
            #x.append(i)
            cnt+=1
        else:
            #tmp
    
    return ''#x

if __name__ == "__main__":
    print get_min([(1,2), (3,5), (100, 10)])# -> (1, 2)
    #print get_min([(1,10), (3,5), (100, 10)])# -> (3, 5)
    pass

