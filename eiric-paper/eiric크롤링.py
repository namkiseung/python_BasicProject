#-*- coding: utf-8 -*-
from selenium import webdriver
import os, sys, wget
def paper_writer():
    저자데이터=list()
    저자=driver.find_elements_by_css_selector("#contents > div.ListPage.ViewPage > div.bTableP > table > tbody > tr:nth-child(3) > td:nth-child(2)")
    for x in 저자:
        #print(str(x.text))
        if x is not None:
            저자데이터.append(str(x.text))
            #저자데이터.append('\n')
    return 저자데이터
def paper_content():
    내용데이터=list()
    내용=driver.find_elements_by_css_selector("#contents > div.ListPage.ViewPage > div.bTableP > table > tbody > tr:nth-child(4) > td")
    for x in 내용:
        #print(str(x.text))
        if x is not None:
            내용데이터.append(str(x.text))
            #내용데이터.append('\n')
    return 내용데이터
def paper_title():
    논문제목텍스트데이터=list()
    논문제목텍스트=driver.find_elements_by_css_selector("#contents > div.ListPage.ViewPage > div.bTableP > table > tbody > tr:nth-child(2) > td > span:nth-child(1)")
    for x in 논문제목텍스트:    
        if x is not None:
            논문제목텍스트데이터.append(str(x.text))
            #논문제목텍스트데이터.append('\n')
    return 논문제목텍스트데이터
def paper_attachment():
    첨부파일데이터=list()
    첨부파일 =driver.find_elements_by_css_selector("#contents > div.ListPage.ViewPage > div.bTableP > table > tbody > tr:nth-child(3) > td.subject.TextACenter > span > a")
    for x in 첨부파일:
        첨부파일데이터.append(x.get_attribute("href"))
    return 첨부파일데이터
def download(url, name):
    wget.download(str(url), name)
    pass
def type_paper():
    논문분야 =driver.find_elements_by_css_selector("#contents > div.ListPage.ViewPage > div.bTableP > table > tbody > tr:nth-child(1) > td:nth-child(2) > b")
    논문분야데이터=list()
    for x in 논문분야:
        if x is not None:
            논문분야데이터.append(str(x.text))
            #논문분야데이터.append('\n')
    return 논문분야데이터

def mkdir_touch(foldername):
    try:
        if not(os.path.isdir(foldername)):
            os.makedirs(os.path.join(foldername))
            #file_touch(foldername, read="aisdjiajsd")
    except Exception as ex:
        print("fail make folder", ex)
    pass

def file_touch(foldername, attach_url, paper_writer, paper_content, paper_title, type_paper):
    download(attach_url, name="C:/Users/namki/Desktop/eiric-paper/"+foldername+"/"+paper_title+".pdf")
    file = open("C:/Users/namki/Desktop/eiric-paper/"+foldername+"/README.txt", 'a')
    try:
        file.write("저자 : "+paper_writer +"\n")
        file.write("주제 : "+type_paper +"\n")
        file.write("제목 : "+paper_title)
        file.write("\n 내용 \n"+paper_content)
        file.close()
    except Exception as ex:
        print("fail relatived files", ex)
    pass

if __name__=="__main__":
    sta_num=6515
    dea_num=7510
    path = "C:\chromedriver.exe"
    driver = webdriver.Chrome(path)
    paper=1
    fail_cnt=0
    while True: 
        while True:
            if paper==10 or paper==11 or paper==12 or paper==13 or paper==14 or paper==16 or paper==17 or paper==18:
                paper+=1
            sta_num+=1
            print("[DASHBOARD] paper : {}, http-fail : {}, sta_num : {}".format(paper, fail_cnt, sta_num))
            try:
                url="https://www.eiric.or.kr/community/post2_cseric.php?m=view&gubun=201612&num={}&pg=1&seGubun={}&seGubun1=&SnxGubun=%C6%F7%BD%BA%C5%CD&searchBy=&searchWord=".format(sta_num, paper)
                driver.get(url)
            except Exception as ex:
                print("url error + get method", ex)
            if paper_attachment() is not "[]":
                __name=''.join(paper_title())
                __type_paper=''.join(type_paper())
                #print(type(paper_attachment()))
                try:
                    mkdir_touch("[%s]%s" % (__type_paper,__name))
                    file_touch(foldername="[%s]%s" % (__type_paper,__name), attach_url=''.join(paper_attachment()),paper_writer=''.join(paper_writer()), paper_content=''.join(paper_content()), paper_title=''.join(paper_title()), type_paper=__type_paper)
                except Exception as ex:
                    print("try fail", ex)
            else:
                fail_cnt+=1
                if fail_cnt > 30:
                    fail_cnt=0
                    paper+=1
            if sta_num == dea_num:
                sta_num=6515
        if paper > 20:
            break
            

'''
전자정보연구정보센터 - 한국정보과학회 43회 정기총회 및 동계학술발표회
다운로드 링크 js-href : document.getElementsByTagName('a')[3].href
1-데이터베이스
2-사물인터
3-정보보호
4-정보통
6-컴퓨터시스템
7-소프트웨어공학
8-국방소프트웨어
9-모바일응용시스템
15-프로그래밍 언어
19-오픈소스소프트웨어
20-학부생및주니어 논문
---->폴더 생성하는데, 폴더이름은 (논문제목+논문분야)
README.txt파일의 내용으로 저장(내용은 아래와같다)
-논문분야 :
-논문제목 :
-저자 :
-주제:

---->README텍스트 파일과 첨부파일이 해당 폴더에 있어야함.
#"document.getElementsByTagName('th')[0]" + "document.getElementsByTagName('b')[1]"
'''

