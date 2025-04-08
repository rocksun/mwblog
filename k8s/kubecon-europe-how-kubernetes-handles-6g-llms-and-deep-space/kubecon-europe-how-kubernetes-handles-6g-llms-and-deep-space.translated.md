# KubeCon 欧洲：Kubernetes 如何处理 6G、LLM 和深空

![Featued image for: KubeCon Europe: How Kubernetes Handles 6G, LLMs and Deep Space](https://cdn.thenewstack.io/media/2025/04/1776f030-kubecon-google-bytedance-1024x768.jpg)

伦敦 — [KubeCon + CloudNativeCon 欧洲](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/)最后一天的最终主题演讲强调了 [Kubernetes](https://www.thenewstack.io/Kubernetes) 在不久的将来必须支持的内容。

即使在那些仍在努力进行 Kubernetes 部署和管理庞大的容器化基础设施（通常扩展到不同的地理环境）的人中，未来也带来了一系列新的挑战。许多这些挑战的解决方案正在开发中。

社区支持仍然是开源开发中必不可少的，以支持[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)最大的项目。

正如在星期五的主题演讲讨论中显示的那样，[Kubernetes 基础设施的巨大覆盖范围](https://thenewstack.io/day-2-kubecon-europe-keynotes-users-share-kubernetes-war-stories/)正在扩展以支持前沿用例。这包括当前 5G 和新兴 6G 基础设施的电信部署，以及减少 Kubernetes 环境中[大型语言模型](https://thenewstack.io/kubecon-europe-day-1-keynote-can-observability-keep-up-with-llms/) (LLM) 的令牌化和实施中的延迟。

对于研究外太空的天体物理学家来说，用于分析数据的基础设施理论上必须能够处理近乎无限数量的计算。

## K8s 上的负载均衡

负载均衡一如既往地需要改进，但 Kubernetes 上的 LLM 为数据传输带来了更多潜在的延迟问题。

在“Kubernetes 中 LLM 感知的负载均衡：效率新纪元”期间，Google 杰出工程师 Clayton Coleman 和 Bytedance 工程师 Jiaxin Shan 讨论了 [Kubernetes Gateway API Inference Extension](https://thenewstack.io/kubecon-europe-kgateway-aims-to-be-the-kubernetes-onramp/)。Coleman 说，它将 Kubernetes 网关转换为推理网关，使大型和小型平台团队受益。

KubeCon 欧洲 2025 伦敦第三天主题演讲：LLM 需要负载均衡来完成双重任务。

[@ByteDanceOSS]‘ Jiaxin Shan 和 ‘s Clayton Coleman: “LLM-Aware Load Balancing in Kubernetes: A New Era of Efficiency.”[@CloudNativeFdn][@thenewstack][pic.twitter.com/OePrvRzltC]— BC Gain (@bcamerongain)

[April 4, 2025]

该扩展由 Google 和 Bytedance 的实验提供信息，解决了从专有模型到开放模型的转变，强调了大型、前沿模型和较小、高效模型之间的权衡。Coleman 说，主要挑战包括不可预测的 GPU 负载、资源密集型模型和硬件异构性。

“运行大型模型正成为应用程序基础设施的基本组成部分，并且在未来几年，它将成为一种标准做法。为了为此做好准备，我们必须确定可以标准化和重用的 API 和组件，”Coleman 说。“我们还需要一个连接最新研究和生产环境的通用框架，以确保从创新到部署的平稳过渡。如果存在标准、动态和可扩展的负载均衡器，它必须不断发展以满足这些需求。”

KubeCon 欧洲 2025 伦敦第三天主题演讲：“电信领域的云原生演进：5G、6G 及未来！”

[@Swisscom]‘s Joel Studler on[@kubernetesio]infrastructure, w/Faseela K, Ericsson Software Technology; Tom Kivlin, Vodafone; Philippe Ensarguet, Orange.[@thenewstack][#KubeCon2025][pic.twitter.com/222HSOXzOw]— BC Gain (@bcamerongain)

[April 4, 2025]

## Kubernetes 用于 5G、6G

在“电信领域的云原生演进：5G、6G 及未来！”期间，Ericsson 的 Faseela K、Vodafone 的 Tom Kivlin、Orange 的 Philippe Ensarguet 和 Swisscom 的 Joel Studler 组成的小组讨论了开源云原生在 5G 网络中发挥的关键作用，并将在未来发挥作用。

Studler 说，Swisscom 依赖于 [Flux for GitOps](https://thenewstack.io/tutorial-a-gitops-deployment-with-flux-on-digitalocean-kubernetes/) 和 Kubernetes 等工具来实现自动化，从而将部署时间从几周缩短到几分钟。Studler 说，CNCF 代理在“我们的网络转型之旅”中至关重要。

Studler 说：“在电信领域，我们仍然习惯于从物理和黑盒解决方案的角度进行思考。“人们一直认为我们需要虚拟化传统系统，这与[云原生技术](https://thenewstack.io/cloud-native/)的开放和简化方法背道而驰。”

Swisscom 的云原生工具包括：

- 用于 CNS 部署的 Flux。
- 用于系统管理的 NetConf。
- 带有其 PKI 的 Cert-Manager。
- 用于使用 ExternalDNS 自动化 DNS 管理的 ExternalDNS。
> “通过 Kubernetes 资源模型 ([Kubernetes Resource Model](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md)) 编排一切，我们实现了显著的生产力提升——将流程时间从数周和数天缩短到数小时和数分钟，” Studler 说。

KubeCon 欧洲 2025 伦敦 Day 3 主题演讲：LLM 需要负载均衡来完成双倍以上的任务。

[@ByteDanceOSS](https://twitter.com/ByteDanceOSS)‘ Jiaxin Shan and [@CloudNativeFdn](https://twitter.com/CloudNativeFdn) [@thenewstack](https://twitter.com/thenewstack) [pic.twitter.com/OePrvRzltC](https://twitter.com/bcamerongain/status/1775914342442223769/photo/1)— BC Gain (@bcamerongain)

[2025年4月4日](https://twitter.com/bcamerongain/status/1775914342442223769)

## 在天空中

在平方公里阵列（SKA）项目的保护下，洛桑瑞士联邦理工学院（EPFL）的系统专家 Carolina Lindqvist 描述了瑞士 SKA 区域中心（CHSRC）部门如何在全球 SKA 区域中心网络（SRCNet）中依赖 Kubernetes 作为服务管理平台，以支持极端数据和计算密集型天文用例，Lindqvist 说。

SKA 每年将接收高达 600PB 的数据，需要全球存储和分发，Lindqvist 说。该项目包括 12 个合作团队和各个合作国家。这些数据将用于研究宇宙领域和太阳物理等主题。瑞士站点使用云原生基础设施，包括一台超级计算机，来处理和分发数据，Lindqvist 说。

在演示过程中，Lindqvist 展示了一个天文工作流程。它包括获取一张用望远镜从太空拍摄的图像，然后对其进行处理以进行分析。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)