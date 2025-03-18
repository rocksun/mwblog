<!--
title: 认识Kagent，Kubernetes 中AI Agent的开源框架
cover: https://cdn.thenewstack.io/media/2025/03/97083fee-kagent-icon-1-copy-2.png
summary: Solo.io开源Kagent，加速 Kubernetes 工作流！基于AutoGen，集成MCP，赋能 DevOps 和平台工程师。内置Argo、Helm、Istio工具，支持Grafana、Prometheus可观测性。通过声明式API和控制器构建AI Agent，实现自动化配置、故障排除和零信任安全。未来将集成OpenTelemetry，支持多Agent和LLM！
-->

Solo.io开源Kagent，加速 Kubernetes 工作流！基于AutoGen，集成MCP，赋能 DevOps 和平台工程师。内置Argo、Helm、Istio工具，支持Grafana、Prometheus可观测性。通过声明式API和控制器构建AI Agent，实现自动化配置、故障排除和零信任安全。未来将集成OpenTelemetry，支持多Agent和LLM！

> 译自：[Meet Kagent, Open Source Framework for AI Agents in Kubernetes](https://thenewstack.io/meet-kagent-open-source-framework-for-ai-agents-in-kubernetes/)
> 
> 作者：Heather Joslyn

云原生应用网络公司 [Solo.io](https://solo.io?utm_content=inline+mention) 今天宣布推出 kagent，这是一个新的开源框架，旨在帮助用户构建和运行 [AI agents](https://thenewstack.io/ai-agents/)，以加速 Kubernetes 工作流程。

[Kagent](https://kagent.dev/) 旨在为 [DevOps](https://thenewstack.io/devops/) 和 [平台工程师](https://thenewstack.io/platform-engineering/) 提供工具、资源和 AI agents，这些工具、资源和 AI agents 可以帮助自动化配置、故障排除、可观测性和网络安全等任务。

该框架通过构建在 [模型上下文协议 (MCP)](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 上的架构与其他云原生工具集成。MCP 由 Anthropic 于 11 月推出，旨在标准化 AI 模型与 API 的集成方式。

Kagent 构建在 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 的开源框架 [AutoGen](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/) 之上，拥有 [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) 开源许可证。

据 Solo.io 的开源高级主管 Lin Sun 称，该项目最初是针对客户问题的内部解决方案。

Sun 告诉 The New Stack：“我们有数百家客户正在运行我们的网关或网格解决方案。因此，当我们与这些客户合作时，我们有内部支持团队。他们是与这些客户合作的代表，他们帮助客户弄清楚云原生生态系统中什么是正确的解决方案？他们帮助客户解决一般问题以及特定领域的问题。”

去年秋天，飓风 Helene 对美国东南部造成破坏性影响后，Solo.io 的一家保险公司客户寻求帮助，此前该保险公司的客户开始尝试在线提交受损房屋的索赔。

“那个周末，我们的团队被叫来帮忙，因为生产方面出现了一些问题，我们正在努力进行故障排除，并试图找出 10 个网络跃点在哪里。以及该网络中心的问题在哪里？”

Solo.io 面向客户的工程师最终利用了他们的常驻专家（他们对 Istio、Envoy 等有更深入的了解）来帮助解决保险公司的问题。

Sun 说：“这就是为什么我们开始思考：当我们继续扩大公司规模时，我们如何才能提高工作效率？我们向列表中添加了更多客户。那么，我们如何更有效地利用我们的内部专业知识？

“我们一直在思考，我们如何才能真正克隆这些专家？这样我们就不必在这些关键情况下将他们拉进来，这样他们就可以度过一个平静的周末，或者他们可以专注于编写代码并专注于创新。”

## 社区的愿望清单

Sun 说，Solo.io 在开源项目的基础上构建其产品，并打算将 kagent 捐赠给 [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention)。如果发生这种情况，它将遵循该公司 11 月将流行的开源 API 网关 Gloo Gateway 捐赠给 CNCF 的做法。

该项目现在名为 [kgateway](https://kgateway.dev/)，本月被命名为 CNCF 官方沙箱项目。

Kagent 的初始版本包括 Argo、Helm、Istio 和 [Kubernetes](https://thenewstack.io/kubernetes/) 的工具，以及 Grafana 和 Prometheus [可观测性](https://thenewstack.io/observability/) 工具。它还包括一个云原生专家知识库，可以扩展到任何与 MCP 兼容的工具服务器。

该框架包括三个层：

- **工具：** AI agents 可以使用预定义的功能，包括精选的知识库、服务的可用性和性能指标、应用程序部署和生命周期的控制、平台管理和调试的实用程序以及应用程序安全防护。
- **Agents：** 可以计划和实施诸如用户应用程序新版本的金丝雀部署、为 Kubernetes 集群中的每个服务建立 [零信任安全](https://thenewstack.io/what-is-zero-trust-security/) 策略以及调试服务故障等任务的自治系统。
- **声明式 API 和控制器：** 这允许用户通过其 UI、CLI 和声明式配置来构建和运行 agents。

“我们希望 kagent 能够激发社区的灵感，”Sun 说。“我们用一些示例 Agent、一些工具以及与 Kubernetes 集成的框架来启动这个项目。然后，我们希望社区的其他成员可以帮助我们增强我们构建的内容，并帮助我们[向目录中添加更多 Agent](https://kagent.dev/tools)，从而极大地惠及整个生态系统。

“我设想的是，对于每个关键的 CNCF 项目或云原生项目，我们都应该在目录中有一个 Agent，这样当新用户进入云原生领域时，他们就可以拥有一个特定于项目的 Agent 在他们身边，他们甚至可以调用多个 Agent。”

Sun 有一个广泛的愿望清单。除了敦促用户尝试现有的工具和 Agent 并贡献改进之外，她还提出了其他想法。

“我们希望拥有一些追踪能力，并可能与 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 集成。我们希望为 kagent 提供更多指标。我们还希望拥有一个反馈系统。”

还有更多：“我们也很乐意添加多 Agent 支持。目前，作为初始发布的一部分，我们专注于单个 Agent，但该框架旨在支持多个 Agent。”

Sun 还希望添加对多个[大型语言模型](https://thenewstack.io/llm/)的支持。“目前，支持主要集中在 OpenAI 上，我们认为它是最好的大型语言模型之一。我们认为它也适用于其他大型语言模型。但我们只专注于测试。”

有兴趣为该项目做出贡献的开发人员可以通过 CNCF Slack 的 #kagent 频道进行联系。Sun 还鼓励大家在 4 月 1 日至 4 日举行的[KubeCon + CloudNativeCon Europe 2025](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上，到 Solo.io 的展位（S150 号）参观。