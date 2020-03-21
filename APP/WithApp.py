# -*- coding: UTF-8 -*-
from appium import webdriver
from common import logger
import os,time
import traceback,threading


class Applib:
    """
        这是整个WEB接口库
        powered by xingye
        at:2020/03/20
    """

    def __init__(self, writer):

        self.driver = None
        # 返回保存的定位信息
        self.ele = ''
        self.writer = writer
        self.port = 4723

    def runappium(self,path, port='',t =''):
        """
        启动appium服务
        :param path:appium的安装路径，可以写全路径
        :param port:启动appium的端口
        :param t:等待时间
        :return:
        """

        try:
            if path =='':
                cmd = 'node C:\\Users\\Xy\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            else:
                cmd = 'node ' + path + '\\resources\\app\\node_modules\\appium\\build\\lib\\main.js'
            if port == '':
                cmd += ' -p 4723'
            else:
                self.port = port
                cmd += ' -p' + port

            if t =='':
                t = 5
            else:
                t = int(t)
            #启动appium服务
            def run(cmd):
                try:
                    os.popen(cmd).read()
                except Exception as e:
                    pass

            th= threading.Thread(target=run, args=(cmd,))
            th.start()
            time.sleep(t)
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())
            logger.exception(e)





    def runapp(self, conf, t=''):
        """
        连接appium服务器，并根据conf配置，启动待测试APP
        :param conf:APP的启动配置，为标准json字符串
        :param port:启动appium的端口
        :param t:默认等待实际
        :return:无
        """
        try:
            if t == '' or t is None:
                self.t = 15
            else:
                self.t = int(t)

            conf = eval(conf)

            self.driver = webdriver.Remote('http://127.0.0.1:'+ self.port + '/wd/hub', conf)
            self.driver.implicitly_wait(self.t)
            self.writer.write(self.writer.row, 7, "PASS")

        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())
            logger.exception(e)

    def __findele(self, xpath):
        """
        定位元素
        :param xpath:元素的定位路径，支持accessibility_id，id，xpath
        :return:找到的元素，如没找到，就返回None
        """

        if xpath.startswith('//'):
            self.ele = self.driver.self.driver.find_element_by_xpath(xpath)
        else:
            try:
                self.ele = self.driver.find_element_by_accessibility_id(xpath)
            except Exception as e:
                self.ele = self.driver.find_element_by_id(xpath)

        return self.ele

    def input(self, xpath, coment):
        """
        输入内容
        :param xpath: 定位的xpath路径
        :param coment: 输入的内容
        :return:
        """

        ele = self.__findele(xpath)
        try:
            if ele is None:
                logger.error('NO such element' + xpath)
            else:
                ele.clear()
                ele.send_keys(coment)
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())
            logger.exception(e)

    def click(self, xpath):
        """
        点击元素
        :param xpath: 定位的xpath路径
        :return: 无
        """

        try:
            ele = self.__findele(xpath)
            if ele is None:
                logger.error('NO such element' + xpath)
            else:
                ele.click()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.writer(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())
            logger.exception(e)

    def closeappium(self):
        """
        杀掉appium进程
        :return:
        """
        try:
            os.popen('taskkill /F /IM node.exe')
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())

    def quit(self):
        """
        退出app
        :return: 无
        """
        try:
            self.driver.quit()
            self.writer.write(self.writer.row, 7, "PASS")
        except Exception as e:
            self.writer.write(self.writer.row, 7, "FAIL")
            self.writer.write(self.writer.row, 8, traceback.print_exc())
            logger.exception(e)

