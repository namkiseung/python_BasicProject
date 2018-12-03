#-*- coding:cp949 -*-
network_port = {
    "well_known" : range(0,1024),
    "registed" : range(1024,49152),
    "dynamic" : range(49152,65336),
    }

want = 'dynamic'
if network_port.has_key(want):
    print("1->Yes")
else:
    print("1->No")

want = 'static'
if network_port.has_key(want):
    print("2->Yes")
else:
    print("2->No")
