# -*- encoding: utf-8 -*-
'''
@文件        :account.py
@说明        :读写userinfo.txt文件
@时间        :2022/06/07 20:51:36
@作者        :TM_FULLNAME
@版本        :1.0
'''
# 导入配置类
from settings import config

file_name = config.userinfo_path

def judge_txt(username):
    for line in open(file_name, "r", encoding='utf-8').readlines():
        user, pwd = line.strip().split("\t")
        if username == user:
            return True
    return False


def register_txt(username, password):
    if judge_txt(username):
        return False
    else:
        with open(file_name, "a", encoding='utf-8') as f:
            f.write(username + "\t" + password + "\n")
        return True


def login_txt(username, password):
    for line in open(file_name, "r", encoding='utf-8').readlines():
        user, pwd = line.strip().split("\t")
        if username == user and password == pwd:
            return True
    return False

'''
测试
'''
if __name__ == "__main__":
    import pathlib,os
    
    pathlib.Path(file_name).touch()
    # 第一次注册
    print("1.测试第一注册\n")
    if register_txt("22", "11"):
        print("注册成功\n")

    # #测试用户名
    # print("2.测试用户名重复\n")
    # if register_txt("test", "1234567"):
    #     register_txt("test", "1234567")
    #     print("注册成功！\n")
    # else:
    #     print("用户名已存在！\n")

    # #测试登录成功
    # print("3.测试登录成功\n")
    # if login_txt("test", "123456"):
    #     print("登录成功\n")
    # else:
    #     print("登录失败\n")

    # #测试登录失败
    # print("4.测试登录失败\n")
    # if login_txt("test", "1234567"):
    #     print("登录成功\n")
    # else:
    #     print("登录失败\n")

    # print("清空测试\n")
    # os.remove(file_name)
