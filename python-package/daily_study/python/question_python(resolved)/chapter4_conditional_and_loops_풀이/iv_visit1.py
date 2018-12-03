# -*- coding: utf-8 -*-


def visit1(in_dict):
    """ dict를 전달받아서, dict가 가진 "키 : 값" 을 문자열로 만들고, "\n"로 붙여서 반환하는 함수를 작성하자

        sample in/out:
            d1 = {"name": "ttamna", "age":31, "fav":['3g', 'chi', 'piz']}
            visit1(d1) -> "age : 31\nfav : ['3g', 'chi', 'piz']\nname : ttamna"
            
            d2 = {"name": "gunin", "age":21, "fav":['choco', 'freetime', 'ohyes', 'chicken', 'pizza']
            visit1(d2) -> "age : 21\nfav : ['choco', 'freetime', 'ohyes', 'chicken', 'pizza']\nname : gunin"
    """
    r = []
    for k, v in in_dict.items():
        r.append("{} : {}".format(k, v))
    return "\n".join(r)


if __name__ == "__main__":
    d1 = {"name": "ttamna", "age":31, "fav":['3g', 'chi', 'piz']}
    print repr(visit1(d1))

