#coding:utf-8
import re
import sys
import md5
import json
import time
import redis
import logging
import function
import threading
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

#################################################################################################
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='app.log',
                filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

def exeTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)
        back = func(*args, **args2)
        print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
        return back
    return newFunc

class alloctor:
    def __init__(self):
        self.url = ''   #url地址
        self.host = '35.187.193.187'    #redis服务器地址
        self.port = 6380    #redis服务端口
        self.db = 0     #redis数据库
        try:
            self.redis_db = redis.ConnectionPool(host = self.host, port = self.port, db = self.db)
            self.redis_db = redis.Redis(connection_pool = self.redis_db)
            logging.debug("Alloctor is already.")
        except:
            logging.error( '装载器无法连接Redis服务器，请检查配置.' )

    def getUrl(self):
        for times in range(3):  #预处理队列读取
            pre_url_json = self.redis_db.spop('preparation')  #弹出预处理url

            if pre_url_json is not None:
                #format: json(data = [{'url':'http://www.126.com', 'level':'1'}])
                pre_url = json.loads(pre_url_json)['url'].encode('utf-8')
                level = json.loads(pre_url_json)['level']
                logging.info( str(pre_url) + ' is selected, level is ' + level )
                return pre_url, level

            else:
                logging.error( '无法从预处理队列取得url，正在重试('+ str(times+1) +')...' )
                time.sleep(1)
                continue

        raise LookupError("无法从预处理队列取得url，请检查Redis服务器.")
        #sys.exit(0) #退出

    def update_data(self, data_name, data):
        #try:
        self.redis_db.hmset(data_name, data)
        logging.info( '数据包回传成功' )
        #except:
        #    logging.error( '数据包回传失败，请检查Redis服务器.' )


class sdriver:
    def __init__(self):
        self.JS_PATH = '/home/dumingzhex/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs'  #PhantomJS路径
        self.IMAGE_PATH = '/home/dumingzhex/Project/Argus/Image/'   #截图保存路径
        self.driver = webdriver.PhantomJS(executable_path = self.JS_PATH)
        self.driver.set_page_load_timeout(10)   #设置渲染超时时间
        self.IMAGE_NAME = md5.new()
        try:
            logging.debug("Sdriver is already.")
        except:
            logging.error( '渲染器无法连接，请检查配置.' )

    def get_page(self, url, level):
        try:
            try:
                self.driver.get(url)
            except TimeoutException:
                logging.info( '页面 ' + url + ' 加载超时，正在停止加载...' )
                self.driver.execute_script('window.stop()')

            logging.info( '开始构建回传数据包...' )

            page_source =  self.driver.page_source
            logging.info( '获取到 ' + url + ' 页面HTML' )

            link_handler = self.driver.find_elements_by_tag_name('a')
            logging.info( '获取到 ' + url + ' 链接资源' )

            self.IMAGE_NAME.update(url)
            md5_name = self.IMAGE_NAME.hexdigest()
            self.driver.save_screenshot( self.IMAGE_PATH + md5_name)
            logging.info( '获取到 ' + url + ' 截图' )

            data = self.structure_data(url, page_source, link_handler, md5_name)

        except Exception:
            print Exception
            logging.error( '页面解析错误，请检查URL是否正确.' )
            #todo：estimate worry url list

        return url, data

    def structure_data(self, original_url, page_source, link_handler, md5_name):
        url_list = []
        pattern = re.compile(r'[a-zA-z]+://[^\s]*')

        try:
            for url in link_handler:
                match_url = pattern.match( url.get_attribute("href") )
                if match_url:
                    url_list.append(match_url.group().encode('utf-8'))
        except:
            logging.info( '外链资源异常.' )

        data = { "page_source":page_source, "link_handler":url_list, "image": self.IMAGE_PATH + md5_name}

        logging.info( '回传数据包构建完成.' )
        return data

    def close_driver(self):
        self.driver.quit()

class spider(threading.Thread):
    def __init__(self, threadID, name):
        logging.info( '正在生成爬取模块...' )
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        logging.info( '爬取模块生成完毕' )

    def run(self):
        logging.debug( self.name + " 开始工作." )

        #############################################################

        alloctor = function.alloctor()  #生成装载器
        logging.info( self.name + ' 生成装载器...' )
        spider = function.sdriver()     #生成渲染器
        logging.info( self.name + ' 生成渲染器...' )

        try:
            while True:
                url, level = alloctor.getUrl()
                logging.info( self.name + ' 接单: ' +  url)
                data_name, data = spider.get_page(url, level)
                alloctor.update_data(data_name, data)
        except LookupError:
            logging.info( self.name + " 装载器无法获取URL信息，即将关闭" )
        finally:
            logging.info( self.name + ' 渲染器关闭' )
            spider.close_driver()

        #############################################################

        logging.debug( self.name + " 已退出." )
        pass
