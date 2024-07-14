# 什么是 NumPy Python 库以及如何使用它？

![Featued image for: What Is the NumPy Python Library and How Do You Use It?](https://cdn.thenewstack.io/media/2024/06/2ed9d903-yunus-tug-uar4s-_zcyg-unsplash-1024x683.jpg)

[NumPy](https://numpy.org/) 代表 Numerical Python，是一个开源库，已成为科学和工程领域的宝贵工具。如果您需要在 [Python](https://thenewstack.io/an-introduction-to-python-a-language-for-the-ages/) 中处理数值数据，NumPy 应该是您的首选库。

NumPy 的目的是处理数组以及 [线性代数](https://thenewstack.io/quantum-algorithms-vs-quantum-inspired-algorithms/)、傅里叶变换和矩阵。但是，为什么在 Python 已经拥有可以作为数组的列表的情况下还要使用 NumPy 呢？简单来说，就是速度。列表可能很慢，尤其是在处理较大的数据列表时（这在科学用例中非常常见）。

因此，有了 NumPy。

NumPy 比 Python 列表快 50 倍，因为它将数组存储在连续的内存块中，这意味着进程能够非常快地访问（和操作）这些信息。最重要的是，NumPy 经过优化以与现代 CPU 协同工作，因此它不仅受益于内存放置，还受益于 [多核/线程 CPU](https://thenewstack.io/ai-hardware-software-dilemma/) 的速度。

不要认为 NumPy 仅对科学数据有用，因为它也可以用于通用数据的多维容器。您甚至可以定义任意数据类型，以便它可以与各种数据库集成。

现在您已经了解了 NumPy 的概念，让我们看看它是如何使用的。

## 您需要什么

您唯一需要的是安装了 Python 和 [Pip](https://pypi.org/project/pip/) 的操作系统。如果您没有安装 Pip，请不要担心，我会向您展示如何安装。我将在 Ubuntu Linux 上演示，因此如果您使用的是其他操作系统，则需要更改 Pip 安装命令。安装 Pip 后，其他所有内容都应该相当通用。

## 安装 Pip

安装 Pip 实际上非常简单。登录您的机器并打开一个终端窗口。在终端窗口中，发出以下命令：

*sudo apt-get install python3-pip -y*

对于使用 DNF 包管理器的操作系统，该命令将是：

*sudo dnf install python3-pip -y*

现在 Pip 已安装，是时候添加 NumPy 了。

## 安装 NumPy

在安装之前，您无法使用 NumPy。要安装它，您需要使用 Pip，如下所示：

*pip install numpy*

如果您发现无法使用 Pip 安装 NumPy（在 Ubuntu 24.04 中就是这种情况），还有另一种方法，它应该不会让您失望。为此，我们像这样返回到默认的包管理器：

*sudo apt-get install python3-numpy -y*

请注意，在 Fedora 基于的 Linux 发行版上安装 NumPy 使用 *pip install numpy* 命令可以正常工作。

无论哪种方式，您都应该能够使用上述任一命令安装 NumPy。

## 使用 NumPy

让我们看看 NumPy 是如何使用的。我们首先必须导入 NumPy 库，以便我们的应用程序可以使用它。这是通过以下方式完成的：

1 |
import numpy as np |

我们在上面所做的是导入 NumPy 并为它指定一个别名 (*np*)。接下来，让我们创建一个数组并将其分配给 *arr*，如下所示：

1 |
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) |

如您所见，我们在这里使用了 NumPy 的 *array* 函数。

最后，我们使用以下命令打印我们的数组：

1 |
print(arr) |

使用以下命令创建一个新文件：

1 |
nano nu_array.py |

将整个代码块粘贴到该文件中，它看起来像这样：

12345 |
import numpy as nparr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])print(arr) |

如果您运行上面的代码（使用命令 *python3 nu_array.py*），输出将是：

1 |
[ 1 2 3 4 5 6 7 8 9 10] |

非常简单。让我们借助 copy 参数来更复杂一些。

## copy 参数

有时您可能想要复制一个数组。当您这样做时，您将使用 *copy* 参数。假设您有以下数组：

1 |
[ 1 2 3 4 5 6 7 8 9 10] |

如果您要使用 *copy* 参数，它将创建该数组的精确副本。这可能看起来过于简单，但 *copy* 是一个非常重要的函数，因为您始终希望确保以最佳方式复制这些数组。

使用 *copy* 参数，有一个主要参数和两个可选参数，它们是：

*original_array* – 这是主要参数，定义要复制的原始数组。*order* – 这是可选参数之一，控制数组中值的复制顺序。*subok* – 这是另一个可选参数，定义是否将任何子类复制到输出数组。

让我们使用 *copy*。我在这里要给您抛出一些难题。

首先，我们将使用以下命令导入 NumPy：

1 |
import numpy as np |
接下来，我们使用 *start* 和 *stop* 参数（定义数组的起始位置和结束位置）创建一个 NumPy 数组，并将数组排列成 2 行 3 列（使用 *reshape*）。我们的数组如下所示：

```python
my_array = np.arange(start = 1, stop = 7).reshape(2,3)
```

需要注意的是，使用 *reshape* 定义了数组中对象的个数。例如，如果您使用 *start =1, stop = 10* 和 *reshape(2,3)*，您将收到以下错误：

```python
ValueError: cannot reshape array of size 9 into shape (2,3)
```

为什么呢？因为 2 行 3 列等于 6 个对象。如果您将形状更改为 (3,3)，则可以使用 *start=1, stop=10*。这都是数学问题。

让我们使用以下代码打印数组（以便我们知道它目前的样子）：

```python
print(my_array)
```

到目前为止，我们的整个应用程序如下所示：

```python
import numpy as np
my_array = np.arange(start = 1, stop = 7).reshape(2,3)
print(my_array)
```

上面的输出将是：

```
[[1 2 3]
 [4 5 6]]
```

现在，让我们使用以下代码创建数组的副本：

```python
copy_array = np.copy(my_array)
```

我们的整个代码如下所示：

```python
import numpy as np
my_array = np.arange(start = 1, stop = 7).reshape(2,3)
copy_array = np.copy(my_array)
print(my_array)
print(copy_array)
```

输出将是：

```
[[1 2 3]
 [4 5 6]]
[[1 2 3]
 [4 5 6]]
```

我们使用 copy 的原因是，如果我们只是使用类似 c*opied_array = my_array* 的代码，如果我们在定义了复制数组后更改原始数组中的值，则复制数组中的值也会发生更改。

请考虑以下情况：

```python
import numpy as np
my_array = np.arange(start = 1, stop = 7).reshape(2,3)
bad_copy = my_array
copy_array = np.copy(my_array)
print(my_array)
print(copy_array)
my_array[-1,-1] = 100
print(my_array)
print(bad_copy)
```

如果您运行上面的代码，两个数组都将打印为：

```
[[ 1  2  3]
 [ 4  5 100]]
[[ 1  2  3]
 [ 4  5 100]]
```

错误的副本不应该发生更改。这就是我们使用 *copy* 的原因。

这就是 NumPy 的入门介绍。下次我们将深入探讨，因为 NumPy 还有更多技巧。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)