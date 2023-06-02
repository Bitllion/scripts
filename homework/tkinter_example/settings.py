# -*- encoding: utf-8 -*-
'''
@文件        :config.py
@说明        :配置类
@时间        :2022/06/07 20:20:45
@作者        :TM_FULLNAME
@版本        :1.0
'''
class Config(object):
    def __init__(self):
        self.icon_path = "data\\logo.ico"
        self.bg_path = "data\\bg.jpg"
        self.userinfo_path = "data\\userinfo.txt"
        self.video_path = "data\\tg.mp4"
        self.voice_path = "data\\tg.mp3"
        self.book_path = "data\\book.txt"
        self.image_list = ["data\gallery\\1.jpg", "data\gallery\\2.jpg", "data\gallery\\3.jpg"]
        self.exam_path = "data\\data.json"
        self.daotu_path = "data\\daotu.png"
config = Config()


    