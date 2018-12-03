# -*- coding: utf-8 -*-


def formated_add(x, y):
    """ 두 개의 정수 x, y를 전달받고, 두 수의 합을 sample 형식에 맞게 반환하는 함수를 작성하자

        sample data: 10, 13
        expedted output: "10+13=23"
    """
    # 여기 작성
    "10+13=23"
    #1차 변환
    args1 = str(x)
    args2 = str(y)
    args3 = x+y
    #2차 변환
    c_args = args1 + '{0}' + args2 + '{1}'

    #3차 변환
    final_c_args = c_args+str(args3)
    return final_c_args.format('+','=')


if __name__ == "__main__":        
    
    print('expedted output', formated_add(10, 13))
    pass

                    
