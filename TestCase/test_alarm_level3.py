'''
Descripttion: 
Author: zlj
Date: 2025-10-16 09:37:55
'''
# -*- coding: utf-8 -*-

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
        self.case1_data=tl.get_datas['alarm_level3_case1']
        self.case2_data=tl.get_datas['alarm_level3_case2']
        self.case3_data=tl.get_datas['alarm_level3_case3']
        self.case4_data=tl.get_datas['alarm_level3_case4']
        self.case5_data=tl.get_datas['alarm_level3_case5']
        self.path=self.case1_data['path']
     
        # data_sucess = tl.content["data_sucess"]
        with allure.step("请求接口信息"):
            allure.attach(name='请求地址', body=self.host)
            allure.attach(name='请求路径', body=self.path )
        yield

        print('over')

    def test_01(self,api_client,login_token,case_data):
        """
            用例描述:三级报警列表按时间段搜索，时间段为今天
        """
        allure.dynamic.title(f"测试用例: {self.case1_data['name']}")
        api_url = self.host + self.path
        data=self.case1_data['params']
        # 获取今天 00:00:00 的时间对象
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 获取当前时间对象
        now = datetime.now()
        # 格式化为指定格式（年-月-日 时:分:秒）
        data['start_time__gt']= today_start.strftime("%Y-%m-%d %H:%M:%S")
        data['start_time__lt']= now.strftime("%Y-%m-%d %H:%M:%S")
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        vin=response["body"]['data'][0]['vin']
        case_data["vin"] = vin
        # print(response["body"]['data'][0]['start_time'])
        start_time_str = response["body"]['data'][0]['start_time']  # 从响应中提取 start_time
        start_date = datetime.strptime(start_time_str.split()[0], "%Y-%m-%d").date()#只取年-月-日
        today = datetime.now().date()#获取今天的日期（只取年-月-日）
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_text(start_date,today) #断言有产生今天的数据
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_按时间段查询",
                                      expect_value=today,actual_value=start_date,assert_desc='断言列表有当日最新数据产生')     
        
    
    def test_02_byvin(self,api_client,login_token,case_data):
        """
            用例描述:三级报警列表按VIN搜索,参数为上一个接口返回值
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
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_按VIN查询")

    def test_02(self,api_client,login_token):
        """
            用例描述:三级报警列表按VIN搜,参数为配置参数
        """
        allure.dynamic.title(f"测试用例: {self.case2_data['name']}")
        api_url = self.host + self.path
        data=self.case2_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect= self.case2_data['expected']['vin']
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect)#断言搜索结果中包含搜索条件
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_按VIN查询")    
     



    def test_03(self,api_client,login_token):
        """
            用例描述:三级报警列表按最高报警等级搜索
        """
        allure.dynamic.title(f"测试用例: {self.case3_data['name']}")
        api_url = self.host + self.path
        data=self.case3_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect= self.case3_data['expected']['alert_level']
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect)
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_最高等级查询")  

    def test_04(self,api_client,login_token):
        """
            用例描述:三级报警列表按报警原因搜索
        """
        allure.dynamic.title(f"测试用例: {self.case4_data['name']}")
        api_url = self.host + self.path
        data=self.case4_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect= self.case4_data['expected']['alert_reason']
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect)
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_按报警原因查询") 

    def test_05(self,api_client,login_token):
        """
            用例描述:三级报警列表按结构号搜索
        """
        allure.dynamic.title(f"测试用例: {self.case5_data['name']}")
        api_url = self.host + self.path
        data=self.case5_data['params']
        print('请求信息:path:{},data:{}---'.format(api_url,data))
        response = api_client.get_request(url=api_url,data=data) 
        msg=response['body']['data'][0]
        expect= self.case5_data['expected']['hierarchy_num']
        assert self.test.assert_code(response['code'], 200)
        assert self.test.assert_in_text(msg,expect)
        Allureconf.allure_report_step(data, response, step_name="三级报警列表接口_按结构号查询")
   