# -*- coding: UTF-8 -*-

from common.excel import *
from Interface.WithInter import HTTP
from WEB.WithWeb import Webinter
from APP.WithApp import Applib
from common import logger
from common.excelresult import Res
from common import config
from common.Mail import Email
import inspect
import datetime
from common.mysql import Mysql

"""
    这是整个自动化框架的主代码运行入口
    powered by will
    at:2020/03/15
"""


# print('暂未实现自动化框架')

# from Interface import test


def runcase(line, http):
    # 用例的第一行第二行为分组信息，不用执行，短路原则
    if len(line[0]) > 0 or len(line[1]) > 0:
        return
    func = getattr(http, line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('['):args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')

    if len(args) == 0:
        func()
        return
    if len(args) == 1:
        func(line[4])
        return
    if len(args) == 2:
        func(line[4], line[5])
        return
    if len(args) == 3:
        func(line[4], line[5], line[6])
    if len(args) == 4:
        func(line[4], line[5], line[6])



#还原数据库

config.get_config('./conf/conf.properties')
mysql = Mysql()
mysql.init_mysql('./conf/userinfo.sql')

read = Read()

casename = 'HTTP接口用例'
read.OpenExcel('./lib/cases/'+ casename +'.xls')
sheetname = read.get_sheets()

writer = Write()
writer.cope_open('./lib/cases/'+ casename +'.xls', './lib/results/result-'+ casename +'.xls')



writer.set_sheets(sheetname[0])
writer.write(1, 3, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

read.Readline()
http = None
casetype = read.Readline()[1]
if casetype == 'HTTP':
    http = HTTP(writer)
if casetype == 'WEB':
    http = Webinter(writer)
if casetype == 'APP':
    http = Applib(writer)


for sheet in sheetname:
    read.set_sheets(sheet)
    # 保持读写在一个sheet页
    writer.set_sheets(sheet)
    for i in range(read.rows):
        writer.row = i
        line = read.Readline()
        logger.info(line)
        runcase(line, http)
writer.set_sheets(sheetname[0])
writer.write(1, 4, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
writer.save_close()

# 解析结果
res = Res()
result = res.get_res('./lib/results/result-'+ casename +'.xls')
logger.info(result)
# 获取html文本

# logger.info(config.config)
html = str(config.config['mailtxt'])

# #替换html模板中的数据
html = html.replace('status', result['status'])
if result['status'] == 'FAIL':
    html = html.replace('#00d800', 'red')
else:
    pass
print(result)
html = html.replace('title', result['title'])
html = html.replace('runtype', result['runtype'])
html = html.replace('passrate', result['passrate'])
html = html.replace('casecount', result['casecount'])
html = html.replace('starttime', result['starttime'])
html = html.replace('endtime', result['endtime'])
email = Email()
email.send(html)
