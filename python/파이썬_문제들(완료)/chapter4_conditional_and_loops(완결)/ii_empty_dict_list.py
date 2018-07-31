# -*- coding: utf-8 -*-


def empty_dict_list(x):
    """ 정수를 전달받고 그 수만큼의 빈 사전 리스트를 반환하는 함수를 작성하자
        sample in/out:
            count_of_dictionaries(5) -> [{}, {}, {}, {}, {}]
            count_of_dictionaries(10) -> [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
    """
    # 여기 작성
    
    #정수 개수 만큼
    #비어있는 사전 리스트 반환하자.
    a=dict()
    b=list()
    for n in range(x):
        b.append(a)            
    return b

if __name__ == "__main__":
    print empty_dict_list(3)
    print empty_dict_list(5)
    print empty_dict_list(10)
    pass

