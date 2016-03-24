#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import threading
from urlparse import *
from selenium import webdriver

class myThread (threading.Thread): 
    def __init__(self, threadID, url):
	threading.Thread.__init__(self)
	self.threadID = threadID
	self.url = url

    def run(self):
	print "Starting " + self.url
	clawing(url)
	print "Exiting " + self.url

def capture(url = "about:blank", save_name = "default.png"):
  driver.get(url)
  driver.execute_script("""
      (function () {
        var y = 0;
        var step = 100;
        window.scroll(0, 0);
 
        function f() {
          if (y < document.body.scrollHeight) {
            y += step;
            window.scroll(0, y);
            setTimeout(f, 50);
          } else {
            window.scroll(0, 0);
            document.title += "scroll-done";
          }
        }
 
        setTimeout(f, 500);
      })();
  """)
 
  for i in xrange(10):
    if "scroll-done" in driver.title:
      break
    time.sleep(1)
 
  driver.save_screenshot(save_name)

  pass

def clawing(uelset):
  print ("clawing...")

  for line in urlset: 
    print (line)
    url = urlparse(line)
    capture(line, "pic/" + url.netloc + ".png")

  output_file.close()
  
  pass

if __name__ == "__main__":
    driver = webdriver.PhantomJS(executable_path='phantomjs')
    driver.set_window_size(1200, 900)
    
    output_file = open('output', 'rb')
    
    webmap = {}
    website = []
    reduce0 = []
    reduce1 = []
    reduce2 = []
    reduce3 = []
    reduce4 = []
    
    for line in output_file:
	website.append(line)
	
    webset = set(website)
    
    count = 0
    for weburl in webset:
       url =  weburl[:-1]
       num = count % 5
       webmap[url] = num
       count = count + 1
       
    for reduce in webmap:
       if webmap[reduce] == 0:
	    reduce0.append(reduce)
       if webmap[reduce] == 1:
	    reduce1.append(reduce)
       if webmap[reduce] == 2:
	    reduce2.append(reduce)
       if webmap[reduce] == 3:
	    reduce3.append(reduce)
       if webmap[reduce] == 4:
	    reduce4.append(reduce)

    thread1 = myThread(1, reduce0)
    thread2 = myThread(2, reduce1)  
    thread3 = myThread(3, reduce2)   
    thread4 = myThread(4, reduce3)   
    thread5 = myThread(5, reduce4)      
    
    thread1.start()
    thread2.start()    
    thread3.start()
    thread4.start()    
    thread5.start()
    
    driver.close()    
    
    pass
    
    
    
    
    
	    
    
    








    
