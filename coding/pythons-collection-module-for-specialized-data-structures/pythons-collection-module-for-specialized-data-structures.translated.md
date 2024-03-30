# Python 的集合模块用于专门的数据结构

![Python 的集合模块用于专门的数据结构的特色图片](https://cdn.thenewstack.io/media/2024/03/debf09cc-heather-m-edwards-tac5veacyia-unsplash-1024x747.jpg)

[Python 编程语言](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 包含许多内置容器数据类型，例如 [列表](https://thenewstack.io/python-for-beginners-lists/)、[元组](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/) 和 [字典](https://thenewstack.io/python-the-many-ways-to-merge-a-dictionary/)。可以将容器视为 [包含其他对象的的对象](https://thenewstack.io/python-oop/)。例如，列表是一个对象，它可能包含诸如 orange、apple、banana、peach 等对象。字典是一个包含 *键:值* 对的对象，例如 “fruit”: “Apple”， “vegetable”: “Tomato”， “season”: “Salt”。

在大多数情况下，内置容器就足够了。但是，当你需要操作专门的数据结构时，你会希望使用 collections 模块。这些基本容器不需要导入。但是，当你需要一些更复杂的东西时，你会使用 collections 模块，它添加了以下容器：

**Counter** **—**字典容器的子类；用于统计可迭代元素的出现次数。
**NamedTuple** **—**类似于类，但不必定义一个完整的类，并使用命名字段创建元组的子类。
**OrderedDict** **—**字典子类，如果请求的键不存在，则返回一个默认值。
**Deque** **—**双端队列，支持从开头或结尾添加和删除元素。

还有其他容器（*ChainMap*、*UserDict*、*UserList* 和 *UserString*），但我们将重点关注上述四个容器。

既然你已经了解了 collections 模块提供的功能，让我们看看每个容器如何工作。

## Counter

counter 容器可以统计容器中的对象。假设你需要统计特定单词中字母的实例。我们将使用单词 subbookkeeper（因为它很有趣，并且有很多重复的字母）。

在使用 counter 之前，我们必须像这样导入 collections：

```
import collections
```

接下来，我们将定义两个变量：

```
word = subbookkeeper
counter = {}
```

使用 counter
*= {}* 我们定义了一个没有值的字典，因此它将用作占位符。

好的，现在我们将创建一个 for 循环来使用 counter 遍历我们定义的变量以统计容器中的对象。

for 循环如下所示：

```
for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1
```

for 循环的作用是遍历 counter，添加每个对象的实例数。

最后，我们像这样使用
* print()* 函数：

```
print(counter)
```

我们的整个应用程序如下所示：

```
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

```
from collections import namedtuple
```

接下来，我们使用 namedtupule 容器定义 Student，然后使用 fname、name、major 和 birthday 创建一个元组，如下所示：

```
Student = namedtuple('Student', ['fname', 'lname', 'major', 'birthday'])
```

现在，我们将定义 S 并将数据注入元组，如下所示：

```
S = Student('Jack', 'Wallen', 'theatre', '10311967')
```

最后，我们将使用这两个行使用索引位置 0 打印名字：

```
print("First name using the index is : ", end="")
print(S[0])
```

然后，我们使用键名打印专业，如下所示：

```
print("Major using keyname is : ", end="")
print(S.major)
```

我们的整个应用程序如下所示：

```
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
letter = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
```

使用 OrderedDict，你可以确保字典中的顺序保持不变，如下所示：

```
from collections import OrderedDict
letter = OrderedDict([('a', 'apple'), ('b', 'banana'), ('c', 'cherry')])
```

现在，如果你迭代字典，它将按插入顺序打印键值对：

```
for key, value in letter.items():
    print(key, value)
```

输出将是：

```
a apple
b banana
c cherry
```
**有序字典**

有序字典非常有用，因为它允许您更改键值对的顺序。例如：

```python
from collections import OrderedDict

# 创建一个有序字典
dict = OrderedDict()
dict['a'] = "卡米尔"
dict['b'] = "科莱特"
dict['c'] = "亚伦"
dict['d'] = "克拉拉"

# 打印原始字典
print("原始：\n")
for key, value in dict.items():
    print(key, value)

# 更改一个键值对
dict['c'] = "让"

# 打印已更改的字典
print("\n已更改：\n")
for key, value in dict.items():
    print(key, value)
```

输出：

```
原始：

a 卡米尔
b 科莱特
c 亚伦
d 克拉拉

已更改：

a 卡米尔
b 科莱特
c 让
d 克拉拉
```

如您所见，即使更改了键值对，我们仍保留了键的顺序。

**双端队列**

双端队列非常有用，因为它允许您在集合的开头或结尾追加一个值。例如：

```python
from collections import deque

# 创建一个双端队列
queue = deque(['姓名', '年龄', '专业'])

# 打印双端队列
print(queue)

# 在右侧追加一个值
queue.append('未成年人')

# 打印已追加的双端队列
print("\n在右侧追加后的容器是：")
print(queue)

# 在左侧追加一个值
queue.appendleft('高级')

# 打印已追加的双端队列
print("\n在左侧追加后的容器是：")
print(queue)
```

输出：

```
双端队列(['姓名', '年龄', '专业'])

在右侧追加后的容器是：
双端队列(['姓名', '年龄', '专业', '未成年人'])

在左侧追加后的容器是：
双端队列(['高级', '姓名', '年龄', '专业', '未成年人'])
```

集合模块提供了四种非常酷的方法来操作集合。虽然您可能不会在早期使用它们，但最终您会发现它们对于操作集合中的数据非常宝贵。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、采访、演示等。