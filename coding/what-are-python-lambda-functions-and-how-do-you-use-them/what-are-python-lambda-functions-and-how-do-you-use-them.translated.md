## Python Lambda 函数是什么以及如何使用它们？

![Python Lambda 函数是什么以及如何使用它们的特色图片](https://cdn.thenewstack.io/media/2024/03/2067792a-gabriel-alenius-ijsv5be3p3m-unsplash-1-1024x576.jpg)

虽然 [Python](https://thenewstack.io/what-is-python/) 通常是一种非常容易学习和理解的语言，但这并不意味着没有一些概念可能更具挑战性。其中一个概念就是 [Lambda 函数](https://thenewstack.io/tips-for-writing-lambda-functions-in-node-8/)。这些 [函数](https://thenewstack.io/so-much-more-python-for-beginners-functions/)（也称为 [匿名函数](https://en.wikipedia.org/wiki/Anonymous_function)）类似于你自行构建的那些函数，但没有名称。

但是这些函数有什么用呢？简单来说，当你想要编写一个只包含简单表达式的函数时，可以使用 Lambda 函数。你可能有一个需要使用的表达式，它不需要一个成熟的函数来正常执行，或者只会在你的代码/应用程序中使用一次。这时 Lambda 函数就派上用场了。

Lambda 函数仅包含三个部分：关键字（即 lambda）、一个占位符来保存要传递给表达式的值，以及表达式。

Lambda 函数的格式如下所示：

```
*lambda 参数 : 表达式*
```

在上面的示例中，

*参数* 是值占位符。

为了说明 Lambda 函数有多么方便，考虑我们想要编写一个函数，将 20 添加到变量 *a* 并打印结果。该函数可能如下所示：

```
x = lambda a : a + 20
```

让我解释一下。我们正在使用 Lambda *a* 函数定义变量 *x *，该函数将 20 添加到 a 变量。当然，我们必须定义 *a*，我们可以在 *print()* 函数中像这样进行定义：

```
print(x10))
```

整个代码如下所示：

```
x = lambda a : a + 20
print(x10))
```

如果你运行以上代码，结果将是 30。为什么？因为我们已经定义了 Lambda 函数，使其将值 20 添加到 *a*，然后我们将 *a* 定义为 10。*20+10=30*

我们还可以创建一个 Lambda 函数，其中包含两个变量（假设为 *x* 和 *y*）并将它们相乘。该 Lambda 函数将如下所示：

```
a = lambda x, y : x * y
```

我们在上面所做的是使用新的 Lambda 函数定义 *a *，然后将 *x * y* 相乘。然后，我们可以在 print 函数中像这样定义 *x* 和 *y*：

```
print(a(10, 50))
```

整个代码如下所示：

```
a = lambda x, y : x * y
print(a(10, 50))
```

运行以上代码，结果将是 500。

10 * 50 = 500

不错。

让我们更进一步。让我们在 Lambda 函数中将多个变量相加。这可能如下所示：

```
x = lambda a, b, c : a + b * c
print(x(10, 20, 30))
```

以上结果为 610。

但是我们如何在代码中有效地使用 Lambda 函数？我们为什么不使用 Lambda 函数定义一个函数，然后在代码中稍后调用该函数？为此，我们将使用 return 语句，该语句用于结束函数调用的执行并返回结果。

我们首先定义一个 Lambda 函数，将 *a* 乘以 *x*，如下所示：

```
def myfunc(x):
return lambda a : a * x
```

接下来，我们将使用以下行将 myfunc(x) 的值乘以三：

```
tripler = myfunc(3)
```

我们在上面所做的是调用 myfunc 并将 *x* 定义为 Lambda 函数的 3。

我们的下一行如下所示：

```
print(tripler(10))
```

我们在这里所做的是将 *a*（来自我们的 Lambda 函数）定义为 10，因此我们实际上有 10 乘以 3。结果（如预期）将是 30。

让我们将 Lambda 函数与标准函数进行比较（这样你就可以看到它有多有效）。考虑以下内容：

```
def a(x):
return x * 10
print(a(3))
```

如果我们运行以上代码，它将打印出 30。

但是它作为 Lambda 函数如何工作？如下所示：

```
a = lambda x : x * 10
print(a(3))
```

以上代码将打印出相同的结果，但我们只需要使用 2 行代码。

当然，如果我们想要创建一个将在代码中反复使用的函数，我们不会选择 Lambda 函数。但是对于那些只使用一次的函数，Lambda 是不二之选。为什么会这样？因为我们的 Lambda 函数没有名称，如果没有名称，它们就不能在以后被调用。

## 在列表中使用 Lambda 函数

你还可以将 Lambda 函数与列表一起使用。这是使用 *filter()* 函数完成的，该函数使用一个函数和一个参数列表，并可以轻松地从函数返回为 true 的序列中过滤出对象。假设你只想从列表中返回奇数。我们可以使用 Lambda 函数来实现：

```
x : (x % 2 !=0)
```
**它有什么作用？**

很简单。使用 `%` 运算符，它在第一个操作数除以第二个操作数时返回余数，然后 `!=` 表示不等于。如果 `x` 不是偶数，该函数将返回 `False`。

**我们的列表将是：**

```
lista = [1, 3, 6, 9, 11, 16, 21, 24, 30, 31]
```

然后，我们使用 Lambda 函数定义 `odd_out`，如下所示：

```
odd_out = list(filter(lambda x : (x % 2 != 0), lista))
```

然后，我们可以使用以下命令打印结果：

```
print(odd_out)
```

**整个代码如下所示：**

```python
lista = [1, 3, 6, 9, 11, 16, 21, 24, 30, 31]
odd_out = list(filter(lambda x : (x % 2 != 0), lista))
print(odd_out)
```

如果我们运行上述代码，我们将获得以下输出：

```
[1, 3, 9, 11, 21, 31]
```

仅打印奇数。

这就是，我的朋友们，Python 中 Lambda 函数的简介。这些小巧的东西非常方便，甚至可以使你的代码更简洁。

[**YOUTUBE.COM/THENEWSTACK**](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。