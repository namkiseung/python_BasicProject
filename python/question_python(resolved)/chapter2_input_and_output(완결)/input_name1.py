# -*- coding: utf-8 -*-

def input_name(name):
    """ 이름을 인자로 입력받고, "Hello "라는 인사와 함께 화면에 출력해봅시다
        sample data: "ttamna"
        Output: Hello ttamna
    """
    # 여기에 작성
    print "Hello", name
    pass

if __name__ == "__main__":

    # 새로 작성, 주석 해제 등등 하면 됨(input 함수 사용)
    name = raw_input('What your name?')
    input_name(name)
    # input_name(name)          # 함수를 작성했으면(문제를 해결했으면) 실행해봅시다(기억이 나지 않으면 readme.py 참고)
