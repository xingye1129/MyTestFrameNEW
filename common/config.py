# -*- coding: UTF-8 -*-
from common import logger
from common.ReadTXT import Txt

# 定义全局变量用来存储配置文件读取后，保存为键值对格式文件
config = {}


def get_config(path):
    """
    用来读取配置文件,生成字典格式
    :param path: 配置文件路径
    :return: 返回配置文件dict
    """
    global config
    # 重新获取时，先清空配置
    config.clear()

    txt = Txt(path)
    # 获取读取到列表文件
    date = txt.read()
    # print(date)
    for s in date:
        # 跳过注释
        if s.startswith('#'):
            continue
        if not s.find('=') > 0:
            logger.warring('配置文件格式错误，请检查：' + s)
        try:
            key = s[0:s.find('=')]
            value = s[s.find('=') + 1:s.__len__()]
            # 使config字典的key=value
            config[key] = value
        except Exception as e:
            logger.exception(e)

    return config


# 调试
# get_config('../conf/conf.properties')
# print(config)
