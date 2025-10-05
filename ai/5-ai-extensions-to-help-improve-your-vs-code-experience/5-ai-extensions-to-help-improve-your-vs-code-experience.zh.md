你以前听过，以后还会听到：AI 将长期存在，没有人能改变它。AI 已经渗透到生活的几乎每个角落，包括[编程](https://thenewstack.io/the-key-fundamentals-of-programming-you-should-know/)。

我已经能听到抱怨声了。

但即便 AI 可以为你完成编码工作，那些反对这一想法的人仍然可以将 AI 用于编写应用程序完整代码之外的其他用途。AI 可以用于增强你的编码工作流，帮助调试代码，清理代码等等。

如何将 [AI 用于编程](https://thenewstack.io/how-ai-can-help-you-learn-the-art-of-programming/)？如果 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) 是你首选的 [IDE](https://thenewstack.io/how-to-use-vs-code-as-your-python-ide/)，那实际上非常简单，这要归功于该应用程序可以添加的大量扩展。那么最大的问题是，你应该使用哪些扩展？

显然，每个项目都不同，所以不是每个 AI 扩展都能满足你的需求。即便如此，总有一些东西可以帮助你提高生产力和创造力。

让我们深入探讨一些可能对你有帮助的 VS Code 扩展。

## 1. Continue.dev

[Continue.dev](https://marketplace.visualstudio.com/items?itemName=Continue.continue) 是一款开源 AI 代码助手，可直接集成到 VS Code（以及其他 IDE）中。此扩展允许开发人员利用各种 AI 模型（包括本地和基于云的[大型语言模型 (LLMs)](https://thenewstack.io/introduction-to-llms/)）来增强其编码工作流。Continue 使团队能够轻松构建共享 AI 编码助手，这些助手包括可定制的工具、集中式配置和安全的凭据管理。Continue 允许你选择想要使用的模型（包括本地和远程），同时全面监督数据和协作。Continue 的一些主要功能包括：

* AI 驱动的代码建议和自动补全。
* 代码编辑和修改。
* 在 IDE 中与 LLM 交互，提出有关代码库的问题，获取解释，并获得调试或理解代码段的帮助。
* 支持创建和使用根据特定开发需求和工作流定制的自定义 AI 代理。
* 提供与各种 LLM 连接的灵活性。
* 利用多种上下文来源，例如代码、文档、终端输出和代码库结构。
* 开源，这意味着它允许透明性、社区贡献和定制。

如果你是独立开发者，可以免费使用 Continue。团队定价为每用户每月 10 美元，你必须联系 Continue.dev 咨询企业版。

## 2. llama.vscode

[llama.vscode 扩展](https://marketplace.visualstudio.com/items?itemName=ggml-org.llama-vscode)用于本地 LLM 辅助的文本补全、与 AI 聊天和代理式编码。此扩展具有大量功能，包括输入时自动建议、通过 Tab 键接受建议、通过 Shift+Tab 接受建议的第一行、通过 Ctrl/Cmd + Right 接受下一个词、控制最大文本生成时间、配置上下文范围、支持非常大的上下文、性能统计、用于代理式编码的 Llama Agent、模型的添加/删除/导出/导入、环境的添加/删除/导出/导入、针对不同用例的预定义环境、[MCP](https://thenewstack.io/mcp-a-practical-security-blueprint-for-developers/) 工具，以及从扩展内搜索/下载 Huggingface 上的模型。Llama.vscode 确实集成了 llama.cpp，后者是一个开源框架 (C/C++)，旨在在各种硬件上高效推理大型语言模型 (LLM)。Llama.vscode 可以免费安装和使用在任何支持 Llama 本地安装的操作系统上。

Llama.vscode 可以免费安装和使用。

## 3. llama-swap

[Llama-swap VSCode 扩展](https://marketplace.visualstudio.com/items?itemName=ggml-org.llama-vscode)是一个轻量级的 VS Code 透明代理服务器，提供对 llama.cpp 服务器的自动模型切换。通过 llama-swap，你可以按需切换模型、使用 Groups 同时运行多个模型、通过超时自动卸载模型、支持 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 和 [Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/) 等等。Llama-swap 能做什么？简而言之，llama-swap 是一款旨在自动加载、管理和切换用于代码辅助任务（如自动补全和聊天）的多个大型语言模型 (LLM) 的工具。请务必仔细阅读此扩展的安装部分，因为它可能比其他扩展稍微复杂一些。

Llama-swap 可以免费安装和使用。

## 4. Cline

[Cline VSCode 扩展](https://cline.bot/)是一个编码代理，它在 Visual Studio Code IDE 中作为代理运行，并利用大型语言模型 (LLM) 自动化各种开发任务，例如编写和重构代码、运行命令，甚至与网络浏览器交互以进行调试和测试。

Cline 功能：

* 代理能力。
* 深入的上下文理解。
* 人机协作控制。
* 模型无关性。
* 透明性。
* 自定义工具和规则。
* 计划模式。

Cline 可以免费安装和使用。

## 5. Roo Code

[Roo Code](https://github.com/RooCodeInc/Roo-Code) 作为一款 AI 驱动的自主编码代理运行，并可作为 Visual Studio Code 的扩展使用。Roo Code 将 AI 开发功能直接集成到你的编辑器中，作为一个理解项目上下文并自动化各种开发任务的编码助手。Roo Code 的主要功能包括：

* 代码生成。
* 自适应模型。
* 代码重构和调试辅助。
* 文档生成。
* 自动化任务。
* 外部工具集成。
* 内存和上下文管理。
* 结构化任务管理。

Roo Code 可以免费安装和使用。

在 VS Code [扩展市场](https://marketplace.visualstudio.com/VSCode)中还有很多 AI 扩展。请务必仔细查看各种选项，并安装任何可能帮助你完成项目甚至学习新语言的扩展。