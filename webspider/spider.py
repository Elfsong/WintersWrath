#coding:utf-8
import time
import logging
import function
import multiprocessing
from termcolor import colored, cprint


#################################################################################################
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='app.log',
                filemode='a')
#################################################################################################

class ClockProcess(multiprocessing.Process):
    def __init__(self, number):
        multiprocessing.Process.__init__(self)
        self.number = number

    @function.exeTime
    def run(self):
        alloctor = function.Alloctor()  #生成装载器
        print(colored('生成装载器...', 'green'))
        spider = function.Sdriver()     #生成渲染器
        print(colored('生成渲染器...', 'green'))
        uploder = function.Uploder()    #生成上传器
        print(colored('生成上传器...', 'green'))

        try:
            while True:
                url, level = alloctor.getUrl()
                url_data = spider.get_page(url, level, uploder)
                alloctor.update_data(url, url_data )
        except LookupError:
            logging.info( colored('装载器无法获取URL信息，即将关闭', 'blue') )

        finally:
            logging.info( colored('渲染器关闭', 'blue') )
            spider.close_driver()
            del spider
            del alloctor

if __name__ == '__main__':
    for Proc in range(6):
        ClockProcess(Proc).start()
