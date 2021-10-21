# @dingzhihui   
# 2021/10/7   
# 2:53 下午   
# PyCharm
import json
import unittest
import requests
# 获取员工列表
from case.hq_a_passPort import get_email_login_token

# 获取岗位信息
# 获取门店信息
# 获取生成的四位码
from case.hq_a_passPort.hq_user_employee import test_role_list, test_get_passcode
from common import get_random_name

# 创建员工
class test_downtown_create_employee(unittest.TestCase):
    def create_employee(self, token, brandId, employee_name, email, mobile, countryCode, promission_role_id, promission_role_key, is_store_all, pass_code):
        url = "https://posuser.downtown8.net/employee/createEmployee"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId
        }
        data = {
            "employeeName": employee_name,
            "email": email,
            "mobile": mobile,
            "countryCode": countryCode,
            "promissionRoleId": promission_role_id,
            "promissionRoleKey": promission_role_key,
            "isStoreAll": is_store_all,
            "passcode": pass_code
        }
        res = requests.post(url, headers=headers, params=param, data=json.dumps(data))
        return res.json()

    def test_create_employee01(self):
        """创建 门店经理"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333,
        employee_name = get_random_name.random_name(),
        # print(employee_name, "姓名000000")
        email = "",
        mobile = "13877349823",
        countryCode = "86",
        promission_role_id = test_role_list.test_downtown_role_list().test_self_detail01().get("promissionRoleId"),
        # print(test_role_list.test_downtown_role_list().test_self_detail01(), "哈哈哈哈哈哈哈")
        promission_role_key = test_role_list.test_downtown_role_list().test_self_detail01().get('promissionRoleKey'),
        # print(promission_role_key, "职位------")
        is_store_all = True,
        pass_code = test_get_passcode.test_downtown_get_passcode().test_get_passcode01()
        # print(pass_code, "4位码 ---7439827423")
        result = test_downtown_create_employee.create_employee(self, token, brandId, employee_name, email, mobile, countryCode, promission_role_id, promission_role_key, is_store_all, pass_code)
        print(result, "------")
        if result.get('result').get("employeeName")[0] == employee_name[0]:
            print("成功添加员工：", employee_name, "职位：", promission_role_key, "员工id：", result.get('result').get("employeeId"))
            return result
        else:
            print("添加员工失败：", result.get('result'))

    def test_create_employee02(self):
        """创建-- 店员"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333,
        employee_name = get_random_name.random_name(),
        # print(employee_name, "姓名000000")
        email = "34094235248@qq.com",
        mobile = "",
        countryCode = "",
        promission_role_id = test_role_list.test_downtown_role_list().test_self_detail04().get("promissionRoleId"),
        # print(test_role_list.test_downtown_role_list().test_self_detail04(), "哈哈哈哈哈哈哈")
        promission_role_key = test_role_list.test_downtown_role_list().test_self_detail04().get('promissionRoleKey'),
        # print(promission_role_key, "职位------")
        is_store_all = True,
        pass_code = test_get_passcode.test_downtown_get_passcode().test_get_passcode01()
        # print(pass_code, "4位码 ---7439827423")
        result = test_downtown_create_employee.create_employee(self, token, brandId, employee_name, email, mobile, countryCode, promission_role_id, promission_role_key, is_store_all, pass_code)
        # print(result, "------")
        if result.get('result').get("employeeName")[0] == employee_name[0]:
            print("成功添加员工：", employee_name, "职位：", promission_role_key, "员工id：", result.get('result').get("employeeId"))
            return result
        else:
            print("添加员工失败：", result.get('result'))

    def test_create_employee03(self):
        """创建----- 财务"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333,
        employee_name = get_random_name.random_name(),
        # print(employee_name, "姓名000000")
        email = "34094235248@qq.com",
        mobile = "",
        countryCode = "",
        promission_role_id = test_role_list.test_downtown_role_list().test_self_detail02().get("promissionRoleId"),
        # print(test_role_list.test_downtown_role_list().test_self_detail04(), "哈哈哈哈哈哈哈")
        promission_role_key = test_role_list.test_downtown_role_list().test_self_detail02().get('promissionRoleKey'),
        # print(promission_role_key, "职位------")
        is_store_all = True,
        pass_code = ''
        # print(pass_code, "4位码 ---7439827423")
        result = test_downtown_create_employee.create_employee(self, token, brandId, employee_name, email, mobile, countryCode, promission_role_id, promission_role_key, is_store_all, pass_code)
        # print(result, "------")
        if result.get('result').get("employeeName")[0] == employee_name[0]:
            print("成功添加员工：", employee_name, "职位：", promission_role_key, "员工id：", result.get('result').get("employeeId"))
            return result
        else:
            print("添加员工失败：", result.get('result'))

    def test_create_employee04(self):
        """创建----- 管理员"""
        token = get_email_login_token.get_login_search_token()
        brandId = 600333,
        employee_name = get_random_name.random_name(),
        # print(employee_name, "姓名000000")
        email = "34094235248@qq.com",
        mobile = "",
        countryCode = "",
        promission_role_id = test_role_list.test_downtown_role_list().test_self_detail03().get("promissionRoleId"),
        # print(test_role_list.test_downtown_role_list().test_self_detail04(), "哈哈哈哈哈哈哈")
        promission_role_key = test_role_list.test_downtown_role_list().test_self_detail03().get('promissionRoleKey'),
        # print(promission_role_key, "职位------")
        is_store_all = True,
        pass_code = ''
        # print(pass_code, "4位码 ---7439827423")
        result = test_downtown_create_employee.create_employee(self, token, brandId, employee_name, email, mobile, countryCode, promission_role_id, promission_role_key, is_store_all, pass_code)
        # print(result, "------")
        if result.get('result').get("employeeName")[0] == employee_name[0]:
            print("成功添加员工：", employee_name, "职位：", promission_role_key, "员工id：", result.get('result').get("employeeId"))
            return result
        else:
            print("添加员工失败：", result.get('result'))
