
import allure
from Common import Consts # 假设 Consts 在 your_module 模块中

def allure_report_step(data, response, step_name="三级报警列表接口",
                       expect_value=None, actual_value=None, assert_desc=None):
    """
    封装 Allure 报告步骤及测试结果收集逻辑
    :param data: 测试数据
    :param response: 接口响应
    :param step_name: Allure 步骤名称
    """
    Consts.RESULT_LIST.append('True')
    with allure.step(step_name):
        allure.attach(name="测试数据", body=str(data))
        allure.attach(name="响应状态码", body=str(response['code']))
        allure.attach(name="响应时间ms", body=str(response['time_consuming']))
        allure.attach(name="响应内容", body=str(response['body']))
        if expect_value is not None and actual_value is not None and assert_desc is not None:
            allure.attach(name="断言描述", body=assert_desc)
            assert actual_value == expect_value, assert_desc