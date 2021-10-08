# @dingzhihui   
# 2021/6/7   
# 6:30 下午   
# PyCharm


# 导入requests和unittest模块
import yaml
import requests
import unittest
# 商家后台登录

class test_downtown_login(unittest.TestCase):
    def login(self, passport, pwd, passport_Type):
        """账号：passport，密码：password，登录方式：passportType"""
        url = "http://eauth.downtown8.net/passport/login"
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

    def test_login1(self):
        """01测试登录：正确账号，正确密码（邮箱）"""
        passport = "758737541@qq.com",  # 正确账号，
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        # print((result.get('result').get("accessToken")))
        if result.get('result').get("accessToken") is not None:
            print("邮箱登录成功", result.get('result').get("accessToken"))
        # 把token值写入配置文件中
        # 保存文件路径
        # r'Users/dingzhihui/dzh_test/PycharmProjects/unittest_python/hq_test_login/a_login/login_email_token.yml'
        yaml_path = r'login_email_token.yml'
        # 提取token字段
        tokenValue = {
            'token': result.get('result').get("accessToken")
        }
        with open(yaml_path, mode="w", encoding="utf-8") as f:
            yaml.dump(tokenValue, f)

    def test_login2(self):
        """02测试登录：正确账号，正确密码 （手机号）"""
        passport = "17816852881",  # 正确账号，
        pwd = "DZH123456",  # 正确密码，
        passport_Type = "mobile",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        # print((result.get('result').get("accessToken")))
        if result.get('result').get("accessToken") is not None:
            print("手机号登录成功", result.get('result').get("accessToken"))
        # 把token值写入配置文件中
        # 保存文件路径
        yaml_path = r'login_mobile_token.yml'
        # 提取token字段
        tokenValue = {
            'token': result.get('result').get("accessToken")
        }
        with open(yaml_path, mode="w", encoding="utf-8") as f:
            yaml.dump(tokenValue, f)

    def test_login3(self):
        """03测试登录：账号错误，正确密码（邮箱）"""
        passport = "758737541",
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == '40002':
            print("账号错误", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))

    def test_login4(self):
        """04测试登录：账号空，正确密码（邮箱）"""
        passport = "",
        pwd = "DZh123456",  # 正确密码，
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == -1:
            print("账号为空", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))

    def test_login5(self):
        """05测试登录：账号正确，密码错误（邮箱）"""
        passport = "758737541@qq.com",  # 正确账号，
        pwd = "DZh1",
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == '40001':
            print("账号或密码错误", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))

    def test_login6(self):
        """06测试登录：账号正确，密码错误（手机）"""
        passport = "17816852881",  # 正确账号，
        pwd = "DZh1",
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == '40002':
            print("密码错误", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))

    def test_login7(self):
        """07测试登录：账号错误，密码正确（手机）"""
        passport = "1781683488155",  # 正确账号，
        pwd = "DZh123456",
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == '40002':
            print("密码错误", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))

    def test_login8(self):
        """08测试登录：账号整，密码为空（手机）"""
        passport = "17816852881",  # 正确账号，
        pwd = "",
        passport_Type = "email",
        result = test_downtown_login.login(self, passport, pwd, passport_Type)
        print(result)
        if result.get('error').get("code") == -1:
            print("密码为空", result.get('error').get("message"))
        else:
            print("系统错误", result.get('error').get("message"))


if __name__ == "__main__":
    unittest.main()