'''
Descripttion: 
Author: zlj
Date: 2025-10-21 09:48:49
'''

import allure
import pytest
import json
from Params.parseYaml import ReadYaml
from Common import Allureconf
# from Conf.Config import Config
from Common import Send_Request
from Common import Consts
from Common import Assert
from Params.parseExcel import ParseExcel
from datetime import datetime

class Test_Rangereport:
    @pytest.fixture(autouse=True)
    def getdata(self):
        print('before')
        tl = ReadYaml()
        self.test = Assert.Assertions()
        self.host = tl.get_datas["host"]
        self.case1_data=tl.get_datas['range_report_case1']
        self.path=self.case1_data['path']
     
  
        with allure.step("请求接口信息"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.path )
        yield

        print('over')

    def test_01(self,api_client,login_token):
        """
            用例描述:单车续航报告生成，任务列表导出状态为已完成
        """
        allure.dynamic.title(f"测试用例: {self.case1_data['name']}")
        api_url = self.host + self.path
        data=self.case1_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]['calculate_status_display']
        expect= self.case1_data['expected']['calculate_status_display']
     
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_text(msg,expect) #断言结果符合预期
        Allureconf.allure_report_step(data, response, step_name="单车续航报告生成接口",
                                      expect_value=expect,actual_value=msg,assert_desc='断言导出任务列表中状态为已完成')     
        