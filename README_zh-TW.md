# PanGuLite

其他語言選擇:

[English](README.md) | [簡體中文](README_zh-CN.md)| 繁體中文

> 此繁體中文譯文由 [@蓝宇](https://www.lanyu.site) 進行機器翻譯並核對

## 介紹

這是一個文字處理程序，它用於在全角、半角符號混輸（你可以理解為中文、英文混輸）的字符串裡在中英文間添加空白。這種空白就叫做『**盤古之白**』（The White of Pangu）。

本來想為一位朋友開發這個工具幫他形成加**盤古之白**的習慣，但是上百度搜索沒有相關案例和代碼。

於是我打算著手用我僅學的一點毛皮技術開發這麼一個玩意：可以為文本、文件批量添加**盤古之白**。

後來在[**一個木函網頁端**](https://ol.woobx.cn)裡找到一個[**盤古之白**](https://ol.woobx.cn/tool/pangu)，裡面標註了技術提供——一個別人（看樣子是繁體中文地區，GitHub 用戶名為“ Vinta Chen ”）寫的為達成同種目的的程序，只不過是 [*JavaScript* 版](https://github.com/vinta/pangu.js)，隨後又順藤摸瓜地找到了同一個人寫的多編程語言版本，其中不乏 [*Python* 版](https://github.com/vinta/pangu.py)。
眼看我写的代码量和工整度不如（至少我这么认为）别人的工程，我默默的把项目名改为了 `PanguLite` 。

---

## 使用

本程序沒有上傳到 Pypi 庫，只有這麼一個開源地址。

為使用本程序，你需要將整個項目下載到本地（壓縮包）。

解壓後你將看到和本倉庫目錄樹一樣的目錄，並看到一個名為 `pangu_lite.py` 的 Python 文件。

為了正常使用此文件，請務必提前安裝並配置好 Python 開發/運行環境。

### 作為程序

作為程序而使用，你可以直接雙擊運行此文件（`pangu_lite.py`），你將看到一個要求你輸入東西的彈窗。

如果你想輸入一個文件名，你應該按要求輸入參數並且能夠看到一個帶有 **Finish** 的處理成功標誌：

```shell
Input something:
test.txt
Is this a file or a paragraph of text?[f/t]: f
Finish!!! test_fixed.txt
===========SESSION END===========
Input something:
```

如果你輸入的是一串想要處理的文字（警告：**不支持**輸入有換行符或多段的文字，**僅支持**輸入一個自然段），一般過程是這樣的：

```shell
Input something:
Eric Matthes，高中science和math teacher，現居住在Alaska，在當地講授Python入門教程。他從5歲就一直在編寫程序。
Is this a file or a paragraph of text?[f/t]: t
Eric Matthes ，高中 science 和 math teacher ，現居住在 Alaska ，在當地講授 Python 入門教程。他從 5 歲就一直在編寫程序。
===========SESSION END===========
Input something:
```

---

### 作為模塊

你需要提取出這個文件（`pangu_lite.py`），將它移植到你的項目裡（很簡單的 C/V 大法），並通過以下代碼將其導入：

```python
import pangu_lite
```

#### 内置的函数/接口/方法

作為一個模塊，這個文件裡提供了很多由開發者封裝好的函數（function），這裡主要講解幾個比較有實際作用的函數。

1. split_lines

這是一個用於分割文本文件裡的內容或多行文本的函數，主要行為是逐行分割（以換行符為分割的評判標準），如果輸入一篇課文、論文、作文則可以分出每一個自然段。

返回內容：一個由各行組成的列表。

用處：文章逐段、逐行讀取

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

再或者，你忘記指定**文本**或**文件**任意一種模式，它會返回一個很友好的提示，讓你記憶深刻，不敢再忘記指定模式：

```python
import pangu_lite
filename = "test.txt"

lines = pangu_lite.split(filename)
print(lines)
```

你會得到以下輸出：

```textile
['你個SB','你個SB','你個SB','你個SB','你個SB']
```

---

2. add_white

這是一個為半角、全角符之間添加空白 x 1 的函數，是整個程序的核心，所有輸入的內容都會經過它，識別出裡面所有英文、數字，並為其首尾添加空白。

識別非中文字符的**正則表達式**是：

> 注意前後的 `{0,}` 前面都有一個空格，用以匹配那些前後有空格甚至不止一個的半角字符串，後面再統一加上一個空白。

```regex
 {0,}[^\u4E00-\u9FFF\uF900-\uFA2D\u3400-\u4DBF\u2F00-\u2FD5\u2E80-\u2EF3\uE400-\uE5E8\uE600-\uE6CF\u31C0-\u31E3\u2FF0-\u2FFB\u3105-\u312F\u31A0-\u31BA\u3007\n，。 ·！ ￥…（）—、【】：；“‘”’《》？ #/<>*]+ {0,}
```

本來是這樣的：

```regex
\w+
```

但是這樣太籠統了，無法對文件名等信息進行合理的容災處理。

雖然後來想起好像下面是可行的：

```regex
 {0,}[\w\."':;\$\(\),`] {0,}
```

原理：找出所有符合條件的字符串後統一替換成首尾各加一個空白的字符串。 】

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

這個不用多說，就是用來獲取文件類型的，最簡單的方法就是獲取文件後綴名。

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

這是個輸出到文件的函數，但是不同於普通的打開文件並輸出內容，而是傳入一個列表，這個列表可以是前面的 `split_lines()` 處理得來的逐行分隔開的字符串列表，然後讓程序讀取後逐行輸出到新文件。

使用：

```python
from pangu_lite import write_out

paras_list = ['不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人','不能信任那些 Terminal 或 Editor 用白底的人']
print(write_out("test_fixed.txt", paras_list))
# 成功：True;失敗：False
```

---

5. file_mode & text_mode

如果你不需要前面所講的實用方法，只是需要調用**文件模式**或**文本模式**對您要處理的對象進行處理，那你可以參考下面方法：

* file_mode

```python
-snip-

filename = "test.txt"
print(file_mode(filename))
# 成功：True;失敗：False
```

* text_mode

```python
-snip-

print(text_mode("不能信任那些Terminal或Editor用白底的人"))
# 不能信任那些 Terminal 或 Editor 用白底的人
```

若你忘記在文本模式中傳入文本參數，像下面這樣：

```python
-snip-

print(text_mode())
```

你將會看到以下結果在目的地輸出：

```textile
Look, you have forgot to give a parameter again..
# 看，你又忘了給參數了。
```

---

## 常見問題解答

* 此程序能對什麼內容進行了特別適配？

此程序通過一起匹配英文句號、`#` 號等方式，對文本里出現的文件名、域名、網址以及 MarkDown 文件內容的排除處理，即盡可能不會破壞文件格式或多了多餘的空白。

* 此項目可以二次開發嗎？

本人對所有拿我的開源項目進行移植、二次開發的行為持支持態度，但是希望各位告知修改的內容，更要提出需要完善之處。

* 更多問題完善中……

* 若輸出內容與你的預期有不同，請提交一條 issue 並附上處理對象、運行結果（若有報錯也一併上傳）。