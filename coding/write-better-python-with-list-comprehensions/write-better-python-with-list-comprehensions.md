
<!--
title: 用列表推导式编写更优秀的Python代码
cover: https://cdn.thenewstack.io/media/2024/11/57ed8192-getty-images-xxmmogao9og-unsplash-1.jpg
-->

本教程演示如何使用Python的列表推导式，它为开发者提供了一种编写更高效、更易读代码的方法，用单行解决方案替换传统的循环。

> 译自 [Write Better Python With List Comprehensions](https://thenewstack.io/write-better-python-with-list-comprehensions/)，作者 Jessica Wachtel。

[Python](https://thenewstack.io/python/) 列表推导式在一行高效易读的代码中，从现有的列表和序列生成新的列表。它们提供了一种简洁的语法来完成此任务，从而减少了代码行数。与其使用多行代码通过循环执行操作，[列表推导式](https://www.w3schools.com/python/python_lists_comprehension.asp) 使用一对方括号将循环和可选条件嵌入到一行中。列表推导式可以使用任何可迭代对象（集合、字符串、元组、列表）来生成新的列表。列表推导式可以用于单个列表或展平嵌套列表。

列表推导式被认为是“[Pythonic](https://thenewstack.io/mit-created-compiler-speeds-up-python-code/)”风格的代码，因为它与 Python 编写简洁高效代码的理念紧密契合。它们不仅在执行操作方面有效，而且列表推导式也更容易一目了然地理解。

这是一个构建偶数列表的循环示例：

```py
even_numbers = []
for n in range(1, 11): 
    if n % 2 == 0:  
        even_numbers.append(n) 

print(even_numbers)
```

输出: [2, 4, 6, 8, 10]

与作为列表推导式执行的相同操作相比：

```py
even_numbers = [n for n in range(1, 11) if n % 2 == 0] 

print(even_numbers)
```

输出: [2, 4, 6, 8, 10]

在许多以前由循环完成的重复性任务和数据处理方面，列表推导式是一个有用的工具。列表推导式在现实世界中的一些示例包括：

快速网页内容渲染：列表推导式自动创建重复的 HTML 标签或字符串。这种动态内容生成简化了创建基于文本内容（例如链接、表格行）的开发过程。

[数据分析](https://thenewstack.io/whats-pipeline-free-real-time-data-analytics/)：列表推导式降低了代码复杂性，从而消除了任何潜在的错误。它们简化了数据转换，并允许快速且易读的数据修改。诸如将值转换为其他值的处理任务，是列表推导式的绝佳用例。

更快的原型设计和测试周期：开发人员可以使用列表推导式创建模拟数据（例如用户配置文件和交易）来模拟现实场景。

更轻松的系统故障排除和监控：列表推导式为快速过滤和分析日志文件提供了一个优雅的框架。开发人员可以编写一行简单的代码，快速扫描日志并提取相关条目，例如系统趋势和应用程序日志。

能够对大型数据集进行高效计算：在执行诸如规范化值或应用统计计算之类的数学和数据密集型任务时，列表推导式减少了对冗长、重复循环的需求。

列表推导式并非万能的解决方案。虽然它们对于特定任务非常强大，但在所有情况下都不能使用。当处理复杂的逻辑、就地修改、错误处理、内存密集型操作和错误处理时，传统的循环提供了更大的控制、可读性和灵活性。列表推导式最适合简单的、单步转换和过滤，其中新的列表是预期的输出。

## 操作方法：

以下是使用单个列表的基本语法：

```py
variable = [expression for item in iterable if condition]
```

`if` 条件不是必需的。只有当你的代码使用条件时才使用 `if` 条件。

这是一个没有 `if` 条件的简单列表推导式示例：

```py
squares = [n ** 2 for n in range(1, 11)]

print(squares)
```

输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

这是一个添加了 `if` 条件的相同示例。

```py
even_squares = [n ** 2 for n in range(1, 21) if n % 2 == 0]

print(even_squares)
```

输出: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

简化嵌套循环的列表推导式的基本语法如下所示：

```py
variable = [expression for item1 in iterable1 for item2 in iterable2]
```

这是一个没有条件语句的示例：

```py
colors = ["red", "green", "blue"]
shapes = ["circle", "square"]

combinations = [(color, shape) for color in colors for shape in shapes]

print(combinations)
```

输出: [('red', 'circle'), ('red', 'square'), ('green', 'circle'), ('green', 'square'), ('blue', 'circle'), ('blue', 'square')]

最后的示例包含一个条件语句：

```py
colors = ["red", "green", "blue"]
shapes = ["circle", "square"]

red_combinations = [(color, shape) for color in colors for shape in shapes if color == "red"]

print(red_combinations)
```

输出: [('red', 'circle'), ('red', 'square')]

列表推导式是[Python编程](https://thenewstack.io/what-is-python/)中宝贵的工具，它提高了效率和可读性，同时简化了许多常见任务。通过了解它们的优势和局限性，开发人员可以利用此功能编写更简洁、更“Pythonic”的代码。
