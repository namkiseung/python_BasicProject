# -*- coding: utf-8 -*-

# 화면에 Hello world를 출력하면서, 문제 파일이 어떤 형태로 구성되어 있는지 살펴봅시다.
# 어떻게 해야하는지 낯선 사람은 교사에게 지도받도록 합시다

def banner():                   # 이렇게 def로 시작하는 것을 함수라고 합니다. 여기선 banner라는 이름의 함수를 정의하고 있습니다.
    print                       # 함수에 대해선 "함수" chapter에서 더 자세히 다루는데, 일단은 정의하고 호출(함수사용)하는 형태만 눈에 익힙니다
    print u"### 파이썬 연습문제 Hello world ###"   # u""  문자열 앞에 붙는 u는 이 문자열이 유니코드라는 것을 명시하는 것입니다.
                                                  # 유니코드는 컴퓨터로 문자를 표현하는 방법 중 하나입니다.

def hello_world():
    print 'Hello world!!'
    """ 
        "Hello world!!"를 화면에 출력하는 코드를 작성해보자.
        hint: print 함수 사용
    """
    # 여기에 작성
    pass                        # pass는 아무 코드도 실행하지 않고 통과시키려고 할때 사용하는데, 
                                # 함수에 이름만 있고 내용이 없으면, 에러가 나기 때문에 사용되었습니다.
                                # 주로 코드의 틀을 (실제작업코드보다)우선적으로 작성해놓으려고 할때 사용합니다.


if __name__ == "__main__":      # 이 코드의 의미는 뒤에서 설명합니다. 메인(주) 코드를 실행하도록 하는 코드라고 기억합시다.
    banner()                    # banner() 함수를 호출합니다.  함수이름과 함께 괄호()를 적으면, 함수를 호출하는 것입니다. 
                                # 실행해보세요.
                                # # 은 주석(comment)입니다. 다른 프로그래머가(또는 미래의 내가) 코드를 이해할 수 있도록 돕는 용도로 사용합니다.
                                # 주석은 코드가 실행되지 않도록 하려는 용도로 사용하기도 합니다.
    # hello_world()             # hello_world 풀이를 작성했으면, 이 라인의 주석을 해제(# 문자를 지움)하고, 스크립트를 실행 해봅시다
                                # 사용하지 않는 코드는 다시 주석처리 하면 됩니다.
hello_world()

# 이어서 x_bonus.py도 살펴봅시다(보너스가 보너스가 아닙니다)