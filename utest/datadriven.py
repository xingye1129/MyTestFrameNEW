# -*- coding: UTF-8 -*-
import inspect, sys, datetime
from common.excel import Read, Write


reader = Read()
writer = Write()
alllist = []
runtype = 'WEB'


# 反射获取关键字
def geffunc(line, http):
    func = None
    try:
        func = getattr(http, line[0])
    except Exception as e:
        print(e)

    return func


# 反射获取参数
def getargs(func):
    if func:
        args = inspect.getfullargspec(func).__str__()
        args = args[args.find('args=') + 5:args.find(', varargs')]
        args = eval(args)
        args.remove('self')
        l = len(args)
        return l
    else:
        return 0


# 运行一条用例
def run(func, lenargs, line):
    # 如果没有这个函数，就不执行
    if func is None:
        return

    if lenargs < 1:
        res = func()
        return res

    if lenargs < 2:
        res = func(line[1])
        return res

    if lenargs < 3:
        res = func(line[1], line[2])
        return res

    if lenargs < 4:
        res = func(line[1], line[2], line[3])
        return res
    if lenargs < 5:
        res = func(line[1], line[2], line[3])
        return res

    print('error：目前只支持3个参数的关键字')


# 选择排序
def selectSort(height):
    # 外层循环代表轮次
    l = len(height)
    for i in range(0, l):
        # 内层循环，选择最大的
        # 以第一个人为基准，记录下标
        tmp = 0
        for j in range(1, l - i):
            if str(height[tmp]) < str(height[j]):
                # 记录最大值下标
                tmp = j

        # # 把最高的放到最后
        t = height[tmp]
        height[tmp] = height[l - i - 1]
        height[l - i - 1] = t

        # 交换
        # height[tmp], height[len(height) - i - 1] = height[len(height) - i - 1], height[tmp]


def mysort(lists):
    # 用来存下标
    l = []
    # 初始化一共有多少个元素
    list1 = []
    for i in range(len(lists)):
        l.append(i)
        list1.append(i)

    selectSort(l)
    # 处理将要执行的用例
    # 把将要被执行的元素，放到unittest执行的下标位置
    for i in range(len(l)):
        list1[l[i]] = lists[i]

    return list1


def getparams(casepath, resultpath):
    global reader, writer, alllist, runtype
    reader.OpenExcel(casepath)
    # 第一行
    reader.Readline()
    # 第二行
    line = reader.Readline()
    # print(line)
    runtype = line[1]

    writer.cope_open(casepath, resultpath)
    sheetname = reader.get_sheets()
    writer.set_sheets(sheetname[0])
    writer.write(1, 3, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    for sheet in sheetname:
        # 设置当前读写的sheet页面
        reader.set_sheets(sheet)
        writer.set_sheets(sheet)
        # 默认写第7列
        writer.clo = 7
        list = [sheet, '', '', '', '', '']
        alllist.append(list)
        for i in range(reader.rows):
            list = [i]
            line = reader.Readline()
            writer.row = i
            # 如果第一列或者第二列有内容，就是分组信息，不运行
            if len(line[0]) > 0 or len(line[1]) > 0:
                pass
            else:
                list += line[2:7]
                alllist.append(list)
    # alllist = mysort(alllist)

    print(alllist)
# getparams('../lib/cases/HTTP接口用例.xls','./lib/results/HTTP接口用例.xls')


# ll = []
# for i in range(100):
#     ll.append(1)
#
# mysort(ll)
