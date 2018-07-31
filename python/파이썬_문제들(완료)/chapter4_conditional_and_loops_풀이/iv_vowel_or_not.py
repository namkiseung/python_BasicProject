# -*- coding: utf-8 -*-


def vowel_or_not(char):
    """ 문자를 전달받아서 모음(aeiou)중 하나면 True를, 아니면 False를 반환하는 함수를 작성하자

    """
    if char in "aeiou":
        return True
    else:
        return False


if __name__ == "__main__":
    print vowel_or_not('a')
    print vowel_or_not('c')

