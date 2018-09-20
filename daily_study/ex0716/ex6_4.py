#-*- coding:cp949-*-
address=250
if 0< address <255:
    print("[*] 1 -> normal")
elif 255<=address<=0:
    print("[*] 2 -> abnormal")


if not 255<=address<=0:
    print("[*] 3 -> normal")
