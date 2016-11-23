import os
import sys
import time
import requests
import md5
import urllib
import urllib2
import multiprocessing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def get_page_source( name ):
	driver.maximize_window()
	driver.get( "http://" + name + ".lofter.com/view" )
	time.sleep(10) #等待页面加载完成
	#其实Selenium有智能等待的功能，但是我看了相关的API之后感觉不是特别好用
	#如果有人有好的方法可以优雅地解决这个问题，请私信告诉我，谢谢。
	return driver.page_source

def alaysis_data( html, name ):
	soup = BeautifulSoup(html)  #创建Soup对象
	
	div = soup.find('div',{'class':'m-filecnt m-filecnt-1'})
	first_page = div.find('a',{'target':'_blank'})
	first_url = "http://" + name + ".lofter.com" + first_page.attrs['href'] 
	return first_url

def get_image_page( url ):
	response = urllib2.urlopen( url )
	html = response.read()
	soup = BeautifulSoup(html)
	
	#这里使用了BeautifulSoup对爬取下来的页面进行了分析处理，过滤出了所有图片的资源地址。

	for img_address in soup.find_all('a',{'class':'img imgclasstag'}):
		img_url = img_address.attrs['bigimgsrc'].split("?")
		img_urls.append( img_url[0] )

	for img_address in soup.find_all('a',{'class':'imgclasstag'}):
		img_url = img_address.attrs['bigimgsrc'].split("?")
		img_urls.append( img_url[0] )
	
	#如果还有新的资源页，继续向下跟踪爬取。
	if( soup.find('a',{'id':'__next_permalink__'}) ):
		return soup.find('a',{'id':'__next_permalink__'}).attrs['href'] 
	else:
		return None

def get_image_url(url):
	next_page = url
	#获取每一个资源页上面的所有图片资源地址
	while(next_page):
		print next_page
		next_page = get_image_page( next_page )
	print next_page

def get_name( url ):
	m = md5.new()
	m.update( url )	#根据资源地址生成MD5
	return m.hexdigest()

def image_downlode( url ):
	print url
	img = requests.get( url )  #下载图片
	img_name = get_name(url)
	try:
		open('图片存储路径'+ name +"/"+img_name,'wb').write(img._content)	#保存图片
		print ( img_name + " done!")
	except e:
		print e	#下载失败
		print ( img_name + " flased!")
	pass

def downlode_reducer( core_num ):
	pool = multiprocessing.Pool(processes = int(core_num) )
	for url in img_urls:
		pool.apply_async(image_downlode,(url, ) )  #将下载任务分配给进程
	pool.close()
	pool.join()  #阻塞等待
	exit()

def create_folder( name ):
	try:
		os.makedirs('/mydata/image/'+ name) #创建文件夹
		print ("- Floder is Created -")	
	except:
		print("Error")
		
if __name__ == "__main__":
	driver = webdriver.PhantomJS('phantomjs执行地址')

	img_urls = []
	
	name = raw_input("Please input Lofter ID: ")	#需要爬取的lofter用户ID
	core_num = raw_input("Please input multiprecessing number: ")	#需要使用的进程数量
	create_folder( name )	#创建该Lofter ID的文件夹
	print("Programming will be loading......")
	
	html = get_page_source( name )	#获取用户首页地址
	first_page = alaysis_data( html, name )	#获得用户首页URL

	get_image_url( first_page )  #获取用户所有图片资源URL
	downlode_reducer(core_num)  #分配下载任务
	
	pass

