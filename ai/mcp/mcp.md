
<!--
title: MCP 协议：一种新型 AI 开发工具构建块
cover: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd73b881-864c-495a-9e99-722fbd76a4a3_2034x1566.png
summary: AI编码提速！Anthropic推出MCP协议，如AI应用“USB-C”，连接LLM与IDE，实现数据库、工单系统互联。VS Code、GitHub等迅速采用，赋能Cursor等AI工具。LSP是MCP灵感来源，但安全威胁需关注，未来或可连接Figma、3D打印机等，云原生AI开发潜力无限。
-->

AI编码提速！Anthropic推出MCP协议，如AI应用“USB-C”，连接LLM与IDE，实现数据库、工单系统互联。VS Code、GitHub等迅速采用，赋能Cursor等AI工具。LSP是MCP灵感来源，但安全威胁需关注，未来或可连接Figma、3D打印机等，云原生AI开发潜力无限。

> 译自：[MCP Protocol: a new AI dev tools building block](https://newsletter.pragmaticengineer.com/p/mcp)
> 
> 作者：Gergely Orosz



# MCP 协议：一种新型 AI 开发工具构建块

### 扩展 IDE 的 AI 功能的模型上下文协议正迅速普及。 为什么会这样，我们开发者为什么要关注它？

*在我们开始之前：这是“你的技术栈里有什么？”调查的最后一周。 如果您尚未填写，请填写此调查并告诉我们。 如果您参与并填写调查，您将提前收到完整的结果，以及我和 Elin 提供的一些额外的独家分析。 （完整的结果，减去独家分析，将在 The Pragmatic Engineer 中发布）。 填写只需 5 分钟——感谢您的帮助！*

AI 编码工具和开发者工具交叉领域的一个热门话题是 MCP 协议（模型上下文协议），由 Anthropic 于 2024 年 11 月[推出](https://www.anthropic.com/news/model-context-protocol)。 它已迅速普及，AI 模型和开发者工具都渴望添加对其的支持。

MCP 的一个类比是，它就像“AI 应用程序的 USB-C 端口”，因为它为 LLM 和开发者工具相互连接创建了一个通用的扩展点；数据库、票务系统等。 这个概念在其他领域也越来越受欢迎，但 MCP 最初是一种扩展开发者 IDE（如 Claude Desktop、Claude Code、VS Code、Cursor、Windsurf 等）功能的方式。 今天，我们专注于这个领域，涵盖：

**什么是 MCP？ 一个实际的例子**。 以前，我使用单独的工具来查询生产应用程序中的数据库。 但是有了 MCP，我可以从 IDE“与”我的数据库“对话”，这感觉像是一个游戏规则改变者！

**MCP 的起源**。 Anthropic 的两位工程师 – David Soria Parra 和 Justin Spahr-Summers – 解决了让 Claude Desktop 更好地与开发者工具配合使用的问题。

**理解语言服务器协议 (LSP) 以理解 MCP**。 MCP 的许多核心思想来自 Microsoft 使 IDE 更容易添加编程语言支持的方法。

**MCP 架构**。 客户端和服务器，其中服务器通常是在本地运行的进程。

**MCP 服务器源代码内部**。 一个简单的本地 MCP 服务器如何帮助我们理解它的工作原理。

**安全威胁**。 目前的 MCP 实现方式对安全的保护看起来非常脆弱，攻击者可能会抓住机会获取 SSH 密钥和其他私有凭据，本地 MCP 服务器可以轻松地未经授权访问这些凭据。 这一领域需要尽快改进。

**未来主义用例**。 将 Figma 与 VS Code 连接，通过 Cursor 进行 3D 建模，以及从 Windsurf 控制 3D 打印机；所有这些都可以通过 MCP 实现。 此外：MCP 在 IDE 之外也获得了发展势头。

*对于这篇文章，我与 MCP 的联合创建者，Anthropic 的软件工程师 David Soria Parra 进行了交谈。 感谢您的投入！*

## 1. 什么是 MCP？ 一个实际的例子

我有一个 API，它为[这个微型网站](https://api.pragmaticengineer.com/kagi_and_perplexity)提供支持，年度付费会员可以在这里申请 12 个月的 Perplexity 免费访问权限和 3 个月的 Kagi 免费访问权限的促销代码。 该网站在 Node.js 上运行，使用 TypeScript，并使用 PostgreSQL 作为其数据库。

每当我调整后端或前端并修改数据时，我都会打开两件事：

*   我的 IDE，其中包含代码本身，以及 IDE 内的终端
*   数据库管理界面，用于查询表或修改架构（如果需要）。 我使用 PgAdmin。

IDE 正在通过 LLM 功能变得越来越智能； Windsurf 和 Cursor 具有代理功能，因此可以建议一次编辑多个文件。 但是，它们无法连接到我的 PostgreSQL 数据库来查询数据。 但是有了 MCP，它们就可以——我也是。

MCP 代表模型上下文协议，它是一座桥梁，允许 AI 增强型 IDE（如 Cursor、Windsurf 等）等 LLM 工具访问其他工具。

以下是我如何使用 LLM 提示使我的数据库在我的 IDE 内部可访问。 在此示例中，我使用了 Windsurf，但同样的操作也可以在 Cursor、Zed 和 VS Code 中完成。

#### 将 PostgreSQL MCP 服务器添加到我的 IDE

首先，在“设置”中的“Cascade”（Windsurf 的代理功能）下，我选择“添加 MCP 服务器”。 在这里，会显示一个带有预构建服务器的下拉列表：

添加它意味着配置到您的数据库的连接字符串，该字符串可以是运行在您机器上的本地 Postgres 数据库，也可以是远程数据库。 我使用远程连接字符串连接到我服务器上的数据库。 添加后，连接的数据库将显示为 MCP 服务器，随时可以使用：

接下来，对于输入到 Cascade 界面的任何命令，LLM 都可以决定使用此服务器。 让我从一个关于促销代码的问题开始：

“过去 10 天内有多少用户申领了 kagi 促销代码？”

LLM 尝试生成一个 SQL 服务器来获取答案，但虚构了表名（这对于 LLM 来说是很典型的）：

**但是，这才是“魔法”开始的地方，这要归功于 LLM 的更多迭代——使用它可以利用的这个新的数据库工具。** LLM 求助于我的 PostgreSQL 实例来查找正确的表名：
![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24913b96-1fa3-45f0-90b9-30d40cf17588_1600x707.png)

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24913b96-1fa3-45f0-90b9-30d40cf17588_1600x707.png)

然后它发出了另一个查询：

D’oh! – 列名又错了！但它查询了表定义并迅速纠正了它：

最后，它做对了：

令人印象深刻的是，这个过程只花了短短几秒钟，而且我根本不需要添加任何输入。LLM 通过访问数据库“弄清楚”了正确的表和列名。

#### PostgreSQL 之上的 LLM 层

现在我已经将我的数据库添加为 MCP 服务器，我可以使用自然语言“与”我的数据“对话”，LLM 会将自然语言转换为 SQL，然后再转换回我的问题。这不仅限于简单的 SQL 查询的简单问题，还包括更模糊的问题。

我问过的其他问题：

*   “过去两个月注册量是否出现异常高峰？”
*   “最近有哪些可疑的电子邮件注册？有什么规律吗？”
*   “哪些域名注册量最多？”
*   “还剩下多少未领取的促销代码？”

**能够通过我的 IDE 与开发工具进行对话，感觉就像“未来”。** 并不是说没有它我就找不到上述问题的答案；我*可以*编写 SQL 命令，或者一系列命令，或者一个循环命令的小程序，并对它们进行总结。但是，我可能不会费心，因为输入 SQL 需要时间。但因为我可以轻松地输入问题，所以我做了！

想想当你通过 IDE “与”你的开发者工具“对话”时会发生什么。例如，使用自然语言与以下工具交互：

*   源代码控制系统（“你能创建一个包含所有更改（除了 index.ts 中的更改）的拉取请求吗？”）
*   数据库（“你能创建一个新的注册日志表吗？使用增量计数器作为主键，并存储每个日志的时间戳”）
*   工单/缺陷跟踪系统（“是否有与此功能相关的缺陷？”）
*   可观测性提供商（“过去一周内，登录错误或注销错误是否出现任何高峰？”）
*   功能标志/实验系统（“哪些标志已经完全推出至少一周了？你能帮助识别这些标志并创建一个删除它们的 PR 吗？”）

能够从 IDE 中使用这些工具，可以使工作更轻松。此外，如果我们能使用它们，那么 AI 代理也能使用它们，这意味着它们可以完成更复杂的任务。

**在我看来，MCP 概念可能是提高开发者生产力的又一步。** 它也可能会提高 AI 代理的能力，因为它们拥有额外的工具来完成更复杂的任务。商业供应商很可能*会*争先恐后地添加 MCP 服务器，这将让客户可以更轻松地从 IDE 中使用工具。

作为开发者，我们将能够尝试使用各种工具来提高我们的生产力。*需要注意的是，MCP 仍处于早期阶段，缺乏经过审查的市场，IDE 对 MCP 的支持只有几个月的时间，而且 MCP 实现存在许多令人担忧的安全漏洞——在下面的“安全威胁”中介绍。*

## 2. MCP 的起源

MCP 协议由 Anthropic 的两位软件工程师 [David Soria Parra](https://www.linkedin.com/in/david-soria-parra-4a78b3a/) 和 [Justin Spahr-Summers](https://www.linkedin.com/in/jspahrsummers/) 构思和构建。David 在 [Latent Space 播客节目](https://www.latent.space/p/mcp) 中分享了起源故事。

“2024 年 7 月，我正在从事内部开发者工具的工作。当时有一项工作是授权 Anthropic 的更多员工能够真正深入地与我们的模型集成，并尽可能多地使用我们的模型。

从开发工具的背景来看，我很快就开始欣赏 Claude Desktop 的强大之处——它具有 Artifacts 等功能——但对其有限的功能集感到沮丧，而且无法扩展它。与此同时，我每天的工作都在 IDE 中进行。IDE 可以访问本地文件系统等内容，但没有像 Artifacts 或类似工具。

我一直在 Claude Desktop 和 IDE 之间来回复制内容，这让我感到沮丧。我认为我知道如何构建所有集成，但我需要做什么才能让这些 IDE 构建集成？

当你仔细观察时，你会发现“AI 集成”问题是一个 MxN 问题。你有 M 个应用程序（如 IDE）和 N 个集成。

在思考这个问题时，我正在从事一个

[Language Server Protocol](LSP) 内部项目——但这个项目没有取得任何进展。但将这些想法结合起来；一个 LSP，加上对 IDE 集成的沮丧，让它酝酿了几个星期，就产生了“让我们构建一些协议来解决它”的想法。”
关于 MCP 协议历史的更多信息，您可以收听[这个 Latent Space 播客节目](https://www.latent.space/p/mcp)。

#### MCP 协议的开源

David 与他的工程师同事 Justin 合作，构建了早期原型，不断迭代，并在六周后为 Claude Desktop 实现了第一个可用的 MCP 集成。

他们在内部共享了原型，Anthropic 的工程同事们对此感到兴奋。在准备开源该协议时，人们在 Anthropic 内部的黑客马拉松中构建了各种有趣的应用，包括一个控制 3D 打印机的 MCP 服务器。这证实了 David 和 Justin 的感觉，即 MCP 在现实世界中可能非常有用。

他们进行了更多的润色，并在去年 11 月 25 日[宣布](https://www.anthropic.com/news/model-context-protocol)了 MCP 协议的开源。当时，MCP 协议包括：

*   [一个网站](https://modelcontextprotocol.io/introduction)，概述了该协议；如何实现 MCP 服务器；以及客户端（如 IDE）如何集成该协议的指南
*   [该协议的规范](https://spec.modelcontextprotocol.io)本身
*   Python、TypeScript、Java、Kotlin 和 C# 的 [SDK](https://modelcontextprotocol.io/introduction)
*   [服务器和客户端实现的示例](https://modelcontextprotocol.io/examples)，供参考

#### 行业快速采用

在短短四个月内，MCP 从 Claude Desktop 使用的一个简洁协议，并被开源，发展到所有主要的 IDE，以及添加了 MCP 支持的 AI 工具，包括 OpenAI：

*   2024 年 7 月：Anthropic 内部开始开发 MCP
*   8 月：
*   2025 年 1 月：
*   2 月：
*   3 月：
*   4 月：

    *   **VS Code**[添加了](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) MCP 支持
    *   **GitHub** 发布了其[官方 MCP 服务器](https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/)(公开预览版)
    *   **Zapier**[发布了](https://zapier.com/blog/mcp/) MCP 服务器列表
    *   **CI/CD 服务，如** 和 [Bitrise](https://bitrise.io/blog/post/chat-with-your-builds-ci-and-more-introducing-the-bitrise-mcp-server)(CI/CD) 发布了他们的 MCP 服务器
    *   [CircleCI](https://github.com/CircleCI-Public/mcp-server-circleci)

目前唯一缺席的著名 IDE 是 JetBrains IDE，预计将在下一个 IDE 版本中[引入](https://www.reddit.com/r/Jetbrains/comments/1jqjqnw/someone_please_create_a_mcp_client_plugin/) MCP 支持，预计很快推出。在所有主要 IDE 中看到如此快速的采用是罕见的。显然，MCP 为使用 AI 工具的开发人员提供了很大的好处，因此 IDE 希望添加它。*巧合的是，工程师们最常提到的具有他们喜爱的 AI 功能的 IDE——Cursor、VS Code、Windsurf、Zed、Neovim 和 Cline——都是首批支持 MCP 的 IDE！*

但它们是如何工作的呢？

## 3. 了解 LSP 以了解 MCP

让我们稍微了解一下语言服务器协议的世界，因为这是启发 MCP 的解决方案。

几十年来，IDE 遇到的一个常见问题是，他们希望添加对尽可能多的编程语言的支持，这也意味着添加对以下内容的支持：

```text
Syntax highlighting

Code completion (autocomplete)

Marking of warnings / errors inline

Offering simple refactoring operations
```

假设有 M 个 IDE，以及 N 种编程语言，这是一个 MxN 问题。最简单的解决方案是让每个 M IDE 尽可能地为每种 N 语言构建手动支持。对于 IDE 供应商来说，这是一项繁重的工作，并且每当一种新的编程语言开始传播时，都必须重复这项工作：

对于我们开发人员来说，这意味着 IDE 仅很好地支持有限数量的语言。例如，祝您好运尝试在 Android Studio 中使用 C# 进行编码！

**扩展/插件** 是一种 IDE 完成繁重工作的变通方法：支持扩展/插件框架的 IDE 可以让第三方开发人员构建插件，例如特定语言的语法突出显示。这总比没有好，但对于开发人员来说是一项繁重的工作。此外，许多 IDE 不提供扩展功能，这些功能为自动完成和语法突出显示等功能提供令人愉悦的开发人员体验。
2016 年，微软发布了 **语言服务器协议 (LSP)** 规范，该协议最初是为 Visual Studio Code 开发的。其思想是，对于每种语言，LSP 服务器实现都可以提供语言功能。编辑器现在可以使用 LSP 服务器——一个现有的实现，通常是开源的——而不是构建自己的：

这改变了许多 IDE 的开发方式：

*   由于易于遵循的协议（LSP），新的和现有的 IDE 可以轻松地为新语言添加语言支持
*   对于大多数语言，都有语言维护者提供的官方 LSP 实现（例如
[gopls](https://github.com/golang/tools/tree/master/gopls)（用于 Go），通常开发者或 IDE 供应商可以选择多个 LSP 实现。例如，对于 C#，流行的 LSP 包括 [OmniSharp](https://www.OmniSharp/omnisharp-roslyn) 和 [csharp-ls](https://github.com/razzmatazz/csharp-language-server)。

如今，支持 LSP 的 IDE 包括：

**VS Code**：由于这一点，所有 VS Code 用户都喜欢

**Cursor**、**Windsurf** 等。
**Zed** 编辑器、**IntelliJ** IDE、**Eclipse**、Neovim、Emacs 以及许多其他小型编辑器，如 Atom、

[Helix Editor](https://helix-editor.com/)、[Kate](https://kate-editor.org/en-gb/) 等。

值得注意的缺失包括：

Visual Studio – Microsoft 的旗舰 IDE（不要与 VS Code 混淆）。使用专有的语言工具来支持语言。

XCode – 有一个官方的 Swift LSP Server，但 XCode 依赖于其专有的代码智能系统。

Android Studio：由于 IDE 基于 IntelliJ Community Edition，因此不支持 LSP，因此与完全成熟的 IntelliJ IDE 相比，支持的编程语言集更有限。

## 4. MCP 架构

David 和 Justin 从 LSP 的成功中吸取了以下经验：该协议允许：