# -*- coding: utf-8 -*-


def get_types_of_elements(input_list):
    """ 리스트를 입력받고, 요소들의 데이터타입을 리스트로 반환하는 함수를 작성하자

        sample in/out:
            sample_list = [100, "hello", [1,2,3], {'d':1, 'i': 2, 'c': 3, 't':4}]
            get_types_of_elements(sample_list) -> ["<type 'int'>", "<type 'str'>", "<type 'list'>", "<type 'dict'>"]

            sample_list = [1452, 11.23, 1+2j, True, (0, -1)]
            get_types_of_elements(sample_list) -> ["<type 'int'>", "<type 'float'>", "<type 'complex'>", "<type 'bool'>", "<type 'tuple'>"]
    """
    # 여기 작성
    a = list()
    for x in range(len(input_list)):
        a.append(type(input_list[x]))
    return a


if __name__ == "__main__":
    sample_list = [100, "hello", [1,2,3], {'d':1, 'i': 2, 'c': 3, 't':4}]
    sample_list2 = [1452, 11.23, 1+2j, True, (0, -1)]
    print get_types_of_elements(sample_list)
    print get_types_of_elements(sample_list2)
    pass


