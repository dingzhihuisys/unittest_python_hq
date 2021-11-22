# @dingzhihui   
# 2021/11/22   
# 4:26 下午   
# PyCharm

# 场景测试 获取手机号登录 查看领券情况
import unittest
import requests
# 手机端会员登录
from common import get_random_mobile


class test_mobile(unittest.TestCase):
    def handtop_mobile(self, mobile, country_code, captcha, store_id, source, brand_id):
        url = "https://memberservice.downtown8.net/mobile/member/login"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "mobile": mobile,
            "countryCode": country_code,
            "captcha": captcha,
            "storeId": store_id,
            "source": source,
            "brandId": brand_id
        }
        res = requests.post(url, headers=headers, json=param)
        return res.json()

    def test_mobile01(self):
        mobile = get_random_mobile.Random_Phone()
        country_code = 86,
        captcha = '2662',
        store_id = 0,
        source = 'mobile',
        brand_id = "600103"
        request_result = test_mobile.handtop_mobile(self, mobile, country_code, captcha, store_id, source, brand_id)
        print(request_result)
        # if request_result.get('result').get('brandInfo')is not None:
        #     if request_result.get('result').get('brandInfo')
        # # if result.get('result').get("accessToken") is not None:
        #     print("邮箱登录成功"+result.get('result').get("accessToken"))
