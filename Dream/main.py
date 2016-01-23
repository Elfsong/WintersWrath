#coding:utf-8

import re
import sys
import time
import logging
import info
from termcolor import colored,cprint


def init():
    global ip
    global address
    global weather
    
    sys.stdout.write("Initalizing")
    sys.stdout.flush()
    
    ip = info.getIp()
    if(ip == -1):
        ip = "Error" 
    sys.stdout.write("..")
    sys.stdout.flush()
        
    address = info.ipToAddress(ip)
    if(address == -1):
        address = "Error" 
    sys.stdout.write("..")
    sys.stdout.flush()    
        
    weather = info.addressToWeather(address)
    if(weather == -1 or weather == -2):
        weather = "Error"        
    sys.stdout.write("..\n")
    sys.stdout.flush() 
    
def print_weather():
    try:
        Time = colored("Time: ", 'green')  
        sys.stdout.write(Time)
        sys.stdout.write( time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(weather.get('time'))) )
        sys.stdout.write("\n")
        sys.stdout.flush()   
    
        Temperature = colored("Temperature: ", 'green')  
        sys.stdout.write(Temperature)
        sys.stdout.write( str(weather.get('temp') - 273.15) + "℃")
        sys.stdout.write("\n")
        sys.stdout.flush()     
    
        Humidity = colored("Humidity: ", 'green')  
        sys.stdout.write(Humidity)
        sys.stdout.write(str(weather.get('humidity')) + "%")
        sys.stdout.write("\n")
        sys.stdout.flush()    
    
        State = colored("State: ", 'green')  
        sys.stdout.write(State)
        sys.stdout.write(weather.get('state'))
        sys.stdout.write("\n")
        sys.stdout.flush()    
    
        Pressure = colored("Pressure: ", 'green')  
        sys.stdout.write(Pressure)
        sys.stdout.write(str(weather.get('pressure')) + "mb")
        sys.stdout.write("\n")
        sys.stdout.flush()    
    
        Sunrise = colored("Sunrise: ", 'green')  
        sys.stdout.write(Sunrise)
        t = weather.get('sunrise')
        sys.stdout.write( time.strftime('%H:%M:%S',time.localtime(weather.get('sunrise'))) )
        sys.stdout.write("\n")
        sys.stdout.flush()    
    
        Sunset = colored("Sunset: ", 'green')  
        sys.stdout.write(Sunset)
        sys.stdout.write( time.strftime('%H:%M:%S',time.localtime(weather.get('sunset'))) )
        sys.stdout.write("\n")
        sys.stdout.flush()       
    
        Wind_d = colored("Wind Direction: ", 'green')  
        sys.stdout.write(Wind_d)
        sys.stdout.write(str(weather.get('wind_d')))
        sys.stdout.write("\n")
        sys.stdout.flush()    
    
        Wind_speed = colored("Wind Speed: ", 'green')  
        sys.stdout.write(Wind_speed)
        sys.stdout.write(str(weather.get('wind_speed')))
        sys.stdout.write("\n")
        sys.stdout.flush()                        
    
    except Exception,e:
        logging.error("Server abnormal:%s" % e)           

if __name__ == "__main__":
    logger = logging.getLogger()
   
    fh = logging.FileHandler('info.log')  
    #ch = logging.StreamHandler()  
     
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s -  %(message)s')  
    fh.setFormatter(formatter)  
    #ch.setFormatter(formatter)      
    
    logger.addHandler(fh)  
    #logger.addHandler(ch)      
          
    
    cprint('Welcome to Dream', 'red', 'on_blue')
    command = ""
    
    global ip
    global address
    global weather    
    init()
    
    while(command != "q"):
        title = colored('Dream ', 'blue')
        hand = colored('> ', 'blue')
        sys.stdout.write(title)
        sys.stdout.write(hand)
        sys.stdout.flush()
        command = raw_input()
        
        #ip
        if(command == "ip"):
            if(ip != "Error"):
                ip = colored(ip, 'green', 'on_blue')
            else:
                ip = info.getIp()
                if(ip != -1):
                    ip = colored(ip, 'green', 'on_blue')    
                else:
                    ip = colored("Error", 'red', 'on_blue')                  
            print ip
        
        #address  
        if(command == "address"):
            if(address != "Error"):
                address = colored(address, 'green', 'on_blue')
            else:
                address = info.ipToAddress(info.getIp())
                if(address != -1):
                    address = colored(address, 'green', 'on_blue')    
                else:
                    address = colored("Error", 'red', 'on_blue')                   
            print address
            
        #weather
        m = re.match(r"^weather(|\s(\w*))$", command)
        if(m):
            if(m.group() == "weather"):
                cityname = info.ipToAddress(info.getIp())

                if(weather == "Error"):
                    weather = info.addressToWeather(info.ipToAddress(info.getIp()))
                    if(weather == -1):
                        weather = colored("Error", 'red', 'on_blue') 
                else:
                    print_weather()
            
            elif(m.group(2) != ''):
                cityname = m.group(2)
                weather = info.addressToWeather(cityname)
                if(weather == -1):
                    weather = colored("Error", 'red', 'on_blue')                 
                else:
                    print_weather()                 
            
                       
        