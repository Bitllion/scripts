# -*- encoding: utf-8 -*-
"""
@文件        :index.py
@说明        :
@时间        :2022/06/07 20:06:04
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入tkinter模块
from tkinter import *
from tkinter import messagebox

# 导入PIL模块
from PIL import Image, ImageTk

# 导入配置类
from settings import config


def get_img(filename, width, height):
    im = Image.open(filename).resize((width, height))
    im = ImageTk.PhotoImage(im)
    return im


class IndexWindow(object):
    def __init__(self):
        # 创建窗口
        self.roots = Tk()
        # 最大化窗口
        # self.roots.state('zoomed')
        # 禁止调整窗口大
        self.roots.resizable(0, 0)
        # 设置窗口标题
        self.roots.title("庆祝建党100周年展示")
        # 设置icon
        self.roots.iconbitmap(config.icon_path)
        # 背景
        canvas = Canvas(self.roots, width=1645, height=805)
        photo = get_img(config.bg_path, 1645, 805)
        canvas.create_image(0, 0, anchor=NW, image=photo)
        canvas.pack()

        # 创建vidoe按钮
        button_video = Button(
            self.roots,
            width=200,
            height=100,
            text="短视频",
            font=("ariel", 30, "bold"),
            bg="yellow",
            fg="red",
            command=self.win_video,
        )
        canvas.create_window(300, 300, width=200, height=100, window=button_video)
        # 创建book按钮
        button_book = Button(
            self.roots,
            width=200,
            height=100,
            text="书籍",
            font=("ariel", 30, "bold"),
            bg="yellow",
            fg="red",
            command=self.win_book,
        )
        canvas.create_window(600, 300, width=200, height=100, window=button_book)
        # 创建gallery按钮
        button_gallery = Button(
            self.roots,
            width=200,
            height=100,
            text="图片",
            font=("ariel", 30, "bold"),
            bg="yellow",
            fg="red",
            command=self.win_gallery,
        )
        canvas.create_window(900, 300, width=200, height=100, window=button_gallery)
        # 创建qa按钮
        button_qa = Button(
            self.roots,
            width=200,
            height=100,
            text="问答",
            font=("ariel", 30, "bold"),
            bg="yellow",
            fg="red",
            command=self.win_qa,
        )
        canvas.create_window(1200, 300, width=200, height=100, window=button_qa)
        # 创建summary按钮
        button_summary = Button(
            self.roots,
            width=200,
            height=100,
            text="总结",
            font=("ariel", 30, "bold"),
            bg="yellow",
            fg="red",
            command=self.win_summary,
        )
        canvas.create_window(750, 500, width=200, height=100, window=button_summary)

        self.roots.mainloop()

    def win_summary(self):
        self.roots.destroy()
        from summary import SummaryWindow

        SummaryWindow()

    def win_qa(self):
        self.roots.destroy()
        from qa import QaWindow

        QaWindow()

    def win_gallery(self):
        self.roots.destroy()
        from gallery import GalleryWindow

        GalleryWindow()

    def win_book(self):
        self.roots.destroy()
        from book import BookWindow

        BookWindow()

    def win_video(self):
        self.roots.destroy()
        from video import VideoWindow

        VideoWindow()


if __name__ == "__main__":
    IndexWindow()
