# -*- coding: utf-8 -*-

def histogram(int_list):
    """ 양의 정수 데이터(리스트 형)를 전달받고, '*' 로 히스토그램을 만들어 반환하는 함수를 작성하자
        ("\n"로 잇는다 print로 출력하면 화면에 그려지도록)

        sample in/out:
          histogram([2,3,6,5]) -> "**\n***\n******\n*****"
          histogram([1,2,3,2,1]) -> "*\n**\n***\n**\n*"
    """
    r = []
    for c in int_list:
        h = "*" * c
        r.append(h)
    return "\n".join(r)

if __name__ == "__main__":
    print repr(histogram([2,3,6,5]))
