# -*- coding: cp949 -*-
import requests as re
from bs4 import BeautifulSoup as bs
import os,time

#클리어런스 베스트 상품 : https://front.wemakeprice.com/special/5000265
#클리어런스 오늘 상품 : https://front.wemakeprice.com/special/5000254
#슈퍼 투데이 상품 : https://front.wemakeprice.com/special/5000119
#90%할인 : https://front.wemakeprice.com/special/5000257

def crawl_init(url):
    request_headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
    res = re.get(url , headers=request_headers)
    soup = bs(res.text, "html.parser")
    return soup
def get_product(url):
    product_name=list()
    product_sale=list()
    ago_price=list()
    after_price=list()
    soup = crawl_init(url)
    for x in soup.findAll("p",{"class":"text"}): #제품 명 
       product_name.append(x.text)
    for x in soup.findAll("span",{"class":"num"}): #할인 전 구매 가격
       ago_price.append(x.text)
    for x in soup.findAll("span",{"class":"sale"}): #할인 율
       product_sale.append(x.text)
    for x in soup.findAll("em",{"class":"num"}): #할인된 실제 구매가격
       after_price.append(x.text)
    return [product_name, product_sale, ago_price, after_price]

if __name__=="__main__":
    clear_best="https://front.wemakeprice.com/special/5000265"
    clear_today="https://front.wemakeprice.com/special/5000254"
    super_today="https://front.wemakeprice.com/special/5000119"
    discount_ninety="https://front.wemakeprice.com/special/5000257"
    tag_name=""
    
    for url in [clear_best, clear_today, super_today, discount_ninety]:  
        try:
            print(url)
            v_data=get_product(url)
            if url == clear_best: #tag name
                tag_name="베스트 상품"
            elif url == clear_today: #tag name
                tag_name="오늘의 상품"
            elif url == super_today: #tag name
                tag_name="슈퍼투데이"
            elif url == discount_ninety: #tag name
                tag_name="90%할인율"
            print("#### {} ####".format(tag_name))
            for x in range(len(v_data[0])):
                print("{} : 할인율({}) 가격 : {}원 --> {}원".format(v_data[0][x], v_data[1][x], v_data[2][x], v_data[3][x]))
                with open("위메프할인정보.txt","a") as f:
                    f.write("#### {} ####".format(tag_name))
                    f.write("{} : 할인율({}) 가격 : {}원 --> {}원".format(v_data[0][x], v_data[1][x], v_data[2][x], v_data[3][x]))
                    f.write("\n")
        except IndexError as s:
            #print(s)
            pass
            

