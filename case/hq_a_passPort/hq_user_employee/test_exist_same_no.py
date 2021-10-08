# @dingzhihui   
# 2021/10/8   
# 2:27 下午   
# PyCharm

import json
import unittest
import requests
from case.hq_a_passPort import get_mobile_login_token
from case.hq_a_passPort.hq_user_employee import test_list_employee
from common import get_random_id

# 检查修改员工的员工id是否存在（唯一性）
class test_downtown_exist_same_no(unittest.TestCase):
    def exist_same_no(self, token, brandId, employee_id, employee_number):
        url = "https://posuser.downtown8.net/employee/existSameNo"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        data = {
            "employeeId": employee_id,
            "employeeNumber": employee_number
        }
        res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
        return res.json()

    def test_exist_same_no01(self):
        """检查修改后的员工编号是否已存在"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333
        employee_id_op = test_list_employee.test_downtown_list_employee().test_self_detail01()
        # print("看这里的内容", employee_id_op[0])
        employee_id = employee_id_op[0].get("employeeId")
        employee_number = get_random_id.get_random_id()  # 随机生成编码
        # 如编码不存在 返回false 已存在 返回true 并给编辑接口
        result = test_downtown_exist_same_no.exist_same_no(self, token, brandId, employee_id, employee_number)
        print("看这里", result)
        if result.get('result').get("isExist") is False:
            print("检查员工编号是品牌唯一：", employee_number)
            return employee_number
        else:
            print("系统报错", result.get('result').get("code"))