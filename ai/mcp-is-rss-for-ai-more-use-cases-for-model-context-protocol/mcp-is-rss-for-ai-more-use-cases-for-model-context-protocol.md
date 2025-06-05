<!--
title: MCP是AI的RSS：模型上下文协议的更多用例
cover: https://cdn.thenewstack.io/media/2025/05/1f0dc7e7-steve-johnson-ujxqaehhzum-unsplashb.jpg
summary: 用AI赋能文档！文章揭秘`MCP`协议如何成为AI时代的`RSS`，通过`JSON-RPC`连接`LLM`与文档，实现`list`、`docs`、`search`、`examples`等功能，让AI像专家一样与文档对话，提升开发效率，测试文档有效性，构建人机协同的文档交互新模式！
-->

用AI赋能文档！文章揭秘`MCP`协议如何成为AI时代的`RSS`，通过`JSON-RPC`连接`LLM`与文档，实现`list`、`docs`、`search`、`examples`等功能，让AI像专家一样与文档对话，提升开发效率，测试文档有效性，构建人机协同的文档交互新模式！

> 译自：[MCP Is RSS for AI: More Use Cases for Model Context Protocol](https://thenewstack.io/mcp-is-rss-for-ai-more-use-cases-for-model-context-protocol/)
> 
> 作者：Jon Udell

和许多英语专业的学生一样，我的软件职业生涯始于技术作家。最近，一位年轻的朋友向我征求进入该行业的建议，我意识到，在经历了数十年的沉寂之后，软件文档现在变得前所未有的有趣。

这种情况已经存在一段时间了，因为 LLM 已经吸收了文档并使其更有用。[MCP](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 服务器对于文档语料库放大了这种好处。你可以把它想象成打了兴奋剂的 [llms.txt](https://llmstxt.org/)，一种作为注意力集中机制的站点地图。当我为我现在正在开发的软件开发工具构建 MCP 服务器时，我意识到 MCP 邀请我们探索人们与我们的东西（文档、源代码、示例）互动的方式与 LLM 互动的方式之间的协同作用。

说“我构建了一个 MCP”服务器可能听起来令人印象深刻，但其机制非常简单——这就是为什么我倾向于将 MCP 视为 AI 的 RSS。RSS 作为一种协议的美妙之处在于它的简单性。你可以手动编写 RSS feed，或者编写非常简单的代码来生成一个。编写 RSS 阅读器是许多初级程序员的入门项目。使用 MCP 的协议 [JSON-RPC](https://www.jsonrpc.org/) 并没有那么容易，但比使用 Fediverse 或 Bluesky 客户端和服务器所使用的协议要容易得多。

MCP 的快速普及不仅让我想起了 RSS，还让我想起了几十年前迅速结合在一起的其他一些东西。其中之一是 RSS 自动发现，它使浏览器能够了解站点的 RSS feed。仍然可以在 Wayback Machine 中找到 Mark Pilgrim 的 [Important change to the LINK tag](https://web.archive.org/web/20060709143418/https://diveintomark.org/archives/2002/06/02/important_change_to_the_link_tag)。

> 感谢过去几天一直在努力使这一切实现的所有人。它出乎意料地轻松且没有摩擦。我们共同提出了一个新的标准，该标准实用、优雅、具有前瞻性且得到广泛实施。在 4 天内。

打开纽约时报的首页，你可以看到它仍在发生。

```html
<link data-rh="true" rel="alternate" type="application/rss+xml" title="RSS" href="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml">
```

还有 [OpenSearch](https://github.com/dewitt/opensearch) 协议。你可以将类似这样的内容放到你的网站上：

```html
  My Site Search
  Search MySite.com
```

以及一个 `<link rel="search"` 标签和浏览器支持，这意味着当你访问该站点时，浏览器会亮起*添加此搜索引擎*，并使你能够从一组主流和定制的搜索引擎中选择它。突然之间，使用这种原始形式的联合搜索变得微不足道。

我们倾向于认为只有在网络的早期才有可能实现这样的突破。看到它们仍然可以发生，令人耳目一新。

## 代理的途径

如果一切都失败了，老笑话说，阅读文档。我肯定不是唯一一个被这个笑话嘲笑的人。我会阅读一个关于软件工具的引人入胜的概述，但是当我尝试使用该工具时，我不想阅读参考文档，我想立即回答战术问题：

*   “是否有一个组件可以执行 [X]？”
*   “[X] 的文档对主题 [Y] 有什么说明？”
*   “源代码如何实现 [X]？”
*   “[X] 如何在实际项目中使用？”

我的 MCP 服务器的核心是一个像这样的 switch 语句：

```
case "list":
    toolName = "list_components"
case "docs":
    toolName = "component_docs"
    args["component"] = arg
case "search":
    toolName = "search"
    args["query"] = arg
case "examples":
    toolName = "examples"
    args["query"] = arg
```

这种结构使代理能够回答此类问题。要弄清楚是否有组件可以执行 [X]，Claude 或 Cursor 或其他代理可以使用 `list_components` 工具（不带参数）来检索组件和描述的列表。如果代理在列表中发现了一个可能的候选者，则可以使用 `component_docs`，传递组件的名称，以检索该组件的文档。当被要求提供详细信息时，它可以使用 `search` 工具来扫描服务器提供的文档和源代码，并使用 `examples` 工具来查找组件 [X] 和与主题 [Y] 相关的其他材料的用法。

> 编写软件文档将受益于与编写代码相同方式的测试。现在我们可以测试文档是否真的有效。

当我“构建”服务器时——加上引号是因为，当然，我只是指示 Claude 为我构建它——我在扩展我们工具的文档和创建示例应用程序的过程中，立即变得更有效率。在[代码与上下文：AI 如何帮助改进我们的文档](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)中，我写了一个顿悟：编写软件文档将受益于与编写代码相同的方式进行测试。现在我们可以测试文档是否真的有效。当读取了文档的 LLM 无法回答我们期望文档应该回答的问题时，这可能是一个 LLM 错误，但更可能是一个文档错误。我们可以改进文档并测试这是否修复了该错误。

通过让 LLM 原始访问文档，这个奇迹已经成为可能。借助 MCP，我们可以创建路径来引导 LLM 进行更富有成效的交互。

## 为什么要构建 MCP 客户端？

MCP 的简单性意味着，就像 RSS 自动发现和 OpenSearch 一样，它是一种可以快速流行并提供强大杠杆作用的东西。因为 MCP 通过 stdio 管道传输 JSON-RPC，所以您只需将命令回显到服务器即可与服务器通信，这就是我一直希望与简单协议交互的方式，以便理解它们的工作原理。在实践中，我发现 JSON-RPC-over-stdio 对于这种方法有点挑战性，所以我为我的服务器“构建”了一个客户端。这是一个令人愉快的提醒，它让我想起了另一个更古老的东西：The gopher。

```
Available commands:
  list              - List all components
  docs        - Docs for a component
  search      - Search code/docs
  examples   - Search usage examples
  quit              - Quit
```

虽然我可以观察 Claude 和 Cursor 与我的服务器交互，并评估如何调整它以改善流程，但进入他们的角色并以与他们相同的方式与我的服务器交谈是一种强大的体验。

我认为我接下来要添加到服务器工具包中的是 `topic` 工具，该工具专注于我们的用户需要理解的概念。长期以来，我们一直试图主要为了阅读文档的人的利益而构建文档，其次是为了机器的利益。人们很容易认为，随着情况的转变，机器成为主要的读者，结构变得不那么重要。只需确保您拥有必要的原材料，将它们全部放入存储桶中，然后让 AI 弄清楚即可。在某种程度上，他们会的。但是，构建机器与我们的文档之间的交互可以增强它们使用文档的能力。令人高兴的是，这正是人们也想要的互动。

## 不仅要阅读文档，还要与文档对话

我们大多不想阅读文档，但我们确实想与它们对话。当我们为文档构建搜索界面时，我们一直试图预测搜索意图。人们不仅仅是在寻找单词；他们需要使用这些材料来解决问题并完成工作。当您创建 MCP 服务器时，您将被迫明确这些搜索意图。这对我们和机器人一样有用，并且将帮助我们更有效地与它们合作。