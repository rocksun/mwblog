
<!--
title: 在 Python 中使用 JSON 数据
cover: https://cdn.thenewstack.io/media/2024/10/fd160d1f-claudio-schwarz-fyeoxvyviyy-unsplash-1.jpg
-->

由于 JSON 凭借其极简高效的特性成为信息共享的首选格式，本教程将展示如何在 Python 编程中使用 JSON 数据。

> 译自 [Working With JSON Data in Python](https://thenewstack.io/working-with-json-data-in-python/)，作者 Jessica Wachtel。

[JavaScript 对象表示法 (JSON)](https://thenewstack.io/an-introduction-to-json/) 简化了应用程序之间信息共享。它是 Web 客户端和服务器之间交换数据以及 [API](https://thenewstack.io/api-management/) 与各种服务或数据源之间通信的首选方式。JSON 的格式既可读懂，又易于理解，使其易于解析、生成和理解。它在减少数据传输方面的效率使 [JSON](https://thenewstack.io/how-to-convert-google-spreadsheet-to-json-formatted-text/) 成为信息共享的首选格式。

**JSON 是**：

* **轻量级**：JSON 简洁高效，适合在网络上传输数据。
* **基于文本**：JSON 的纯文本格式由可读字符和符号组成。虽然 JSON 基于 [JavaScript](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/) 的一个子集，但它是与语言无关的，并且与大多数 [现代编程语言](https://thenewstack.io/the-fastest-programming-language-daves-garage-seeks-the-answer/) 兼容。
* **结构化数据**：JSON 将数据表示为 [键值](https://thenewstack.io/akamai-brings-key-value-data-to-the-edge-adds-api-acceleration/) 对，这些对可以组织成嵌套结构，如对象（字典）和列表。

在构建和维护应用程序时，处理 JSON 数据是一种常见的现象。

## JSON 在现实世界中的应用

JSON 快速高效地执行以下任务。

* **API 交互**：[Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) 应用程序通常以 JSON 格式发送和接收响应。
    * 示例：天气数据和股票数据共享
* **数据存储**：JSON 用于在系统不同部分之间以及不同系统之间存储和共享数据。
    * 示例：配置文件和日志
* **序列化和反序列化**：JSON 将数据结构转换为字符串格式（序列化），然后将其重建为原始形式（反序列化）。此过程简化了数据共享和交换。
    * 示例：存储用户偏好和复杂数据对象的传输

## 入门：在 Python 应用程序中使用 JSON

导入 `json` 模块是第一步。

```py
import json
```

**解析和访问 JSON 数据**

**解析数据**

解析 JSON 数据将 JSON 编码的数据（通常以字符串形式）转换为可以在编程环境中访问的格式。在 Python 应用程序中，JSON 字符串被转换为本机 Python 数据结构，如字典和列表。

`json.loads()` 是 `json` 模块的数据解析函数。

```python
json_data = '''
{
    "apple": "red",
    "banana": "yellow",
    "cucumber": "green",
    "types": ["fruit", "vegetable"]
}
'''

# parse JSON data into a Python dictionary
data = json.loads(json_data)

print(data)
```

输出：{‘apple’: ‘red’, ‘banana’: ‘yellow’, ‘cucumber’: ‘green’, ‘types’: [‘fruit’, ‘vegetable’]}

`json.loads()` 函数对于嵌套数据和非嵌套数据都相同。

**访问非嵌套数据**

解析后，您可以访问 JSON 数据。

**硬编码**：

```python
print(data['apple'])    
print(data['banana'])         
print(data['types'])
```

输出：

```
red
yellow
[‘fruit’, ‘vegetable’]
```

**动态**：

```python
import json

json_string = '{"apple": "red", "banana": "yellow", "cucumber": "green", "types": ["fruit", "vegetable"]}'
data = json.loads(json_string)

key = 'cucumber'
print(data[key])  # 输出：green
```

#### 访问嵌套数据

通常，JSON 数据是嵌套的。这意味着数据包含其他字典或列表中的字典或列表。

嵌套数据非常常见，因为它反映了现实世界中数据的组织方式。嵌套数据的示例是电子商务网站上的用户配置文件，其中包含个人详细信息、地址和购买列表，所有这些都具有自己的属性。

访问嵌套 JSON 数据需要与非嵌套数据不同的代码设置。

**硬编码**：

```python
import json

json_string = '{"student": {"name": "Sarah Ellington", "grade": "B+"}}'
data = json.loads(json_string)

print(data['student']['name'])  # 输出：Sarah Ellington
print(data['student']['grade'])  # 输出：B+
```

**动态**：

动态处理嵌套数据需要递归或迭代函数。虽然两者都有效，但递归解决方案更优雅，也更容易阅读。

```python
import json

json_string = '{"student": {"name": "Sarah Ellington", "grade": "B+"}}'
data = json.loads(json_string)

def print_nested_data(data):
    for key, value in data.items():
        if isinstance(value, dict):
            print_nested_data(value)
        else:
            print(f"{key}: {value}")

print_nested_data(data)
```

输出：

```
name: Sarah Ellington
grade: B+
```

### 将 JSON 数据读写到文件

#### 写入

`json.dumps()` 将 JSON 数据保存到文件中。`json.dumps()` 将 Python 对象转换为 JSON 格式的字符串，称为序列化数据。然后将序列化数据写入文件或通过网络传输。写入嵌套数据和非嵌套数据遵循类似的协议。

**非嵌套**：

```python
import json

data = {'apple': 'red', 'banana': 'yellow', 'cucumber': 'green', 'types': ['fruit', 'vegetable']}

with open('data.json', 'w') as f:
    json.dump(data, f)
```

**嵌套**：

```python
import json

data = {'student': {'name': 'Sarah Ellington', 'grade': 'B+'}}

with open('data.json', 'w') as f:
    json.dump(data, f)
```

`open('data.json', 'w')` 以写入模式打开 `data.json`。写入模式会覆盖现有文件，或者如果文件不存在，则创建新文件。

#### 读取

读取数据在嵌套数据和非嵌套数据之间有所不同。由于嵌套数据非常常见，因此在有疑问时，请编写一个读取嵌套数据的函数。`json` 模块的数据读取函数是 `json.load(file)`。

以下是仅供参考和比较的非嵌套版本。

```python
import json

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
```

### 美化打印

美化打印 JSON 数据通过使用缩进和换行符来格式化数据，从而提高可读性和简化调试。美化打印为共享数据提供了一种清晰、易于访问的格式。这有助于文档编制和协作。

```python
import json

data = {'apple': 'red', 'banana': 'yellow', 'cucumber': 'green', 'types': ['fruit', 'vegetable']}

json_string = json.dumps(data, indent=4)
print(json_string)
```

`indent` 参数控制缩进级别。

```json
{
    "apple": "red",
    "banana": "yellow",
    "cucumber": "green",
    "types": [
        "fruit",
        "vegetable"
    ]
}
```
`json.dumps()` 函数中的参数用于格式化 JSON 数据并添加缩进。无论是嵌套数据还是非嵌套数据，美化打印都遵循相同的流程。

`json.dumps()` 函数中 `indent` 后面的数字决定缩进多少个空格。虽然 4 个空格比较常见，但缩进的最佳实践可能因系统而异。

输出：

### 错误处理
JSON 会根据您与数据交互的方式抛出不同的异常，但在所有情况下，使用 `try…except` 块都是处理 JSON 错误的标准方法。

输出：
无法解码 JSON：预期属性名称用双引号括起来：第 1 行第 29 列（字符 28）

有关如何处理错误的更多信息，请查看我们的错误处理教程。

### 从 API 获取 JSON 数据
JSON 是通过 API 传输数据的常用格式，`requests` 库经常用于在 Python 中处理此类数据。

以下是如何使用错误处理从 API 获取 JSON 数据的示例：

## 结论
JavaScript 对象表示法 (JSON) 是应用程序之间数据交换的基本工具。它在减少数据传输方面的效率使其成为 Web 客户端、服务器和 API 交互的首选。了解 JSON 的功能和最佳实践，包括正确的错误处理和美化打印，是高效处理现实世界场景的第一步。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)