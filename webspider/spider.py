#coding:utf-8
import time
import logging
import function
import multiprocessing


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
        logging.info(  ' 生成装载器...' )
        spider = function.Sdriver()     #生成渲染器
        logging.info( ' 生成渲染器...' )

        try:
            while True:
                url, level = alloctor.getUrl()
                url_data = spider.get_page(url, level)
                alloctor.update_data(url, url_data )
        except LookupError:
            logging.info( " 装载器无法获取URL信息，即将关闭" )
        finally:
            logging.info( ' 渲染器关闭' )
            spider.close_driver()
            del spider
            del alloctor

if __name__ == '__main__':
    for Proc in range(8):
        ClockProcess(Proc).start()
