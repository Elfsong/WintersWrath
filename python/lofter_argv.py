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
	time.sleep(10)
	return driver.page_source

def alaysis_data( html, name ):
	soup = BeautifulSoup(html)
	
	div = soup.find('div',{'class':'m-filecnt m-filecnt-1'})
	first_page = div.find('a',{'target':'_blank'})
	first_url = "http://" + name + ".lofter.com" + first_page.attrs['href'] 
	return first_url

def get_image_page( url ):
	response = urllib2.urlopen( url )
	html = response.read()
	soup = BeautifulSoup(html)

	for img_address in soup.find_all('a',{'class':'img imgclasstag'}):
		img_url = img_address.attrs['bigimgsrc'].split("?")
		img_urls.append( img_url[0] )

	for img_address in soup.find_all('a',{'class':'imgclasstag'}):
		img_url = img_address.attrs['bigimgsrc'].split("?")
		img_urls.append( img_url[0] )
	
	if( soup.find('a',{'id':'__next_permalink__'}) ):
		return soup.find('a',{'id':'__next_permalink__'}).attrs['href'] 
	else:
		return None

def get_image_url(url):
	next_page = url

	while(next_page):
		print next_page
		next_page = get_image_page( next_page )
	print next_page

def get_name( url ):
	m = md5.new()
	m.update( url )
	return m.hexdigest()

def image_downlode( url ):
	print url
	img = requests.get( url )
	img_name = get_name(url)
	try:
		open('/mydata/image/'+ name +"/"+img_name+".jpg",'wb').write(img._content)
		print ( img_name + " done!")
	except e:
		print e
		print ( img_name + " flased!")
	pass

def downlode_reducer( core_num ):
	pool = multiprocessing.Pool(processes = int(core_num) )
	for url in img_urls:
		pool.apply_async(image_downlode,(url, ) )
	pool.close()
	pool.join()
	exit()

def create_folder( name ):
	try:
		os.makedirs('/mydata/image/'+ name)
		print ("- Floder is Created -")
	except:
		print("Folder is existed!")
		
if __name__ == "__main__":
	driver = webdriver.PhantomJS('/home/erik/source/phantomjs-2.1.1/bin/phantomjs')

	img_urls = []
	
	name = sys.argv[1]
	core_num = sys.argv[2] 
	create_folder( name )
	print("Programming will be loading......")
	
	html = get_page_source( name )
	first_page = alaysis_data( html, name )

	get_image_url( first_page )
	downlode_reducer(core_num)

	driver.close()
	
	pass

