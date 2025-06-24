<!--
title: 加速Python循环：实用技巧提升代码速度
cover: https://cdn.thenewstack.io/media/2025/06/cfc9462d-steve-johnson-ctcdhpqbh8o-unsplash.jpg
summary: 本文探讨了Python循环速度慢的原因，如解释器开销和动态类型成本，并提供了优化循环的策略，包括基准测试、使用内置函数、向量化、优化循环体和采用有效的迭代模式。
-->

本文探讨了Python循环速度慢的原因，如解释器开销和动态类型成本，并提供了优化循环的策略，包括基准测试、使用内置函数、向量化、优化循环体和采用有效的迭代模式。

> 译自：[Speed Up Python Loops: Proven Techniques To Make Your Code Faster](https://thenewstack.io/speed-up-python-loops-proven-techniques-to-make-your-code-faster/)
> 
> 作者：Jack Wallen

## 引言

循环是 [Python 编程语言](https://thenewstack.io/python/) 不可或缺的一部分。循环是一种控制结构，允许重复执行代码块特定的迭代次数，直到满足条件为止。

循环具有多种优点，例如有效利用时间、简化编码、灵活性、提高生产力、减少错误和增强可读性。

您可以使用循环进行文件操作、数据分析和游戏开发。

但是，[Python 循环](https://thenewstack.io/how-to-use-loops-in-python/) 存在一个缺点：速度慢。

## 为什么 Python 循环感觉很慢

Python 循环以速度慢而闻名，原因有很多，例如解释器开销、内存分配和释放、对象创建、函数调用和递归、[全局解释器锁](https://thenewstack.io/pythons-gil-multithreading-and-multiprocessing/) 等等。

让我们来看看这些问题的一些具体细节。

### 解释器开销

当 Python 循环运行时，解释器必须执行额外的任务，例如解析代码、为每次迭代创建堆栈帧以及更新变量和数据结构。所有这些都会使循环感觉比应有的速度慢。

### 动态类型成本

与静态类型语言相比，[动态类型](https://thenewstack.io/python-under-the-hood/) 引入了额外的复杂性和开销。对于动态类型语言，解释器必须为每个操作执行运行时类型检查，这涉及到验证变量、函数参数和返回值的类型。由于额外的计算，这种类型检查可能会导致性能下降。

### 首先进行基准测试：分析你的循环

分析循环是优化其性能的重要过程。要分析一个循环，你必须识别瓶颈并了解执行时间。为此，你必须选择一个分析工具，例如 timeit、cProfile 模块或 line\_profiler 库。

### 使用 Timeit 进行微基准测试

使用 timeit 对 Python 循环进行微基准测试看起来像这样：

```py
import timeit

def add_numbers(a, b):

    return a + b

a = 10
b = 20

add_time = timeit.timeit(lambda: add_numbers(a, b), number=100000)

print(f"Addition result: {a + b}")

print(f"Execution time: {add_time:.6f} seconds")
```

在使用 timeit 编写有效的微基准测试时，请考虑以下提示：

* 通过避免依赖外部库或模块的代码来最大限度地减少外部依赖项。
* 在所有运行中使用一致的种子。
* 运行多次迭代。
* 使用合适的置信区间或 p 值分析。

### 使用 cProfile 发现热路径

热路径是指程序中最常执行的代码行，可能会影响整体性能。使用 cProfile 可以帮助识别它们，以便可以对其进行优化。要使用 cProfile，你必须：

* 安装并导入库。
* 使用 @profile() 装饰器包装你的函数或模块。
* 在运行代码之前通过调用 profiler.enable() 启用分析器，然后在运行代码之后使用 profiler.disable() 禁用分析器。

这是一个例子：

```py
import cProfile

def my_function():
    # Your code here
    pass

# Enable profiling and run the function
profiler = cProfile.Profile()
profiler.enable()
my_function()
profiler.disable()

# Print the results
profiler.print_stats(sort='cumulative')
```

## 用内置函数替换循环

用内置函数替换循环是优化性能的好方法。例如，你可以使用 map() 代替 for 循环。

这是一个 for 循环的示例：

```py
numbers = [1, 2, 3, 4, 5]

# Using a for loop
result_for_loop = []
for num in numbers:
    result_for_loop.append(num ** 2)

print(result_for_loop)  # Output: [1, 4, 9, 16, 25]

Here's the same script, using map():

import math

numbers = [1, 2, 3, 4, 5]

# Using map()
result_map = list(map(lambda x: x ** 2, numbers))

print(result_map)  # Output: [1, 4, 9, 16, 25]
```

如果你不确定何时应该使用循环与内置函数：

* 对小数据集使用循环。
* 对复杂逻辑使用循环。
* 对自定义操作使用循环。

除上述情况外，请使用内置函数。

## 拥抱向量化

向量化是指一次对整个数组或向量执行操作（而不是单独迭代每个元素）的过程。完成此操作的最佳方法是通过 [Numpy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/)。

这是一个使用 Numpy 进行向量化的示例：

```py
import numpy as np

# Create two vectors
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Perform element-wise addition using vectorization
result = x + y
print(result)  # Output: [5 7 9]
```

## 优化循环体

优化循环体涉及：

* 减少迭代次数。
* 最小化计算。
* 利用内置函数。

要优化循环体，你可以：

* 使用列表推导式。
* 避免全局变量。
* 使用迭代器。

## 有效的迭代模式

有效的迭代模式涉及为任何给定的任务使用最合适的构造，利用内置函数并最大限度地减少不必要的开销。

枚举是一个内置函数，它返回一个迭代器，该迭代器生成一个包含计数以及从迭代获得的值的元组。这是一个例子：

```py

fruits = ['apple', 'banana', 'cherry']

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
```

Zip 是另一个内置函数，它接受可迭代对象并将它们聚合到元组的单个迭代器中。这是一个例子：

```py
names = ['John', 'Alice']
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# John is 25 years old
# Alice is 30 years old
```

解包使得可以将来自迭代器的值直接分配给变量，其工作方式如下：

```py
numbers = [1, 2, 3]

for num in numbers:
    print(num)

# Output:
# 1
# 2
# 3

# Unpack the list of tuples into separate variables using unpacking
x, y, z = (10, 20, 30)
print(x)       # Output: 10
print(y)       # Output: 20
print(z)       # Output: 30
```

## 结论

有很多其他方法可以加快 Python 循环的速度，但以上内容应该为你提供一个坚实的起点。请记住，如果你不优化循环，[你的 Python 代码](https://thenewstack.io/all-basic-python-syntaxes/) 可能会变慢，并且鉴于 Python 已经以速度慢而闻名，那么再加上这种速度的不足会真正损害你的脚本。