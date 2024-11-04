# 为什么 Python 开发者应该关注测试

![为什么 Python 开发者应该关注测试的专题图片](https://cdn.thenewstack.io/media/2024/11/d6f8348e-testing-1024x574.png)

曾经听过那首老诗 *“Tick says the clock.. .Tick tick. What you have to do, do quick.”*?

现在，想象一下这句诗: *“请测试代码……先测试。你想要推送的内容，先测试。”*  我在写这篇文章时，这句诗就跳进了我的脑海。

7月19日将作为互联网时代主要停电事件之一载入史册。那天，网络安全提供商 Crowdstrike 向全球 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Windows 用户推送了一个更新，导致他们的系统崩溃，出现了可怕的蓝屏死机。这是 [由于越界内存读取](https://en.wikipedia.org/wiki/2024_CrowdStrike_incident) 造成的，影响了大约 850 万用户。实际上，我们任何人都可能要为将代码推送到生产环境负责。然而，在阅读了这次事件的教训之后，它又回到了一个永恒的 [预防措施](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/#:~:text=How%20Do%20We%20Prevent%20This%20From%20Happening%20Again): 测试你的代码。

**什么是测试**

虽然我们将重点关注测试 [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) 代码，但核心概念也适用于其他标准编程语言。

软件开发中的测试只是验证你的应用程序是否按预期工作。这意味着你的代码应该满足你设计它要做的 [预期](https://en.wikipedia.org/wiki/Software_testing)。在 [使用 Python 构建软件或数据管道](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) 时，你可能需要函数或类的组合来执行一些业务逻辑。这些函数通常需要一个输入来处理并产生一个预期的输出，甚至引发一个异常，因此需要对它们进行测试以确保它们能够正常工作。

假设正在为一家零售企业构建一个电子商务应用程序，以便在线向客户销售商品。可以从 [这里](https://github.com/VICIWUOHA/python-tests-tutorial) 克隆完整版本的源代码。

**测试类型**

在 [Python 编程](https://thenewstack.io/what-is-python/) 中，你的应用程序可能需要的最常见的测试包括但不限于：

- 静态测试
- 单元测试
- 集成测试

**静态测试**

静态检查可确保我们的代码在执行前能够正确编译。这包括格式检查和语法检查，其中一些可能会被你的 IDE 自动捕获。对于我们的电子商务应用程序，我们可能有一个如下所示的 `Item` 类：

```python
from dataclasses import dataclass, field
import uuid

@dataclass
class Item:
    name: str
    description: str
    price: int
    sku: str = field(default_factory=lambda: str(uuid.uuid4()))
```

静态检查将帮助我们识别 `Item` 类的 `price` 字段中缺少冒号“：”。因此，这在生产环境中永远不会起作用。详细的 [Item 类可能如下所示](https://github.com/VICIWUOHA/python-tests-tutorial/blob/main/src/item.py)。可以使用 Flake8、Pylint 等模块，以及最近构建于 Rust 之上并用于验证 Python 代码的 Ruff，在将 Python 代码合并到生产环境之前进行静态检查。本教程使用了 Ruff。

**单元测试**

假设开发者已经编写了没有语法错误的良好代码，单元测试可以说是最重要的测试类型。单元测试确保应用程序的各个组件（类和方法/函数）能够独立按预期工作。它们确保应用程序/业务逻辑不被违反。单元测试中使用的两个流行框架是 `unittest` 和 `pytest`。我们的单元测试示例将使用 `unittest` 模块。

这两个库的工作方式类似，但略有不同。这些模块使用断言进行工作，断言通常应产生 True 或 False 结果。`pytest` 使用原始断言，而 `unittest` 模块有自己的断言方法，例如 `assertEquals`、 `assertIn`、 `assertRaises` 等。`unittest` 模块还要求我们通过子类化 `unittest.TestCase` 来创建测试用例类。

### 使用 unittest 模块进行单元测试

在我们的电子商务应用程序中，对 `Item` 类的一个简单测试是验证创建的商品价格永远不会为负。这可能会给零售企业造成巨大的损失。请参阅下面的测试示例。

```python
import unittest

class TestItem(unittest.TestCase):
    def test_item_price_cannot_be_negative(self):
        # 如果价格低于零，我们的 item 类应该引发 ValueError
        with self.assertRaises(ValueError):
            Item("External SSD", "High-speed storage for data transfer", -5.0)
```
在业务逻辑之前定义这样的测试是[测试驱动开发 (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)的一部分。上面的测试使用 unittest 模块运行，只是断言如果我们的 Item 类包含负价格，则会引发 `ValueError`。让我们看看如何使上述测试用例通过。

```python
class Item:
    """Represents a sample item in an e-commerce system."""
    name: str
    description: str
    price: int
    sku: str = field(default_factory=lambda: str(uuid.uuid4()))

    # Added to ensure our items never have a -ve price.
    def __post_init__(self):
        if self.price < 0:
            raise ValueError(f"Item Price cannot be a negative value: {self.price}")
```

**运行测试**

要在 Python 中运行我们的 unittest 测试，我们只需键入如下所示的命令。

当我们运行此命令时，unittest 模块会自动查找任何父类为 `unittest.TestCase` 的文件夹，并将其函数视为要验证的测试。如果满足断言，测试将通过，否则将失败。

其他常见的 CLI 命令包括：

`python -m unittest test_module` 用于运行模块中的所有测试。

在我们的示例中，这将是：

`python -m unittest unit_tests/test_item.py` （指向 unit_tests 文件夹中的文件路径）或 `python -m unittest unit_tests.test_item`

其他具体示例可以在[项目仓库](https://github.com/VICIWUOHA/python-tests-tutorial/tree/main/unit_tests#running-tests)中找到。请注意，使用 pytest 构建的测试也以类似的方式执行。

**集成测试**

集成测试可确保我们应用程序的不同组件无缝协作。

这很有用，因为[在软件开发过程中，功能通常是逐步实现或增强的](https://thenewstack.io/how-to-define-and-use-your-own-functions-in-python/)。

在我们的电子商务应用程序的案例中，我们构建了一个 ShoppingCart 类以允许用户购买商品。我们的第一个方法显然是添加商品的功能，然后是删除商品的方法。下面显示了我们类的简约版本，但完整版本已在[此处](https://github.com/VICIWUOHA/python-tests-tutorial/blob/main/src/shopping_cart.py)实现。


```python
from datetime import datetime as dt
from src.item import Item
import uuid
import json

class ShoppingCart:
    """Shopping Cart Class (shortened)"""

    def add_item(self, item: Item, quantity: int):
        # check if item exists in cart , then update
        if self.__item_in_cart(item):
            self.increase_cart_item_quantity(item, quantity)
        else:
            # add new item using it's __dict__ property for easy access
            self.cart_obj[f"{item.sku}"] = {
                "item": item.__dict__,
                "quantity": quantity,
                "added_at": dt.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
                "updated_at": dt.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            }
            print(f"==>> `{item.name}` Added to Cart.")
            return json.dumps(
                {
                    "status": ShoppingCartStatus.CART_ITEM_ADDED.value,
                    f"{item.name}": self.cart_obj[f"{item.sku}"],
                },
                indent=4,
            )
```

**使用 pytest 运行测试**

我们可以使用以下命令的单元测试来验证上述方法是否有效：

`python -m pytest -k test_add_items_to_cart -v`
（其中 `-k` 搜索与其后模式匹配的测试/文件，`-v` 帮助我们获得更详细的输出。更多详细信息[此处](https://github.com/VICIWUOHA/python-tests-tutorial/tree/main/pytest_tests#running-tests)）。

```python
def test_add_items_to_cart(shopping_cart: ShoppingCart, item: Item):
    shopping_cart.add_item(item, 40)
```

**使用 pytest 进行集成测试**

虽然上述测试本身有效，但有必要测试将 `remove_cart_item` 函数添加到我们的 ShoppingCart 可以与 `add_item` 方法一起正常工作。

我们可以编写此测试，假设我们有一个 `cart_size` 属性，它向我们显示购物车中唯一商品的数量。

```python
def test_single_item_cart_size_is_zero_after_removal(
    shopping_cart: ShoppingCart, item: Item
):
    shopping_cart.add_item(item, 40)
    shopping_cart.remove_cart_item(item)
    assert shopping_cart.cart_size == 0
```

上述测试验证了在将单个商品添加到购物车并从购物车中移除后，购物车大小应减少到零。这验证了我们的 ShoppingCart 及其方法之间的交互产生了预期的行为。
我们现在可以使用下面的简单命令运行所有测试用例。

`python -m pytest`

**关于 pytest 的注意事项**

* 通过运行上述命令，请注意，如果没有明确告诉 pytest 使用哪个文件夹、文件或模式进行测试发现，它将运行目录中的所有测试，包括 `unittest.TestCase` 的子类的测试用例。
* Pytest 不需要我们为测试用例定义类。另一方面，Unittest 需要类，因为它最初的灵感来自用于 Java 应用程序的 JUnit 测试框架。
* 有关配置测试的更多信息已在...中提供。
[源代码库](https://github.com/VICIWUOHA/python-tests-tutorial/)

**结论**

在 Python 中进行测试有助于减少或完全避免生产环境中不必要的故障。需要注意的是，可以使用 GitHub Actions 等持续集成平台自动运行代码库上的测试。

与任何编程范例一样，几乎不可能测试所有未来在现实场景中可能出现的边缘情况。因此，经过实战检验的软件的部署仍应制定回滚计划，并在可能的情况下分阶段进行，以防万一出现问题。

您是否正在寻找熟练的 Python 专家来帮助您的项目更上一层楼？ 那么请查看 Andela 的指南“[如何聘请 Python 开发人员](https://www.andela.com/blog-posts/how-to-hire-a-python-developer-a-guide-to-finding-the-right-fit/?utm_medium=contentmarketing&utm_source=tns&utm_campaign=brand-global-python-testing-blog&utm_content=how-to-hire-python-developers)”。


[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，不容错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)