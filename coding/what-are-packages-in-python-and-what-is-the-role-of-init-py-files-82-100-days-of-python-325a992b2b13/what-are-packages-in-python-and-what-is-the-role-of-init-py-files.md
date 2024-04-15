
<!--
title: Python中`__init__.py`文件的作用是什么？
cover: ./cover.png
-->

在 Python 中，`__init__.py` 文件是一个特殊文件，在包中扮演着几个重要的角色。在本教程中，我们将解释…

> 译自 [What are Packages in Python and What is the Role of `__init__.py` files? (82/100 Days of Python)](https://martinxpn.medium.com/what-are-packages-in-python-and-what-is-the-role-of-init-py-files-82-100-days-of-python-325a992b2b13)，作者 Martin Mirakyan。

在深入了解 `__init__.py` 文件的细节之前，了解 Python 中的包是什么非常重要。包是一种将相关模块（Python 文件）组织到一个易于使用的命名空间中的方式。包允许你将相关功能组合在一起，从而更容易组织和重用你的代码。

Python 中的包只是一个包含名为 `__init__.py` 的特殊文件的目录。`__init__.py` 文件在导入包时执行，它可以包含你喜欢的任何 Python 代码。

## `__init__.py` 文件的含义是什么？

`__init__.py` 文件在 Python 中有几个含义。首先，它用于将目录标记为包。当 Python 解释器遇到包含 `__init__.py` 文件的目录时，它将该目录视为包，并允许你使用点表示法从该包导入模块。

其次，`__init__.py` 文件用于初始化包。这意味着你可以使用 `__init__.py` 文件来设置包所需的任何配置或状态。例如，你可以定义包级变量或导入包依赖的其他模块。

最后，`__init__.py` 文件用于控制从包中导出的符号。当你从包中导入模块时，Python 首先在模块中查找符号，然后在包的 `__init__.py` 文件中查找。这允许你选择性地从包中导入符号，而不会弄乱命名空间。

## 为什么需要 `__init__.py` 文件？

`__init__.py` 文件出于几个原因是必需的。首先，它们允许你将代码组织成称为包的逻辑单元。这使得管理和重用代码变得更容易，并且还有助于避免命名冲突。

其次，`__init__.py` 文件是控制包的导入行为所必需的。通过选择性地从包中导入符号，你可以避免名称冲突并保持代码井然有序。

最后，`__init__.py` 文件通常用于设置包级配置和状态。这可以包括定义包级变量或导入包依赖的其他模块。

## `__init__.py` 文件的示例

以下是一些 `__init__.py` 文件如何在 Python 包中使用的示例。

### 定义包级变量

```python
# mypackage/__init__.py

# Define a package-level variable
__version__ = '1.1.42'
```

在此示例中，我们在 `__init__.py` 文件中定义了一个名为 __version__ 的包级变量。可以使用点表示法（mypackage.__version__）从包中的任何模块访问此变量。这是库开发人员的常见做法，他们将包版本和一些其他元数据包含在包的根目录中。

### 将模块导入包命名空间

```python
# mypackage/__init__.py

# Import the mymodule module into the package namespace
from . import mymodule
```

在此示例中，我们使用点表示法（from . import mymodule）将 mymodule 模块导入包命名空间。这允许我们使用点表示法（mypackage.mymodule）从包中的任何模块访问 mymodule 的内容。

### 定义包级函数

```python
# mypackage/__init__.py

# Define a package-level function
def my_package_function():
    print('Hello from my_package_function!')
```

在此示例中，我们在 `__init__.py` 文件中定义了一个名为 my_package_function 的包级函数。可以使用点表示法（mypackage.my_package_function()）从包中的任何模块访问此函数。

### 控制从包中导出的符号

```python
# mypackage/__init__.py

# Only export mymodule2 from the package namespace
from .mymodule2 import *
__all__ = ['mymodule2']
```

在此示例中，我们使用 `__all__` 变量来控制从包中导出的符号。我们使用星号表示法（`from .mymodule2 import *`）将 `mymodule2` 模块导入包命名空间，然后将 `__all__` 设置为应导出的符号列表（`__all__ = ['mymodule2']`）。这允许我们选择性地从包中导入符号，而不会弄乱命名空间。

## 关于 `__init__.py` 文件的重要事项

1.  `__init__.py` 文件可以为空：如果你不需要，不必在 `__init__.py` 文件中放置任何代码。一个空的 `__init__.py` 文件仍然是将目录标记为包所必需的，但它不必包含任何代码。
2. `__init__.py` 文件可用于执行设置操作：除了定义包级变量和函数之外，你还可以使用 `__init__.py` 文件来执行设置操作，例如，您可能希望初始化数据库连接或加载配置数据。
3. `__init__.py` 文件可以嵌套：如果您的包中有子包，您也可以在每个子包中包含一个 `__init__.py` 文件。这允许您为每个子包定义包级变量和函数。
4. `__init__.py` 文件可以引发 ImportError：如果您需要为包执行一些设置操作，例如导入必需的模块，您可以使用 `__init__.py` 文件来执行此操作。但是，如果设置操作失败，您可以在 `__init__.py` 文件中引发 ImportError 以防止使用该包。
5. 在 Python 3.3+ 中不需要 `__init__.py` 文件：从 Python 3.3 开始，您不必在包目录中包含 `__init__.py` 文件。但是，为了确保与旧版本 Python 的兼容性，仍然建议包含一个。
