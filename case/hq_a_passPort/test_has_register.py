# @dingzhihui   
# 2021/6/12   
# 1:35 下午   
# PyCharm
import unittest
import requests

class test_downtown_register(unittest.TestCase):
    def register(self, passport, pwd, passport_Type):
        url = "http://eauth.downtown8.net/passport/hasRegister"
        headers = {
            "content-type": "application/json; charset=utf-8"
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "passport": passport,
            "pwd": pwd,
            "passportType": passport_Type
        }
        # print(param)
        res = requests.post(url, headers=headers, params=param)
        # print(res.text)
        return res.json()

    def test_register01(self):
        passport = "758737541@qq.com",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = test_downtown_register.register(self, passport, pwd, passport_Type)
        print(result)



