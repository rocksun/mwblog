
<!--
title: Python Try...Except的使用
cover: https://cdn.thenewstack.io/media/2024/09/5bb27c44-python-try-except-command.jpg
-->

Python 本身不会提供关于导致应用程序停止的错误的详细信息。尝试...除了填补了这些空白。

> 译自 [Python Try ... Except: What It Is and How to Use It](https://thenewstack.io/python-try-except-what-it-is-and-how-to-use-it/)，作者 Jack Wallen。

代码越复杂，您就越依赖于处理[异常](https://thenewstack.io/python-how-to-work-with-basic-exception-handling/)。如果您还没有遇到异常，它们是在程序执行期间发生的错误。使用[Python](https://thenewstack.io/python/)，异常不会产生信息丰富的错误，而是会直接停止。当您的应用程序毫无解释地停止时，您（或您的用户）可能会不知所措。

对于 Python，有一个一石二鸟的方法可以帮助缓解这个问题，`try … except`。`Try`允许您测试代码块以查找错误，而 `except`允许[处理错误](https://thenewstack.io/error-handling-from-backends-to-the-frontend/)。

这样想：

Python 会*尝试*执行您的代码，如果发生错误，*except* 会处理它。

`try … except`的结构如下：

```python
try: 
   <try to do something> 
except 
   Exception: <handle the error>
```

以下是一个非常简单的 `try … except`示例：

```python
try:
   print(x)
except:
   print("An exception has occurred")
```

如果您运行上面的代码，输出将是：

```
An exception has occurred
```

为什么呢？在上面的代码中，`x`从未定义。为了更好地说明这一点，让我们只运行 `print(x)`行，这将输出：

```
NameError: name 'x' is not defined
```

当我们有 `try … except`块时，Python 会看到 `x`没有定义，然后转到 `except`部分并执行第二个 `print`行。

也可以指定要注意的错误。让我们坚持我们所知道的（在本例中是 `NameError`）。看看下面的代码块：

```python
try:
  print(x)
except NameError:
  print("You've not defined x")
except:
  print("Something other than a NameError went wrong")
```

您可能可以预测输出将是什么：

```
You've not defined x
```

还有其他类型的异常可以使用 `try … except`捕获，例如：

- Exception：非系统退出异常和用户定义异常。
- ArithmeticError：各种算术错误。
- BufferError：当缓冲区相关操作无法执行时。
- LookupError：当映射或序列上的键或索引无效时。
- AssertionError：当断言语句失败时。
- AttributeError：当属性引用或赋值失败时。
- EOFError：当函数在没有读取任何数据的情况下遇到文件结尾条件时。
- ImportError：当 import 语句无法加载模块或当“from list”中找不到名称时。

您可以在[官方文档](https://docs.python.org/3/library/exceptions.html)中找到 Python 异常的完整列表。

还记得上面有两个 `except`语句的示例吗？您还可以使用 `finally`语句，无论代码块是否引发错误，该语句都会执行。`finally`语句如下所示：

```python
try:
  print(x)
except:
  print("X was not defined")
finally:
  print("Our try … except block is complete")
```

您可能会认为上面的代码块将打印出一行：

```
X was not defined
```

但是，`finally`语句无论如何都会执行代码，因此输出实际上将是：

```
X was not defined
Our try … except block is complete
```

`finally`语句可以帮助关闭对象和清理宝贵的资源。

创建一个代码块，该代码块将创建一个用于写入的文件，写入文件，关闭文件，然后在出现错误时打印错误。代码块如下所示：

```python
try:
  x = open("newstack.txt")
  try:
    x.write("Hello, New Stack!")
  except:
    print("An error occurred when writing to the file")
  finally:
    x.close()
except:
  print("Something went wrong when opening the file")
```

您能猜到上面的输出是什么吗？如果您猜到 `Something went wrong when opening the file`，那么您是正确的。我们收到此错误是因为 newstack.txt 文件没有以写入权限打开。

像这样授予文件适当的访问权限：

```python
try:
  x = open("newstack.txt", 'w')
  try:
    x.write("Hello, New Stack!")
  except:
    print("An error occurred when writing to the file")
  finally:
    x.close()
except:
  print("Something went wrong when opening the file")
```

当您运行上面的代码时，输出中不会出现任何错误。相反，`Hello, New Stack!`行将写入 newstack.txt 文件。没有错误。但是，由于 `finally`语句，您知道 newstack.txt 文件已正确关闭，因此您可以继续进行。

您还可以使用 `raise`关键字引发异常。`raise`关键字用于引发异常并停止程序的流程。例如，这可用于在用户输入超出所需参数的数据时停止程序。

以下是 `raise`关键字的工作原理：

```python
x = "New Stack"
 
if not type(x) is int:
   raise TypeError("You can only input integers")
```

上面的命令输出将包括以下语句：

```
You can only input integers
```

为什么？因为 `New Stack`
是一个字符串，而不是一个整数。

这就是 Python 的 `try … except` 语句的精髓。这将非常有助于确保您的 Python 程序能够更好地处理由于编程问题或用户输入而发生的错误。
