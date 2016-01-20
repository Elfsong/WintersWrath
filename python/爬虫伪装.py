#!/uesr/Desktop
#coding:utf-8

import urllib
import urllib2

def save(filename, contents): 
    fh = open(filename, 'w') 
    fh.write(contents) 
    fh.close()

if __name__ == '__main__':
    try:
        class_number = raw_input("«Î ‰»Î≤È—Ø∞‡º∂∫≈£∫")
        url = 'http://csujwc.its.csu.edu.cn/XSXJ/FB_BJXS_rpt.aspx?Sel_BJ=' + class_number
        print url
        user_agent = 'MOzilla/4.0 (compatible;MSIE 5.5;Windows NT)'
        values = {'name':'DMZ',
                  'location':'CSU',
                  'language':'Python'}
        data = urllib.urlencode(values)
        headers = {'User-Agent':user_agent}

        req = urllib2.Request(url,data,headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        
        save('result.txt', the_page)
        print 'OK!'
        print 'Info():'  
        print response.info()  
    except urllib2.URLError,e:
        print e
