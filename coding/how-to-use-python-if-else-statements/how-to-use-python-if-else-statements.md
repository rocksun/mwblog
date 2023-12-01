<!--
title: Python条件判断的应用
cover: https://cdn.thenewstack.io/media/2023/11/c37661ff-adi-goldstein-mdinbvq1sfg-unsplash-e1701215290162-1024x588.jpg
-->

本教程将详细说明如何在 Python 中运用 if-else 条件判断。

> 译自 [How to Use Python If-Else Statements](https://thenewstack.io/how-to-use-python-if-else-statements/)，作者 Jack Wallen。

您每天都要做出决定。当您醒来时，您要决定吃什么早餐，这可能会导致您在咖啡或橙汁之间进行选择。您决定喝什么饮料可能取决于您选择麦片、燕麦片还是酸奶作为您的膳食。

这种类型的决定将持续整天。穿什么衣服，走哪条路上班，使用哪个应用程序执行哪项任务，午餐吃什么，跟谁说话......无休无止。

这里有一个现实生活中的 [if-else](https://thenewstack.io/so-much-more-python-for-beginners-functions/) 语句的完美例子:

如果下雨，我会带伞出门。

很简单。

大多数[编程语言](https://thenewstack.io/25-most-popular-programming-languages-used-by-devops-pros/)都有条件语句，有助于指导程序流程将如何继续。对于 [Python](https://thenewstack.io/yet-more-python-for-beginners-saving-input-to-a-file/)，该条件语句是 if-else，这是您可以利用的非常方便的工具。if-else 语句应该被视为成功的 [Python 程序员](https://thenewstack.io/python/)的必备条件。

本质上，if-else 语句用于执行任何给定条件的 true 和 false 部分。继续我上面的例子，true 部分可以是“我会带伞”，false 部分可以是“如果不下雨”。换句话说，如果下雨我会带伞，否则(如果不下雨)我就不会带。

那么，如何在 Python 中使用 if-else 语句呢?

非常容易。

让我向你展示。

## If-Else 语句的工作原理

在 Python 中，if-else 语句的结构如下:

如果条件:

```
# 如果语句为真，执行此操作
```

if-else 语句的流程如图 1 所示。

图1

![](https://cdn.thenewstack.io/media/2023/11/b8f23bf6-ifelse.jpg)

*if-else 语句流程图。*

当 Python 进入 if-else 语句时，如果条件的结果为 true，它会从条件移动到执行，否则它会跳过执行并退出语句。

## 一个简单的例子

让我们创建一个 if-else 语句，它将根据语句打印一条消息。这个示例应用程序将执行以下操作:

如果 i 小于 10，它将打印出“i 小于 10”，否则它将打印出“i 不满足条件”。非常简单。

因为 if-else 语句是内置在 Python 中的，所以我们不需要担心导入任何库，所以我们可以直接进入脚本本身。我们的示例脚本如下所示:

i = 10

如果(i > 10): 
打印("i 小于 10")
打印("i 不满足条件")

使用以下命令创建 Python 脚本:

nano ifelse.py

将上面的脚本粘贴到文件中并保存/关闭新文件。

使用以下命令运行新的 Python 应用程序:

python3 ifelse.py

输出将是:

i 不满足条件

让我们使其更实用些。我们将做的是允许用户输入。为此，我们将使用 float() 方法定义 i，该方法从字符串返回浮点数。这是必需的，因为用户可以输入小数点值。如果没有 float()，用户输入小数，应用程序将失败。

float() 行如下所示:

i = float(input("输入一个数字:"))

接下来，我们将采用完整的 if-else 语句，因此我们将首先有一个 if 语句，然后是一个 else 语句，每个语句都将使用 print() 函数输出不同的文本字符串。完整的脚本如下所示:

i = float(input("输入一个数字:"))

如果 i < 10:
 打印("i 小于 10")
否则:
 打印("i 不满足条件")

使用以下命令创建脚本:

nano ifelse2.py

粘贴上面的脚本，然后保存文件。

使用以下命令运行脚本:

python3 ifelse2.py

系统会要求您输入一个数字。只要数字(即使带有小数点值)小于 10，输出将是:

i 小于 10

如果输入大于 10(否则)，输出将是:

i 不满足条件

让我们创建一个带有复合测试的脚本。我们的测试将是年龄和身高是否满足坐过山车的要求(其要求乘客必须年满 12 岁且至少 48 英寸高)。

首先，我们将定义年龄和身高变量，如下所示:

age = int(input("输入你的年龄:"))
height = int(input("输入你的身高(英寸):"))

接下来是将使用我们的变量的 if-else 语句。诀窍在于我们的 if 语句将使用复合测试，如下所示:

if age > 12 and height > 48: 

在 if 语句之后，我们使用 print() 函数并打印出享受这趟旅程。我们的 else 语句将不幸地打印出抱歉，您无法享受这次乘坐。

完整的脚本如下所示:

age = int(input("输入你的年龄:"))
height = int(input("输入你的身高(英寸):"))

如果 age > 12 and height > 48:
 打印("享受这趟旅程。")
否则:
 打印("抱歉，您无法享受这次乘坐。")

使用以下命令创建新文件:

nano ride.py

粘贴脚本并保存/关闭新文件。

使用以下命令运行脚本:

python3 ride.py 

输入你的年龄，然后输入你的身高。如果您满足这两个要求，您将看到享受这趟旅程，否则(else)您将看到抱歉，您无法享受这次乘坐。

如果您觉得您已经掌握了 Python，那么您的学习到此结束。

否则......下周再来获取更多 Python 好东西。
