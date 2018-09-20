# -*- coding: utf-8 -*-


def get_sum(input_list):
    """ 정수들을 요소로 갖는 리스트를 전달받아서, 그 정수들의 총 합을 반환하는 함수를 작성해보자
        hint: sum

        sample data: [10,20,30]
        expected output: 60
    """
    # 여기 작성
    #리스트를 전달 받고 리스트의 총 길이를 반복하여 변수 추가로 더해서 담자.
    result_value = 0   #1. 합계를 담을 지역변수를 만든다
    for result in range(len(input_list)):  #2. 배열처음부터 끝까지 반복하는 수를 만들자
        result_value += input_list[result] #3. 반복하는 수를 리스트의 인덱스로 담아서 매번 값을 뽑아 저장
    
    return result_value  #4. 값 돌려주자


if __name__ == "__main__":
    sample_data = [10,20,30]
    print(get_sum(sample_data))  #프린트하
    
    pass
