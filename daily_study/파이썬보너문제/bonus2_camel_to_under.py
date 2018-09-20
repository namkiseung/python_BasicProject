
def swap(str_sample):    
    
    a=list(50)
    for x in range(len(str_sample)):        
        a[x] = str_sample.split(' ')
        print a[0].swapcase()
    return ''

if __name__ == "__main__":
    print swap('Iphone Apple Akawk Akwkqq Book Mouse')
