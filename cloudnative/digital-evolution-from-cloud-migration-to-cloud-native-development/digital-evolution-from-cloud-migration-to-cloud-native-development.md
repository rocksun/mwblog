<!--
title: 数字进化：从云迁移到云原生开发
cover: https://cdn.thenewstack.io/media/2024/01/fb978790-migratory-birds-7242608_1280-1024x683.jpg
-->

传统的单体架构常常导致像 Blockbuster 这样的企业被抛在了后面。如今，企业可以根据需求提供资源，降低与数据中心管理相关的开销。

> 译自 [Digital Evolution from Cloud Migration to Cloud Native Development](https://thenewstack.io/digital-evolution-from-cloud-migration-to-cloud-native-development/)，作者 Amy Groden-Morrison 是 Alpha Software 的市场营销和销售运营副总裁。她在 TIBCO Software、RSA Security 和 Ziff-Davis 等公司担任市场传播领导职务超过 15 年。

企业面临着演进传统基础架构的同时确保 IT 运营敏捷性和可扩展性的双重挑战。云原生技术的兴起为前所未有的灵活性和性能提供了机遇，其中容器化、无服务器计算和微服务是这一转型的关键驱动因素。

根据 Gartner 的数据，到 2025 年，95% 的新数字工作负载将在[云原生平台上实现](https://www.gartner.com/en/newsroom/press-releases/2021-11-10-gartner-says-cloud-will-be-the-centerpiece-of-new-digital-experiences)。对于参与这一演进的企业，以下是关于云原生原则的重要性以及它们如何彻底改变数字时代的事项。

## 从传统到云原生的转变

从传统系统向[云原生平台](https://thenewstack.io/the-3-paradoxes-of-cloud-native-platform-engineering/)的转变主要受到对更大敏捷性和灵活性的需求驱动。我们来看看 Blockbuster 和 Netflix。Blockbuster 对物理基础设施的依赖和对创新的犹豫导致了它的衰落，而 Netflix 则以云为先的方法重新定义了娱乐。

传统的单体架构，由于其刚性的可扩展性，常常导致像 Blockbuster 这样的企业落后。它们在软件复杂性、硬件瓶颈和不断上升的维护成本方面面临着困境。IaaS 和 PaaS 解决方案的出现带来了重大变化。

企业可以根据需求进行资源配置，并按使用量付费，降低与数据中心管理相关的开销。像 Spotify 这样的公司通过使用 Google Cloud 的 [Bigtable](https://techcrunch.com/2020/02/18/how-spotify-ran-the-largest-google-dataflow-job-ever-for-wrapped-2019/) 实现了高效的数据存储和检索，从中获益匪浅。显而易见的核心优势在于灵活的[按需扩展](https://thenewstack.io/covid-19-kubernetes-helps-retail-gaming-meet-sudden-scaling-demands/)以及仅支付已使用资源的能力。

这种对可扩展基础架构的需求增加，网络应用的激增以及云服务的成本效益模式催生了云采用的指数级增长。

## 云原生原则及其与无服务器计算和微服务的关系

云原生的核心是容器化，通常利用 [Docker](https://www.docker.com/?utm_content=inline-mention) 容器，并由 Kubernetes 进行[编排](https://thenewstack.io/what-is-container-orchestration/)，为部署应用提供了标准化环境。这种一致性对于像 [Airbnb](https://www.codemotion.com/magazine/microservices/microservices-migration/) 这样的企业至关重要，他们需要在不同环境中保持一致，以确保应用稳定性并减少部署问题。

无服务器计算，如 [AWS](https://aws.amazon.com/?utm_content=inline-mention) Lambda 所示，通过减轻开发人员的基础设施管理负担来补充这一点。企业不必再担心服务器的维护或正常运行时间，而可以专注于[代码和应用](https://thenewstack.io/offloading-authentication-and-authorization-from-application-code-to-a-service-mesh/)功能。

重要的是，容器化和无服务器计算可以与 [AWS Fargate](https://aws.amazon.com/fargate/) 等平台集成，允许容器化应用的无服务器部署。这既确保了应用一致性（来自容器）又确保了操作效率（来自无服务器）。

[微服务](https://thenewstack.io/microservices/what-is-microservices-architecture/)进一步拓展了这种协同作用。这些是独立的应用组件，可以分别开发和部署。在容器化提供的基础一致性支持下，微服务能够平稳运行，并且通过像 Kubernetes 这样的编排工具，它们的部署和扩展变得更加可管理。以 [Monzo 银行](https://iviewlabs.medium.com/real-world-implication-of-microservices-in-the-fintech-industry-25c24193aa56)为例，他们利用微服务确保更快的功能发布和更容易的维护。

因此，容器化提供了稳定的环境；无服务器确保了高效的运行；而微服务则提供了部署的灵活性。它们共同使企业能够开发和维护稳健、可扩展且具有成本效益的应用程序。

## 抽象化云基础设施的优势：从扩展到快速部署

云基础设施的抽象特性为企业提供了重大优势，确保它们可以将应用程序的特性和功能优先于基础架构的挑战。以下是其中的优势：

- **专注于业务逻辑**：随着[基础架构复杂性的抽象化](https://thenewstack.io/developer-portals-can-abstract-away-kubernetes-complexity/)，开发人员可以将精力集中在塑造业务逻辑上。他们不再需要被服务器配置、网络设置或存储细节的复杂性所分散注意力。
- **动态资源扩展**：由[像亚马逊 EC2](https://thenewstack.io/inside-a-privilege-escalation-attack-via-amazon-web-services-ec2/) 和 Kubernetes 这样的服务支持的云原生环境将适应性置于前沿。无论应用程序需求是增加更多实例（横向扩展）还是增强现有实例的能力（纵向扩展），这些平台都能迅速适应。
- **加速部署周期**：将 CI/CD 工具与云原生平台集成可以简化代码集成、测试和部署。其结果是大大缩短的发布周期，确保产品和功能更快地到达用户手中，并根据他们的反馈进行改进。
- **利用低代码进行快速开发**：低代码平台正在成为云原生演进中的重要工具。它们提供了一种快速[开发应用程序](https://www.alphasoftware.com/blog/why-cloud-native-developers-are-turning-to-low-code)的方式，缩短了传统编码的障碍。此外，它们提供的无缝连接器、API 集成和迁移工具能够确保企业从传统系统过渡时不会遇到障碍或数据丢失。它们与流行的 SaaS 工具和数据库兼容，意味着数据集成轻而易举，即使在过渡期间也能保持数据流畅。

要对企业的核心需求进行批判性评估，并将其与适当的技术解决方案相匹配，这是至关重要的。在拥抱新技术之前，确保其与当前业务模型的一致性以及与客户需求的共鸣。

业务目标应始终引导技术选择。虽然策略应该决定工具的选择，但在数字化演进中，[云原生开发](https://thenewstack.io/cloud-native/)的出现确保了这种一致性，强调的是策略而不是简单的工具采用。
