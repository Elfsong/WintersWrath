#coding:utf-8
import sys
import time
import urllib2

from bs4 import BeautifulSoup
from selenium import webdriver


class proxy:
	def __init__(self):
		self.ip = ''
		self.port = ''
		self.address = ''
		self.time = ''
		self.date = ''

def spider():
	global proxylist 
	proxylist = []

	driver = webdriver.PhantomJS('/home/erik/source/phantomjs-2.1.1/bin/phantomjs')
	url = "http://www.kuaidaili.com/free/inha/"
	driver.get( url )
	response = driver.page_source.encode("utf8")

	soup = BeautifulSoup(response)
	
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

	return proxylist
	pass


if __name__ == "__main__":
	spider()


