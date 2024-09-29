# 为什么 Grafana 向初创公司提供 10 万美元用于可观测性

![用于“为什么 Grafana 向初创公司提供 10 万美元用于可观测性”的特色图片](https://cdn.thenewstack.io/media/2024/09/af5535be-alexander-mils-hyob4ml_yso-unsplash-1-1024x576.jpg)

纽约 - 本周在 [ObservabilityCON](https://grafana.com/events/observabilitycon/) 上，[Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) 宣布将向选定的初创公司提供 10 万美元的补助金。这项资金支持旨在减轻成本障碍，使初创公司能够专注于发展业务，而不会牺牲维持运营效率所需的 [可观测性](https://thenewstack.io/observability/)。

根据 Grafana 最近的一项研究，成本是组织的重中之重，尤其是在可观测性方面。对于初创公司来说，这种担忧尤为关键，因为它们通常资金有限，必须确保每项投资都能节省成本或产生收入和利润。

虽然普遍认为可观测性对于各种原因都是必要的——从管理基础设施到增强安全性，再到简化测试和 [CI/CD](https://thenewstack.io/ci-cd/) 等流程——但实施可观测性工具的成本可能是一个重大问题。即使是那些获得风险投资支持的公司，也很容易对那些似乎会增加额外财务负担的工具望而却步。


[@grafana]’s[@nopzor]: Grafana 成本方面向初创公司提供 10 万美元.. «我们不要求初创公司获得风险投资支持或位于美国.. »[#ObservabilityCon] 2024 年主题演讲。[@thenewstack][pic.twitter.com/gsbBStDJFj]— BC Gain (@bcamerongain)

[2024 年 9 月 24 日]
“显然，我们有一个开源项目，因此许多初创公司可以免费使用我们的开源软件，这是我们设计的。但是，我们注意到，对于那些不一定获得风险投资支持并且正在经历快速增长和扩展阶段的初创公司来说，存在差距——这显然是一个好问题，但对这些公司来说，它也带来了财务风险，”[Grafana Labs](https://grafana.com/) 联合创始人兼首席执行官 [Raj Dutt](https://www.linkedin.com/in/radutt) 在主题演讲中说。“特别是对于资金有限的初创公司来说，它们经常在重新投资于增长和维持运营之间左右为难。我们认为不必如此。”

虽然 [Grafana Cloud](https://thenewstack.io/grafana-extends-free-access-for-cloud-managed-observability/) 已经为任何用户提供了一个相当大的免费使用层级，但 Grafana 的补助金优惠可以说是属于扩展的免费使用计划，是对 Grafana 希望将导致成功的初创公司扩展可观测性需求的投资，而这种投资的基础是 Grafana 在可观测性领域的广泛影响力，以及开源的优势。Grafana 还希望展示如何使用 [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) 和许多其他开源替代方案，包括用于日志的 Loki、用于跟踪的 Tempo 和用于指标的 Mimir，来帮助组织管理其遥测数据和决策，从而在云价格持续上涨的情况下降低成本。

这些成本问题是 ObservabilityCON 的一个主要主题。演讲者强调，实施有效可观测性实践不仅可以提高运营效率，还可以用于降低与维护可观测性本身相关的成本。Grafana Labs 今年发布的一项研究还指出，关于可观测性的首要问题是成本，56% 的受访者将其列为他们最大的问题。可以理解的是，管理系统的复杂性紧随其后，为 50%，而基数位居第三。

有人可能会说，管理基数的挑战直接导致了更高的成本，因为它属于更广泛的财务问题范畴。这将使成本成为组织在实施可观测性时面临的各种挑战等级中更为重要的因素。

同样，信号噪声比也是一个挑战，它会让负责调试和过滤大量警报的人员感到头疼，34% 的受访者将其列为首要问题。此外，这一问题与资源成本相关联，比例为 30%，这进一步突出了许多可观测性挑战最终都与财务压力有关。

## 适应性
Grafana helps organizations save observability costs by focusing on "adaptive" metrics, logs, and traces. According to Grafana, customers using [adaptive metrics](https://thenewstack.io/why-did-grafana-labs-need-to-add-adaptive-metrics/) can reduce their metrics costs by 35% by lowering their bills through aggregation, identifying, and eliminating unused metrics. Grafana says that TeleTracking, a comprehensive healthcare operations platform provider, used adaptive metrics to reduce its billable metric series by 50%, lowering costs by 33%.

Grafana Labs announced at GrafanaCon that it is extending this "adaptive" concept to logs and traces, leveraging AI/ML technology to analyze observability data at a scale that manual processes cannot achieve. With the general availability of adaptive logs this week, adaptive logs help organizations reduce observability costs by reducing the number of unnecessary logs. Adaptive logs identify common log patterns and create a set of custom sampling recommendations based on the frequency of those patterns. This allows customers to prune away low-value logs so they only keep the logs that matter.

For adaptive tracing, Grafana Labs acquired the startup TailCtrl, an early-stage company founded by [Sean Porter](https://github.com/portertech), who is also the co-founder of Sensu.

In a presentation about adaptive metrics, [Oren Lion](https://www.linkedin.com/in/oren-lion/), Director of Software Engineering at healthcare services platform provider TeleTracking, noted that Grafana adaptive metrics act as "log levels for metrics." Lion said that adaptive metrics effectively reduce the verbosity of metrics. Since every label in a metric can potentially lead to the generation of many time series, adaptive metrics effectively reduce the number of labels in metrics, thereby reducing the number of time series generated.

The recommendations that adaptive metrics release allow organizations to automate the process of evaluating which metrics are necessary and where they are needed. The organization, through its use of an early version of Grafana Cloud adaptive metrics, quickly reduced its metrics costs. Within a few weeks, after addressing all the bugs and getting adaptive metrics fully up and running, they achieved a 50% cost reduction.

Lion described it as "custom metrics and dependency metrics," saying, "We built incredible metric generators." "Teams think about design and how to monitor services and dependencies, but they don't estimate and track the cost of monitoring services," Lion said. "In reality, the cost of metrics isn't in the plan until you get the bill, and then you're scrambling."


[@grafana] Jen Villa: Developers can get involved and reduce observability costs. Grafana Explore Metrics and Logs, using AI/ML is now generally available [#ObservabilityCon] 2024 keynote. [@thenewstack][pic.twitter.com/yXVB3ostSf]— BC Gain (@bcamerongain)

[September 25, 2024]
Meanwhile, in her presentation, [Jennifer Villa](https://www.linkedin.com/in/jevilla/), Director of Product Management for Grafana Databases, said, "The money-saving part can also be very interesting and exciting." However, "What I'm going to introduce you to is a deeper dive into what we talked about yesterday. The keynote was about applying AI/ML through our adaptive telemetry strategy to help everyone adopt observability at an increasingly larger scale, because we're making it more affordable than ever," Villa said. "We don't just want to make observability more cost-effective, but we also want to empower all the engineers in your organization to participate in the mission of improving costs, right? We don't want that responsibility to be in the hands of just a few."

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don't miss a single episode. Subscribe to our YouTube
channel to watch all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)