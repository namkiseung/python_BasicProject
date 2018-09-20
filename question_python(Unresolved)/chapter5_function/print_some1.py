# -*- coding: utf-8 -*-

v_global = 10
def print_some1(num):
    """ 참조 전용
    """
    return v_global+num


if __name__ == "__main__":
    print print_some1(10)

