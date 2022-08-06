#!/usr/bin/python
# -*- coding: <utf-8> -*-
"""
 @ File    :   pangu.py
 @ Time    :   2022/8/2 19:41
 @ Author  :   @灰尘疾客
 @ Version :   1.0 Final
 @ Contact :   2736550029@qq.com
 @ Desc    :   全网为数偏少的盘古之白实现代码（Python）
"""
import re
import os.path

def split_lines(object_, mode):  # 获取文件并分行
    if mode == "file":
        with open(object_, encoding="utf-8") as f:
            m = f.read()
        f.close()
        lines = m.split('\n')
    elif mode == "text":
        lines = object_.split('\n')
    else:
        lines = ['你个SB','你个SB','你个SB','你个SB','你个SB']
    return lines  # 返回一个所有段落的列表

def add_white(x):  # 增白
    obj = re.compile(r" {0,}[^\u4E00-\u9FFF\uF900-\uFA2D\u3400-\u4DBF\u2F00-\u2FD5\u2E80-\u2EF3\uE400-\uE5E8\uE600-\uE6CF\u31C0-\u31E3\u2FF0-\u2FFB\u3105-\u312F\u31A0-\u31BA\u3007\n，。·！￥…（）—、【】：；“‘”’《》？#/<>*]+ {0,}")  # 用于获取（英文单词）->所有非汉字（排除换行符）所在位置的正则表达式
    words = obj.findall(x)
    for word in words:
        x = x.replace(word, " " + word.strip() + " ").lstrip()  # strip 用于去除匹配内容首尾所有空白，lstrip 用于去除出现在段首的空白。
    result = x
    return result

def get_file_type(filename):  # 用于获取文件类型（后缀名）
    file_type = "." + object_.split(".")[1]
    return file_type

def handle(object_, mode):
    if mode == "file":
        new_paras_list = []
        for line in object_:
            new_line = add_white(line)
            new_paras_list.append(new_line)
        result = new_paras_list
    elif mode == "text":
        new_text = add_white(object_)
        result = new_text
    else:
        result = "你好像没有指定哪一种 mode，please 说明一下，OK？"
    return result

def write_out(filename, new_paras_list):  # 支持将一个自然段集逐行输出到文件
    file_type = get_file_type(filename)
    fixed_filename = filename.replace(file_type, "") + "_fixed" + file_type
    with open(fixed_filename,"w",encoding = "utf-8")as ff:
        for para in new_paras_list:
            ff.write(para + "\n")
    ff.close()
    return os.path.isfile(fixed_filename)

def file_mode(filename):   # 文件模式
    if os.path.isfile(filename):
        lines = split_lines(filename, mode = "file")
        new_paras_list = handle(lines, "file")
        return write_out(filename, new_paras_list)
    else:
        return "Can't find your file..."

def text_mode(text = "Look, you have forgot to give a parameter again.."):  # 文本模式
    result = handle(text, "text")
    return result

if __name__ == '__main__':
    while True:
        object_ = input("Input something:\n")
        mode = input("Is this a file or a paragraph of text?[f/t]: ")
        if mode == "f":  
            if file_mode(object_):
                file_type = get_file_type(object_)
                fixed_filename = object_.replace(file_type, "") + "_fixed" + file_type
                print("Finish!!!", fixed_filename)
            else:
                print(file_mode(object_))
        elif mode == "t":
            if object_ != "":
                print(text_mode(object_))
            elif object_ == "":
                print(text_mode())
        else:
            print("The input content is invalid..")
        print("===========SESSION END===========")
