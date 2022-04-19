# encoding=utf-8
import json
import unittest
import warnings

from ddt import ddt, data

from test_case.login import *
from tool.do_excel import GetExcel
from tool.my_log import Mylog
from tool.project_path import *

# 获取excel中数据
test_data2 = GetExcel(testcase_path, 'creat_q').get_data()

mylog = Mylog()


@ddt()
class Creat_q(unittest.TestCase):
    @data(*test_data2)
    def test_creat(self, item):
        # 从反射中获取最新的token值
        # 第一轮执行登录用户，没有token值的时候，header值为空
        header = {"Authorization": getattr(GetData, "token")}
        # 第一次执行登录成功用例，保存token值到反射中
        res = Http_Request().http_request(item['method'], item['url'], eval(item['data']), header)
        print(header)
        # 判断GetData.token是空值，如果是None的话给token值写入GetData中
        # if getattr(GetData, 'token') is None:
        #     setattr(GetData, 'token', res.json()['data']['token'])

        # 可以不用setattr更简单的方法
        if GetData.token is None:
            GetData.token = res.json()['data']['token']

        print("现在反射文件中token的结果是：", getattr(GetData, "token"))
        warnings.simplefilter("ignore", ResourceWarning)
        print("创建圈子的结果是：", res.json())
        try:
            self.assertEqual(10000, res.json()['code'])
            test_result = "测试通过"
        except Exception as e:
            mylog.error("这里出现异常了".format(e))
            test_result = "测试不通过"
        finally:
            GetExcel(testcase_path, 'creat_q').data_write(item['case'] + 1, test_result, str(res.json()))


if __name__ == '__main__':
    unittest.main()
