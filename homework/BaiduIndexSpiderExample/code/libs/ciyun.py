import wordcloud, os, jieba
import numpy as np
from PIL import Image

def ciyun():
    pwd = os.getcwd()
    pic = Image.open(pwd+"\\data\\pikaqiu.jpg")
    shape = np.array(pic)
    wc = wordcloud.WordCloud(
        mask=shape, font_path="simkai.ttf", background_color="white", max_font_size=100
    )
    text = open(pwd + "\\data\\ci.txt", "r", encoding="UTF-8").read()
    cut_text = jieba.cut(text)
    result = " ".join(cut_text)
    wc.generate(result)
    wc.to_file(pwd + "\\data\\cloud.jpg")
