
<!--
title: 如何在VS Code中运行 Pytest
cover: https://pytest-with-eric.com/images/Install_python_extension_vscode.JPG
-->

作为一名 Python 开发人员，您可能熟悉 Pytest，这个流行的单元测试框架。它是一个强大的工具，可以使用简单简洁的语法测试您的 Python 程序，并拥有丰富的内置功能。

> 译自 [How To Run Pytest In VS Code (Easy To Follow Step-By-Step Tutorial)](https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/index.html)，作者 Eric Sales De Andrade。

作为一名 Python 开发人员，您可能熟悉 Pytest，这是一个流行的单元测试框架。

它是一个强大的工具，可以使用简单简洁的语法测试您的 Python 程序，并具有大量内置功能和 [Pytest 插件](https://pytest-with-eric.com/pytest-best-practices/pytest-plugins/) 来增强您的测试体验。

大多数开发人员使用 CLI 运行测试。但实际上，您可以（并且更容易）只需单击鼠标即可运行测试。您可能想知道，“真的吗？但是怎么做呢？”。

如果您使用的是 VS Code，那么您可以在几分钟内完成设置。为您节省了在迭代开发和测试中花费的大量时间。

本文将指导您在 VS Code 环境中设置 Pytest。您将学习如何在 VS Code 上设置和配置 Pytest，包括自动测试发现（如果自动发现失败，则手动发现）。

我们将使用一个基本的 Python 模块（简单的计算器）来演示 VS Code 中的测试过程。

让我们开始吧。

## 目标

在本篇文章结束时，您应该能够：

- 在 VS Code 中设置和配置 Pytest
- 在 VS Code 中自动发现测试
- 使用 VS Code 中的 Pytest 执行测试

## 为什么在 VS Code 中使用 Pytest？

Visual Studio Code (VS Code) 因其广泛的功能、易用性、令人印象深刻的可定制性和大量扩展而受到开发人员的欢迎。

它包含一个嵌入式终端，允许您立即执行任何 CLI 命令，而无需单独打开命令提示符。

此外，还有数千个扩展可用于多种编程语言、工具和框架，使您可以根据需要自定义环境。

VS Code 包含 IntelliSense（代码建议）、语法高亮、错误检查、代码风格检查和错误高亮等功能。

根据 [Stack Overflow 开发者调查 2023](https://survey.stackoverflow.co/2023/)，大约 73.71% 的开发人员（业余和专业）将其用作其主要开发环境工具，并且随着嵌入式 AI（如 GitHub CoPilot 和聊天）的出现，它变得越来越受欢迎。

如果您是一名 Python 开发人员，那么您很可能将编写单元测试作为工作的一部分。使用 VS Code，您无需运行多个 CLI 命令来执行测试。

您可以设置一次，然后只需在 VS Code 中单击一个按钮即可。

好了，我们来看看如何实际操作。

## 先决条件

在我们在 VS Code 中设置 Pytest 之前，您需要在您的操作系统中安装以下先决条件，

- Python
- VS Code（本例中版本为：1.81.0）

## 在 VS Code 中设置 Pytest

要在 VS Code 中设置 Pytest，请按照以下步骤操作，

### 步骤 1 - 安装 Python 扩展

这是第一步，我们将在此步骤中在 VS Code 中安装 Python 扩展。打开您的 VS Code，并在扩展搜索引擎中搜索 *Python*。您将在搜索结果的顶部找到 Python 扩展。打开并安装它。

![](https://pytest-with-eric.com/images/Install_python_extension_vscode.JPG)

### 步骤 2 - 配置 Pytest

现在，Python 扩展安装将自动在您的环境中安装 Pytest。您只需要配置 Pytest。请按照以下步骤配置 Pytest。

1. **步骤 1**：单击左侧工具栏上的烧瓶图标。您可以在打开包含 Python 单元测试的存储库后找到它。

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step1.JPG)


2. **步骤 2**：现在单击“配置 Python 测试”，

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step2.JPG)

3. **步骤 3**：您将有两个选项可供选择。在此处选择 Pytest。

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step3.JPG)

4. **步骤 4**：选择包含测试代码的文件夹。

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step4.JPG)

5. **步骤 5**：假设您的测试已发现，请单击播放图标以运行测试。

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step5.JPG)

6. **步骤 6**：测试完成后，您将看到一个绿色勾号。

