# -*- coding: utf-8 -*-


def sum_sum2(x, y, z):
    """ 세 개의 정수를 전달받아 합을 반환하는 함수를 작성하자.
        단, 세개의 수 중에 두개 이상이 같은 값이면, 0을 반환한다
        
        sample in/out:
            sum_sum2(1,2,3) -> 6
            sum_sum2(2,2,3) -> 0
            sum_sum2(10, 10, 10) -> 0
    """
    # 여기 작성
    if x == y or y==z or x==z:
        return '0'
    else:
        return x+y+z        
    return


if __name__ == "__main__":
    print sum_sum2(1,2,3) #-> 6
    print sum_sum2(2,2,3) #-> 0
    print sum_sum2(10, 10, 10) #-> 0
    pass
