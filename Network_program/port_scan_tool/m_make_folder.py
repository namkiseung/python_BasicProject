import os

def create_dir(directory):
    if not os.path.exists(directory): #경로없을경우
        #디렉터리 만들기
        os.makedir(directory)
        
#파일 만드는 함수(write_file())
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
    pass