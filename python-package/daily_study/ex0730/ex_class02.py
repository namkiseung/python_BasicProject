# -*- coding: cp949 -*-
class Phouse:
    washer = "wwwwwwwwwwwww"
    refrigerator = "bbbbbbbbbbbbb"
    def secu(self):
        print "aaaaaaaaaaaa"
    def bell(self):
        print "qqqqqqqqqqqqqqqqqqqq"

class Chouse(Phouse):
    game_console = "PS4"
    def iot_control(self):
        print "32124124214124asdasdasdasdasdasd"
    

c_house = Chouse()
#print dir(c_house)
print c_house.secu()
print c_house.bell()

print c_house.iot_control()
