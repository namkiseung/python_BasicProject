import os

def get_whois(url):
    command = "whois " + url
    process = os.popen(command)
    result = str(process.read())
    return result

print(get_whois("https://www.tistory.com"))