#coding:utf-8
import time
import logging
import function

#################################################################################################
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='app.log',
                filemode='a')
#################################################################################################



@function.exeTime
def work():
    spider1 = function.spider(1, "spider-1")
    spider2 = function.spider(2, "spider-2")

    spider1.start()
    spider2.start()

    spider1.join()
    spider2.join()

if __name__ == "__main__":
    work()
    logging.debug( "主进程退出." )
