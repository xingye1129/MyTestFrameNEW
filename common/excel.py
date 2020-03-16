# -*- coding: UTF-8 -*-

import xlrd, os
from xlutils.copy import copy


class Read:

    """
    用来读取excel文件中的内容
    """

    def __init__(self):
        # 整个excel工作簿的缓存
        self.workbook = None
        # 当前sheet页
        self.sheet = None
        # 当前sheet页的总行数
        self.rows = 0
        # 当前读到的行数
        self.r = 0
        self.rows = 0

    def OpenExcel(self, srcfile):
        # 判断要打开的文件是否存在，不存在就报错
        if not os.path.isfile(srcfile):
            print('erro: %s not exist!' % srcfile)
            return
        # 设置读取excel的编码
        xlrd.Book.encoding = "utf8"
        # 读取excel的内容缓存workbook
        self.workbook = xlrd.open_workbook(srcfile)
        # 选取第一个sheet页
        self.sheet = self.workbook.sheet_by_index(0)
        # 当前sheet页下的总行数
        self.rows = self.sheet.nrows
        # # 设置默认读取为第一行
        self.r = 0
        return

    # 获取sheet页面
    def get_sheets(self):
        sheets = self.workbook.sheet_names()
        # print(sheets)
        return sheets

    # 切换sheet页面
    def set_sheets(self, name):
        # 通过sheet页的名字，切换到sheet页面
        self.sheet = self.workbook.sheet_by_name(name)
        # 获取当前sheet页面的所有行
        self.rows = self.sheet.nrows
        self.r = 0
        return

    def Readline(self):
        # 定义row1变量，用来返回没一行中每一列的值
        row1 = None

        if self.r < self.rows:
            row = self.sheet.row_values(self.r)
            self.r += 1
            # 辅助循环里面的列
            i = 0
            row1 = row
            for strs in row:
                # 读取的数据变为字符串，从列表中遍历
                row1[i] = str(strs)
                i += 1

            return row1


class Write:

    """
    用来写入的excel文件，保存在新的文件夹中
    """

    def __init__(self):
        #读取需要复制的excel，保存在workbook缓存中
        self.workbook = None
        #拷贝的工作空间
        self.wb = None
        #记录生成的文件，用来保存
        self.df = None
        #当前的sheet
        self.sheet = None
        self.row = 0
        self.col = 0

    def cope_open(self,startfile,endfile):

        if not os.path.isfile(startfile):
            print("erro:源文件" + startfile + "not exist!")
            return
        if  os.path.isfile(endfile):
            print('erro:目标文件' + endfile + "file is exist!")

        #记录要保存的文件
        self.df = endfile

        #读取到excel缓存，formatting_info带原有文件格式的形式
        self.workbook = xlrd.open_workbook(filename=startfile,formatting_info=True)

        #拷贝
        self.wb = copy(self.workbook)
        #默认使用第一个sheet
        # sheet = self.wb.get_sheet('授权接口')
        # print(sheet)


    #获取sheet页面
    def get_sheets(self):
        #获取所有sheet页的名字，并返回一个列表
        sheets = self.workbook.sheet_names()
        # print(sheets)
        return sheets


    #切换sheet页
    def set_sheets(self,name):

        #通过sheet页的名字,切换到sheet页面
        self.sheet = self.wb.get_sheet(name)

        return self.sheet

    def write(self, row, col, value):
        """ Change cell value without changing formatting. """

        def _getOutCell(sheet, rowIndex, colIndex):
            """ HACK: Extract the internal xlwt cell representation. """
            row = sheet._Worksheet__rows.get(rowIndex)
            if not row:
                return None
            #获取单元格
            cell = row._Row__cells.get(colIndex)
            return cell

        # HACK to retain cell style.
        previousCell = _getOutCell(self.sheet, row, col)
        # END HACK, PART I
        # 写入值
        self.sheet.write(row, col, value)

        # HACK, PART II
        if previousCell:
            newCell = _getOutCell(self.sheet, col, row)
            # 设置写入后格式和写入前一样
            if newCell:
                newCell.xf_idx = previousCell.xf_idx

        return col

    def save_close(self):

        self.wb.save(self.df)



if __name__ == '__main__':

    read = Read()
    read.OpenExcel('../lib/cases/HTTP接口用例.xls')
    sheetname = read.get_sheets()
    print(sheetname)
    for sheet in sheetname:
        read.set_sheets(sheet)
        for i in range(read.rows):
            print(read.Readline())
    writer = Write()
    writer.cope_open('../lib/cases/HTTP接口用例.xls', '../lib/results/result-HTTP接口用例.xls')
    sheetname = writer.get_sheets()
    writer.set_sheets(sheetname[0])
    writer.write(1,1,'xingye')
    writer.save_close()

