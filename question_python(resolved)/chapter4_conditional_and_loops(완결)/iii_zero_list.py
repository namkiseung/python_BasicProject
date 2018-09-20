# -*- coding: utf-8 -*-


def zero_list(length):
    """ 정수를 전달받아서, 정수 개수 만큼의 0으로 채워진 리스트를 만들어서 반환하는 함수를 작성하자

        sample in/out:
            zero_list(10) -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            zero_list(5) -> [0, 0, 0, 0, 0]
            zero_list(0) -> []
    """
    # 여기 작성
    #length
    a=list()
    for x in range(length):
        a.append([])
    return a


if __name__ == "__main__":
    print zero_list(10) #-> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print zero_list(5) #-> [0, 0, 0, 0, 0]
    print zero_list(0) #-> []
    pass

