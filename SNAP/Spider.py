#coding = utf-8
import time
import logging
import comm
from urlparse import *
from selenium import webdriver

############################################################################################
def set_logging():
	logging.basicConfig(level=logging.DEBUG,
	                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	                datefmt='%a, %d %b %Y %H:%M:%S',
	                filename='Spider.log',
	                filemode='w')
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
	console.setFormatter(formatter)
	logging.getLogger('').addHandler(console)
############################################################################################

def claw_url(url):
	if(url != ''):
		url_info = urlparse(url)
		start = time.clock()
		driver.get(url)
		driver.get_screenshot_as_file("pic/"+url_info.netloc[:-1]+".png")
		end = time.clock()
		print( driver.title + " Done with %0.3f seconds\n" % (end - start) )

def get_input(filename):
	input = open(filename)

	for line in input:
		claw_url(line)

if __name__ == "__main__":
	set_logging()
	
	driver = webdriver.PhantomJS()

	get_input("input.txt")
	
	print(comm.get_url_info("www.123.edu.cn", 2))

	driver.quit()
