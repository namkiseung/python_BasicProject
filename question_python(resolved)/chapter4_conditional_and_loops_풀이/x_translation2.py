# -*- coding: utf-8 -*-
import string


msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def tran(char, num):
    """ 문자열과, 정수를 전달받고, 문자열의 문자를 각각 num 만큼 shift시킨 문자열을 반환하는 함수를 작성하자.
          (만약, shift 결과가 알파벳 마지막(z)을 넘어가면 다시 a부터 시작한다)
        hint: 시져 암호, ord, chr
    """
    ascii = string.ascii_lowercase
    ascii_to = ascii[num:] + ascii[:num]
    table = string.maketrans(ascii, ascii_to)
    r = msg.translate(table)
    return r

# 함수 작성이 끝나면, msg 변수의 내용을 해독해보자

if __name__ == "__main__":
    
    for i in range(1, 25):
        print tran(msg, i)
        print ''
