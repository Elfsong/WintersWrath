#coding=utf-8
import socket
import sys
import html_pb2
import zlib
import redis

#reload(sys)
#sys.setdefaultencoding( "utf-8" ) 

BUF_SIZE = 8192
host = 'localhost'
port = int(sys.argv[1]) 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#server.setblocking(0)
server.bind((host, port))
server.listen(1) 
client, address = server.accept()


data = client.recv(BUF_SIZE)

result = zlib.decompress(data.decode('utf-8'))

print result
client.close()
server.close()

print data




