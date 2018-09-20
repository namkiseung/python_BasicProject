# -*- coding: utf-8 -*-

import requests
def get_web_page(url):
    """ 웹 url을 전달받아서, 페이지를 요청하고 웹 페이지 소스코드를 반환하는 함수를 작성하자
        hint: requests
    """
    # 여기 
    res = requests.get(url)
    
    return res.content


if __name__ == "__main__":
    print get_web_page("http://www.op.gg")
    pass

