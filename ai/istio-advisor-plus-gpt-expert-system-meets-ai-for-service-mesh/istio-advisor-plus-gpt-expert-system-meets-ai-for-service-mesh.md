<!--
title:当Istio智能顾问遇到GPT
cover: https://cdn.thenewstack.io/media/2023/12/7be7c338-isstio-chatgpt-1024x683.png
-->

智能技术与Istio文档巧妙结合，可极大地便利开发者解析这一热门开源Service Mesh的技术架构与实现机制。

> 译自 [Istio Advisor Plus GPT: Expert System Meets AI for Service Mesh](https://thenewstack.io/istio-advisor-plus-gpt-expert-system-meets-ai-for-service-mesh/)，作者 Steven J. Vaughan-Nichols ，也称 sjvn，自 CP/M-80 成为领先的 PC 操作系统，300bps 成为快速的互联网连接，WordStar 成为最先进的文字处理器以来，他一直在写有关技术及其商业的文章，我们很喜欢它。

还记得专家系统吗？计算机科学家爱德华·费根鲍姆(Edward Feigenbaum)因在 20 世纪 60 年代提出这个概念而出名。这个想法是通过在知识库的基础上构建一个基于规则的系统，通常用第一代人工智能(AI)语言 [Lisp](https://lisp-lang.org/) 编写，可以创建一个只有专家才能回答问题的系统。

虽然一些系统，比如 [Mycin](https://www.britannica.com/technology/MYCIN)，这是早期试图匹配药物与诊断的尝试，运行得很好，但它们被证明太慢太贵而无法成功。

那是过去。这是现在。

如今，诸如 OpenAI 的 [ChatGPT](https://chat.openai.com/) 之类的生成式 AI 程序既快速又便宜。这给了服务网格和网络公司 [Tetrate](https://tetrate.io/) 这样的想法：为 [Istio 服务网格](https://istio.io/latest/about/service-mesh/)创建一个基于 ChatGPT 的专家系统：[Istio Advisor Plus](https://chat.openai.com/g/g-pv9WQ7xgm-istio-advisor-plus)。

这个开源服务网格可帮助您运行分布式的基于微服务的应用程序。Istio 通常与 Kubernetes 一起使用，在 Envoy 服务代理的配合下建立可编程的、应用程序感知的网络。

Istio Advisor Plus 使用 [Python 前端](https://thenewstack.io/python-for-beginners-data-types/)、[OpenAI API](https://platform.openai.com/) 和 Tetrate 及其他云原生文档的数据，呈现一个精通 Istio 的专家系统。最后这一部分至关重要，因为如果放任自流，生成式 AI 系统[会幻想过度](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)。或者，我更愿意这么想，捏造事实。

然而，以真实信息武装，Istio Advisor Plus 可以(请鼓掌)

1. **解释 Istio 的概念和功能**:它详细解释了 Istio 的核心功能，包括流量管理、安全性、可观测性，以及这些概念如何应用于您的服务网格。
2. **指导 Istio 配置**:需要有关配置 Istio 组件(如网关、虚拟服务和目标规则)的建议吗？Istio 顾问 GPT 提供定制的指导，以适应您的具体使用案例。
3. **帮助解决 Istio 问题**:在遇到 Istio 问题时，这个 GPT 模型可以帮助诊断问题和提供解决方案。这包括解释错误消息、审查配置文件和推荐最佳实践。
4. **性能优化提示**:获取优化 Istio 服务网格性能的见解和策略，涵盖扩展、调优和高效利用资源等方面。
5. **最佳安全实践**:遵循[零信任安全](https://thenewstack.io/what-is-zero-trust-security/)原则在 Istio 中实施指导，确保您的服务网格安全。这包括相互 TLS、授权策略和保护入口/出口配置。
6. **流程的视觉表示**:Istio 顾问 GPT 可以使用 Mermaid 代码创建视觉图表，以表示复杂的网络或服务网格流程，使其更容易理解。
7. **升级 Istio 的帮助**:计划升级 Istio？这个 GPT 模型提供宝贵的指导，包括解决兼容性问题和有效利用新的功能。
8. **错误报告指南**:如果您在 Istio 中遇到潜在的错误，Istio 顾问 GPT 可以帮助您编制详细的错误报告，确保您提供所有必要的细节以进行有效的故障排除。这可以是一个很大的帮助。
9. **参考相关文档**:对于复杂的查询，这个 GPT 模型可以指导您参考 Istio 文档或其他相关资源的特定部分，以获得更深入的理解。
10. 关**于 Istio 生态系统工具的建议**:深入了解 Istio 生态系统中的工具和集成，例如 Prometheus、Grafana 和 Jaeger，并发现如何有效地使用它们。

当然，您可以通过查看文档来找到所有这些和更多信息。但是，与其在文档、FAQ 和论坛消息中搜索，这些信息可能更新也可能没有更新，不如让程序为您完成这项工作。

它还可以回答更复杂的问题。

例如，当我问“如何使用 Istio 和 Envoy 一起从 [Nginx 数据库](https://thenewstack.io/nginxs-reference-architecture-for-kubernetes-microservices/)拉取数据？”它回复我“应该将 Envoy 配置为与 Nginx 数据库通信的 Istio 服务网格中的服务的边车代理”。

它还为我的假设 Nginx 数据库给出了一个 Kubernetes 服务配置和一个 Istio 虚拟服务的示例。

然后它详细解释了在启用了 Istio 的 Kubernetes 集群中，我的每个需要与 Nginx 数据库通信的服务 Pod 中必须自动注入 Envoy 边车代理。并且，我需要为 Nginx 服务定义一个 Istio 虚拟服务和一个目标规则，使用[mutual TLS(mTLS)](https://tetrate.io/learn/what-is-mtls/)保护我的通信线路，并确保使用 Istio 和 Envoy 的遥测功能来监控和记录流量。

现在，这是一个简单的问题，但答案是准确的、切中要点的，我不需要在文档中找到它。不，它没有为我编写代码，但它帮助我理解正在发生的事情，让我得以明智地掌握整个情况。

与通用的 GPT-4 不同，它还为其答案提供了参考资料。虽然它们没有将我指向文档中的特定位置，但它们指向了它用于向我提供答案的来源。尽管如此，我真的很欣赏这一点。

听起来有趣吗？自己试一试。您需要 [ChatGPT Plus 订阅](https://openai.com/blog/chatgpt-plus)，这将为您提供最新版本的 OpenAI 大型语言模型(LLM)，即 GPT-4。

坦白说，我非常印象深刻。我可以认真地看到许多其他项目为其程序创建类似的专家系统。我们不得不面对，云原生计算既复杂又难以理解。有太多移动的部分。在我看来，任何可以帮助我们更快更轻松地适应这项技术的东西都是好事。
