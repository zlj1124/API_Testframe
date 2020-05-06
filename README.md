# API_Automation
基于Pytest+request+Allure的接口自动化框架

----
#### 模块类的设计
`Request.py` 封装request方法，可以支持多协议扩展（get\post\put\path\delete）

`Config.py`读取配置文件，包括：不同环境的配置，email相关配置

`Log.py` 封装记录log方法，分为：debug、info、warning、error、critical

`Email.py`封装smtplib方法，运行结果发送邮件通知

`Assert.py` 封装assert方法

`Session.py` 封装获取登录cookies方法

`run.py` 核心代码。定义并执行用例集，生成报告

##### 打开报告： allure open Report/html
  
----

