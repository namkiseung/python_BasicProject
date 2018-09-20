# -*- coding: utf-8 -*-

sample_data = ["co.kr", "com", "org", "net", "re", "ru"]    # 리스트 정의
def get_last_element(input_list):
    """ 마지막에 있는 있는 데이터를 반환하는 함수를 작성해보자
        hint: -(마이너스), 음수, 인덱싱
        
        sample data: ["co.kr", "com", "org", "net", "re", "ru"]
        expected output: "ru"
    """
    # 여기 작성            
    #슬라이싱
    return sample_data[-1:]


if __name__ == "__main__":    
    print(get_last_element(len(sample_data))  )
    pass

#함수의 매개변수에 리스트의 길이 값을 넣자
#함수는 길이값의 숫자 크기 중 마지막 번째를 리턴하자
#출
