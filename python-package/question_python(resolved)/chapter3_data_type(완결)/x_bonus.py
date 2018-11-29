# -*- coding: utf-8 -*-

def banner():    
    print u"### Chapter3 Data-type bonus 문제 ###"
    

def stringed_float_to_int(stringed_float):
    """ '36.5' 처럼 문자열로 되어 있는 수를 소수점 아래는 버리고 int형으로 반환하는 함수를 작성하자.
        hint: 타입 변환(type casting, type conversion), (두번 변환)

        sample data: '36.5'
        expected output: 36

        sample data: '246.2458'
        expected output: 246
    """    
    # 여기 작성
    a= int(stringed_float)
    return a

def n_nn_nnn(n):
    """ 정수를 전달받아서, (정수가 n이면)정수의  n+nn+nnn 을 계산해서 반환하는 함수를 작성하자

        sample data: 5
        expected output: 615    
            # 5+55+555 의 결과

        sample data: 7
        expected output: 861
    """
    newnn=str(n)+str(n)
    newnnn=str(n)+str(n)+str(n)
    result = n+int(newnn)+int(newnnn)
    # 여기 작성
    return result

def duplication(input_list):
    """ 리스트를 전달받고, 중복을 제거한 리스트를 반환하는 함수를 작성하자
        hint: set은 중복을 허용하지 않는 자료형이다, set 자료형을 list로 형변환할 수 있다

        sample data : [1,1,2,2,2,3,3,3,1]
        expected output: [1, 2, 3]
    """
    # 여기 작성
    a = set(input_list)
    b = set(input_list)
    
    
    return a

if __name__ == "__main__":    
    print(banner())
    
    sample_data = 36.5
    sample_data2 = 246.2458
    print(stringed_float_to_int(sample_data))
    print(stringed_float_to_int(sample_data2))
    print()
    
    sample_data3 = 5
    sample_data4 = 7
    print(n_nn_nnn(sample_data3))
    print(n_nn_nnn(sample_data4))
    print()
    
    sample_data5 = [1,1,2,2,2,3,3,3,1]
    print(duplication(sample_data5))

    pass
