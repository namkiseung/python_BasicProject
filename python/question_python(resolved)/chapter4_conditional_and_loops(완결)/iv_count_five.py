# -*- coding: utf-8 -*-


def count_five(input_list):
    """ 리스트를 전달받아 리스트에 포함된 5와 '5'의 개수를 리스트 형태로 반환하는 함수를 작성하자
        hint: type, isinstance

        sample in/out:
            count_five([1,2,3,4,5,5, '5544555']) -> [2, 5]  # 숫자 5가 2개, 문자 5가 5개(여기 주석은 설명일 뿐, 출력하는 거 아닙니다)
            count_five([1,2,3,4,5,5, '44']) -> [2, 0]       # 숫자 5가 2개, 문자 5가 0개

    """
    # 여기 작성
    #숫자형 개수 세기 -> 리스트 반환
    #문자형 개수 세기 -> 리스트 반환
    #<시나리오>   
    #만약 0 번째가 숫자다 그러면 숫자변수의 카운트 1개 올리자
    #아니다 0번째는 문자다 그러면 문자변수의 카운트 1개 올리자
    num_re=0
    str_re=0
    input_list_result = [1, 2, 3, 4, 5]
    result_str=''
    for x in range(len(input_list)):        
        if type(input_list[x]) != type(input_list_result[0]):          #문자라면            
            result_str=input_list[x]                        
            str_re = ','.join(result_str)
            str_re=str_re.count('5')
        elif type(input_list[x]) == type(input_list_result[0]) and input_list[x]==input_list_result[4]:        #숫자라면     
            num_re += 1
            
    return num_re,str_re


if __name__ == "__main__":
    print count_five([1,2,3,4,5,5, '55445555']) #-> [2, 5]  # 숫자 5가 2개, 문자 5가 5개(여기 주석은 설명일 뿐, 출력하는 거 아닙니다)
    print count_five([1,2,3,4,5,5, '44']) #-> [2, 0]  
    pass

