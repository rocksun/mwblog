# Tetrate 与彭博合作打造基于 Envoy 的 AI 网关

![Tetrate 与彭博合作打造基于 Envoy 的 AI 网关的特色图片](https://cdn.thenewstack.io/media/2024/10/7d62fd5a-tetrate-1024x683.png)

[Tetrate](https://tetrate.io/) 和 [彭博](https://www.bloomberg.com/) 宣布合作创建 AI 网关的开放标准。该计划将基于 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention) (CNCF) 的 [Envoy 网关](https://gateway.envoyproxy.io/) 项目，该项目是 [Kubernetes 网关](https://gateway-api.sigs.k8s.io/) 应用程序编程接口 (API) 的实现。

具体来说，[Envoy 网关](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/) 基于 Envoy 反向代理作为网络网关，允许它引导内部 [微服务](https://thenewstack.io/category/microservices/) 流量并管理进入网络的外部流量。网关每秒可以处理数百万个请求，非常适合高流量场景。它还支持自定义过滤器并具有灵活的架构。这使开发人员能够扩展其功能，而 Tetrate 和彭博正在做的事情正是如此。

他们的合作解决了将 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 有效地集成到企业应用程序中的日益增长的需求。通过扩展 Envoy 网关的功能，该项目将提供一个社区主导的开源解决方案，用于 AI 集成，而不会出现供应商锁定或商业许可限制。

该项目的最初想法源于彭博云原生计算服务的工程团队负责人，也是 [KServe](https://github.com/kserve/kserve) 项目的联合创始人 Dan Sun，他来到 Envoy 社区并概述了他对问题空间的看法以及解决问题的潜在路径。Tetrate 作为 Envoy 上游的主要贡献者，主动表示有兴趣帮助 Sun 和彭博将他们对 Envoy AI 网关 API 的愿景变为现实。

KServe 为服务预测性和生成式机器学习 (ML) 模型提供 Kubernetes [自定义资源定义](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)。它旨在通过提供用于 TensorFlow、XGBoost、ScikitLearn、PyTorch 和 Huggingface Transformer/LLM 模型的高抽象接口来解决生产模型服务用例，这些接口使用标准化的数据平面协议。

新 AI 网关的主要功能包括：

- 针对 LLM 提供商的高可用性路由的应用程序流量管理。
- 在不同组织级别监控和控制 LLM 使用情况。
- 用于 LLM 请求的统一接口，具有与多个提供商的后端连接。

Envoy 网关和 KServe 可以一起使用，允许将流量路由到自托管和供应商托管的 LLM。在这种情况下，AI 网关位于顶部，使用 KServe 将开源 LLM 模型流量路由到自托管端点，而供应商托管的模型流量则路由到 AWS Bedrock 或类似的基于云的服务。

Tetrate 创始人 Varun Talwar 在一份声明中补充道：“我们与彭博和 CNCF 的合作旨在设计和交付一个社区主导的完全开源的 AI 网关，该网关由领先的竞争者提供支持，以取代 Kubernetes 入口的传统模型。这是市场需求的解决方案，我们很高兴成为创建它的维护者和贡献者团队的一部分。”

彭博云原生计算服务的工程主管 Steven Bower 表示：“作为一家‘开源优先’的公司，彭博相信开源社区的力量和协作性，可以开发 Web 规模的解决方案，而这种重要的差异使该项目成为其他正在进行的努力的宝贵替代方案。”

CNCF 首席技术官 Chris Aniszczyk 赞扬了该计划，称其证明了 Envoy 的灵活性和云原生生态系统中社区协作的力量。“彭博和 Tetrate 做了我们社区旨在做的事情：将人和组织聚集在一起解决共同的问题。他们使用 Envoy 网关来做到这一点，这仅仅证明了该项目的强大功能和可扩展性。”

要了解有关 [Envoy AI 网关项目的更多信息，感兴趣的各方可以参加 CNCF 于 2024 年 10 月 17 日举办的即将举行的网络研讨会](https://community.cncf.io/events/details/cncf-cncf-online-programs-presents-cloud-native-live-enabling-ai-adoption-at-scale-the-ai-platform-with-envoy-ai-gateway/)。小组讨论将邀请来自彭博和 Tetrate 的工程师参加。它将涵盖该项目以及企业 AI 采用和 AI 平台的作用等主题。

因此，很明显，随着公司将 AI 集成到其应用程序中，Envoy 网关将发挥重要作用。

[
YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看所有播客、访谈、演示等。

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)