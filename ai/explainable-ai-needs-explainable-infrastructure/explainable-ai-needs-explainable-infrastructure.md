
<!--
title: 可解释的AI需要可解释的基础设施
cover: https://cdn.thenewstack.io/media/2025/04/c67639a2-emile-perron-xrvdyzrgdw4-unsplash-scaled.jpg
summary: AI模型性能骤降？竟是基础设施在作祟！可解释AI需可解释基础设施！用`OpenTelemetry`追踪推理管道，`Grafana`可视化指标，配置告警应对延迟。统一可观测性，主动告警，定期审查，打造可信赖的AI系统！
-->

AI模型性能骤降？竟是基础设施在作祟！可解释AI需可解释基础设施！用`OpenTelemetry`追踪推理管道，`Grafana`可视化指标，配置告警应对延迟。统一可观测性，主动告警，定期审查，打造可信赖的AI系统！

> 译自：[Explainable AI Needs Explainable Infrastructure](https://thenewstack.io/explainable-ai-needs-explainable-infrastructure/)
> 
> 作者：Pronnoy Goswami

在开发 AI 系统时，您是否曾经花费数天甚至深夜的时间，最终才意识到真正的问题深藏在您的基础设施层中？最近，我在开发一个 AI 系统时就遇到了完全相同的挑战。令我惊讶的是，我推断出：

模型准确性的突然下降或不一致不是由错误的模型引起的。然而，它们根植于细微的基础设施问题，例如延迟峰值或其他错误配置。

从这个根本原因分析中，我了解到，实现真正的可解释 AI (XAI) 不仅需要模型的透明性，还需要构成 AI 模型基础的基础设施层的透明性。我将这种方法称为“可解释的基础设施”，它弥合了透明性和运营可观测性之间的关键差距。

## 现实问题：无法解释的模型性能下降

我当时正在构建一个高流量的推荐系统。突然，我观察到预测准确性突然且无法解释的下降。在对模型本身进行了严格的调查后，我发现根本原因可以追溯到分布式存储系统中的间歇性延迟问题，在本例中为 [AWS Simple Storage Service (S3)](https://aws.amazon.com/s3/)。

根据 [Gartner 2023 年的报告](https://www.gartner.com/en/articles/what-s-new-in-artificial-intelligence-from-the-2023-gartner-hype-cycle)关于云基础设施可靠性的报告，**47%** 的 AI/ML 系统计划外停机源于基础设施错误配置，包括网络延迟和存储瓶颈。

## 为什么基础设施透明性很重要

AI 模型的性能取决于底层基础设施的可靠性。数据库延迟、网络性能和内存分配等基础设施的基本要素会间接影响 AI 模型的决策，从而引入细微但影响重大的偏差或不准确性。

正如 [Google Cloud SRE Handbook, 2022](https://sre.google/sre-book/monitoring-distributed-systems/) 中所述，分布式系统中的延迟峰值导致 **~35%** 的 AI 模型性能下降，通常伪装成**模型漂移**。

为了解决这个问题，我利用了通常用于大规模分布式系统中的可观测性技术，特别是**分布式追踪**。这使我们能够弥合基础设施指标和 AI 模型预测之间的差距。

## 可解释的 AI 基础设施的架构

为了可视化组件如何交互，请考虑以下简化的架构：

*图 1. 基础设施设置的架构图*

用于 AI 推理管道的 OpenTelemetry 设置

以下是我如何将 [OpenTelemetry](https://opentelemetry.io/docs/concepts/instrumentation/libraries/) 集成到我们的 AI 推理管道中，以实现从基础设施到模型决策的透明性。

**我的 OpenTelemetry 设置：** 我们初始化 OpenTelemetry 以跟踪和捕获整个推理管道中的详细 span，从而提供对延迟和性能瓶颈的精细可见性。

```python
# OpenTelemetry setup
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
jaeger_exporter = JaegerExporter(agent_host_name="localhost", agent_port=6831)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# implement distributed tracing
def ai_inference(input_data):
    with tracer.start_as_current_span("ai_inference_pipeline") as span:
        infra_latency = measure_storage_latency()
        span.set_attribute("storage_latency_ms", infra_latency)
        prediction = run_model(input_data)
        span.set_attribute("model_prediction", prediction)
        return prediction

# measuring storage latency for calls to AWS s3
def measure_storage_latency():
    start_time = time.time()
    perform_user_query()
    latency_ms = (time.time() - start_time) * 1000
    return latency_ms
```

*代码 1. 用于 AI 推理管道的 OpenTelemetry 设置*

### 使用 Grafana 仪表板可视化指标

我们创建了 Grafana 仪表板，以将 [基础设施事件与 AI 模型性能相关联](https://thenewstack.io/cios-heed-on-premises-app-and-infrastructure-performance/)。这是一个简化的配置：
**用于延迟可视化的 Grafana 仪表盘面板：** 此面板以可视化方式跟踪[随时间变化的存储延迟](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/)，从而可以立即识别潜在的基础设施瓶颈。

```
123456789101112131415161718 |
{ "title": "Storage Latency", "type": "graph", "datasource": "Jaeger", "targets": [ { "expr": "rate(storage_latency_ms[5m])", "interval": "1m" } ], "yaxes": [ { "format": "ms", "label": "Latency (ms)" }, {} ]} |
```

*代码 2. 用于测量延迟的 Grafana 仪表盘设置*

### 配置 Grafana 警报以应对延迟峰值

我们使用警报主动监控基础设施。为了检测延迟问题并发出警报，我设置了一个简单的 Grafana 警报规则：

```
1234567891011121314151617181920 |
{ "alert": { "conditions": [ { "evaluator": {"params": [300], "type": "gt"}, "query": {"params": ["A", "5m", "now"]}, "reducer": {"params": [], "type": "avg"}, "type": "query" } ], "executionErrorState": "alerting", "frequency": "1m", "handler": 1, "name": "High Storage Latency Alert", "noDataState": "no_data", "notifications": [] }, "title": "Storage Latency Alert", "type": "graph"} |
```

*代码 3. 配置警报以应对延迟峰值*

## 可执行的见解

**统一可观测性：** 将 AI 模型的指标与基础设施指标集成至关重要。 最终目标应该是跟踪系统的端到端健康状况。

**主动警报：** 设置基础设施级别的异常警报可以主动检测问题。 这样可以缩短修复补丁的交付时间，并改善用户体验。

**定期审查：** 在定期运营审查期间，[定期检查基础设施健康状况](https://thenewstack.io/automate-routine-tasks-with-an-ad-hoc-ansible-script/)以及模型性能。

这些可解释的基础设施实践，尤其是通过可观测性，可以帮助组织大幅缩短故障排除时间。 这是思维方式的重大转变，调试变得**主动**而非**被动**。 因此，显着提高了系统可靠性并建立了对 AI 解决方案的信任。

## 最后的想法

依我拙见，基础设施可观测性和可解释 AI 的交叉领域已经成熟，可以进行创新。 未来的 AI 系统将大量依赖于透明的基础设施可观测性工具、方法和流程。 这确保了利益相关者承担更大的责任，并在使用 AI 系统时建立最终用户的信心。[麻省理工科技评论，2024](https://www.technologyreview.com/2024/01/04/1086046/whats-next-for-ai-in-2024/) 在他们的研究中指出 -

值得信赖的 AI 的下一个前沿领域不仅仅是可解释的模型，而是可解释的基础设施。

可解释的 AI 基础设施不仅仅是一种技术解决方案； 它是构建值得信赖的、可靠的 AI 的基础和必要条件。 我很想听听您的想法——您如何确保 AI 系统的透明度？

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)