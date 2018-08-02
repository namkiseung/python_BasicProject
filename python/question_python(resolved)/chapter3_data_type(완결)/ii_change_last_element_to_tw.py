# -*- coding: utf-8 -*-


def change_last_element_to_tw(input_list):
    """ 마지막 요소를 'tw'로 변경해서 반환하는 함수를 작성해보자
        
        sample data: ["co.kr", "com", "org", "net", "re", "ru"]
        expected output: ["co.kr", "com", "org", "net", "re", "tw"]
    """
    #마지막 어떤게 있을지만 그곳에 'tw' 리터럴 변수 덮어쓰기
    input_list[-1]='tw'
    
    return input_list
''' 
    # 여기 작성
    #1. 마지막 요소 알아내기
    original_word=input_list.pop()
    #2. 마지막 요소 스왑
    cd_word = 'tw'
    original_word = cd_word
    #3. 변환한 리스트 반환
    input_list.append(original_word)
'''




if __name__ == "__main__":
    ex_list = ["co.kr", "com", "org", "net", "re", "ru"]
    change_last_element_to_tw(ex_list)
    print(ex_list)
    pass
