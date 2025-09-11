
<!--
title: Zed IDE 本地 AI 工作指南
cover: https://cdn.thenewstack.io/media/2025/09/81587bd6-tim-mossholder-qvwngmotbik-unsplash.jpg
summary: Zed 是一款下一代代码编辑器，旨在实现人与 AI 之间的高性能协作。它可以与本地大型语言模型 (LLM) 连接，例如 gpt-oss。安装 Ollama 并拉取 gpt-oss LLM 后，在 Zed 的默认设置中配置 Ollama 的 API URL，即可在 Zed 中使用本地 LLM。Zed 集成了 GPU 渲染、语言服务器协议等功能。尽管使用本地 LLM 时速度可能较慢，但 Zed 仍然是一款有趣的 IDE。
-->

Zed 是一款下一代代码编辑器，旨在实现人与 AI 之间的高性能协作。它可以与本地大型语言模型 (LLM) 连接，例如 gpt-oss。安装 Ollama 并拉取 gpt-oss LLM 后，在 Zed 的默认设置中配置 Ollama 的 API URL，即可在 Zed 中使用本地 LLM。Zed 集成了 GPU 渲染、语言服务器协议等功能。尽管使用本地 LLM 时速度可能较慢，但 Zed 仍然是一款有趣的 IDE。

