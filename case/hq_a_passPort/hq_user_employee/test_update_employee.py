# @dingzhihui   
# 2021/10/8   
# 11:34 上午   
# PyCharm
import json
import unittest
import requests
from case.hq_a_passPort import get_email_login_token
# 修改单个员工的基本信息
from case.hq_a_passPort.hq_user_employee import test_list_employee, test_exist_same_no
from common import get_random_id

class test_downtown_update_employee(unittest.TestCase):
    def update_employee(self, token, brandId, employee_id, promission_role_key, employee_name, employee_number, email, mobile, countryCode):
        url = "https://posuser.downtown8.net/employee/updateEmployee"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        data = {
            "employeeId": employee_id,
            "promissionRoleKey": promission_role_key,
            "employeeName": employee_name,
            "employeeNumber": employee_number,
            "email": email,
            "mobile": mobile,
            "countryCode": countryCode
        }
        res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
        return res.json()

    def test_update_employee01(self):
        """修改员工的基本信息-编号"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        # print("看这里的内容", employee_id_op[0])
        employee_id = employee_id_op[0].get("employeeId")
        promission_role_key = employee_id_op[0].get("promissionRoleKey"),
        # employee_name = "戚高峰", get_random_id.get_random_id()
        employee_name = employee_id_op[0].get("employeeName")
        # print("快点看这里----", employee_name)
        # 获取到检验接口返回的：employee_number
        employee_number = test_exist_same_no.test_downtown_exist_same_no().test_exist_same_no01(),
        email = "34094235248@qq.com",
        mobile = "",
        countryCode = '86'
        result = test_downtown_update_employee.update_employee(self, token, brandId, employee_id, promission_role_key, employee_name, employee_number, email, mobile, countryCode)
        # print("看这里", result)
        if result.get('result').get("employeeId") == {}:
            print("成功修改员工的编号，姓名：", result.get('result').get("employeeName"))
        else:
            print("系统报错", result.get('result').get("code"))
