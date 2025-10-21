'''
Descripttion: 
Author: zlj
Date: 2025-09-16 09:37:55
'''
# -*- coding: utf-8 -*-

import allure
import pytest
import json
from Params.parseYaml import ReadYaml
# from Conf.Config import Config
from Common import Send_Request
from Common import Consts
from Common import Assert
from Params.parseExcel import ParseExcel


class Alarm_level3:
    @pytest.fixture()
    def getdata(self):
        print('before')
        tl = ReadYaml()
        self.test = Assert.Assertions()
        self.host = tl.get_datas["host"]
        self.path = tl.get_datas["alarm_level_3"]
        with allure.step("请求接口信息"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.path )
        
         

        yield

        print('over')

    @staticmethod
    def get_data():
        exe =ParseExcel(filename='jacData.xlsx')
        sheet=exe.get_sheet_by_name('list')
        data =exe.get_all_values_of_sheet(sheet)
        return data
 

    @allure.title("测试用例：{name}") 
    @pytest.mark.parametrize("limit,page,keyword,expected,name", get_data())
    def test_basic_01(self,limit, page,keyword,expected,name,getdata):
        """
            用例描述：运营商列表接口:按运营商名称/ID搜索
        """
        data=dict(zip(['limit','page','keyword'],[limit,page,keyword]))
        request = Send_Request.Request()
        api_url = self.host + self.path
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = request.post_request(api_url,data=json.dumps(data))    
        msg=response['body']['data']['records'][0]
        
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expected)
        
        Consts.RESULT_LIST.append('True')
        with allure.step("运营商列表接口"):
            allure.attach(name='测试数据', body=str(data))
            allure.attach(name='响应状态码', body=str(response['code']))
            allure.attach(name='响应时间ms', body=str(response['time_consuming']))
            allure.attach(name='响应内容', body=str(response['body']))

