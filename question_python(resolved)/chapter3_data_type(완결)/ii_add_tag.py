# -*- coding: utf-8 -*-


def add_tag(tag, data):
    """ 문자열을 두 개 tag, data 를 전달받아서, data를 tag 로 감싼 형태로 반환하는 함수를 작성하자.(sample 참조)
          (html 태그 형태인데, 나중에 많이 보게 될 것)

        sample data: tag="i", data="italic"
        expected output: "<i>italic</i>"

        sample data: tag="b", data="strong bold"
        expected output: "<b>strong bold</b>"
    """
    # 여기 작성
    
    element1 = '<'
    element2 = '>'
    element3 = '</'
    return element1+str(tag)+element2+str(data)+element3+str(tag)+element2


if __name__ == "__main__":
    print(add_tag('i','italic'))  #tag - data
    print(add_tag('b','strong bold'))  #tag - data
    pass


'''
예상하는 output

<html>
<head>
<title><span style='italic'>italic</span></title>
</head>
<body>
<b>스크립트</b>
<script>alert('hi');</script>
</body>
</html>
'''
