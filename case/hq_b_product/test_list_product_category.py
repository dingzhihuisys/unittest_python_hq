# @dingzhihui   
# 2021/10/9   
# 4:49 下午   
# PyCharm

import unittest
import requests
from case.hq_a_passPort import get_email_login_token

# 获取品牌餐品分类
class test_downtown_list_product_category(unittest.TestCase):
    def list_product_category(self, token, brandId, type):
        url = "https://posconfig.downtown8.net/productCategory/listProductCategory"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId,
            "type":type
        }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_list_product_categoryt01(self):
        """获取餐品分类-列表"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333
        type = "default"
        result = test_downtown_list_product_category.list_product_category(self, token, brandId, type)
        print(result)
        if result.get('result').get("totalElements") is not None:
            print("当前品牌下餐品分类的数量为：", result.get('result').get("totalElements"))
            return result.get('result').get("content")
        else:
            print("系统报错", result.get('result').get("code"))