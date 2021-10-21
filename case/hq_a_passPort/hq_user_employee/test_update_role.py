# @dingzhihui   
# 2021/10/8   
# 2:55 下午   
# PyCharm
import json
import unittest
import random

import requests
from case.hq_a_passPort import get_email_login_token
# 修改单个员工的岗位信息
from case.hq_a_passPort.hq_user_employee import test_list_employee, test_exist_same_no


class test_downtown_update_role(unittest.TestCase):
    def update_role(self, token, brandId, employee_id, promission_role_key, promission_role_id, storeIds, isStoreAll):
        url = "https://posuser.downtown8.net/employee/updateRole"
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
            "promissionRoleId": promission_role_id,
            "storeIds": storeIds,
            "isStoreAll": isStoreAll
        }
        res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
        return res.json()

    def get_role_is(self):
        list_key = ['storeManager', 'operationalManager', 'finance', 'server']
        list_id = [103, 105, 104, 107]
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        role_key = employee_id_op[0].get("promissionRoleKey")
        role_id = employee_id_op[0].get("promissionRoleId")
        if list_key.__contains__(role_key):
            list_key.remove(role_key)
            list_id.remove(role_id)
            random_index = random.randint(0, 2)
            role_key = list_key[random_index]
            role_id = list_id[random_index]
            key_id_list = [role_key, role_id]
            print("----get_role_is----", key_id_list)
            return key_id_list

    def test_update_role01(self):
        """修改员工的岗位信息"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        employee_id = employee_id_op[0].get("employeeId")
        # print("hahhahhahahhahhhhhhh", self.get_role_is()[0])
        promission_role_key = self.get_role_is()[0],
        # print("hahhahhahahhahhhhhhh", self.get_role_is()[1])
        promission_role_id = self.get_role_is()[1],
        storeIds = [801447],
        isStoreAll = 0
        result = test_downtown_update_role.update_role(self, token, brandId, employee_id, promission_role_key, promission_role_id, storeIds, isStoreAll)
        print("看这里", result)
        if result.get('result').get("employeeId") == {}:
            print("成功修改员工姓名：", result.get('result').get("employeeName"))
        else:
            print("系统报错", result.get('result').get("code"))