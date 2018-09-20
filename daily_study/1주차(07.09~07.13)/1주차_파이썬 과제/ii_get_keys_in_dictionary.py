# -*- coding: utf-8 -*-


def get_keys_in_dictionary(input_dict):
    """ 딕셔너리를 전달받아서, 키 리스트를 반환하는 함수를 작성하자
        
        sample data: {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}
        expected output: ['phone', 'favorite', 'year']

        sample data: {"key1": "green", "key2": "black"}
        expected output: ['key2', 'key1']
    """
    # 여기에 작성
    #dict에서 list로 변환하고 내용을 담자
    #3가지방법(insert/append/extend)
    result = list()
    result.append(input_dict.keys())
    
    return result


if __name__ == "__main__":    
    dict_ex = {"year": 2017, "favorite": ["Chicken", "Pizza", "Zazangmyun", "Ramyun"], "phone": "01012345678"}
    print(get_keys_in_dictionary(dict_ex))
    
    
    dict_ex2 = {"key1": "green", "key2": "black"}
    print(get_keys_in_dictionary(dict_ex2))
    pass

