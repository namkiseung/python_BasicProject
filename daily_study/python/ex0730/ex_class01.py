#-*- coding : utf-8 -*-
class Calc:
    def __init__(self):
        pass
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2

calc = Calc()
print calc.add(1,2)
print ''
print calc.sub(100,99)

class Person:
    """
    æ»≥Á«œºº
    """
    name = ""
    age = ""
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def intro(self):
        print "Hi I'm {}, {}".format(self.name, self.age)

ttamna = Person("ttamna", 99)
ttamna.intro()
