# -*- coding: utf-8 -*-


def file_extension(filename):
    """ 파일 이름을 전달받아서 확장자를 반환하는 함수를 작성하자

        sample data: python.exe
        expteted output: exe
    """
    # 여기 작성
    #print(dir(filename))
    
    # .발견되면 그 뒤로 쭉 반환
    dat = "."    
    return filename[filename.index(dat)+1:]


if __name__ == "__main__":
    file1='a.txt'
    file2='a.war'
    file3='a.jpeg'
    file4='a.egg'
    file5='a.bat'
    print(file_extension(file1))
    print(file_extension(file2))
    print(file_extension(file3))
    print(file_extension(file4))
    print(file_extension(file5))
    pass

