# # @dingzhihui
# # 2021/10/7
# # 6:35 下午
# # PyCharm
# import json
# import unittest
# import requests
# from case.hq_a_passPort import get_email_login_token
# # 发送邀请信息
# from case.hq_a_passPort.hq_user_employee import test_create_employee
#
#
# class test_downtown_employee_notify(unittest.TestCase):
#     def employee_notify(self, token, brandId, mobile, countryCode, email, employeeId, messageType):
#         url = "https://posuser.downtown8.net/employee/notify"
#         headers = {
#             "content-type": "application/json; charset=utf-8",
#             "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOSwidG9rZW5faWQiOiJlZThmMTgxMVMzOGNmUzQyYjBTOGZjMVM5MmYyZWUyOTdiYzgiLCJicmFuZF9pZHMiOls2MDAxMDIsNjAwMTAzLDYwMDI4OSw2MDAzMzMsMTExNjAwNzI5LDExMTYwMDg0OCwxMTE2MDA4NDksMTExNjAwODUyLDExMTYwMDg2NiwxMTE2MDA4MTksMTExNjAwMzM0LDExMTYwMTAwOV0sImJyYW5kX2lkIjo2MDAzMzMsIm9wX2VtcGxveWVlIjo1OTAsImlhdCI6MTYzMzkzMzY0NCwiZXhwIjoxNjM0NTM4NDQ0fQ.jLuoETphWWh9YmolCbTHkwppCKm-EQmzWVVKiETs1hdEmBNgLgeAIyPEyvJ1UfnId2snxdIXW3Sg7RH5noamDlKRPqQBMLelux0QlIWER1dsS8SvYR8TKyGvZoW9koXaVU7RI7G1_aEpZc-ySkO2VYjKUlN_ro7v0MJ-htmff2Z0Yegxl2ecZrJdHKGrjDKczEkM1rbtUnWZj9ZzdwDO6H981JnDck0jaq7aFIb1WNQzRXBNUP0c8SkW4q8fuxgST7uSJjgOC2Adr4vCOLs9FbQq-0vQYfSaWrj246qMn088RmNaIKhAl4YXqB-GjbZ43Pz1KUA_yEE705Dj1xuDSw"
#         }  # get方法其它加个ser-Agent就可以了
#         param = {
#             "brandId": brandId
#         }
#         data = {
#             "mobile": mobile[0],
#             "countryCode": countryCode[0],
#             "email": email[0],
#             "employeeId": employeeId,
#             "messageType": messageType
#         }
#         res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
#         return res.json()
#
#     def test_employee_notify01(self):
#         """给门店经理发送短信信息"""
#         token = get_email_login_token.get_login_search_token()
#         brandId = 600333,
#         # 获取创建门店经理的返回数据
#         res = test_create_employee.test_downtown_create_employee().test_create_employee01().get('result')
#         print("test_employee_notify01------", res)
#         mobile = res.get('mobile')[0],
#         countryCode = res.get('countryCode')[0],
#         email = res.get('email')[0],
#         employeeId = res.get('employeeId'),
#         messageType = ["Passcode", "Hq"]
#         result = test_downtown_employee_notify.employee_notify(self, token, brandId, mobile, countryCode, email, employeeId, messageType)
#         print(result, "这里是门店经理-notify")
#         if result.get('result') == {}:
#             print("创建门店经理信息发送成功")
#         else:
#             print("系统错误")

    # def test_employee_notify02(self):
    #     """给财务发送短信信息"""
    #     token = get_email_login_token.get_login_search_token()
    #     brandId = 600333,
    #     res = test_create_employee.test_downtown_create_employee().test_create_employee03().get('result')
    #     print("test_employee_notify02------", res)
    #     mobile = res.get('mobile'),
    #     countryCode = res.get('countryCode'),
    #     email = res.get('email'),
    #     employeeId = res.get('employeeId'),
    #     messageType = ["Hq"]
    #     result = test_downtown_employee_notify.employee_notify(self, token, brandId, mobile, countryCode, email, employeeId, messageType)
    #     print(result, " 这里是财务-notify")
    #     if result.get('result') == {}:
    #         print("创建财务信息发送成功")
    #     else:
    #         print("系统错误")

    # def test_employee_notify03(self):
    #     """给店员发送短信信息"""
    #     token = get_email_login_token.get_login_search_token()
    #     brandId = 600333,
    #     res = test_create_employee.test_downtown_create_employee().test_create_employee02().get('result')
    #     mobile = res.get('mobile')[0]
    #     countryCode = res.get('countryCode')[0]
    #     email = res.get('email')[0],
    #     employeeId = res.get('employeeId')
    #     messageType = ["Passcode"]
    #     result = test_downtown_employee_notify.employee_notify(self, token, brandId, mobile, countryCode, email, employeeId, messageType)
    #     print(result, " 这里是店员-notify")
    #     if result.get('result') == {}:
    #         print("创建店员信息发送成功")
    #     else:
    #         print("系统错误", result.get('result').get("code"), result.get('result').get("message"))
    #
    # def test_employee_notify04(self):
    #     """给管理员发送短信信息"""
    #     token = get_email_login_token.get_login_search_token()
    #     brandId = 600333,
    #     res = test_create_employee.test_downtown_create_employee().test_create_employee04().get('result')
    #     mobile = res.get('mobile')[0]
    #     countryCode = res.get('countryCode')[0]
    #     email = res.get('email')[0],
    #     employeeId = res.get('employeeId')
    #     messageType = ["Hq"]
    #     result = test_downtown_employee_notify.employee_notify(self, token, brandId, mobile, countryCode, email, employeeId, messageType)
    #     print(result, " 这里是管理员-notify")
    #     if result.get('result') == {}:
    #         print("创建管理员信息发送成功")
    #     else:
    #         print("系统错误", result.get('result').get("code"), result.get('result').get("message"))

