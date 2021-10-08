# @dingzhihui   
# 2021/6/25   
# 10:30 上午   
# PyCharm
# 手机点餐首页
import json
import unittest
import requests

class test_mobile_homePage(unittest.TestCase):
    def homePage(self, brand_id):
        """brandId:600102"""
        # url = "https://posmobile.downtown8.net/homePage/homePage"
        url = "https://jpos.downtown8.net/jmobile/mobileHomePage/homePage"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brand_id
               }
        res = requests.post(url, headers=headers, json=param)
        return res.json()

    def test_homePage1(self):
        """brandId:600102"""
        brand_id = "600102"  # 品牌id
        request_result = test_mobile_homePage.homePage(self, brand_id)
        print(request_result)
        # if request_result.get('result').get('brandInfo')is not None:
        #     if request_result.get('result').get('brandInfo')
        # # if result.get('result').get("accessToken") is not None:
        #     print("邮箱登录成功"+result.get('result').get("accessToken"))