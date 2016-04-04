def get_url_info(url, seg):
	import tldextract
	url_info = tldextract.extract( url )
	#get subdomain
	if(seg == 1):
		return url_info.subdomain
	#get domain
	if(seg == 2):
		return url_info.domain
	#get suffix
	if(seg == 3):
		return url_info.suffix
	#get domain and suffix
	if(seg == 4):
		return url_info.domain+'.'+url_info.suffix

def set_logging():
	import logging
	logging.basicConfig(level=logging.DEBUG,
						format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
						datefmt='%a, %d %b %Y %H:%M:%S',
						filename='spider.log',
						filemode='w')
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	console.setFormatter(formatter)
	logging.getLogger('').addHandler(console)

def get_302_url(url):
	import urllib2,socket
	from termcolor import colored, cprint

	try:
		request = urllib2.urlopen(urllib2.Request(url, headers = {'User-Agent':'Mozilla/8.0 (compatible; MSIE 8.0; Windows 7)'}))
		socket.setdefaulttimeout(15)
		return request.url
	except:
		cprint("Sorry...... Socket Timeout!",'red')
		return url

def connect_to_redis(DB=0):
	import redis
	global r
	r = redis.Redis(host='localhost',port=6379,db=DB)

def write_url_redis(original_url, skip_url):
	r.hset(original_url, 'Skip_url',  skip_url)

def write_url_source_redis(url, source):
	r.hset(url, 'Url_Source',  source)

def base64_encode(input):
	import base64
	return base64.b64encode( input )

def base65_decode(input):
	import base64
	return base64_b64decode( input )







