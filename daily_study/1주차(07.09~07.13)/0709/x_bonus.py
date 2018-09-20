# -*- coding: utf-8 -*-
import calendar     # 모듈이 처음으로 등장했습니다.

# 앞서 파이썬을 소개하면서, 다양한 모듈들이 있다고 설명했는데, 
# calendar는 그런 모듈 중에 하나 입니다. 
# 누군가 달력을 편하게 출력하고 싶어서 작성해 놓은 모듈이죠. (덕분에 편하게 사용합니다)
# import '모듈이름' 이라고 선언하면 내 파이썬 프로그램에서 그 모듈의 기능을 사용할 수 있게 됩니다.
# 
# 모듈에 대한 자세한 내용은 뒤에 "모듈" 챕터에서 다룹니다.

""" 파이썬 쉘에서 아래처럼 실행해봅시다. help는 도움말을 출력하는 함수입니다

>>> import calendar
>>> help(calendar.month)
Help on method formatmonth in module calendar:

formatmonth(self, theyear, themonth, w=0, l=0) method of calendar.TextCalendar instance
    Return a month's calendar string (multi-line).

"""

def banner():
    print
    print "### Chapter 2 bonus"

def month():
    """ 년도와 월을 입력받아 달력을 반환하는 함수를 작성해보자
        hint: calendar.month(<년도_숫자>, <월_숫자>), 문자열로 된 달력을 반환한다(출력해보면 무슨 말인지 암)
    """
    yy = 2018   # 여기 작성
    mm = 2      # 여기 작성

    mon_string = calendar.month(yy, mm)     # 달력 구하기

    return mon_string               

# return 이 등장했습니다.
#
# 함수는 내부에서 어떤 처리를 하고, 그 결과를 호출자에게 돌려줄 수 있습니다.
#
# 이 때 return이란 문법을 사용합니다.  return <반환할 값> 이렇게 사용합니다
# 위에선 calendar.month 라는 함수가 리턴한 값을 mon_string 이란 변수에 저장하고
# 그 mon_string 변수를 반환(리턴)하고 있습니다


def month2(yy, mm):     # 괄호 안에, 변수가 있는데, 이런 변수를 파라미터라고 합니다.
                        # 파라메터는 함수 호출자로부터 전달받는데, "이 값에 대해 어떤 처리를 해라" 하는 용도로 사용합니다.
    """ 년도와 월을 입력받아 달력을 반환하는 함수
    """
    print yy            # 파라메터는 함수 내부에서 자유롭게 사용할 수 있습니다.
    print mm
    mon_string = calendar.month(yy, mm)     # 달력 구하기

    return mon_string  


if __name__ == "__main__":
    banner()
    month_result = month()                              # 달력이 반환되었으니 ,
    # 여기 작성                                          # 출력해봅니다


    # 인자를 전달받는 함수를 실행 해봅시다(아래 주석 해제 ㄱㄱ)
    #month_result2 = month2(2018, 2)                    # month2 는 2개의 파라메터를 받는 함수 입니다.
                                                        # 따라서 호출자는, 함수를 호출하면서, 괄호 안에 인자를 적어야 합니다.
                                                        # 인자는 아규먼트(arguments) 라고도 합니다
    