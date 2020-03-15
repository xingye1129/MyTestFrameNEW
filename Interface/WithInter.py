# -*- coding: UTF-8 -*-
import requests,json

class HTTP:
    """
        这是整个接口测试库
        powered by xingye
        at:2020/03/15
    """

    def __init__(self):
        self.session = requests.session()
        #定义实例变量，用来保存返回utf8编码的返回值
        self.result = ''
        #保存json格式的结果
        self.jsonres = {}
        #用来保存关联数据的字典
        self.params = {}
        #用来保存数据为字典模式：比如：'username=test2&password=test2'
        self.dates = {}

    def post(self,url,d=None,j=None,encode='utf8'):
        if d is None:
            pass
        else:
            d = self.__get_param(d)
            d = self.__get_data(d)

        res = self.session.post(url,d,j)
        self.result = res.content.decode(encode)
        self.jsonres = json.loads(self.result)

    def addheader(self,key,value):
        value = self.__get_param(value)
        self.session.headers[key] = value

    def assertequals(self,key,value):
        """
        :param key: 用来比较的键
        :param value: 传入要关联的值（从响应中获取的）传入格式为{}形式的
        :return: 断言判断
        """
        if str(self.jsonres[key]) == str(value):
            print('Pass')
        else:
            print('Fail')

    def savejson(self,key,t):
        """

        :param key: 需要保存的参数的键
        :param t: 保存在参数为p的值
        :return:
        """
        #将需要保存的参数的，保存为参数t的值
        self.params[t] = self.jsonres[key]

    #计算处理的方法，将传入的value值作为s传入到__get_param方法中获取对应的值
    def __get_param(self,s):

        #按规则获取关联的参数 意义的格式为{}的形式
        #遍历保存的关联数据的字段
        for key in self.params:
            #遍历已经保存的参数，用传入到字符串里面，满足{key}的所有字符传用它的值来替换
            s = s.replace('{'+key+'}',self.params[key])
        return s

    def __get_data(self,s):
        #传入的参数s为'username=test2&password=test2'格式,先用&分割，结果为['username=test2', 'password=test2']
        p =s.split('&')
        #循环
        for pp in p:
            #用等号分割为['username', 'test2']['password', 'test2']这个格式
            ppp =pp.split('=')
            #保存在dates字典中
            self.dates[ppp[0]] = ppp[1]
        return self.dates






