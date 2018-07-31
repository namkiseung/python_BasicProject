# -*- coding: utf-8 -*-

def write_list(input_list):
    """ 전달받은 리스트를 파일에 저장하는 함수를 작성하자
        리스트의 각 요소는 개행으로 구분한다

        note: 저장되는 파일이름은 m_list.txt로 한다
    """
    a =''
    with open('m_list_txt', 'w') as f:        
        for x in input_list:            
            a += str(x) + '\n'
        f.write(a)
    return 


if __name__ == "__main__":
    a=[1,2,3,4,5,6,7,8,9]
    print write_list(a)    