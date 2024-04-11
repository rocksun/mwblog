
<!--
title: 如何（以及何时）使用Python While循环
cover: https://cdn.thenewstack.io/media/2024/04/32cec1d4-etienne-girardet-chp1itgplka-unsplash-1.jpg
-->

本教程将教你如何在 Python 编程中使用 while 循环以及何时使用它。

> 译自 [How (and When) to Use a Python While Loop](https://thenewstack.io/how-and-when-to-use-a-python-while-loop/)，作者 Jack Wallen。

While 循环是[编程](https://thenewstack.io/why-literate-programming-might-help-you-write-better-code/)的一个基本要素。While [循环](https://thenewstack.io/how-to-use-loops-in-python/)所做的是继续执行一条语句（或一组语句），直到满足特定条件。一个显而易见的例子（许多人都会理解）可能是这样的：*只要我的银行账户有钱，我就可以买东西。*

> 该语句是*我可以买东西*，条件是*只要我的银行账户有钱*。当您花光所有钱时，您将无法再购买东西（或支付账单）。

当您需要重复执行一条语句（或多条语句）时，While 循环是一个不错的选择。

*for* 和 *while* 循环之间的区别在于，*for* 循环只是遍历集合（或可迭代对象）并完成，而 *while* 循环则持续到满足特定条件为止。

*for* 循环更容易使用，但在某些情况下需要使用 *while* 循环。例如，您可能不知道必须重复执行该语句的次数。

我们来看一下执行相同操作的基本 Python 循环示例。首先，一个将打印范围内的数字的 for 循环。该循环可能如下所示：

```python
for i in range(11):
    print (i)
```

我们已将 for 循环设置为打印 11 范围内的 i。该代码的输出将如下所示：

```
0
1
2
3
4
5
6
7
8
9
10
```

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
     new_name = input("Type the names to be added and end with 'end: ")
 
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
    new_name = input("Type the names to be added and end with 'end': ")
 
    names.append(new_name)
 
print(names)
```

运行上述代码，它将指示用户输入姓名，并通过输入 *end* 结束运行。输出可能如下所示：

*[‘Aaron Kennedy’，‘Camile St. Joan’，‘Anton Frank’，‘Jean Barber’，‘Clara Beach’，‘end’]*

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
    new_name = input("Type the names to be added and end with 'end': ")
 
    if new_name != 'end':
        names.append(new_name)
 
print(names)
```

如果我们输入与上面相同的姓名，并通过输入 end（并按 Enter）结束，则输出现在将如下所示：

*[‘Aaron Kennedy’，‘Camile St. Joan’，‘Anton Frank’，‘Jean Barber’，‘Clara Beach’]*

已修复。

这里有另一个接受用户输入但为他们提供可供选择的菜单的示例。我们将提供不同类型的食物。首先，我们用以下语句指导用户该怎么做：

```python
print("\nWelcome to the food ordering center. What would you like to eat today?")
```

接下来，我们将 *choice* 定义为空变量：

```python
choice = ' '
```

接下来是我们的 while look，它将通知用户选项、接受输入、根据其输入输出文本，并在用户输入 *q* 时结束。循环如下所示：

```python
while choice != ‘q’:

   print(“\n[1] Enter 1 to order Thai.”)
    print(“[2] Enter 2 to order Indian.”)
    print(“[3] Enter 3 to order Mexican.”)
    print(“[4] Enter 4 to order Chinese.”)
    print(“[q] Enter q to quit.”)

    choice = input(“\nWhat kind of food would you like to order? “)
    if choice == '1':
        print("\nEnjoy your Thai food!\n")
    elif choice == '2':
        print("\nEnjoy your Indian food!!\n")
    elif choice == '3':
        print("\nEnjoy your Mexican food!\n")
    elif choice == '3':
        print("\nEnjoy your Chinese food!\n")
    elif choice == 'q':
        print("\nThanks for ordering. Have a great day.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
```

请注意，最后一条语句告知用户他们输入的内容超出了此应用程序的范围。

最后，我们通过以下方式打印一条告别消息：

```PY
print("Thank you and have a wonderful day.")
```

整个代码如下：

```PY
print("\nWelcome to the food ordering center. What would you like to eat today?")
 
choice = ''
 
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 to order Thai.")
    print("[2] Enter 2 to order Indian.")
    print("[3] Enter 3 to order Mexican.")
    print("[4] Enter 4 to order Chinese.")
    print("[q] Enter q to quit.")
 
    choice = input("\nWhat kind of food would you like to order? ")
 
    if choice == '1':
        print("\nEnjoy your Thai food!\n")
    elif choice == '2':
        print("\nEnjoy your Indian food!!\n")
    elif choice == '3':
        print("\nEnjoy your Mexican food!\n")
    elif choice == '3':
        print("\nEnjoy your Chinese food!\n")
    elif choice == 'q':
        print("\nThanks for ordering. Have a great day.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
 
print("Thank you and have a wonderful day.")
```

当你运行这个应用，它将会打印出：

```
Welcome to the food ordering center. What would you like to eat today?

[1] Enter 1 to order Thai.
[2] Enter 2 to order Indian.
[3] Enter 3 to order Mexican.
[4] Enter 4 to order Chinese.
[q] Enter q to quit.

What kind of food would you like to order? 
```

后续的输出将基于用户的输入。例如，如果用户输入 2，则输出将是：

```
Enjoy your Indian food!!
```

当用户键入 q 时，程序结束。

这是 Python while 循环的要点。这些循环是一个基本的编程方面，您将在代码中经常使用它们。