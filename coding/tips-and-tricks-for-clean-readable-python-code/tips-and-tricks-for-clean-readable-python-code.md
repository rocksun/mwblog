
<!--
title: 编写整洁、可读 Python 代码的技巧和窍门
cover: https://cdn.thenewstack.io/media/2024/11/1f937e51-pablo-merchan-montes-ckosbupolsq-unsplash.jpg
-->

从装饰器到列表解析，这些内置 Python 特性帮助开发者将笨拙的代码转换成简洁、可读的解决方案，而无需重新发明轮子。

> 译自 [Tips and Tricks for Clean, Readable Python Code](https://thenewstack.io/tips-and-tricks-for-clean-readable-python-code/)，作者 Jessica Wachtel。

学习编程是一个陡峭的攀登。学习的一方面涵盖如何编程，而另一方面包括如何优雅地编程。对我来说，这是最难的部分。我可以蛮力解决许多问题，但当涉及到编写一个优雅的解决方案时，不，谢谢，我每次都会选择 [嵌套循环](https://thenewstack.io/how-to-use-loops-in-python/)。但当然，由于代码应该是 DRY（不要重复自己）、内存友好且可供其他人阅读，因此这出于一些原因不起作用。但 [Python](https://thenewstack.io/python/) 的内置帮助器有助于提高代码的可读性和易用性。

## *args 和 **kwargs

*args 和 **kwargs 有助于使函数广泛可用。将 *args 用作函数参数允许函数获取任意数量的参数。如果没有 *args，则必须考虑整数和字符串参数。

使用 *args：

```python

def add(*args):
    results = []
    for n in args:
        results.append(n)

    return results

print(add())
print(add(1,"dog"))
print(add(1,"strawberry",3))


# []
# [1, 'dog']
# [1, 'strawberry', 3]
```

如果没有它，就会抛出一个错误...

**kwargs 具有与 *args 相似的功能，但对键值对执行此操作。**kwargs 可用于没有必需数量或未知数量的函数中[键值对](https://thenewstack.io/akamai-brings-key-value-data-to-the-edge-adds-api-acceleration/)。

```python
def dictionary_builder(**kwargs):
    for x,y in kwargs.items():
        print(f'key: {x}, value: {y}')

dictionary_builder(topic = 'Python')
dictionary_builder(city = 'Brooklyn', state = 'New York')
dictionary_builder(month = 'March', day = 1, year = 2024)

# key: topic, value: Python
# key: city, value: Brooklyn
# key: state, value: New York
# key: month, value: March
# key: day, value: 1
# key: year, value: 2024
```

## 列表解析

列表解析允许开发人员仅使用一行创建列表。在不使用列表解析的情况下，可以使用以下代码构建数字列表：

```python
numbers = []

for i in range (1, 5):
    numbers.append(i)
```

列表解析将该代码转换为一行。基本语法是：

```python
numbers= [i for i in range(5)]
```

在简单代码中，它看起来像这样：

```python
even_numbers = [i for i in range(1,5) if i % 2 == 0]
print(even_numbers) # [2, 4]
```

列表解析还可以包括过滤功能。

```python
numbers = [i for i in range(1, 11) if i % 2 == 0]
```

列表不是您能以这种方式创建的唯一数据结构。我们可以使用相同的创建模式创建字典并设置它。字典的基本语法是：

```python
{key_expression: value_expression for item in 可迭代对象}
```

我们可以将数字列表中的每个数字乘以 10，得到一个 by_tens 字典。

```python
by_tens = {i: i * 10 for i in range(1, 11)}
```

我们也可以用集合来做到这一点。基本语法是

```python
{expression for item in 可迭代对象}
```

代码如下所示：

```python
my_set = {i for i in range(1, 11)}
```

## zip()

zip() 允许您同时迭代多个列表并创建相应元素的元组。

```python
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1, my_list2):
    print(item)
```

zip() 将可能的多行迭代缩短为一行代码。

```python
my_list = [(1, 'a'), (2, 'b'), (3, 'c')]
```

zip() 迭代到最小列表的长度。如果给定的列表长度不同，则元组将仅与最小列表一样长。以下代码清楚地说明了以上两点：

```python
my_list1 = [1, 2, 3, 4, 5]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1, my_list2):
    print(item)
```

## 合并字典

您可以使用
update() 功能或字典解包语法 (
**) 合并字典。

```python
land_pets = {'dog', 'cat', 'hamster'}
water_pets = {'fish', 'turtle', 'frog'}

# 使用 update() 函数
land_pets.update(water_pets)

# 使用字典解包语法
new_dict = {**land_pets, **water_pets}
```

或者您可以使用 update 函数将
water_pets 对象添加到
land_pets 对象：

```python
land_pets.update(water_pets)
```

## 链式比较运算符

链式比较运算符允许您将多个比较组合到一个表达式中。链式消除了对显式 and` 运算符的需求。它有助于提高代码的可读性和性能，因为它减少了单独比较的数量。

下面的示例比较变量
miles 以确定距离是否在范围内。没有链式比较运算符，代码如下所示：

```python
if miles >= 0 and miles <= 100:
    print("距离在范围内")
```

当比较表示为复合条件时，它看起来像这样：

```python
if 0 <= miles <= 100:
    print("距离在范围内")
```

## 三元运算符

三元运算符允许开发人员在一行中编写 if 条件。基本语法是：

```python
result = true_value if condition else false_value
```

如果条件评估为
True，则表达式返回真值。如果条件评估为
False，则表达式返回假值。这里有一个没有转弯运算符的示例：

```python
if x > 0:
    result = "x 是正数"
else:
    result = "x 不是正数"
```

与带有三元运算符的 if 条件相比：

```python
result = "x 是正数" if x > 0 else "x 不是正数"
```

## 装饰器

装饰器在不更改源代码的情况下修改函数。装饰器是一个新函数，它将原始函数作为参数，使用新函数对其进行修改，然后返回具有更新功能的函数。

让我们从一个基本的除法函数开始。

```python
def division(a, b):
    return a / b
```

division(10,5) 打印 2
division(9, 3) 打印 3

出于此示例的目的，让我们假设此函数始终需要将较大的数字除以较小的数字。有许多原因导致编辑源代码是不理想的，在这些情况下，装饰器派上了用场。如果您熟悉闭包，这看起来会很熟悉。对于不熟悉的人来说，装饰器是一个构建、修改和返回函数的函数。装饰器的外壳将如下所示：

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # 在这里执行一些操作
        return func(*args, **kwargs)
    return wrapper
```

在内部函数中，我们将检查参数是否按正确顺序排列，如果不是，则进行必要的交换（另一个 Python 技巧）。

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0] < args[1]:
            args = args[1], args[0]
        return func(*args, **kwargs)
    return wrapper
```

内部函数的外观和行为与任何基本函数一样。
现在有几种不同的方法可以使用装饰器函数来修改除法函数。第一种方法是使用 `@decorator`，如下所示：

```python
@decorator
def divide(a, b):
    return a / b
```

另一种方法是将函数分配给一个变量：

```python
divide = decorator(divide)
```

## 愉快地编码！

这些技巧肯定会将代码从基础提升到优雅。您使用 Python 的次数越多，它就越容易。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。