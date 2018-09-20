import os

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

print ("Size: " + str(getFolderSize("c:")))



##folder=os.getcwd()

##number=0
##string=""
##
##for root, dirs, files in os.walk(folder):
##    for file in files:
##        pathname=os.path.join(root,file)
##        print(os.path.getsize(pathname))

##def get_size(path):
##    total_size = 0
##    for dirpath, dirnames, filenames in os.walk(path):
##        for f in filenames:
##            if os.path.exists(fp):
##                fp = os.path.join(dirpath, f)
##                total_size += os.path.getsize(fp)
##    
##    return total_size
##
#if __name__=="__main__":

##    print(get_size('c:\\'))
    
#p = popen('dir','r')
#print(p.read())


