<!--
title: Qodo Aware：AI 编程助手的“第二大脑”
cover: https://cdn.thenewstack.io/media/2025/09/bddc11e3-shawn-day-znkhpagiolm-unsplash-scaled.jpg
summary: Qodo Aware 通过增强上下文感知能力，改进 AI 编码代理。它利用语义搜索、代码结构分析和代码差异分析等技术，超越了传统方法，并预处理数据以提高效率。Qodo 计划推出代码审查专家代理，并探索“审查开发体验”的新界面。
-->

Qodo Aware 通过增强上下文感知能力，改进 AI 编码代理。它利用语义搜索、代码结构分析和代码差异分析等技术，超越了传统方法，并预处理数据以提高效率。Qodo 计划推出代码审查专家代理，并探索“审查开发体验”的新界面。

> 译自：[Qodo Aware Is a 'Second Brain' for AI Coding Agents](https://thenewstack.io/qodo-aware-is-a-second-brain-for-ai-coding-agents/)
> 
> 作者：Frederic Lardinois

大多数 AI 编码代理在底层都使用类似的大型语言模型 (LLM)。 它们之间的区别在于它们的上下文工程。 早期，代理专注于将项目代码库的正确部分添加到其不断扩展的上下文窗口中，或者使用检索增强生成 (RAG)。 但这些技术有其局限性，而且由于它们只关注代码库，因此它们确实错过了工程师在 GitHub、[GitLab](https://about.gitlab.com/?utm_content=inline+mention) 和 Bitbucket 等工具中生成的许多额外上下文。

借助 [Qodo Aware](https://www.qodo.ai/products/qodo-aware/)，Qodo 旨在为几乎所有代理编码工具带来增强的上下文感知能力，无论该工具是 Qodo 本身还是像 Claude Code 这样的编码代理，后者可以通过模型上下文协议 (MCP) 服务器访问该服务。

Qodo Aware 具有三个主要代理。 第一个用于上下文检索，并使用语义搜索（如果需要，可以跨多个存储库）来查找给定任务的相关代码段。 第二个称为 Deep Research，顾名思义，它旨在通过分析代码结构来回答有关代码库的复杂查询。 第三个代理 Deep issues 专注于查看代码差异并分析重大更改。

[![](https://cdn.thenewstack.io/media/2025/09/baad05c7-qodo-aware.jpeg)](https://cdn.thenewstack.io/media/2025/09/baad05c7-qodo-aware.jpeg)

*图片来源：Qodo。*

还有一个免费的开源版本，[Open Aware](https://github.com/qodo-ai/open-aware)，它索引流行的开源库。

正如 Qodo 的 CEO 和联合创始人 [Itamar Friedman](https://www.linkedin.com/in/itamarf/) 告诉我的那样，当团队构建其代码质量代理时，它很快意识到仅访问代码库不足以获得最佳结果。 他认为，这些系统缺少的是一个“第二大脑”，所有上下文都可以在其中聚合和存储。

“问题是，我们需要对这 100 万个 [token] 上下文进行推理，所以这个想法是双重的。 首先，即使你想利用那个上下文，以有组织的方式重组上下文并将其提供给 LLM 也非常关键，”他说。 “仅仅将所有内容无组织地塞入上下文，与进行适当的提示工程（你说：嘿，这是代码。它与那个相关联。 这是与此相关的相关评论……）之间是有区别的。 第二件事：即使这样，你也想确保你提供的是最相关的上下文，而不是提供太多的上下文。”

[![](https://cdn.thenewstack.io/media/2025/09/30f8b913-qodo-aware-1.jpeg)](https://cdn.thenewstack.io/media/2025/09/30f8b913-qodo-aware-1.jpeg)

*图片来源：Qodo。*

代码本身是此上下文的基础，但 Qodo Aware 现在可以提取的是代码的由来，这可以添加有关错误如何产生的有用信息（以及如何修复它）。 例如，这可能封装在 GitHub 中有关 pull request 的讨论和其他元数据中。 [Friedman](https://www.linkedin.com/in/itamarf/) 承认并非所有这些讨论都发生在 pull request 中，因此该团队也在考虑随着时间的推移添加其他来源，包括电子邮件和聊天消息。

该团队做出的一个有趣的架构决策是，它会预处理所有上下文数据，从而使代理可以更快、更高效地召回此数据并将其用于任何给定的任务。 （[Friedman](https://www.linkedin.com/in/itamarf/) 将此比作训练 LLM。）

在 Qodo 的基准测试中，该系统结合使用了 [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP)、知识图谱和向量嵌入，在代码理解和检索准确性方面轻松击败了 OpenAI 的 Codex、Claude Code 和 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 Gemini CLI 等编码代理。

[![](https://cdn.thenewstack.io/media/2025/09/206b4982-qodo-benchmark.jpeg)](https://cdn.thenewstack.io/media/2025/09/206b4982-qodo-benchmark.jpeg)

*图片来源：Qodo。*

[Friedman](https://www.linkedin.com/in/itamarf/) 指出，他同意 Anthropic 的 CEO 和联合创始人 [Dario Amodei](https://www.linkedin.com/in/dario-amodei-3934934/) 以及 OpenAI 的 CEO [Sam Altman](https://x.com/sama) 的观点，即在几年后，绝大多数代码将由 AI 生成。 但是，为了能够信任此代码，重点必须放在质量和审查上，并且需要新一代工具才能做到这一点。 毫不奇怪，Qodo 计划推出其他专家代理来帮助进行代码审查。 他还认为，虽然终端和 IDE 可以很好地生成代码，但随着开发人员与代理的交互多于与代码本身的交互，用户界面范例将会发生变化。

他说：“有一种新的范例来决定这应该是什么样子 —— 这就是我们一直在努力的方向。” 在他看来，这意味着从集成的开发体验转变为他所谓的“审查开发体验”。 该公司计划在未来几个月内详细介绍这种新体验。