# -*- coding: utf-8 -*-


def print_dict(input_dict):
    """ 입력된 dict의 키와 값을 아래와 같이 문자열로 만들어 반환하는 함수를 작성하자

        sample in/out:
            print_dict({"ham":"yes", "egg":"yes", "spam":"no"}) -> "(1) egg -> yes\n(2) ham -> yes\n(3) spam -> no"
    """
    r = []
    items = input_dict.items()
    for i in range(len(items)):
        m = "{} {} -> {}".format(i+1, items[i][0], items[i][1])
        r.append(m)
    return "\n".join(r)


if __name__ == "__main__":
    print print_dict({"ham":"yes", "egg":"yes", "spam":"no"})

