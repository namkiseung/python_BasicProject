# -*- coding: utf-8 -*-


def vowel_or_not(char):
    """ 문자를 전달받아서 모음(aeiou)중 하나면 True를, 아니면 False를 반환하는 함수를 작성하자

    """
    # 여기 작성
    if char.count('a') or char.count('e') or char.count('i') or char.count('o') or char.count('u'):
        return True
    else:
        return False        
    return ''


if __name__ == "__main__":
    print vowel_or_not('phone')
    print vowel_or_not('bottle')
    print vowel_or_not('zzzzwjfqzzzzj')
    pass

