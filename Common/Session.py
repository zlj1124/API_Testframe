# -*- coding: utf-8 -*-


"""
封装获取cookie方法

"""

import requests
import json
from Common import Log
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self, env='qiye6'):
        """
        获取session
        :param env: 环境变量
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
                    
           
            "Content-Type": "application/json;charset=UTF-8"
        }
        
        if env == 'qiye6':
            
            parm={"username":"10086","password":"rootroot"}    
            session = requests.session()
 
            response = session.post(url='http://192.168.3.21:30236/auth/login/', json=parm, headers=headers)
          
          
            auth = "JWT " + response.json()["token"]
        
            # print(response.cookies.get_dict())          
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session()