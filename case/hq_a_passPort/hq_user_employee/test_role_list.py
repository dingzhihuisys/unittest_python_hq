# @dingzhihui   
# 2021/10/7   
# 3:11 下午   
# PyCharm
import unittest
import requests
# 获取员工列表
from case.hq_a_passPort import get_mobile_login_token

# 获取岗位信息
class test_downtown_role_list(unittest.TestCase):
    def role_list(self, token, brandId, promission_key, promission_app_id):
        url = "https://posuser.downtown8.net/employee/roleList"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId,
            "promissionKey": promission_key,
            "promissionAppId": promission_app_id,
        }
        res = requests.get(url, headers=headers, params=param)
        return res.json()

    def test_self_detail01(self):
        """获取岗位信息-----门店经理"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333,
        promission_key = 'add',
        promission_app_id = 33
        result = test_downtown_role_list.role_list(self, token, brandId, promission_key, promission_app_id)
        print(result)
        print(result.get('result')[0].get('promissionRoleId'))
        if result.get('result')[0].get('promissionRoleId') == 103:
            print("获取到当前的职位是：", result.get('result')[0].get('name'), result.get('result')[0].get('roleKey'))
            print(result.get('result')[0], "这里需要获取单个列表")
            return result.get('result')[0]
        else:
            print("系统报错")

    def test_self_detail02(self):
        """获取岗位信息-----财务"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333,
        promission_key = 'add',
        promission_app_id = 33
        result = test_downtown_role_list.role_list(self, token, brandId, promission_key, promission_app_id)
        print(result)
        print(result.get('result')[1].get('promissionRoleId'))
        if result.get('result')[1].get('promissionRoleId') == 104:
            print("获取到当前的职位是：", result.get('result')[1].get('name'), result.get('result')[1].get('roleKey'))
            return result.get('result')[1]
        else:
            print("系统报错")

    def test_self_detail03(self):
        """获取岗位信息-----管理员"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333,
        promission_key = 'add',
        promission_app_id = 33
        result = test_downtown_role_list.role_list(self, token, brandId, promission_key, promission_app_id)
        print(result)
        print(result.get('result')[2].get('promissionRoleId'))
        if result.get('result')[2].get('promissionRoleId') == 105:
            print("获取到当前的职位是：", result.get('result')[2].get('name'), result.get('result')[2].get('roleKey'))
            return result.get('result')[2]
        else:
            print("系统报错")

    def test_self_detail04(self):
        """获取岗位信息-----店员"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333,
        promission_key = 'add',
        promission_app_id = 33
        result = test_downtown_role_list.role_list(self, token, brandId, promission_key, promission_app_id)
        print(result)
        print(result.get('result')[3].get('promissionRoleId'))
        if result.get('result')[3].get('promissionRoleId') == 107:
            print("获取到当前的职位是：", result.get('result')[3].get('name'), result.get('result')[3].get('roleKey'))
            return result.get('result')[3]
        else:
            print("系统报错")