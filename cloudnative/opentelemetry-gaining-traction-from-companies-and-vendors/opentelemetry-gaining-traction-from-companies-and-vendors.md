# OpenTelemetry 获得公司和供应商的青睐

翻译自 [OpenTelemetry Gaining Traction from Companies and Vendors](https://thenewstack.io/opentelemetry-gaining-traction-from-companies-and-vendors/) 。

随着越来越多的公司采用 OpenTelemetry 来改善用户体验并降低成本，Elastic 和 OpenTelemetry 将合并标准。

![](https://cdn.thenewstack.io/media/2023/04/c2b7bda5-pexels-tim-gouw-5800216-1024x683.jpg)
*Tim Gouw 在 Pexels 拍摄的照片*

阿姆斯特丹——OpenTelemetry 的核心是识别复杂系统中的问题以创造更好的用户体验。但要做到这一点，它必须理解数千甚至数十万个节点上的 PB 级数据。

本质上，遥测监控三个来源：

* Logs
* Metrics
* Traces （监控交互路径，例如端到端事务和服务之间发生的事情）

存在在处理这些信息的竞争性标准显然会成为解释该信息的障碍。然而，这在历史上已经发生过。” Lightstep 开发者关系负责人、 CNCF 孵化项目 OpenTelemetry 维护者 Austin Parker 说道。

“我们正在努力做的是将所有这些人聚集在一起，因为所有这些项目的共同点多于它们的不同之处，” Parker 告诉 The New Stack。 “可观测性要求您作为开发人员或运营商将所有这些不同类型的数据和这些不同的技术汇集在一起​​，并将它们融合在一起，以真正了解正在发生的事情。”

## 合并标准公布

这就是为什么更受欢迎的标准之一——由可观测性和安全公司 Elastic 开发的弹性公共模式（Elastic Common Schema）正在合并到 OpenTelemetry 语义约定中，这一点非常重要。弹性公共模式定义了在 Elasticsearch 中存储事件数据（如 log 和 metric ）时要使用的通用字段集。OpenTelemetry 将创建一个专门的工作组来维护合并后的标准。该团队在周二举行的 Observability Day 上宣布了此次合并，该活动是 KubeCon+CloudNativeConEurope 2023 会议的一部分，地点位于阿姆斯特丹。

微软的 OpenTelemetry 项目代表 Reiley Yang 写道，结果将是“在可观测性和安全事件的不同支柱上获得更一致的信号。

## OpenTelemetry 的采用率不断增长

Parker 表示，OpenTelemetry 正在跨行业获得越来越多的关注，大多数公司现在都有一定程度的采用。

“我们正在从较小的预生产或内部工作负载转向全面生产、更重要的工作负载，并超越那些较小的 Kubernetes 集群，进入更大的集群，” Parker 说。 “那是因为该项目仍在快速发展和变化。”

遥测供应商也加入了这一努力。最近，可观测性公司 Sumo Logic 宣布它“全面支持” OpenTelemetry ，周二，Lightstep/ServiceNow 表示将“深化”其对 OpenTelemetry 项目的承诺，通过“使客户能够在采用本地 OpenTelemetry 工具时跨环境运行非供应商特定组件以实现完整的遥测可移植性。” 具体而言， ServiceNow 的 Lightstep 团队将提交开源和上游所有由 Lightstep 工程团队生成的 OpenTelemetry 增强功能。

“在 Lightstep，我们看到许多组织都在努力应对‘云原生标签冲击’，因为他们开始明白这些复杂的系统需要跨架构和专有解决方案筛选大量数据，”该公司在其公告中表示。 “在当今的宏观经济环境中，组织希望在推动创新的同时降低成本，尤其是在云原生应用方面。”

OpenTelemetry 可以帮助公司找到这些节省，这可能是其在宏观经济环境下迅速流行的原因。

“我们所看到的，尤其是在这些正在经历云转型的非常大的组织中，Kubernetes 对他们来说有点陌生，”Parker 说。 “随着他们添加更多服务，变得越来越复杂，它只会变得越来越混乱，而他们现有的工具并不能真正涵盖它。”

这就是 OpenTelemetry 通过提供收集数据、建模数据和汇集不同数据源的标准发挥作用的地方。

“可观测性不是一组产品。这是你如何使用所有这些数据来了解你的系统的实践，要了解你的系统，你需要的不仅仅是日志，你需要的不仅仅是指标，你需要的不仅仅是跟踪，”Parker 说。 “我们将它们整合在一起，帮助您将这些不同类型的数据叠加在一起，这样您就可以获得更好的问题答案，从而真正了解正在发生的事情。”

他补充说，所有这些都可以带来更好的最终用户体验，因为它提供了对重要事项的洞察力。

通过理解，你可以真正关注绩效与我的最终用户之间的联系，我如何确保我的客户在使用我的应用程序时度过愉快的时光 - 我实际上是让他们感到高兴而不是拥有一堆不相关的性能指标，这些指标并不能真正告诉我发生了什么。” Parker 说。

