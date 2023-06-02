# -*- encoding: utf-8 -*-
"""
@文件        :summary.py
@说明        :总结窗口
@时间        :2022/06/08 03:17:24
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入tkinter模块
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from matplotlib.pyplot import text

# 导入配置类
from settings import config


class SummaryWindow(object):
    def __init__(self) -> None:
        self.roots = Tk()
        # 设置窗口大小
        self.roots.geometry("800x400")
        # 禁止调整窗口大
        self.roots.resizable(0, 0)
        # 设置窗口标题
        self.roots.title("总结")
        # 设置icon
        self.roots.iconbitmap(config.icon_path)

        # 放置图片
        img = Image.open(config.daotu_path).resize((800, 300))
        py_imgage = ImageTk.PhotoImage(img)
        label_img = Label(self.roots, image=py_imgage)
        label_img.pack()

        # 放置文本
        text1 = Label(
            self.roots,
            text="1.课程应用与本专业结合如下：xxx",
            width=100,
            font=("宋体", 12),
            justify=LEFT,
        )
        text1.pack()

        text2 = Label(
            self.roots,
            text="2.建议如下：xxx",
            width=100,
            font=("宋体", 12),
            justify=LEFT,
        )
        text2.pack()

        # 返回按钮
        Button(
            self.roots,
            text="返回",
            width=10,
            height=2,
            font=("宋体", 12),
            command=self.back,
        ).pack()
        self.roots.mainloop()
    def back(self):
        self.roots.destroy()
        from index import IndexWindow
        IndexWindow()

if __name__ == "__main__":
    SummaryWindow()
