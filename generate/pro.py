import os
import json
import pandas as pd
from nltk.tokenize import word_tokenize


def delete_short_text_json(folder_path, min_length):
    # 遍历文件夹下的所有json文件
    num=0
    lili=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            num+=1
            print(num)
    # print(num)
            file_path = os.path.join(folder_path, filename)
            # # 读取json文件
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # # 检查"text"键的值长度

            tmp=data['text'].split()
            # num+=len(data['text'])
            tokens = word_tokenize(data['text'])
            
            if 'text' in data and len(tokens) < min_length:
                # 如果"text"的值太短，删除这个json文件
                # os.remove(file_path)
                print(f"Deleted: {filename}")
            else:
                lili.append(len(tokens))

# 示例用法
    return lili

series=delete_short_text_json('./after_pro', 2000)  # 假设最小长度为10
print(series)
series = pd.Series(series)
mean = series.mean()  # 平均值
median = series.median()  # 中位数
std = series.std()  # 标准差
min_val = series.min()  # 最小值
max_val = series.max()  # 最大值
print(mean,median,std,min_val,max_val)