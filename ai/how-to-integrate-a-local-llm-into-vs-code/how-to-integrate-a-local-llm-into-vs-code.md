
<!--
title: 如何在 VS Code 中集成本地 LLM
cover: https://cdn.thenewstack.io/media/2025/08/a2c9a7c3-vardan-papikyan-jze1dheaaew-unsplash.jpg
summary: 本文介绍了如何在 VS Code 中集成本地 LLM (Ollama) 以增强编码体验。步骤包括安装 Ollama，安装 Continue 扩展，配置扩展以连接到 Ollama，以及使用 Continue 编写、运行和调试代码。
-->

本文介绍了如何在 VS Code 中集成本地 LLM (Ollama) 以增强编码体验。步骤包括安装 Ollama，安装 Continue 扩展，配置扩展以连接到 Ollama，以及使用 Continue 编写、运行和调试代码。

> 译自：[How To Integrate a Local LLM Into VS Code](https://thenewstack.io/how-to-integrate-a-local-llm-into-vs-code/)
> 
> 作者：Jack Wallen

如果你的首选 [IDE](https://thenewstack.io/best-open-source-ides/) 是 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/)，并且你想知道使用本地化 AI [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 会是什么感觉，那么你很幸运。

但是为什么要这样做呢？

嗯，你可能想利用 AI 来增强你的工作流程，帮助调试你的代码，甚至学习一门新的 [编程语言](https://thenewstack.io/introduction-to-java-programming-language/)。无论你有什么原因，将 VS Code 与本地 LLM（比如 [Ollama](https://thenewstack.io/install-ollama-ai-on-ubuntu-linux-to-use-llms-on-your-own-machine/)，我的首选 AI）集成，并没有你想象的那么难。最终的结果是一个强大的工具，你可以利用它来满足你任何编码或与编码相关的需求。

与本地 LLM 集成的好处是，你不需要使用 API，你将拥有更多的隐私，它可以离线使用，并且你可以选择你喜欢的模型。

我将向你展示如何在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 机器（确切地说是 Pop!\_OS）上使用 Ollama 设置它。是的，你也可以在 macOS 和 Windows 上做到这一点；唯一的区别是 Ollama 的安装过程。在 Windows 上，安装 Ollama 就像下载应用程序并完成通常的安装过程一样简单。

## 你需要什么

要使此方法有效，你需要安装 VS Code，并且（对于 Linux）需要一个具有 sudo 权限的用户。就是这样。让我们开始工作吧。

## 在 Linux 上安装 Ollama

要在 Linux 上安装 Ollama，你只需运行以下命令：

```shell
curl -fsSL https://ollama.ai/install.sh | bash
```

在 macOS 上，该命令是：

```shell
curl https://ollama.ai/install.sh | sh
```

当该命令完成后，你就可以拉取模型了。在你这样做之前，请查看 [Ollama 模型库](https://ollama.com/library)，找到你想要使用的模型。用于代码工作的更好的模型之一被称为 codellama，可以使用以下命令拉取：

```shell
ollama pull codellama
```

## 安装所需的扩展

有问题的扩展名为 Continue。要安装 Continue，请打开 VS Code，然后按 Ctrl+P 键盘快捷键（对于 Linux 和 Windows），或 Cmd+P 快捷键（对于 macOS）。当搜索栏出现时，在其中键入以下内容：

```shell
ext install continue.continue
```

Continue 扩展应该会出现在左侧边栏中。单击安装（图 1），扩展将会安装。

[![](https://cdn.thenewstack.io/media/2025/08/9e86d332-continue1.jpg)](https://cdn.thenewstack.io/media/2025/08/9e86d332-continue1.jpg)

*图 1. 为 VS Code 安装 Continue。*

## 配置扩展

打开 VS Code 后，单击左侧边栏中的 Continue 图标，应该会出现 Continue 弹出窗口。在该窗口中，单击“Or, configure your own models”（或者，配置你自己的模型）（图 2）。

[![](https://cdn.thenewstack.io/media/2025/08/b15c0685-continue2.jpg)](https://cdn.thenewstack.io/media/2025/08/b15c0685-continue2.jpg)

*图 2. 你也可以使用 Continue Hub 帐户登录，但我们使用的是本地模型，因此没有必要。*

在下一个窗口中，滚动到底部，然后单击“Click here to view more providers.”（单击此处查看更多提供商）。在结果窗口中，选择 Ollama 作为提供商，然后从模型下拉列表中选择 CodeLlama（图 3）。

[![](https://cdn.thenewstack.io/media/2025/08/9d858136-continue3.jpg)](https://cdn.thenewstack.io/media/2025/08/9d858136-continue3.jpg)

*图 3. 将 VS Code 连接到 Ollama。*

单击“Connect”（连接），将会出现一个教程。我建议你阅读一下，以便更好地了解它的工作原理。你将会找到有关如何使用自动完成、编辑、聊天和代理功能的说明。

## 使用 Continue/Ollama

假设你希望 Ollama 为你编写一段 [Python](https://thenewstack.io/what-is-python/) 代码，该代码接受用户输入并将其保存到文件中。在 Continue 提示符（使用 Ctrl+I 访问）中，键入如下内容：

*write a Python program that accepts input from a user and saves it to a file*

你选择的模型将会开始工作，不仅会创建脚本，还会解释它的工作原理。

你将会注意到输出中有一个运行按钮（实际上是“应用代码”）。完成后，你可以提出一个后续问题，例如：

*run the above code*

你应该会看到运行该代码的示例输出。如果它有效，你就知道该代码是完美的。

你还可以选择打开一个终端窗口（通过 VS Code），打开一个新文件，将代码复制/粘贴到该文件中，保存它，然后像往常一样运行它。或者，你可以返回到 VS Code 主窗口，将代码复制/粘贴到一个新项目中，然后像那样运行/调试它。

说到调试，如果你想使用 Continue 调试代码，你可以返回到聊天窗口，键入类似 *fix the following Python code* 的内容，将代码粘贴到窗口中，然后按 Enter 键。你的本地模型应该能够检查代码，修复它发现的任何问题，并显示结果。

使用带有本地模型的 VS Code 的好处是，它让你有机会在你工作时了解你正在使用的语言。你可以提出问题，例如“What is a Python Tuple?”（什么是 Python 元组？）结果出奇地有帮助。

朋友们，这就是你如何将本地 LLM 集成到 VS Code 中，以使用 AI 来提高你的技能。