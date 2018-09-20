# -*- coding: utf-8 -*-

def fibonacci(end):
    """ 양의 정수 x를 입력받고, x 까지의 피보나치 수열을 list로 반환하는 함수를 작성하자
        Note : The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
               Every next number is found by adding up the two numbers before it.

        sample in/out:
            fibonacci(20) -> [0, 1, 1, 2, 3, 5, 8, 13]
            fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
    """
    #8+13=21
    # 여기 작성
    #end + end = double
    #<시나리오>
    # 1 경우 [0]
    # 2 경우 [0, 1]
    # 3 경우 [0, 1, 1, 2]
    # 4 경우 [0, 1, 1, 2, 3]
    # 5 경우 [0, 1, 1, 2, 3]
    # 6 경우 [0, 1, 1, 2, 3, 5]

    #tmp_list[0,1,2,3,4,5,6,7]

    # 리스트 0번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (0이 들어가야한다) 0 + 0  1보다 작거나 같으면 그대로
        #if sam_list[0] < end
        #    sam_list[0] = 0+0
    # 리스트 1번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (1이 들어가야한다) 0 + 1   1보다 작거나 같으면 그대로
        #if sam_list[1] < end
        #    sam_list[1] = 0+1
    # 리스트 2번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (1이 들어가야한다) 1 + 1   1보다 작거나 같으면 그대로
        #if sam_list[2] < end
        #    sam_list[2] = 1+1
    # 리스트 3번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (2이 들어가야한다) 1 + 2   1보다 작거나 같으면 그대로  
        #if sam_list[3] < end
        #    sam_list[3] = 1+2
    # 리스트 4번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (3이 들어가야한다) 2 + 3
        #if sam_list[4] < end
        #    sam_list[4] = 2+3
    # 리스트 5번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (5이 들어가야한다) 3 + 5
    # 리스트 6번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (8이 들어가야한다) 5 + 8
    # 리스트 7번째 들어갈 값은 -> (end보다 작아야한다) 그리고 (13이 들어가야한다) 8 + 13        

    #for문으로 1~end까지 담은 배열 생성
    tmp=list()
    for yyy in range(end):
        tmp.append(yyy)

    #[0, 1, 2, 3, 4, 5, 6, 7, 8]
    # tmp[0] = 0
    # tmp[1] = 1
    # tmp[2] = 2
    # tmp[3] = 3
    # tmp[4] = 4
    # tmp[5] = 5
    # tmp[6] = 6
    #fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
    #                     ->
    a=list()
    a.append(0)
    a.append(1)
    for x in range(end):  #자리수 마다 넣어줄껄 조건해주는 것 [0]자리 [1]자리 [2]자리 [3]자리 [4]자리 ----
        #if a[x] < end:
            if x <= 1:   # 0 1
                ''
            else:        # 2 3 4
                a.append(a[x-2]+a[x-1]) # 0번째 1번째
                if a[x-2]+a[x-1] > end:
                    return a[:-1]
                #a.append(a[1]+a[2]) # 1번째 2번째
                #a.append(a[2]+a[3]) # 2         
       # else:
        #    ''

        
    return ''

if __name__ == "__main__":
    print fibonacci(10)
    print fibonacci(20)
    print fibonacci(90)
    pass
