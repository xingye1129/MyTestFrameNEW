# -*- coding: UTF-8 -*-

import logging
path ='..'
#create logger,输出到日志文件
logger = None

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt = '%Y-%m-%d %H:%M:%S')
#设置输出的格式
c = logging.FileHandler(path + "/lib/logs/all.log",mode='a',encoding='utf8')
logger = logging.getLogger()
#输出日志等级开关
logger.setLevel(logging.INFO)
c.setFormatter(formatter)
#将logger添加到handler里面
logger.addHandler(c)

#将日志输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)

#打印日志的级别
def debug(ss):
    global logger
    try:
        logging.debug(ss)
    except:
        return
#打印info级别的日志
def info(ss):
    try:
        logging.info(ss)
    except Exception as e:
        return
#打印warn级别的日志
def warring(ss):
    try:
        logging.warning(ss)
    except:
        return
#打印erro级别的日志
def error(ss):
    try:
        logging.error(ss)
    except:
        return
#打印异常信息
def exception(e):
    try:
        logging.exception(e)
    except:
        return

if __name__=='__main__':
    debug('wwwww')
    info('成功')
    warring('wwww')
    error('ererererer')

    try:
        print(1 + '2')
    except Exception as e:
        exception(e)