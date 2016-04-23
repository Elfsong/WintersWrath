#coding:utf-8
import socket
import urllib2
import html_pb2
import zlib
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


host = 'localhost'
port = int(sys.argv[1])
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

result = zlib.compress( "www.baidu.com" ).encode('utf-8')
print (result)
	
client.send( result )  

client.close()
