# -*- coding: UTF-8 -*-

from Interface.WithInter import HTTP
import inspect


http = HTTP()
#登录首页
http.post('http://47.102.153.86:8080/inter/HTTP//auth')
print(http.result)
http.assertequals('status','200')

#保存token
http.savejson('token','t')
#添加信息头
http.addheader('token','{t}')

#登录
http.post('http://47.102.153.86:8080/inter/HTTP//login',d='username=test2&password=test2')
print(http.result)
http.assertequals('status','200')

#保存userid
http.savejson('userid','id')
#查询信息
http.post('http://47.102.153.86:8080/inter/HTTP//getUserInfo',d='id={id}')
print(http.result)
http.assertequals('status','200')

#注销
http.post('http://47.102.153.86:8080/inter/HTTP//logout')
print(http.result)
http.assertequals('status','200')

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

