# -*- coding: utf-8 -*-


import allure
import pytest
import json
from Params.params import Datas
from Conf.Config import Config
from Common import Send_Request
from Common import Consts
from Common import Assert
from Common.DB_sql import DbConnect
from Params.parseExcel import ParseExcel
local_db=DbConnect()
# ret=local_db.select_sql(
#             "id","vehicleFrameNo","create_time","truck_truck","deleted","0","create_time"
#             ) 

class TestLogin:

   
    @pytest.fixture()
    def get_data(self):
        """
            获取测试数据
        """
        print('before')

        conf = Config()
        self.data = Datas()
        self.request = Send_Request.Request()
        self.host = conf.host_qiye6
        self.urls = self.data.url 
        with allure.step("获取测试地址和路径"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.urls[1])
         

        yield

        print('over')
  
    @allure.feature('登录')
    @allure.severity('blocker')
    @allure.story('测试登录成功')
    # @pytest.mark.parametrize("data1,", [("10086", "10086"),] )
    def test_login_01(self, get_data):
        """
            用例描述：login成功接口
        """
       
        api_url = self.host + self.urls[1]     
        params = json.dumps(self.data.data[1]['postdata'])
        response = self.request.post_request(api_url,  params)
        
        with allure.step("登录post请求接口"):
            allure.attach(name='测试数据', body=params)
            allure.attach(name='响应状态码', body=str(response['code']))
            allure.attach(name='响应时间', body=str(response['time_consuming']))
            allure.attach(name='响应内容', body=str(response['body']))

        with allure.step("校验返回响应码"):
            allure.attach(name='预期响应码', body='200')
            allure.attach(name='实际响应码', body=str(response['code']))
        assert response['code'] == 200    
        Consts.RESULT_LIST.append('True')

   



