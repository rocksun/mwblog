<!--
title: Google的ADK是一个用于构建多智能体系统的新开源框架
cover: https://cdn.thenewstack.io/media/2025/04/95ee701a-img_0679-scaled.jpg
summary: 重磅！Google发布开源框架ADK，助力开发者低代码构建AI多智能体系统！支持Python，集成MCP协议，兼容Gemini、Vertex AI及Anthropic等200+模型。另有Agent Engine提供托管运行时，Agent Garden加速开发，对标LangChain/LangGraph、AutoGen，云原生AI迎来新选择！
-->

重磅！Google发布开源框架ADK，助力开发者低代码构建AI多智能体系统！支持Python，集成MCP协议，兼容Gemini、Vertex AI及Anthropic等200+模型。另有Agent Engine提供托管运行时，Agent Garden加速开发，对标LangChain/LangGraph、AutoGen，云原生AI迎来新选择！

> 译自：[Google’s ADK Is a New Open Source Framework for Building Multiagent Systems](https://thenewstack.io/googles-adk-is-a-new-open-source-framework-for-building-multiagent-systems/)
> 
> 作者：Frederic Lardinois

拉斯维加斯 - [Google](https://cloud.google.com/?utm_content=inline+mention) 今天发布了 Agent Development Kit (ADK)，这是一个用于构建[多智能体系统](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/)的新开源框架。这与 [Google Agentspace](https://cloud.google.com/products/agentspace) 使用的框架相同，后者是该公司用于在企业中构建 AI 代理的服务。

谷歌承诺，使用 ADK，开发人员将能够用不到 100 行代码构建一个 AI 代理。使用 ADK，开发人员可以协调他们的代理系统，并为各个代理创建防护栏。

其中一个有趣的方面是，谷歌指出，开发人员将能够“通过 ADK 独特的双向音频和视频流功能，以类似人类的对话方式”与他们的代理进行交互。这具体是什么样子还有待观察。谷歌承诺在 Next 上展示此功能的演示，一旦我们看到更多细节，我们将更新此报道。

ADK 目前仅支持 Python，今年晚些时候将推出更多语言。它还支持 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction)，以允许这些代理连接到来自第三方服务的数据。

虽然谷歌表示该框架已针对与其自己的 Gemini 模型和 Vertex AI 平台一起使用进行了优化，但 ADK 还支持来自 Anthropic、[Meta](https://about.meta.com/?utm_content=inline+mention)、Mistral AI、AI21 Labs、CAMB.AI 和 Qodo 等第三方提供商的 200 多个模型。

开发人员还可以选择他们想要部署这些代理的位置。谷歌自己的 Vertex AI 是这里的明显选择，但该框架支持任何容器化环境作为部署选项（包括谷歌自己的 Cloud Run）。

对于希望获得完全托管的运行时以在生产环境中部署其代理的企业，谷歌现在还提供 Agent Engine。Agent Engine 允许开发人员使用任何框架部署代理，无论是 ADK、LangGraph、Crew.ai 还是其他框架。

为了帮助开发人员入门，谷歌今天还推出了 Agent Garden。Agent Garden 具有预构建的代理模式和组件，可快速启动开发过程。

很多这些听起来可能很熟悉。[LangChain/LangGraph](https://www.langchain.com/) 当然已经成为构建代理系统的某种标准。[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 也以 [AutoGen](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/core-concepts/agent-and-multi-agent-application.html) 的形式提供了一个用于构建多智能体系统的开源框架。它也支持各种模型（包括谷歌的 Gemini 模型），但 Microsoft 对 AutoGen 的重点似乎更多在于连接专门代理集群以解决复杂问题，而谷歌的目标似乎是更通用的工具包。[Solo.io](https://solo.io?utm_content=inline+mention) 的 [Kagent](https://thenewstack.io/meet-kagent-open-source-framework-for-ai-agents-in-kubernetes/) 是一个在 Kubernetes 之上构建多智能体系统的框架，例如，它构建在 AutoGen 之上，并于 3 月推出。