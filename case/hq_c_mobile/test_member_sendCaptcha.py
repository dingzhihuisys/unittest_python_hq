# @dingzhihui   
# 2021/11/4   
# 4:40 下午   
# PyCharm
import unittest
import requests
from case.hq_c_mobile.test_member_check import test_member_check

class test_member_sendCaptcha(unittest.TestCase):
    def member_sendCaptcha(self, brand_id, countryCode, mobile, type_t):
        """brandId:600103"""
        url = "https://memberservice.downtown8.net/mobile/member/sendCaptcha"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        param = {
            "type": type_t,
            "mobile": mobile,
            "countryCode": countryCode,
            "brandId": brand_id
        }
        res = requests.post(url, headers=headers, json=param)
        return res.json()

    def test_sendCaptcha(self):
        """已经注册返回false"""
        brand_id = 600103  # 品牌id
        countryCode = 86
        mobile = test_member_check().test_check01()
        print('-------------', mobile)
        type_t = "login"
        request_result = test_member_sendCaptcha.member_sendCaptcha(self, brand_id, countryCode, mobile, type_t)
        print("内容", request_result)