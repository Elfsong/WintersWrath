import os
import sys
import md5
import requests
import urllib
import urllib2
from bs4 import BeautifulSoup

def for_one_page( url ):
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
		open('/home/elfsong/Desktop/image/'+name,'wb').write(img._content)
		print ( name + " done!")
		return True
	except e:
		print e
		print ( name + " flased!")
		return False
	pass

def get_name( url ):
	m = md5.new()
	m.update( url )
	return m.hexdigest()


if __name__ == "__main__":
	start = 1950
	end = 1960
	for page in range(start,end+1):
		print ("http://jandan.net/ooxx/page-" + str(page))
		for_one_page( "http://jandan.net/ooxx/page-" + str(page) )
	




