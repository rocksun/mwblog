
<!--
title: 不，MCP没有扼杀 RAG——事实上，它们是互补的
cover: https://cdn.thenewstack.io/media/2025/05/160e561e-aakash-dhage-xpmgpcdqboq-unsplashb.jpg
summary: RAG已死？Contextual AI认为不然！RAG与MCP互补，而非替代。RAG通过检索增强生成，MCP作为通信协议，简化Agent集成。Contextual AI提供RAG Agent、指令跟随重排序器及文档解析器等模块化产品，助力企业构建高效GenAI应用，支持A2A协议，实现Agent间通信。
-->

RAG已死？Contextual AI认为不然！RAG与MCP互补，而非替代。RAG通过检索增强生成，MCP作为通信协议，简化Agent集成。Contextual AI提供RAG Agent、指令跟随重排序器及文档解析器等模块化产品，助力企业构建高效GenAI应用，支持A2A协议，实现Agent间通信。

> 译自：[No, MCP Hasn’t Killed RAG — in Fact, They’re Complementary](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/)
> 
> 作者：Richard MacManus

RAG 已经过时了吗？这是 Contextual AI 的 CEO [Douwe Kiela](https://www.linkedin.com/in/douwekiela/) [最近提出](https://contextual.ai/blog/is-rag-dead-yet/)的一个半开玩笑的问题。Kiela 对 RAG（检索增强生成）颇有研究——他曾领导 Meta 团队在 [2020 年 5 月的一篇研究论文](https://arxiv.org/abs/2005.11401)中介绍了这项技术。

当然，Kiela 的帖子是对当前围绕[模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)（MCP）的炒作的回应，MCP（错误地）被吹捧为 [RAG](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) 的终结者。但正如 Kiela 在接受 The New Stack 采访时指出的那样，RAG 可以*与* MCP 结合使用——他自己基于 RAG 的公司 Contextual AI 经常这样做。

## RAG 代理之路

首先，Kiela 和他的 Meta 同事是如何发明 RAG 的？他告诉我，这可以追溯到他关于将语言扎根于真实世界背景的博士研究，后来在 Facebook AI Research 继续进行。在那里，他和他的团队探索了 AI 模型如何在不进行持续重新训练的情况下，与不断演变的真实信息（如 Wikipedia）保持一致。随着早期语言模型和向量数据库的出现，他们将两者结合起来：从向量数据库中检索（R），并通过语言模型生成（G）。这促成了 RAG 技术，使生成式 AI 能够参考外部知识。

“所以我认为这是一种非常直观的方式，使 GenAI（生成模型）可以在真实数据之上工作，而无需对其进行训练，”他说。

在 RAG 开始受到关注后，Kiela 决定离开 Meta，并在 2023 年初创办了自己的 RAG 公司。现在，Contextual AI 将自己定位为“构建准确、可扩展的 RAG 代理的最快方式”。

我问“RAG 代理”这个术语是否是最近添加的，因为目前围绕代理的炒作。Kiela 回答说，是的，代理的措辞是在 2024 年添加的。

“我们的系统的工作方式，我们以前称它们为应用程序，但这听起来有点被动，而在现代范式中真正使其发挥作用的是更加主动。所以这就是为什么它是一个代理。”

## RAG 工作流程范围：静态到代理

AI 代理通常被视为自主的[软件应用程序](https://thenewstack.io/how-to-build-rag-applications-using-model-context-protocol)——它们代表人类用户出去做事。那么，“RAG 代理”也主要是自主的吗？

Kiela 回答说，静态 RAG 工作流程和更高级的代理系统之间存在一个范围。他说，典型的 RAG 管道是一种静态代理：它计划检索策略，获取相关数据，重新排序结果，并将它们发送到经过 RAG 训练的基础语言模型以生成答案。虽然这在某种程度上是代理的——因为它决定是否以及如何检索——但它仍然是一个固定的过程。

相比之下，他继续说，一个完全代理的系统会在运行时动态生成可执行代码（如 Python），使其能够根据中间结果调整其检索和推理策略。这可以包括重新运行搜索或根据需要调整其方法。Kiela 认为，关键的创新不是自主性，而是在测试时进行主动推理——他称之为“测试时计算”。

“围绕它有很多炒作，”他在 2025 年谈到代理系统时说。“很多人都在说，‘哦，它必须是活跃的，并且正在采取行动，或者它是自主的，或者……’但真正重要的是它能积极地推理。”

我请他澄清他所说的“积极推理”是什么意思，他回答说，代理正在“思考，我现在需要做什么？”

## RAG 和 MCP

正如[代理系统](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/)今年非常流行一样，MCP 也是如此。但有时人们谈论 MCP 好像它是 RAG 的*替代品*。因此，让我们回顾一下定义。

在他的“RAG 已经过时了吗？”帖子中，Kiela 将 RAG 定义如下：

“简而言之，RAG 通过从语言模型未接受训练的数据源中检索相关信息并将其注入到模型的上下文中来扩展语言模型的知识库。”

至于 MCP（中间的字母代表“上下文”），根据 [Anthropic 的文档](https://modelcontextprotocol.io/introduction)，它“提供了一种将 AI 模型连接到不同数据源和工具的标准化方式。”
这定义不是一样的吗？根据 Kiela 的说法并非如此。在他的文章中，他认为 MCP 是对 RAG 和其他 AI 工具的补充：“MCP 简化了 Agent 与 RAG 系统（和其他工具）的集成。”

> MCP “并不像很多人认为的那么具有革命性”。
>
> – Douwe Kiela, Contextual AI 的 CEO

在我们的对话中，Kiela 进一步补充了（清嗓子）背景信息。他解释说，MCP 是一种通信协议——类似于 API 的 REST 或 SOAP——基于 JSON-RPC。它使不同的组件（如检索器和生成器）能够使用相同的语言进行通信。他指出，MCP 本身不执行检索，它只是组件交互的通道。

“所以我想说，如果你有一个向量数据库，然后你通过 MCP 使其可用，然后让语言模型通过 MCP 使用它，那就是 RAG，”他继续说道。“所以基本上……你正在使用检索来增强生成器。所以那是 RAG。只是这两个部分相互通信的方式是通过 MCP，而不是你使用标准 RAG 的方式，后者只是将其更直接地放入上下文中。”

Kiela 补充说，MCP “并不像很多人认为的那么具有革命性，因为我们已经有了标准化的 API 通信——但它是一种很好、很简洁的方式。”

> “我们有自己的 MCP 服务器可用，因此人们可以通过 MCP 访问我们。”
>
> – Kiela

至于 Contextual AI 的客户，Kiela 表示，MCP 只是他们访问模型外部内容的方式之一。

“我们有自己的 MCP 服务器可用，因此人们可以通过 MCP 访问我们，”他说。“我们可以从我们的 Agent 调用 MCP。它不是标准方式，它只是我们可以与这些系统交互的方式之一。”

然后我询问了 Agent2Agent (A2A)，这是 Google 开发的允许 Agent 相互通信的开放协议。Kiela 回复说，Contextual AI 是 Google 的合作伙伴之一，因此他们也支持 A2A。

“所以我认为这是一个很棒的主意。它基本上高了一个层次，对吧。所以，MCP 用于：Agent 如何使用工具？然后 A2A 更多的是：Agent 如何与 Agent 对话？”

## RAG，RAG，以及更多的 RAG

最终，Contextual AI 是一家专注于将 RAG 技术以各种形式引入企业的公司。今年 MCP 的突然出现似乎使该公司进入了一种防御模式——或者至少是解释性的，因为它不得不解释为什么 MCP 不能替代 RAG。

除此之外，Contextual AI 拥有大量的 RAG 产品——例如 3 月份发布的[指令跟随重排序器](https://contextual.ai/blog/introducing-instruction-following-reranker/)，以及本月刚刚发布的新的 [RAG 文档解析器](https://contextual.ai/blog/document-parser-for-rag/)。Kiela 说，像这样的产品使他们的平台更加模块化。

他说：“你可以使用我们有主见的 API 来进行开箱即用的 RAG，但你也可以使用各个组件来改进你现有的 RAG 管道。”