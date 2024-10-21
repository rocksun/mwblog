# 使用 Docstring 文档化 Python 代码

![使用 Docstring 文档化 Python 代码的特色图片](https://cdn.thenewstack.io/media/2024/10/fab2a3a1-bozhin-karaivanov-iiiu2fiury8-unsplash-1-1024x683.jpg)

[文档化代码](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/) 是必不可少的，尤其是在团队合作开发项目时。如果没有适当的文档，团队中的其他开发人员可能无法理解你试图用代码块实现的目标，这会导致瓶颈。在一个效率至上的世界里，避免工作流程中的减速至关重要。

你如何做到这一点？

文档化你的代码。

当然，始终存在传统的代码文档化方法，看起来像这样：

```python
# 这是一个简单的 Hello World 应用程序
print("Hello, World!")
```

上面我们有一个简单的 [Hello World 应用程序](https://thenewstack.io/typescript-tutorial-go-beyond-hello-world/)，只有一个由单个 # 字符定义的注释。如果该注释换行到第二行，你可以添加另一个 # 字符，如下所示：

```python
# 这是一个简单的 Hello World 应用程序
# 它打印 "Hello, World!" 到控制台
print("Hello, World!")
```

这是一种简单的代码注释方法，但不是唯一的方法。让我向你介绍另一种文档化 [Python 代码](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/) 的方法，即 docstring。

## Docstring

当你知道你的注释将占用多行，并且不想用一列 # 字符来使代码混乱时，docstring 是一种很好的注释方法。

本质上，docstring 是一种特殊的注释类型，用于描述代码块的目的和/或功能。这可以用于模块、类、方法和/或函数，并放置在每个定义的后面。

要使用 docstring，你可以在代码块的开头和结尾放置三个双引号 (“””)，如下所示：

```python
"""
这是一个简单的 Hello World 应用程序
它打印 "Hello, World!" 到控制台
"""
print("Hello, World!")
```

在上面的示例中，我们的 docstring 是：

```python
"""
这是一个简单的 Hello World 应用程序
它打印 "Hello, World!" 到控制台
"""
```

如你所见，顶部和底部都有三个双引号，这表示它是 Python 的 docstring。以下是一个完整的应用程序（它接收用户输入并将其写入文件），其中包含两个 docstring 以及常规注释：

```python
"""
这是一个简单的 Python 应用程序，它接收用户输入并将其写入文件。
"""
def write_to_file(filename, content):
    """
    将内容写入文件。

    Args:
        filename: 文件名。
        content: 要写入文件的内容。
    """
    with open(filename, "w") as f:
        f.write(content)

# 获取用户输入
user_input = input("请输入一些内容：")

# 将用户输入写入文件
write_to_file("my_file.txt", user_input)
```

Docstring 也可以占用一行，如下所示：

```python
"""这是我的 Python 代码注释"""
```

需要注意的是，与常规注释一样，[Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) 标准库要求代码行不超过 79 个字符，Python 代码的样式指南建议 docstring 的行长限制为 72 个字符。这意味着注释的单行不应超过 72 个字符，这就是 docstring 重要的原因。当你的注释需要多行来解释你正在做什么时，你可以使用 # 字符在每行之前添加一个 # 字符，或者使用 docstring。

但是，典型的最佳实践表明，docstring 通常用于解释对象。对于其他代码片段，请使用传统的注释。Docstring 通常包含以下组件：

- 一行摘要。
- 摘要下方的一行空白。
- 进一步的阐述。
- 另一行空白。

我们在上面的代码中已经看到了这一点。例如：

```python
"""
这是一个简单的 Python 应用程序，它接收用户输入并将其写入文件。
"""
```

第一行是摘要，后面跟着一行空白。接下来是阐述，后面跟着结束的 “””。要正确完成 docstring，在结束的 “”” 和下一行代码之间应该有一个空格。

## 类 Docstring

然后是类 docstring，用于解释你创建的类。类 docstring 包含以下内容：

- 类功能的简要摘要。
- 属性和方法的描述。
- 任何重要的注意事项或使用示例。

以下是一个类 docstring 的示例：

```python
class MyClass:
    """
    这是一个简单的类，它演示了如何使用 docstring。

    Attributes:
        name: 类的名称。
        age: 类的年龄。

    Methods:
        greet(): 打印问候语。
    """
    def __init__(self, name, age):
        """
        初始化 MyClass 对象。

        Args:
            name: 类的名称。
            age: 类的年龄。
        """
        self.name = name
        self.age = age

    def greet(self):
        """打印问候语。"""
        print(f"你好，我的名字是 {self.name}，我 {self.age} 岁。")
```

如你所见，我们有一个多行类 docstring 和两个单行 docstring。

你可以使用其他 docstring，例如：

- 包和模块 docstring：列出导出的模块和子包。这些类似于类 docstring，只是用于模块及其内部的函数。
- 脚本 docstring：描述整个 Python 脚本或模块的总体目的和功能的 docstring。

这就是你对 Python docstring 的介绍。使用这些方法可以确保你的代码易于阅读和理解，这使得它们成为必须的，因为在多个团队成员必须参与你编写的代码的项目中，你不想让你的代码被多个传统的注释块弄得乱七八糟。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)