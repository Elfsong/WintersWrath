import re
import urllib2
import logging

def get_ip():
    logger = logging.getLogger('root.ip')
    try:
        return re.search('\d+\.\d+\.\d+\.\d+', urllib2.urlopen("http://www.whereismyip.com").read()).group(0)
    except:
        logging.error("Network abnormal") 
        return -1
    
#test
if __name__ == "__main__":
    result = get_ip()
    print result