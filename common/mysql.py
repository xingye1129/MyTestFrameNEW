# -*- coding: UTF-8 -*-
import pymysql
from common import logger
from common import config


class Mysql:
    def __init__(self):
        self.mysql_config = {
           'mysqluser' : "root",
           'mysqlpassword' : "xy123456",
           'mysqlport' : "3306",
           'mysqlhost' : "47.102.153.86",
           'mysqldb' : "test_project",
           'mysqlcharset' : "utf8"
        }
        for key in self.mysql_config:
            try:
                self.mysql_config[key] = config.config[key]
            except Exception as e:
                logger.exception(e)
        # 把端口处理int类型
        try:
            self.mysql_config['mysqlport'] = int(config.config['mysqlport'])
        except Exception as e:
            logger.exception(e)

    # 处理.sql文件为sql语句，并存储在列表中
    def __read_sql_file(self,filepath):
        sql_list = []
        with open(filepath,'r',encoding='utf8') as f:
            # 逐行读取和处理SQL文件
            for line in f.readlines():
                # 如果是配置数据库的SQL语句，就去掉末尾的换行
                if line.startswith('SET'):
                    sql_list.append(line.replace('\n',''))
                    # 如果是删除表的语句，则改成删除表中的数据
                elif line.startswith('DROP'):
                    sql_list.append(line.replace('DROP', 'TRUNCATE').replace('IF EXISTS', '').replace('\n',''))
                    # 如果是插入语句，也删除末尾的换行
                elif line.startswith('INSERT'):
                    sql_list.append(line.replace('\n',''))
                # 如果是其他语句，就忽略
                else:
                    pass
        return sql_list



    #初始化数据库

    def init_mysql(self,filepath):
        # 创建连接，执行语句的时候是在这里连接
        connect = pymysql.connect(
            user = self.mysql_config['mysqluser'],
            password = self.mysql_config['mysqlpassword'],
            port = self.mysql_config['mysqlport'],
            host = self.mysql_config['mysqlhost'],
            db = self.mysql_config['mysqldb'],
            charset = self.mysql_config['mysqlcharset']
        )
        # 获取游标
        cursor = connect.cursor()
        logger.info("正在连接恢复%s数据库" % filepath)
        #一步步执行sql
        for sql in self.__read_sql_file(filepath):
            cursor.execute(sql)
            connect.commit()
        cursor.execute("DELETE from userinfo where username = 'xin';")
        connect.commit()
        cursor.execute("select * from userinfo;")
        #打印表结果
        # print(cursor.description)
        # 打印表信息
        fet =cursor.fetchall()
        # print(fet)
        # serch =[]
        # col =[]
        # for line in fet:
        #     for i in line:
        #         col.append(i)
        # serch.append(col)
        # print(serch)
        connect.commit()
        # 关闭游标和连接
        cursor.close()
        connect.close()
        logger.info('数据更新成功')



if __name__=='__main__':
    config.get_config('../conf/conf.properties')
    mysql = Mysql()
    mysql.init_mysql('../conf/userinfo.sql')
