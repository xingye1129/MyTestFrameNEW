# -*- coding: UTF-8 -*-

from common.excel import *
from Interface.WithInter import HTTP
import inspect

"""
    这是整个自动化框架的主代码运行入口
    powered by will
    at:2020/03/15
"""

# print('暂未实现自动化框架')

# from Interface import test



def runcase(line,http):
    #用例的第一行第二行为分组信息，不用执行，短路原则
    if len(line[0]) > 0 or len(line[1]) > 0:
        return
    func = getattr(http, line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('['):args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')

    if len(args) == 0:
        return
    if len(args) == 1:
        func(line[4])
        return
    if len(args) == 2:
        func(line[4],line[5])
        return
    if len(args) == 3:
        func(line[4],line[5],line[6])
    if len(args) == 4:
        func(line[4],line[5],line[6])




read = Read()
read.OpenExcel('./lib/cases/HTTP接口用例.xls')
sheetname = read.get_sheets()

writer = Write()
writer.cope_open('./lib/cases/HTTP接口用例.xls', './lib/results/result-HTTP接口用例.xls')
http = HTTP(writer)



for sheet in sheetname:
    read.set_sheets(sheet)
    #保持读写在一个sheet页
    writer.set_sheets(sheet)
    for i in range(read.rows):
        writer.row = i
        line = read.Readline()
        print(line)
        runcase(line, http)

writer.save_close()