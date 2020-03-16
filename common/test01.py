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

res = os.popen("ipconfig").read()
print(res)