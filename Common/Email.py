'''
@Descripttion: 
@Author: zlj
@Date: 2020-04-13 14:40:09
'''
# -*- coding: utf-8 -*-


"""
封装发送邮件的方法

"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from Common import Consts
from Common import Log
from Conf.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self):
        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        print("stress_body:{}".format(stress_body))
        print("result_body:{}".format(result_body))
        test_dir = os.path.join(os.getcwd(), "Report/")
        rep_dir= os.path.join(test_dir,'Report.html')
        with open(rep_dir, "rb") as f:
            mail_content = f.read()
           
        annex = MIMEMultipart()
        # 添加正文
        body = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        mail_body = MIMEText(mail_content , "html", 'utf-8')
        
        # 添加附件
        msg_html = MIMEText(mail_content, "html", "utf-8")
        msg_html["Content-Type"] = "application/octet-stream"
        msg_html["Content-Disposition"] = "attachment; filename=Report.html"
        annex.attach(mail_body)
        annex.attach(msg_html)
        annex["Subject"] = Header('接口测试报告', "utf-8")
        annex['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        annex['To'] = ",".join(toclause)

       

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, annex.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")

        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
