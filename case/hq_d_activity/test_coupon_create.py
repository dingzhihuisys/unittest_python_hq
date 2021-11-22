# @dingzhihui   
# 2021/10/9   
# 6:24 下午   
# PyCharm

import unittest
import requests
from case.hq_a_passPort import get_email_login_token

# 创建优惠券
class test_downtown_create_coupon(unittest.TestCase):
    def create_coupon(self, token, coupon_name, type_single, eat_types, is_all_store, store_s, discount_type,
                    discount_value, product_relation, category_no, product_no, scale_no, product_combo_relation, combo_products, when_effect,
                    effect_day, description_s, is_give, picture_s, is_all_time, is_include_modifier, brandId):
        url = ""
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "couponName": coupon_name,
            "type": type_single,
            "eatTypes": eat_types,
            "isAllStore": is_all_store,
            "stores": store_s,
            "discountType": discount_type,
            "discountValue": discount_value,
            "productRelation": product_relation,
            "products": [
                {
                    "categoryNo": category_no,
                    "productNo": product_no,
                    "scaleNo": scale_no}
            ],
            "productComboRelation": product_combo_relation,
            "comboProducts": combo_products,
            "whenEffect": when_effect,
            "effectDay": effect_day,
            "description": description_s,
            "isGive": is_give,
            "picture": picture_s,
            "isAllTime": is_all_time,
            "isIncludeModifier": is_include_modifier,
            "brandId": brandId

        }
        res = requests.get(url, headers=headers)
        return res.json()

    def test_coupon_list01(self):
        """创建优惠券"""
        token = get_email_login_token.get_login_search_token()
        coupon_name = "创建单品优惠券001",
        type_single = "item",
        eat_types = ["dineinMobile", "togoMobile", "dineinPos", "togoPos"],
        is_all_store = True,
        store_s = [],
        discount_type = "discountFee",
        discount_value = 30,
        product_relation = "included",
        category_no = "2e542107-7f8f-4173-acd2-bb884713bfae",
        product_no = '',
        scale_no = '',
        product_combo_relation = "included",
        combo_products = [],
        when_effect = "today",
        effect_day = '',
        description_s = "文案内容",
        is_give = False,
        picture_s = "https://eshine-image-test.oss-cn-hangzhou.aliyuncs.com/image/d28ab24cae8e4069abfa305595090964.jpg",
        is_all_time = True,
        is_include_modifier = False,
        brandId: 600333
        result = test_downtown_create_coupon.create_coupon(self, token, coupon_name, type_single, eat_types, is_all_store,
                                                       store_s, discount_type,discount_value, product_relation,
                                                       category_no, product_no, scale_no, product_combo_relation,
                                                       combo_products, when_effect, effect_day, description_s, is_give,
                                                       picture_s, is_all_time, is_include_modifier, brandId)
        print(result)
        # if result.get('result').get("accessToken") is not None:
