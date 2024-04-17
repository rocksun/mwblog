## Python “集合”是什么，如何使用？

![Python “集合”是什么，如何使用？的特色图片](https://cdn.thenewstack.io/media/2024/04/d6b02580-libby-penner-qw5xllbdeao-unsplash-1-1024x684.jpg)

### Python 集合

Python 集合是一种可迭代、可变且不可重复的数据类型。此数据类型非常方便。例如，你需要存储员工 ID 的信息。你肯定不希望这些 ID 在应用程序中重复，因为这可能会导致问题。

例如，你有以下员工 ID：

- 001
- 002
- 003
- 004
- …

你可以将特定信息附加到每个 ID，例如姓名、电子邮件、电话号码、生日等。如果 ID 重复，数据的交叉授粉可能会导致混乱或应用程序无法按预期运行。

集合可以包含任意数量的项目，甚至可以是不同类型，例如 [字符串](https://thenewstack.io/what-are-python-f-strings-and-how-do-you-use-them/)、整数、[元组](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/)、浮点数等。

集合的主要用例包括删除重复项、检查集合成员资格以及执行某些数学运算（例如并集、交集、差集和对称差集）。

### 创建集合

Python 包含内置的 `set()` 函数，可以轻松创建集合，如下所示：

```python
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
```

上面你看到的是一个集合，其中包含一个数字列表，其中一些数字重复。如果我们想确保删除那些重复的数字呢？多亏了 `set()`，该功能已内置其中。例如，我们可以使用以下行打印 `set1`：

```python
print('Set1: ', set1)
```

我们的整个代码块如下所示：

```python
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
print('Set1: ', set1)
```

如果我们运行 about，`set()` 将删除所有重复的数字，因此输出将是：

```
Set1: {2, 4, 6, 8, 10}
```

请记住，集合还可以包含混合类型，因此我们可以有一个如下所示的集合：

```python
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
```

上面的集合使用元组而不是列表。我们可以为该集合添加一个打印行，如下所示：

```python
print('Set2: ', set2)
```

我们的整个代码块现在如下所示：

```python
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
print('Set1: ', set1)
print('Set2: ', set2)
```

然后输出将是：

```
Set1: {2, 4, 6, 8, 10}
Set2: {1, 3, 'dog', 5, 'cat', 'mouse'}
```

所有重复项都已删除。

另一种封闭集合的方法是使用 `{}`，如下所示：

```python
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1)}
```

最终集合的输出将是：

```
Set3: {'cat', 2, 3.14, 'dog', 4, 6, (3, 2, 1), 'mouse'}
```

需要注意的一件事是，我们确实有一个重复的元素……2。这是怎么回事？因为 `(1, 2, 3)` 本身就是一个元素。如果我们只复制该元素，则只会打印一个实例。该集合可能如下所示：

```python
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1), (3, 2, 1)}
```

运行应用程序，`Set3` 输出将保持不变：

```
Set3: {'cat', 2, 3.14, 'dog', 4, 6, (3, 2, 1), 'mouse'}
```

因此，`(3, 2, 1)` 重复项也被删除了。

### 检查成员资格

还可以检查元素是否存在于集合中。这是通过 `in` 关键字完成的。检查结果将为 `True` 或 `False`。

例如，我们想检查 `cat` 是否在 `set3` 中，从 `print()` 语句中，可以这样做：

```python
print('cat' in set3)
```

我们可以将其添加到我们的完整代码块中，如下所示：

```python
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1), (3, 2, >
print('cat' in set3)
print('Set1: ', set1)
print('Set2: ', set2)
print('Set3: ', set3)
```

如果我们运行上述代码，输出将如下所示：

```
*True
* *Set1: {2, 4, 6, 8, 10}*
*Set2: {1, 3, 5, ‘cat’, ‘mouse’, ‘dog’}*
*Set3: {2, 3.14, 4, 6, ‘cat’, (3, 2, 1), ‘mouse’, ‘dog’}*
```

我们可以这样运行相反的检查：

```python
print('cat' not in set3)
```

我们的输出现在将如下所示：

```
*True
* *False*
*Set1: {2, 4, 6, 8, 10}*
*Set2: {1, 3, 5, ‘cat’, ‘mouse’, ‘dog’}*
*Set3: {2, 3.14, 4, 6, ‘cat’, (3, 2, 1), ‘mouse’, ‘dog’}*
```

### 创建空集合

我们还可以创建空集合，如下所示：

```python
empty_set1 = set()
```

然后我们可以对新集合的数据类型运行测试，如下所示：

```python
print('Data type of our empty set = ', type(empty_set1))
```

上述输出将是：

```
*Data type of our empty set = <class ‘set’>*
```

### 添加或更新项目

如果你需要在集合中添加或更新项目，那也是可能的。假设我们的集合是：

```python
set1 = {21, 12, 21, 42, 33}
```

让我们使用以下命令打印该集合：

```python
print('Initial Set:',set1)
```

输出将是：

```
*Initial Set: {33, 42, 12, 21}*
```
**集合**

再次，`set()` 去掉了重复的 21。

我们可以使用 `add()` 函数向集合中添加元素，如下所示：

```python
set1.add(32)
```

添加另一行打印更新后的内容，如下所示：

```python
print('更新后的集合：', set1)
```

新的输出将是：

```
初始集合：{33, 42, 12, 21}
更新后的集合：{32, 33, 42, 12, 21}
```

我们还可以对集合使用 `update()`。假设我们有两个集合：

```python
set1 = {'汤姆·索亚', '模拟小子', '车轮之间'}
set2 = {'拉维拉·斯特兰吉亚托', 'YYZ', '主要猴子业务'}
```

然后我们使用 `update()` 函数，如下所示：

```python
set1.update(set2)
```

添加一个打印语句，如下所示：

```python
print(set1)
```

此代码块的输出将是：

```
{'汤姆·索亚', '主要猴子业务', 'YYZ', '模拟小子', '车轮之间', '拉维拉·斯特兰吉亚托'}
```

最后，我们将使用 `discard()` 函数从集合中删除一个元素，如下所示：

```python
removedValue = set1.discard('车轮之间')
```

我们的代码将如下所示：

```python
set1 = {'汤姆·索亚', '模拟小子', '车轮之间'}
print('初始集合：',set1)
removedValue = set1.discard('车轮之间')
print('discard 后的集合：', set1)
```

我们的输出现在是：

```
初始集合：{'汤姆·索亚', '车轮之间', '模拟小子'}
discard 后的集合：{'汤姆·索亚', '模拟小子'}
```

这就是 Python 中集合的基础知识。当你需要删除重复项或检查各种数据类型的元素时，此功能将派上用场。要详细了解你可以使用集合做什么，请务必查看 [官方文档](https://docs.python.org/2/library/sets.html)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。