# -*- coding: utf-8 -*-


def sum_sum(n1, n2, n3):
    """ 세 개의 정수를 전달받고, 합을 반환하는 함수를 작성한다.
        단, 세 개의 수가 모두 같은 수면, 합에 3을 곱한 결과를 반환한다

        sample in/out:
            sum_sum(1,2,3) -> 6
            sum_sum(2,2,3) -> 7
            sum_sum(3,3,3) -> 27
    """
    r = n1 + n2 + n3
    if n1 == n2 == n3:
        r = r * 3  # r *= 3
    return r


if __name__ == "__main__":
    print sum_sum(1,2,3)# -> 6
    print sum_sum(2,2,3)# -> 7
    print sum_sum(3,3,3)# -> 27

