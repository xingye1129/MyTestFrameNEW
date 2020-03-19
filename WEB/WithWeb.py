# -*- coding: UTF-8 -*-


from selenium import webdriver
import os
import time,traceback
from common.logger import logger
from selenium.webdriver.common.action_chains import ActionChains
class  Webinter:
    """
        这是整个WEB接口库
        powered by xingye
        at:2020/03/19
    """

    def __init__(self,writer):
        self.driver = None
        self.title = ''
        self.current = None
        self.all_handler = None
        self.writer = writer
        self.text = ''
        self.t = ''

    def Openbrower(self,type='Chrome',t =''):
        """
        浏览器打开的封装实例方法
        :param type: 浏览器的类型，不传值值默认为Chrome浏览器，IE为谷歌浏览器，gc为火狐浏览器
        :param t: 打开浏览器的默认等到时间
        :return: 返回driver的值
        """

        if t == '' or t == None:
            self.t = 3
        else:
            self.t = int(t)
        #Chrome浏览器
        if type == 'Chrome' or type == '':
            # 创建一个ChromeOptions的对象
            option = webdriver.ChromeOptions()
            #去掉浏览器提示框的提示
            option.add_argument('disable-infobars')

            #异常处理，获取本地用户目录，如果没获取到则使用默认的用户目录
            try:
                userdir = os.environ['USERPROFILE']
            except Exception as e:
                traceback.print_exc()
                userdir = 'C:\\Users\\Xy'
            #拼接chromer的目录
            userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
            userdir = '--user-data-dir=' + userdir
            #添加用户目录
            option.add_argument(userdir)

            # 调用谷歌浏览器
            self.driver = webdriver.Chrome(executable_path="./Web/lib/chromedriver.exe",options=option)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.driver.implicitly_wait(self.t)

        #谷歌浏览器：
        elif type == 'gc':
            self.driver = webdriver.Firefox(executable_path="./Web/lib/geckodriver.exe")
            self.driver.implicitly_wait(self.t)
            self.writer.write(self.writer.row, 7, 'PASS')
        #IE浏览器
        elif type == 'IE':
            self.driver = webdriver.Ie(executable_path='./Web/lib/IEDriverServer.exe')
            self.driver.implicitly_wait(self.t)
            self.writer.write(self.writer.row, 7, 'PASS')
        else:
            print('输入参数有误，暂无实现该浏览器的封装！')
        return self.driver


    def close(self):
        self.driver.close()

    def get(self,url):
        """
        打开URL页面
        :param url:url地址
        :return: 无
        """
        try:
            self.driver.get(url)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, url)
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)

    def click(self,xpath):
        """
        点击元素
        :param xpath:要点击元素的xpath定位
        :return: 无
        """
        try:
            re = self.driver.find_element_by_xpath(xpath).click()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)

    def input(self,xpath,content):
        """
        通过定位输入内容
        :param xpath: 输入框的xpath路径
        :param content: 要输入的内容
        :return: 无
        """
        try:

            self.driver.find_element_by_xpath(xpath)
            self.driver.find_element_by_xpath(xpath).send_keys(content)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)

    def intoiframe(self,xpath):
        """
        进入iframe框
        :param xpath:iframe所在的xpath路径
        :return: 无
        """
        try:
            self.driver.switch_to_frame(self.driver.find_element_by_xpath(xpath))
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def outiframe(self):
        """
        退出iframe页面，返回到根目录
        :return: 无
        """
        try:
            self.driver.switch_to_default_content()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def Moveto(self,xpath):
        '''
        滑动窗口到目标元素，实现翻页
        :param xpath: 目标元素的xpath路径
        :return: 无
        '''
        try:
            actions = ActionChains(self.driver)
            ele = self.driver.find_element_by_xpath(xpath)
            actions.move_to_element(ele).perform()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)


    def excutejsLeft(self,lenth):
        '''
        横行滑动滚轴
        :param y: 向右滑动的坐标长度
        :return: 无
        '''
        try:
            js = "document.documentElement.scrollLeft=" + str(lenth)
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)


    def assertequals(self,p,value):
        try:
            p = p.replace('{text}',self.text)
            if str(p) == str(value):
                self.writer.write(self.writer.row, 7, 'PASS')
            else:
                self.writer.write(self.writer.row, 7, 'FAIL')
                self.writer.write(self.writer.row, 8, '实际结果为：' + str(p) +'  预期结果为:' + value)
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))
            logger.exception(e)

    def excutejs(self,y):
        '''
        通过javascript实现向下滑动滚轴
        :param y: 向下滑动的坐标长度
        :return: 无
        '''
        try:
            js = "var q=document.documentElement.scrollTop=" + str(y)
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, logger.exception(e))


    def windowsHandler(self):
        '''
        切换窗口，并关闭当前的窗口
        :return:无
        '''
        self.current = self.driver.current_window_handle
        print(self.current)
        self.all_handler = self.driver.window_handles
        print(self.all_handler)
        try:
            if len(self.all_handler)>1 and self.current == self.all_handler[0]:
                self.driver.close()
                self.current = self.all_handler[1]
                self.driver.switch_to_window(self.current)
                self.writer.write(self.writer.row, 7, 'PASS')
            else:
                pass
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def gettitle(self):
        '''
        获取当前窗口标题
        :return: 返回当前窗口标题
        '''
        try:
            self.title =self.driver.title
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def implicitly_wait(self,outtimes):
        '''
        隐式等待
        :param outtimes: 最长等待的时间
        :return: 无
        '''
        try:
            self.driver.implicitly_wait(outtimes)
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, logger.exception(e))

    def sleep(self,s):
        try:
            time.sleep(int(s))
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))

    def gettext(self,xpath):
        try:
            self.text = self.driver.find_element_by_xpath(xpath).text
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


    def quck(self):
        try:
            self.driver.close()
            self.writer.write(self.writer.row, 7, 'PASS')
        except Exception as e:
            logger.exception(e)
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(traceback.format_exc()))


if __name__=='__main__':
    driver = Webinter()
    driver.Openbrower()
    driver.quit()