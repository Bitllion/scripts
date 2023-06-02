# -*- encoding: utf-8 -*-
"""
@文件        :spider.py
@说明        :爬虫核心函数
@时间        :2022/05/27 14:16:02
@作者        :fanyq
@版本        :1.0
"""
import time, random, json, pandas as pd
from qdata.baidu_index import get_search_index
from qdata.baidu_index.common import split_keywords


def spider(keywords_list, start_date, end_date, cookies):
    print("爬虫开始工作")
    all_list = []
    # 计时
    tic = time.time()
    # 遍历关键词
    for keywords in split_keywords(keywords_list):
        for index in get_search_index(
            keywords_list=keywords,
            start_date=start_date,
            end_date=end_date,
            cookies=cookies,
        ):
            if index["type"] == "all":
                s = {
                    "keyword": index["keyword"][0],
                    "date": index["date"],
                    "index_num": int(index["index"]),
                }
                all_list.append(s)
                print("正在爬取：%s" % index)
        # 随机睡眠，防止被屏蔽
        time.sleep(random.uniform(3, 5))
    toc = time.time()
    shijian = toc - tic
    print("耗时%.2f秒,爬取完成！\n开始写入json" % shijian)

    # 写入json
    with open(".\\data\\temp.json", "w") as f:
        f.write(json.dumps(all_list))
        print("写入json完成！")

    print("json转csv")
    # 写入csv
    df = pd.read_json(".\\data\\temp.json")
    df.to_csv(".\\data\\temp.csv", index=None)
    print("转csv完成！")
