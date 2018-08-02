# -*- coding: utf-8 -*-


def remove_key(input_dict, key_to_remove):
    """ dict형 변수 input_dict와 문자열 변수 key_to_remove 를 전달받아서
          input_dict에 key_to_remove에 해당하는 key가 있으면,
          그 키:값 쌍을 지우고 input_dict를 반환하는 함수를 작성하자
        
        sample data: {'a':1,'b':2,'c':3,'d':4}, 'b'
        expected output: {'a': 1, 'c': 3, 'd': 4}
    """
    '''
    -시나리오-
    1. 입력받은 dict
        1.1 dict의 키값을 리스트에 순서대로 담자
        1.2 리스트의 0번째 value ---- dict의 0번째 키 문자가 같은지 비교
        1.3 리스트의 1번째 value ---- dict의 1번째 키 문자가 같은지 비교
        1.4 리스트의 2번째 value ---- dict의 2번째 키 문자가 같은지 비교
        1.5 리스트의 3번째 value ---- dict의 3번째 키 문자가 같은지 비교
        1.6 리스트의 4번째 value ---- dict의 4번째 키 문자가 같은지 비교
        1.7 리스트의 n-1번째 value ---- dict의 n-1번째 키 문자가 같은지 비교
        1.8 리스트의 n번째 value ---- dict의 n번째 키 문자가 같은지 비교
        
    2. 발견되는 키가 있다면 그 데이터 remove하고 나머지 반환
        2.1 del 함수사용
    3. 발견되는게 없다면 그 리스트 그대로 반환
    '''
    #print('a' in input_dict.keys()[0])
    #print('b' in input_dict.keys()[1])
    #print('c' in input_dict.keys()[2])
    #print('d' in input_dict.keys()[3])
    
    #for seq in range(len(input_dict.keys())):
    #    result[seq] = 
    #result[0]
    #print(type(result))
    # 여기 작성
    #print(type(input_dict.keys())
    #for matching_word in len(input_dict):
    #   if input_dict['key_to_remove'] == key_to_remove
    del input_dict[key_to_remove]     
    return input_dict


if __name__ == "__main__":
    dict_sample = {'a':1,'b':2,'c':3,'d':4}
    index_str = 'b'
    
    print('원본 값 :',dict_sample)
    print('(삭제할 특정 key :"'+index_str+'")')
    print('결과 : ',remove_key(dict_sample, index_str))
    #print(dict_sample.keys('a'))
    pass

