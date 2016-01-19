# -*- coding: cp936 -*-
import logging
# 创建一个logger
logger = logging.getLogger('__name__')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
file_h = logging.FileHandler('test.log')
file_h.setLevel(logging.DEBUG)
# 创建一个handler，用于输出到控制台
console_h = logging.StreamHandler()
console_h.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')
file_h.setFormatter(formatter)
console_h.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(file_h)
logger.addHandler(console_h)
# 记录一条日志
logger.info('Info')
logger.debug('Debug')
