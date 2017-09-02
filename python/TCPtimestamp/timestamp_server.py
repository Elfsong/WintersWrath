from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "Waiting for connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "Connected from: ", addr

    while True:
        data = tcpCliSock.recv(BUFFSIZE)
        if not data:
            break
        tcpCliSock.send("[%s] %s" % (ctime(), data))

    tcpCliSock.close()
tcpSerSock.close()
