import os
import time
import sys
from urlparse import *
from selenium import webdriver

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


def clawing(mapnumber=''):
  global driver
  driver = webdriver.PhantomJS(executable_path='phantomjs')
  driver.set_window_size(1200, 900)
  print ("clawing" + str(mapnumber) + "...")

  output_file = open('output'+str(mapnumber), 'rb')
  
  for line in output_file: 
    print (line)
    url = urlparse(line)
    capture(line, "pic/" + url.netloc + ".png")

  output_file.close()
  driver.close()
  pass

def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

 
if __name__ == "__main__":
	num = sys.argv[1]
        clawing(num)
        




  
  










