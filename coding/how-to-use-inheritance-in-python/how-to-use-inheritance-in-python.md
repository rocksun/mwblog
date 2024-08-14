
<!--
title: Python中如何使用继承
cover: https://cdn.thenewstack.io/media/2024/07/2e411f9b-getty-images-tngwwfmfhnq-unsplash.jpg
-->

本教程解释了 Python 中的继承，它允许您定义一个类，该类继承另一个类中的所有方法和属性。

> 译自 [How To Use Inheritance in Python](https://thenewstack.io/how-to-use-inheritance-in-python/)，作者 Jack Wallen。

在 [面向对象编程](https://thenewstack.io/python-oop/) 中，有一个名为继承的功能，它允许一个新类继承现有类的属性和方法。通过使用继承，您不必总是重新发明轮子，这也意味着您的代码将更加简洁，更易于阅读和调试。

首先，什么是类？

将类想象成创建对象的蓝图，以及定义与从类创建的对象相关的属性（属性）和行为（方法）。类就像一个模板，您可以在代码中使用和重复使用。

继承需要两种类型的类：

**基类**（又名**父类**）：这是将继承其属性和方法的类。**派生类**（又名**子类**）：这是继承属性和方法的类。

有五种类型的继承：

* **单继承**: 派生类从单个基类继承。
* **多继承**: 派生类从多个基类继承。
* **多级继承**: 一个类从一个类派生，而该类又从另一个类派生。
* **层次继承**: 多个类从单个基类派生。
* **混合继承**: 两种或多种继承类型的组合。

使用继承的好处包括：

* [代码可重用性](https://thenewstack.io/coding-from-scratch-creates-new-risks/)
* [可扩展性](https://thenewstack.io/webassembly-could-be-the-key-for-cloud-native-extensibility/)
* 更好的代码组织

类继承的基本语法如下所示：

```python
class baseClass:
      # Base class attributes and methods
 
class derivedClass(baseClass)
      # Derived class attributes and methods
```

让我们先创建一个基类。这将使用我在本 [Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) 系列中概述的几个概念。

我们将创建一个定义人名并类似于此的基类：

```python
class Person:
  def __init__(fullName, fname, lname):
    fullName.firstname = fname
    fullName.lastname = lname
 
  def printname(fullName):
    print(fullName.firstname, fullName.lastname)
```

现在我们已经创建了类，我们使用它来创建对象并像这样打印对象：

```python
x = Person("Jack", "Wallen")
x.printname()
```

将所有这些放在一起，它看起来像这样：

```python
class Person:
    def __init__(fullName, fname, lname):
        fullName.firstname = fname
        fullName.lastname = lname
    def printname(fullName):
        print(fullName.firstname, fullName.lastname)

x = Person("Jack", "Wallen")
x.printname()
```

运行上面的命令，它将打印“Jack Wallen”。

那是基类。我们创建了一个派生类，它继承了基类（Person）的属性和方法。这是简单部分。我们将创建一个名为 Staff 的新类，它继承自 Person。该类看起来像这样：

```python
class Staff(Person):
    pass
```

通过使用 `pass`，我们通知 Python 我们没有向新类添加任何新属性或方法。

然后我们可以像这样从派生类创建一个新对象：

```python
x = Staff("Olivia", "Nightingale")
```

使用以下方法打印新对象：

```python
x.printname()
```

整个代码现在看起来像这样：

```python
class Person:
    def __init__(fullName, fname, lname):
        fullName.firstname = fname
        fullName.lastname = lname
    def printname(fullName):
        print(fullName.firstname, fullName.lastname)

x = Person("Jack", "Wallen")
x.printname()

class Staff(Person):
    pass

x = Staff("Olivia", "Nightingale")
x.printname()
```

运行上面的代码，它将打印：

```
Jack Wallen
Olivia Nightingale
```

请记住，我们之前使用 `pass` 是因为我们不想向新类添加任何新属性或方法。现在，我们将向新类添加新属性和方法。我们将坚持与我们的原始类类似的东西 - 我们的基类。这次，基类是：

```python
class Person(object):
    def __init__(fullName, name):
        fullName.name = name
    def getName(fullName):
        return fullName.name
    def isEmployee(fullName):
        return False
```

我们在上面添加了两个新函数，`getName`（返回人的全名）和 `isEmployee`（假设 `isEmployee` 等于 false）。

接下来，我们将创建一个派生类来定义 `isEmployee` 等于 True，它看起来像这样：

```python
class Employee(Person):
    def isEmployee(fullName):
        return True
```

到目前为止，我们有一个名为 Person 的类和一个名为 Employee 的类。正如您可能假设的那样，Person 不是员工，而 Employee 是。您将在下面看到它的实际应用：

```python
emp = Person("Jack Wallen")
print(emp.getName(), emp.isEmployee())

emp = Employee("Olivia Nightingale")
print(emp.getName(), emp.isEmployee())
```

你应该能够猜到会发生什么。由于 Jack Wallen 是 Person 类的对象，因此他不会被列为员工，而 Olivia Nightingale 是 Employee 类的对象，因此会被列为员工。
整个代码如下：

```python
class Person(object):
    def __init__(self, fullName, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Jack Wallen")
print(emp.getName(), emp.isEmployee())
emp = Employee("Olivia Nightingale")
print(emp.getName(), emp.isEmployee())
```

运行上面的代码，输出将是：

```
Jack Wallen False
Olivia Nightingale True
```

很不错，对吧？

**使用 super() 函数**

还有 `super()` 函数，它强制派生类继承基类中的所有属性和方法。这次，我们将重点关注学生及其毕业年份。

`super()` 函数的使用方法如下：

```python
class Student(Person):
    def __init__(self, fullName, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
```

`super()` 函数（在上面的示例中）的解释是：

- `super()`：返回超类的临时对象，允许调用其方法
- `__init__()`：用于初始化新对象的 Python 构造函数方法
- `(fname, lname)`：传递给超类构造函数的参数


我们的整个代码如下：

```python
class Person:
    def __init__(self, fullName, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fullName, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Jack", "Wallen", 2026)
x.welcome()
```

运行上面的代码，输出将是：

```
Welcome Jack Wallen to the class of 2026
```

这就是 Python 继承的基础知识。要了解更多关于继承的信息，请查看 [关于该主题的官方 Python 文档](https://docs.python.org/3/tutorial/classes.html#inheritance)。
