
<!--
title: 掌握这些技巧，精通Python调试艺术
cover: https://cdn.thenewstack.io/media/2025/03/28e4ccdd-getty-images-cnekrh4k6f8-unsplash-1.jpg
summary: Python开发者必看！掌握Debug神技，告别"解决不了"心态！巧用`print()`、`pdb`定位Bug，善用`logging`模块，编写`unittest`保证代码质量。集成IDE断点调试、单步执行、变量监视，配合`pylint`、`mypy`等外部工具，提升Debug效率，搞定云原生AI项目！
-->

Python开发者必看！掌握Debug神技，告别"解决不了"心态！巧用`print()`、`pdb`定位Bug，善用`logging`模块，编写`unittest`保证代码质量。集成IDE断点调试、单步执行、变量监视，配合`pylint`、`mypy`等外部工具，提升Debug效率，搞定云原生AI项目！

> 译自：[Master the Art of Python Debugging With These Tips](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/)
> 
> 作者：Jessica Wachtel

每位开发者，无论经验如何，都会遇到 bug。**Bug 是编码的正常组成部分**——也许不是每个人最喜欢的部分，但绝对是他们日常工作的一部分。编码的成功不在于避免 bug，而在于你如何处理和解决它们。[调试代码](https://thenewstack.io/rookout-brings-debugging-to-third-party-code/)是任何程序员的一项基本技能，作为一名 [Python](https://thenewstack.io/python/) 初学者，培养有效的调试习惯将帮助你更快地解决问题并更好地学习这门语言。[调试](https://thenewstack.io/how-generative-ai-is-revolutionizing-debugging/)不是你编码能力的反映；而是一个成长和进步的机会。这些 [Python 初学者](https://thenewstack.io/python-for-beginners-lists/)调试技巧将帮助你入门！

**“我能做到”的心态 > “哦不！我永远解决不了这个问题”**

在许多挑战中，正确的心态是成功的关键。调试也不例外。

- 调试需要时间和实践。要有耐心。
- 一次只更改一件事并重新测试。不要试图一次完成所有事情。
- 调试是一个谜题。很容易感到疲惫，但要保持冷静。冷静和勤奋会带来清晰。
- 休息一下！如果调试变得过于令人沮丧或难以承受，请走开，在户外散步或吃一块披萨后回来。

开始调试的最简单方法是检查常见的错误。这可能包括缩进错误（因为 Python 对缩进很敏感）、变量作用域问题或意外的拼写错误。如果这不起作用，请查看以下工具。

**理解错误消息**

当出现问题时，Python 会提供有用的错误消息，也称为堆栈跟踪。以下是如何有效地使用它们：

- 首先阅读最后一行。这是实际的错误类型和消息。
- 追溯这些行。堆栈跟踪显示了错误发生在代码中的哪个位置。

代码示例：

```
x = 1 / 0
```

Output: ZeroDivisionError: division by zero

**使用 `print()` 语句**

在代码中添加 `print()` 语句有助于跟踪变量的流程和值。如果出现错误，请检查打印的值是否符合你的预期。你可以根据需要使用任意数量的 `print()` 语句。

代码示例：

```py
def add_numbers(a, b):
    # Debugging: Print the values of a and b
    print(f"Debug: a = {a}, b = {b}")
    result = a + b
    # Debugging: Print the result of the addition
    print(f"Debug: result = {result}")
    return result

# Calling the function with sample values
add_numbers(5, 3)
```

```
Output: Debug: a = 5, b = 3

Debug: result = 8

8
```

- **输入值的打印语句**：第一个打印显示了操作之前 a 和 b 的值，有助于验证它们是否符合你的预期。
- **结果的打印语句**：第二个打印显示了加法后的结果，这有助于确认函数是否按预期执行。

**利用 `pdb`**

`pdb` 是 Python 的内置调试器。它允许你暂停执行并以交互方式检查变量。

在你想要调试的地方添加此行：

```python
import pdb; pdb.set_trace()
```

代码示例：

```py
x = 10
y = 20
import pdb; pdb.set_trace()
result = x + y
print(result)
```

在调试器中，你可以：

- 键入 `n` 转到下一行。
- 键入 `p variable_name` 检查变量。
- 键入 `c` 继续执行。

**检查假设**

确保没有简单的错误和修复。问自己以下问题：

- 数据类型是否正确？
- 循环和条件是否按预期运行？

代码示例：

```python
Python 有内置函数可以帮助解决这个问题。在此示例中，`len(nums)` 将确认范围限制。[此处有更多信息](https://docs.python.org/3/library/functions.html#len)，你可以阅读有关 `len()` 函数以及在何处阅读更多类似函数的信息。
```

### 使用 `logging`

Python 中的 `logging` 模块为从你的应用程序发出日志消息提供了一个灵活的框架。与使用 `print()` 语句进行调试不同，`logging` 允许你按严重性（例如，`DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL`）对日志消息进行分类，并将它们输出到不同的目标（控制台、文件、远程服务器）。

代码示例：

```python
Output:

INFO:root:Application started

DEBUG:root:Starting data processing

INFO:root:Data processing started

WARNING:root:Data quality is low

ERROR:root:Error occurred during processing

CRITICAL:root:Processing failed!
```

有关 `logging` 的更多信息，请查看 [Python 文档](https://docs.python.org/3/library/logging.html)。

### 编写单元测试

Python 有一个 `unittest` 模块，可以帮助你编写验证代码的测试。

代码示例：

```python
**要测试的函数**：`add_numbers(a, b)` 返回 `a` 和 `b` 的总和。**测试用例类**：`TestAddNumbers` 继承自 `unittest.TestCase`，并包括三个测试方法（`test_add_positive_numbers`、`test_add_negative_numbers` 和 `test_add_mixed_numbers`），每个方法都测试 add_numbers 函数的不同场景。**断言**：`assertEqual()` 方法检查 `add_numbers(a, b)` 的结果是否与预期结果匹配。
```

### 使用带有内置调试功能的 IDE
[集成开发环境 (IDEs)](https://thenewstack.io/best-open-source-ides/)，例如 [PyCharm](https://thenewstack.io/getting-started-with-python-on-macos/)、[VS Code](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) 或 [Thonny](https://thonny.org/) 都内置了调试工具。IDEs 提供以下工具来方便调试。

**断点 (Breakpoints)**

大多数 IDE 允许你在代码中设置断点。断点会在特定行暂停程序的执行，使你能够检查变量、评估表达式并逐行单步执行代码。

**单步执行 (Step Over, Step Into, Step Out)**

这些功能允许你控制程序的执行流程。

- Step Over: 执行当前行代码并移动到下一行。
- Step Into: 进入函数或方法以逐行调试它。
- Step Out: 退出当前函数并返回到调用函数。

**变量监视 (Variable Watch)**

此工具允许你跟踪程序执行期间特定变量的值。你可以监视它们在单步执行代码时的变化，从而帮助识别与变量状态相关的问题。

**调用堆栈检查 (Call Stack Inspection)**

调用堆栈显示导致当前执行点的函数调用。通过检查调用堆栈，你可以了解函数调用的顺序以及代码在其执行流程中的位置。

**控制台输出/日志窗口 (Console Output/Log Window)**

IDEs 通常包含一个控制台或日志窗口，你可以在其中查看打印语句或日志记录的输出。这对于跟踪实时输出、错误消息和警告非常有用，这些可以为调试提供重要的上下文。

### 使用外部工具

**linter** 是一种分析源代码以检测基于预定义编码标准的潜在错误、bug 或样式问题的工具。流行的 linters，如 `pylint` 和 `flake8` 可以捕获样式和语法问题。

**静态分析器 (static analyzer)** 是一种检查源代码而不执行它以查找潜在错误、bug 或安全漏洞的工具。它检查代码的结构、流程和逻辑，通常标记诸如未初始化的变量、内存泄漏和违反编码标准等问题。`mypy` 是一个静态分析器，可以帮助检查类型一致性。

### 随着时间的推移会变得更容易！

调试是一种可以通过实践提高的技能。将调试作为开发的正常组成部分来接受。通过遵循这些技巧，你将更有信心识别和解决 Python 代码中的 bug。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。