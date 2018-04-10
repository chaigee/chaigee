rom os import path
import jieba.analyse as analyse

d = path.dirname(__file__)

text_path = '我来到北京清华大学' #设置要分析的文本路径
text = open(path.join(d, text_path)).read()

for key in analyse.extract_tags(text,50, withWeight=False):