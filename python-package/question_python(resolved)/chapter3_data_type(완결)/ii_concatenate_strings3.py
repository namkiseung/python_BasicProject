# -*- coding: utf-8 -*-


def concatenate_strings3(input_list):
    """ 입력받은 문자열 리스트를 '\t' 로 연결해서 반환하는 함수를 작성하자

        sample data: ['Red', 'White', 'Black'] 
        expected output: 'Red\tWhite\tBlack'
    """
    # 여기 작성
    str_tmp = ' '
    for seq in range(len(input_list)):
        str_tmp += input_list[seq]+'{0}'    
    return str_tmp.format(u"\t")[1:]


if __name__ == "__main__":
    color_name_lists = ['Red', 'White', 'Black']    
    print('sample data\n'+concatenate_strings3(color_name_lists))
    print()
    print('expected output\n'+'Red\tWhite\tBlack')
    pass

