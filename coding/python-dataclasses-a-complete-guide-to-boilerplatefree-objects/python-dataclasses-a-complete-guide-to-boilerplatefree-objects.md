<!--
title: Python 数据类：告别样板代码，轻松构建高效对象
cover: https://cdn.thenewstack.io/media/2025/09/f275b82a-henry-lai-qu14c53dmtg-unsplash-1.jpg
summary: Python数据类是精简的类，用于结构化存储相关数据。它们自动生成常用方法，支持类型提示，减少样板代码，比字典和常规类更具优势，提升代码可读性与可维护性。
-->

Python数据类是精简的类，用于结构化存储相关数据。它们自动生成常用方法，支持类型提示，减少样板代码，比字典和常规类更具优势，提升代码可读性与可维护性。

> 译自：[Python Dataclasses: A Complete Guide to Boilerplate‑Free Objects](https://thenewstack.io/python-dataclasses-a-complete-guide-to-boilerplatefree-objects/)
> 
> 作者：Jessica Wachtel

一个 [数据类](https://thenewstack.io/python-for-beginners-data-types/) 在 [Python](https://thenewstack.io/what-is-python/) 中是一种以结构化、可重用的方式存储和组织相关值的方法。但我们不是已经有字典、变量和类来在 Python 中做到这一点了吗？为什么我们需要数据类？

## 简介

区别如下：

*   一个变量保存一个单一的值（person = “Jessica”）。
*   一个字典以键值对的形式保存多个相关值（`person = {"name": "Jessica", "age": 30, "email": "jessica@example.com"}`），适用于临时或一次性数据。
*   一个类定义了对象的蓝图，这些对象可以保存多个值并执行不同的行为。
*   数据类是一种精简的类，旨在以最少的 [样板代码](https://thenewstack.io/python-vibe-coding-tools/) 保存相关值（例如字典中的人物示例）。不要与字典混淆，数据类就像常规类一样。它们是 [Python 对象](https://thenewstack.io/python-oop/) 的蓝图。

乍一看，数据类可能很像字典。一个实用的经验法则：将字典用于单个对象或结构动态变化的情况。当你想要创建多个具有相同字段的结构化对象时，使用数据类。

数据类和字典都存储键值对。数据类是一种带有类型注解的对象，支持点语法访问、内置方法如 `__init__` 和 `__repr__`，以及实例之间的轻松比较。

数据类也可能看起来与 Python 类相似。当你想要存储相关数据而不是实现复杂行为时，优先使用数据类而不是常规 Python 类。

### 为什么使用数据类

在 Python 3.7 版本引入数据类之前，开发者仍然需要创建带有相关数据的对象。为此最常见的选择是常规类、字典和命名元组（namedtuples）。但这三者都有各自的缺点。类需要大量不必要、重复的样板代码。字典无法自动生成且没有类型提示。命名元组默认是不可变的，灵活性有限，并且添加默认值和方法是劳动密集型的。

因此，Python 开发者创建了解决方案：数据类。

开发者可以使用数据类编写更具声明性、更易维护的代码。它们通过自动生成常用方法来减少样板代码。它们强制执行类型提示。你还可以用最少的语法添加更高级的功能（[不可变性](https://thenewstack.io/the-immutability-of-time-series-data/)、排序和高效内存使用）。

### 快速入门：声明你的第一个数据类

`@dataclass` 装饰器将一个类标记为数据类，表明它将用于存储结构化数据。

```
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(3, 5)




print(p.x) 
print(p.y)  
print(p)    
```

输出：

3

5

Point(x=3, y=5)

### 自动 `__init__`、`__repr__` 和 `__eq__`

数据类内置了这些方法（这就是为什么你没有看到为它们添加任何代码）。

*   `__init__` 在你创建对象时设置其字段。
*   `__repr__` 提供对象的易读字符串表示。
*   `__eq__` 允许你按值比较两个对象。

## 定义字段和类型

在数据类中，你通过在类内部列出每个带有类型注解的属性来定义字段及其类型，例如 `x: int` 或 `name: str`。

### 必填字段与可选字段

默认情况下，数据类要求所有字段都必须提供。你可以添加一个值或一个默认值。默认值是一个预设值，如果你在创建实例时没有提供，字段将使用该值。默认值可以在创建实例时被覆盖。

```
from dataclasses import dataclass


@dataclass
class Person:
    name: str  # required value
    age: int = 30  # default value


# instance using the default age
person1 = Person(name="Jess")
 
# instance overriding the default age
person2 = Person(name="Dani", age=25)
print(person1) 
print(person2) 
```

输出：

Person(name=’Jess’, age=30)

Person(name=’Dani’, age=25)

你还可以将字段设为可选：

```
from typing import Optional


@dataclass
class User:
    name: str
    age: Optional[int] = None
```

### 类型提示和静态分析

数据类依赖于类型提示。类型提示是指定 Python 中变量、函数参数或返回值预期数据类型的注解。它们在代码中看起来像 `name: str` 或 `age: int`。类型提示通过 [静态分析](https://thenewstack.io/how-static-analysis-can-save-your-software/) 帮助及早发现错误。 [静态分析](https://thenewstack.io/how-static-analysis-can-save-your-software/) 使用像 `mypy` 和 [IDE](https://thenewstack.io/best-open-source-ides/) 这样的工具来警告你，如果你尝试分配错误类型的值。这提高了代码的安全性和可读性。

### 默认值和 `default_factory`

在 Python 中，使用可变对象（如列表或字典）作为默认值可能会导致意外行为，因为所有实例都共享同一个对象。这被称为可变默认值陷阱。为了防止这种情况，数据类提供了 `default_factory`，它为每个实例创建一个新对象：

```
from dataclasses import dataclass, field


@dataclass
class Team:
    members: list = field(default_factory=list)  # each instance gets its own list


team1 = Team()
team2 = Team()


# add member to the first team
team1.members.append("Leslie")


# print members of each team
print("team1 members:", team1.members)  # Output: ['Alice']
print("team2 members:", team2.members)  # Output: [] — separate list


# show different objects
print("team1 list id:", id(team1.members))
print("team2 list id:", id(team2.members))
```

输出：

team1 members: [‘Leslie’]

team2 members: []

team1 list id: 4425609792

team2 list id: 4419089664

## 控制生成的方法

我们知道数据类会自动创建 `__init__`、`__repr__` 和 `__eq__` 方法。你还可以自定义你的类，并控制哪些方法被生成以及它们的行为方式。

### 使用 `order=True` 进行比较

`@dataclass(order=True)` 根据字段顺序生成比较方法，例如 `<`、`<=`、`>` 和 `>=`。这允许你轻松比较和排序实例。这对于对象列表或优先级排序非常有用。

```
from dataclasses import dataclass


@dataclass(order=True)
class Item:
    price: float
    name: str


item1 = Item(10.99, "Notebook")
item2 = Item(5.49, "Pen")
item3 = Item(7.25, "Pencil")


# compare instances
print(item1 > item2)  
print(item2 < item3)   


# sort a list of items
items = [item1, item2, item3]
items.sort()
print(items)
```

输出：

True

True

[Item(price=5.49, name=’Pen’), Item(price=7.25, name=’Pencil’), Item(price=10.99, name=’Notebook’)]

### 可哈希性和 `frozen=True`

`frozen=True` 使数据类实例不可变，这意味着它们的字段在创建后无法更改。它还使它们可哈希，因此它们可以用作字典键或存储在集合中。这对于创建依赖稳定值的安全、常量对象很重要。

```
from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    code: str
    symbol: str


usd = Currency("USD", "$")
eur = Currency("EUR", "€")


# attempting to modify a field will raise an error
try:
    usd.symbol = "US$"  
except AttributeError as e:
    print(e) 


# they can be used as dictionary keys
currency_rates = {
    usd: 1.0,
    eur: 0.92
}


print(currency_rates[usd])
print(currency_rates[eur]) 
```

输出：

cannot assign to field ‘symbol’

1.0

0.92

### 自定义 `__post_init__`

`__post_init__` 方法在数据类初始化后运行，允许你强制执行约束、验证值或执行额外的设置。它确保数据完整性，而无需手动编写初始化器。

```
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price must be non-negative")


product1 = Product("Laptop", 1200.00)
print(product1)  


# attempt to create a product with a negative price
try:
    product2 = Product("Headphones", -50.00)
except ValueError as e:
    print(e)  
```

输出：

Product(name=’Laptop’, price=1200.0)

Price must be non-negative

### 高级功能

数据类提供了几个更高级的功能，以提高内存效率、代码清晰度以及与现代 Python 特性的集成。

### 插槽（Slots）支持以提高内存效率

在 Python 3.10+ 中，你可以使用 `slots=True` 来告诉数据类预定义其属性，这会减少内存使用并加快属性访问速度。

### 仅限关键字字段 (`kw_only=True`)

使用 `kw_only=True` 强制所有字段都必须作为关键字参数传递，从而提高清晰度并防止因传递顺序错误而导致的错误。

### 数据类与模式匹配

你可以根据对象的字段进行匹配（在 3.10 版本发布），因为数据类与结构化模式匹配无缝集成。

## 继承和混合（Mixins）

继承和混合（mixins）都允许类重用或扩展其他类的行为和功能，使代码更具模块化且更易于维护。

### 扩展数据类（继承）

如果你以前使用过类，这个会很熟悉。数据类可以像父类和子类一样，从其他类继承字段和行为。在下面的示例中，子类 `DiscountedProduct` 自动从 `Product` 继承了 `name` 和 `price`，因此你只需要定义新增的内容（在本例中是 `discount`）。

```
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


@dataclass
class DiscountedProduct(Product):
    discount: float


dp = DiscountedProduct("Laptop", 1200.0, 150.0)
print(dp)
```

输出：

DiscountedProduct(name=’Laptop’, price=1200.0, discount=150.0)

### 混合常规和数据类基类

你可以将数据类与常规类结合起来，以“混合”额外的行为和方法。这种方法让你能够将数据类的便利性与附加功能结合起来。如果你确实决定混合使用，你需要了解你的方法解析顺序（MRO）。MRO 决定了当多个基类定义相同方法时使用哪个方法。

```
class Logger:
    def log(self, message):
        print(f"LOG: {message}")


@dataclass
class Event(Logger):
    name: str
    time: str


e = Event("Meeting", "10:00")
e.log(f"{e.name} at {e.time}") 
```

输出：

LOG: Meeting at 10:00

## 性能和内存考量

数据类很方便，但每个实例会使用更多的内存，因为每个对象都将其属性存储在一个动态的 `__dict__` 中。`__dict__` 是一个 Python 字典，它将属性名映射到它们的值。`__dict__` 允许动态属性赋值和修改（在运行时添加、更改或删除属性）。这种灵活性很方便，但需要额外的内存来存储字典结构。开销来自于 Python 需要为每个实例的属性维护一个动态映射。这使得数据类比元组或插槽（slots）等固定存储使用更多的内存。

对于需要成千上万甚至数百万个数据类对象的应用程序，有一种更轻量级的解决方案。在这些情况下，你可以使用 `slots=True` 来预定义字段。这消除了 `__dict__`，减少了内存使用，同时加快了属性访问速度。

为什么不将 `slots=True` 用于所有应用程序？`slots=True` 并不是一个万能的改进；它专门用于内存受限的应用程序。当只处理少量对象时，内存和速度的改进将微不足道。你不能动态添加新属性；所有字段都必须预定义，这可能会带来限制。它还会使类继承复杂化，特别是当你混合使用带插槽和不带插槽的类时。

## 常见陷阱和局限性

### 可变默认值

数据类在所有实例之间共享默认值。这意味着使用可变对象作为默认值可能会导致意外行为。为避免意外行为，请使用 `default_factory` 为每个实例创建一个新对象。`default_factory` 确保每个实例都有自己独立的对象。

### 递归类型

递归数据类可行，但它们使类型提示和静态分析变得棘手且容易出错。在递归中，数据类可能具有引用自身类型的字段，例如链表和树。Python 类型提示在运行时不会自动解析递归类型。这使得在这种情况下进行静态分析变得具有挑战性。你可以使用字符串注解或 `from __future__ import annotations` 来解决这个问题。

```
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional[Node] = None 
```

## 实际用例

让我们看看数据类在实际应用中的一些用例。

### 配置对象

数据类非常适合在应用程序中表示结构化设置。你可以定义一个具有特定字段、类型提示和默认值的数据类，而不是使用带有任意键的字典，这提高了可读性、安全性以及可维护性。

```
from dataclasses import dataclass


@dataclass
class AppConfig:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False


config = AppConfig(port=5000, debug=True)
print(config) 
```

输出：

AppConfig(host=’localhost’, port=5000, debug=True)

### API 中的轻量级 DTO

数据传输对象（DTOs）是 Web 服务中的请求和响应载荷。当你使用数据类创建它们时，它们提供了一种清晰、结构化的数据格式，而无需编写冗长的类。用数据类构建的 DTOs 可以轻松与序列化库集成。

```
from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    name: str
    email: str


# web API
request_payload = UserDTO(id=1, name="Jess", email="jess@example.com")
print(request_payload)
```

输出：

UserDTO(id=1, name=’Jess’, email=’jess@example.com’)

### 不可变领域实体

使用 `frozen=True` 的数据类可以轻松定义不可变领域实体，这在不变性很重要的系统中非常有用，例如领域驱动设计（DDD）。这可以防止 bug 并强制执行业务逻辑，因为 `frozen=True` 的对象在创建后无法更改。

```
from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    code: str
    symbol: str


usd = Currency("USD", "$")
eur = Currency("EUR", "€")


# attempt to modify a frozen field
try:
    usd.code = "US Dollar"  
except AttributeError as e:
    print(e)  
```

输出：

cannot assign to field ‘code’

## 测试和 [调试](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/) 数据类

数据类是一种独特的类，但许多 [调试](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/) 技巧与其他 Python 工具的调试技巧一致。

*   及早验证：`__post_init__` 在你创建对象时立即捕获无效值。
*   轻松打印：`__repr__` 显示所有字段，因此你可以看到对象内部的内容。
*   注意可变值，必要时使用冻结类（`frozen=True`）。

## 结论

像 Python 中的许多工具一样，数据类可能看起来很复杂，但稍加练习，它们就会变得更容易使用。它们是处理多个有组织数据实例的有用工具。一旦你熟悉它们，你会发现你的代码变得多么整洁和可读。它们还通过提供结构、类型提示以及用于比较和表示的内置方法来帮助防止常见错误。