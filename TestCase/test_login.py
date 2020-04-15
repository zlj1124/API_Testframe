# -*- coding: utf-8 -*-


import allure
import pytest
import json
from Params.params import Datas
from Conf.Config import Config
from Common import Send_Request
from Common import Consts
from Common import Assert



class TestLogin:


    @pytest.fixture()
    def getdata(self):
        print('before')
        conf = Config()
        self.data = Datas()
        self.request = Send_Request.Request()
        self.host = conf.host_debug  
        self.urls = self.data.url

        yield

        print('over')
  
    # @pytest.allure.feature('Login')
    @allure.severity('blocker')
    @allure.story('Datas')
    def test_login_01(self, action,getdata):
        """
            用例描述：login接口
        """
        api_url = self.host + self.urls[1]     
        params = json.dumps(self.data.data[1]['postdata'])
        response = self.request.post_request(api_url, params, )
    
        assert response['code'] == 200
        Consts.RESULT_LIST.append('True')

   



