
<!--
title: Prometheus集成OpenTelemetry：这些“顽疾”急需根治！
cover: https://cdn.thenewstack.io/media/2025/11/32fce064-getty-images-mx88anchvle-unsplash-1.jpg
summary: OpenTelemetry与Prometheus集成挑战多：丢失拉取和健康监控，OTel SDK复杂且性能差。虽有改进，如直方图兼容，但仍需解决服务发现、命名规范和性能问题，以实现更好融合。
-->

OpenTelemetry与Prometheus集成挑战多：丢失拉取和健康监控，OTel SDK复杂且性能差。虽有改进，如直方图兼容，但仍需解决服务发现、命名规范和性能问题，以实现更好融合。

> 译自：[Fixes Required for Prometheus’ OpenTelemetry Integration](https://thenewstack.io/fixes-required-for-prometheus-opentelemetry-integration/)
> 
> 作者：B. Cameron Gain

我们已经讨论了 [OpenTelemetry 和 Prometheus 之间的一些冲突](https://thenewstack.io/prometheus-and-opentelemetry-just-couldnt-get-along/)，原因诸多。其中很大一部分原因是 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) 曾是——并且仍然是——一个久经考验、备受信任的开源指标解决方案，它先于 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 提供的标准化替代方案以及其他在可观测性方面确实出色的特性。

在最近于慕尼黑举行的 Prometheus 年度用户大会 [PromCon](https://promcon.io/) 上，Prometheus 联合创始人 [Julius Volz](https://www.linkedin.com/in/julius-volz/?originalSubdomain=de) 在开幕主题演讲中深入阐述了将 OpenTelemetry 与 Prometheus 结合使用仍存在的问题以及如何解决这些问题。

首先是坏消息：使用 OpenTelemetry 时，服务发现和主动拉取功能会从根本上丢失，而且 OpenTelemetry SDKs 的复杂性也是一个问题。性能问题也比比皆是。在一个基准测试中—— [RevCom](https://standards.ieee.org/about/sasb/revcom/) 尚未验证——Volz 指出，与原生 Prometheus 检测相比，使用 OpenTelemetry 检测时，[Go](https://thenewstack.io/introduction-to-go-programming-language/) 基准测试的速度差异高达 22 倍。

显然，提高性能是关键，特别是对于旨在提高性能并频繁运行的可观测性代码。但正如我们在之前的文章中讨论过的，语义约定也带来了问题。Prometheus 和 OpenTelemetry 团队之间也需要持续协作。

Volz 说：“我确实想指出 [将 OpenTelemetry 与 Prometheus 集成] 的缺点，或许能让你们思考一下，‘如果我们主要关注指标并将其与 Prometheus 结合使用，我们真的想走这条路吗？’”，“此外，就服务发现和 SDK 慢的缺点而言，我真诚地希望其他人能对此进行更多思考，或许能改进一些东西，而不是因噎废食，失去我们在 Prometheus 中长期以来精心构建的所有这些优势。”

自 [Richard “RichiH” Hartmann](https://www.linkedin.com/in/richih/?originalSubdomain=de)（他的职务是 Grafana Labs 社区总监）于 2020 年开始正式努力改善这两个项目之间的互操作性以来，已经取得了许多改进。

Hartmann 在会后告诉我，虽然 OpenTelemetry 缺乏服务发现功能将始终给操作员带来额外工作，但大多数根本问题都已解决。Hartmann 说，OpenTelemetry 已经改变，可以说修复了，其直方图桶定义以支持 Prometheus。“Prometheus 随后扩展了对数据标签的支持以支持 OpenTelemetry，”Hartmann 说，“两个项目早期就基于 [Björn “Beorn” Rabenstein](https://www.linkedin.com/in/beorn7/) 的工作，在原生直方图方面进行了合作，最终双方都发布了完全兼容的版本。”

与此同时，Volz 说，OpenTelemetry “已经全面普及，并且不会消失，各组织寻求将其与 Prometheus 结合使用，使用 OpenTelemetry 检测其服务，然后将指标部分发送到 Prometheus 系统。” Volz 说：“然而，与使用 Prometheus 自己的原生检测客户端库相比，存在许多缺点。”“如果主要关注指标和 Prometheus，那么在选择 OpenTelemetry 路线之前了解这些很重要。”

两个系统的快速对比显示，Prometheus 是一个完整的监控系统，仅专注于指标信号类型。相比之下，Volz 说，OpenTelemetry “只关心”生成信号——包括 [日志、指标、追踪和配置文件](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/)——然后将它们传递给某种第三方后端系统。这与 OpenTelemetry 创建者旨在在排放方面进行标准化的目标相符，并反映了 OpenTelemetry 中代表的许多不同的存储供应商。

Volz 说，传输方式呈现出关键差异：OpenTelemetry 使用 [OTLP](https://thenewstack.io/why-google-clouds-otlp-support-matters-for-your-telemetry-pipeline/) 通过推送发送这些指标，而 Prometheus 使用基于文本的格式并主动拉取它们。Volz 说，通过 OpenTelemetry 收集器将指标发送到 Prometheus 服务器中的 OTLP 接收器端点会带来几个缺点。

## 失去主动拉取和健康监控

Volz 说，第一个也是最不幸的缺点是抛弃了许多使 Prometheus 优秀和强大的特性：将服务发现与基于拉取的主动目标监控相结合。Prometheus 通过与 [Kubernetes](https://thenewstack.io/kubernetes/) API 服务器等系统通信来解决这个问题，以获得始终最新的视图。Volz 说，然后它主动尝试拉取或抓取指标，记录一个值为零或一的 up 指标，这对于目标健康警报至关重要。

Volz 说，由于 OpenTelemetry 没有内置此功能，因此更难判断目标是正在运行但未发送指标，还是已宕机。相反，当推送意外指标时，安全控制会被绕过。Volz 说：“很多人完全忽视了这一点，把他们的 Prometheus 服务器当作一个随机的指标容器，然后他们不知道一个应该运行的进程是否没有运行。”“OTLP 摄取的人造 up 指标的想法已经有所耳闻，但目前尚不存在。”

Volz 说，第二个缺点是导致指标名称改变或有些“丑陋的 PromQL 选择器”。OpenTelemetry 引入了字符集差异，允许使用以前 Prometheus 3 不支持的点和斜杠等字符。Volz 说：“这表明 OpenTelemetry 的标准化人员没有高度优先考虑指标在 [PromQL](https://docs.cloud.google.com/monitoring/promql) 等查询语言中的使用方式。”

Prometheus 约定为单位和指标类型都添加了后缀，以立即阐明含义。然而，OpenTelemetry 表示“不要将单位和类型放入指标名称中。”结果是，Prometheus 摄取层在转换过程中会重新添加这些后缀。Volz 说，随着扩展字符集的使用，PromQL 选择器变得比原生选择器更复杂，更难编写和阅读。

事实上，OpenTelemetry 及其 SDK 相当复杂，而且可能相当慢。如上所述，Go 语言的基准测试表明，原生 Prometheus 客户端库在计数器增量方面比 OpenTelemetry SDK 快 22 倍。Volz 说：“即使添加两个标签，OpenTelemetry SDK 也会慢 90%。”“OpenTelemetry 的复杂性是内在的，难以去除，使其成为可观测性领域的 [XML](https://thenewstack.io/xslt-debate-leads-to-bigger-questions-of-web-governance/) 或 [CORBA](https://thenewstack.io/the-end-of-tribalism-in-software/)，因为它试图一次性解决所有问题。”

## 卷起袖子

Volz 说，为了解决健康检查问题，未来的工作可能涉及为 OTLP 摄取引入一个合成的 up 指标。Volz 说，这个功能将利用服务发现，并将预期数据与传入数据关联起来，在数据缺失时生成一个 up 指标。

Volz 说：“在指标方面，Prometheus 团队正在积极尝试改进，包括创建一个实验性的 Delta 到累积处理器，以支持 OpenTelemetry 的 Delta 时间性。”“对于 Prometheus 从一开始就没有语义约定也存在公认的遗憾，这表明未来与 OpenTelemetry 人员的合作可能有助于引入类似的标准化命名结构。”