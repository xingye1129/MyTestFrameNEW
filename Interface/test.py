# -*- coding: UTF-8 -*-

# from Interface.WithInter import HTTP
# import inspect
#
#
#
# from common.test02 import HTTP
# http = HTTP()
# #登录首页
# http.post('http://47.102.153.86:8080/inter/HTTP//auth')
# print(http.result)
# http.assertequals('status','200')
#
# #保存token
# http.savejson('token','t')
# #添加信息头
# http.addheader('token','{t}')
#
# #登录
# http.post('http://47.102.153.86:8080/inter/HTTP//login',d='username=test2&password=test2')
# print(http.result)
# http.assertequals('status','200')
#
# #保存userid
# http.savejson('userid','id')
# #查询信息
# http.post('http://47.102.153.86:8080/inter/HTTP//getUserInfo',d='id={id}')
# print(http.result)
# http.assertequals('status','200')
#
# #注销
# http.post('http://47.102.153.86:8080/inter/HTTP//logout')
# print(http.result)
# http.assertequals('status','200')

# http = HTTP()
#
# func = getattr(http,'post')
# print(func)
# func('http://47.102.153.86:8080/inter/HTTP//auth')
# args = inspect.getfullargspec(func).__str__()
# print(args)
# args =args[args.find('['):args.rfind(', varargs')]
# print(type(args))
# args =eval(args)
# print(type(args))
# args.remove('self')
# print(args)
#
# # print(func.__doc__)

# -*- coding: UTF-8 -*-
import os

# a = os.path.isfile('../lib/cases/HTTP接口用例.xls')
# print(a)
# if not os.path.isfile('../lib/cases/HTTP接口用例.xls'):
#     print('www')

s ='username=test2&password=test2'
s =s.split('&')
print(s)
for ss in s:
    print(ss)
    sss =ss.split('=')
    print(sss)
#
# res = os.popen("ipconfig").read()
# print(res)

# date = []
# a = open('../conf/conf.properties',mode='r',encoding='utf8')
# print(a)
# for i in a:
#     date.append(i)
# print(date)
# print(date.__len__())
# # print(date.__getattribute__())
# for b in range(date.__len__()):
#     date[b] =date[b].encode('utf8').decode('utf-8-sig')
# # print(date)
#     date[b] = date[b].replace('\n','')
# print(date)
#
# c = open('../conf/conf.properties',mode='a',encoding='utf8')
# c.write('22222')
# c.close()

# from common.ReadTXT import Txt
# txt =Txt('../conf/conf.properties')
# date = txt.read()
# congigs ={}
# print(date)
# for s in date:
#     if s.startswith('#'):
#         continue
#
#     if not s.find('=') > 0:
#         print('peizhiwenti')
#
#     key = s[0:s.find('=')]
#     value = s[s.find('=') +1:s.__len__()]
#     congigs[key] = value
# print(congigs)

# mailto='993843278@qq.com,22333@qq.com'
# a =','.join(mailto)
# print(a)

# import jsonpath,json
# a = {'status': 405, 'msg': '非法请求'}
#
#
# res1 = jsonpath.jsonpath(a,'status')
# res2 = jsonpath.jsonpath(a,'status')[0]
# res3 = jsonpath.jsonpath(a,'$.[status]')[0]
# print(res1)
# print(res2)
# print(res3)
import os
res = os.popen('netstat -aon | findstr 4333').read()
print(res)
print(type(res))