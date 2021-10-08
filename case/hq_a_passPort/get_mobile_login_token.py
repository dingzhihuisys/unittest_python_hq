# @dingzhihui   
# 2021/10/7   
# 1:52 下午   
# PyCharm
import yaml


def get_login_token():
    yamlPath = '/Users/dingzhihui/dzh_test/PycharmProjects/unittest_python_hq/case/hq_a_passPort/login_mobile_token.yml'
    # 获取yaml文件路径
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    login_monile_token = f.read()
    f.close()
    login_monile_self_detail = yaml.load(login_monile_token, Loader=yaml.FullLoader)
    # print(login_monile_self_detail.get('token'))
    return login_monile_self_detail.get('token')