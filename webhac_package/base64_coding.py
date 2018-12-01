#-*- coding: utf-8 -*-
 
import base64
 
def main() :
    text = "VFdwSmQweHFZekZNYWtVMFRVTTBlRTlFWXowPQ="
    #print text
 
    #encoded_text = base64.encodestring(text)
    #print encoded_text
    decoded_text = base64.decodestring(text)
    print decoded_text
 
    print text == decoded_text
 
    return
 
if __name__ == "__main__" :
    main()
