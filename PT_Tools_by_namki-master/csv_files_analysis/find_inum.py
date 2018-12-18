#-*- coding:utf-8 -*-
import requests, csv, sys, codecs, re

def select_query(url):
    for x in range(100):    
        requests.get(url)    
    pass #return res.content

def csv_file_read(filename):    
    f = open(filename, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    #print type(rdr)
    for line in rdr:
        
        print line[4]
    f.close()
    pass

def parse_regi_number(text):
    pat = re.compile("\d(6)\-[1-4]\d(6)")
    return pat.match(text)

def parse_csv(filename):
    f = codecs.open(filename, 'r')
    rdr = csv.reader(f)
    for line in rdr:
        for text in line:
            if parse_regi_number(text) is not None:
                print line
    f.close()

def csv_file_write(filename):
    f = open(filename, 'w', newline='')
    wr = csv.writer(f)
    wr.writerow([1, "김정수", False])
    wr.writerow([2, "박상미", True])
    f.close()
    pass
    
if __name__=="__main__":    
    #print select_query("http://192.168.0.193:5000/main/view?bbs_no=635")
    #parse_csv("my_table.csv")
    #csv_file_read("my_table.csv")
    
    #print select_query("http://192.168.0.209:1111/")
    
    f = open("my_table.csv", "r")
    f.readline()
    res = f.read()
    print res
    print res.index("-")
    print res.find("-")
    while True:
        line = f.readline()
        if not line: break
        print line[5]
    f.close()
    
    
    
