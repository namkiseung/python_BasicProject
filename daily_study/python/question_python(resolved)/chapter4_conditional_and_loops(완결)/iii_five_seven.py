# -*- coding: utf-8 -*-


def five_seven(x, y):
    """ 전달 받은 두 수(경계 모두 포함)의 범위에서 7로 나눠지면서, 5의 배수인 수의 목록을 "," 로 구분한 문자열로 반환하는 함수를 작성하자

        sample in/out:
            five_seven(1500, 1600) -> "1505, 1540, 1575"
            five_seven(1500, 1700) -> "1505, 1540, 1575, 1610, 1645, 1680"
    """
    # 여기 작성
    result = ''
    # x부터 y 사이 숫자중    
    for num in range(x, y+1):
        
        if num % 7 == 0 and num % 5 == 0:
            result ='',num
            print num
        else:
            continue
    # 만약 x가 7로 나누었을때 나머지 0
        #만약 x가 
    return 'success'


if __name__ == "__main__":
    print five_seven(1500, 1600)
    print five_seven(1500, 1700)
    pass

