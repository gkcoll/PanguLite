# PanGuLite

其他语言选择:

[English](README.md) | 简体中文 | [繁體中文](README_zh-TW.md)

## 介绍

这是一个文字处理程序，它用于在全角、半角符号混输（你可以理解为中文、英文混输）的字符串里在中英文间添加空白，这种空白就叫做『**盘古之白**』（The White of Pangu）。

本来想为一位朋友开发这个工具帮他形成加**盘古之白**的习惯，但是上百度搜索没有相关案例和代码。

于是我打算着手用我仅学的一点毛皮技术开发这么一个玩意：可以为文本、文件批量添加**盘古之白**。

后来在[**一个木函网页端**](https://ol.woobx.cn)里找到一个[**盘古之白**](https://ol.woobx.cn/tool/pangu)，里面标注了技术提供——一个别人（看样子是繁体中文地区，GitHub 用户名为“ Vinta Chen ”）写的为达成同种目的的程序，只不过是 [*JavaScript* 版](https://github.com/vinta/pangu.js)，随后又顺藤摸瓜地找到了同一个人写的多编程语言版本，其中不乏 [*Python* 版](https://github.com/vinta/pangu.py)。

眼看我写的代码量和工整度不如（至少我这么认为）别人的工程，我默默的把项目名改为了 `PanguLite` 。

---

## 使用

本程序没有上传到 Pypi 库，只有这么一个开源地址。

为使用本程序，你需要将整个项目下载到本地（压缩包）。

解压后你将看到和本仓库目录树一样的目录，并看到一个名为 `pangu_lite.py` 的 Python 文件。

为了正常使用此文件，请务必提前安装并配置好 Python 开发/运行环境。

### 作为程序

作为程序而使用，你可以直接双击运行此文件（`pangu_lite.py`），你将看到一个要求你输入东西的弹窗。

如果你想输入一个文件名，你应该按要求输入参数并且能够看到一个带有 **Finish** 的处理成功标志：

```shell
Input something:
test.txt
Is this a file or a paragraph of text?[f/t]: f
Finish!!! test_fixed.txt
===========SESSION END===========
Input something:
```

如果你输入的是一串想要处理的文字（警告：**不支持**输入有换行符或多段的文字，**仅支持**输入一个自然段），一般过程是这样的：

```shell
Input something:
Eric Matthes，高中science和math teacher，现居住在Alaska，在当地讲授Python入门教程。他从5岁就一直在编写程序。
Is this a file or a paragraph of text?[f/t]: t
Eric Matthes ，高中 science 和 math teacher ，现居住在 Alaska ，在当地讲授 Python 入门教程。他从 5 岁就一直在编写程序。
===========SESSION END===========
Input something:
```

---

### 作为模块

你需要提取出这个文件（`pangu_lite.py`），将它移植到你的项目里（很简单的 C/V 大法），并通过以下代码将其导入：

```python
import pangu_lite
```

#### 内置的函数/接口/方法

作为一个模块，这个文件里提供了很多由开发者封装好的函数（function），这里主要讲解几个比较有实际作用的函数。

1. split_lines

这是一个用于分割文本文件里的内容或多行文本的函数，主要行为是逐行分割（以换行符为分割的评判标准），如果输入一篇课文、论文、作文则可以分出每一个自然段。

返回内容：一个由各行组成的列表。

用处：文章逐段、逐行读取

使用：

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

或

```python
import pangu_lite
filename = "test.txt"

lines = pangu_lite.split(filename, mode = "file")
print(lines)
```

再或者，你忘记指定**文本**或**文件**任意一种模式，它会返回一个很友好的提示，让你记忆深刻，不敢再忘记指定模式：

```python
import pangu_lite
filename = "test.txt"

lines = pangu_lite.split(filename)
print(lines)
```

你会得到以下输出：

```textile
['你个SB','你个SB','你个SB','你个SB','你个SB']
```

---

2. add_white

这是一个为半角、全角符之间添加空白 x 1 的函数，是整个程序的核心，所有输入的内容都会经过它，识别出里面所有英文、数字，并为其首尾添加空白。

识别非中文字符的**正则表达式**是：

> 注意前后的 `{0,}` 前面都有一个空格，用以匹配那些前后有空格甚至不止一个的半角字符串，后面再统一加上一个空白。

```regex
 {0,}[^\u4E00-\u9FFF\uF900-\uFA2D\u3400-\u4DBF\u2F00-\u2FD5\u2E80-\u2EF3\uE400-\uE5E8\uE600-\uE6CF\u31C0-\u31E3\u2FF0-\u2FFB\u3105-\u312F\u31A0-\u31BA\u3007\n，。·！￥…（）—、【】：；“‘”’《》？#/<>*]+ {0,}
```

本来是这样的：

```regex
\w+
```

但是这样太笼统了，无法对文件名等信息进行合理的容灾处理。

虽然后来想起好像下面是可行的：

```regex
 {0,}[\w\."':;\$\(\),`] {0,}
```

原理：找出所有符合条件的字符串后统一替换成首尾各加一个空白的字符串。】

用法示例：

```python
-snip-

message = "不能信任那些Terminal或Editor用白底的人"
reuslt = pangu_lite.add_white(message)
print(result)
# 不能信任那些 Terminal 或 Editor 用白底的人
```

---

3. get_file_type

这个不用多说，就是用来获取文件类型的，最简单的方法就是获取文件后缀名。

使用：

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

4. write_out

这是个输出到文件的函数，但是不同于普通的打开文件并输出内容，而是传入一个列表，这个列表可以是前面的 `split_lines()` 处理得来的逐行分隔开的字符串列表，然后让程序读取后逐行输出到新文件。

使用：

```python
from pangu_lite import write_out

paras_list = ['不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人']
print(write_out("test_fixed.txt", paras_list))
# 成功：True;失败：False
```

---

5. file_mode & text_mode

如果你不需要前面所讲的实用方法，只是需要调用**文件模式**或**文本模式**对您要处理的对象进行处理，那你可以参考下面方法：

* file_mode

```python
-snip-

filename = "test.txt"
print(file_mode(filename))
# 成功：True;失败：False
```

* text_mode

```python
-snip-

print(text_mode("不能信任那些Terminal或Editor用白底的人"))
# 不能信任那些 Terminal 或 Editor 用白底的人
```

若你忘记在文本模式中传入文本参数，像下面这样：

```python
-snip-

print(text_mode())
```

你将会看到以下结果在目的地输出：

```textile
Look, you have forgot to give a parameter again..
# 看，你又忘了给参数了。
```

---

## 常见问题解答

* 此程序能对什么内容进行了特别适配？

此程序通过一起匹配英文句号、`#` 号等方式，对文本里出现的文件名、域名、网址以及 MarkDown 文件内容进行排除处理，即尽可能不会破坏文件格式或多了多余的空白。

* 此项目可以二次开发吗？

本人对所有拿我的开源项目进行移植、二次开发的行为持支持态度，但是希望各位告知修改的内容，更要提出需要完善之处。

* 更多问题完善中……

* 若输出内容与你的预期有不同，请提交一条 issue 并附上处理对象、运行结果（若有报错也一并上传）。
