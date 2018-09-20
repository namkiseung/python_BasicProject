from bs4 import BeautifulSoup


html = """
<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
</head>
<body bgcolor="#FFFFFF" text="#000000" leftmargin="0" topmargin="0">
<table border="0" cellspacing="0" cellpadding="0" align=center width='100%'>
  <tr> 
    <td width="113" background="/image/top_left_bg.jpg">&nbsp;</td>
    <td width="905" background="/image/top_right_bg1.jpg"></td>
        </tr>
      </table>
</body>
</html>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')  #BeautifulSoup 객체를 가져와서 1번 인자는 html형식의 문자 2번 인자는 어떤 파서를 사용할지 지정.
title = soup.find_all()
for a in title:
    print(title)
#soup.select_one() #하나를 선택하는 메서드
# header = soup.select_one("body > div > h1")
# list_items = soup.select("ul.items > li")

# print(soup.select_one("ul"))
# for li in list_items:
#   print(li)



# 선택자는
#     "ul" "div"   는 태그 선택자
#      특정한 아이디를 선택할때 예를 들어 <div id="meigen">을 선택하려면 "#meigen"라고 한다 
#      클래스라는 이름을 가진 속성을 선택할때 <ul class="items">이면, ".items"라고 한다
