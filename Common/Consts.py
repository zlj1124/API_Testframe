'''
Descripttion: 
Author: zlj
Date: 2020-11-17 09:37:52
'''
# -*- coding: utf-8 -*-

import os
"""
接口全局变量

"""

# 接口全局配置
API_ENVIRONMENT= 'jac'
# API_ENVIRONMENT_hz = 'hz'

# 接口响应时间list，单位毫秒
STRESS_LIST = []

# 接口执行结果list
RESULT_LIST = []
# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
 # ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'Conf', 'config.ini')
# 测试数据所在目录
DATA_PATH = os.path.join(ROOT_DIR, 'Params', 'Datas.yaml')


