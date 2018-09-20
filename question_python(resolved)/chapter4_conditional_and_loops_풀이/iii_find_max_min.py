# -*- coding: utf-8 -*-


def find_max_min(input_list):
    """ 전달받은 정수 리스트에서 가장 큰 값과, 가장 작은 값을 찾아 리스트형태로 반환하는 함수를 작성하자

    sample in/out:
        find_max_min([1,2,3,4,5]) -> [5, 1]
        find_max_min([-1,-2,-3,-4,-5]) -> [-1, -5]
    """
    r = [max(input_list), min(input_list)]
    return r


if __name__ == "__main__":
    print find_max_min([1,2,3,4,5])

