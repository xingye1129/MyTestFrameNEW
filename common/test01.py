# -*- coding: UTF-8 -*-
import os

# a = os.path.isfile('../lib/cases/HTTP接口用例.xls')
# print(a)
# if not os.path.isfile('../lib/cases/HTTP接口用例.xls'):
#     print('www')

# s ='username=test2&password=test2'
# s =s.split('&')
# print(s)
# for ss in s:
#     print(ss)
#     sss =ss.split('=')
#     print(sss)
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

mailto='993843278@qq.com,22333@qq.com'
a =','.join(mailto)
print(a)

