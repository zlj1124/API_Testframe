'''
Descripttion: 
Author: zlj
Date: 2020-11-17 09:37:52
'''
# -*- coding: utf-8 -*-

import yaml
import configparser
from Common.Consts import DATA_PATH 

class ReadYaml(object):
  

    def __init__(self):
        
        self.yaml_path=DATA_PATH 
        self.conf = configparser.ConfigParser()

    @property
    def get_datas(self):
        with open(self.yaml_path,'r')as f:
            self.content=yaml.safe_load(f)
        return self.content
    
if __name__ == "__main__":
    redy = ReadYaml()
    print(redy.get_datas)

# """
# 定义所有测试数据

# """
# import os
# from Params import tools
# from Common import Log
# log = Log.MyLog()
# path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


# def get_parameter(name):
#     data = tools.GetPages().get_page_list()
#     param = data[name]
#     return param


# class Datas:

#     log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Datas.yaml')
#     params = get_parameter('Datas')
#     url = []
#     data = []
#     # print(params)

#     for i in range(0, len(params)):
     
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])

# if __name__ == "__main__":
#     data = Datas()     
#     data.url
  
   
