import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
datas={
    'user_id':'admin\"--',
    'user_pw':'1111'
}

def get_html():
    result = {}
    list_writer = []
    list_title = []
    with requests.Session() as a:
        a.header = header
        login = a.post("http://172.30.87.166:1111/login_chk",data=datas)
        html = a.get("http://172.30.87.166:1111/list")
        soup = BeautifulSoup(html.text, "html.parser")
        
        writer = soup.findAll("td", {'class':"tail"})
        title = soup.findAll('b')
        
        for x in writer:
            if x not in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']:
                list_writer.append(x.text)#print("글 제목 : {}".format(x.text))
        for y in title:
            list_title.append(y.text)#print("작성자 {}".format(y.text))    
        
        for num in range(len(list_title)): 
            try:
                result[list_writer[num]] = list_title[num]  
            except Exception as a:
                pass
        
        for key, value in result.items():
           print("작성자 : {}, 글제목 : {}".format(key, value))
    pass
        

if __name__=="__main__":
    get_html()