# -*- coding: utf-8 -*-


def odd_even(x):
    """ 정수를 전달받아서 그 수가 짝수면 'even'을, 홀수면 'odd'를 반환하는 함수를 작성하자

        sample in/out:
            odd_even(2) -> 'even'
            odd_even(1000) -> 'even'
            odd_even(777) -> 'odd'
    """
    if x%2==0:
        r = "even"
    else:
        r = "odd"
    return r


if __name__ == "__main__":
    print odd_even(2)# -> 'even'
    print odd_even(1000)# -> 'even'
    print odd_even(777)# -> 'odd'

