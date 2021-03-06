# -*- coding: UTF-8 -*-
import requests, json, traceback
from common import logger
import jsonpath

class HTTP:
    """
        这是整个接口接口库
        powered by xingye
        at:2020/03/15
    """

    def __init__(self,writer):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
        # 定义实例变量，用来保存返回utf8编码的返回值
        self.result = ''
        # 保存json格式的结果
        self.jsonres = {}
        # 用来保存关联数据的字典
        self.params = {}
        # 用来保存数据为字典模式：比如：'username=test2&password=test2'
        self.dates = {}
        self.url = ''
        #传入Write类的writer对象，用来写入测试用例
        self.writer = writer

    def seturl(self,u):
        '''
        #设置url的地址
        :param u:url的host地址
        :return:无
        '''

        if u.startswith('http') or u.startswith('https'):
            self.url = u
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.url))
            return True
        else:
            logger.error('url格式错误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'url格式错误')
            return False

    def get(self, url,params =None, encode='utf8'):

        if not (url.startswith('http') or url.startswith('https')):
            url = self.url + '/' + url + '?' + params
        else:
            url = url + '?' + params

        res = self.session.get(url, verify=False)
        try:
            self.result = res.content.decode(encode)
        except Exception as e:
            self.result = res.text
        try:
            jsons = self.result
            jsons = jsons[jsons.find('{'):jsons.rfind('}') + 1]
            self.jsonres = json.loads(jsons)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))
            return False

    def post(self, url, d=None, j=None, encode='utf8'):
        """
        发送post请求
        :param url:url路径，可以是全局的host路径+请求路径，也可以是以http,https开头的绝对请求路径
        :param d:标准的date传参
        :param j:标准的json传参
        :param encode:
        :return:

        """
        if not (url.startswith('http') or url.startswith('https')):
            url = self.url + '//' + url
        if d is None or d=='':
            pass
        else:
            d = self.__get_param(d)
            d = self.__get_data(d)

        res = self.session.post(url, d, j, verify=False)
        self.result = res.content.decode(encode)
        try:
            self.jsonres = json.loads(self.result)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            return True
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))
            return False
        # print(self.result)
        # logger.info(self.result)



    def addheader(self, key, value):
        """
        添加信息头
        :param key: 需要添加的键
        :param value:添加数据的键的值
        :return:无
        """
        value = self.__get_param(value)
        self.session.headers[key] = value
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.session.headers))
        return True

    def removeheader(self,key):
        """
        删除信息头
        :param key: 要删除的信息头的键
        :return:无
        """

        try:
            self.session.headers[key]
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
            return True
        except Exception as e:
            logger.error('没有' + key +'这个值')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
            logger.exception(e)
            return False


    def assertequals(self, key, value):
        """
        :param key: 用来比较的键
        :param value: 实际结果参数
        :return: 断言判断
        """
        value = self.__get_param(value)
        res = self.result
        try:
            res = str(jsonpath.jsonpath(self.jsonres,key)[0])
        except Exception as e:
            pass
        if res == str(value):
            logger.info('Pass')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, res)
            return True
        else:
            logger.info('Fail')
            # print(traceback.print_exc())
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际结果： ' + res + "  预期结果：" + value)
            return False

    def savejson(self, jpath, t):
        """

        :param key: 需要保存的参数的键
        :param t: 保存在参数为的值
        :return:
        """
        # 将需要保存的参数的，保存为参数t的值
        try:
            self.params[t] = str(jsonpath.jsonpath(self.jsonres,jpath)[0])
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[t]))
            return True
        except Exception as e:
            logger.error('没有' + jpath + '这个值')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            logger.exception(e)
            return False

    # 计算处理的方法，将传入的value值作为s传入到__get_param方法中获取对应的值
    def __get_param(self, s):

        # 按规则获取关联的参数 意义的格式为{}的形式
        # 遍历保存的关联数据的字段
        for key in self.params:
            # 遍历已经保存的参数，用传入到字符串里面，满足{key}的所有字符传用它的值来替换
            s = s.replace('{' + key + '}', self.params[key])
        return s

    def __get_data(self, s):

        #默认为标准的字符
        flag = False
        # 传入的参数s为'username=test2&password=test2'格式,先用&分割，结果为['username=test2', 'password=test2']

        # 用来保存数据为字典模式：比如：'username=test2&password=test2' 转化为字典模式
        dates = {}
        p = s.split('&')
        # 循环
        for pp in p:
            # 用等号分割为['username', 'test2']['password', 'test2']这个格式
            ppp = pp.split('=')
            # 保存在dates字典中
            try:
                dates[ppp[0]] = ppp[1]
            except Exception as e:
                flag = True
                logger.error('erro:参数传值不规范')
                logger.exception(e)
        if flag:
            return s.encode('utf-8')
        else:
            return dates
