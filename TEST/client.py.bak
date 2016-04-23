import socket
import urllib2
import html_pb2
import zlib
import time
import sys

reload(sys)
sys.setdefaultencoding( 'utf-8' ) 

host = 'localhost'
port = int(sys.argv[1])
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

response = urllib2.urlopen("http://www.baidu.com")
result =  response.read() 
#print( result )
send_html = []

while result:
	if(len(result) > 8000):
		send_html.append( result[:8000] )
		result = result[8000:]
	else:
		send_html.append( result )
		send_html.append( "EOF")
		result = ''

send_list = []
segment_obj = html_pb2.html_segment()

count = 1
for html in send_html:
	segment_obj.id = count
	count = count + 1
	
	segment_obj.segment = html.decode('utf-8','ignore')
	out = segment_obj.SerializeToString()
	send_list.append(out)


for url in send_list:
	client.send( url )  
	time.sleep(1)
	print('send a segment')


client.send( "EOF" )
client.close()
