import unittest,datetime,time
from parameterized import parameterized
from WEB.WithWeb import Webinter
from APP.WithApp import Applib
from Interface.WithInter import HTTP
from utest import datadriven
from common import logger


class TestWeb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = None
        if datadriven.runtype == 'WEB':
            cls.obj = Webinter(datadriven.writer)

        if datadriven.runtype == 'APP':
            cls.obj = Applib(datadriven.writer)

        if datadriven.runtype == 'HTTP':
            cls.obj = HTTP(datadriven.writer)

    # 关键字执行
    @parameterized.expand(datadriven.alllist)
    def test_all(self,index, name, key, param1, param2, param3):
        """"""
        # print(name)
        # 标识是否运行
        flg = False
        try:
            index = int(index)
            # 设置当前执行写入的行数
            datadriven.writer.row = index
            # 如果不是sheet就运行
            flg = True
        except:
            # 如果是sheet，就切换写入的sheet页面，不执行
            datadriven.writer.set_sheets(index)

        # 如果需要运行用例
        if flg:
            line = [key, param1, param2, param3]
            logger.info(line)
            func = datadriven.geffunc(line, self.obj)
            # print(func)
            lenargs = datadriven.getargs(func)
            # print(lenargs)
            # 反射执行
            res = datadriven.run(func, lenargs, line)

            if res == False:
                self.fail('关键字执行失败')

