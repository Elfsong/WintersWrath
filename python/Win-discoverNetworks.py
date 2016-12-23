#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import optparse
import mechanize
import urllib
import re
import urlparse
import json
import _winreg

def val2addr(val):
    addr = ''
    for ch in val:
        addr += '%02x ' % ord(ch)
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr


def wiglePrint(username, password, netid):
    browser = mechanize.Browser()
    browser.open('https://wigle.net/')
    reqData = urllib.urlencode({'credential_0': username, 'credential_1': password})
    browser.open('https://wigle.net/gps/gps/main/confirmquery', reqData)
    
    params = {}
    params['netid'] = netid
    reqParams = urllib.urlencode(params)
    
    resp = browser.open('https://api.wigle.net/api/v2/network/search?first=0&netid=' + netid).read()

    data = json.loads(resp)
    
    mapLat = 'N/A'
    mapLon = 'N/A'
    rLat = data['results'][0].get('trilat', None)
    if rLat:
        mapLat = rLat
    rLon = ata['results'][0].get('trilong', None)
    if rLon:
        mapLon = rLon
    print '[-] Lat: ' + mapLat + ', Lon: ' + mapLon


def printNets(username, password):
    keypath = r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged"
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keypath)

    print ('[*] Networks you have joined.')

    for i in range(1):
	try:
	    guid = _winreg.EnumKey(key, i)
	    netKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keypath+r"\\"+str(guid))
			
	    (n, addr, t) = _winreg.EnumValue(netKey, 0)
	    (n, name, t) = _winreg.EnumValue(netKey, 1)

	    macAddr = val2addr(addr)
			
	    print (' [+] ' + name + ' ' + macAddr)

	    #wiglePrint(username, password, macAddr)
            _winreg.CloseKey(netKey)

	except Exception, e:
            print e
	    break

def main():
    parser = optparse.OptionParser('usage %prog '+\
      '-u <wigle username> -p <wigle password>')
    parser.add_option('-u', dest='username', type='string',
                      help='specify wigle password')
    parser.add_option('-p', dest='password', type='string',
                      help='specify wigle username')
    (options, args) = parser.parse_args()
    username = options.username
    password = options.password
    if username == None or password == None:
        print parser.usage
        exit(0)
    else:
        printNets(username, password)


if __name__ == '__main__':
    main()
