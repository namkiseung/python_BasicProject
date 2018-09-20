# -*- coding: utf-8 -*-


def it_is_4():
    """ 아래 dict_b 로부터 [11, 22, 33] 을 얻으려면 어떤 키를 사용해야 하는가?
    """
    dict_b = {"key1": [11,22,33], "key2": [100, 200, 300]}
    a1 = "key1"
    a2 = "key2"
    nn = "I don't know"
    return a1 # nn을 답으로 대체


if __name__ == "__main__":
    print('it_is_4()의 답은?',it_is_4())
    pass

