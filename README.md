# Python词频统计:speech_balloon:

## 介绍:smile:

> 用python进行文本分词并生成词云，对HungryGoogle的wordCloud-master做了一定的改动，可以将结果输出到Excel，并且屏蔽了标点符号和空格，和其他的小改动，使程序更号用。原项目链接https://github.com/HungryGoogle/wordCloud-master

## 主要需要的包：

- jieba
- wordcloud

## 其他

* 分词采用结巴分词，并支持自定义字典
* 分词结果进行词频统计分析，并导出excel
* 词云图可自己设定背景图（英文词云图不需先进行分词）

## 使用方法:grey_question:

1. 在main.py中设置需要分析的txt文件位置

2. 运行main.py程序

3. 会输出excel文件和词云图，下次执行时请先把result中的excel删除或移出，否则会重名错误