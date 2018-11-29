# -*- coding: utf-8 -*-


def xx_age(age):
    """ 변수 age로 나이를 전달 받고, 
          60보다 크면, “노년”, 
          40~59 사이면, “중년”, 
          20~39 사이면, “청년”, 
          그 외에는 “유년” 이라고 출력해보자.
    """
    if age >= 60:
        r = u"노년"
    elif age >= 40:
        r = u"중년"
    elif age >= 20:
        r = u"청년"
    else:
        r = "유년"
    
    return r


if __name__ == "__main__":
    print xx_age(70)
    print xx_age(45)
    print xx_age(25)
    print xx_age(15)

