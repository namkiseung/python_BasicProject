# -*- coding: utf-8 -*-


def wicked(msg):
    """ 문자열을 전달받아서, 소문자는 대문자로 대문자는 소문자로 바꿔서 반환하는 함수를 작성하자

        sample in/out:
            wicked("Hello world ..") -> "hELLO WORLD .."
            wicked("Good Luck :)") -> "gOOD lUCK :)"
    """
    # 여기 작성    
    return msg.swapcase()


if __name__ == "__main__":
    print wicked('desktop')
    print wicked('i2sec')
    print wicked('Emaily')
    print wicked('Cmaily')
    pass

