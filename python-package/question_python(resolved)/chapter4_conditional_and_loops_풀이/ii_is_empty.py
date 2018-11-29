# -*- coding: utf-8 -*-


def is_empty(input_list):
    """ 사전들이 담긴 리스트를 전달받아서, 모든 사전이 비어있는지 검사하고, 비어있으면 True를, 아니면 False를 반환하는 함수를 작성하자

    sample in/out:
        is_empty([{},{},{}]) -> True
        is_empty([{1,2},{},{}]) -> False
    """
    for m in input_list:
        if len(m) != 0:
            return False
    return True


if __name__ == "__main__":
    print is_empty([{},{},{}])# -> True
    print is_empty([{},{1,2},{}])# -> False

