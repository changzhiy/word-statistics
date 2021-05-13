# coding:utf-8

from collections import Counter
from os import path
import jieba
# 写入excel
import xlwt
# 引入正则表达式提取中文
import re

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)

jieba.load_userdict(path.join(path.dirname(__file__), 'userdict//userdict.txt'))  # 导入用户自定义词典

def remove(text):
    pattern = re.compile("[^\u4e00-\u9fa5]")  # 模式匹配所有中文字符

    return re.sub(pattern, '', text)

def word_segment(text):
    # 先去除标点
    text = remove(text)
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''

    # 计算每个词出现的频率，并存入txt文件
    jieba_word = jieba.cut(text, cut_all=False)  # cut_all是分词模式，True是全模式，False是精准模式，默认False
    data = []
    for word in jieba_word:
        data.append(word)
    dataDict = Counter(data)

    i = 0
    for k, v in dataDict.items():
        sheet.write(i, 0, k)
        sheet.write(i, 1, v)
        i += 1
        # 保存excel
    book.save('./result/result.xls')


    # 返回分词后的结果
    jieba_word = jieba.cut(text, cut_all=False)  # cut_all是分词模式，True是全模式，False是精准模式，默认False
    seg_list = ' '.join(jieba_word)
    return seg_list
