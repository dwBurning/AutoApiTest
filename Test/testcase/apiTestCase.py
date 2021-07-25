from helper.requestHelper import RequestHelper
from helper.excelHelper import ExcelHelper
from config import setting
import requests
import ddt
import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


testData = ExcelHelper(setting.SOURCE_FILE, "Sheet1").read()


@ddt.ddt
class PersonAPI(unittest.TestCase):
    """发布会系统"""

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass

    @ddt.data(*testData)
    def test_api(self, data):
        # 获取ID字段数值，截取结尾数字并去掉开头0
        rowNum = int(data['ID'].split("_")[2])
        print("******* 正在执行用例 ->{0} *********".format(data['ID']))
        print("请求方式: {0}，请求URL: {1}".format(data['method'], data['url']))
        print("请求参数: {0}".format(data['params']))
        print("post请求body类型为：{0} ,body内容为：{1}".format(
            data['type'], data['body']))
        # 发送请求
        re = RequestHelper().sendRequests(self.s, data)
        # 获取服务端返回的值
        self.result = re.json()
        print("页面返回信息：%s" % re.content.decode("utf-8"))
        # 获取excel表格数据的状态码和消息
        readData_code = int(data["code"])
        readData_msg = data["message"]
        if readData_code == self.result['code'] and readData_msg == self.result['message']:
            OK_data = "PASS"
            print("用例测试结果:  {0}---->{1}".format(data['ID'], OK_data))
            ExcelHelper(setting.TARGET_FILE).write(rowNum + 1, OK_data)
        if readData_code != self.result['code'] or readData_msg != self.result['message']:
            NOT_data = "FAIL"
            print("用例测试结果:  {0}---->{1}".format(data['ID'], NOT_data))
            ExcelHelper(setting.TARGET_FILE).write(rowNum + 1, NOT_data)
        self.assertEqual(
            self.result['code'], readData_code, "返回实际结果是->:%s" % self.result['code'])
        self.assertEqual(
            self.result['message'], readData_msg, "返回实际结果是->:%s" % self.result['message'])


if __name__ == '__main__':
    unittest.main()
