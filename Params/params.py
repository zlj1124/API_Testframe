# -*- coding: utf-8 -*-


"""
定义所有测试数据

"""
import os
from Params import tools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Datas:

    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Datas.yaml')
    params = get_parameter('Datas')
    url = []
    data = []
    print(params)

    for i in range(0, len(params)):
     
        url.append(params[i]['url'])
        data.append(params[i]['data'])

if __name__ == "__main__":
    data = Datas()     
    data.url
  
   
