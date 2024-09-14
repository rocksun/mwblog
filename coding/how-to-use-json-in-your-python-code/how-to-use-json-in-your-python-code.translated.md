# 如何在 Python 代码中使用 JSON

![如何在 Python 代码中使用 JSON 的特色图片](https://cdn.thenewstack.io/media/2024/09/00feadeb-getty-images-wy-8vsqrj5w-unsplash-1-1024x683.jpg)

如果您熟悉 [容器](https://thenewstack.io/containers/), 您可能也熟悉 [JSON](https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/). 如果您不熟悉，JSON 非常容易理解。JSON 代表 [JavaScript 对象表示法](https://thenewstack.io/an-introduction-to-json/), 它是一种用于存储和交换数据的语法。JSON 特别适用于从服务器发送到网页的数据。

JSON 的基本结构是名称/值对，用逗号分隔，对象用大括号括起来，数组用方括号括起来。它看起来像这样：

```json
{"students":[ {"firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}, {"firstName":"Anton", "lastName":"Frank", "year":"sophomore"}, {"firstName":"Jean", "lastName":"Barber", "year":"freshman"}]}
```

分解如下：

- “firstName”:”Olivia” 是一个键/值对
- *{“firstName”:”Olivia”, “lastName”:”Nightingale”, “year”:”senior”}* 是一个对象
- *“students”:[*
    - *{“firstName”:”Olivia”, “lastName”:”Nightingale”, “year”:”senior”},*
    - *{“firstName”:”Anton”, “lastName”:”Frank”, “year”:”sophomore”},*
    - *{“firstName”:”Jean”, “lastName”:”Barber”, “year”:”freshman”}*
    - *] *是一个数组。

但是如何在我们的 [Python](https://thenewstack.io/python/) 代码中使用 JSON 呢？幸运的是，有一个库可以实现这一点。该库是 *json*, 可以使用以下代码导入：

```python
import json
```

很简单。

要在 [Python](https://thenewstack.io/python/) 中使用 JSON，您需要了解如何将 JSON 转换为 Python 以及将 Python 转换为 JSON。让我们首先看看这两个操作是如何完成的。

## 将 JSON 转换为 Python

让我们获取一个 JSON 字符串并在一个简单的 Python 代码块中进行转换。为此，我们必须使用 *json.loads()* 函数。在我们的 *import json* 行之后，我们将使用一些 JSON 键/值对定义 x，如下所示：

```python
x = '{ "firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}'
```

请注意，我们必须将对象用单引号括起来。如果我们不这样做，Python 会报告错误。

接下来，我们使用 json.loads() 函数解析 JSON 对象（作为“y”），如下所示：

```python
y = json.loads(x)
```

最后，我们使用以下代码打印出对象中的一个元素：

```python
print(y["year"])
```

整个代码如下所示：

```python
import json
x = '{ "firstName":"Olivia", "lastName":"Nightingale", "year":"senior"}'
y = json.loads(x)
print(y["year"])
```

上面代码块的输出将是：

*senior*

## 将 Python 转换为 JSON

我们也可以通过将 Python 对象转换为 JSON 字符串来执行相反的操作。这次，我们使用 *json.dumps() *函数。

让我们使用与上面类似的示例。我们将使用 Python 字典 (dict) 定义 x，如下所示：

```python
x = { "name": "Olivia Nightingale", "age": "17", "year": "senior"}
```

然后我们使用 *json.dumps() *函数定义“y”，如下所示：

```python
y = json.dumps(x)
```

让我们使用以下代码打印结果：

```python
print(y)
```

整个代码块如下所示：

```python
import json
x = { "name": "Olivia Nightingale", "age": "17", "year": "senior"}
y = json.dumps(x)
print(y)
```

上面代码的输出将以 JSON 对象的形式出现，如下所示：

*{“name”: “Olivia Nightingale”, “age”: “17”, “year”: “senior”}*

使用 json 库，您可以将以下对象转换为其 JSON 等效项：

- dic
- list
- tuple
- str
- int
- float
- True
- False
- None

重要的是要了解 JSON 值仅限于以下内容：

- object – 键值对的集合
- array – 方括号中包含的值列表
- string – 用双引号括起来的文本
- number – 整数或浮点数
- boolean – true 或 false
- null – 空值

让我演示如何使用单个代码块将上述每个对象转换为其 JSON 等效项：

```python
import json
x = { "name": "Olivia", "age": "20", "graduated": False, "married": False, "majors": ("Theatre", "Communications"), "minors": None, "vehicles": [ {"type": "bicycle", "color": "pink"}, {"type": "car", "make": "Mini Cooper"} ]}
print(json.dumps(x))
```

上面代码的输出将是：

*{“name”: “Olivia”, “age”: “20”, “graduated”: false, “married”: false, “majors”: [“Theatre”, “Communications”], “minors”: null, “vehicles”: [{“type”: “bicycle”, “color”: “pink”}, {“type”: “car”, “make”: “Mini Cooper”}]}*

这看起来很丑。让我们进行一些格式化。使用 *json.dumps()*, 您可以定义缩进和分隔符。让我们缩进 5 个空格，并使用 . 和 = 分隔符，这在 *print* 行中完成，如下所示：

```python
print(json.dumps(x, indent=5, separators=(". ", " = ")))
```

现在输出看起来像这样：

```json
{
    "name" = "Olivia".
    "age" = "20".
    "graduated" = false.
    "married" = false.
    "majors" = [
        "Theatre".
        "Communications"
    ].
    "minors" = null.
    "vehicles" = [
        {
            "type" = "bicycle".
            "color" = "pink"
        },
        {
            "type" = "car".
            "make" = "Mini Cooper"
        }
    ]
}
```
```json
{
    "age": "20",
    "graduated": false,
    "majors": [
        "Theatre",
        "Communications"
    ],
    "married": false,
    "minors": null,
    "name": "Olivia",
    "vehicles": [
        {
            "color": "pink",
            "type": "bicycle"
        },
        {
            "make": "Mini Cooper",
            "type": "car"
        }
    ]
}
```

这样好多了。

我们还可以使用 *json.dumps()* 函数和 *sort_keys* 参数对结果进行排序。这一行代码如下所示：

1 |
print(json.dumps(x, indent=5, separators=(". ", " = "), sort_keys=True)) |
现在我们的输出如下所示：
```json
{
    "age": "20",
    "graduated": false,
    "majors": [
        "Theatre",
        "Communications"
    ],
    "married": false,
    "minors": null,
    "name": "Olivia",
    "vehicles": [
        {
            "color": "pink",
            "type": "bicycle"
        },
        {
            "make": "Mini Cooper",
            "type": "car"
        }
    ]
}
```
我们还可以从 [Python 代码](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/) 中写入 JSON 文件，这非常方便（尤其是在需要将数据从 Python 应用程序传递到需要 JSON 格式的 Web 应用程序时）。让我们使用上面的示例并将数据写入文件“students.json”。代码如下所示：

12345678910111213141516 |
import jsonx = { "name": "Olivia", "age": "20", "graduated": False, "married": False, "majors": ("Theatre", "Communications") "minors": None, "vehicles": [ {"type": "bicycle", "color": "pink"}, {"type": "car", "make": "Mini Cooper"} ]}with open("students.json", mode="w", encoding="utf-8") as write_file: json.dump(x, write_file) |
上面的代码不会在终端打印任何输出，而是将输出写入文件“students.json”。打开文件查看，您将看到数据以 JSON 格式显示。
这就是我的 Python 学习朋友们：如何在 Python 代码中轻松使用 JSON 或将数据从 Python 转换为 JSON。当您深入 Python 的兔子洞时，此功能将非常有用。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以收看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)