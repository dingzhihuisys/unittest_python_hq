# @dingzhihui   
# 2021/10/7   
# 4:02 下午   
# PyCharm
import random as r
def random_name():
    frist_name = ["时","郝","包","朱","魏","贾","谢","荣","宋",
                  "苏","田","盛","孔","马","戚","钱","徐","崔",
                  "房","高","祝","皮","戚","管","贺","陆","岑",
                  "马","樊","莫","湛","昌","朱","邓","裘","徐",
                  "姚","褚","卜","黄","鲍","孟","裴","贺","周",
                  "云","赵","贝","和","方","严","章","潘","汤",
                  "胡","鲁","米","杨","毕","尹","余","周","樊"]
    last_name = ["艳峰","晓梅","晓强","小强","高峰","晓强","成丽",
                 "长全","春鹏","春峰","成娟","成丽","长丽","小梅",
                 "高梅","小娟","高鹏","春梅","小鹏","春全","晓梅",
                 "成全","晓强","高娟","春梅","长峰","小梅","成娟",
                 "艳全","小全","春丽","长峰","晓梅","艳丽","春娟",
                 "高丽","春强","小峰","高梅","长娟","艳鹏","晓鹏",
                 "小娟","晓强","晓全","春峰","春丽","成鹏","高峰"]
    for i in range(1):
        name = r.choice(frist_name) + r.choice(last_name)
        return name
