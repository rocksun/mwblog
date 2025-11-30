<!--
title: Cursor 2.0 IDE：AI赋能，开发体验惊艳升级！
cover: https://cdn.thenewstack.io/media/2025/11/8379b3d5-wesley-tingey-z0lr-6fa2r8-unsplash-1.jpg
summary: Cursor 2.0 更新，集成AI，含Composer。支持多智能体，代码效率高，提供免费及付费版。
-->

Cursor 2.0 更新，集成AI，含Composer。支持多智能体，代码效率高，提供免费及付费版。

> 译自：[Cursor 2.0 IDE Is Now Supercharged With AI and I'm Impressed](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/)
> 
> 作者：Jack Wallen

[Cursor IDE](https://thenewstack.io/install-cursor-and-learn-programming-with-ai-help/) 最近已更新至 2.0 版本，并带来了强大的 [AI 集成](https://thenewstack.io/six-reasons-youll-want-to-use-mcp-for-ai-integration/)功能。这次新更新于十月底发布，其中包含一个名为 Composer 的新功能，它是一个前沿模型，据称比同类模型快四倍。

新版本专为 Cursor 内的低延迟智能体编程而构建，并使用多种工具进行训练，包括代码库范围内的语义搜索。这种训练使 Cursor 更能理解和处理大型代码库。

[Cursor 2.0](https://cursor.com/blog/2-0) 还拥有一个全新的、更简洁的界面，因此应该更容易上手。您还会发现大量可启用/禁用的智能体，例如：

*   Composer 1
*   Sonnet 4.5
*   Gemini 3 Pro
*   GPT-5.1 Codex High
*   GPT-5.1
*   GPT-5.1 Codex Mini
*   Grok Code
*   Gemini 2.5 Flash
*   Deepseek V3.1
*   Ollama
*   GPT-5.1 Codex Fast

以上列表只是冰山一角（图 1）。

[![](https://cdn.thenewstack.io/media/2025/11/ae083f47-cursor1.jpg)](https://cdn.thenewstack.io/media/2025/11/ae083f47-cursor1.jpg)

*图 1：如您所见，Cursor 2.0 可以使用大量的智能体。*

Cursor 2.0 中的其他功能包括：

*   可以并行运行多个智能体（最多 8 个）。
*   使用多个智能体时，合并的差异视图。
*   全新的专用智能体视图。
*   支持多步编码任务。
*   集成了 Chrome DevTools。
*   在集成式和常规 Chrome 浏览器之间无缝切换。
*   团队现在可以定义和共享自定义命令和规则，以简化工作流程。
*   内置语音转文本功能。
*   增强的语言特定功能，使代码导航和调试更容易。
*   Shell 命令在安全、沙盒化的环境中运行。

我决定试用一下 Cursor 2.0，看看它的效果如何。我使用了一个我编写的用于掷 D&D 骰子的旧 [Python](https://thenewstack.io/what-is-python/) 脚本，看看智能体能如何改进代码（以及代码的功能）。

我原始代码的问题是骰子掷法的格式。最初的格式是“3d6+2”，这意味着掷三个六面骰子并将二添加到总数中。但是如果我只想掷一个骰子或者添加一个负修饰符呢？也许我想用空格来表示骰子掷法，例如“3 d 6 + 2”？骰子掷法输入格式有各种排列组合，我的原始代码无法处理它们。

在此之前，让我们先谈谈 Cursor 的安装和设置。

## 安装 Cursor

这实际上非常简单。如果您使用的是 macOS 或 Windows，只需下载相关的安装程序文件，双击它，然后按照安装向导的指示操作即可。很简单。

对于 Linux，您需要下载所需的安装程序（例如 .deb 或 .rpm）。如果您的发行版设置正确，您可能会获得使用默认应用商店打开文件的选项。如果不是，请等待文件下载完成并运行安装命令，例如：

```bash
sudo dpkg -i cursor*.deb -y
suro ym install cursor*.rpm -y
```

安装完成后，您应该会在桌面菜单中找到 Cursor 启动器。启动应用程序，准备开始工作。

## 配置 Cursor

Cursor 开箱即用。事实上，我打开了我的 Python 项目，打开了智能体，输入了我的查询，然后让它自动处理。

但是，您可能需要进行一些配置。要访问设置，请单击主窗口右上角附近的齿轮图标。这将打开一个新选项卡，您将看到所有可用选项。

单击“Agents”选项卡，您可以自定义一些选项，例如：

*   默认模式 (Agent, 计划, 提问, 上次使用的模式)。
*   默认位置 (编辑器或窗格)。
*   文本大小 (小, 默认, 大, 超大)。
*   自动清除聊天 (启用/禁用)。
*   最大选项卡数量。
*   消息队列 (立即发送, 当前消息后发送, 停止并立即发送)。
*   使用情况摘要 (自动, 总是, 从不)。
*   自定义模式 (启用/禁用) — 此功能处于测试阶段。
*   以及更多。

接下来，您应该转到“Models”选项卡，在那里您可以启用或禁用您想要使用的任何/所有模型。在该选项卡底部，您还可以添加各种 API 密钥（如果需要），例如 [OpenAPI](https://thenewstack.io/openapi-initiative-new-standards-and-a-peek-at-the-roadmap/)、[Anthropic](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)、[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-foundry/models/openai/) 等。您还可以设置一个云智能体，这需要一个包含 Git 仓库的文件夹。

浏览完各种选项后，关闭“Settings”选项卡，您就可以开始了。

## 在我的 Python 项目上工作

打开项目（该项目保存在本地存储上）后，我首先运行了应用程序（通过单击编辑器窗格顶部附近的右向箭头），以确保应用程序仍然可以运行。当我尝试使用它时，我才想起为什么我想要修复输入格式，因为我最终遇到了一个错误。

项目打开后，我单击了右上角附近的“Agent”按钮（看起来像一个右上方箭头的图标），然后查询：

```
Using the current project, can you simplify the dice_notation format so it's more user-friendly?
```

这就是我所说的全部。

Cursor 然后让其智能体开始改进脚本。Cursor 花了大约两分钟解决了问题。以下是智能体报告它们所做的工作（图 2）：

*   简化了单骰子表示法：现在可以使用“d6”而不是“1d6”——它默认一个骰子。
*   允许空格：诸如“3 d 6 + 2”或“2d10 – 1”之类的格式现在有效（空格被忽略）。
*   不区分大小写：“3D6+2”与“3d6+2”的作用相同。
*   更好的错误消息：当格式无效时，提供更具描述性的错误。
*   更强大的解析：使用正则表达式进行更可靠的解析。

[![](https://cdn.thenewstack.io/media/2025/11/f08b0dfc-cursor2.jpg)](https://cdn.thenewstack.io/media/2025/11/f08b0dfc-cursor2.jpg)

*图 2：Cursor 智能体在改进我原始代码方面做得非常出色。*

然后我重新运行了 Python 应用程序，看看 Cursor 是否真的改进了脚本，结果确实如此。我可以输入多种骰子格式，并且它完美运行。

我可能需要一个多小时才能完成的工作，Cursor 只用了几分钟。

仅这一点就值回票价了。

说到价格……