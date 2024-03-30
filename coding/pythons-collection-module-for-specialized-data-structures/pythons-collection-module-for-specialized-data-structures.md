
<!--
title: Python用于专门数据结构的集合模块
cover: https://cdn.thenewstack.io/media/2024/03/debf09cc-heather-m-edwards-tac5veacyia-unsplash-scaled.jpg
-->

有些时候，Python 的内置数据类型根本不够用。好消息是，Python 的集合模块提供了一些容器，用于高级数据整理。

> 译自 [Python's Collection Module for Specialized Data Structures](https://thenewstack.io/pythons-collection-module-for-specialized-data-structures/)，作者 Jack Wallen。

[Python 编程语言](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 包含许多内置容器数据类型，例如[列表](https://thenewstack.io/python-for-beginners-lists/)、[元组](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/) 和[字典](https://thenewstack.io/python-the-many-ways-to-merge-a-dictionary/)。可以将容器视为[包含其他对象的的对象](https://thenewstack.io/python-oop/)。例如，列表是一个对象，它可能包含诸如 orange、apple、banana、peach 等对象。字典是一个包含 *键:值* 对的对象，例如 “fruit”: “Apple”， “vegetable”: “Tomato”， “season”: “Salt”。

在大多数情况下，内置容器就足够了。但是，当你需要操作专门的数据结构时，你会希望使用 collections 模块。这些基本容器不需要导入。但是，当你需要一些更复杂的东西时，你会使用 collections 模块，它添加了以下容器：

- **Counter** **—** 字典容器的子类；用于统计可迭代元素的出现次数。
- **NamedTuple** **—** 类似于类，但不必定义一个完整的类，并使用命名字段创建元组的子类。
- **OrderedDict** **—** 字典子类，如果请求的键不存在，则返回一个默认值。
- **Deque** **—** 双端队列，支持从开头或结尾添加和删除元素。

还有其他容器（*ChainMap*、*UserDict*、*UserList* 和 *UserString*），但我们将重点关注上述四个容器。

既然你已经了解了 collections 模块提供的功能，让我们看看每个容器如何工作。

## Counter

counter 容器可以统计容器中的对象。假设你需要统计特定单词中字母的实例。我们将使用单词 subbookkeeper（因为它很有趣，并且有很多重复的字母）。

在使用 counter 之前，我们必须像这样导入 collections：

```py
import collections
```

接下来，我们将定义两个变量：

```py
word = "subbookkeeper"
counter = {}
```

使用 `counter = {}` 我们定义了一个没有值的字典，因此它将用作占位符。

好的，现在我们将创建一个 for 循环来使用 counter 遍历我们定义的变量以统计容器中的对象。

for 循环如下所示：

```py
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1
```

for 循环的作用是遍历 counter，添加每个对象的实例数。

最后，我们像这样使用 `print()` 函数：

```py
print(counter)
```

我们的整个应用程序如下所示：

```py
import collections
word = "subbookkeeper"
counter = {}
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1
print(counter)
```

运行以上代码，输出将是：

```
{'s': 1, 'u': 1, 'b': 2, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1}
```

## NamedTuple

使用 NamedTuple，我们可以创建类似于类的结构，但不必定义一个完整的类。在处理对象详细信息时，这非常方便。例如，假设你正在创建一个应用程序来添加学生详细信息，并且不想创建一个完整的类。为此，你可以使用 NamedTuple。

在使用它之前，你必须像这样从 collections 导入它：

```py
from collections import namedtuple
```

接下来，我们使用 namedtupule 容器定义 Student，然后使用 fname、name、major 和 birthday 创建一个元组，如下所示：

```py
Student = namedtuple('Student', ['fname', 'lname', 'major', 'birthday'])
```

现在，我们将定义 S 并将数据注入元组，如下所示：

```py
S = Student('Jack', 'Wallen', 'theatre', '10311967')
```

最后，我们将使用这两个行使用索引位置 0 打印名字：

```py
print("First name using the index is : ", end="")
print(S[0])
```

然后，我们使用键名打印专业，如下所示：

```py
print("Major using keyname is : ", end="")
print(S.major)
```

我们的整个应用程序如下所示：

```py
from collections import namedtuple
 
Student = namedtuple('Student', ['fname', 'lname', 'major', 'birthday'])
 
S = Student('Jack', 'Wallen', 'theatre', '10311967')
 
print("First name using the index is : ", end="")
print(S[0])
 
print("Major using keyname is : ", end="")
print(S.major)
```

## OrderedDict

OrderedDict 容器在迭代期间始终保留序列的顺序。假设你有一个键值对的字典，看起来像 letter = name，并且你始终希望保留定义它们的顺序。例如，你可能拥有：

```
a = Camille
b = Colette
c = Aaron
d = Clara
```

您可能希望在不更改 a、b、c、d 顺序的前提下更改其中一个名称。此键值更改在 OrderedDict 中固有，并按如下方式使用：

从 collections 导入 OrderedDict。

```py
print("Original:\n")
dict = OrderedDict()
dict['a'] = "Camille"
dict['b'] = "Colette"
dict['c'] = "Aaron"
dict['d'] = "Clara"
 
for key, value in dict.items():
    print(key, value)
 
print("\nChanged:\n")
dict['c'] = "Jean"
for key, value in dict.items():
    print(key, value)
```

如果您运行上面的代码，输出将为：

最初：

```
a Camille
b Colette
c Aaron
d Clara
```

变更后：

```
a Camille
b Colette
c Jean
d Clara
```

正如您所看到的，即使 c 的值发生了改变，我们仍保留了键的顺序。

## Deque

双端队列非常有用，因为它允许您在集合的开头或结尾追加一个值。

假设我们有以下代码：

```py
from collections import deque 
 
queue = deque(['name','age','major'])  
 
print(queue)
```

运行这个 app 并获得： 

deque([‘name’, ‘age’, ‘major’]) 

太棒了。

现在，假设你想要将 minor 添加到集合的右侧。可以通过以下附加操作来实现：

```py
queue.append('minor')
 
print("\nThe container after appending to the right is: ")
print(queue)
```

如果我们现在运行该应用，那么我们会得到：

```py
deque(['name', 'age', 'major'])
```

通过在此处附加代码，我们可以将年份附加到容器的开头：

```py
queue.appendleft('Senior')
 
print("\nThe container after appending to the left is: ")
print(queue)
```

现在我们的输出变为：

```py
deque(['name', 'age', 'major'])
```

在尾部追加后，容器变为： 

```py
deque(['name', 'age', 'major', 'minor'])
```

在头部追加后，容器变为：

```py

deque(['Senior', 'name', 'age', 'major', 'minor'])
```

就这样。得益于 collections 模块，我们有了四种非常酷的方式来操作集合。尽管早期您可能不需要这些操作，但最终你会发现它们对于在集合中操作数据非常宝贵。