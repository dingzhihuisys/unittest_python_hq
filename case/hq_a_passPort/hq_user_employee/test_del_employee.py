# @dingzhihui   
# 2021/10/8   
# 5:35 下午   
# PyCharm
import json
import unittest
import requests
from case.hq_a_passPort import get_mobile_login_token
# 获取单个员工的信息与详情
from case.hq_a_passPort.hq_user_employee import test_list_employee
class test_downtown_del_employee(unittest.TestCase):
    def del_employee(self, token, brandId, employee_id,promission_role_key):
        url = "https://posuser.downtown8.net/employee/delEmployee"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        data = {
            "employeeId": employee_id,
            "promissionRoleKey": promission_role_key
        }
        res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
        return res.json()

    # def test_del_employee01(self):
    #     """删除第一个获取的是门店经理的员工 删除"""
    #     token = get_mobile_login_token.get_login_token()
    #     brandId = 600333
    #     employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
    #     employee_id = employee_id_op[0].get("employeeId")
    #     promission_role_key = ''
    #     result = test_downtown_del_employee.del_employee(self, token, brandId, employee_id, promission_role_key)

    # def test_del_employee02(self):
    #     """删除第一个获取的是财务的员工 删除"""
    #     token = get_mobile_login_token.get_login_token()
    #     brandId = 600333
    #     employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
    #     employee_id = employee_id_op[0].get("employeeId")
    #     promission_role_key = ''
    #     result = test_downtown_del_employee.del_employee(self, token, brandId, employee_id, promission_role_key)

    def test_del_employee03(self):
        """删除第一个获取的是员工 删除"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        print("---------------", type(employee_id_op))
        list_id_name = self.delete_element_form_list(employee_id_op, 'operationalManager')
        employee_id = list_id_name[0]
        promission_role_key = list_id_name[1]
        result = test_downtown_del_employee.del_employee(self, token, brandId, employee_id, promission_role_key)
        print('test_del_employee03', result)

    #
    # def test_del_employee04(self):
    #     """删除第一个获取的是管理员 删除"""
    #     token = get_mobile_login_token.get_login_token()
    #     brandId = 600333
    #     employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
    #     employee_id = employee_id_op[0].get("employeeId")
    #     promission_role_key = ''
    #     result = test_downtown_del_employee.del_employee(self, token, brandId, employee_id, promission_role_key)

    def delete_element_form_list(self, employee_list, role_name):
        for employee in employee_list:
            if employee.get('promissionRoleKey') == role_name:
                return [employee.get('employeeId'), role_name]
            else:
                return "系统报错"

