#coding:utf-8
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

    def get_link_url(self, original_url):
        print original_url
        link_handler, level = self.redis_db.hmget(original_url, "link_handler", "level")
        print level

        for link_url in link_handler:
            print link_url
            if not self.redis_db.hexists(link_url,"level"):
                data = {"url":"link_url", "level":int(level)+1}
                data = json.dumps(data)
                self.redis_db.sadd('preparation', data)


updater = Updater()
original_url = updater.get_original_url()
updater.get_link_url(original_url)

