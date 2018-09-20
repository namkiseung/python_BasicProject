# -*- coding: utf-8 -*-
import requests

def get_web_page2(url_list):
    """ 웹 url 리스트를 전달받아서, 차례로 페이지를 요청하고, 
        각 페이지의 소스코드를 한개의 list에 담아서 반환하는 함수를 작성하자
    """
    # 여기 작성
    
    
    #a= r.split()
    a=''
    b=[]
    for x in url_list:
        res = requests.get(x)    
        b.append(res.content)
    
    return b


if __name__ == "__main__":
    print get_web_page2(["http://www.op.gg", "http://192.168.0.120/tmp/index.php"])
    pass

