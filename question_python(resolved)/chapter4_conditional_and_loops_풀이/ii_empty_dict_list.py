# -*- coding: utf-8 -*-


def count_of_dictionaries(x):
    """ 정수를 전달받고 그 수만큼의 빈 사전 리스트를 반환하는 함수를 작성하자

        sample in/out:
            count_of_dictionaries(5) -> [{}, {}, {}, {}, {}]
            count_of_dictionaries(10) -> [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    """
##    r = []
##    for i in range(x):
##        r.append({})
    r = [{}] * x
    return r


if __name__ == "__main__":
    print count_of_dictionaries(5)# -> [{}, {}, {}, {}, {}]
    print count_of_dictionaries(10)

