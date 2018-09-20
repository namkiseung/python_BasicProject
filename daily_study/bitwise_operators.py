# -*- coding: utf-8 -*-

a = 0b11001100
b = 0b00110011
c = 0b01010101

print ''
print "[*] Bitwist operators."

print "[*] and, or, xor"
print "a: {:08b}".format(a)
print "b: {:08b}".format(b)
print " a & b = {:08b}".format(a&b)
print " a | b = {:08b}".format(a|b)
print " a ^ b = {:08b}".format(a^b)
print " a ^ c = {:08b}".format(a^c)
print ''

print "[*] shift left"
for cnt in range(8):
    print "a << {} = {:08b}".format(cnt, a<<cnt&0xff)

print "[*] shift right"
for cnt in range(8):
    print "a >> {} = {:08b}".format(cnt, a>>cnt&0xff)


