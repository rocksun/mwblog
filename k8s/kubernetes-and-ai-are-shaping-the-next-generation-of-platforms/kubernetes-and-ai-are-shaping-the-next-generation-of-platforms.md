
<!--
title: Kubernetes和AI：定义下一代平台
cover: https://cdn.thenewstack.io/media/2025/10/8f2e1ec9-wires.jpeg
summary: 平台工程采用IDP，以Kubernetes为基石，通过AI驱动API构建自适应平台，实现自动化、智能化并赋能开发者。
-->

平台工程采用IDP，以Kubernetes为基石，通过AI驱动API构建自适应平台，实现自动化、智能化并赋能开发者。

> 译自：[Kubernetes and AI Are Shaping the Next Generation of Platforms](https://thenewstack.io/kubernetes-and-ai-are-shaping-the-next-generation-of-platforms/)
> 
> 作者：Ana Margarita Medina, Viktor Farcic

平台工程已成为云原生生态系统中最重大的转变之一。各地的团队都在采用[内部开发者平台](https://thenewstack.io/platform-engineering-face-off-to-idp-or-not-to-idp/)（IDPs），以降低复杂性、加速交付并为开发者提供一致的生产“[黄金路径](https://thenewstack.io/heres-one-golden-path-to-build-an-mvp-enterprise-idp/)”。

但IDPs只是故事的一部分。Kubernetes已成为运行应用程序的标准控制平面。[Crossplane](https://www.crossplane.io/)在此基础上，将控制权向外扩展，从云资源到任何具有API的事物，使通用控制平面的理念成为可能。

伴随着[Backstage](https://backstage.io/)、[Argo CD](https://argoproj.github.io/cd/)和[Kyverno](https://kyverno.io/)等项目，这一转变正在塑造新一代的平台，这些平台统一了基础设施、开发者体验、交付和策略。这正成为[平台工程](https://thenewstack.io/platform-engineering/)下一阶段的基础，在这个阶段，人工智能不仅编写代码，还协助操作基础设施。

## **Kubernetes：平台的API**

[Kubernetes](https://thenewstack.io/kubernetes-complexity-realigns-platform-engineering-strategy/)最初是作为一种容器编排方式，但其真正的创新在于其API模型。声明式资源模式，及其期望状态、实际状态和持续协调，已被证明是一种通用抽象。它适用于工作负载、基础设施、策略等。

这种通用性是Kubernetes成为IDPs基础的原因。它提供了一种定义、扩展和强制执行平台构建块的一致方式。无论您是配置云数据库、管理网络策略还是应用合规性规则，Kubernetes API都使平台具有可编程性、可预测性和可组合性。

这种API优先的基础也使Kubernetes为AI时代做好了独特的准备。代理和大型语言模型（LLMs）不浏览仪表盘或部落知识；它们与API交互。Kubernetes提供了一个从第一天起就为机器到机器通信设计的、一致的、结构化的接口。

## **平台API的演进**

随着人工智能进入运营领域，我们开始看到平台API的演进。API不再是僵化、预定义的接口，而是变得更加动态和可发现。将它们视为可探索、查询和引导的模型，而不是静态契约。

这一转变可以从根本上简化开发者使用平台的方式。开发者不再需要记住YAML schemas或阅读冗长的文档，他们可以与一个理解平台API和组织规则的代理进行对话式交互。

## **超越IDPs：迈向自适应平台**

那么，平台工程将走向何方？

*   **IDPs**是当下：整合最佳实践，强制一致性，并提升开发者体验。
*   **Kubernetes**是基石：一个通用控制平面，标准化了平台的表达和消费方式。
*   **AI驱动的API**指向未来：能够引导、适应甚至从自身运营中学习的平台。

这些趋势预示着一个未来，平台不仅是自动化工具，更是人类和代理的积极合作伙伴。一篇关于[智能控制平面](https://mkto.upbound.io/rs/975-TPU-636/images/The%20Intelligent%20Control%20Plane%20-%20Towards%20Autonomous%20Infrastructure.pdf?version=0&utm_campaign=2025_Q3_8.5_GBL_FEV_UXP2-Launch&utm_medium=blog&utm_source=corporate-event)的最新论文进一步探讨了这一愿景，概述了如何统一状态、策略、知识和智能，从而实现平台随时间学习和适应。开发者不再需要拼凑脚本和运行手册，平台本身可以提供上下文、推荐解决方案并持续优化。

这并不意味着取代工程师。而是将他们从重复的繁琐工作中解放出来，以便他们能够专注于更高价值的工作。

IDPs为我们提供了今天所需的黄金路径。但在AI时代，平台还需要变得自适应、上下文感知，并能够服务于人类和机器。平台工程的未来不仅仅是自动化，更是关于智能。

## **加入讨论**

在2025年北美KubeCon + CloudNativeCon大会上，我们邀请您参加我们的会议，共同探讨平台工程的现在与未来：

*2025年北美KubeCon + CloudNativeCon大会将于11月10日至13日在乔治亚州亚特兰大举行。*[*立即注册*](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*。*