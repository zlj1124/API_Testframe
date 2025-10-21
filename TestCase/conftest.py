'''
Descripttion: 
Author: zlj
Date: 2020-11-23 09:38:40
'''
# -*- coding: utf-8 -*-


"""

# @allure.feature # 用于定义被测试的功能，被测产品的需求点
# @allure.story # 用于定义被测功能的用户场景，即子功能点
# @allure.severity #用于定义用例优先级
# @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
# @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

# @allure.attach # 用于向测试报告中输入一些附加的信息，通常是一些测试数据信息
# @pytest.allure.step # 用于将一些通用的函数作为测试步骤输出到报告，调用此函数的地方会向报告中输出步骤
# allure.environment(environment=env) #用于定义environment

"""

import allure
import pytest
import requests
from Common import Consts
from Params.parseYaml import ReadYaml
tl = ReadYaml()
from Common.DB_sql import DbConnect
local_db=DbConnect()

from Common.Send_Request import Request

# @pytest.fixture()
# def action():
#     # 定义环境 
#     env = Consts.API_ENVIRONMEN
#     # 定义报告中environment
#     # conf = Config()
#     # host = conf.host
#     # tester = conf.tester
#     # allure.environment(environment=env)
#     # allure.environment(hostname=host)
#     # allure.environment(tester=tester)
#     return env

@pytest.fixture(scope="module")  # 作用域：模块内共享（可根据需求调整为 session/class）
def case_data():
    return {}  # 空字典，用于存储用例间传递的参数

@pytest.fixture(scope="session")
def api_client():
    """创建一个全局的 requset 实例（基础配置）"""
    # base_url = "https://xxx.com"
    request =Request()
    
    return request



@pytest.fixture(scope="session")
def login_token(api_client):
    # 登录请求参数
    # host = tl.get_datas["host"]
    # login_path = tl.get_datas["login_path"]
    # captcha_path = tl.get_datas["captcha_path"]

    # #获取验证码
    # response = api_client.get(url=host+captcha_path)
    # hash_key = response.json()["data"]["hash_key"]
    # ret=local_db.select_sql(
    #         "challenge","response","hashkey","captcha_captchastore","hashkey",hash_key,"id"
    #         ) 

    # data_sucess = tl.content["data_sucess"]
    # data_sucess['captcha']=ret['response']
    # data_sucess['hashkey']=hash_key
   
    # print(login_data)
    # # 发送登录请求
    # response = api_client.post(
    #     url=host+login_path,
    #     data=json.dumps(data_sucess)
    # )
    # print(response.text())
    # token = response.json()["data"]["token"]
    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IjE1Mzc1MjIyMzQzIiwiZXhwIjoxNzYxMTg3NTkyLCJlbWFpbCI6IiIsInBob25lIjoiMTUzNzUyMjIzNDMifQ.7zr6TMyMvFZ8Tg_GyntKsT27eWS3efzIp-3hr-HsS3s'
    # assert response.status_code == 200, "登录失败"
    api_client.update_headers({"Authorization": f"JWT {token}"})
    return token  # 返回 token，供其他用例使用



# if __name__ == '__main__':
#     login_token()
    