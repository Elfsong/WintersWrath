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
def work(procs):
    alloctor = function.Alloctor()  #生成装载器
    logging.debug( str(procs) + ' 生成装载器...' )
    spider = function.Sdriver()     #生成渲染器
    logging.debug( str(procs) + ' 生成渲染器...' )

    try:
        while True:
            url, level = alloctor.getUrl()
            url_data = spider.get_page(url, level)
            alloctor.update_data(url, url_data )

    except Exception as e:
        print(e)
        logging.info( str(procs) + "装载器取不到url" )
    finally:
        spider.close_driver()


if __name__ == "__main__":
    work(1)
