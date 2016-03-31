
import urllib2,socket
from selenium import webdriver

url = "http://www.bclt88.com"

try:
	request = urllib2.urlopen(urllib2.Request(url, headers = {'User-Agent':'Mozilla/8.0 (compatible; MSIE 8.0; Windows 7)'}))
	socket.setdefaulttimeout(10)
	print(request.url)
except:
	print('http://about:blank')


driver = webdriver.PhantomJS('/home/elfsong/phantomjs-2.1.1/bin/phantomjs')
driver.implicitly_wait(10)

try:
	driver.get(request.url)
	print( "Current_url:"+driver.current_url )
except:
	print("Timeout!")
     
driver.get_screenshot_as_file("show.png")

