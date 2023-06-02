# -*- encoding: utf-8 -*-
"""
@文件        :init.py
@说明        :启动程序
@时间        :2022/05/30 11:03:30
@作者        :fanyq
@版本        :1.0
"""
from datetime import date
from config.settings import Config
from libs.spider import spider
from libs.analyse import analyse
from libs.draw import *
from libs.ciyun import ciyun
# 绘图
def draw():
    pass


if __name__ == "__main__":
    # 初始化
    keywords = [["抑郁症"], ["疫情"]]
    config = Config(
        keywords_list=keywords, start_date=date(2020, 1, 1), end_date=date(2022, 5, 30)
    )
    keywords_list = config.keywords_list
    start_date = config.start_date
    end_date = config.end_date
    config.cookies = config.cookies
    # 爬虫
    spider(keywords_list, start_date, end_date, config.cookies)
    # 分析
    analyse(len(keywords_list))
    # 绘图
    keyword_list = []
    for i in keywords:
        keyword_list.append(i[0])
        #折线图
        draw_single_line(i[0])
        #柱状图
        draw_single_bar(i[0])
    draw_mulite_line(keyword_list)
    draw_mulite_matrix(keyword_list)
    draw_mulite_bar(keyword_list)
    draw_mulite_pie(keyword_list)
    
    #词云
    ciyun()