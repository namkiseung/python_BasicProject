# -*- coding: utf-8 -*-


def count_frequency(input_string):
    """ 문자열을 전달 받아서, 각 문자가 몇번 나오는지(빈도)를 dict로 만들어 반환하는 함수를 작성하자

        sample in/out:
            count_frequency("google.com") -> {'c':1, 'e':1, 'g':2, 'm':1, 'l':1, 'o':3, '.':1}
            count_frequency("apple") -> {'a':1, 'p':2, 'e':1, 'l':1}
            count_frequency("banana") -> {'a':3, 'b':1, 'n':2}
    """
    d = {}
    for ch in set("google.com"):
        d[ch] = input_string.count(ch)
    return d


if __name__ == "__main__":
    print count_frequency("google.com")

