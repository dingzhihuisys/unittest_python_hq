# @dingzhihui   
# 2021/10/7   
# 1:52 下午   
# PyCharm
import yaml

from main import project_path


def get_mobile_login_token():
    yamlPath = project_path + '/case/hq_a_passPort/hq_login_token/login_mobile_token.yml'
    # yamlPath = '/Users/dingzhihui/dzh_test/PycharmProjects/unittest_python_hq/case/hq_a_passPort/hq_login_token/login_mobile_token.yml'
     # 获取yaml文件路径
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    login_mobile_token = f.read()
    f.close()
    login_monile_self_detail = yaml.load(login_mobile_token, Loader=yaml.FullLoader)
    # print(login_monile_self_detail.get('token'))
    return login_monile_self_detail.get('token')

def get_email_login_token():
    yamlPath = project_path + '/case/hq_a_passPort/hq_login_token/login_email_token.yml'
    # yamlPath = '/Users/dingzhihui/dzh_test/PycharmProjects/unittest_python_hq/case/hq_a_passPort/hq_login_token/login_mobile_token.yml'
    # 获取yaml文件路径
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    login_email_token = f.read()
    f.close()
    login_monile_self_detail = yaml.load(login_email_token, Loader=yaml.FullLoader)
    # print(login_monile_self_detail.get('token'))
    return login_monile_self_detail.get('token')

def get_login_search_token():
    yamlPath = project_path + '/case/hq_a_passPort/hq_login_token/get_login_search_token.yml'
    # yamlPath = '/Users/dingzhihui/dzh_test/PycharmProjects/unittest_python_hq/case/hq_a_passPort/hq_login_token/login_mobile_token.yml'
    # 获取yaml文件路径
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    login_email_token = f.read()
    f.close()
    login_monile_self_detail = yaml.load(login_email_token, Loader=yaml.FullLoader)
    # print(login_monile_self_detail.get('token'))
    return login_monile_self_detail.get('token')