# @dingzhihui   
# 2021/10/11   
# 10:36 上午   
# PyCharm
# 导入requests和unittest模块
import yaml
import requests
import unittest
# 获取可选择的品牌列表
from case.hq_a_passPort import get_email_login_token

class test_downtown_search_brand(unittest.TestCase):
    def search_brand(self, token):
        url = "https://posconfig.downtown8.net/brand/searchBrand"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        res = requests.post(url, headers=headers)
        return res.json()

    def test_search_brand1(self):
        """切换品牌列表"""
        token = get_email_login_token.get_email_login_token()
        result = test_downtown_search_brand.search_brand(self, token)
        print('search_brand1', result.get('result'))
        brand_list = result.get('result')
        for brand_id in brand_list:
            if brand_id['brandId'] == 600333:
                print(brand_id)
                return brand_id


