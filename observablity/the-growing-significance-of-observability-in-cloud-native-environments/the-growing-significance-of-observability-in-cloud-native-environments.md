<!--
title: 云原生环境中可观测性日益增长的重要性
cover: https://cdn.thenewstack.io/media/2025/03/8ffd6ae8-fast-glass-fx-lxtcrejbjnm-unsplash-scaled.jpg
summary: 云原生可观测性迎来AI驱动时代！预测性监控、异常检测助力快速定位问题。拥抱OpenTelemetry标准化遥测数据，降低运营成本。DevSecOps融合安全与可观测性，FinOps实现成本优化。未来可观测性将更智能、更安全、更经济！
-->

云原生可观测性迎来AI驱动时代！预测性监控、异常检测助力快速定位问题。拥抱OpenTelemetry标准化遥测数据，降低运营成本。DevSecOps融合安全与可观测性，FinOps实现成本优化。未来可观测性将更智能、更安全、更经济！

> 译自：[The Growing Significance of Observability in Cloud Native Environments](https://thenewstack.io/the-growing-significance-of-observability-in-cloud-native-environments/)
> 
> 作者：Vimal Patel

想象一下这个场景：午夜时分，一个全球在线零售平台突然面临交易失败的激增。运营团队赶紧确定问题，但他们传统的监控工具只产生高级指标，无法查明根本原因。经过几个小时的故障排除，他们发现第三方支付 API 存在延迟问题。随着当代云架构变得越来越复杂，这种情况正变得越来越频繁。

这就是云原生可观测性发挥作用的地方。

在 2025 年，可观测性将超越基本的日志指标和追踪，整合 AI 开源框架和安全导向的策略，以生成对系统行为的广泛洞察。让我们来看看[塑造可观测性未来的关键趋势](https://thenewstack.io/trend-report-merging-observability-and-it-service-management/)。

## AI 支持的可观测性

### 在问题发生之前预见问题

被动可观测性的时代已经成为过去。通过将 AI 和机器学习整合到可观测性平台中，团队可以有效地转向预测性监控。AI 支持的可观测性解决方案评估历史数据，查明模式，并在潜在问题影响用户之前预测这些问题。例如，AI 驱动的异常检测可以发现[微服务响应时间的微小变化，并在服务中断之前提醒工程师](https://thenewstack.io/what-does-a-platform-engineer-do-and-do-you-need-one/)。像 New Relic 和 Dynatrace 这样的公司正处于改进 AI 驱动的洞察力的前沿，我们预计到 2025 年，在[与根本原因分析相关的自动化](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/)、自主系统和动态可观测性仪表板方面将取得重大进展。

### AI 在可观测性中的主要优势

- 更快的事件解决：AI 通过改进根本原因分析过程来减少平均检测时间 (MTTD) 和平均恢复时间 (MTTR)。
- 主动性能增强：预测分析使工程团队能够在潜在的性能问题之前调整应用程序。
- 警报噪音缓解：AI 区分重要警报和非关键警报，将注意力集中在重要事项上，同时最大限度地减少警报疲劳。

## OpenTelemetry 和开源可观测性标准

由于供应商锁定在可观测性领域提出了相当大的挑战，因此 OpenTelemetry (OTel) 和开源可观测性标准现在已准备好彻底改变该行业。作为收集分布式追踪、指标和日志的领先标准，OpenTelemetry 正在[云服务](https://thenewstack.io/pros-and-cons-of-cloud-native-to-consider-before-adoption/)提供商和企业中得到强劲采用。

到 2025 年，OpenTelemetry 的生态系统预计将进一步扩大，具有改进的集成、增强的追踪可视化功能以及[对](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/)事件驱动架构的更好支持。越来越多的组织可能会从专有代理过渡，转而选择 OTel 的多功能性，以在混合和多云设置中检测应用程序。

**OpenTelemetry 的意义**

- 标准化：一个用于在多个环境中收集遥测数据的全方位框架。
- 互操作性：与云原生可观测性工具（包括 Prometheus Grafana 和 Jaeger）的平滑集成。
- 成本效益：通过消除对各种专有代理的需求来降低运营费用。

## 在 Kubernetes 中设置 OpenTelemetry 以进行分布式追踪

为了帮助您开始使用 OpenTelemetry，这里有一个关于[如何在 Kubernetes 中实现分布式追踪](https://thenewstack.io/how-to-run-databases-on-kubernetes-an-8-step-guide/)设置的详细指南。

**步骤 1：部署 OpenTelemetry Collector**

创建一个专门用于可观测性的 Kubernetes 命名空间。

```bash
kubectl create namespace observability
```

通过 Helm 部署 OpenTelemetry Collector。

```
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts 
helm repo update
helm install otel-collector open-telemetry/opentelemetry-collector -n observability
```

**步骤 2：为你的应用埋点**

将 OpenTelemetry SDK 集成到你的应用程序中（Python 示例）。

```bash
pip install opentelemetry-sdk opentelemetry-exporter-otlp
```

配置应用程序以将跟踪信息转发到 OpenTelemetry Collector。

```python
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter
tracer_provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://otel-collector:4317"))
tracer_provider.add_span_processor(processor)
```

**步骤 3：在 Jaeger 中可视化追踪**

部署 Jaeger 以进行追踪可视化：

```bash
kubectl apply -f https://raw.githubusercontent.com/jaegertracing/jaeger-kubernetes/master/all-in-one/jaeger-all-in-one-template.yml
```

访问 Jaeger UI：

```bash
kubectl port-forward svc/jaeger-query 16686:16686 -n observability
Open http://localhost:16686 in your browser to view traces.
```

Open http://localhost:16686 在浏览器中打开以查看追踪。

通过执行这些步骤，你可以实时了解微服务交互，并更有效地检测性能瓶颈。

## DevSecOps：安全与可观测性的融合

安全性不再是一个独立的功能，它正成为可观测性不可或缺的一部分。随着组织[实施 DevSecOps](https://thenewstack.io/5-steps-to-implement-devsecops/) 工作流程，对安全监控的关注向左转移，从而可以在软件开发生命周期中更早地检测到安全漏洞。例如，[可观测性工具现在通过审查应用程序](https://thenewstack.io/application-delivery-controllers-a-key-to-app-modernization/)日志中是否存在可能表明安全漏洞的不规则模式，从而实现实时威胁检测。到 2025 年，安全可观测性将包括：

- SBOM（软件物料清单）监控，以发现软件依赖项中的漏洞；
- 运行时安全可观测性，用于识别和缓解发生时的威胁。
- 合规性自动化，以保证云环境符合 GDPR 和 HIPAA 等监管标准。

## FinOps 对可观测性支出的影响

可观测性会产生大量成本，并且随着组织增强其遥测数据收集，云支出可能会迅速增加。这就是 FinOps（云财务管理）变得不可或缺的地方。

在 2025 年，许多公司将拥抱具有成本意识的可观测性，从而平衡可见性和财务限制。受 FinOps 启发的观测策略将包括：

- 智能数据保留：保留高价值的遥测信息，同时消除多余的日志。
- 动态采样率：调整跟踪采样以响应系统工作负载波动。
- 基于云的成本分析：提供有关可观测性支出的见解，以实现有效的成本管理。

## 最后的思考

可观测性的演变 随着云原生技术的采用加速，可观测性已成为确保性能可靠性和安全性的重要因素。随着 AI 驱动的分析、开源遥测安全集成和经济高效的方法的出现，组织已做好充分准备，可以在未来增强其可观测性框架。

在未来的几年中，采用这些创新的工程团队将能够更好地管理与现代云环境相关的复杂性。无论你是 DevOps 工程师、站点可靠性工程师 (SRE) 还是安全分析师，现在都是重新评估你的可观测性策略并为即将到来的创新做好准备的绝佳时机。