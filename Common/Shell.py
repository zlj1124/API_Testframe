'''
Descripttion: 
Author: zlj
Date: 2020-04-13 14:40:09
'''
# -*- coding: utf-8 -*-


"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        #启动一个新的进程中执行一个子程序
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        # print(o)
        return o
if __name__ == "__main__":
    s=Shell.invoke("pwd")
    print(s)
