<!--
title: Python索引 vs. For循环：哪个更快？
cover: https://cdn.thenewstack.io/media/2025/07/79ae533f-maksym-kaharlytskyi-q9y3lruuxmg-unsplash-1.jpg
summary: Python 提供了 for 循环和索引循环两种迭代数据的方法。for 循环更简洁高效，适用于简单迭代；索引循环提供更多控制，适用于需要元素位置或修改元素的场景。大数据集下，for 循环性能更优。选择合适的方法可以优化代码性能。
-->

Python 提供了 for 循环和索引循环两种迭代数据的方法。for 循环更简洁高效，适用于简单迭代；索引循环提供更多控制，适用于需要元素位置或修改元素的场景。大数据集下，for 循环性能更优。选择合适的方法可以优化代码性能。

> 译自：[Python Indexing vs. For Loops: What’s Really Faster?](https://thenewstack.io/python-indexing-vs-for-loops-whats-really-faster/)
> 
> 作者：Jessica Wachtel

作为数据处理和分析大型数据集的首选语言，[Python](https://thenewstack.io/python/) 提供了多种迭代各种大小数据集的方法，这并不令人惊讶。

迭代是为集合中的每个项目重复执行一个操作的过程，一次一个。在编程中，它通常意味着逐步遍历列表、字符串或其他值组。你“访问”每个项目，通常是为了读取它、更改它或对它执行某些操作。可以将迭代想象成叠衣服。你拿出一件衣服，叠好，然后继续下一件，直到篮子空了。

在 Python 中迭代数据的两种常见方法是 [`for`](https://thenewstack.io/how-to-use-loops-in-python/) [循环](https://thenewstack.io/how-to-use-loops-in-python/) 和使用索引进行循环。 `for` 循环逐个处理序列中的每个项目。将循环与 [Python 的索引系统](https://thenewstack.io/how-to-use-the-python-slice-function/) 结合使用，可以访问每个元素的位置和值。

在许多情况下，这两种方法都可以让你获得相同的结果。但是，你可能选择一种方法而不是另一种方法的原因，以及它们在底层如何运作以及如何大规模影响应用程序性能，却大相径庭。

## 什么是 Python 循环中的索引？

使用索引进行循环是一种通过循环访问序列（例如[列表、元组或字符串](https://thenewstack.io/write-better-python-with-list-comprehensions/)）的索引，然后使用这些索引来访问每个元素的方式。此方法将 for 循环的结构与 Python 索引系统的精度相结合，该系统从 0 开始计数。

### 何时在循环中使用索引

* 你需要每个元素的位置和值。
* 你计划就地修改元素，例如通过索引更新值。
* 你处理多个序列，并且需要按位置同步它们。
* 你想要显式控制要访问哪些元素以及如何访问。

### Python 循环中的索引：基本语法

```
for i in range(len(sequence)):
    # Access each element with sequence[i]
    # Perform actions using i or sequence[i]
```

### Python 使用索引循环的示例

```py
data = [4, 7, 9, 1, 5]


for i in range(len(data)):
    print(data[i])
```

输出：

```
4

7

9

1

5
```

### 什么是 Python `for` 循环？

`for` 循环直接迭代序列的元素，为每个项目执行一个代码块，而无需显式使用它们的索引。这种方法更简单、更易读，尤其是在你不需要每个元素的位置或修改序列时。

### 何时使用 `for` 循环

* 你只需要读取或处理每个项目。
* 你不需要修改原始列表。
* 你不关心每个项目的索引。

### Python `for` 循环：基本语法

```
for element in sequence:
    # 使用 element 执行操作
```

### `for` 循环的示例

```
data = [4, 7, 9, 1, 5]


for item in data:
    print(item)
```

### 功能：索引与 `for` 循环

虽然这两个循环可以执行类似的任务，但索引提供更多原生功能。例如，要将列表中的每个数字翻倍，你可以使用循环中的索引轻松地做到这一点：

```py
data = [4, 7, 9, 1, 5]


for i in range(len(data)):
    data[i] = data[i] * 2  # 通过索引修改列表元素


print(data)
```

输出：

```
[8, 14, 18, 2, 10]
```

尝试使用 `for` 循环执行相同的操作会产生不同的结果。

```
data = [4, 7, 9, 1, 5]


for item in data:
    item = item * 2  # 仅更改循环变量，而不是列表元素


print(data)
```

输出：

```
[4, 7, 9, 1, 5]`
```

为什么结果会有所不同？当使用语法 `for item in data` 时，`item` 是每个元素值的临时副本，而索引指向的是实际值本身。更改循环内的 `item` 不会影响原始列表。但是，循环中的索引通过其索引访问实际元素，因此赋值给 `data[i]` 会直接修改原始列表。

### 速度和性能：Python 中索引与 `for` 循环

功能并不是索引和 `for` 循环之间唯一的区别。它们的性能特征也不同。两者都允许你迭代数据，但它们在内部访问元素的方式会影响速度（和内存）。

## 基准测试方法

让我们使用 Python 的 `time` 模块和一个测量函数运行时间的函数来进行测试。

```
import time


def time_function(func):
    start = time.time()
    func()
    return time.time() - start
```

### 示例 1：小数据集比较

```
data = list(range(1000))


def with_indexing():
    for i in range(len(data)):
        _ = data[i] * 2


def with_for_loop():
    for item in data:
        _ = item * 2


print("Indexing:", time_function(with_indexing))
print("For loop:", time_function(with_for_loop))
```

输出：

Indexing: 0.00013685226440429688

`for` loop: 7.009506225585938e-05

在此示例中，`for` 循环和索引似乎都在执行相同的功能，那么为什么一个更快呢？因为尽管它们看起来相似，但在底层，它们的执行方式却不同。

* `with_indexing()` 循环访问一系列索引，并通过索引 (`data[i]`) 访问每个元素。
* `with_for_loop()` 直接循环访问列表中的每个项目，而无需计算索引。

`for` 循环跳过了生成索引号和执行索引查找的开销。这减少了少量的计算，这在多次迭代中很重要。

### 示例 2：大数据集比较

```
data = list(range(10_000_000))


def with_indexing_large():
    for i in range(len(data)):
        _ = data[i] * 2


def with_for_loop_large():
    for item in data:
        _ = item * 2


print("Indexing (large):", time_function(with_indexing_large))
print("For loop (large):", time_function(with_for_loop_large))
```

输出：

Indexing (large): 0.8469340801239014

`for` loop (large): 0.405224084854126

同样，`for` 循环的性能优于索引。在每次迭代中计算索引和执行查找的成本会累加。`for` 循环通过使用内部迭代器来避免这种情况，该迭代器：

* 不计算索引位置。
* 不使用括号表示法重复查找值。
* 具有较低的 CPU 和内存开销。

### 为什么 `for` 循环更快？

索引显式引用位置 (`data[i]`)。虽然列表索引是恒定时间操作 (O(1))，但每次迭代都涉及计算索引和执行查找，从而增加开销。

`for` 循环使用 Python 的内部迭代器协议直接获取元素，而无需计算索引。这种简化的过程减少了开销，从而使 `for` 循环更快，尤其是在大型数据集上。

在实践中，对于简单迭代，`for` 循环更有效，而索引提供更多控制，但会产生略微的性能成本。

## 影响速度的因素：索引与 `for` 循环

有几个因素会影响索引和 `for` 循环之间的速度差异。

* Python 实现：不同的解释器（如 [CPython](https://thenewstack.io/python-under-the-hood/) 和 [PyPy](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/)）处理循环的方式不同。PyPy 的 JIT 编译器可以比 CPython 更好地优化索引，从而影响结果。
* 数据类型：列表和元组与这两种方法配合良好。但是，对于 [Numpy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) 数组，矢量化操作通常优于循环，无论样式如何。
* 数据集大小：索引开销随着数据集的增大而增加，从而使 `for` 循环通常更快。对于小型数据集，差异很小。
* 操作复杂性：简单的任务会突出显示迭代开销。复杂的操作或 I/O 可能会掩盖差异。

## 常见错误和误解

* 在不需要时使用索引：这会增加代码复杂性，并可能由于索引管理开销而降低性能。如果不需要元素位置，请使用简单的 `for` 循环。
* 假设索引总是更快：正如我们所看到的，事实并非如此。`for` 循环通常通过避免重复的索引计算来获得更好的性能，并且通常更易读。
* 在迭代期间修改列表：在迭代时更改列表可能会导致错误，例如跳过元素或出错。使用副本、小心索引或构建新列表以避免问题。

## 发现结果摘要

`for` 循环通常更有效，并且对于只需要处理每个项目的简单迭代更易读。它们的清晰度减少了错误并提高了可维护性。

当需要元素位置或必须就地修改项目时，使用循环进行索引非常有用。这种控制会以一定的可读性为代价，有时还会以性能为代价。

随着数据集变得越来越大，这些方法之间的性能差异变得显着。选择正确的方法会影响速度和资源使用。

## Python 开发人员的后续步骤

为了在你的项目中做出明智的性能决策，请使用 `cProfile` 或 `timeit` 等分析工具来衡量你的代码在实际场景中的行为方式。这可以帮助你识别特定的瓶颈，而不是依赖于一般的假设。探索 NumPy 或 Pandas 等库，这些库为数据处理提供了优化的矢量化替代方案，以替代手动循环。

在编写 Python 代码时，尽可能倾向于使用更易读和 Pythonic 的方法，即使用 `for item in iterable` 进行直接迭代。这种做法可以减少错误、提高清晰度，并且通常可以提高性能。通过了解不同循环技术之间的权衡并应用最佳实践，你将能够更好地构建高效、可维护的 Python 应用程序。