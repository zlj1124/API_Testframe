# -*- encoding: utf-8 -*-
'''
@File    :   run.py
@Author  :   zlj
@Time    :   2020/04/15 16:59:41
'''


"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""
import sys

import pytest

from Common import Log
from Common import Shell
from Conf import Config
from Common import Email

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    args = ['-s', '-q', '--alluredir', xml_report_path]

    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    # print(cmd)
    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    # try:
    #     mail = Email.SendMail()
    #     mail.sendMail()
    # except Exception as e:
    #     log.error('发送邮件失败，请检查邮件配置')
    #     raise

