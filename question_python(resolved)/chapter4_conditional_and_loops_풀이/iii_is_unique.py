# -*- coding: utf-8 -*-


def is_unique(input_list):
    """ 리스트를 전달받아서, 리스트에 담긴 요소들이 모두 다른 값인지(중복된게 없는지)를 True/False로 반환하는 함수를 작성하자

        sample in/out:
            is_uniques([2,4,5,7,9])     -> True
            is_uniques([2,4,5,5,7,9])   -> False
    """
    r = len(set(input_list)) == len(input_list)
    return r


if __name__ == "__main__":
    print is_unique([2,4,5,7,9])
    print is_unique([2,4,5,5,7,9])

