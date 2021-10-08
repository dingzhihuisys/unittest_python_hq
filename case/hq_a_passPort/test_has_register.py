# @dingzhihui   
# 2021/6/12   
# 1:35 下午   
# PyCharm
import unittest
import requests
# 注册

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
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_register01(self):
        """验证邮箱是否注册：True"""
        passport = "758737541@qq.com",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = test_downtown_register.register(self, passport, pwd, passport_Type)
        # print(result)
        if result.get('result').get('hasRegister'):
            print("该账号已注册", result.get('result').get("hasRegister"), passport)
        else:
            print("该账号未注册", result.get('result').get("hasRegister"), passport)

    def test_register02(self):
        """验证手机号是否注册：false"""
        passport = "13783495334",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "mobile",
        result = test_downtown_register.register(self, passport, pwd, passport_Type)
        # print(result.get('result').get('hasRegister'))
        if result.get('result').get('hasRegister'):
            print("该账号已注册", result.get('result').get("hasRegister"), passport)
        else:
            print("该账号未注册", result.get('result').get("hasRegister"), passport)

    def test_register03(self):
        """验证手机号是否注册：True"""
        passport = "17816852881",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "mobile",
        result = test_downtown_register.register(self, passport, pwd, passport_Type)
        # print(result.get('result').get('hasRegister'))
        if result.get('result').get('hasRegister'):
            print("该账号已注册", result.get('result').get("hasRegister"), passport)
        else:
            print("该账号未注册", result.get('result').get("hasRegister"), passport)


if __name__ == "__main__":
    unittest.main()


