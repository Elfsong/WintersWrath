#coding:utf-8
import re
import time
import json
import redis
import logging


#################################################################################################
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='app.log',
                filemode='a')
#################################################################################################

class Updater:
    def __init__(self):
        self.url = ''   #url地址
        self.host = '35.187.193.187'    #redis服务器地址
        self.port = 6380    #redis服务端口
        self.db = 0     #redis数据库
        try:
            self.redis_db = redis.ConnectionPool(host = self.host, port = self.port, db = self.db)
            self.redis_db = redis.Redis(connection_pool = self.redis_db)
            logging.debug("Updater is already.")
        except:
            logging.error( '更新器无法连接Redis服务器，请检查配置.' )

    def get_original_url(self):
        url = self.redis_db.spop("done")
        return url

    def get_link_url(self, original_url):
        print(original_url)
        link_handler, level = self.redis_db.hmget(original_url, "link_handler", "level")

        if int(level) < 3:
            pattern = re.compile('"(.*?)"')
            for link_url in pattern.findall(str(link_handler)[2:-1]):
                print(link_url)
                if not self.redis_db.hexists(link_url,"level"):
                    data = {"url":link_url, "level":int(level)+1}
                    data = json.dumps(data)
                    self.redis_db.sadd('preparation', data)
    def get_size(self):
        size = int(self.redis_db.scard('done'))
        return size

if __name__ == "__main__":
    updater = Updater()
    flag = 0

    while flag < 3:
        size = updater.get_size()
        if size == 0:
            flag += 1
            print("未获取到元素，正在重试")
            time.sleep(2)
        else:
            while updater.get_size() > 0:
                original_url = updater.get_original_url()
                updater.get_link_url(original_url)
        pass

    print("进程退出")

