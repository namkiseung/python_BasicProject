# -*- coding: utf-8 -*-

def game_of_three(x):
    """ 양의 정수를 전달받아, x 까지의 숫자(경계 포함) 리스트 반환하는 함수를 작성한다
        단, (3, 6, 9)중 하나가 수에 포함되면 리스트 추가하지 않는다

        sample in/out:
            game_of_three(10) -> [1, 2, 4, 5, 7, 8, 10]
            game_of_three(20) -> [1, 2, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 20]
    """
    # 여기 작성
    result = list()
    for num in range(1,x+1):
        if num%10==3 or num%10==6 or num%10==9:
            ''
        elif num/10==3 or num/10==6 or num/9:
            ''
        else:
            result.append(num)

##    s = list()
##    for i in range(1, x+1):
##        s=str(i)
##        if '3' in s or '6' in s or '9' in s:
##            continue
##        else:
##            s.append(i)
    return result

if __name__ == "__main__":
    print game_of_three(5)
    print game_of_three(20)
    print game_of_three(51)
    pass
