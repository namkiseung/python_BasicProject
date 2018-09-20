# -*- coding: utf-8 -*-


def get_values_in_dictionary(input_dict):
    """ 딕셔너리를 전달받아서, 밸류 리스트를 반환하는 함수를 작성하자
        
        sample data: {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}
        expected output: ['01012345678', ['Chicken', 'Pizza', 'Zazangmyun', 'Ramyun'], 2017]

        sample data: {"key1": "green", "key2": "black"}
        expected output: ['black', 'green']
    """
    # 여기에 작성
    '''
    <시나리오>
    1. 키 값 기준으로 데이터를 모두 뽑자
    2. list변수에 순서대로 담자
    3. 반환하
    '''
    sample_list = list()
    sample_list = input_dict.values()
    return sample_list


if __name__ == "__main__":
    dict_ex1 = {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}
    dict_ex2 = {"key1": "green", "key2": "black"}
    print('1번 예제의 values')
    print(get_values_in_dictionary(dict_ex1))
    print('\n')
    print('2번 예제의 values')
    print(get_values_in_dictionary(dict_ex2))
    pass

