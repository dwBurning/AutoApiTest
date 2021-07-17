import time
import unittest

from HTMLTestRunner import HTMLTestRunner

from config import setting
from helper.sendEmailHelper import send_mail
from package.HTMLTestRunner import HTMLTestRunner


def add_case(test_path=setting.TEST_CASE):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='*apiTestCase.py')
    return discover

def run_case(all_case,result_path=setting.TEST_REPORT):
    """执行所有的测试用例"""

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =  result_path + '/' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='人事信息接口自动化测试报告',
                            description='环境：windows 7 浏览器：chrome',
                            tester='burning')
    runner.run(all_case)
    fp.close()
    send_mail(filename) #调用发送邮件模块

if __name__ =="__main__":
    cases = add_case()
    run_case(cases)
