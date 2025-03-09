
<!--
title: unittest: Python 开发者内置的安全网
cover: https://cdn.thenewstack.io/media/2025/02/97b6f181-levi-meir-clancy-9fpm0ruywww-unsplash-1.jpg
-->

Python 内置的 unittest 模块为初学者提供了一个可访问的测试驱动开发切入点，同时为经验丰富的程序员提供了一个确保代码质量的框架。

> 译自：[unittest: Python's Built-In Safety Net for Developers](https://thenewstack.io/unittest-pythons-built-in-safety-net-for-developers/)
> 
> 作者：Jessica Wachtel

对于大多数开发者来说，测试通常不是编码中最受欢迎的部分，但它却是 100% 必要的。我[编程训练营](https://thenewstack.io/?p=2176624)的一位导师曾经把测试比作“编码的蔬菜”，这确实很贴切。通过在开发过程中[捕获错误](https://thenewstack.io/meet-early-the-ai-that-catches-bugs-before-they-bite/)，全面的测试可以增强对软件质量和稳定性的信心，而这正是你想要捕获它们的时机。它可以降低生产环境中不当软件行为的风险，从而提高应用程序性能、增强安全性并最大限度地减少停机时间。

经过良好测试的代码也能使你的工程师同事受益，因为它可靠、可维护且更易于重构。测试就像一个安全网，确保在进行更改后，现有功能仍然可以正常工作。此外，自动化测试可以加快迭代速度、加强协作，并提供关于代码预期行为的清晰文档。

在选择测试框架时，有很多选择。本教程将重点介绍使用 Python 内置包 [unittest](https://docs.python.org/3/library/unittest.html) 进行的简单测试。本教程主要面向没有单元测试经验的编码新手。`unittest` 对于喜欢内置方法的开发者来说是一个极好的选择。Python 的 `unittest` 模块擅长处理基本的单元测试，这些测试可以验证单个函数或方法在隔离状态下的正确性。这也是构建你自己的测试并熟悉它们工作原理的一个很好的起点。

## Python `unittest` 入门

`unittest.TestCase` 是 Python 的 `unittest` 模块中的一个类，它为编写和运行测试提供了框架。它是创建测试的基础类，测试是 Python 中的单个单元。
当你创建一个继承自 `unittest.TestCase` 的类时，你可以定义方法来测试代码中的特定功能。这些测试方法应该以 `test` 开头（例如，`test_addition` ）。在每个方法中，你使用各种断言方法来检查实际结果是否与预期结果匹配。

断言是一个检查条件是否为真的语句。如果为假，它会引发错误或异常。`unittest.TestCase` 提供以下断言：

*   `assertEqual(a, b)` 如果 `a == b` 则通过
*   `assertNotEqual(a, b)` 如果 `a != b` 则通过
*   `assertTrue(x)` 如果 `x` 为 `True` 则通过
*   `assertFalse(x)` 如果 `x` 为 `False` 则通过
*   `assertIsNone(x)` 如果 `x` 为 `None` 则通过
*   `assertRaises(Exception, func, *args)` 如果 `func(*args)` 引发异常则通过

## 构建你的第一个测试

这非常简单。在导入 `unittest` 之后，我们需要做的就是构建函数，然后创建并运行测试。

定义函数：

```py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

使用 `unittest.TestCase` 类创建测试：

```py
import unittest

class Operations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0) # Test with negative numbers

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

if __name__ == "__main__":
    unittest.main()
```

请注意，如果你使用的是 Jupyter notebook，你需要替换以下代码……

```py
if __name__ == "__main__":
    unittest.main()
```

用这段代码……

```py
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Operations))
```

在你的代码底部。

运行此测试将产生一条成功消息。

但是，只需进行一些小的调整就会导致测试失败：

```py

class Operations(unittest.TestCase):
    def test_add(self):
        # This test will pass
        self.assertEqual(add(2, 3), 5)  # Test if 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0) # Test with negative numbers

    def test_subtract(self):
        # This test will fail
        self.assertEqual(subtract(5, 3), 3)  # Incorrect expected value (should be 2)
        self.assertEqual(subtract(0, 4), -4)

if __name__ == "__main__":
    unittest.main()
```

## setup() 和 teardown()

`setup()` 和 `teardown()` 这些方法确保每个测试都是隔离的，并在一个干净的环境中运行，其中包含它所需的一切。

- `setup()` 是一个在每个单元测试之前运行的方法，用于设置任何必要的状态或资源。这可以用于在每个测试方法运行之前准备特定的环境或资源（例如，数据库连接或测试文件）。
- `teardown()` 清理测试之间的这些连接和资源，以确保每个测试都是独立的。

```py
class TestExample(unittest.TestCase):
    def setUp(self):
        self.x = 10
        self.y = 5

    def test_add(self):
        self.assertEqual(add(self.x, self.y), 15)

    def tearDown(self):
        print("Cleaning up after test")
```

## 对象 Mock

`unittest.mock` 允许你用模拟对象替换依赖项（例如，API 请求）。以下是如何模拟 API 请求：

```py
from unittest.mock import patch
import requests

def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()

class TestAPI(unittest.TestCase):
    @patch("requests.get")
    def test_get_data(self, mock_get):
        mock_get.return_value.json.return_value = {"message": "success"}
        self.assertEqual(get_data(), {"message": "success"})
```

## 结论

Python 的 `unittest` 模块提供了比上面列出的更复杂的测试需求的工具，但这些是入门的基础知识。`unittest` 非常适合初学者和经验丰富的工程师，使其成为希望寻找内置、可靠的解决方案来保护其代码质量的开发者的绝佳选择。
