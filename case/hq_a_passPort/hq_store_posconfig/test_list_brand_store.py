# @dingzhihui   
# 2021/10/7   
# 1:50 下午   
# PyCharm

# 获取品牌下门店
import unittest
import requests
from case.hq_a_passPort import get_email_login_token


class test_list_brand_store(unittest.TestCase):
    def list_brand_store(self, token, brandId):
        url = "https://posconfig.downtown8.net/store/listBrandStore"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        res = requests.get(url, headers=headers, params=param)
        return res.json()

    def test_list_brand_store01(self):
        """获取品牌下的门店信息"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333,
        result = test_list_brand_store.list_brand_store(self, token, brandId)
        print(result)
        # if result.get('result').get("accessToken") is not None: