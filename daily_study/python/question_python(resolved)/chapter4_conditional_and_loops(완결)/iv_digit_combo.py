# -*- coding: utf-8 -*-


def digit_combo(x):
    """ 정수(positive) x를 입력받고, 0~x 까지의 수를 네 자리로 구성된 문자열로 리스트로 만들어서 반환하는 함수를 작성하자
        (빈 자리수는 0으로 채운다)
        hint: str.zfill

        sample in/out:
            digit_combo(5) -> ["0000", 0001", "0002", "0003", "0004", "0005"]
            digit_combo(10) -> ['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010']
    """
    # 여기 작성
    sam = []
    a=x
    for y in range(x+1):
        print "{}{:03}".format(0x10&y<<x, y)
        #sam.append(bb)
    return ''#sam


if __name__ == "__main__":
    print digit_combo(5) #-> ["0000", 0001", "0002", "0003", "0004", "0005"]
    print digit_combo(15) #-> ['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010']
    pass

