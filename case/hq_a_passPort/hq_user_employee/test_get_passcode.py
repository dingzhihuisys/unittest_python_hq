# @dingzhihui   
# 2021/10/7   
# 3:40 下午   
# PyCharm
import unittest

import requests

from case.hq_a_passPort import get_mobile_login_token

# 生成4位码
class test_downtown_get_passcode(unittest.TestCase):
    def get_passcode(self, token, brandId):
        url = "https://posuser.downtown8.net/common/getPasscode"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_get_passcode01(self):
        """生成4位码"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333
        result = test_downtown_get_passcode.get_passcode(self, token, brandId)
        print(result.get('result').get('passcode'))
        return result.get('result').get('passcode')