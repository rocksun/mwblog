<!--
title: 边缘计算并非简单的“近端云计算”
cover: https://cdn.thenewstack.io/media/2025/08/acd77790-heroimage.png
summary: 文章讨论了软件开发的五大转变，以及边缘计算的兴起及其独特的挑战，如资源限制、安全性和连接问题。掌握边缘云原生实践能带来实时洞察和创新体验。
-->

文章讨论了软件开发的五大转变，以及边缘计算的兴起及其独特的挑战，如资源限制、安全性和连接问题。掌握边缘云原生实践能带来实时洞察和创新体验。

> 译自：[Why the Edge Isn't Just 'Cloud Computing, But Closer'](https://thenewstack.io/why-the-edge-isnt-just-cloud-computing-but-closer/)
> 
> 作者：Charles Humble

*注：本文节选自 The New Stack 的新电子书“[边缘的 Kubernetes：大规模容器编排](https://thenewstack.io/ebooks/kubernetes/kubernetes-at-the-edge-container-orchestration-at-scale/)”。*

---

在我从事软件工作的 30 多年里，我看到了企业软件构建和部署方式的五个主要转变：采用更高级的语言，如 [Java](https://thenewstack.io/introduction-to-java-programming-language/) 和 C#；敏捷运动；公共云；[DevOps](https://thenewstack.io/introduction-to-devops/)，特别是持续交付；以及 [微服务](https://thenewstack.io/introduction-to-microservices/)。

每个转变最终都成功了，因为它缩短了价值实现的时间。它使企业中的某个人能够更快、更低成本地将想法呈现给客户。这种结合使企业能够[尝试更多想法](https://blog.container-solutions.com/why-run-thousands-of-failed-experiments)，并利用市场的反应来确定哪些想法能引起共鸣，哪些不能。尽管人们对此大肆宣传和兴奋不已，但生成式 AI (GenAI) 是否会成为第六个转变仍有待观察。

在许多方面，容器化在边缘的兴起反映了这种历史模式。重用云启用的实践，如 CI/CD，支持更以开发者为中心的框架，即使在分布式物理环境中也是如此。通过使应用程序能够以通用格式打包，并在开发、测试和生产环境中以相同的方式运行，容器化简化了原本复杂的部署过程。

当我们继续探索 [AI 在企业中的作用](https://thenewstack.io/ai/)时，边缘代表了这种演变的下一个前沿。边缘设备的功能越来越强大。实时推理、数据本地性要求和延迟约束都推动计算更接近数据生成和决策制定的位置。

## 灾难边缘

边缘不仅仅是“云计算，但更近”。相反，它将 [云原生实践](https://thenewstack.io/introduction-to-cloud-native-computing) 扩展到传统云假设失效的位置。边缘是一个独特的挑战性环境，需要周到地关注以下因素：

* **有限或没有 IT 人员：** 如果边缘环境中的基础设施出现问题，您可能没有当地的专家来处理这些问题。
* **物理约束：** 部署到边缘的设备的 CPU/GPU 功率和内存都受到限制。与 Tier 1 数据中心相比，电源通常不可靠，并且环境可能异常炎热、寒冷或脏乱，这会增加故障率。
* **安全性：** 在数据中心，物理访问可以轻松控制和限制；但在边缘环境中，情况并非如此。这意味着您必须密切关注谁有权访问网络边缘的设备。
* **连接问题和中断：** 连接可能受到限制，因此如果您必须依赖互联网，您可能无法运行您的应用程序。
* **不可预测的需求：** 在更成熟的企业中，您可能会发现已经运行了几十年的传统本地应用程序与现代、云原生、容器化的应用程序并行运行。

掌握边缘云原生实践的组织将能够最好地利用实时洞察力，响应当地情况，并提供以前不可能实现的功能和体验。

---

## 了解更多

我们的新电子书 *“[边缘的 Kubernetes：大规模容器编排](https://thenewstack.io/ebooks/kubernetes/kubernetes-at-the-edge-container-orchestration-at-scale/)*”* 是在边缘环境中部署容器化应用程序的策略、最佳实践和供应商选项的综合指南。通过阅读这本免费电子书，您将了解：

* 边缘计算的真正含义，以及它如何从区域数据中心扩展到单个传感器。
* 构建强大且具有弹性的边缘基础设施的可操作的最佳实践。
* 真实世界的用例，展示了公司如何利用边缘来实现 AI、可持续性等。
* 领先的 Kubernetes 边缘供应商的市场调查，以帮助您选择合适的平台。
* 组建团队并在边缘部署 Kubernetes 而不中断当前运营的“操作指南”。