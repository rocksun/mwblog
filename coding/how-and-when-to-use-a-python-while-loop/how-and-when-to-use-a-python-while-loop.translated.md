## 如何（以及何时）使用 Python While 循环

![如何（以及何时）使用 Python While 循环的特色图片](https://cdn.thenewstack.io/media/2024/04/32cec1d4-etienne-girardet-chp1itgplka-unsplash-1-1024x768.jpg)

While 循环是编程的一个基本方面。While 循环所做的是继续执行一条语句（或一组语句），直到满足特定条件。一个显而易见的例子（许多人都会理解）可能是这样的：*只要我的银行账户有钱，我就可以买东西。*

该语句是*我可以买东西*，条件是*只要我的银行账户有钱*。当您花光所有钱时，您将无法再购买东西（或支付账单）。

当您需要重复执行一条语句（或多条语句）时，While 循环是一个不错的选择。

*for* 和 *while* 循环之间的区别在于，*for* 循环只是遍历集合（或可迭代对象）并完成，而 *while* 循环则持续到满足特定条件为止。

*for* 循环更容易使用，但在某些情况下需要使用 *while* 循环。例如，您可能不知道必须重复执行该语句的次数。

我们来看一下执行相同操作的基本 Python 循环示例。首先，一个将打印范围内的数字的 for 循环。该循环可能如下所示：

```python
for i in range(11):
    print (i)
```

我们已将 for 循环设置为打印 11 范围内的 i。该代码的输出将如下所示：

*0*
*1*
*2*
*3*
*4*
*5*
*6*
*7*
*8*
*9*
*10*

请记住，在编程中，编号从 0 开始，因此 11 的范围将从 0-10。

现在，让我们使用 *while* 循环执行相同操作。我们必须做的第一件事是用以下内容定义 *i*：

```python
i = 1
```

接下来，我们创建 lop，其中指出当 i 小于 11 时，以 1 的增量打印 i。该循环如下所示：

```python
while i < 11:
    print(i)
    i += 1
```

整个代码是：

```python
i = 1
while i < 11:
    print(i)
    i += 1
```

如果我们运行上述代码，我们将获得与 *for* 循环相同的输出。

但是，当条件未知时如何运行 *while* 循环呢？例如，您希望接受用户的姓名输入，并允许他们继续输入姓名，直到完成。当他们输入所有姓名后，他们可以输入 *end* 退出循环。退出是条件，从输入中接受姓名是语句。

我们做的第一件事是将 *names* 定义为一个空列表，如下所示：

```python
names = []
```

接下来，我们将 *new_name* 定义为除 quit 之外的任何内容。在这种情况下，我们将它定义为空，如下所示：

```python
new_name = ' '
```

现在，我们可以编写一个循环，以这种方式接受用户的输入：

```python
while new_name != 'end':
    new_name = input("输入要添加的姓名，并以 'end: ' 结束：")
    names.append(new_name)
```

我们使用 append 函数来接受在前面姓名之后输入的新姓名。

最后，我们使用以下内容打印姓名：

```python
print(names)
```

整个代码如下所示：

```python
names = []
new_name = ''
while new_name != 'end':
    new_name = input("输入要添加的姓名，并以 'end: ' 结束：")
    names.append(new_name)
print(names)
```

运行上述代码，它将指示用户输入姓名，并通过输入 *end* 结束运行。输出可能如下所示：*[‘Aaron Kennedy’，‘Camile St. Joan’，‘Anton Frank’，‘Jean Barber’，‘Clara Beach’，‘end’]*

上述问题在于输出包括 *end*，这不是一个姓名。我们可以使用一个将 *new_name* 定义为除 *end* 之外的任何内容的 *for* 循环来解决此问题，如下所示：

```python
if new_name != 'end':
    names.append(new_name)
```

现在，我们的代码如下所示：

```python
names = []
new_name = ''
while new_name != 'end':
    new_name = input("输入要添加的姓名，并以 'end: ' 结束：")
    if new_name != 'end':
        names.append(new_name)
print(names)
```

如果我们输入与上面相同的姓名，并通过输入 end（并按 Enter）结束，则输出现在将如下所示：

*[‘Aaron Kennedy’，‘Camile St. Joan’，‘Anton Frank’，‘Jean Barber’，‘Clara Beach’]*

已修复。

这里有另一个接受用户输入但为他们提供可供选择的菜单的示例。我们将提供不同类型的食物。首先，我们用以下语句指导用户该怎么做：

```python
print("\n欢迎来到订餐中心。您今天想吃什么？")
```

接下来，我们将 *choice* 定义为空变量：

```python
choice = ' '
```

接下来是我们的 while look，它将通知用户选项、接受输入、根据其输入输出文本，并在用户输入 *q* 时结束。循环如下所示：

```python
while choice != ‘q’:
    print(“\n[1] 输入 1 订购泰国菜。”)
    print(“[2] 输入 2 订购印度菜。”)
    print(“[3] 输入 3 订购墨西哥菜。”)
    print(“[4] 输入 4 订购中国菜。”)
```
**订餐中心**

欢迎来到订餐中心。您今天想吃点什么？

**菜单：**

* [1] 泰国菜
* [2] 印度菜
* [3] 墨西哥菜
* [4] 中国菜
* [q] 退出

**输入您的选择：**

```
print("\n欢迎来到订餐中心。您今天想吃点什么？")
choice = ''
while choice != 'q':
    # 在一系列 print 语句中给出所有选择。
    print("\n[1] 输入 1 订购泰国菜。")
    print("[2] 输入 2 订购印度菜。")
    print("[3] 输入 3 订购墨西哥菜。")
    print("[4] 输入 4 订购中国菜。")
    print("[q] 输入 q 退出。")
    choice = input("\n您想点什么菜？ ")
    if choice == '1':
        print("\n祝您用餐愉快！\n")
    elif choice == '2':
        print("\n祝您用餐愉快！\n")
    elif choice == '3':
        print("\n祝您用餐愉快！\n")
    elif choice == '4':
        print("\n祝您用餐愉快！\n")
    elif choice == 'q':
        print("\n感谢您的惠顾。祝您生活愉快。\n")
    else:
        print("\n我不明白您的选择，请重试。\n")
print("谢谢惠顾，祝您生活愉快。")
```

**运行示例：**

```
欢迎来到订餐中心。您今天想吃点什么？

[1] 输入 1 订购泰国菜。
[2] 输入 2 订购印度菜。
[3] 输入 3 订购墨西哥菜。
[4] 输入 4 订购中国菜。
[q] 输入 q 退出。

您想点什么菜？ 2

祝您用餐愉快！
```