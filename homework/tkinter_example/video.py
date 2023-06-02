# -*- encoding: utf-8 -*-
"""
@文件        :video.py
@说明        : 视频播放器
@时间        :2022/06/07 20:55:32
@作者        :
@版本        :1.0
"""
# 导入配置类
from settings import config
import pygame as py
from tkinter import *

# 导入opencv
import cv2

# 导入PIL模块
from PIL import Image, ImageTk

# 导入多线程
import multiprocessing
from index import IndexWindow

# 初始化变量
window_width = 960
window_height = 720
imagepos_x = 0
imagepos_y = 0
butpos_x = 450
butpos_y = 450
vc1 = cv2.VideoCapture(config.video_path)


class VideoWindow(object):
    def __init__(self):
        self.roots = Tk()
        self.roots.geometry(str(window_width) + "x" + str(window_height))
        self.canvas = Canvas(
            self.roots, bg="white", width=window_width, height=window_height * 0.9
        )
        self.canvas.place(x=imagepos_x, y=imagepos_y)
        # 添加退出按钮
        Button(self.roots, text="退出", command=self.exit_win).place(
            x=butpos_x, y=window_height * 0.95
        )
        self.video()
        # p1 = multiprocessing.Process(target=self.video())
        # p1.start()

    # 图像转换，用于在画布中显示
    def tkImage(self):
        # 设置窗口标题
        self.roots.title("欢迎观看党史影片")
        # 设置icon
        self.roots.iconbitmap(config.icon_path)
        ref, frame = vc1.read()
        cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pilImage = Image.fromarray(cvimage)
        pilImage = pilImage.resize((window_width, window_height), Image.ANTIALIAS)
        tkImage = ImageTk.PhotoImage(image=pilImage)
        return tkImage

    # 图像的显示与更新
    def video(self):
        def video_loop():
            try:
                while True:
                    picture1 = self.tkImage()
                    self.canvas.create_image(0, 0, anchor="nw", image=picture1)
                    self.roots.update_idletasks()  # 最重要的更新是靠这两句来实现
                    self.roots.update()
            except:
                pass

        video_loop()
        self.roots.mainloop()
        vc1.release()
        cv2.destroyAllself.rootsdows()

    def exit_win(self):
        # 关闭窗口
        self.roots.destroy()
        # 打开主页
        IndexWindow()
        # # 关闭所有进程
        # self.p1.terminate()
        # self.p2.terminate()
        # 关闭所有窗口
        cv2.destroyAllWindows()
        # 退出程序
        exit()


class Voice(object):
    def __init__(self):
        py.mixer.init()
        # 文件加载
        track = py.mixer.music.load(config.voice_path)
        # 播放，第一个是播放值 -1代表循环播放， 第二个参数代表开始播放的时间
        py.mixer.music.play(-1, 0)
        while 1:  # 一定要有whlie让程序暂停在这，否则会自动停止self.roots
            pass


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=VideoWindow())
    p1.start()
    p2 = multiprocessing.Process(target=Voice())

    p2.start()
