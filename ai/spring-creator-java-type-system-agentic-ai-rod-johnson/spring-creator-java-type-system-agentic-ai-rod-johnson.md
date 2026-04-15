<!--
title: Spring 创始人欲借助 Java 类型系统驯服智能体 AI
cover: https://cdn.thenewstack.io/media/2026/04/0a04cfe8-hj-project-2yigxg4wrjc-unsplash-1-1.jpg
summary: Spring 创始人 Rod Johnson 推出 JVM 智能体框架 Embabel。该框架利用 Java 强类型系统与 GOAP 算法，通过任务分解与输出验证，旨在为企业 AI 应用提供确定性。
-->

Spring 创始人 Rod Johnson 推出 JVM 智能体框架 Embabel。该框架利用 Java 强类型系统与 GOAP 算法，通过任务分解与输出验证，旨在为企业 AI 应用提供确定性。

> 译自：[Spring creator wants Java's type system to tame agentic AI](https://thenewstack.io/spring-creator-java-type-system-agentic-ai-rod-johnson/)
> 
> 作者：Darryl K. Taft

[Rod Johnson](https://github.com/johnsonr) 是 [Spring 框架](https://thenewstack.io/spring-framework-has-three-major-pitfalls-heres-what-to-do/)的创始人，他带着另一个开源项目回归了——这一次，他的目标是解决他所认为的企业级 AI 的核心问题：让大语言模型驱动的应用程序具备足够的预测性，从而能够真正运行业务。

Johnson 在上周微软 [JDConf](https://jdconf.com/) 开发者大会的现场演示中展示了 [Embabel](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014)，这是一个针对 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 的[智能体 AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) 框架。该框架采用 Apache 许可证，托管在 GitHub 上，并构建于 [Spring Boot](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/) 之上。这意味着熟悉企业级 Java Spring 生态系统的 Java 开发者应该能很快上手。

Johnson 开发 Embabel 的目标是证明 Java 在智能体系统（尤其是企业系统）方面的表现与基于 [Python](https://thenewstack.io/what-is-python/) 的同类产品一样好，甚至更好。

基于 Python 的智能体框架包括 [LangChain](https://www.langchain.com/) 和 [Crew.ai](https://crewai.com/)，而基于 Java 的智能体框架包括 Embabel、[JetBrains Koog](https://www.jetbrains.com/koog/)、[LangChain4j](https://docs.langchain4j.dev/) 和 [Crew4j](https://crew4j.com/)。

Java 运行时提供商 Azul Systems 的副首席技术官 [Simon Ritter](https://www.linkedin.com/in/siritter/) 告诉 *The New Stack*，此举可能有助于缩小智能体领域日益扩大的差距。

“我个人认为，Java 框架可用性的提高将有助于缩小 Python 和 Java 在 AI 智能体领域的使用差距，”Simon Ritter 说道。

“我决定看看构建智能体的理想框架是什么样子的，”Johnson 告诉 *The New Stack*，“我很快得出结论，对于我想做的事情，以及我认为能够释放现有业务价值的事情，[JVM](https://thenewstack.io/java-language-architect-brian-goetz-on-how-java-could-evolve/) [Java 虚拟机] 将是一个更好的选择……”

然而，Johnson 在他的 JDConf 主旨演讲中表示：“我并不一定主要将自己视为一个 Java 人。我将自己视为一个想要解决企业软件问题的人。在 21 世纪初，问题是如何利用 Java 提高生产力。在 20 世纪 20 年代中期，问题是如何利用生成式 AI 并将其与业务应用联系起来。”

## Embabel 的起源

Embabel 是一个用于构建[生成式 AI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 业务应用的 JVM 框架。Johnson 于 2025 年 5 月推出该项目，目前已有超过 5 名全职工程师参与开发，GitHub 星数超过 3000。

Johnson 表示，Embabel 构建在 Spring Boot 之上，使用 [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/) 编写，具有出色的 Java 互操作性。他告诉 *The New Stack*，这是一种开源技术，计划采用类似于 [SpringSource](https://en.wikipedia.org/wiki/Spring_(company)) 模式的商业实体。

行业分析公司 RedMonk 的联合创始人 [James Governor](https://redmonk.com/team/james-governor/) 在一篇[博文](https://redmonk.com/jgovernor/java-relevance-in-the-ai-era-agent-frameworks-emerge/)中写道：“随着分布式系统和云革命的到来，如此多的应用程序和系统，如此多的基础设施，都是用 Java 构建的，尽管出现了 [Go](https://thenewstack.io/introduction-to-go-programming-language/) 和 [Rust](https://thenewstack.io/rust-programming-language-guide/) 等新语言。认为 Java 不能很好地与 AI 配合的想法是毫无道理的。”

James Governor 在同一篇博文中讨论 Johnson 时写道：“他现在创建了 [Embabel](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014)，这是一个为 JVM 编写的强类型智能体框架。它旨在通过使用非 LLM 的模型，然后使用自主智能体生成映射到该计划的代码，为您的项目计划带来确定性。并非所有事情都由 LLM 决定。”

与此同时，在关于 [Java 26](https://thenewstack.io/java-26-performance-ai/)（上个月发布的最新 Java 版本）的简报中，前 Oracle 开发者关系副总裁 [Chad Arimura](https://www.linkedin.com/in/chadarimura/) 告诉 *The New Stack*，Java 26 支持 Embabel 的“原生智能体”特性。

## 确定性问题

Johnson 表示，他将企业级 AI 采用的核心挑战视为一个光谱。他指出，一端是像 OpenAI 的 ChatGPT 这样的东西，它强大且具有生成性，但没有哪个理智的组织会基于它来运行业务流程。另一端则是 Java 开发者几十年以来一直在编写的结构化、确定性代码。

Embabel 旨在回答的问题是，一个给定的应用程序应该落在该光谱的哪个位置，以及如何实现这一目标。

Johnson 的答案是分解。将大问题分解为离散的步骤。某些步骤作为普通代码运行，其他步骤则调用 [LLM](https://thenewstack.io/introduction-to-llms/)。这些 LLM 调用本身可以调用工具。在 Johnson 看来，将这些步骤以可预测、可审计的方式连接起来，是一个真正的智能体框架的核心工作。

他说，大多数框架通过两种方式之一处理这种连接：让 LLM 在运行时决定调用哪些工具，这牺牲了可预测性；或者使用预先定义的状态机，这是 Python 生态系统中 [LangGraph](https://www.langchain.com/langgraph) 采用的方法。Embabel 则两者都不采用。

Johnson 解释说，相反，它使用 GOAP（目标导向行动计划，Goal-Oriented Action Planning）——一种借鉴自游戏开发的非 LLM AI 路径搜索算法——通过强类型的 Java 方法在运行时动态选择执行路径。

“Java 能够且正在生成式 AI 领域进行创新，”Johnson 说道。

在去年的[一篇 Medium 文章](https://medium.com/@springrod/ai-for-your-gen-ai-how-and-why-embabel-plans-3930244218f6)中，Johnson 这样描述 GOAP：“GOAP 本质上是一种路径搜索算法。它可以找到从未被编程过的路径。然而，它是确定性的，它只能选择由显式添加到系统的单个动作（步骤）组成的路径。如果 GOAP 找到了路径，它可以解释为什么该路径是成本最低的有效路径。

“GOAP 基于事实寻找路径，这些事实表现为前置条件和后置条件。目标（对应于我们智能体流程的现实世界目标）具有前置条件。动作具有前置条件和预期的后置条件。因此，在给定状态和目标之间可以找到零条或多条动作链。”

## Java 的类型系统是一项特性

Johnson 宣传中的一个反复出现的主题是，Java 开发者拥有一项被低估的资产：他们的领域模型。Embabel 的构建就是为了利用这一点。他说，该框架原生理解结构化返回类型——Java records、POJO（普通 Java 对象）、Jakarta EE 验证注解。

当一个字段带有验证约束时，Embabel 会将该约束作为提示词（prompt）的一部分呈现给 LLM，这样模型在生成响应之前就知道有效的响应是什么样的。Johnson 说，如果响应未能通过验证，框架会进行循环反馈并告诉模型原因。

其效果是，LLM 成为了应用程序类型系统的参与者，而不是位于系统之外的黑匣子。“LLM 成为了应用程序的一部分，而不仅仅是一个与之交谈的端点，”他说道。

Embabel 还会自动向每个 LLM 提示词注入上下文信息，包括当前日期和时间以及所调用模型的知识截止日期——当驱动智能体的步骤需要做出时间敏感的决策时，这些细节至关重要。

## 模型选择作为设计原则

Embabel 开箱即用地支持多个 LLM 提供商，包括 OpenAI、Anthropic 和 Llama。Johnson 强调，模型选择应该是针对每个步骤的决策，而不是全局应用程序设置。他说，工作流中的不同步骤可能根据成本、延迟或功能要求而需要不同的模型。该框架可以方便地在单个步骤级别通过名称或角色指定模型。

Johnson 还指出，Embabel 处于比大多数智能体框架更高的抽象层级——与其说是低级编排库，不如说是他所谓的“智能体安全带（agent harness）”。这一定位包括了针对 [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) 和 GitHub Copilot 等编码智能体的集成点，允许基于 Embabel 的应用程序直接整合这些工具。

## 快速上手

Embabel 可在 github.com/embabel 获取。Johnson 还建议开发者关注他的 Medium 博客，以深入了解该框架的理念以及支撑其运行时行为的 GOAP 规划模型。