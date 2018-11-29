# -*- coding: utf-8 -*-


def xx_age(age):
    """ 변수 age로 나이를 전달 받고, 
          60보다 크면, “노년”, 
          40~59 사이면, “중년”, 
          20~39 사이면, “청년”, 
          그 외에는 “유년” 이라고 출력해보자.
    """
    # 여기 작성
    if age>60:
        return '노년'
    elif 40 <= age <60:
        return '중년'
    elif 20 <= age <40:
        return '청년'
    elif age==60:
        return '60살은 정의 되있지 않지만, 노년(진)..."강사님 이렇게 해도 맞겠죠?"'
    else:
        return "유년"
    


if __name__ == "__main__":
    print xx_age(50)
    print xx_age(20)
    print xx_age(55)
    print xx_age(60)
    print xx_age(10)
    print xx_age(2)
    print xx_age(34)
    pass

