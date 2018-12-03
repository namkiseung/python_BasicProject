# -*- coding: utf-8 -*-


def concatenate_strings2(input_list):
    """ 입력받은 문자열 리스트를 ', ' 로 연결해서 반환하는 함수를 작성하자

        sample data: ['Red', 'White', 'Black'] 
        expected output: 'Red, White, Black'
    """
    concat_word = ''
    # 여기 작성
    for seq in range(len(input_list)):
        concat_word += input_list[seq]+(', ')
    return concat_word[:-2]


if __name__ == "__main__":
    color_lists = ['Red', 'White', 'Black']    
    print(concatenate_strings2(color_lists))
    pass

