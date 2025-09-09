
<!--
title: AI被困在1996？打破现状，通向未来！
cover: https://cdn.thenewstack.io/media/2025/09/b0b8b8f1-future.jpg
summary: 人工智能发展面临挑战，如工具选择和系统通信。RAG架构在企业中普及，但AI代理正崭露头角，构建代理仍具难度。向量数据库选择及文本向量化过程复杂。未来多代理系统协同工作是发展方向，目标是简化AI开发。
-->

人工智能发展面临挑战，如工具选择和系统通信。RAG架构在企业中普及，但AI代理正崭露头角，构建代理仍具难度。向量数据库选择及文本向量化过程复杂。未来多代理系统协同工作是发展方向，目标是简化AI开发。

> 译自：[AI Development Is Stuck in 1996. Here's How to Get to the Future.](https://thenewstack.io/ai-development-is-stuck-in-1996-heres-how-to-get-to-the-future/)
> 
> 作者：Pete Johnson

通往人工智能未来的道路上发生了一件有趣的事情。我们正深陷于困扰我们几十年的老问题中。你可能会认为，有了关于大型语言模型（LLMs）的所有讨论以及一个美好新世界的承诺，我们已经解决了这些问题。但事实是，变化越多，就越停留在原地。我们仍然在努力解决一些基本问题，例如选择正确的工具并确保我们的系统可以相互通信。

人工智能的景象很像互联网的早期。早在1996年，构建网站是一个痛苦的手动过程，充满了硬编码的HTML和笨拙的CGI-BIN脚本，用来处理像支持文档提交这样简单的事情。直到那年年底才有CSS。没有集成框架或技术栈来简化这个过程。一切都是你必须从头开始解决的难题。

今天，我们有像[MEAN这样的技术栈](https://thenewstack.io/the-evolution-of-the-ai-stack-from-foundations-to-agents/)（MongoDB、[Express.js](https://thenewstack.io/a-showdown-between-express-js-and-fastify-web-app-frameworks/)、[Angular](https://thenewstack.io/angular-vs-react-how-to-choose-the-right-framework-for-you/)、[Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/)），让Web开发变得轻而易举。我们正在人工智能开发中看到类似的演变，特别是在[检索增强生成（RAG）](https://thenewstack.io/no-mcp-hasnt-killed-rag-in-fact-theyre-complementary/)和[AI代理](https://thenewstack.io/23-of-devs-regularly-use-ai-agents-per-stack-overflow-survey/)方面。

## AI 采用曲线和 RAG 的兴起

根据世界经济论坛和埃森哲联合发布的[2025 年报告](https://reports.weforum.org/docs/WEF_Transforming_Consumer_Industries_in_the_Age_of_AI_2025.pdf)，70% 的组织正处于 AI 采用曲线的“实验和试点”阶段，运行着多个通常与其核心业务战略脱节的 AI 实验。一小部分领导者（约 10-15%）已经开始通过在营销或客户服务等特定业务领域大规模部署 AI 来看到可衡量的价值。好消息是，早期的 AI 采用者已经看到了好处，自 2019 年以来，一些公司的收入增长了 18%。最成功的公司（被归类为“AI 未来构建”的公司）在三年平均水平上实现了 50% 的收入增长和 60% 的股东总回报增长。

在 2024 年，企业中生成式 AI 的主要架构方法是 RAG。[RAG 的使用量](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/)从 2023 年到 2024 年增长了 1.6 倍。虽然提示工程是 2023 年的主要方法，但其使用量直线下降。与此同时，根据 market.us 的数据，RAG 市场预计到 2034 年将增长到惊人的 745 亿美元，复合年增长率为 49.9%。

## 主动转向及其挑战

虽然 RAG 很受欢迎，但 AI 代理正开始作为一种新方法出现。LangChain 在 2024 年 12 月进行的一项[调查](https://www.langchain.com/stateofaiagents)发现，超过一半的公司 (51.1%) 已经将代理投入生产，甚至有更大比例 (78.1%) 的公司正在积极开发代理并计划部署它。代理最适合执行研究和总结 (58.2%)、个人助理 (53.5%) 和客户服务 (45.8%) 等任务。

但关键是：构建代理很难。这很像 Web 开发的早期。你面临着令人眼花缭乱的选择，而错误的选择可能会让你陷入复杂性和挫败感的泥潭。你需要做出的选择包括：

* **选择框架**。你是选择像 LangChain、LlamaIndex 或 CrewAI 这样的独立于供应商的框架，还是选择像 Azure AI Foundry Agent Service 这样特定于供应商的框架？
* **选择 LLM 以及在哪里托管它**。选择范围很广，OpenAI、Anthropic、Google 和 Meta 等公司都在争夺市场份额。与 2024 年全年相比，企业在 2025 年前六个月的[基础模型 API 支出](https://menlovc.com/perspective/2025-mid-year-llm-market-update/)增加了一倍多。在切换 LLM 时，最大的触发因素是性能 (61%) 和所有权成本 (36%)。
* **选择向量数据库**。这是另一个关键的决定。截至 2024 年 6 月，PostgreSQL 和 MongoDB 是[最常用的两个向量数据库](https://retool.com/blog/state-of-ai-h1-2024)，使用率分别为 21.3% 和 21.1%。

## 未见的复杂性：向量和嵌入

即使在你做出这些选择之后，你仍然会遇到 RAG 和主动开发的细微之处。将文本、图像或音频等非结构化数据转换为称为向量的数字表示形式的过程充满了挑战。这是一个复杂的过程，你所做的选择可能会影响存储空间和检索质量。你必须考虑以下事项：

* **块大小**：你嵌入的内容片段有多大？
* **相似度函数**：你如何衡量两个向量的接近程度？
* **维度**：你的嵌入模型输出多少个向量？
* **量化**：你是将向量存储为浮点数、整数还是二进制数组？
* **重新排序**：你如何对检索到的文本进行排序？

## 前进的道路

好消息是，我们已经看到了使 Web 开发变得如此轻松的创新。例如，MongoDB 正在通过帮助管理一些技术细节来简化 RAG 的复杂过程。具体来说，它引入了解决分块、维度、量化和重新排序的功能，从而简化了开发人员的工作。

正如我们从手动构建静态 HTML 页面转变为使用强大的集成 Web 技术栈一样，我们也在 AI 中看到了同样的转变。我们的目标是从每个 AI 项目都是困难的、定制构建的工作，转变为开发人员可以专注于构建能够交付真正价值的代理的世界。

未来是多代理系统，不同的代理，如“协调者”、“战略家”和“实用代理”协同工作以解决复杂的问题。“协调者”分配任务，“战略家”将目标转化为可操作的计划，“实用代理”自主执行基本任务。我们已经在 Claude Code 中看到了这一点，其中一个子代理团队协作构建了一个电影浏览 Web 应用程序。协调者代理制定了一个计划，后端和前端子代理协同工作以执行该计划，所有这些都在几分钟内完成。这种协作的、主动的方法是下一个前沿。

从空白屏幕到功能齐全的 AI 代理的旅程仍然有些坎坷，但工具正在迅速发展。我们正处于一个 AI 开发将像现代 Web 开发一样精简和易于访问的时代的风口浪尖。我的朋友们，这是一个值得构建的未来。