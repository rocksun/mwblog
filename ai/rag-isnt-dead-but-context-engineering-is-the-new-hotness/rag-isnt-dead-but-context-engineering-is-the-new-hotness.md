<!--
title: RAG未死，上下文工程才是新热点
cover: https://cdn.thenewstack.io/media/2026/01/f3a072ec-amin-zabardast-torash0awyk-unsplashc.jpg
summary: RAG并非消亡，而是被重新定义为“上下文工程”。Contextual AI推出Agent Composer，赋能企业在多元数据源上构建代理，强调集中式、企业级的上下文状态管理，是提示工程的演进。
-->

RAG并非消亡，而是被重新定义为“上下文工程”。Contextual AI推出Agent Composer，赋能企业在多元数据源上构建代理，强调集中式、企业级的上下文状态管理，是提示工程的演进。

> 译自：[RAG isn’t dead, but context engineering is the new hotness](https://thenewstack.io/rag-isnt-dead-but-context-engineering-is-the-new-hotness/)
> 
> 作者：Richard MacManus

那么，RAG（检索增强生成）现在已经消亡了吗？去年五月，[我向Contextual AI的首席执行官](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/) Douwe Kiela 提出了这个问题，因为围绕MCP（模型上下文协议）的炒作日益高涨。两者都是大型语言模型的数据检索机制，但在过去一年中，[MCP已经占据了所有头条](https://thenewstack.io/ai-engineering-trends-in-2025-agents-mcp-and-vibe-coding/)。

事实是，RAG作为一个被开发者和AI工程师使用的术语已经逐渐淡出。即使是合著了[2020年学术论文](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)（该论文向世界介绍了RAG）的 Kiela 也承认，一个时髦的新术语已经取而代之。

“我认为人们现在将其重新命名为‘上下文工程’，它包括MCP和RAG，”他说。“我的意思是，RAG中的‘R’仅代表‘检索’。所以，我想我上次也说过，如果你使用MCP进行检索，那么它本质上就是RAG，对吧？”

RAG仍然是Contextual AI技术栈不可或缺的一部分——尽管其[文档](https://docs.contextual.ai/how-to-guides/platform)中有所提及，但其主页上已不再突出。无论如何，如果“上下文工程”现在是流行术语，那么Contextual AI选择了一个正确的公司名称。

## Agent Composer 发布

与其他许多AI公司一样，[Contextual AI](https://contextual.ai/)现在也全力投入到代理领域。本周，它推出了一款名为[Agent Composer](https://contextual.ai/blog/introducing-agent-composer)的新工具，该公司在新闻稿中将其描述为“管理上下文、强制实施防护措施并在多步骤工程工作流中保持代理可靠性的基础设施和编排层”。

Agent Composer加入了Contextual AI平台上可用的其他工具，Kiela将其描述为“上下文层”。

“所以你拥有语言模型，你拥有你的数据，”他解释说。“如果你是一家企业，你的数据无处不在，而且非常非常嘈杂，对吧？这些公司不会将所有数据整合到一个地方，因此你可以使用我们的平台连接所有这些不同的数据源。”

从所有这些数据源中，用户创建了Contextual AI所称的“数据存储”。Kiela说，Agent Composer的一部分功能是帮助企业在其数据存储之上构建代理。

如下方图表所示，Agent Composer包含了企业创建代理所需的所有组件：预构建模板、提示界面、可视化构建器、API等。

[![Contextual AI 平台](https://cdn.thenewstack.io/media/2026/01/b3be3b64-contextual-agent-composer.png)](https://cdn.thenewstack.io/media/2026/01/b3be3b64-contextual-agent-composer.png)

*Contextual AI 平台；图片由该公司提供。*

## Claude Code 和企业包装器

我注意到，像Claude Code和Cursor这样的AI编码工具在过去一年左右的时间里在企业中非常流行。据推测，许多企业开发者已经在使用这些工具创建自定义代理，那么Contextual AI的Agent Composer提供了哪些Claude Code等工具没有的功能呢？

“我想说，那些[AI编码工具]本质上是语言模型的‘线束’，” Kiela 回答道。“所以‘线束’是当前的一个流行词。我认为你可以将我们的平台视为创建‘自定义线束’的一种方式。你可以在我们的平台上基本构建自己的Cursor，或者运行自己的特定Claude Code实例，这样你就无需担心在本地运行，或者类似的事情。”

我认为他的意思是，Claude Code和Cursor是围绕AI模型的包装器，但它们通常通过命令行工具或桌面应用程序与开发人员的计算机绑定。Contextual允许企业创建自己的包装器，但它们是集中托管的——这带来了企业通常所需的安全和治理优势。

> “……你可以将我们的平台视为创建‘自定义线束’的一种方式。你可以在我们的平台上基本构建自己的Cursor，或者运行自己的特定Claude Code实例。”  
> **– Douwe Kiela，Contextual AI 首席执行官**

目前另一个大趋势是代理开发平台。[LangChain](https://www.langchain.com/)，或许是[最初的AI工程工具](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)，目前正在其主页上推广其名为LangSmith的“代理工程平台”。我问 Kiela，Contextual AI 与 LangSmith 这样的产品相比如何？

“我认为他们更侧重于低级开发者，以及我所称的更独立的开发者，”他回答道。“所以它更多是关于SaaS原型开发，他们有很多不同的选择。我认为我们更具倾向性，也更偏向企业级，所以我们真正专注于企业开发者和[这些]解决方案的用户。”

## 从提示工程到上下文工程

在AI开发时代，术语变化如此之快。那么“上下文工程”究竟意味着什么，尤其是在与AI代理相关的背景下？碰巧的是，Anthropic，也许是目前最时尚的AI开发公司，归功于Claude Code，[去年九月写了一篇解释性文章](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)。

Anthropic认为“上下文工程是提示工程的自然演进。”与[2022-2023年的旧时代](https://thenewstack.io/generative-ai-how-companies-are-using-and-scaling-ai-models/)向大型语言模型提供一系列提示不同，现在鼓励工程师管理“整个上下文状态（系统指令、工具、模型上下文协议（MCP）、外部数据、消息历史等）”。

“代理”这个术语本身存在问题，但大多数人同意它是一个循环运行的软件程序。根据Anthropic的说法，一个“循环运行的代理会生成越来越多可能与下一次推理相关的数据，并且这些信息必须循环地进行优化。” 这就是上下文工程的作用。

> “……在你想预处理多少信息 […] 和你想在查询时搜索多少信息之间，总是存在一个权衡。”  
> **– Kiela**

具体来说，Anthropic表示Claude Code对上下文工程采取了“即时”方法，这意味着它将“在运行时使用工具动态加载数据到上下文中。” 我问 Kiela，Contextual AI 是否也做类似的事情？

“是的，所以，这些解决方案大多都是即时的，”他说。“如果你稍微退一步看，在你想预处理多少信息（即当你摄取文档时）与你想在查询时搜索多少信息（即本质上的即时）之间，总是存在一个权衡。因此，这两种处理模式之间的正确权衡真正取决于你正在解决的问题。所以在某些情况下，如果你必须非常快，你可能希望进行更多的预处理。如果你有更多时间并且可以采用代理式方法，那么你可能不需要做那么多，因为你可以有多次尝试和各种不同的策略来获取答案。”

## 代理用例

那么，Contextual AI的客户目前正在实际实施哪些代理式解决方案呢？ Kiela 回答说，他的公司倾向于专注于“硬核工程”，例如半导体行业。

“所以在这方面，我们看到很多围绕通过访问所有内部知识来让工程师更快行动的吸引力，这有点像是解锁机构工程知识，”他说。

他们更受欢迎的用例之一是使用代理进行根本原因分析，[十一月的一篇博客文章](https://contextual.ai/blog/user-feedback-and-annotation)中描述了这一过程。

“所以这非常强大，”他继续说道。“它实际上是获取关于出现问题的日志转储或各种不同数据集，然后你需要分析根本原因是什么。你可以将其与内部文档，也许是现有的错误报告进行交叉引用。也许你想自动在你的代码库上打开一个修复它的PR。所以对此有很多兴趣。”

## 结论

总而言之，RAG并未消亡——它只是被重新命名为“上下文工程”了。

此外，很明显，代理时代的软件工程实践仍在不断发展。Contextual AI和Anthropic等公司为各种开发人员提供了调整代理循环的工具。

提示？那已经过时了。现在，正如Anthropic所说，重点在于管理“整个上下文状态”。