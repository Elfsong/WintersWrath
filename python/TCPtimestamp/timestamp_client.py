from socket import *

HOST = "45.76.111.7"
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input(">> ")
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()
