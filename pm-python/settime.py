import ntplib,time
def get_time():
    local_time=''
    try:
        c = ntplib.NTPClient()
        response = c.request('europe.pool.ntp.org',version=3)
        local_time = time.ctime(response.tx_time) #시간출력
    except ntplib.NTPException:
        local_time = time.ctime()
    return local_time

if __name__=="__main__":
    print(settime())
