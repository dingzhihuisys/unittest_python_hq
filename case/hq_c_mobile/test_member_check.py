# @dingzhihui   
# 2021/11/4   
# 4:32 下午   
# PyCharm
import unittest
import requests
# 手机号检查是否注册
from common import get_random_mobile


class test_member_check(unittest.TestCase):
    def member_check(self, brand_id, countryCode, mobile):
        """brandId:600103"""
        url = "https://memberservice.downtown8.net/mobile/member/checkIsRegister"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }
        param = {
            "mobile": mobile,
            "countryCode": countryCode,
            "brandId": brand_id
        }
        res = requests.post(url, headers=headers, json=param)
        return res.json()

    def test_check01(self):
        """已经注册返回True"""
        brand_id = 600103  # 品牌id
        countryCode = 86
        mobile = get_random_mobile.Random_Phone()
        request_result = test_member_check.member_check(self, brand_id, countryCode, mobile)
        print("内容", request_result)
        if request_result.get('result').get('isRegister') is False:
            return mobile
        # print("查看结果", request_result.get('result').get('isRegister'), mobile)
