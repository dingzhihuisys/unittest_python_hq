# @dingzhihui   
# 2021/11/4   
# 4:19 下午   
# PyCharm

import random
# 导入随机模块
def Random_Phone():
    phone_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                  "153", "155", "156", "157", "158", "159", "186", "187", "188", "173", "177", "180", "181", "189",
                  "199"]    # 创建一个正确的手机前三位列表
    random_phone = random.choice(phone_list) + "".join(random.choice("0123456789") for i in range(8))
    """
    随机选取前三位，之后字符串拼接，随机选取数字循环8次
    """
    return random_phone


print("随机生成的手机号为:{}".format(Random_Phone()))