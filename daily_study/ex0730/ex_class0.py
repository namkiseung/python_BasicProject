#-*- coding : utf-8 -*-
class Calc2:
    last=0
    def __init__(self):        
        pass
    def add(self, num1, num2):
        self.last=num1 + num2
        return num1 + num2
    def sub(self, num1, num2):
        self.last=num1 - num2
        return num1 - num2
    def mul(self, num1, num2):
        self.last=num1 * num2
        return num1 * num2
    def div(self, num1, num2):
        self.last=num1 / num2
        return num1 / num2

calc = Calc2()
print calc.add(4,2)
print calc.mul(4,4)
print calc.last
