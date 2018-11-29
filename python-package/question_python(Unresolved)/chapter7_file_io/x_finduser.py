# -*- coding: utf-8 -*-
import hashlib
import os

def decrypt(hex_digest):
    """ 가지고 있는 user와 password 정보를 가지고 입력된 hex_digest가 어떤
        조합인지 알아내, (user, password) 형태로 튜플로 반환하는 함수를 작성하자

        note1: hash에는 sha256 알고리즘이 사용됐다
        note2: hash할 때 message는 user+password 조합을 사용했다
        note3: '\n' 개행 문자가 없어야 정상적으로 연산이 된다
    """
    p = os.path.dirname(__file__)
    uf = os.path.join(p, "attachments/500_username_sample.txt") # user 정보
    pf = os.path.join(p, "attachments/500_password_sample.txt") # password 정보
    a=[]
    b=[]
    c=()
    with open(uf, 'r') as f:
        a = f.read().split()
    
    with open(pf, 'r') as f:
        b = f.read().split()
    
    for x in a:
        for y in b:
            heg = hashlib.sha256(x+y).hexdigest()
            if heg == hex_digest:
                c = (x,y)                
    return c

if __name__ == "__main__":
    p = os.path.dirname(__file__)
    hf = os.path.join(p, "attachments/user_pwd_digests.txt")    # hexdigest 모음 (이걸로 테스트 합시다)
    with open(hf, 'r') as f:
        hex_digests = f.read().split()

    dg_to_find = hex_digests[9]
    print decrypt(dg_to_find)
    

    