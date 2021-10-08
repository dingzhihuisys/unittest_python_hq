# @dingzhihui   
# 2021/10/6   
# 4:36 下午
import unittest
import requests
# 获取个人信息
from case.hq_a_passPort import get_mobile_login_token

class test_downtown_self_detail(unittest.TestCase):
    def self_detail(self, token):
        url = "https://posuser.downtown8.net/employee/selfDetail"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        res = requests.get(url, headers=headers)
        return res.json()

    def test_self_detail01(self):
        """获取个人信息详情"""
        token = get_mobile_login_token.get_login_token()
        result = test_downtown_self_detail.self_detail(self, token)
        print(result)
        # if result.get('result').get("accessToken") is not None:
