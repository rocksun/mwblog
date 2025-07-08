能够阅读他人的代码对于维护、改进和协作任何有意义的软件项目至关重要。 你很少会自己编写应用程序中的所有原始代码，而且从头开始完全重写应用程序的情况更是罕见。 更常见的情况是，你的工作流程将涉及到使用由其他人编写的代码（他们可能不再可以解释它），并由其他人在它出现在你的屏幕上很久之前进行迭代（他们也可能无法联系到）。

这使得阅读和理解现有代码与自己编写代码一样重要。 如果不知道每一行、每一个字符发生了什么，你将无法[调试](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/)、增强功能、改进产品或与任何人进行有效协作。 有时代码整洁、有条理且有据可查。 有时则不然。 你理解代码的能力不应取决于代码的完善程度。

在本教程中，我们将逐步完成一个命名不清晰的小应用程序。 以清单为指导，我们将逐步解码正在发生的事情。

下面的文件名为 `script.py`：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | import json |
|   | from collections import defaultdict |
|   |   |
|   | def f1(path): |
|   |     with open(path, 'r') as f: |
|   |         return json.load(f) |
|   |   |
|   | def f2(items): |
|   |     result = defaultdict(list) |
|   |     for i in items: |
|   |         k = i.get('category', 'Unknown') |
|   |         result[k].append(i) |
|   |     return result |
|   |   |
|   | def f3(d): |
|   |     out = {} |
|   |     for k, v in d.items(): |
|   |         s = sum(x['value'] for x in v) |
|   |         m = s / len(v) |
|   |         out[k] = m |
|   |     return out |
|   |   |
|   | def runner(): |
|   |     data = f1('data.json') |
|   |     grouped = f2(data) |
|   |     stats = f3(grouped) |
|   |     for k, v in stats.items(): |
|   |         print(f"{k}: {v:.2f}") |
|   |   |
|   | if \_\_name\_\_ == '\_\_main\_\_': |
|   |     runner() |

