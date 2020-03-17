# -*- coding: UTF-8 -*-
from common import logger


class Txt:

    # 构造函数打开txt
    def __init__(self, path, mode='r', coding='utf8'):
        # 定义一个列表，用来保存读取到的值
        self.date = []
        # 写入后文件缓存
        self.f = None

        if mode == 'r':
            for line in open(path, encoding=coding):
                self.date.append(line)
            # 去掉末尾的换行
            for i in range(self.date.__len__()):
                # 处理非法字符串
                self.date[i] = self.date[i].encode(coding).decode('utf-8-sig')
                # 去掉末尾的换行
                self.date[i] = self.date[i].replace('\n', '')
            return

        if mode == 'w':
            # 打开可写文件，mode=a代表在末尾追加
            self.f = open(path, mode='a', encoding=coding)
            return

        if mode == 'rw':
            # 打开可写可写文件，读取全部并追加，mode=a代表在末尾追加
            for line in open(path, encoding=coding):
                self.date.append(line)
            # 去掉换行
            for i in range(self.date.__len__()):
                self.date[i] = self.date[i].encode(coding).decode('utf-8-sig')
                self.date[i] = self.date[i].replace('\n', '')
            self.f = open(path, 'a', encoding=coding)
            return

    # 读取
    def read(self):
        """
        将txt文件格式按行读取，并储存未列表
        :return: 返回txt所有内容的列表
        """
        return self.date

    def writeline(self, s):
        """
        往txt文件末尾写入一行
        :param s:需要写入的内容，如果需要换行自己添加\n
        :return:无
        """
        if self.f is None:
            logger.error("未打开可写入txt文件")
        self.f.write(str(s))

    # 保存
    def sava_close(self):
        """
        写入文件后，必须要保存
        :return: 无
        """
        if self.f is None:
            logger.error("未打开可写入txt文件")
        self.f.close()


if __name__ == '__main__':
    txt = Txt('../conf/conf.properties', mode='r')
    t = txt.read()
    print(t)

    # write = Txt('../conf/conf.properties', mode='rw')
    # write.writeline('\nmail_enco=utf8')
    # write.sava_close()
