# @dingzhihui   
# 2021/10/7   
# 10:13 下午   
# PyCharm
import unittest
import requests
from case.hq_a_passPort import get_mobile_login_token
# 获取单个员工的信息与详情
from case.hq_a_passPort.hq_user_employee import test_list_employee
class test_downtown_detail_employee(unittest.TestCase):
    def detail_employee(self, token, brandId, employee_id):
        url = "https://posuser.downtown8.net/employee/detailEmployee"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "employeeId": employee_id,
            "brandId": brandId
        }
        res = requests.get(url, headers=headers, params=param)
        return res.json()

    def test_detail_employee01(self):
        """获取单个员工的信息"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        # print("看这里的内容", employee_id_op[0].get("employeeId"))
        employee_id = employee_id_op[0].get("employeeId")
        result = test_downtown_detail_employee.detail_employee(self, token, brandId, employee_id)
        # print("看这里", result)
        if result.get('result').get("employeeId") == employee_id_op[0].get("employeeId"):
            print("成功获取员工的信息，姓名：", result.get('result').get("employeeName"))
        else:
            print("系统报错", result.get('result').get("code"))