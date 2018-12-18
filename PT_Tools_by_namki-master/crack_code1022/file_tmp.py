# -*- coding:utf-8 -*-

def crack_id(file_name):
    input_id=list()
    with open(file_name+".txt","r") as f:
        content = f.read()
        for x in content.split():
            x.strip('\n')
            if x == '\n' or x == '':                
                pass
            else:
                input_id.append(x)
        return input_id

def crack_pw(file_name):
    input_pw=list()
    with open(file_name+".txt","r") as f:
        content = f.read()
        for x in content.split():
            #x = x.split()
            if x == '\n' or x == '':
                pass
            else:
                input_pw.append(x)
        return input_pw

    #res = f.readline()
    #print res
#res = files.read()
#tmp = 

#print res
if __name__ == "__main__":
    '''
    id_list = crack_id("wl_id")
    for x in id_list:
        print "user_id : %s" % x
    pw_list = crack_pw("wl_pw")
    for x in pw_list:
        print"user_pw : %s" % x
'''
