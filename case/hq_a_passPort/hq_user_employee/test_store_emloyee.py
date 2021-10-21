# @dingzhihui   
# 2021/10/7   
# 3:22 下午   
# PyCharm
import unittest

import requests

from case.hq_a_passPort import get_email_login_token

# 获取可以选择的门店
class test_downtown_store_employee(unittest.TestCase):
    def store_employee(self, token, brandId):
        url = "https://posuser.downtown8.net/employeeStore/listStore"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_store_employee01(self):
        """获取门店列表"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333
        result = test_downtown_store_employee.store_employee(self, token, brandId)
        print(result)
        # if result.get('result').get("accessToken") is not None: