import get_info.get_addr
import get_info.get_ip
import get_info.get_weather

def getIp():
    return get_info.get_ip.get_ip()

def ipToAddress(ip):
    return get_info.get_addr.get_addr(ip)

def addressToWeather(addr):
    return get_info.get_weather.get_weather(addr)


if __name__ == "__main__":
    print ipToAddress(getIp())