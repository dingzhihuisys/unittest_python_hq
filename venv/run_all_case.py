# @dingzhihui   
# 2021/6/7
# 6:32 下午   
# PyCharm
import os
import unittest
start_dir = "/Users/dingzhihui/dzh_test/PycharmProjects/unittest_python_hq/case"
def all_case():
    # 待执行用例的目录
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(start_dir, pattern="test*.py", top_level_dir=None)
    # discover方法筛选出用例，循环添加到测试套件中
    # for test_suit in discover:
    #     for test_case in test_suit:
    #         # 添加用力到testcase
    testcase.addTests(discover)
    print(testcase)
    return testcase


if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run 所有用例
    runner.run(all_case())





