# -*- encoding: utf-8 -*-
"""
@文件        :gallery.py
@说明        :
@时间        :2022/06/07 23:57:47
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入tkinter模块
from tkinter import *
from PIL import Image, ImageTk
from settings import config
import random
from index import IndexWindow

image_list = config.image_list


class GalleryWindow(object):
    def __init__(self):
        self.roots = Tk()
        # 设置窗口大小
        self.roots.geometry("1360x680")
        # 禁止调整窗口大
        self.roots.resizable(0, 0)
        # 设置窗口标题
        self.roots.title("党史照片展")
        # 设置icon
        self.roots.iconbitmap(config.icon_path)
        image = Image.open(random.choice(image_list)).resize((1360, 650))
        py_imgage = ImageTk.PhotoImage(image)

        self.label = Label(self.roots, image=py_imgage)
        self.label.grid(row=1, column=0, columnspan=3)

        # 添加按钮
        Button(self.roots, text="随机一张", command=self.previous).grid(row=2, column=0)
        # 添加退出按钮
        Button(self.roots, text="退出", command=self.exit_window).grid(row=2, column=1)
        self.roots.mainloop()

    def exit_window(self):
        self.roots.destroy()
        IndexWindow()

    def previous(self):
        try:
            self.roots.destroy()
            GalleryWindow()
            # 从image_list 随机获取图片
            image = Image.open(random.choice(image_list)).resize((1360, 650))
            py_imgage = ImageTk.PhotoImage(image)
            # 更新图片
            label = Label(self.roots, image=py_imgage)
            label.grid(row=1, column=0, columnspan=3)
        except:
            pass


if __name__ == "__main__":
    GalleryWindow()
