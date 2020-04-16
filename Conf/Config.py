# -*- coding: utf-8 -*-


from configparser import ConfigParser
from Common import Log
import os


class Config:
    # titles:
    TITLE_PLAT= "qiye6_dev"
    TITLE_EMAIL = "mail"

    # values:

    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "tokenHost"
    VALUE_LOGIN_INFO = "loginInfo"
    VALUE_HEADER = "headers"

    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'
        self.config.read(self.conf_path, encoding='utf-8')
        # 平台信息
        self.tester = self.get_conf(Config.TITLE_PLAT, Config.VALUE_TESTER)
        self.environment_qiye6 = self.get_conf(Config.TITLE_PLAT, Config.VALUE_ENVIRONMENT)
        self.versionCode_qiye6= self.get_conf(Config.TITLE_PLAT, Config.VALUE_VERSION_CODE)
        self.host_qiye6= self.get_conf(Config.TITLE_PLAT, Config.VALUE_HOST)
        self.tokenHost_qiye6 = self.get_conf(Config.TITLE_PLAT, Config.VALUE_LOGIN_HOST)
        self.loginInfo_qiye6 = self.get_conf(Config.TITLE_PLAT, Config.VALUE_LOGIN_INFO)
        self.headers = self.get_conf(Config.TITLE_PLAT,Config.VALUE_HEADER)
        
        # 邮件
        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
      
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == "__main__":
    a=Config()