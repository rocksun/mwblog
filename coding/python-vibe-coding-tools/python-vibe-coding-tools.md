<!--
title: Python氛围编程工具
cover: https://cdn.thenewstack.io/media/2025/08/36fa9428-a-c-qqvg560p-r4-unsplash.jpg
summary: 氛围编程是一种通过与AI对话而不是自己编写代码的编程方式。文章介绍了GitHub Copilot、Cursor、Open Interpreter和AI Notebook Tools等Python氛围编程工具，并提供了提示技巧。
-->

氛围编程是一种通过与AI对话而不是自己编写代码的编程方式。文章介绍了GitHub Copilot、Cursor、Open Interpreter和AI Notebook Tools等Python氛围编程工具，并提供了提示技巧。

> 译自：[Python Vibe Coding Tools](https://thenewstack.io/python-vibe-coding-tools/)
> 
> 作者：Jessica Wachtel

准备好迎接一个疯狂的数据了吗？在《华尔街日报》这篇关于[氛围编程的文章](https://www.wsj.com/articles/vibe-coding-has-arrived-for-businesses-5528e942?)中，Gartner 预测，在三年内，40% 的新商业软件将使用 [AI 辅助技术](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/)开发。看到自从我上编程学校以来事情发生了如此大的变化，真是令人惊叹。我想象如果有了 AI 的帮助，我的经历会大不相同。

也就是说，既然我们已经进入了氛围编程的新世界，那么氛围编程到底是什么？我们又该如何确保自己不被落下呢？[氛围编程](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/) 是 [Andrej Karpathy](https://github.com/karpathy?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 在 2025 年 2 月提出的一个术语。他说：“你要完全沉浸在氛围中，拥抱指数增长，忘记代码的存在……我只是看看东西，说说东西，运行东西，复制/粘贴东西，而且大多时候都能正常工作。”

Karpathy 认为，氛围编程是一种通过与 AI 对话而不是自己编写所有代码的编程方式。你用简单的语言描述你想要什么，然后 AI 为你编写代码。然后，你给出更多指令，测试结果，并通过与 AI 对话来进行更改，而不是键入每一行代码。简而言之，这意味着减少编写代码，更多地描述想法和功能。《商业内幕》的[这篇文章](https://www.businessinsider.com/amazon-q-developer-ai-vibe-coding-aws-2025-4?) 认为，这不会让开发者过时，但掌握这项技能绝对会有帮助。

AI 工具无处不在，而且似乎每天都会冒出五个新的工具。让我们来看看一些更有用的工具，以帮助你在 [Python](https://thenewstack.io/what-is-python/) 中进行氛围编程。

## Python 氛围编程工具

*大多数这些工具都可以生成任何语言的代码，但最好坚持使用你熟悉的语言；在本教程中，我们将使用 Python。*

### GitHub Copilot

[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 是一个存在于你的代码编辑器中的 AI 助手。它可以读取你的注释或代码，并建议完整的函数、代码片段或测试。GitHub Copilot 在以下方面特别有用：

* 编写重复或样板代码。
* 根据简单的描述获取函数或代码片段的建议。
* 学习如何使用新的库或 API。
* 在不从头开始的情况下进行原型设计。

**如何使用它**

在 IDE 中安装它之后，你可以输入像 `# Download an image from a URL and convert it to grayscale` 这样的注释。Copilot 将会回复完整的代码段：

### Cursor

[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 是 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 的一个版本，它带有一个内置的 AI 助手。它可以随时编辑、重构或解释你的代码。由于 Cursor 是一个代码编辑器，你可以直接在你的机器上安装它。Cursor 在以下方面特别有用：

* 改进和清理现有代码。
* 添加像异步函数或错误处理这样的功能。
* 调试大型项目中棘手的部分。
* 保持你的代码组织良好且易于维护。

Cursor 允许你高亮显示一段代码，然后输入一个请求，比如“Refactor this to use async”。

```
# Original code
def fetch_data():
    data = get_data_from_api()
    process(data)
```

它会自动回复更新后的代码：

```
# Refactored code with async
async def fetch_data():
    data = await get_data_from_api()
    process(data)
```

### Open Interpreter

[Open Interpreter](https://github.com/openinterpreter/open-interpreter) 是一个本地的、开源的 AI 助手，它的行为就像一个精通终端的编码伙伴。它可以运行命令，生成脚本，并帮助直接从你的机器上自动化任务。Open Interpreter 在以下方面特别有用：

* 快速编写和运行小型脚本。
* 自动化重复性任务。
* 在本地或离线环境中工作。
* 通过自然语言与你的终端进行交互。

在本地安装它之后，在你的终端中启动该助手：

```
pip install open-interpreter
interpreter
```

一旦你进入 Open Interpreter 界面，你只需输入一个简单的英语请求，比如“创建一个 Python 脚本，每小时发送一次桌面通知。”

Open Interpreter 将会通过生成和运行（必要时）类似这样的东西来做出回应：

```
# notification_script.py


import time
from plyer import notification


while True:
    notification.notify(
        title='Reminder',
        message='Time to take a break!',
        timeout=10
    )
    time.sleep(3600)
```

如果你说类似“将该脚本保存为 reminder.py 并运行它”这样的话，它也会按照这些指示执行。

### AI Notebook Tools

AI notebook 工具（如 AI Notebook Copilot）是 Jupyter 的附加组件，可以将自然语言提示转换为代码单元格。这些工具在以下方面特别有用：

* 快速生成数据分析或可视化代码。
* 交互式地探索数据集。
* 通过即时代码示例进行教学或学习。
* 简化基于 notebook 的开发。

你需要在 VS Code 中安装 Jupyter 和 GitHub Copilot 扩展，然后打开你的 Jupyter notebook 才能开始使用。

在 Jupyter Notebook 代码单元格中，以注释的形式输入一个提示：

```
# %% Prompt
# Create a pandas DataFrame with 5 rows of random integers between 1 and 100
```

AI 将在下一个单元格中填充代码：

```
import pandas as pd
import numpy as np


data = np.random.randint(1, 101, size=(5, 3))  # 5 rows, 3 columns of random integers between 1 and 100
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)
```

## 更好的氛围编程技巧

* **对你的提示要具体。** 不要只是说“制作一个图表”，像“绘制一个显示华氏温度下三个温度读数的条形图”这样的指令会产生更好的结果。
* **与实际编码类似，将大的步骤分解成小的部分。** 给 AI 提供逐步指导会产生更清晰、更准确的代码。
* **不要假设一切都是完美的——AI 也会犯错。** 测试代码的正确逻辑和安全性。
* **练习！** 仅仅因为它是由 AI 生成的，并不意味着它没有学习曲线。你的第一个项目永远是你最糟糕的项目，但你只能从这里开始进步！

## 结论

氛围编程可以帮助你快速地将想法转化为可工作的代码，而不会迷失在语法或样板代码中。它是关于与 AI 协作，以加速开发，并将你的注意力集中在最重要的事情上：构建很酷的东西。