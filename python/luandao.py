#coding:utf-8
import sys
import time
import urllib2

from bs4 import BeautifulSoup
#from selenium import webdriver


class proxy:
	def __init__(self):
		self.ip = ''
		self.port = ''
		self.address = ''
		self.time = ''
		self.date = ''

def get(num = 1):
	global proxylist 
	proxylist = list()
	url = "http://www.kuaidaili.com/free/inha/"
	logo()

	for page in range(1,num+1):
		#driver = webdriver.PhantomJS('/home/erik/source/phantomjs-2.1.1/bin/phantomjs')
		#driver.get( url )
		#response = driver.page_source.encode("utf8")

		uurl = url + str(page)

		response = urllib2.urlopen( uurl ).read()

		soup = BeautifulSoup(response, "lxml")
		
		for tr in soup.find_all('tr'):
			temp = proxy()
			for td in tr.find_all('td'):
				title = td.get('data-title').encode('utf8')
				content = td.string.encode('utf8')
				if title == "IP":
					temp.ip = content
				elif title == "PORT":
					temp.port = content
				elif title == "位置":
					temp.address = content
				elif title == "响应速度":
					temp.time = content
				elif title == "最后验证时间":
					temp.date = content
			proxylist.append( temp )

	output()
	pass

def getlist(num = 1):
	get(num)
	return proxylist
	pass

def logo():
	from termcolor import colored
	logo = """
.____                              .___              
|    |    __ _______    ____     __| _/____    ____  
|    |   |  |  \__  \  /    \   / __ |\__  \  /  _ \ 
|    |___|  |  // __ \|   |  \ / /_/ | / __ \(  <_> )
|_______ \____/(____  /___|  / \____ |(____  /\____/ 
        \/          \/     \/       \/     \/       
----------------------------------------------------
	"""
	print colored(logo , 'blue')

def output():
	for proxy in proxylist:
		if(proxy.ip == ''):
			continue
		print (proxy.ip + ":" + proxy.port).ljust(25) + proxy.date.ljust(25) + proxy.address.ljust(40)
	pass

if __name__ == "__main__":
	if(len(sys.argv) == 1):
		page = raw_input("how much do u want : ")
		assert( int(page) < 20 )
		get(int(page))
	else:
		assert( int(sys.argv[1]) < 20 )
		get(int(sys.argv[1]))


