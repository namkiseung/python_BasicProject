import hashlib, sys, time, random

#http://tendollar.kr/profile
#namki
#dd7702563

#f7b72301524eeeb1510dc8139dfff395815d3f5d
#cbb0d1c7c417086e8347473fe2b8307139b77bf2
#6d034d892ef07308ac6948e984cf10e98863b7be

def hash_status_code(args="a", args2=''):
    if hashlib.sha1(args).hexdigest() == args2:
        return True
    else:
        return False

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s Time: %0.3f s' % (f.func_name, float(time2 - time1))
        return ret
    return wrap

def decryptMD5(testHash):
    #303A6626CE8BEDE210E97A2158A81CFDC
    return len(hashlib.md5(testHash).hexdigest())

print(decryptMD5("d"))
#print hash_status_code(args2="5f0d0c2671cc62b19d2716256a49e3d34fd982f4")
    
#print len("03A6626CE8BEDE210E97A2158A81CFDC")
