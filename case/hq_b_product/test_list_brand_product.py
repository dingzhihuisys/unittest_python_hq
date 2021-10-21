# @dingzhihui   
# 2021/10/9   
# 4:43 下午   
# PyCharm
import unittest
import requests
from case.hq_a_passPort import get_email_login_token

# 获取品牌餐品
class test_downtown_list_brand_product(unittest.TestCase):
    def list_brand_product(self, token, brandId):
        url = "https://posconfig.downtown8.net/product/ListBrandProduct"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_list_brand_product01(self):
        """获取餐品-列表"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333
        result = test_downtown_list_brand_product.list_brand_product(self, token, brandId)
        print(result)
        if result.get('result').get("totalElements") is not None:
            print("当前品牌下餐品的数量为：", result.get('result').get("totalElements"))
            return result.get('result').get("content")
        else:
            print("系统报错", result.get('result').get("code"))
