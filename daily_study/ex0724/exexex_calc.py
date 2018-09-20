# -*- coding: utf-8 -*-

##import yyyy
##
##if __name__ == "__main__":    
##    print yyyy.calculate(5,2,1)
##    pass


from yyyy import calculate

if __name__ == "__main__":
    a = input('first num : ') 
    b = input('second num : ')
    c = input('select calc : (1 : +)(2 : -)(3 : *)(4 : /)')
    print calculate(a,b,c)    



