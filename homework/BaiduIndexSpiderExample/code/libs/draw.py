import matplotlib.pyplot as plt
import sys, json, pandas as pd
import numpy as np

sys.path.append(".")


from libs.time import get_date_list

# fig, axes = plt.subplots(1, 1, figsize=(8, 4))


def get_index_list(keyword):
    with open(".\\data\\index_list.json", "r") as f:
        date_list_json = json.load(f)

    for i in range(len(keyword)):
        if date_list_json[i]["keyword"] == keyword:
            return date_list_json[i]["index_sum"]


def draw_single_line(keyword):
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.xlabel("时间")
    plt.ylabel("指数")
    plt.plot(get_date_list(), get_index_list(keyword))
    plt.title("%s" % keyword)
    plt.grid()
    plt.savefig(".\\data\\%s_single_line.png" % keyword)
    plt.close()


def draw_single_bar(keyword):
    plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
    plt.xlabel("时间")
    plt.ylabel("指数")
    plt.bar(get_date_list(), get_index_list(keyword))
    plt.title("%s" % keyword)
    plt.savefig(".\\data\\%s_single_bar_.png" % keyword)
    plt.close()


def draw_mulite_pie(list):
    print("开始绘制饼多图")
    x = 1
    for i in list:
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
        plt.subplot(1, 2, x)
        x = x + 1
        plt.xticks(rotation=30)
        plt.pie(get_index_list(i), labels=get_date_list(), autopct="%.2f%%")
        plt.title("%s" % i)
        plt.suptitle("饼图")
    plt.savefig(".\\data\\mulite_pie.png")
    plt.close()
    print("绘制完毕")


def draw_mulite_bar(list):
    print("开始绘制柱状多图")
    x = 1
    for i in list:
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
        plt.xlabel("时间")
        plt.ylabel("指数")
        plt.subplot(1, 2, x)
        x = x + 1
        plt.xticks(rotation=30)
        plt.bar(get_date_list(), get_index_list(i))
        plt.title("%s" % i)
        plt.suptitle("柱状图图")
    plt.savefig(".\\data\\mulite_bar.png")
    plt.close()
    print("绘制完毕")


def draw_mulite_matrix(list):
    print("开始绘制矩阵点多图")
    x = 1
    for i in list:
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
        plt.xlabel("时间")
        plt.ylabel("指数")
        plt.subplot(1, 2, x)
        x = x + 1
        plt.xticks(rotation=30)
        plt.scatter(get_date_list(), get_index_list(i))
        plt.grid()
        plt.colorbar()
        plt.title("%s" % i)
        plt.suptitle("散点图")
    plt.savefig(".\\data\\mulite_scatter.png")
    plt.close()
    print("绘制完毕")


def draw_mulite_line(list):
    print("开始绘制折线多图")
    date_list = get_date_list()
    x = 1
    for i in list:
        plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
        plt.xlabel("时间")
        plt.ylabel("指数")
        plt.subplot(1, 2, x)
        x = x + 1
        plt.xticks(rotation=30)
        plt.plot(date_list, get_index_list(i))
        plt.grid()
        plt.title("%s" % i)
        plt.suptitle("折线图")
    plt.savefig(".\\data\\mulite_line.png")
    plt.close()
    print("绘制完毕!")
