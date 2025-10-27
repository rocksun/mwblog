<!--
title: 云原生AI时代：开源，为何亟需MCP这类标准？
cover: https://cdn.thenewstack.io/media/2025/10/3c5041d3-argocd-mcp-logo-2.png
summary: 云原生与AI融合是未来趋势。Akuity捐赠Argo CD的MCP服务器，成为连接AI与基础设施的开源社区项目。开放标准和开源协作对AI基础设施至关重要，能加速创新。
-->

云原生与AI融合是未来趋势。Akuity捐赠Argo CD的MCP服务器，成为连接AI与基础设施的开源社区项目。开放标准和开源协作对AI基础设施至关重要，能加速创新。

> 译自：[Cloud Native and AI: Why Open Source Needs Standards Like MCP](https://thenewstack.io/cloud-native-and-ai-why-open-source-needs-standards-like-mcp/)
> 
> 作者：Alexander Matyushentsev

云原生技术在过去十年中致力于通过 [Kubernetes](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/) 和 [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) 扩展微服务。接下来的十年将围绕这些系统如何与人工智能协同工作。

今年早些时候，Argo Project 社区收到了一项重大贡献：由 [Akuity](https://akuity.io/) 捐赠的适用于 Argo CD 的 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 服务器，现作为社区项目进行维护。这表明，随着人工智能和云原生技术的融合，像 MCP 这样的开放标准与开源协作相结合变得至关重要。

## **为什么标准对人工智能和基础设施很重要**

云原生技术通过标准得以发展。[容器](https://thenewstack.io/introduction-to-containers/) 通过开放容器倡议 (OCI) 规范变得实用。服务网格通过互操作性获得了采用。GitOps 通过 [Argo CD 和 Flux](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux/) 等项目中的常见实践得以扩展。

人工智能正处于类似阶段。模型和代理功能强大，但将它们连接到部署平台、可观测性堆栈或安全扫描器等基础设施工具通常需要定制代码。

MCP 定义了一种统一的方式，使人工智能系统能够与这些工具连接。它充当了云原生环境中人工智能的通用适配器。

## **GitOps 示例：Argo CD 遇见 MCP**

GitOps 提供了一个实用示例。[Argo CD](https://thenewstack.io/survey-argocd-leaves-flux-and-other-gitops-platforms-behind/) 是最广泛使用的 GitOps 运算符，为数千家组织保持 Kubernetes 工作负载的同步和可靠。

过去，将人工智能添加到 GitOps 意味着构建定制集成。借助适用于 Argo CD 的新 MCP 服务器，AI 代理可以直接与核心工作流协同工作，例如检查状态、同步部署和拉取日志。这表明人工智能辅助操作如何减少手动工作并简化故障排除。

## **将 Argo CD MCP 服务器捐赠给社区**

要使 MCP 取得成功，项目需要在开放环境中开发。这就是为什么最初由 Akuity 工程师构建的 Argo CD MCP 服务器被捐赠给了 Argo Project 社区。它现在位于 [argoproj-labs/mcp-for-argocd](https://github.com/argoproj-labs/mcp-for-argocd) 之下，任何人都可以贡献力量。

该项目已经获得关注。用户正在测试它，提交功能请求并提交拉取请求。最初作为一项实验的项目，现在已成为一项由社区主导的努力，以实际方式连接人工智能和 GitOps。

## **超越 GitOps：一场更大的运动**

同样的理念适用于整个云原生技术栈。MCP 可以使 AI 代理能够：

*   查询可观测性工具中的指标或跟踪。
*   检查服务网格中的流量流或应用策略。
*   在安全扫描器中运行合规性检查。

在每种情况下，MCP 都降低了集成摩擦，并为实验创建了一个共享基础。企业受益于更快、更安全的采用。社区通过避免碎片化和加速创新而受益，就像 OCI 标准化容器所做的那样。

## **为什么开源是关键**

当社区开放协作时，云原生发展最快：共享代码、统一标准并共同解决问题。

Argo CD MCP 服务器的捐赠体现了这种方法。通过将项目置于社区所有权之下，其发展将由共同需求而非个别供应商的优先事项来指导。在云原生领域，开源不仅仅是一种许可模式，它是实现真正进步的方式。

## **展望未来**

MCP 尚处于早期阶段，但其发展轨迹似曾相识：

*   容器在 OCI 等标准出现后成为主流。
*   GitOps 之所以能够扩展，是因为 Argo CD 和 Flux 等项目凝聚了社区力量。
*   服务网格的采用在互操作性被优先考虑后加速。

基础设施中的人工智能很可能遵循同样的道路。开放标准和开源项目将使其变得安全、一致且可扩展。

## **社区呼吁**

MCP 的成功取决于社区实验。无论您是贡献者、操作员，还是仅仅对 Kubernetes 中的人工智能感到好奇，现在都是参与其中的时候了。

Argo CD MCP 服务器的捐赠是开源贡献如何加速进步的一个例子。通过使此类项目归社区所有，生态系统可以塑造人工智能和云原生融合的方式。

共享标准改变了我们构建和运行应用程序的方式。它们现在可以改变我们在人工智能时代操作应用程序的方式。社区驱动的方法，而非专有解决方案，将使这成为可能。