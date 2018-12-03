

adress_book=[]
for c in range(10):
    for d in range(10):
        ip = "192.168.{0}, {1}".format(c,d)
        print ip

    adress_book.append(ip)

##for a in range(10):
##    for b in range(10):
##        print a,'x',b ,'=', a*b

for a in range(10):
    for b in range(1, 10):
        print (9-a),'x',b ,'=', (9-a)*b
    print ' '
