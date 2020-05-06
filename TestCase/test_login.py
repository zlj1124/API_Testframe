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
    def getdata(self):
        print('before')

        conf = Config()
        self.data = Datas()
        self.request = Send_Request.Request()
        self.host = conf.host_qiye6
        self.urls = self.data.url
       

        yield

        print('over')
  
    @allure.feature('Login')
    @allure.severity('blocker')
    @allure.story('测试登录成功')
    # @pytest.mark.parametrize("data1,", [("10086", "10086"),] )
    def test_login_01(self, action,getdata):
        """
            用例描述：login接口
        """
        api_url = self.host + self.urls[1]     
        params = json.dumps(self.data.data[1]['postdata'])
        response = self.request.post_request(api_url,  params)
    
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

   



