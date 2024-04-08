
<!--
title: JetBrains推出本地运行的AI代码补全
cover: https://cdn.thenewstack.io/media/2024/04/1bc544ba-despaired-2261021_1920.jpg
-->

人工智能驱动的全新代码补全工具旨在将代码保留在本地，从而降低受监管行业的安全性问题。

> 译自 [JetBrains Launches AI Code Completion on Local Machines](https://thenewstack.io/jetbrains-launches-ai-code-completion-on-local-machines/)，作者 Loraine Lawson。

[JetBrains](https://www.jetbrains.com/) 在其 IDE 中提供全行代码补全功能，这要归功于在本地机器上运行的 AI 模型，因此无需将代码发送到场外。

该公司指出，此功能旨在吸引对数据隐私法规有严格要求的行业，例如医疗保健和金融行业，或任何可能对将代码发送到外部持犹豫态度的组织。

JetBrains 的高级机器学习工程师 [Daniel Savenkov](https://www.linkedin.com/in/daniel-savenkov-098b41149/?originalSubdomain=rs) 解释道：“我们的产品如何运作？您在本地计算机上运行一个不太大但很智能的语言模型，所有操作都在本地进行。”“这非常重要，因为并非所有人都愿意将自己的代码共享到云端。”

## 模型在内部机器上运行

JetBrains 代码补全功能在本地运行这一事实使其有别于其他代码补全工具，包括 [GitHub 的 Copilot](https://thenewstack.io/hey-github-tries-a-voice-interface-for-copilot/)，后者依赖于对底层基于云的大语言模型的外部调用。Savenkov 表示，虽然 Copilot 已有用户协议禁止将代码用于代码补全以外的任何用途，但在某些行业，由于安全问题，这还不够。

JetBrains 代码补全模型仍然是[大语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/)，但有 1 亿个参数。Savenkov 补充说，相比之下，行业标准模型要大 100 倍。较小的模型是代码补全模型处理全行代码补全而不是大块代码的原因之一。Savenkov 表示，处理大块生成的代码确实很难。由于某些建议可能不好，因此编码人员必须查看 AI 模型创建的所有代码。

Savenkov 表示，业界对于哪种长度的代码补全效果最好存在一些争论。一些代码补全产品可以生成大量的代码块，但也可能产生 API 调用等幻觉。他补充说，JetBrains 将代码补全确定为一行，作为一种“相当公平的折衷”，[开发人员可以轻松使用](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/)。

在本地运行这一事实还最大程度地减少了延迟问题。

他说：“这比生成 10 行代码或一个块或整个方法或整个类要简单得多。”“因此，我们有机会使用较小的模型并获得真正有意义且有用的结果。所以，我们大致是这样到达这里的，我们有一个本地、不太大的模型，生成[一行](https://thenewstack.io/preflight-defends-against-supply-chain-attacks-with-single-line-of-code/)代码。”

## 较小的 LLM 提供了可比的质量

他声称，即使 LLM 较小，质量也相似。

Savenkov 告诉 The New Stack：“与真正基于云的大模型相比，在我们的用例中，质量没有大幅下降。当然，如果我们开始尝试生成代码块，差异会更大，但保持单行，差异不会那么大。”

该模型还利用来自 IDE 的信息来过滤掉幻觉，例如对不存在的 API 的调用。他还指出，这也有助于确保代码建议不包含语法错误，例如不存在的变量或方法。

此外，该公司机器学习产品经理 [Mikhail Kostyukov](https://www.linkedin.com/in/mikhailkin/?originalSubdomain=nl) 补充说，由于语言模型是针对特定语言和框架进行训练的，而不是一般性训练，因此它可以更小。

JetBrains 在其 Python IDE PyCharm 中试用了代码补全功能。截至今日，它已在相应的 JetBrains IDE 中开箱即用地提供给 Java、Kotlin、JavaScript、TypeScript、CSS、PHP、Go 和 Ruby：IntelliJ IDEA、WebStorm、PhpStorm、GoLand 和 RubyMine。

在未来几个月内，该公司将在所有支持这些语言的 JetBrains IDE 中将此功能扩展到 C#、Rust 和 C++，包括 Rider、RustRover、CLion Nova 等。

除了其代码补全产品外，[JetBrains 还提供 AI 助手](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/)，作为附加订阅服务，可以自动完成整个代码块。该公司表示，AI 助手还提供了改进的测试生成和云代码补全、提交消息的自定义提示、从 AI 聊天创建文件以及更新的编辑器内代码生成功能。

此更新可在 IntelliJ IDEA、PyCharm、PhpStorm、ReSharper 和其他 JetBrains IDE 中使用，以及 Fleet 中作为补充功能。

此 2024.1 更新还为 JetBrain 的 IDE 引入了其他新功能，包括一个经过全面检修的终端功能，其中包含简化命令行任务的增强功能。该公司在新闻稿中指出，该终端现在支持在块内导航，分别嵌套每个命令、命令完成功能以及轻松访问命令历史记录。

特定 IDE 的改进包括：

- IntelliJ IDEA 将为新发布的 Java 22 中的功能提供支持。它还结合了基于 K2 Kotlin 编译器的新 Kotlin K2 模式，以增强代码分析。
- RubyMine 可以执行当前产品本地 SDK 中的 VCS 命令。
- PyCharm 2024.1 为[集成 Jupyter 笔记本](https://thenewstack.io/integrate-jupyter-notebooks-with-github/)带来了新功能，以及简化的版本控制，其中包含新的可视化差异、小部件渲染以及使用 AI 助手解释 pandas 和 Polars DataFrames 的功能。此外，Hugging Face 模型的所有文档都可以在 PyCharm 中直接访问。
- PhpStorm 为 Symfony 的 AssetMapper 添加了支持。新闻稿指出，开发人员现在可以通过 importmap.php 快速安装缺失的模块和包，并为其类和方法利用完全自动完成。他们还可以为 PHP 类和方法生成 [Pest 测试](https://pestphp.com/)，并直接从 Intention 操作菜单创建新的 Pest 测试。