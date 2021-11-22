# @dingzhihui   
# 2021/11/4   
# 4:30 下午   
# PyCharm
import unittest
import requests
# 手机端会员登录
class test_mobile_homePage(unittest.TestCase):
    def homePage(self, brand_id, login_pwd, captcha, nick_name, avatar_url, mobile, country_code, store_id, source):
        """brandId:600102"""
        url = " https://memberservice.downtown8.net/mobile/member/login"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "loginPwd": login_pwd,
            "captcha": captcha,
            "nickName": nick_name,
            "avatarUrl": avatar_url,
            "mobile": mobile,
            "countryCode": country_code,
            "storeId": store_id,
            "source": source,
            "brandId": brand_id
        }
        res = requests.post(url, headers=headers, json=param)
        return res.json()

    def test_homePage1(self):
        """brandId:600102"""
        brand_id = "600102"
        login_pwd = ''
        captcha = ''
        nick_name = ''
        avatar_url = ''
        mobile = ''
        country_code = ''
        store_id = ''
        source = ''
        request_result = test_mobile_homePage.homePage(self, brand_id, login_pwd, captcha, nick_name, avatar_url, mobile, country_code, store_id, source)
        print(request_result)
        # if request_result.get('result').get('brandInfo')is not None:
        #     if request_result.get('result').get('brandInfo')
        # # if result.get('result').get("accessToken") is not None:
        #     print("邮箱登录成功"+result.get('result').get("accessToken"))