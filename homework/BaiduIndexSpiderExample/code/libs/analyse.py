# -*- encoding: utf-8 -*-
"""
@文件        :analyse.py
@说明        :pandas分析数据
@时间        :2022/05/30 10:35:09
@作者        :fanyq
@版本        :1.0
"""
import os, json, pandas as pd
from config.settings import Config


def analyse(keywords_length):
    print("开始分析数据")
    df = pd.read_csv(".\\data\\temp.csv")
    # keyword分组 合算 每天到每月 的 index_num 数值 ，并重新将分组后的数据放入新的dataframe中
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").groupby("keyword").resample("m").sum().reset_index()
    # 保存
    df.to_csv(".\\data\sum.csv")

    # 转化为list
    list_df = pd.read_csv(".\\data\\sum.csv")
    index_list_df = list_df.groupby("keyword")["index_num"].apply(list)
    # 保存为json
    index_list = []

    for i in range(keywords_length):
        index_json = {
            "keyword": index_list_df.index[i],
            "index_sum": index_list_df.values[i],
        }
        index_list.append(index_json)

    with open(".\\data\\index_list.json", "w") as f:
        f.write(json.dumps(index_list))

    print("分析完成！")
    os.remove(".\\data\\temp.csv")
    os.remove(".\\data\\temp.json")
