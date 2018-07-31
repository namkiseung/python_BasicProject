import os



def getfoldersize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        #else:
        #elif os.path.isdir(itempath):
            #total_size += getfoldersize(itempath)
    return total_size




#4,996,550,656 + 2,048,750,510
