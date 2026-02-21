关于[Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/)和[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)之间常被误解的争议，更多是源于技术不兼容，而这些不兼容现已得到解决。不深入探讨这些争议的历史，可以说Prometheus仍然是[Kubernetes](https://thenewstack.io/kubernetes/)部署中指标的黄金标准。

OpenTelemetry作为Prometheus的管道，通过分布式追踪，以及最近的日志来对其进行补充。尽管OpenTelemetry主要提供推式（push-based）方法，但与OpenTelemetry一起使用时，Prometheus可以继续作为拉式（pull-based）系统运行，或者作为指标和可观测性分析的独立选项。双方都在持续取得进展。

具体来说，在布鲁塞尔[FOSDEM 2026](https://fosdem.org/2026/)之后，最近举行的[OTel Unplugged EU](https://opentelemetry.io/blog/2025/otel-unplugged-fosdem/)会议上，就OpenTelemetry和Prometheus集成的巨大改进进行了富有成效的讨论和描述。这些改进的一个关键催化剂是Prometheus现在支持UTF-8以及其他[OTLP](https://thenewstack.io/search/)-原生增强功能。Prometheus对UTF-8的支持主要体现在指标名称和标签中使用点、破折号和其他非字母数字符号。这在过去一直是协调OpenTelemetry标签和属性的语义约定的一大障碍，在两者集成时构成巨大挑战。

[UTF-8](https://en.wikipedia.org/wiki/UTF-8)被构建为一种文本标准，涵盖语言、符号和表情符号。在过去，Prometheus和OpenTelemetry之间不同的命名约定一直让开发人员和实践者头疼不已。

但现在，随着对标签、注释、指标名称的Unicode字符支持，以及其他方面的改进，它显然促进了两者的集成。

“OpenTelemetry和Prometheus现在正在领导层面探讨如何更紧密地合作，现在Prometheus支持UTF-8和其他由OpenTelemetry引发的改变，OpenTelemetry可能会吸取Prometheus一些经过实战检验的规范、代码和导出器。”[Grafana Labs](https://grafana.com/)社区总监Richard “RichiH” Hartmann说，“对用户来说，这意味着更少的摩擦和更少的选择困扰。希望将来做某些事情会有一种单一的方式。它将在双方以相同的方式工作，并且高效有效。”

## 深度背景

已经依赖Prometheus获取遥测信号的组织通常会觉得有必要添加OpenTelemetry来补充其指标，并将其追踪和日志添加到其[可观测性](https://thenewstack.io/introduction-to-observability/)数据流中。这样做通常被认为是冒着破坏未损坏事物的风险，同时可能通过为指标实施OpenTelemetry而增加其环境的复杂性。OpenTelemetry和Prometheus之间的兼容性问题已随着[Prometheus 3.0](https://prometheus.io/blog/2024/11/14/prometheus-3-0/)的发布而基本解决。

Prometheus现在与OpenTelemetry良好集成，并仍然是生态系统核心的一部分。这种竞争只是表面上的。话虽如此，Prometheus 2.0在通过OpenTelemetry用作指标后端时确实带来了挑战，早期使采用变得复杂。

兼容性问题可以追溯到Prometheus 3.0发布之前。在非常基本的层面上，存在设计理念上的差异。Prometheus内部与数据格式相关的兼容性问题，特别是直方图（histograms）和数据转发协议（data forwarding protocol），现在通过原生直方图（Native Histograms）和OTLP摄取（OTLP ingestion）等功能在Prometheus 3.0中得到了原生支持。

随着Prometheus 3.0的发布，已经有许多改进使得通过OpenTelemetry收集指标比过去更好、更少痛苦。虽然如上所述仍存在一些小的边缘情况，但工作仍在进行中，在开源社区的支持下，我可以亲身证实，目前有很多动力来克服这些问题，这些问题将在未来的Prometheus版本中得到解决。

这是Prometheus发挥作用的一个领域。当前的努力包括积极转换这些标签，使其更符合Prometheus和Mimir定义的约定，以改善数据的结构和可整理性。