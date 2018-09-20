# -*- coding: utf-8 -*-


def count_five(input_list):
    """ 리스트를 전달받아 리스트에 포함된 5와 '5'의 개수를 리스트 형태로 반환하는 함수를 작성하자
        hint: type, isinstance

        sample in/out:
            count_five([1,2,3,4,5,5, '5544555']) -> [2, 5]  # 숫자 5가 2개, 문자 5가 5개(여기 주석은 설명일 뿐, 출력하는 거 아닙니다)
            count_five([1,2,3,4,5,5, '44']) -> [2, 0]       # 숫자 5가 2개, 문자 5가 0개

    """
    i_cnt = 0
    s_cnt = 0
    for m in input_list:
        if isinstance(m, str):
            s_cnt += m.count('5')  # s_cnt = s_cnt + m.count('5')
        else:
            i_cnt += str(m).count('5')
            
    return [i_cnt, s_cnt]


if __name__ == "__main__":
    print count_five([1,2,3,4,555,555, '5544555'])

