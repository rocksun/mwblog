
<!--
title: JetBrains增强AI代码补全功能
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
-->

其他消息，Figma 推出了一个名为 Handoff 的新的开源项目，该项目可以自动将设计转换为代码。

> 译自 [JetBrains Improves AI Code Completion, OpenAI Boosts JSON](https://thenewstack.io/jetbrains-improves-ai-code-completion-openai-boosts-json/)，作者 Loraine Lawson。

[JetBrains](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/) 本周宣布了其年度 IDE 更新，并宣布其 [AI 助手](https://thenewstack.io/jetbrains-launches-new-ai-assistant-powered-by-multiple-llms/) 现在利用更新的 [大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) (LLM)，这意味着该助手可以为 [Java](https://thenewstack.io/how-to-protect-your-java-against-licensing-liability-risks/)、[Kotlin](https://thenewstack.io/angular-18-kotlins-new-compiler-astro-adds-react-19-support/) 和 [Python](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/) 提供更快的代码补全。

公司新闻稿中指出：“AI 聊天现在通过 GPT-4o 支持变得更加智能，并包含聊天参考以提供更好的上下文。新功能包括 AI 辅助 VCS 冲突解决、终端内命令生成以及可自定义的文档和单元测试提示。”

此外，此次更新还将新的 [JetBrains UI](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/)（旨在减少视觉复杂性并提供对基本功能的更轻松访问）设置为所有用户的默认界面。但是，对于那些不喜欢改变的人来说，经典 UI 仍然可以作为插件使用。

![JetBrains 新 UI 的截图](https://cdn.thenewstack.io/media/2024/08/90c82ae7-jetbrainsui.jpg)

*JetBrains 新 UI 的截图，[来自 JetBrains](https://blog.jetbrains.com/blog/2024/07/08/the-new-ui-becomes-the-default-in-2024-2/)。*

最后，搜索所有内容对话框现在允许开发人员预览他们正在搜索的代码库元素。JetBrains IDE 默认情况下会自动检测并使用开发人员机器上配置的系统代理设置。

除了这些新闻之外，一些 IDE 特定的更新包括：

- 改进的 [Jupyter 笔记本](https://thenewstack.io/jupyter-notebooks-the-web-based-dev-tool-youve-been-seeking/) 和新的 AI 单元，帮助在 PyCharm 2024.2 中更快地迭代数据分析工作负载；
- 新的 IDE 功能，例如“将方法添加到接口及其所有实现”重构，以及对最新 [Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/) 功能的支持，这些功能在 GoLand 2024.2 中可用。更新还包括性能改进、远程开发和开发容器的修复以及对 Go 框架的增强支持；以及 
- WebStorm 2024.2 支持针对具有基于文件系统的路由的框架（例如
[Next.js](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/)）的特殊路径解析，对 Bun 的初始调试支持，直接运行和调试 TypeScript 文件的能力，版本控制增强功能以及改善用户体验的功能。

## OpenAI 新功能确保输出与 JSON 模式匹配

[OpenAI 本周在 API 中引入了结构化输出](https://openai.com/index/introducing-structured-outputs-in-the-api/)，这是一项功能，可确保模型生成的输出完全匹配开发人员提供的 [JSON](https://thenewstack.io/no-cache/key-concepts-json/) 模式。

这是 OpenAI 去年在 DevDay 上推出 JSON 模式后的一项努力。JSON 模式提高了模型生成有效 JSON 输出的可靠性，但不能保证模型的响应符合特定模式。该公司在其博客中表示，API 中的结构化输出确保模型生成的输出将完全匹配开发人员提供的 JSON 模式。

OpenAI 解释说，从非结构化输入生成结构化数据是 AI 在应用程序中的核心用例之一。

“开发人员使用 OpenAI API 来构建功能强大的助手，这些助手能够通过函数调用（在新窗口中打开）获取数据并回答问题，提取结构化数据以进行数据输入，以及构建允许 LLM 采取行动的多步骤代理工作流程，”它指出。

但该团队指出，开发人员必须在 LLM 的限制内工作，使用开源工具、提示和重试请求来确保模型输出与与他们的系统互操作所需的格式匹配。

![图表显示了基于 JSON 模型生成方式的 OpenAI gpt 的可靠性](https://cdn.thenewstack.io/media/2024/08/d19938e3-openaichart.jpg)

*图表显示了基于 JSON 模型生成方式的 OpenAI gpt 的可靠性。截图来自 [OpenAI 的博客文章](https://openai.com/index/introducing-structured-outputs-in-the-api/)。*

“结构化输出通过约束 OpenAI 模型以匹配开发人员提供的模式，以及通过训练我们的模型更好地理解复杂的模式来解决这个问题，”它补充道。

结构化输出在 API 中包含两种形式：

1. 博客指出，“通过工具进行结构化输出的函数调用可以通过在函数定义中设置 `strict: true` 来实现。”当启用结构化输出时，模型输出将与提供的工具定义匹配。
2. 该帖子指出，“`response_format` 参数的新选项：开发人员现在可以通过 `json_schema`（`response_format` 参数的新选项）提供 JSON Schema。”“当模型不调用工具，而是以结构化方式响应用户时，这很有用。

帖子中概述了一些限制和约束，例如 [结构化输出仅允许使用 JSON Schema 的子集](https://platform.openai.com/docs/guides/structured-outputs)，这有助于 OpenAI 确保最佳性能。

## 新的开源工具将 Figma 设计转换为代码

Figma 推出了一个 [名为 Handoff 的新开源项目](https://www.figma.com/community/file/886892605736203125/handoff-components)，它为创作者和工程师提供了一种将 Figma 设计自动转换为代码的新方法。

Handoff 轻量级、与云无关，并根据 MIT 许可证为 [开源社区](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/) 构建。该公司表示，它可以提取、转换和分发 Figma 决策作为代码，弥合设计和开发之间的差距。其代码可以在 GitHub 上进行测试、改进或部署。

Handoff 基于 Figma 的 Rest API，可通过 [Figma Marketplace](https://www.figma.com/community/plugin/1376124565609689822/handoff) 获得。

