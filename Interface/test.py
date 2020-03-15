# -*- coding: UTF-8 -*-

from Interface.WithInter import HTTP



http = HTTP()
#登录首页
http.post('http://47.102.153.86:8080/inter/HTTP//auth')
http.assertequals('status','200')

#保存token
http.savejson('token','t')
#添加信息头
http.addheader('token','{t}')

#登录
http.post('http://47.102.153.86:8080/inter/HTTP//login',d='username=test2&password=test2')
http.assertequals('status','200')

#保存userid
http.savejson('userid','id')
#查询信息
http.post('http://47.102.153.86:8080/inter/HTTP//getUserInfo',d='id={id}')
http.assertequals('status','200')

#注销
http.post('http://47.102.153.86:8080/inter/HTTP//logout')
http.assertequals('status','200')
