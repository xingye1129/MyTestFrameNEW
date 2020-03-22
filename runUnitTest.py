# -*- coding: UTF-8 -*-
import datetime
import unittest,sys
from BeautifulReport import BeautifulReport as bf
from utest import datadriven
from common import config
from common.mysql import Mysql
from common import logger
from common.Mail import Email
from common.excelresult import Res

# 运行的相对路径
path = '.'
# 用例路径
casepath = ''
resultpath = ''

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testWeb))
    # suite = unittest.defaultTestLoader.discover(".", pattern="baidu.py", top_level_dir=None)
    # # 生成执行用例的对象
    # runner = bf(suite)
    # runner.report(filename='./test.html', description='这个描述参数是必填的')

    try:
        casepath = sys.argv[1]

    except:
        casepath = ''
    # 为空，则使用默认的
    if casepath == '':
        casepath = path + '/lib/cases/HTTP接口用例.xls'
        resultpath = path + '/lib/results/result-HTTP接口用例.xls'
    else:
        # 如果是绝对路径，就使用绝对路径
        if casepath.find(':') >= 0:
            # 获取用例文件名
            resultpath = path + '/lib/cases/result-' + casepath[casepath.rfind('\\') + 1:]
        else:
            logger.error('非法用例路径')
    # print(path)
    config.get_config(path + '/conf/conf.properties')

    # logger.info(config.config)
    mysql = Mysql()
    mysql.init_mysql(path + '/conf/userinfo.sql')
    datadriven.getparams(casepath,resultpath)

    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(baidu))
    suite = unittest.defaultTestLoader.discover("./utest/", pattern="WebTest.py", top_level_dir=None)
    # 生成执行用例的对象
    runner = bf(suite)
    runner.report(filename='./test.html', description='自动化测试报告')

    sheetname= datadriven.writer.get_sheets()
    datadriven.writer.set_sheets(sheetname[0])
    datadriven.writer.write(1, 4, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    datadriven.writer.save_close()

    res = Res()
    result = res.get_res('./lib/results/result-HTTP接口用例.xls')
    logger.info(result)
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

