# -*- coding: utf-8 -*-


def test_number(x, y):
    """ 두 개의 수를 전달받아, 그 차가 5면 True를 반환하고, 아니면 False를 반환하는 함수를 작성한다

        sample in/out:
            test_number(10, 5) -> True
            test_number(5, 10) -> True
            test_number(1, 5) -> False
            test_number(-5, 0) -> True
    """
    if abs(x-y) == 5:
        return True
    else:
        return False


if __name__ == "__main__":
    print test_number(10, 5)

