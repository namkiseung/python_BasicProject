# -*- coding: cp949 -*-
def swap(str_sample):    
    a = str_sample.split('_')
    for x in range(len(a)):
        print a[x].title()
    return ''

if __name__ == "__main__":
    print swap('iphone_apple_akawk_akwkqq_book_mouse')
