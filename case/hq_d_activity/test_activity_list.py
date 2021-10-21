# @dingzhihui   
# 2021/10/9
# 8:41 下午   
# PyCharm
import unittest
import requests
from case.hq_a_passPort import get_email_login_token

# 创建活动接口
class test_downtown_activity(unittest.TestCase):
    def self_activity(self, token):
        url = "https://posuser.downtown8.net/employee/selfDetail"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        res = requests.get(url, headers=headers)
        return res.json()

    def test_self_activity01(self):
        """获取活动列表"""
        token = get_email_login_token.get_login_search_token()
        result = test_downtown_activity.self_activity(self, token)
        print(result)
        # if result.get('result').get("accessToken") is not None:
