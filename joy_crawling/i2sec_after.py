# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

def open_file2(data, num): #exist
    res = requests.get("http://seoul.i2sec.co.kr/index.php?mid=community&category=235&document_srl={}".format(data))
    if 'consult' in res.url:
        return ''
    print '({}) : {}'.format(res.status_code, res.url)
    result = res.text
    soup = BeautifulSoup(result, 'html.parser')
    stored =''        
    if "rd_nav img_tx fr m_btn_wrp" in result:
        try:
            __name=soup.select('div.rd_hd.clear > div.board.clear > div.btm_area.clear > div > a')[0].get_text()
            __date=soup.select('div.rd.rd_nav_style2.clear > div.rd_hd.clear > div.board.clear > div.top_area.ngeb > div > span')[0].get_text()
            stored += '-------이름: {}, 날짜: {}----------------------------\n'.format(__name.encode('utf-8'),__date.encode('utf-8'))
            try:
                stored_content = soup.select('div.rd.rd_nav_style2.clear > div.rd_body.clear > article > div')[0].get_text()
                stored += stored_content.encode('utf-8')
            except IndexError:
                stored += "내용 없음"
            stored += '\n------------------------------------------------------'            
        except UnicodeDecodeError:            
            print 'failed : '+__date.encode('utf-8')
            print 'failed : '+__name.encode('utf-8')
        with open('C:/Users/namki/Desktop/i2sec_after/i2sec_read{}.txt'.format(num), 'a') as f:
            print stored
            f.write(stored)
    else:
        pass    
    pass
cnt=0
file_num=0
for x in range(12640,328,-1):
    cnt += 1    
    open_file2(x, file_num)
    if cnt == 50:
       cnt = 0
       file_num += 1   
       



