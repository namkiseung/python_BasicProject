# -*- coding: utf-8 -*-


def concatenate_strings(input_list):
    """ 입력받은 문자열 리스트를 '-' 문자로 연결해서 반환하는 함수를 작성하자
        hint: join

        sample data: ['Red', 'White', 'Black'] 
        expected output: 'Red-White-Black'
    """    
    # 여기 작성
    #[이해]
    #1.리스트가 입력되어 들어왔다    
    #2.첫번째 방에 있는 값 이름 배치
    #3.두번째 방에 있는 값 이름을 연결
    #4.세번째,네번째 ~ n번째 연결
        #4-1 연결 사이에 '-'문자 삽입
    #5 리스트 문자들을 연결하여 반환

    #[알고리즘]
    #반복문으로 문자열 길이 만큼 반복해 데이터를 저장하자
    #사이사이에 '-' 문자를 삽입하여 반환
    concat_list_name=''
    for seq in range(len(input_list)):
        concat_list_name += input_list[seq]+'{0}'    
    
    return concat_list_name.format('-')[:-1]


if __name__ == "__main__":
    color_list=['Red','White','Black']
    print(concatenate_strings(color_list))
    pass

# 리스트 이름 자체를 나열해야하는지?
# 리스트의 인덱스 값을 뽑아 나열해야하는지?


"""
[정리]
1) 리스트의 출력할 문자를 담을 변수 'a' 생성
2) 리스트길이만큼 반복해서 인덱스를 추출한다
3) 길이만큼 추출한 데이터를 변수'a'에 문자를 이어 저장한다
4) 모든 인덱스를 연결한 변수'a'의 사이사이에 '-'라는 문자 삽입
-> 맨 마지막 문자 뒤에 '-'가 튀어나오는 문제발생
5) [:-1] 슬라이스로 맨 마지막 문자 제거
6) 데이터가 반복되어 저장할때 '-'문자 추가시  .format() 메서드로 해결

"""
