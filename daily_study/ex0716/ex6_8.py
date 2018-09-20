# -*- coding: cp949 -*-

address_book = {"odd":[], "even":[]}
for c in range(1,10):
    for d in range(1, 10):
        ip_address = "192.168.{0}.{1}".format(c,d)
        if d%2 == 0:
            address_book["even"].append(ip_address)            
        else:
            address_book["odd"].append(ip_address)

#
#print 'Q.2', address_book.keys()
#
for p in address_book.keys():    
    print address_book
#print 'Q.3', address_book('odd')
#


##res = {"g":[]}
##for a in range(2):
##    for b in res[a]:
##       if " " ==b:
##           break
##        print b

    #1 반복문 key 1
    #2  반복문 value(1~end)
        #1 반복문 key 2
        #2  반복문 value(1~end)


#for k in address_book.keys():
 #   for m in address_book[k]:
        #print(type(address_book.keys()))
        #print(type(address_book[k]))
        #print(type(m))
   #     if m == "192.168.5.5":            
  #          break        
        #print m   
        
        

