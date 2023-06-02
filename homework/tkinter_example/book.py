# -*- encoding: utf-8 -*-
"""
@文件        :book.py
@说明        : 书籍播放器
@时间        :2022/06/07 22:33:46
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入tkinter模块
from tkinter import *
from tkinter import messagebox

# 导入配置类
from settings import config
from index import IndexWindow


class BookWindow(object):
    def __init__(self):
        self.roots = Tk()
        # 设置窗口大小
        self.roots.geometry("500x800")
        # 禁止调整窗口大
        self.roots.resizable(0, 0)
        # 设置窗口标题
        self.roots.title("欢迎观看党史展")
        # 设置icon
        self.roots.iconbitmap(config.icon_path)

        text = Text(self.roots, width=500, height=780)
        scroll = Scrollbar()
        # 放到窗口的右侧, 填充Y竖直方向
        scroll.pack(side=RIGHT, fill=Y)

        # 两个控件关联
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)

        text.pack()
        with open(config.book_path, "r", encoding="utf-8") as f:
            str1 = f.read()

        text.insert(INSERT, str1)

        # 添加退出按钮
        Button(self.roots, text="退出", command=self.exit_win).place(x=450, y=0)
        self.roots.mainloop()

    def exit_win(self):
        self.roots.destroy()
        IndexWindow()


if __name__ == "__main__":
    book = BookWindow()
