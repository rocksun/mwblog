# 从基础到最佳实践：Python 正则表达式精通

![特色图片：从基础到最佳实践：Python 正则表达式精通](https://cdn.thenewstack.io/media/2025/03/8972e1e0-getty-images-rkoajjc93r0-unsplash-1-1024x683.jpg)

[Regex](https://thenewstack.io/magic-regexp-a-javascript-package-for-regular-expressions/)（[正则表达式](https://thenewstack.io/how-to-speed-up-regular-expressions-under-production-pressure/)的缩写）是匹配和操作文本的强大工具。它可以自动执行各种文本处理任务，例如验证电子邮件地址、从日志文件中提取数据以及清理混乱的数据集。虽然正则表达式语法在各种编程语言中非常相似，但本教程将重点介绍它在 [Python](https://thenewstack.io/python/) 中的具体工作方式。

## 正则表达式的作用是什么？

*   数据提取：从文本中提取数据点，如电子邮件地址、电话号码和错误代码
*   验证用户输入：确保用户输入（例如，电子邮件地址、电话号码和密码）的格式正确
*   搜索和替换数据：无需人工干预即可修改文本
*   自动化重复性任务：自动化处理日志、文件和大型数据集

## 正则表达式最佳实践

*   逐步构建：逐步开发正则表达式模式，以避免复杂代码块中的混淆。
*   测试效率：通过测试正则表达式效率来避免执行缓慢。
*   使用原始字符串：通过使用原始字符串（例如，`r"\d+"`）来防止反斜杠被解释为转义字符。
*   使用工具调试：使用 [Regex101](https://thenewstack.io/dont-fear-regex-getting-started-regular-expressions/) 等在线工具来帮助调试和改进模式。

### `re` 模块

在 Python 中，正则表达式功能由 `re` 模块提供。此模块支持模式匹配、搜索和字符串操作。`re.search()`、`re.match()` 和 `re.sub()` 等内置函数允许进行复杂的模式匹配。如果没有 `re` 模块，Python 支持使用 `.find()`、`.startswith()`、`.endswith()` 和 `.replace()` 等方法进行基本模式匹配。虽然这些内置方法允许基本匹配，但 `re` 模块对于更高级的正则表达式操作是必需的。

您可以使用与所有其他 Python 导入相同的语法导入 `re` 模块。

常用的正则表达式内置函数：

`re` 模块提供了许多有用的函数，包括：

*   `re.match()`：从字符串的开头匹配模式
*   `re.search()`：查找模式的第一次出现
*   `re.findall()`：返回模式的所有出现
*   `re.finditer()`：返回匹配对象的一个迭代器
*   `re.sub()`：用指定的字符串替换模式匹配项
*   `re.subn()`：替换匹配项并返回替换次数
*   `re.split()`：按模式拆分字符串
*   `re.compile()`：将模式编译为正则表达式对象
*   `re.fullmatch()`：检查整个字符串是否匹配模式
*   `re.escape()`：转义字符串中的特殊字符

## 正则表达式类别及其应用

### 字符和字面量

搜索字符和字面量可以找到字符串中指定字符或序列的精确匹配项。这对于查找固定模式非常有用，例如日志文件中的错误代码或发票上的产品 ID。

基本语法：

*   `.`：匹配除换行符以外的任何字符
*   `a, b, 1`：匹配字面字符 a、b 或 1

代码示例：

输出：cat

### 字符类

字符类允许搜索定义集合中的任何字符（例如，数字、字母）。当您需要匹配具有不同字符的模式时，此类别非常有用，例如提取客户电话号码或日期。

基本语法：

*   `[abc]`：匹配字符 a、b 或 c 中的任何一个
*   `[^abc]`：匹配除 a、b 或 c 以外的任何字符
*   `[0-9]`：匹配任何数字
*   `[a-z]`：匹配任何小写字母
*   `\d`：匹配任何数字（等效于 [0-9]）
*   `\D`：匹配任何非数字
*   `\w`：匹配任何单词字符（字母、数字和下划线）
*   `\W`：匹配任何非单词字符
*   `\s`：匹配任何空白字符（空格、制表符和换行符）
*   `\S`：匹配任何非空白字符

代码示例：

输出：[‘12345’]

### 量词

[量词](https://thenewstack.io/taming-text-search-with-the-power-of-regular-expressions/)控制模式应重复多少次，这在数据长度变化时非常有用。当匹配重复的单词或短语，或者搜索电子邮件地址等长度可能变化的数据时，它们会派上用场。

基本语法：

*   `*`：匹配 0 个或多个前面的元素
*   `+`：匹配 1 个或多个前面的元素
*   `?`：匹配 0 个或 1 个前面的元素（可选）
*   `{n}`：完全匹配前面元素的 n 个实例
*   `{n,}`：匹配 n 个或多个实例
*   `{n,m}`：匹配 n 和 m 之间的实例

代码示例：

输出：[‘Hello’, ‘world’]

### 锚点
锚点用于匹配字符串中的位置，而不是字符。它们对于验证固定位置的模式很有用，例如检查电子邮件地址是否以特定域名结尾，或者句子是否以问号结尾。

基本语法：

*   `^`: 匹配字符串的开头（如果在多行模式下，则匹配行的开头）
*   `$`: 匹配字符串的结尾（如果在多行模式下，则匹配行的结尾）
*   `\b`: 匹配单词边界
*   `\B`: 匹配非单词边界

代码示例：

```python
import re

text = "Hello world"
pattern_start = r"^Hello"
pattern_end = r"world$"

match_start = re.search(pattern_start, text)
match_end = re.search(pattern_end, text)

print(match_start)
print(match_end)
```

Output:

```
<re.Match object; span=(0, 5), match='Hello'>
<re.Match object; span=(6, 11), match='world'>
```

### 组和捕获

组和捕获允许您通过捕获匹配文本的部分以供以后使用，从而提取和操作字符串的各个部分。当您需要从日志中提取特定数据（如名称或错误代码）时，这尤其有用。

基本语法：

*   `(abc)`: 将组 abc 捕获为匹配项
*   `\1`: 引用第一个捕获的组
*   `(?:abc)`: 匹配 abc 但不捕获它（非捕获组）

代码示例：

```python
import re

text = "My name is John"
pattern = r"(My) name"

match = re.search(pattern, text)

print(match.group(1))
```

Output:

```
My
```

### 替换

替换对于匹配多个模式之一很有用。当您需要匹配不同的可能性时，通常会使用它，例如在日志文件中搜索多个错误代码。

基本语法：

*   `a|b`: 匹配 a 或 b

代码示例：

```python
import re

text = "I have a cat and a dog"
pattern = r"cat|dog"

matches = re.findall(pattern, text)

print(matches)
```

Output:

```
['cat', 'dog']
```

### 转义特殊字符

在正则表达式中，某些字符（如`.`、`*`或`?`）具有特殊含义。转义这些字符允许您匹配文字字符本身，当它们出现在您的输入中但不应被解释为元字符时，这很有用。

基本语法：

*   `\.`: 匹配文字点 (.)
*   `\*`: 匹配文字星号 (*)

代码示例：

```python
import re

text = "This is a test. This is another test."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)
```

Output:

```
['.', '.']
```

## 修饰符或标志

修饰符（或标志）修改正则表达式模式的应用方式，例如在进行不区分大小写的搜索或启用多行匹配时。这些对于根据上下文调整搜索行为很有用。

基本语法：

*   `i`: 不区分大小写的匹配 (`re.IGNORECASE`)
*   `g`: 全局匹配（查找所有匹配项，在 Python 中由 `re.findall()` 隐式处理）
*   `m`: 多行模式（匹配每行的开头 `^` 和结尾 `$`）

代码示例：

```python
import re

text = "hello"
pattern = r"HELLO"

match_case_sensitive = re.search(pattern, text)
match_case_insensitive = re.search(pattern, text, re.IGNORECASE)

print(match_case_sensitive)
print(match_case_insensitive.group(0))
```

Output:

```
None
Hello
```

## 结论

正则表达式是文本处理的重要工具，可以实现数据提取、验证和替换等任务。无论您是清理数据、自动化任务还是从文本中提取有价值的信息，理解正则表达式语法和最佳实践都是关键。通过利用 Python 的 `re` 模块，您可以轻松匹配复杂模式并自动化重复性任务，从而提高工作效率和准确性。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)