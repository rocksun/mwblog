
<!--
title: 如何在Kubernetes上为容器化的LLM设置防护措施
cover: https://cdn.thenewstack.io/media/2025/03/c2434756-securing-containerized-llms-kubernetes-guardrails.jpg
summary: 容器化 LLM 风险高？用 Kubernetes + NVIDIA Guardrails 打造安全防护！本文详解 OKE 上 LLM 容器安全，多层网络策略防提示注入。集成 Kubeflow 实现 MLOps，持续训练、验证、部署，保障 AI 应用安全。云原生时代，安全先行！
-->

容器化 LLM 风险高？用 Kubernetes + NVIDIA Guardrails 打造安全防护！本文详解 OKE 上 LLM 容器安全，多层网络策略防提示注入。集成 Kubeflow 实现 MLOps，持续训练、验证、部署，保障 AI 应用安全。云原生时代，安全先行！

> 译自：[How to Put Guardrails Around Containerized LLMs on Kubernetes](https://thenewstack.io/how-to-put-guardrails-around-containerized-llms-on-kubernetes/)
> 
> 作者：Sanjay Basu; Victor Agreda

随着[大型语言模型 (LLMs)](https://thenewstack.io/what-is-a-large-language-model/)在企业应用中变得越来越重要，安全地部署它们变得至关重要。常见的威胁，如提示注入，可能导致意外行为、数据泄露或未经授权访问内部系统。传统的应用程序级安全措施虽然有价值，但通常不足以保护 LLM 端点。

容器化可以帮助应对这些挑战。通过将 LLM 及其支持组件封装在容器中，组织可以在基础设施级别强制执行严格的安全边界。这种多层方法，结合强大的防护栏机制（例如，NVIDIA 的 [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)），有助于防止可疑或恶意提示到达核心模型逻辑。

本文概述了实施企业级安全 LLM 部署所需的设计和注意事项。作为示例，我们使用 [Kubernetes](https://thenewstack.io/kubernetes/) 平台在 [Oracle Cloud Infrastructure](https://thenewstack.io/how-oracle-is-meeting-the-infrastructure-needs-of-ai/) (OCI) 上，并使用 OCI Kubernetes Engine (OKE)，它与 Cloud Native Computing Foundation (CNCF) 的开源 Kubernetes 高度一致。此实现也应适用于开源 Kubernetes。我们的示例包括：

- 基于容器的防护栏，以对抗提示注入攻击。
- OKE 中的多层网络、资源和访问策略。
- 与 [Kubeflow](https://thenewstack.io/smooth-sailing-for-kubeflow-1-9-thanks-to-cncf-red-hat-support) 集成，用于持续训练、验证和部署（机器学习运营或 [MLOps](https://thenewstack.io/what-is-mlops/)）。

## 端到端工作流程图

此图显示了我们将在本文中介绍的解决方案的架构。

![](https://cdn.thenewstack.io/media/2025/03/23cef979-e2e_kubernetes-container-workflow.png)

## 了解提示注入漏洞

提示注入是一种特定于 LLM 的攻击类型，其中攻击者精心制作输入（提示）来操纵模型的行为。例如，攻击者可能会精心制作文本，绕过内容过滤器或泄露应保密的系统指令。这种利用可能导致：

- **未经授权的数据访问：** 深入了解隐藏的提示、机密的用戶数据或系统 API。
- **意外的 LLM 行为：** 产生有害、有偏见或不允许的输出。

提示注入攻击带来了独特的挑战，使其在企业环境中尤其危险。与传统的注入攻击（如 SQL 注入或跨站脚本 (XSS)，可以通过签名匹配检测到）不同，提示注入涉及微妙的文本操作，很容易逃避标准检测方法。

LLM 的动态、上下文相关的性质进一步使这个问题复杂化，因为恶意行为者可以利用模型自身的推理能力来规避保护措施。此外，在复杂的企业系统中，成功的提示注入攻击（泄露敏感数据）可以成为攻击者发起更广泛的基于网络的威胁的垫脚石。

## 防护栏和基于容器的安全性

我们需要的是安全过滤器，并且有多种选择可以创建能够扫描和清理提示的此类过滤器。让我们看一个这样的解决方案：

### NVIDIA Guardrails

[NVIDIA](https://thenewstack.io/nvidia-unveils-next-gen-rubin-and-feynman-architectures-pushing-ai-power-limits/) Guardrails 是一个开源框架，用于集成安全过滤器，这些过滤器可以在提示到达 LLM 推理引擎之前对其进行扫描和清理。主要功能包括：

- **文本过滤：** 识别提示中的恶意或可疑模式。
- **上下文强制：** 限制操作上下文（例如，确保 LLM 仅讨论某些主题）。
- **自适应学习：** 随着新威胁的出现，不断改进规则集和响应策略。

当与 [Kubernetes 的容器编排](https://roadmap.sh/kubernetes) 结合使用时，NVIDIA Guardrails 可以作为预推理容器运行，该容器对传入的请求强制执行安全策略。

### 多层容器安全控制

在容器中集成防护栏逻辑提供了多层安全优势，从而增强了 LLM 部署的整体保护。这些容器化的安全控制与防护栏协同工作，以创建全面的防御策略。好处包括：

- **网络隔离：** Kubernetes 网络策略限制 Pod 之间的流量。LLM 容器仅与防护容器和授权服务通信。
- **资源约束：** Kubernetes 中的 CPU 和内存限制有助于防止任何单个容器垄断集群资源或触发拒绝服务场景。
- **运行时安全策略：** Seccomp、AppArmor 或 SELinux 等工具通过限制容器可以执行的系统调用来减少攻击面。

### 容器级访问控制

在容器中部署 LLM 端点的组织可以实施几个关键的访问控制来增强安全性：

- **最小权限访问：** 细粒度的基于角色的访问控制 (RBAC) 限制了谁可以部署、修改或访问来自特定容器的日志。
- **密钥管理：** 此方法将 API 密钥、加密密钥或凭据安全地存储在 OCI Vault 或 Kubernetes 密钥等服务中。

## 部署模型

在较高层面上，部署模型实施了一种结构化的方法来处理用户请求，其中包含多个专用容器，每个容器都提供特定的安全和操作功能。此架构有助于确保每个请求在到达 LLM 并返回给用户之前都经过适当的验证和处理。一些组件包括：

- **用户提示：** 用户的请求通过前端应用程序或 API 网关进入系统。
- **防护容器：** 请求被转发到专用容器（例如，NVIDIA Guardrails），该容器检查提示中是否存在恶意或不允许的内容。
- **LLM 推理容器：** 如果提示通过了防护检查，则会将其转发到托管 LLM 的容器。所有推理操作和有状态数据都保留在此处。
- **输出处理容器：** （可选）另一个容器可以重新检查 LLM 的响应或对其进行清理，然后再将其返回给用户。
- **持续监控：** 日志和指标馈送到集中式监控堆栈中，如果发生可疑活动，则会向操作员发出警报。

![OKE 环境](https://cdn.thenewstack.io/media/2025/03/6d5841db-oke-environment.jpg)

*OKE 环境*

## 整合 Kubeflow 以实现 MLOps

Kubeflow 作为一个重要的开源 MLOps 平台，以 Kubernetes 原生的方式运行，为管理 LLM 部署提供关键功能。它支持全面的实验跟踪，允许团队监控和比较 LLM 模型的各种微调实验。

通过管道自动化功能，Kubeflow 简化了从数据提取到模型训练、验证和部署的工作流程。利用 Kubernetes 原生的扩展功能，它可以高效地处理大型训练数据集并支持多个并发实验，使其成为企业级 LLM 操作的理想选择。

### 工作流程集成

Kubeflow 的工作流程集成功能通过自动化关键流程并确保安全控制的一致应用，从而增强了 LLM 部署的安全性与可靠性。该平台支持以下几个以安全为中心的关键工作流程：

- **训练和验证：** 使用 Kubeflow 管道来安排和自动化数据准备、LLM 微调和验证步骤。
- **防护规则更新：** 当您在训练期间或从生产日志中发现新的潜在提示注入模式时，您可以更新防护规则或过滤器。此更新可以通过 Kubernetes 滚动更新自动应用于防护容器。
- **部署：** 当模型或防护规则集经过验证时，Kubeflow 会触发 Kubernetes 中的容器构建和部署，从而确保以最短的停机时间实现持续交付。

## 运维最佳实践

- **持续监控和日志记录：** 从防护容器和 LLM 容器收集日志。Prometheus 和 Grafana 等工具跟踪响应时间、错误和使用模式。
- **审计日志记录：** 出于合规性目的，维护谁访问了 LLM、输入的提示以及是否有任何提示被防护容器标记的日志。
- **定期安全评估：** 定期运行渗透测试，重点关注提示注入和绕过防护逻辑的尝试。
- **多集群或混合部署：** 对于灾难恢复或特殊用例，请考虑跨多个集群或混合设置（本地 + 云）进行部署。

## 结论

提示注入代表了对 LLM 部署的严重且不断演变的威胁。通过将应用程序级别的防护（例如，NVIDIA Guardrails）与容器级别的安全措施相结合，组织可以实施强大、多层防御。这种方法有助于防止恶意或操纵性输入损害 LLM 的功能或更广泛的基础设施。
使用 Kubeflow 进行 MLOps 可以进一步提高弹性和敏捷性，从而能够持续改进 LLM 模型及其相关的防护规则。这种容器化的、高度编排的架构为企业级 LLM 部署提供了必要的可扩展性、安全性和可管理性。