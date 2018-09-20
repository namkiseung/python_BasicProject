# -*- coding: cp949 -*-
def word_count(s):
    r = {}#리턴은 딕트
    words = s.split()
    for word in set(words):
        cnt = words.count(word)
        r[word] = cnt
    return r


if __name__=="__main__":
    s1 = "dog gand wjqiai aijc iasjc iasjdfuqwh uqfqwf dog iasjc"
    print word_count(s1)
    [r[word] = words.count(word) for word in set(words)]
    pass
