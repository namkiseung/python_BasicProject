# -*- coding: utf-8 -*-

address_book = {"odd": [], "even": []}

for c in range(1, 10):
    for d in range(1, 10):
        ip_address = "192.168.{0}.{1}".format(c, d)
        if d % 2 == 0:
            address_book["even"].append(ip_address)
        else:
            address_book["odd"].append(ip_address)

# 2 address_book의 키는?
print address_book.keys()

# 3 홀수주소 출력하기
for a in address_book["odd"]:
    print a
print "\n".join(address_book["odd"])

# 4
for k in address_book.keys():
    for addr in  address_book[k]:
        print addr

# 5
for k in address_book.keys():
    for addr in  address_book[k]:
        if addr == "192.168.5.5":
            break
        print addr
