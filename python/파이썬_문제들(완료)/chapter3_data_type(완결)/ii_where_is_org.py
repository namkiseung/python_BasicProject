# -*- coding: utf-8 -*-


def where_is_org(input_list):
    """ 입력된 list에서 'org'가 몇번째에 있는지를 반환하는 함수를 작성해보자
        ! 'org' 가 반드시 포함돼 있어야 함

        sample data: ["co.kr", "com", "org", "net", "re", "ru"]
        expected output: 2
    """
    
    for result in range(len(input_list)):
        if 'org' == input_list[result]:
            a=result            
        else:
            pass
    
    # 여기 작성
    return a


if __name__ == "__main__":
    sample = ["co.kr", "com", "org", "net", "re", "ru"]
    print(where_is_org(sample))
    pass
