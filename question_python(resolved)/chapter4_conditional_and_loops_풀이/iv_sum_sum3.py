# -*- coding: utf-8 -*-


def sum_sum3(x, y):
    """ 두 개의 수를 전달받아 합을 반환하는 함수를 작성하자.
        단, 그 합이 15~20 사이의 값이면, 20을 반환한다

        sample in/out:
            sum_sum3(10, 20) -> 30
            sum_sum3(5, 10) -> 20
            sum_sum3(1, 5) -> 6
    """
    r = x + y
    if 15 <= r <= 20:
        return 20
    else:
        return r


if __name__ == "__main__":
    print sum_sum3(10, 20)
    print sum_sum3(5, 10)# -> 20
    print sum_sum3(10, 8)# -> 20
    print sum_sum3(1, 5)# -> 6
