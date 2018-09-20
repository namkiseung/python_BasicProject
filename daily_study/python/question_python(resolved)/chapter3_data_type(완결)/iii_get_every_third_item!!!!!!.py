# -*- coding: utf-8 -*-


def get_every_third_item(input_list):
    """ list를 전달받아서 세번째에 오는 요소들만 따로 목록으로 만들어 반환하는 함수를 작성하자
          (말로 설명이 어려우니 sample_data, expected_output을 보자)
        
        sample data: [1,2,3,4,5,6,7,8,9]
        expected output: [3,6,9]

        sample data: [10, 20, 30, 40, 50, 60, 70]
        expected output: [30, 60]
    """
##list = (3)           1*3
##list = (6)           2*3
##list = (9)           3*3
##list = (12)          4*3
##list = [3, 6, 9, 12]
##
##1번 회전할때 list[2]
##2번 회전할때 list[5]
##3번 회전할때 list[8]
##4번 회전할때 list[12]
##5번 회전할때 list[15]
##
##
##   <1>각 인덱스에 *3값을 넣기
##   <2>2, 5, 8 자리수값을 다른 리스트에 넣기
    # 여기 작성
    #a=list()
    #a=input_list[range(2,len(input_list),3)]
    """
    #1. 리스트의 인덱스 위치의 규칙을 찾기
        1.1 3번째 자리의 리스트를 출력하는 규칙을 찾자
        1.2 list[2]->list[5]->list[8]->list[12]->list[15]
        1.3 (2,5,8,12,15) (2.5.8.12) (2.5.8) 과 같이 리스트(패키지)를 만든다
        1.4 입력받는 리스트의 길이보다 작은 리스트(패키지)를 비교한다
        1.5 적절한 리스트(패키지)를 사용해서 index별로 value를 새로운 리스트에 담는다
        1.6 새로운 리스트를 반환해준다.
    #2. 정렬방법
        2.1 맨 마지막 번째 숫자를 pop()한다
        2.2 3의 배수일 경우 새로운 리스트에 담는다
        2.3 반복한다
        2.4 반복한다면 점점 작은숫자가 나올텐데 '3'이라는 숫자가 나오면
        2.5 '3'까지 담은 새로운 리스트를 반환한다.
    #3. 3의 배수 이용
        3.1 리스트의 인덱스 값을 0~리스트 길이 만큼반복한다
        3.2 반복하면서 %3==0 과 같이 3의 배수인 value가 발견된다면
        3.3 새로운 리스트 인덱스 0번째에 담는다(발견시 그다음 인덱스에 담는다)
        3.4 만들어진 리스트를 반환한다
    """    
##    a=list()
##    a=input_list.pop()
##    b=[input_list.pop(1)]
    
    return input_list[2::3]

if __name__ == "__main__":
    list_01=[1,2,3,4,5,6,7,8,9]
    list_02=[10, 20, 30, 40, 50, 60, 70]

    print(get_every_third_item(list_01))
    print(get_every_third_item(list_02))
    


