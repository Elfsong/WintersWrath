import json
import urllib2
import logging
import info_log

def get_addr(ip):
    logger = logging.getLogger('root.addr')

    flag = False
    
    #first method
    try:
        url = "http://ip-api.com/json/" + ip
        #response = eval(urllib2.urlopen(url).read())
        response = json.loads(urllib2.urlopen(url).read())
        cityname = response["city"]
        flag = True
    except Exception,e:
        logging.error("Locating fault, switching the channel, please wait for a moment...") 

    #second method
    if(flag == False):
        try:
            url = "http://freegeoip.net/json/" + ip
            #response = eval(urllib2.urlopen(url).read())
            response = json.loads(urllib2.urlopen(url).read())
            cityname = response["city"]
            flag = True
        except Exception,e:
            logging.error("Locating fault, switching the channel, please wait for a moment...")     
    
    if(flag == False):
        logging.error("Locating fault, Please Confirm network is connected") 
        return -1
    else:
        return cityname
    
#test
if __name__ == "__main__":
    print get_addr("175.8.21.166") 