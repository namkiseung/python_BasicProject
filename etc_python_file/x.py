# -*- coding: cp949 -*-
# you can write to stdout for debugging purposes, e.g.
#print("this is a debug message")

def solution(S):
    # write your ce in Python 3.6
    V=int()
    V = S
    #print "입력값 %d " % V
    if not V < 0:
        count =0
        while True:
            count=count+1
            print "단계 : {}".format(count)            
            if not V % 2 == 0: #홀수
               V = V - 1               
               #print "홀 {}".format(V)
               if V == 0:
                   return V
            elif V % 2 == 0:#짝수
               V = V / 2
               #print "짝 {}".format(V)
               if V == 0:
                   return V
    else:
        pass
if __name__=="__main__":
    print solution(28)