在 [Gist](https://gist.github.com/JessicaWachtel/ee7f77b7b7d6c86e9b0bf660ae14c907) 上查看代码。

此文件为 `data.json`：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | [ |
|   |     {"category": "A", "value": 10}, |
|   |     {"category": "B", "value": 20}, |
|   |     {"category": "A", "value": 30}, |
|   |     {"category": "C", "value": 40}, |
|   |     {"category": "B", "value": 25} |
|   | ] |

在 [Gist](https://gist.github.com/JessicaWachtel/4ffb4be4acc9e66767b88fb1317e23fe) 上查看代码。

## 我们将使用一个 5 步清单来确定此代码正在做什么

### 项目 1：程序总体上做什么？

了解程序的大局目的为理解其细节提供了蓝图。

一个好的起点是查找其主函数，并查看其他函数如何与其交互。 在我们的示例中，`runner()` 是主函数。 我们可以判断它是主函数，因为它分别调用了 `f1`、`f2` 和 `f3`。

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def runner(): |
|   |     data = f1('data.json') |
|   |     grouped = f2(data) |
|   |     stats = f3(grouped) |
|   |     for k, v in stats.items(): |
|   |         print(f"{k}: {v:.2f}") |

在 [Gist](https://gist.github.com/JessicaWachtel/f6edf4ed8451453c725cc881bda1aa33) 上查看代码。

在 `runner()` 中，我们可以理解以下工作流程：

* f1('data.json') 是首先发生的事情。
* f2(data) 处理 f1 返回的数据。
* f3(grouped) 处理 f2 的结果。
* 最后，它循环遍历 stats.items() 并打印一些格式化的数字 ({v:.2f})。

我们还可以得出合理的结论：

`f1` 加载数据（我们可以通过 `json.load()` 来判断）。

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def f1(path): |
|   |     with open(path, 'r') as f: |
|   |         return json.load(f) |

在 [Gist](https://gist.github.com/JessicaWachtel/d12ceff15dd0e4d535365d312d975b4b) 上查看代码。

`f2` 使用 `defaultdict(list)` 和每个类别的 `append(i)` 对其进行分组或重新组织。

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def f2(items): |
|   |     result = defaultdict(list) |
|   |     for i in items: |
|   |         k = i.get('category', 'Unknown') |
|   |         result[k].append(i) |
|   |     return result |

在 [Gist](https://gist.github.com/JessicaWachtel/aa17a7557e1c5f465ba8513b4dd1f84a) 上查看代码。

`f3` 使用 `sum(...)` 并除以 `len(v)` 来计算数值摘要或聚合。

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | def f3(d): |
|   |     out = {} |
|   |     for k, v in d.items(): |
|   |         s = sum(x['value'] for x in v) |
|   |         m = s / len(v) |
|   |         out[k] = m |
|   |     return out |

在 [Gist](https://gist.github.com/JessicaWachtel/e93e6bd733cac38f95fdc98a1505698a) 上查看代码。

该循环打印结果：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | for k, v in stats.items(): |
|   |     print(f"{k}: {v:.2f}") |

在 [Gist](https://gist.github.com/JessicaWachtel/e23562f318014799e94af69abdd08816) 上查看代码。

我们已准备好回答下一个问题…

### 项目 2：代码是如何组织的？

理解结构可以告诉你从哪里查找每个逻辑片段。

理解代码如何组织的一个很好的起点是查找导入、函数和入口点。

文件顶部标识导入：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | import json |
|   | from collections import defaultdict |

在 [Gist](https://gist.github.com/JessicaWachtel/7956d303dfb7b82f1653e45c31d23de1) 上查看代码。

这意味着我们的脚本正在使用其他模块的功能。 通过理解导入，你可以预测代码中使用的数据类型或方法。

你可以通过查找以 `def` 开头的行来识别函数。 将代码分解为函数可帮助你一次读取和理解一个片段。

你可以在脚本底部的这个特殊块中识别入口点：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | if \_\_name\_\_ == '\_\_main\_\_': |
|   |     runner() |

在 [Gist](https://gist.github.com/JessicaWachtel/770291ad825b69ab7f53958892da75ab) 上查看代码。

理解程序从哪里开始可以帮助你从头到尾跟踪流程。 这意味着当你直接运行脚本 (`python script.py`) 时，[Python](https://thenewstack.io/python/) 会运行此块中的代码。 此处调用的函数或代码（在本例中为 `runner()`）是执行的起点。

在我们的示例中，脚本导入 `json` 和 `defaultdict`，因此你可以预期它会处理 [JSON](https://thenewstack.io/how-to-use-json-in-your-python-code/) 数据并执行分组操作。 它定义了函数 `f1`、`f2`、`f3` 和 `runner()`。 基于我们在上一节中学到的知识，这表明代码被组织成模块化任务，例如文件读取、数据处理和运行主逻辑。

入口点调用 `runner()`，表明此函数是协调程序执行的主要例程。

### 项目 3：主要输入和输出是什么？

理解进入程序的内容（输入）和输出的内容（输出）有助于你从高层次上构建脚本正在做什么。

以下是如何查找输入。

查看在 `runner()` 中调用的第一个函数：`data = f1('data.json')`。 这告诉我们以下信息：

* 脚本从名为 `data.json` 的文件中读取。
* 如果我们查看 `f1()` 内部，我们会看到它使用 `json.load(f)`，这确认输入是 JSON 格式的文件。
* 实际内容（在 `data.json` 中）是字典列表，每个字典都有一个 `category` 和一个 `value` 字段。
* 此结构化输入被解析为 [Python 列表](https://thenewstack.io/python-for-beginners-lists/) 字典，每个字典代表一个数据点。

以下是如何查找输出。

此循环位于 `runner()` 的末尾：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | for k, v in stats.items(): |
|   |     print(f"{k}: {v:.2f}") |

在 [Gist](https://gist.github.com/JessicaWachtel/4b91e92856c9c0a8f3a888d5c344f9f0) 上查看代码。

该循环打印每个键（可能是一个类别名称）和一个带有两位小数的浮点数。 根据前面的函数，我们可以推断出这是每个类别的平均值。

此循环的示例输出：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | A: 20.00 |
|   | B: 22.50 |
|   | C: 40.00 |

在 [Gist](https://gist.github.com/JessicaWachtel/736e559e37236bfeb0876013cc0cd1cd) 上查看代码。

这确认脚本正在按类别汇总值并打印结果。

从所有这些细节中，我们可以理解输入和输出。 主要输入是一个 JSON 文件，其中包含一个项目列表，每个项目都有一个类别和一个值。 输出是打印到控制台的纯文本（具体来说，是一个摘要，显示每个类别的平均值）。

### 项目 4：数据如何在函数之间流动？

逐步跟踪数据如何移动和更改是理解代码做什么的最重要的方法之一。 它可以帮助你不仅了解每个函数单独做什么，还可以了解它们如何协同工作以将输入转换为输出。

让我们按照调用顺序跟踪数据通过每个函数。

`f1('data.json')`

*输入为 `data.json`*

该函数以读取模式打开名为 `data.json` 的文件。 它使用 `json.load()` 来解析内容。 结果作为字典列表返回（`json.load()` 始终输出字典和列表）。

*输出：*

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | [ |
|   |     {"category": "A", "value": 10}, |
|   |     {"category": "B", "value": 20}, |
|   |     {"category": "A", "value": 30}, |
|   |     {"category": "C", "value": 40}, |
|   |     {"category": "B", "value": 25} |
|   | ] |

在 [Gist](https://gist.github.com/JessicaWachtel/340738cd3abacd5691fd513a5b77d7e1) 上查看代码。

*然后，这成为 `f2` 的输入。*

`f2(items)`

此函数创建一个空的 `defaultdict`，其中列表作为默认值。 它循环遍历 `f1` 返回的列表中的每个字典。 它查找每个项目的 `'category'` 键。 如果不存在任何类别，则返回 `'Unknown'`。 然后，它将整个字典附加到相应类别的列表。

*输出：*

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | { |
|   |     'A': [ |
|   |         {"category": "A", "value": 10}, |
|   |         {"category": "A", "value": 30} |
|   |     ], |
|   |     'B': [ |
|   |         {"category": "B", "value": 20}, |
|   |         {"category": "B", "value": 25} |
|   |     ], |
|   |     'C': [ |
|   |         {"category": "C", "value": 40} |
|   |     ] |
|   | } |

在 [Gist](https://gist.github.com/JessicaWachtel/2f42c8590d6e5d201f019a6dbed3400b) 上查看代码。

*此数据成为 `f3` 的输入。*

`f3(d)`

此函数采用来自 `f2` 的分组字典。 它创建一个名为 `out` 的空字典。 在每个键值对中，`k` 是类别，`v` 是该类别中的项目列表。

它计算以下内容：

* `s = sum(x['value'] for x in v)`：所有 `value` 字段的总和
* `m = s / len(v)`：平均值

它将平均值存储在 `out[k]` 中。

*输出：*

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | { |
|   |     'A': 20.0, |
|   |     'B': 22.5, |
|   |     'C': 40.0 |
|   | } |

在 [Gist](https://gist.github.com/JessicaWachtel/eb5f53922130b0b3c16277edef13e503) 上查看代码。

*它成为 `runner()` 中的变量 `stats`，然后将其打印出来。*

`runner()`

`runner()` 按照正确的顺序调用 `f1`、`f2` 和 `f3`。 它接收最终的平均值字典。 然后，它循环遍历 `stats.items()` 并打印每个类别及其平均值，格式化为 2 位小数。

*输出：*

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | A: 20.00 |
|   | B: 22.50 |
|   | C: 40.00 |

在 [Gist](https://gist.github.com/JessicaWachtel/a9f0fe8d2b964d503932b2feff814085) 上查看代码。

这意味着什么？

通过每个函数跟踪数据会显示渐进式转换：

原始 JSON 列表按类别分组，然后按类别求平均值，最后打印为摘要。

要自行完成此操作并查看任何函数返回的内容，请在每次调用后添加 `print()` 语句：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | print("Data loaded:", data) |
|   | print("Grouped data:", grouped) |
|   | print("Computed stats:", stats) |

在 [Gist](https://gist.github.com/JessicaWachtel/056a6b14d7b369bc93602f2d6e03b15f) 上查看代码。

### 项目 5：运行代码并查看发生了什么

运行脚本是验证你对代码正在做什么的心理模型的较快方法。 你可以在此过程中的任何时间执行此步骤。 运行代码还有助于你捕获缺失的文件、日期格式问题和所有其他意外错误。

如何运行此文件：

1. 确保将脚本另存为 `script.py`。
2. 确保你的 `data.json` 文件与 `script.py` 位于同一文件夹中。
3. 打开你的终端或命令提示符。
4. 导航到包含这两个文件的文件夹。
5. 运行：`python script.py`。

实际输出：

此文件包含隐藏或双向 Unicode 文本，这些文本的解释或编译结果可能与下方显示的内容不同。 要查看，请在能够显示隐藏 Unicode 字符的编辑器中打开此文件。
[详细了解双向 Unicode 字符](https://github.co/hiddenchars)

|   |   |
|---|---|
|   | A: 20.00 |
|   | B: 22.50 |
|   | C: 40.00 |

在 [Gist](https://gist.github.com/JessicaWachtel/d6455197df334f13d3c07247e24c1979) 上查看代码。

当预期输出与实际输出匹配时，它确认你没有任何错误并且你的环境已正确设置。 它还确认你对代码正在做什么有正确的理解。

### 有用的提示

以下是一些你可以做的除了清单之外的事情，以帮助你理解代码：

* 使用工具来检查变量。 检查变量可以让你确切地看到内存中有什么。
* 基于代码做笔记和图表。 笔记和图表可以帮助你跟踪数据结构之间的关系。
* 了解正在使用哪些库。 了解库可以帮助你知道有哪些助手可用。

最后：要有耐心！ 即使是经验丰富的开发人员也需要时间来解码不明确的名称。

## 结论

阅读别人的 Python 代码，尤其是当名称不明确时，可能具有挑战性，尤其是在一开始时。 但是通过逐步分解它，你可以将令人困惑的脚本变成你完全理解的东西。