<!--
title: Kubernetes远程MCP架构：赋能LLM工具规模化
cover: https://cdn.thenewstack.io/media/2025/12/c7e43fad-remote123.jpeg
summary: 为解决本地LLM工具（MCP服务器）扩展性差的问题，文章提出在Kubernetes上远程部署工具，实现独立扩展、更新和可观测性，从而构建可靠的企业级AI系统。
-->

为解决本地LLM工具（MCP服务器）扩展性差的问题，文章提出在Kubernetes上远程部署工具，实现独立扩展、更新和可观测性，从而构建可靠的企业级AI系统。

> 译自：[Scale LLM Tools With a Remote MCP Architecture on Kubernetes](https://thenewstack.io/scale-llm-tools-with-a-remote-mcp-architecture-on-kubernetes/)
> 
> 作者：Nikhil Kassetty

随着人工智能系统从实验阶段走向生产阶段，开发人员开始发现一个新问题：[大型语言模型 (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) 所依赖的工具在单台笔记本电脑上运行时无法很好地扩展。早期的代理原型通常从一个简单的本地[模型上下文协议 (MCP)](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/) 服务器开始，这在探索想法时非常完美，但一旦有多个团队或实际工作负载介入，这些设置很快就会崩溃。

我在企业环境中构建 LLM 驱动的自动化时亲身体验了这一点。我们的早期 MCP 工具在演示期间运行 flawless，但当我们将其连接到实际工作流时，一切都变得脆弱。本地进程在没有日志的情况下崩溃，多个工程师无法共享同一个工具实例，版本更新破坏了工作流，我们也没有清晰的方法来推出新的工具功能。很明显，如果 MCP 要为生产系统提供支持，服务器需要远程运行，具备可扩展性，并有适当的隔离和可观测性。

这就是那些经验催生出的架构。它概述了一种实用且生产就绪的方法，用于在 [Kubernetes](https://thenewstack.io/kubernetes/) 上远程运行 MCP 服务器。该方法使用 Amazon Elastic Kubernetes Service (EKS)、Elastic Container Registry (ECR)、Docker 和[入口应用负载均衡器](https://thenewstack.io/deploy-a-multicluster-ingress-on-google-kubernetes-engine/) (ALB) 来创建一种可扩展的模式，将 LLM 客户端与 MCP 服务器分离。这种分离使得 MCP 工具可以独立于核心 LLM 工作流进行部署、更新、调试和扩展，这对于真实的生产 AI 系统至关重要。

## 架构概述

[![架构概述](https://cdn.thenewstack.io/media/2025/12/d3aae05e-image1-905x1024.png)](https://cdn.thenewstack.io/media/2025/12/d3aae05e-image1-905x1024.png)

该图展示了远程 MCP 设置的端到端流程。LLM 与 MCP 客户端通信，然后客户端与运行在 Kubernetes 集群内的远程 MCP 服务器交互。MCP 服务器被打包成存储在 ECR 中并部署在 EKS 上的容器镜像，而应用负载均衡器为外部流量提供了一个稳定且安全的入口点。

实际上，这种分离是我们将 MCP 工具从本地机器迁移出来时看到的最大的改进之一。一旦服务器远程运行，团队就可以在不中断彼此工作流的情况下更新工具，日志不再绑定到单台笔记本电脑，我们终于有了一个受控的、可观测的环境来调试实际的生产问题。通过将 LLM 与其使用的工具隔离，架构的操作、维护和扩展变得显著更容易。

## **为什么 MCP 需要远程架构**

MCP 作为 LLM 可以调用的工具的标准接口，正获得越来越多的关注。在我自己的早期实验和团队环境中，第一个想法总是将 MCP 服务器进程在本地运行。这在概念验证期间运行良好，但一旦多个工程师或实际工作负载依赖于相同的工具，其局限性就变得显而易见。以下问题迅速且反复出现。

*   **本地执行无法扩展** — 如果许多用户或许多 LLM 调用命中工具，本地进程无法处理负载。
*   **难以在多个环境中共享** — 本地工具只存在于单个开发人员机器上。它们无法为暂存、测试或生产系统的工作负载提供服务。
*   **有限的可观测性和操作控制** — 团队在不将 MCP 服务器迁移到托管平台的情况下，无法轻松监控日志、指标或资源使用情况。
*   **安全和隔离问题** — 本地工具可能会混淆职责，并允许未经授权地访问敏感系统。

在我们的案例中，这些痛点是我们开始将 MCP 工具迁移到 Kubernetes 的原因。远程部署解决了阻碍本地设置的扩展性、可观测性和协作挑战，并允许架构随着应用程序的增长而发展。

## 为什么 Kubernetes 天然适合 MCP 服务器

当我们第一次将 MCP 工具从本地机器迁移出来时，Kubernetes 很快就成为了显而易见的平台。我们将工具容器化并部署到集群后，许多早期的痛点就消失了。团队终于可以在不同环境之间共享工具，我们获得了适当的**可观测性**，并且可以在不中断现有工作流的情况下推出新版本。Kubernetes 提供了本地 MCP 进程所缺乏的操作基础。

Kubernetes 提供了多项优势，使其成为 MCP 工作负载的理想选择：

*   **可扩展性** — 水平 Pod 自动伸缩允许 MCP 服务器根据需求增长。
*   **关注点清晰分离** — LLM 专注于推理和语言任务。MCP 服务器在隔离的容器中处理工具执行。
*   **滚动更新** — 团队可以部署新工具或更新现有工具而无需停机。
*   **网络访问控制** — 入口规则、安全组和私有网络使团队能够更好地控制流量。
*   **可观测性** — Kubernetes 直接与日志、追踪和监控栈集成，有助于快速诊断问题。
*   **基于容器的打包** — 每个 MCP 工具都成为一个版本化、经过测试且可部署的容器镜像。

这些功能与我们在生产中扩展 AI 工具时所需的功能高度契合，使得 Kubernetes 成为大规模托管 MCP 服务器最实用的选择。

这些功能与现代 AI 基础设施的演进方式非常吻合。

## 远程 MCP 架构如何工作

将 MCP 工具迁移到 Kubernetes 时，我们看到的最大优势之一是请求流的清晰度。一旦所有东西都远程且可观测，就更容易理解延迟发生在哪里，故障发生在哪里，以及如何独立扩展不同的组件。以下序列反映了在我们的生产设置中持续出现的模式。

下面是系统如何处理请求的简化解释。

**1. 用户触发操作 —** 用户与应用程序交互，促使 LLM 执行任务。

**2. LLM 创建 MCP 工具调用 —** LLM 使用 MCP 标准向 MCP 客户端发送工具调用。

**3. MCP 客户端向远程服务器发送请求 —** 客户端通过 HTTP 与 MCP 服务器通信。服务器 URL 通过 Kubernetes ALB 公开。

**4. ALB 将请求路由到 EKS —** ALB 接收调用并将其转发到集群内正确的 Kubernetes 服务。

**5. MCP 服务器 Pod 处理请求 —** 服务器运行在从源代码构建并存储在 ECR 中的容器内。它执行工具逻辑，处理输入输出，并返回结果。

**6. 结果流回 LLM —** 响应通过相同的链条返回：MCP 服务器到 ALB 到 MCP 客户端到 LLM。

**7. LLM 使用结果继续工作流 —** LLM 将工具输出集成到其推理中，并为用户生成最终响应。

在实际部署中，这种清晰的分离使故障排除变得容易得多，并使团队能够独立地观测和扩展每个阶段。通过适当的日志、指标和路由，我们可以找出在本地设置中可能不可见的瓶颈。

## **MCP 服务器的 Kubernetes 部署示例**

下面是一个 MCP 服务器如何在 EKS 上部署的简化示例。

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mcp-server
  template:
    metadata:
      labels:
        app: mcp-server
    spec:
      containers:
      - name: mcp-server
        image: <aws-account>.dkr.ecr.<region>.amazonaws.com/mcp:latest
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: mcp-service
spec:
  type: NodePort
  selector:
    app: mcp-server
  ports:
  - port: 80
    targetPort: 8000
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mcp-ingress
spec:
  ingressClassName: alb
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mcp-service
            port:
              number: 80
```

这足以实现一个最小的远程 MCP 设置。

## 远程 MCP 架构的关键优势

我们在扩展基于 MCP 的工具时最大的体会之一是，架构本身和工具一样重要。在 Kubernetes 上运行 MCP 服务器解锁了一系列本地进程或临时部署无法实现的实际优势。这些优势在实际工程用例中持续出现。

*   **工具工作负载的独立扩展 —** 某些工具所需的计算资源远多于其他工具。通过将每个 MCP 服务器隔离在其自己的 Pod 中，系统可以独立扩展它们而不会影响管道的其余部分。
*   **清晰的运营边界 —** LLM 仍然专注于推理和编排，而 MCP 服务器处理实际的工具执行。这种分离保持了职责的清晰，并防止了跨组件的故障。
*   **轻松升级和实验 —** 团队可以推出新版本的 MCP 工具，升级依赖项，或测试新功能，而无需触及生产 LLM 工作负载。这大大降低了破坏下游工作流的风险。
*   **同时支持多种工具 —** 一个 EKS 集群可以托管数十甚至数百个工具容器。每个工具都可以按照自己的速度发展，这在多个团队贡献不同功能时非常有用。
*   **更好的安全态势 —** 入口控制、虚拟私有云边界、身份和访问管理角色以及容器隔离，使得保护敏感数据和确保每个工具只拥有所需访问权限变得更容易。
*   **企业级 AI 的理想选择 —** 金融服务、医疗保健和其他高信任度领域的组织受益于可预测、可审计和可扩展的架构。Kubernetes 带来了满足这些标准所需的结构和**可观测性**。

实际上，这些优势将这种架构从实验性转变为能够大规模支持真实生产 AI 系统的方案。

## 结论

模型上下文协议正在为一类新的基于工具的 AI 工作流打开大门，但大多数早期实现仍然停留在个人笔记本电脑或临时本地服务器上。根据我在生产 AI 系统方面的工作经验，实验和实际部署之间的差距会很快变得显而易见。团队越依赖 MCP 工具，他们就越需要可预测的环境、审计追踪、扩展能力和清晰的运营边界。

在 Kubernetes 上运行 MCP 服务器提供了一种满足这些需求的实用方法。通过将 LLM 客户端与工具实现分离，团队能够独立部署和更新工具，通过集中日志跟踪行为，并根据工作负载扩展单个工具。这也为工程师提供了一个更安全的空间来实验新的 MCP 功能，而不会中断生产 LLM 管道。

随着 MCP 的普及，我预计这些云原生模式将成为 AI 工程团队的默认选择。那些能够大规模成功应用 AI 的组织，会将工具视为一等基础设施，而不是本地脚本。Kubernetes 提供了支持这一转变所需的可靠性和结构，而我概述的架构反映了我在真实企业环境中看到的有效实践。