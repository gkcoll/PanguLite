# PanguLite

Other Language Choose:

English | [简体中文](README_zh-CN.md) | [繁體中文](README_zh-TW.md)

> This English doc translated by machine ( Youdao & Baidu )  & the developer. 
> 
> Ckecker: the Developer ([@灰尘疾客](https://www.gkcoll.xyz)).

## Introduction

This is a word processing program, which is used to add whitespace between Chinese and English in the string of mixed input of full width and half width symbols (you can understand it as mixed input of Chinese and English). This whitespace called **The White of Pangu** (盘古之白).

Originally, I wanted to develop this tool for a friend to help him form the habit of adding **The White of Pangu**, but there was no relevant cases or codes on Baidu.

So I plan to develop such a program with the little fur technology I only learned: it can add **The White of Pangu**.

Later, I found a function of add [***The White of Pangu***](https://ol.woobx.cn/tool/pangu) on the [***Web WoodBox***](https://ol.woobx.cn). It marked that the tech provision: a program written by someone else (it looks like the traditional Chinese area) to achieve the same purpose, But It just a [*JavaScript* version](https://github.com/vinta/pangu.js). Then I find other languages version written by the same man, including [*Python* version](https://github.com/vinta/pangu.py).

When I seeing that the amount of code and neatness of the program I wrote are not as good as other‘s ( at least I think so ), I silently changed the project name to `Pangu Lite`.

## Usage

This project didn't upload to Pypi lib, and it onlt have this open-source url.

In order to use this program, you need to download all of this project into your locol PC.

In order to use this program, you need to download the entire project (a `.zip` package) to your local PC .

You will see the same directory as the repository tree and a Python file named `pangu_lite.py` when you finish unzip.

In order to use this file properly, make sure that the Python development/run environment is installed and configured in advance.

### As Program

If you want to use it as a program, you can run the file `pangu_lite.py` by double-click. Then you will see a window which need you to input something. 

If you want enter a file name, you should enter the parameters as required and see a successful processing flag with **Finish**.

```shell
Input something:
Eric Matthes，高中science和math teacher，现居住在Alaska，在当地讲授Python入门教程。他从5岁就一直在编写程序。
Is this a file or a paragraph of text?[f/t]: t
Eric Matthes ，高中 science 和 math teacher ，现居住在 Alaska ，在当地讲授 Python 入门教程。他从 5 岁就一直在编写程序。
===========SESSION END===========
Input something:
```

---

### As Module

You need to extract the pangu_lite.py file separately, port it to your project, and import it by this code:

```python
import pangu_lite
```

#### Built-in Functions/Interfaces/Methods

As a module, this file provides many of functions wrapped by the developer.

1. *split_lines*

This is a function which used for **Multiline text** in a text file. The main action of it is split text line by line (**Newline Character** is used as the segmentation criterion). If you enter a article, essay, composition, each paragraph of them will be split.

Return: a list include all lines.

Used to: Read paragraph by paragraph/line by line in a article.

Usege: 

```python
from pangu_lite import split_lines
message = """
多行text
多行text

多行text
"""
lines = split_lines(message, mode = "text")
print(lines)
# ['多行text','多行text','','多行text']
```

Or:

```python
import pangu_lite
filename = "test.txt"

lines = pangu_lite.split(filename, mode = "file")
print(lines)
```

Again or, you forgot to chose **text** or **file** mode, it will return a friendly prompt, make you remember deeply, dare not forget to choose mode:

```python
import pangu_lite
filename = "test.txt"

lines = pangu_lite.split(filename)
print(lines)
```

You will get this output:

```textile
['你个SB','你个SB','你个SB','你个SB','你个SB']
```

---

2. *add_white*

This is a function that can adds whitespace between the content of half width character (English, English periods, numbers, etc.) and full width character (Chinese characters, etc.), and it's the ***HEART*** of the whole program.

All input content will go through it, identify all the English and numbers in it, and add blanks at the beginning and end.

The **Regex** for identifying non-Chinese characters is:

> Note that there is a space in front of the `{0,}` before and after it, to match those half-width strings with more than one whitespace before and after (If have), and then add a space uniformly.

```regex
 {0,}[^\u4E00-\u9FFF\uF900-\uFA2D\u3400-\u4DBF\u2F00-\u2FD5\u2E80-\u2EF3\uE400-\uE5E8\uE600-\uE6CF\u31C0-\u31E3\u2FF0-\u2FFB\u3105-\u312F\u31A0-\u31BA\u3007\n，。·！￥…（）—、【】：；“‘”’《》？#/<>*]+ {0,}
```

It would have been like this:

```regex
\w+
```

However, this is too general, and cannot reasonably adapt information such as file names.

Though after thinking about it, the following seems to work:

```regex
 {0,}[\w\."':;\$\(\),`] {0,}
```

原理：找出所有符合条件的字符串后统一替换成首尾各加一个空白的字符串。

Principle: Find all qualified strings and add a whitespace at their beginning and end.

replace them with a blank string at the beginning and the ending.

Usage example: 

```python
-snip-

message = "不能信任那些Terminal或Editor用白底的人"
reuslt = pangu_lite.add_white(message)
print(result)
# 不能信任那些 Terminal 或 Editor 用白底的人
```

---

3. *get_file_type*

Needless to say, this is used to get the file type. The principle is to get the file suffix name.

Usage: 

```python
-snip-

filename_1 = "test.txt"
filename_2 = "test.md"

type_1 = pangu_lite.get_file_type(filename_1)
type_2 = pangu_lite.get_file_type(filename_2)

print(type_1, type_2)
# .txt .md
```

---

4. *write_out*

This a function which can achieve output something into a file, but it is different from opening a file and outputting the content. Instead, a list is passed in. This list can be a list of strings separated line by line processed by the previous `split_lines()`, and then let the program read it one by one. Then the lines will be output to a new file.

Usage: 

```python
from pangu_lite import write_out

paras_list = ['不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人']
print(write_out("test_fixed.txt", paras_list))
# True; False
```

---

5. *file_mode & text_mode*

If you don&#39;t need the utility methods mentioned above, but just need to call **file mode** or **text mode** to process the object you want to process, then you can refer to the following methods:

* **file_mode**

```python
-snip-

filename = "test.txt"
print(file_mode(filename))
# True; False
```

* **text_mode**

```python
-snip-

print(text_mode("不能信任那些Terminal或Editor用白底的人"))
# 不能信任那些 Terminal 或 Editor 用白底的人
```

If you forgot to give a parameter in **text_mode**, like this: 

```python
-snip-

print(text_mode())
```

You will see the following results output at the destination:

```textile
Look, you have forgot to give a parameter again..
```

---

## FAQ

* What does this program specifically adapt to?

This program excludes file names, domain names, URLs, and Markdown document content that appear in the text by matching English periods, `#` signs, etc. together. 

That is, as far as possible, without destroying the file format or adding extra blanks.

* Can this project be redeveloped?

I support my open source projects being ported and developed by users, but I hope you can tell me what you modified and what areas of application, and where improvements are needed.

* More questions are completing...

* If the output content is different from your expectations, please submit an issue and attach the processing object and the running result (if any error is reported, upload it as well).
