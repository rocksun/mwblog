<!--
title: 提升你的Python技能：高阶函数详解
cover: https://cdn.thenewstack.io/media/2025/03/2ee18a0d-ruliff-andrean-6o2_eo628cq-unsplash-1.jpg
summary: Python进阶必看！掌握map(), filter(), reduce()等高阶函数，告别循环地狱！轻松实现数据处理和转换，代码更简洁高效。函数式编程范式加持，模块化设计提升代码可读性！云原生时代，玩转Python，你就是DevOps大神！
-->

Python进阶必看！掌握`map()`, `filter()`, `reduce()`等高阶函数，告别循环地狱！轻松实现数据处理和转换，代码更简洁高效。函数式编程范式加持，模块化设计提升代码可读性！云原生时代，玩转Python，你就是DevOps大神！

> 译自：[Level Up Your Python: Higher-Order Functions Explained](https://thenewstack.io/level-up-your-python-higher-order-functions-explained/)
> 
> 作者：Jessica Wachtel

在 [Python](https://thenewstack.io/python/)，以及像 [JavaScript](https://thenewstack.io/javascript/) 和 [Ruby](https://thenewstack.io/return-to-the-rails-way-installing-ruby-on-rails-in-2024/) 这样的语言中，高阶函数如 `map()`, `filter()` 和 `reduce()` 被用于处理和转换数据。它们可以在不需要显式循环的情况下对数据进行灵活的操作。高阶函数对其他函数进行操作——或者将函数作为参数，或者在某些情况下，返回函数作为结果。最终的结果是清晰、简洁、可读和模块化的代码。

虽然高阶函数通常与 [函数式编程](https://thenewstack.io/introduction-to-gleam-a-new-functional-programming-language/) 范式相关联，但采用函数式编程风格并不是使用 `map()`, `filter()` 或 `reduce()` 的必要条件。这些函数可以被整合到任何应用程序结构中。`map()`, `filter()` 和 `reduce()` 不是唯一的高阶函数。任何函数，如果它接受一个函数作为参数或返回一个函数作为结果，都可以是一个高阶函数。

在这篇文章中，我们将探讨 `map()`, `filter()` 和 `reduce()` 函数，它们的基本语法，并提供一些简单的实现。

## map()

当你需要对一个可迭代对象（如列表或元组）中的每个项目应用一个特定的操作或转换，并返回一个新的可迭代对象（通常是一个 map 对象）作为结果时，可以使用 `map()` 函数。

基本语法：

```py
map(function, iterable)
```

`map()` 在执行诸如将数据从一种形式转换为另一种形式的任务时特别有用，例如将字符串转换为整数或更改日期格式。

```py
#original list
string_numbers = ["1", "2", "3", "4"]

#implementation of map()
int_numbers = map(int, string_numbers)

#transformed data
print(list(int_numbers))
```

输出：

```
[1, 2, 3, 4]
```

当你需要一个对单个元素进行操作的函数时，`map()` 也非常有用。你可以在 `map()` 中构建该功能，通过将其应用于可迭代对象的每个元素，从而消除对显式循环的需求。

```py
#main action
def add_five(x):
    return x + 5

#original list
numbers = [1, 2, 3]

#map() implementation
result = map(add_five, numbers)

#results
print(list(result))
```

输出：

```
[6, 7, 8]
```

## filter()

`filter()` 基于函数中指定的条件过滤掉可迭代对象中的元素。它返回一个 filter 对象，可以将其转换为列表。

基本语法：

```py
filter(function, iterable)
```

`filter()` 对于执行诸如从列表中删除不需要的元素之类的任务很有帮助。下面的示例从数字列表中删除 None：

```py
#original list
data = [0, None, 1, 2, None, 3]

#implementatio of filter
filtered_data = filter(None, data)

#results
print(list(filtered_data))
```

输出：

```
[1, 2, 3]
```

你还可以根据条件过滤列表，例如提取偶数：

```py
#condition
def is_even(x):
    return x % 2 == 0

# original list
numbers = [1, 2, 3, 4, 5, 6]

# implementation of filter
even_numbers = filter(is_even, numbers)

#results
print(list(even_numbers))
```

输出：

```
[2, 4, 6]
```

## reduce()

`reduce()` 可以说是最难掌握的高阶函数。虽然有一些更简单的实现，但更复杂的实现可能会变得非常具有挑战性。为了本文的目的，我们将专注于更简单的实现。

基本语法：

```py
#import statement
from functools import reduce

reduce(function, iterable)
```

你将看到的 `reduce()` 最常见的例子是求一个数字列表的和。

```py
# addition function
def add(x, y):
    return x + y

#original list
numbers = [1, 2, 3, 4, 5]

#implementation of reduce
result = reduce(add, numbers)

#results
print(result) 
```

输出：

```
[15]
```

`reduce()` 在查找列表中的最大值时也很有用：

```py

# condition
def max_value(x, y):
    return x if x > y else y

#original list
numbers = [10, 2, 33, 4, 7]

#implementation of reduce
result = reduce(max_value, numbers)

#results
print(result)
```

输出：

```
[33]
```

## 最后的思考

像 `map()`, `filter()` 和 `reduce()` 这样的高阶函数提供了强大的方法，可以用干净、简洁和可读的代码来处理和转换数据。这些函数可以帮助你抽象通用操作，减少对显式循环的需求，并提高代码的模块化程度。