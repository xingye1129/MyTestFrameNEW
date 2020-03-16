# -*- coding: UTF-8 -*-
import requests, json, traceback


class HTTP:
    """
        这是整个接口测试库
        powered by xingye
        at:2020/03/15
    """

    def __init__(self,writer):
        # requests.packages.urllib3.disable_warnings()
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
        else:
            print('erro:url格式错误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'url格式错误')

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
        except Exception as e:
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))

        # print(self.result)



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
        except Exception as e:
            print('erro:没有' + key +'这个值')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
            traceback.print_exc()



    def assertequals(self, key, value):
        """
        :param key: 用来比较的键
        :param value: 实际结果参数
        :return: 断言判断
        """
        value = self.__get_param(value)
        res = self.result
        try:
            res = str(self.jsonres[key])
        except Exception as e:
            pass
        if res == str(value):
            print('Pass')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, res)
        else:
            print('Fail')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, '实际结果： ' + res + "  预期结果：" + value)

    def savejson(self, key, t):
        """

        :param key: 需要保存的参数的键
        :param t: 保存在参数为的值
        :return:
        """
        # 将需要保存的参数的，保存为参数t的值
        try:
            self.params[t] = self.jsonres[key]
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[t]))
        except Exception as e:
            print('erro:没有' + key + '这个值')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.jsonres))
            traceback.print_exc()

    # 计算处理的方法，将传入的value值作为s传入到__get_param方法中获取对应的值
    def __get_param(self, s):

        # 按规则获取关联的参数 意义的格式为{}的形式
        # 遍历保存的关联数据的字段
        for key in self.params:
            # 遍历已经保存的参数，用传入到字符串里面，满足{key}的所有字符传用它的值来替换
            s = s.replace('{' + key + '}', self.params[key])
        return s

    def __get_data(self, s):
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
                print('erro:参数传值不规范')
                traceback.print_exc()

        return dates
