# -*- coding: utf-8 -*-


def get_types_of_elements(input_list):
    """ 리스트를 입력받고, 요소들의 데이터타입을 리스트로 반환하는 함수를 작성하자

        sample in/out:
            sample_list = [100, "hello", [1,2,3], {'d':1, 'i': 2, 'c': 3, 't':4}]
            get_types_of_elements(sample_list) -> ["<type 'int'>", "<type 'str'>", "<type 'list'>", "<type 'dict'>"]

            sample_list = [1452, 11.23, 1+2j, True, (0, -1)]
            get_types_of_elements(sample_list) -> ["<type 'int'>", "<type 'float'>", "<type 'complex'>", "<type 'bool'>", "<type 'tuple'>"]
    """
    #r = []
##    for i in range(len(input_list)):
##        t = type(input_list[i])
##        r.append(t)
##    ############
##    for m in input_list:
##        t = type(m)
##        r.append(t)
    r = map(type, input_list)
    return r


if __name__ == "__main__":
    sample_list = [100, "hello", [1,2,3], {'d':1, 'i': 2, 'c': 3, 't':4}]
    print get_types_of_elements(sample_list)
