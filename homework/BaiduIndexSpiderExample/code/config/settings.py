# -*- encoding: utf-8 -*-
"""
@文件        :settings.py
@说明        :配置类
@时间        :2022/05/27 10:06:20
@作者        :fanyq
@版本        :1.0
"""
import sys

sys.path.append(".")
import libs.time as time
from qdata.baidu_login import get_cookie_by_qr_login


class Config(object):
    def __init__(self, **kwargs):

        timemap = time.generate_date(kwargs.get("start_date"), kwargs.get("end_date"))
        self.start_date = timemap[0]
        self.end_date = timemap[-1]

        self.keywords_list = kwargs.get("keywords_list")
        self.cookies = get_cookie_by_qr_login()
