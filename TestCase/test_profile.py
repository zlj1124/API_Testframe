# -*- coding: utf-8 -*-

import allure
import pytest
import json
from Params.params import Datas
from Conf.Config import Config
from Common import Send_Request
from Common import Consts
from Common import Assert


class TestProfile:
    @pytest.fixture()
    def getdata(self):
        print('before')
        conf = Config()
        self.data = Datas()
        self.request = Send_Request.Request()
        self.test = Assert.Assertions()

        self.host = conf.host_debug  
        self.urls = self.data.url

        yield

        print('over')

 
    # @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Datas')
    def test_basic_02(self, action,getdata):
        """
            用例描述：profile接口
        """
    
        request = Send_Request.Request()
      
      
        params = json.dumps(self.data.data[0]['postdata'])
        api_url = self.host + self.urls[0]
        response = request.post_request(api_url,params)       
        assert self.test.assert_code(response['code'], 201)
        Consts.RESULT_LIST.append('True')
