# @dingzhihui   
# 2021/10/11   
# 11:21 上午   
# PyCharm
import requests
import unittest
# 从列表中选择一个品牌进入


# 选择一个品牌
import yaml

from case.hq_a_passPort import get_email_login_token
from case.hq_a_passPort.hq_login_token import test_search_brand


# def search_brand_one(result_one_brand, brand_id):
#     for result_one in result_one_brand:
#         if result_one.get('brandId') == brand_id:
#             return result_one
#         else:
#             "系统报错"
from main import project_path

class test_downtown_change_brand(unittest.TestCase):
    def change_brand(self, token, new_brand_id):
        url = "https://posconfig.downtown8.net/brand/changeBrand?newBrandId=600333"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "newBrandId": new_brand_id

        }
        res = requests.post(url, headers=headers)
        return res.json()

    def test_change_brand01(self):
        """切换品牌列表"""
        token = get_email_login_token.get_login_search_token()
        brand_list = test_search_brand.test_downtown_search_brand().test_search_brand1()
        print(brand_list, "这里是获取上一个search_brand1的返回数据")
        new_brand_id = brand_list.get('brandId')
        result = test_downtown_change_brand.change_brand(self, token, new_brand_id)
        print('search_brand1+++++++', result.get('result'))
        if result.get('result') is None:
            print("系统报错")
        else:
            yaml_path = project_path + '/case/hq_a_passPort/hq_login_token/get_login_search_token.yml'
            # 提取token字段
            tokenValue = {
                'token': result.get('result').get("accessToken")
            }
            with open(yaml_path, mode="w", encoding="utf-8") as f:
                yaml.dump(tokenValue, f)
            print("获取切换的Token")