> 译自：[How To Work With Local AI in the Zed IDE](https://thenewstack.io/how-to-work-with-local-ai-in-the-zed-ide/)
> 
> 作者：Jack Wallen

对于那些认为 AI 不仅是学习新 [编程语言](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/) 的好方法，而且还有助于改进代码的人来说，有一款 [IDE](https://thenewstack.io/best-open-source-ides/) 可能非常适合你。这款 IDE 就是 [Zed](https://zed.dev/)。

[Zed 的创建者](https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/) 称其为“一种下一代代码编辑器，旨在实现人与 AI 之间的高性能协作”。

我测试了几款包含 AI 支持的 IDE，虽然 Zed 可能没有其他一些 IDE 的庞大功能列表，但在 AI 集成方面，我认为它可以与其中最好的 IDE 相媲美。

Zed 是一款跨平台 IDE（目前仅适用于 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 和 macOS，Windows 版本即将推出），可以免费使用（仅供个人使用），或者 Pro 版本每月 20 美元。 两者之间的区别在于，免费版本每月只提供 50 个 Zed 托管的提示，2000 个已接受的编辑预测以及无限个带有 API 密钥的提示。 Pro 计划每月提供 500 个提示（超过 500 个后按使用量计费）、无限的编辑预测和社区支持。

Zed 的功能集包括 GPU 渲染、语言服务器协议、Tree-sitter、支持调试适配器协议的调试器、AI 辅助、[模型上下文协议 (MCP)](https://thenewstack.io/is-model-context-protocol-the-new-api/)、[Git 支持](https://thenewstack.io/need-to-know-git-start-here/)、多缓冲区编辑、远程开发以及与其他 Zed 用户或 AI 代理的实时协作编辑。 还有数百个扩展来扩展功能集。

对于许多人来说，最大的吸引力将是 AI 集成。 我决定将重点放在这里，并且特别专注于将 Zed 与本地 [大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms/) 连接起来。 我选择的本地 LLM 是 gpt-oss，它由本地安装的 [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 实例提供支持。

你如何实现这一点？ 令人惊讶的是，这很容易。

让我们一步一步地完成它。

## 你需要什么

为了实现这一点，你需要一台 Linux 或 macOS 机器以及互联网连接。 就是这样。 我将在 Pop!\_OS Linux 上演示该过程。 在 Linux 和 macOS 上使用 Zed 的唯一区别是安装过程。 对于 macOS，你只需从官方下载页面获取二进制安装程序，双击它并按照安装向导进行操作。

## 安装 Ollama

在我们开始安装 Zed 之前，你需要先安装 Ollama，然后拉取 gpt-oss LLM。 要安装 Ollama，请打开一个终端窗口并发出以下命令：

```
curl -fsSL https://ollama.com/install.sh | sh
```

安装完成后，你需要下载我们将与 Zed 一起使用的 LLM。 为此，请发出以下命令：

```
ollama pull gpt-oss:20b
```

拉取模型后，它就可以使用了。 你可以通过发出以下命令来测试它：

```
ollama run gpt-oss:20b
```

如果进入 Ollama 控制台，恭喜，gpt-oss:20b 已安装并准备就绪。 你可以使用以下命令退出提示符：

```
/exit
```

## 安装 Zed

正如我提到的，我将在 Pop!\_OS Linux 上安装 Zed，这可以通过以下命令完成：

```
curl -f https://zed.dev/install.sh | sh
```

上面的命令安装的是稳定版本。 如果你想要预览版本（比稳定版本提前一周收到更新），则命令是：

```
curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh
```

安装完成后，在桌面菜单中找到 Zed 并单击以启动。

## 将 Zed 与 Ollama 一起使用

首次打开 Zed 时，你需要确保在默认设置中配置 Ollama，可以从 Zed 窗口左上角的汉堡菜单访问默认设置。 从下拉菜单中，单击“默认设置”。

在结果页面中，单击搜索图标并在搜索字段中键入 language\_models。 按 Enter 键，它将带你进入设置中的正确部分。 请记住，Zed 设置在一个 JSON 文件中进行处理（图 1），你将编辑该文件。

[![](https://cdn.thenewstack.io/media/2025/09/7ef7d831-zedsettings.jpg)](https://cdn.thenewstack.io/media/2025/09/7ef7d831-zedsettings.jpg)

*图 1. Zed 中的默认设置文件。*

在该部分中，你应该看到一个类似于这样的条目：

```
},
"ollama": {
"api_url": "http://localhost:11434"
},
```

如果你没有看到该条目，请添加它。 并且如果你已将 Ollama 设置为使用不同的端口，请确保更改它。

你无需保存任何内容，因为任何更改都会自动保存。

关闭“默认设置”选项卡。

## 将你的本地 LLM 与 Zed 一起使用

从 Zed 主窗口中，单击右上角的 +，然后单击“新建线程”。 打开“新建线程”窗格时，查看右下角附近，你将看到一个 LLM 下拉列表，用于选择要使用的 LLM。 从该列表中，你应该看到列出了 gpt-oss。 选择该选项，你就完成了设置。 从正左侧的下拉列表中，确保已选择“写入”。

让我们让 Zed 编写一个 C++ Hello World 程序（图 2）。 为此，请输入查询：

*编写一个 C++ Hello World 应用程序*

[![](https://cdn.thenewstack.io/media/2025/09/22bd603f-zedcplus.jpg)](https://cdn.thenewstack.io/media/2025/09/22bd603f-zedcplus.jpg)

*图 2. Zed 成功创建了一个 C++ Hello World 应用程序。*

根据你的机器（它是否具有 GPU，有多少内核等），此过程可能需要一些时间。 我首先使用一个 [Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/) 程序测试了 Zed，该程序接受来自用户的输入并将输入写入文件。 该查询花费了大约五分钟才能完成。

是的，Zed 在使用本地 LLM 时可能会非常慢，但它确实有效并且效果很好。 我已经测试了它生成的所有应用程序，它们还没有让我失望。

你还可以打开自己的项目，从模型选择器左侧的下拉列表中选择“提问”，提出你的问题（例如“我的 Python 代码有什么问题？”），粘贴你的代码，然后按键盘上的 Enter 键。

我对 Zed 唯一的抱怨是它在使用本地 LLM 时速度太慢。 我已经使用过类似的工具，发现它们要快得多。 但是，如果你有 GPU 和功能强大的 CPU，你可能不会遇到同样的问题。

无论如何，我发现 Zed 是一款非常有趣的 IDE，可能对你有所帮助。