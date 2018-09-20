# -*- coding: utf-8 -*-


def square_dict(x):
    """ 정수(positive) x를 전달받고 1~x 까지(x포함)의 키를 가진 dict를 만들어서 반환하는 함수를 작성하자
          키의 쌍이 되는 값은 키의 제곱이다
        
        sample in/out:
            square_dict(10) -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
            square_dict(3) -> {1: 1, 2: 4, 3: 9}
    """
    r = {}
    for i in range(1, x+1):
        r[i] = i*i  # i**3
    return r


if __name__ == "__main__":
    print square_dict(10)