![](https://pytest-with-eric.com/images/Configuring_tests_with_Pytest_Step6.JPG)

注意 - 请注意，为了使自动发现正常工作，您需要在测试文件夹中有一个 `__init__.py` 文件，以及在 VS Code 工作区中打开一个单独的存储库文件夹（因为如果您在包含多个存储库的目录中，VS Code 可能无法发现测试）。

## 在 VS Code 中发现测试

配置 Pytest 后，VS Code 将自动发现您的单元测试。您可以在 `.vscode/settings.json` 文件中的 `"python.testing.cwd"` 参数下的设置中自定义要查找测试的文件夹。

例如 `.vscode/settings.json`

```json
{
    "files.autoSave": "onFocusChange",
    "[python]": {
        "editor.defaultFormatter": "ms-python.black-formatter"
    },
    "python.testing.pytestArgs": [],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.cwd": "${workspaceFolder}/tests",
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
}

```

您可以看到我已将其设置为在 `tests` 文件夹中查找测试。

并且为了使 Pytest 将您的 Python 文件检测为单元测试，请不要忘记在您的文件名中使用 `test` 作为前缀或后缀。例如 `test_example.py` 。

## 手动测试发现（如果自动发现失败）

测试发现是一项自动功能，它会检测您的测试，或者在未检测到测试时通知您。
启用 Python 项目的 Pytest 后，它会自动启动。但您可以按照以下步骤手动运行它：

**步骤 1**： 从 `视图 > 命令面板` 打开命令面板
或按 `Ctrl+Shift+P`
.**步骤 2**： 搜索 “测试：刷新测试” 并点击它。

![](https://pytest-with-eric.com/images/Test_discovery_command_palatte.JPG)

现在，如果没有错误，您将看到测试已成功发现。

![](https://pytest-with-eric.com/images/Test_discovery_success.JPG)

或者，如果您的测试文件或代码中缺少文件或存在错误，您将看到如下所示的错误消息：

![](https://pytest-with-eric.com/images/Test_discovery_fail.JPG)

如果在测试发现期间遇到任何错误，请确保您的测试文件位于正确的目录中，并且您的测试代码中没有错误。

现在我们已成功在 VS Code 中设置和配置 Pytest。让我们在 VS Code 环境中执行一个简单的测试。

## 示例代码

我们将从创建一个简单的项目开始。下面共享的 Python 代码是一个简单的计算器程序，它对两个变量执行数学运算。

src/calculator.py


```python
"""
Python code to perform mathematical operations on two variable
"""

def summation(num1: int, num2: int) -> int:
    """
    Calculate the summation of two number
    """
    return num1 + num2

def subtraction(num1: int, num2: int) -> int:
    """
    Calculate the subtraction of two number
    """
    return num1 - num2

def multiplication(num1: int, num2: int) -> int:
    """
    Calculate the multiplication of two number
    """
    return num1 * num2

def division(num1: int, num2: int) -> float:
    """
    Calculate the division of two number
    """
    return num1 / num2
```

## Tests

让我们为我们的计算器程序创建一个测试。以下是一个测试代码的简单示例，

tests/unit/test_calculator.py

```py
from src.calculator import (
    summation, 
    subtraction, 
    multiplication, 
    division
)

def test_summation():
    """
    Testing Summation function
    """
    assert summation(2, 10) == 12
    assert summation(3, 5) == 8
    assert summation(4, 6) == 10

def test_subtraction():
    """
    Testing Subtraction function
    """
    assert subtraction(8, 2) == 6
    assert subtraction(7, 5) == 2
    assert subtraction(4, 2) == 2

def test_multiplication():
    """
    Testing Multiplication function
    """
    assert multiplication(2, 2) == 4
    assert multiplication(7, 2) == 14
    assert multiplication(10, 2) == 20

def test_Division():
    """
    Testing Division function
    """
    assert division(5, 5) == 1
    assert division(70, 10) == 7
    assert division(16, 4) == 4
```


## 运行测试

现在我们已经有了简单的 Python 程序，让我们按照本文中描述的步骤进行测试。

![](https://pytest-with-eric.com/images/example_test_result.JPG)

*您也可以通过点击测试旁边的绿色播放图标来运行单个单元测试。*

您可以看到这对于迭代地测试/调试您的单元测试是多么有用。

还可以为您的测试定义配置和其他设置，例如运行时环境变量，但这将是另一个主题。

同时，如果您想学习如何执行此操作，我们有一篇关于设置 [Pytest 环境变量](https://pytest-with-eric.com/pytest-best-practices/pytest-environment-variables/) 和 [使用 Pytest.ini 的 Pytest 配置](https://pytest-with-eric.com/pytest-best-practices/pytest-ini/) 的有趣文章。

## 结论

Pytest 是一个很棒的测试框架，将其与 VS Code 相结合使测试过程更加轻松和高效。

在本文中，您学习了如何在 VS Code 环境中设置和配置 Pytest。

通过自动化重复工作，您可以节省手动传递 CLI 命令、配置或环境变量的时间。

VS Code 将自动发现测试，如果这不起作用，还有其他方法可以手动发现您的测试。

通过利用这些知识，您可以改进您的测试过程，使其更加高效。