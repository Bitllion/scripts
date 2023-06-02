# -*- encoding: utf-8 -*-
"""
@文件        :login.py
@说明        :登录窗口
@时间        :2022/06/07 19:42:15
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入配置类
from settings import config

# 导入账户读写模块
from account import *

# 导入tkinter模块
from tkinter import *
from tkinter import messagebox

# 导入注册窗口模块
from register import RegisterWindow
from index import IndexWindow

class LoginWindow(object):
    def __init__(self):
        self.roots = Tk()

        # 设置窗口大小
        self.roots.geometry("480x240")
        # 禁止调整窗口大
        self.roots.resizable(0, 0)
        # 设置窗口标题
        self.roots.title("欢迎观看党史展")
        # 设置logo
        self.roots.iconbitmap(config.icon_path)

        # 创建横幅标签,grid()控件布局管理器，以行、列的形式对控件进行布局, 将横幅标签放置在窗口中,位置为(0,0)，距离左边距离为0，上边距离为0
        label0 = Label(
            self.roots,
            text=" 热烈庆祝中国共产党成立100周年! ",
            bg="red",
            fg="yellow",
            font=("Times", 20, "bold italic"),
            width=30,
            height=2,
        ).grid(row=0, column=0, columnspan=2, sticky=W)

        # 新建文本标签，将文本标签放置在窗口中，位置为(1,0)，距离左边距离为0，上边距离为0
        label_username = Label(
            self.roots, text="账号：", font=("Times", 20, "bold italic")
        ).grid(row=1, sticky=W)
        label_password = Label(
            self.roots, text="密码：", font=("Times", 20, "bold italic")
        ).grid(row=2, sticky=W)

        # 创建两个输入框控件,并将输入内容绑定到变量var_username和var_passwor,其中密码输入框设置为密文显示
        self.var_username = StringVar()
        self.var_password = StringVar()

        self.entry_username = Entry(
            self.roots,
            textvariable=self.var_username,
            font=("Times", 20, "bold italic"),
        ).grid(row=1, column=1, sticky=W)
        self.entry_password = Entry(
            self.roots,
            textvariable=self.var_password,
            font=("Times", 20, "bold italic"),
            show="*",
        ).grid(row=2, column=1, sticky=W)

        # 新建三个按钮，并绑定事件，设置布局
        btn_login = Button(
            self.roots, text="登录", font=("bold italic", 10), command=self.fun_login
        ).grid(row=3, column=0, sticky=W, padx=10, pady=5)

        # 注册
        btn_register = Button(
            self.roots, text="注册", font=("bold italic", 10), command=self.win_register
        ).grid(row=3, column=1, sticky=W, padx=10, pady=5)

        btn_canncle = Button(
            self.roots, text="取消", font=("bold italic", 10), command=self.fun_canncle
        ).grid(row=4, column=1, sticky=W, padx=10, pady=5)
        # 启动消息循环
        self.roots.mainloop()

    # 登录事件
    def fun_login(self):
        username = self.var_username.get()
        password = self.var_password.get()
        if username and password:
            if judge_txt(username):
                if login_txt(username, password):
                    messagebox.showinfo("登录成功", "欢迎您，" + username)
                    self.win_index()
                else:
                    messagebox.showerror("登录失败", "用户名或密码错误")
            else:
                messagebox.showerror("登录失败", "用户名不存在")
        else:
            messagebox.showwarning("登录失败", "用户名或密码不能为空")

    # 注册事件窗口
    def win_register(self):
        self.roots.destroy()
        RegisterWindow()

    # 清空输入框内容
    def fun_canncle(self):
        self.var_password.set("")
        self.var_username.set("")

    def win_index(self):
        self.roots.destroy()
        IndexWindow()

if __name__ == "__main__":
    LoginWindow()
