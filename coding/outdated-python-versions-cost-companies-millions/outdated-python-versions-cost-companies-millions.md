
<!--
title: 过时Python版本致企业损失数百万
cover: https://cdn.thenewstack.io/media/2025/08/b0e47ae7-katelyn-perry-uze9nxp5er8-unsplash.jpg
summary: 根据 JetBrains 报告，多数 Python 开发者使用旧版本，导致企业在云支出上浪费资金。升级到 Python 3.13 可显著提升性能，降低成本。容器化并未加速升级，许多团队未意识到财务影响。数据科学工作负载的转变使性能改进更重要。
-->

根据 JetBrains 报告，多数 Python 开发者使用旧版本，导致企业在云支出上浪费资金。升级到 Python 3.13 可显著提升性能，降低成本。容器化并未加速升级，许多团队未意识到财务影响。数据科学工作负载的转变使性能改进更重要。

> 译自：[Outdated Python Versions Cost Companies Millions](https://thenewstack.io/outdated-python-versions-cost-companies-millions/)
> 
> 作者：Darryl K. Taft

如果你的公司正在运行任何版本低于 3.13 的 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) 应用程序，那么你可能正在白白烧钱。

根据 [JetBrains](https://www.jetbrains.com/) 发布的 [2025 年 Python 现状](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/) 报告，高达 83% 的 [Python 开发者](https://thenewstack.io/python-developers-hold-the-key-to-blockchain-adoption/) 正在运行一年前或更早的版本，其中近一半 (48%) 仍在使用 Python 3.11，而 27% 还在使用 Python 3.10 或更早版本。

但这不仅仅是一个[技术债务](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)问题，更是一个财务上的大出血，正在消耗着企业的云账单。

## “足够好”的隐藏成本

受访者给出的不使用最新版本的主要原因包括：“我使用的版本满足我所有的需求”（53%）和“我没有时间更新”（25%）。

这是一种老旧的“没坏就别修”策略，但这些开发者没有意识到的是，他们“足够好”的 [Python 版本](https://thenewstack.io/python-mulls-a-change-in-version-numbering/)正在让他们的企业在不必要的云计算支出上花费大量资金。

## 性能差距和财务影响

Python 的最新版本不仅增加了新功能，还提供了显著的性能改进，可以直接转化为成本节约。Python 3.11 到 3.13 的执行速度大约快 11%，内存使用量减少 10-15%。从 Python 3.10 到 3.13 的飞跃代表着速度提高了惊人的 42%，内存使用量减少了 20-30%。这些改进代表着根本的效率提升。

根据该报告，对于年度 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 账单中位数为 230 万美元的中型市场公司而言，如果 EC2 计算成本占 50-70%（115 万至 160 万美元），那么从 Python 3.10 升级到 3.13 每年可节省 42 万美元。

对于年度 AWS 支出为 2400 万至 3600 万美元，EC2 计算成本为 1200 万至 2500 万美元的大型企业而言，相同的升级带来的潜在节省每年可达 560 万美元。报告显示，这些计算假设基于已记录的性能改进，计算密集型工作负载的效率保守提高了 30%。

## 容器化的悖论

[Talk Python](https://talkpython.fm/) 的创始人兼 [Python 软件基金会](https://www.python.org/psf-landing/) 的研究员 [Michael Kennedy](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/#author) 在一篇关于该报告的[博客文章](https://blog.jetbrains.com/pycharm/2025/08/the-state-of-python-2025/)中写道：“调查还表明，我们中的许多人正在使用 Docker 和容器来执行我们的代码，这使得 83% 甚至更高的数字更加令人惊讶。使用容器，只需选择容器中最新的 Python 版本即可。由于一切都是隔离的，因此你无需担心它与系统其余部分的交互。”

然而，容器化并未加速 Python 升级这一事实表明，许多开发团队并未意识到其财务影响。

## 超越直接计算成本

财务影响不仅仅限于计算效率。团队花费时间来解决性能限制，而不是构建功能，这代表着机会成本，这些成本不会直接显示在云账单中。

Kennedy 写道：“运行旧版本 Python 的 83% 的开发者可能错过了比他们意识到的更多的东西。不仅仅是他们错过了一些语言特性。[Python](https://thenewstack.io/python-3-14-0-alpha-is-now-available-heres-whats-included/) 3.11、3.12 和 3.13 都包含主要的性能优势，即将推出的 3.14 将包含更多优势。”

## 升级经济学

Kennedy 说，Python 版本升级提供了软件开发中可获得的最高投资回报率的改进之一。

他写道：“令人惊奇的是，你无需更改代码即可获得这些好处。你只需选择较新的运行时，你的代码运行速度就会更快。CPython 在向后兼容性方面做得非常好。升级很少涉及大量工作。”

与架构变更或重大重构项目不同，大多数应用程序无需更改代码，迁移风险最小，部署后可立即获得性能优势，并提供随着规模增长的复合节省，Kennedy 指出。

## 数据科学因素

调查显示，数据科学现在占所有 Python 使用量的 51%，其中 [pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/) 和 [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) 是最常用的工具。

Kennedy 强调了这种转变的重要性：“我们 Python 权威领域的许多人都在谈论 Python 被分为三部分：三分之一用于 Web 开发，三分之一用于数据科学和纯科学，三分之一作为一个包罗万象的类别。现在我们需要重新考虑这种定位，因为这三分之一中的一个已经成为 Python 中最重要的部分。”

Kennedy 表示，这种向计算密集型工作负载的转变使得性能改进在财务上更加重要。涉及大型数据集处理、模型训练和推理、复杂统计计算和扩展批处理作业的数据科学工作流程都将受益于 Python 最近的性能改进。

## 最终结论

在一个企业都在寻求优化成本和提高效率的时代，Python 版本升级代表着唾手可得的成果。