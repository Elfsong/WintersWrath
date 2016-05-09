import os
import sys
import md5
import time
import requests
import urllib
import urllib2
import multiprocessing
from bs4 import BeautifulSoup

def for_one_page_test( url ):
	response = urllib2.urlopen( url )
	html = response.read()
	#print html
	soup = BeautifulSoup(html)

	for img_address in soup.find_all('a'):
		if ( isinstance(img_address.get('class'), (list,str) ) and img_address.get('class')[0] == "view_img_link" ):
			try:			
				img_url = img_address.get('href')
				image_downlode( img_url )
			except:
				print ("Cannot get attr!")
				continue
			

def image_downlode( url ):
	img = requests.get( url )
	name = get_name(url)
	try:
		open('/mydata/image/'+name,'wb').write(img._content)
		print ( name + " done!")
	except e:
		print e
		print ( name + " flased!")
	pass

def get_name( url ):
	m = md5.new()
	m.update( url )
	return m.hexdigest()


if __name__ == "__main__":
	start = 1950
	end = 1960
	
	pool = multiprocessing.Pool(processes = 4)

	btime = time.time()
	
	for page in range(start,end+1):
		url = "http://jandan.net/ooxx/page-" + str(page)
		pool.apply_async(for_one_page_test, (url, ) )

	pool.close()
	pool.join()

	etime = time.time()

	print etime - btime
	
	
	




