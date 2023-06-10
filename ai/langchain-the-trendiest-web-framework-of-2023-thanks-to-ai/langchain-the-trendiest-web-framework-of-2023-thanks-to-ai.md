# LangChain：2023 年最流行的 Web 框架，这要归功于 AI

翻译自 [LangChain: The Trendiest Web Framework of 2023, Thanks to AI](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 。

我们来看看 JavaScript 开发人员需要了解的关于 LangChain 的信息，LangChain 是由 Harrison Chase 创建的快速崛起的 LLM 应用程序框架。

![](https://cdn.thenewstack.io/media/2023/06/320ea731-harrison_chase_feature-1024x558.jpg)

LangChain 是一个用于在应用程序中使用大型语言模型（LLM）的编程框架。就像生成式 AI 中的所有内容一样，[该项目](https://python.langchain.com/en/latest/index.html)的发展速度非常快。它于 2022 年 10 月作为 Python 工具开始，然后在 2 月添加了 [TypeScript 支持](https://blog.langchain.dev/typescript-support/)。到四月，它[支持多种 JavaScript 环境](https://blog.langchain.dev/js-envs/)，包括 Node.js，浏览器，Cloudflare Workers，Vercel / Next.js，Deno 和 Supabase Edge Functions。

那么 JavaScript 开发人员（特别是）需要了解 LangChain 的哪些信息，以及一般使用 LLM 的信息？在这篇文章中，我们旨在通过分析 LangChain 创始人 Harrison Chase 最近的两个演讲来回答这个问题。

LangChain 最初是一个开源项目，但一旦 GitHub 星开始堆积，它就迅速被分[拆成一家初创公司](https://golden.com/wiki/LangChain-BYE5888)。对于 Harrison Chase 来说，这是一个迅速的崛起，他最近在 2017 年在哈佛大学学习，但现在是硅谷最热门的初创公司之一的首席执行官。本月早些时候，微软首席技术官 Kevin Scott 在他的 [Build 主题演讲](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)中向 Chase 进行了个人大声疾呼。

## 聊天应用程序风靡一时

不出所料，LangChain 目前的主要用例是在 LLM（特别是ChatGPT）之上构建基于聊天的应用程序。正如流行的 bytes.dev 通讯中的 Tyler McGinnis 对 LangChain 的[讽刺评论](https://bytes.dev/archives/191)，“人们永远不可能有足够的聊天界面。

在今年早些时候接受 Charles Frye [采访](https://www.youtube.com/watch?v=zaYTXQFR0_s)时，Chase 说，目前最好的用例是“通过你的文档聊天”。LangChain 提供了其他功能来增强应用程序的聊天体验，例如流式传输——在 LLM 上下文中，这[意味](https://blog.langchain.dev/streaming-support-in-langchain/)着按令牌返回 LLM 令牌的输出，而不是一次返回所有内容。

但是，Chase表示其他接口将迅速发展。

“从长远来看，可能有比聊天更好的用户体验，”他说。“但我认为目前这是当务之急，你可以超级轻松地站起来，不需要很多额外的工作。六个月后，我是否期望聊天成为最好的用户体验？应该不会。但我认为现在，你目前可以构建什么来提供价值，可能是[即聊天]。

鉴于使用 LLM 开发应用程序是一件新鲜事，像 LangChain 这样的初创公司一直在争先恐后地提出工具来帮助解决 LLM 的一些问题。例如，对于提示工程，Chase 表示，它仍然主要归结为开发人员的直觉，哪些提示效果更好。但 LangChain 今年引入了“追踪”等功能来帮助解决这个问题。

## 代理

LangChain 最近的功能之一是“[自定义代理](https://blog.langchain.dev/custom-agents/)”， Chase 在四月份在旧金山举行的 [Full Stack LLM 训练营](https://fullstackdeeplearning.com/llm-bootcamp/)中[谈到](https://youtu.be/DWUdGhRrv2c)了这一点。他将代理定义为一种“使用语言模型作为推理引擎”的方法，以[确定](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/chase-agents/)如何根据用户输入与外部世界进行交互。

![why use agents](https://cdn.thenewstack.io/media/2023/06/df136a43-hchase1.jpg)
*Harrison Chase 在 LLM 训练营。*

他举了一个与 SQL 数据库交互的例子，解释说通常你有一个自然语言查询，语言模型会将其转换为 SQL 查询。你可以执行该查询并将结果传递回语言模型，要求它根据原始问题进行综合，最终得到 Chase 所说的“ SQL 数据库周围的自然语言包装器”。

代理的作用是处理 Chase 称之为“边缘案例”的情况，这可能是(例如) LLM 在上述示例的任何时间产生的部分输出幻觉。

“你使用 LLM 作为代理来选择要使用的工具，以及该工具的输入，”他解释说。“那你...执行该操作，返回一个观察结果，然后将其反馈到语言模型中。然后你继续这样做，直到满足停止条件。

![Typical implementation](https://cdn.thenewstack.io/media/2023/06/16112940-hchase2.jpg)
*实现代理。*

一种流行的代理方法称为“React”。这与流行的同名 JavaScript 框架无关；这个版本的“ReAct”代表 Reason + Ac t。 Chase 表示，与其他形式的快速工程相比，此过程产生“更高质量，更可靠的结果”。

![ReAct](https://cdn.thenewstack.io/media/2023/06/0e967dac-hchase3-scaled.jpg)
*ReAct（不是 React）*

Chase 承认，代理“面临很多挑战”，“大多数代理目前还没有做好生产准备”。

## 内存问题

他列出的一些问题似乎是基本的计算机概念，但它们在 LLM 的背景下更具挑战性。例如，LLM通常没有长期记忆。正如 [Pinecone 教程](https://www.pinecone.io/learn/langchain-conversational-memory/)中所指出的，“默认情况下，LLM 是无状态的 - 这意味着每个传入的查询都是独立于其他交互进行处理的。

这是 LangChain 旨在帮助开发人员的一个领域，通过在处理 LL M的过程中添加内存等组件。事实上，在 JavaScript 和 TypeScript 中，LangChain 有两个与内存相关的方法： `loadMemoryVariables` 和 `saveContext` 。根据文档，第一种方法“用于从内存中检索数据（可选地使用当前输入值），第二种方法用于将数据存储在内存中。

Chase 谈到的另一种代理形式是 [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)，这是一种允许您配置和部署自主 AI 代理的软件程序。

他说:“ Auto-GPT 引入的事情之一就是代理和工具交互之间的长期记忆的概念——为此使用检索向量存储”，他指的是向量数据库。

## 新的 LAMP ？

显然，在使用 LLM 构建应用程序时，还有很多工作要做。在其 Build 主题演讲中，微软将 LangChain 归类为开发人员“ Copilot 技术堆栈”中“编排”层的一部分。在微软的系统中，编排包括提示工程和所谓的“元提示”。

微软有自己的工具 [Semantic Kernel](https://thenewstack.io/microsoft-semantic-kernel-for-ai-dev-a-chat-with-john-maeda/) ，它与 LangChain 类似。它还宣布了一个名为 Prompt Flow 的新工具，微软首席技术官 Kevin Scott 表示，这是“另一种实际上统一 LangChain 和语义内核的编排机制”。

同样值得注意的是 LangChain 名称中的 “chain” 一词，这表明它可以与其他工具进行互操作 - 不仅仅是各种LLM，还有其他开发框架。今年五月，[Cloudflare 宣布](https://blog.cloudflare.com/langchain-and-cloudflare/) LangChain 支持其 Workers 框架。

甚至还有一个涉及 LangChain 的新首字母缩略词：[OPL](https://towardsdatascience.com/building-llms-powered-apps-with-opl-stack-c1d31b17110f)，代表 OpenAI ， Pinecone 和 LangChain 。其灵感可能是 [LAMP 堆栈](https://webdevelopmenthistory.com/1995-mysql-lamp-stack/)（Linux，Apache，MySQL，PHP / Perl / Python），这是1990年代的关键部分，并导致了Web 2.0的出现。谁知道 OPL 是否会作为一个术语坚持下去——当然，它的组件并不都是开源的——但无论如何，这是一个很好的迹象，表明 LangChain 已经成为许多开发人员个人堆栈的重要组成部分。