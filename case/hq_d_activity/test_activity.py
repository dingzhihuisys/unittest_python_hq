# @dingzhihui   
# 2021/7/6   
# 8:41 下午   
# PyCharm
import unittest
import requests
# class test_downtown_activity(unittest.TestCase):
#     def activity(self, passport, pwd, passport_Type):
#         """账号：passport，密码：password，登录方式：passportType"""
#         url = "http://eauth.downtown8.net/passport/login"
#         headers = {
#             "content-type": "application/json; charset=utf-8"
#         }  # get方法其它加个ser-Agent就可以了
#         param = {
#             "passport": passport,
#             "pwd": pwd,
#             "passportType": passport_Type
#                }
#         res = requests.post(url, headers=headers, params=param)
#         return res.json()
#
#     def test_activity01(self):
#         """测试登录：正确账号，正确密码（邮箱）"""
#         passport = "758737541@qq.com",  # 正确账号，
#         pwd = "DZh123456",  # 正确密码，
#         passport_Type = "email",
#         result = test_downtown_login.login(self, passport, pwd, passport_Type)
#         # print((result.get('result').get("accessToken")))
#         if result.get('result').get("accessToken") is not None:
#             print("邮箱登录成功"+result.get('result').get("accessToken"))
#         # 把token值写入配置文件中
#         # 保存文件路径
#         # r'Users/dingzhihui/dzh_test/PycharmProjects/unittest_python/hq_test_login/a_login/login_email_token.yml'
#         yaml_path = r'login_email_token.yml'
#         # 提取token字段
#         tokenValue = {
#             'token': result.get('result').get("accessToken")
#         }
#         with open(yaml_path, mode="w", encoding="utf-8") as f:
#             yaml.dump(tokenValue, f)