'''
Descripttion: 
Author: zlj
Date: 2020-11-17 09:37:55
'''
# -*- coding: utf-8 -*-

import allure
import pytest
import json
from Params.parseYaml import ReadYaml
# from Conf.Config import Config
# from Common import Send_Request
from Common import Consts
from Common import Assert
from Params.parseExcel import ParseExcel


class TestProfile:
    @pytest.fixture()
    def getdata(self):
        print('before')
        tl = ReadYaml()
        self.host = tl.get_datas["host"]
        self.path = tl.get_datas["login_path"]
        with allure.step("获取测试地址和路径"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.path )
         

        yield

        print('over')

    @staticmethod
    def get_data():
        exe =ParseExcel(filename='tcData.xlsx')
        sheet=exe.get_sheet_by_name('login')
        data =exe.get_all_values_of_sheet(sheet)
        print(data)
       
        return data
 
    # @allure.feature('Profile')
    # @allure.severity('normal')
    # @allure.story('add profile')
    @allure.title("测试用例：{expected}") 
    @pytest.mark.parametrize("username,password,expected", get_data())
    def test_basic_01(self,username, password,expected,getdata):
        """
            用例描述：profile接口
        """
        print(username,password,expected)
        print(self.host)
        print(self.path)
        assert 1==1
        # request = Send_Request.Request()
        # params = json.dumps(self.data.data[0]['postdata'])
        # api_url = self.host + self.urls[0]
        # response = request.post_request(api_url,params)    
        # print(response['body'])   
        # assert self.test.assert_code(response['code'], 201)
        # Consts.RESULT_LIST.append('True')


