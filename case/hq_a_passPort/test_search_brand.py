# @dingzhihui   
# 2021/10/6   
# 4:36 下午   
# PyCharm
# 切换品牌 更换token
import unittest

import requests


class test_downtown_search_brand(unittest.TestCase):
    def search_brand(self, token):
        url = "https://posconfig.downtown8.net/brand/searchBrand"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "token": token,
             }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_search_brand01(self):
        token = "",
        result = test_downtown_search_brand.search_brand(self, token)
