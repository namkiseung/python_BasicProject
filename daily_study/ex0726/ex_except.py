#-*- coding :cp949-*-
##try:
##    f = open("C:/Users/student/Desktop/hosts_re","r")
##    data = f.read()
##    print data
##    f.close()
##except IOError:
##    print ""
##    print "[*] data not found"
##
##print "#################"
##print "#####   END   #####"
##print "#################"
    
##try:
##    print 4/0
##except ZeroDivisionError:
##    print "not exec"
##except IOError:
##    print "not exec"
##except IOError:
##    print "not exec"

##try:
##    f = open("C:/Users/student/Desktop/hosts_re","r")
##    data = f.read()
##    print data
##    f.close()
##    #print 4/0
##except IOError:
##    print "IOError"
##    print "[*] data not found"
##except ZeroDivisionError:
##    print "ZeroDivisionError"
##    print "[*] Zero error"
##except:
##    print '###'
##    
##print "#################"
##print "#####   END   #####"
##print "#################"


if True:
    print "ifififififif"
try:
    print "[print : try]"    
except:
    print "[print : except]"
else:
    print "[print : else]"
finally:
    print "[print : finally]"
