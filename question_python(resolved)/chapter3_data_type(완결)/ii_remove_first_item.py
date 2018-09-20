# -*- coding: utf-8 -*-


def remove_first_item(input_list):
    """ list를 입력받아서 첫번째 요소를 제거한 후 반환하는 함수를 작성하자

        sample data: ['apple', 'banana', 'cat', 'dinner']
        expected output: ['banana', 'cat', 'dinner']
    """
    # 여기 작성
    
    temp = input_list[0]    
    input_list.remove(temp)
    
    return input_list


if __name__ == "__main__":
    sample_lists = ['apple', 'banana', 'cat', 'dinner']
    print(remove_first_item(sample_lists))
    pass

