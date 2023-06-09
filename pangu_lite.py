'''
@File    :   pangu_lite.py
@Time    :   2023/03/11 18:16:30
@Author  :   @灰尘疾客
@Version :   1.0 Fixed
@Site    :   https://www.gkcoll.xyz
@Desc    :   为中英混排文本（主体为中文）的中英文之间添加空白。
'''


import re
import os.path


def split_lines(file_content: str) -> list[str]:
    """将文本内容按行分割成列表"""
    return file_content.split('\n')


def add_whitespace(text: str) -> str:
    """在中英文、数字和符号之间添加适当的空格"""

    # 匹配所有非汉字字符（包括英文、数字和符号），排除换行符
    regex_1 = re.compile(r" {0,}[^\u4E00-\u9FFF\uF900-\uFA2D\u3400-\u4DBF\u2F00-\u2FD5\u2E80-\u2EF3\uE400-\uE5E8\uE600-\uE6CF\u31C0-\u31E3\u2FF0-\u2FFB\u3105-\u312F\u31A0-\u31BA\u3007\n，。·！￥…（）—、【】『』「」：；“‘”’《》？#]+ {0,}")
    matches_1 = list(set(regex_1.findall(text)))
    for match in matches_1:
        # 去除匹配内容首尾的空格，并在首尾添加一个空格
        text = text.replace(match, f" {match.strip()} ")
    
    # 匹配所有全角标点符号及其左右的空白，统一替换为该标点符号。
    regex_2 = re.compile(r" {0,}[，。·~！￥……（）——【】：；”“’‘《》？] {0,}")
    matches_2 = list(set(regex_2.findall(text)))
    for match in matches_2:
        text = text.replace(match, f"{match.strip()}")

    return text.rstrip().lstrip()


def get_file_extension(filename: str) -> str:
    """获取文件扩展名"""
    return os.path.splitext(filename)[1]


def process_text(text: str = "汉学家称这个空白字元为『盘古之白』，because它劈开了全形字和半角字之间的混沌。另有investigate显示，typing的时候不喜欢在Chinese和English之间加whitespace(s)的人，感情路都走得很辛苦，有70%会在34岁的时候wedding with自己不爱的人，而其余30%的人最后只能把遗产留给自己的cat。毕竟爱情跟书写都需要适时地留白。") -> str:
    """处理文本，增加合适的空格"""
    return add_whitespace(text)


def process_file(filename: str) -> bool:
    """处理文件，增加合适的空格，并将结果写入新文件"""
    if not os.path.isfile(filename):
        return False

    with open(filename, encoding="utf-8") as f:
        file_content = f.read()

    lines = split_lines(file_content)
    new_lines = [add_whitespace(line) for line in lines]

    # 写入新文件
    file_extension = get_file_extension(filename)
    output_filename = filename.replace(file_extension, f"_fixed{file_extension}")
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write('\n'.join(new_lines))

    return True


if __name__ == '__main__':
    while True:
        object_ = input("Input something:\n")
        mode = input("Is this a file or a paragraph of text?[f/t]: ")

        if mode == "f":
            if process_file(object_):
                print("Finish!!!")
            else:
                print("Can't find your file...")
        elif mode == "t":
            if object_ != "":
                print(process_text(object_))
            else:
                print(process_text())
        else:
            print("Invalid input..")

        print("======================")
