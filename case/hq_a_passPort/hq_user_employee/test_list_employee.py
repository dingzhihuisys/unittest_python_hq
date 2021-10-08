# @dingzhihui   
# 2021/10/7   
# 2:03 下午   
# PyCharm
import unittest
import requests
# 获取员工列表
from case.hq_a_passPort import get_mobile_login_token


class test_downtown_list_employee(unittest.TestCase):
    def list_employee(self, token, brandId, page_no, page_size, store_ids, promission_role_id, query):
        url = "https://posuser.downtown8.net/employee/listEmployee"
        headers = {
            "content-type": "application/json; charset=utf-8",
            "token": token
        }  # get方法其它加个ser-Agent就可以了
        param = {
            "brandId": brandId,
            "pageNo": page_no,
            "pageSize": page_size,
            "storeIds": store_ids,
            "promissionRoleId": promission_role_id,
            "query": query
        }
        res = requests.post(url, headers=headers, params=param)
        return res.json()

    def test_self_detail01(self):
        """获取员工列表"""
        token = get_mobile_login_token.get_login_token()
        brandId = 600333,
        page_no = 1,
        page_size = 10000,
        store_ids = [],
        promission_role_id = '',
        query = ''
        result = test_downtown_list_employee.list_employee(self, token, brandId, page_no, page_size, store_ids, promission_role_id, query)
        print("--获取员工的列表--", result)
        if result.get('result').get("totalElements") >= 0:
            # print("员工信息", result.get('result').get("content"))
            print("成功获取信息列表共计：", result.get('result').get("totalElements"), "条员工信息")
            print("999999：", result.get('result').get("content"), "条员工信息")
            return result.get('result').get("content")
