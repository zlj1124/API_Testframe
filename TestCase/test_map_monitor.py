'''
Descripttion: 
Author: zlj
Date: 2025-10-21 10:39:39
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

class Test_searchlist:
    @pytest.fixture(autouse=True)
    def getdata(self):
        print('before')
        tl = ReadYaml()
        self.test = Assert.Assertions()
        self.host = tl.get_datas["host"]
        self.case1_data=tl.get_datas['map_monitor_case1']
        self.case2_data=tl.get_datas['map_monitor_case2']
        self.case3_data=tl.get_datas['map_monitor_case3']
        self.path=self.case1_data['path']
     
       
        with allure.step("请求接口信息"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.path )
        yield

        print('over')

    def test_01(self,api_client,login_token,case_data):
        """
            用例描述:地图监控搜索在线车辆
        """
        allure.dynamic.title(f"测试用例: {self.case1_data['name']}")
        api_url = self.host + self.path
        data=self.case1_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        vin=response["body"]['data'][0]['vin']
        case_data["vin"] = vin
        msg = response["body"]['data'][0]['dynamic_online_status_display']  # 从响应中提取 
        expect= self.case1_data['expected']['dynamic_online_status_display']
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_text(msg,expect) 
        Allureconf.allure_report_step(data, response, step_name="地图监控列表接口_按在线查询",
                                      expect_value=expect,actual_value=msg,assert_desc='断言列表有当日在线车辆')     
        
    
    def test_02(self,api_client,login_token,case_data):
        """
            用例描述:地图监控列表按VIN搜索,参数为上一个接口返回值
        """
        allure.dynamic.title(f"测试用例: {self.case2_data['name']}")
        api_url = self.host + self.path
        vin = case_data.get("vin") #使用上一个接口返回的vin进行传参
        data=self.case2_data['params']
        data['vin']=vin
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect= vin
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect)#断言搜索结果中包含搜索条件
        Allureconf.allure_report_step(data, response, step_name="地图监控列表接口_按VIN查询")

    def test_03(self,api_client,login_token,case_data):
        """
            用例描述:地图监控，车辆卡片详情,vin为上一个接口返回值
        """
        allure.dynamic.title(f"测试用例: {self.case3_data['name']}")
        path=self.case3_data['path']
        api_url = self.host + path
        vin = case_data.get("vin") #使用上一个接口返回的vin进行传参
        data=self.case3_data['params']
        data['vin']=vin
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect1= vin
        expect2= self.case1_data['expected']['dynamic_online_status_display']
       
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect1)#断言详情中vin与搜索时一致
        assert self.test.assert_in_text(msg,expect2)#断言详情的在线状态符合预期
        Allureconf.allure_report_step(data, response, step_name="地图监控车辆详情接口")
    
