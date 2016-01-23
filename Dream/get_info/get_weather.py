import json
import urllib2
import logging

def get_weather(addr):
    logger = logging.getLogger('root.weather')
    weather = {}
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + addr + "&appid=44db6a862fba0b067b1930da0d769e98"
        response = json.loads(urllib2.urlopen(url).read())
    except Exception,e:
        logging.error("Network abnormal")  
        return -1
    
    try:
        weather["time"] = response['dt']
        weather["temp"] = response['main']['temp']
        weather["humidity"] = response['main']['humidity']
        weather["state"] = response['weather'][0]['description']
        weather["pressure"] = response['main']['pressure']
        weather["sunrise"] = response['sys']['sunrise']
        weather["sunset"] = response['sys']['sunset']
        weather["wind_d"] = response['wind']['deg']
        weather["wind_speed"] = response['wind']['speed']
        
                                                  
    except Exception,e:
        logging.error("Server abnormal")  
        return -2
    
    return weather

#test
if __name__ == "__main__":
    result = get_weather("Changsha")
    humidity = result.get('humidity')
    print humidity
