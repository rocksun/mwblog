# OpenTelemetry 和 Elastic Common Schema 来得正是时候

通过 OpenTelemetry  和 Elastic Search 之间的合作，这正是标准化势在必行的时刻。

翻译自 [OpenTelemetry and Elastic Common Schema Comes Not Too Soon](https://thenewstack.io/opentelemetry-and-elastic-common-standard-comes-not-too-soon/) 。

![](https://cdn.thenewstack.io/media/2023/06/406b7811-maarten-van-den-heuvel-s9xmnem-m9c-unsplash-e1687452871739-1024x681.jpg)

标准化始终是一件好事，但当涉及到非常流行和广泛使用的工具和技术时，至少有一个共同的标准会让开发人员的生活变得更加轻松。而在另一个极端，一个技术的生存取决于是否有共同的标准。这正是 WebAssembly 的情况，关于对组件的共同标准的迫切需要，以便可以在任何类型的设备上使用 Wasm 高效地部署代码。今天我们讨论的是可观测性工具 [Elastic Common Schema（ECS）](https://www.elastic.co/guide/en/ecs/current/index.html)和 [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) 的结合。具体来说，开源 Elastic 的创建者正在为 OTel 贡献 ECS ，并致力于[两个项目的联合开发](https://www.elastic.co/guide/en/ecs/current/ecs-using-ecs.html)。

## 第二高速项目

由于用户基础的强劲增长，在 [CNCF](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/) “[velocity project](https://www.cncf.io/blog/2023/01/11/a-look-at-the-2022-velocity-of-cncf-linux-foundation-and-top-30-open-source-projects/)”  中，OpenTelemetry 成为第二高速项目。OpenTelemetry 已成为广泛采用的方式，用于为应用程序添加 instrumentation ，从您喜欢的可观测性来源收集指标、日志和跟踪。然后，来自不同来源的遥测数据（指标、日志和跟踪）可以组合起来进行监控，例如使用 [Grafana](https://grafana.com/) 等喜爱的面板。广受欢迎的 ECS 用于定义在 [Elasticsearch](https://thenewstack.io/properly-monitor-elasticsearch/) 中存储事件数据（如日志和指标）时要使用的一组常见字段，以及每个字段的特定字段名和 Elasticsearch 数据类型，并根据文档提供描述和示例用法。在 OTel 的框架下， ECS 将变得更加出色。事实上，机器学习正在与 Elastic 集成，该集成已经提供了一些非常有趣的结果。通过 OpenTelemetry 和 Elastic Search 之间的合作，这正是标准化势在必行的时刻。" ECS 和 OpenTelemetry 之间的这种合作是天作之合，"企业管理协会（EMA）的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 说道。" ECS 解决了真正可见性和可观测性的最关键瓶颈：为所有遥测数据创建和维护一个共同的数据模型。"

## 开发者的选择

现在，OpenTelemetry 可以可靠地从 Python、C#、JavaScript 或开发者选择的语言中收集数据字段，从各种 APM 工具和基准测试平台中填补通常会减慢或完全阻止应用程序监控的上下文差距，Volk 说。

"例如，电子商务平台在闪购期间突然遇到服务器负载激增。由于不同服务使用不同语言编码，并由不同 APM 工具监控，根因分析将会变得棘手，" Volk 说道。"但是有了共同的数据模型，所有不同的语言和 APM 工具都将它们的遥测数据转储到一致的 JSON 文件中，今天的魔法 AI 驱动的可观测性平台可以轻松分析这些数据。进一步思考， ECS 标准可以帮助 OpenTelemetr y分析来自当今异构智能设备宇宙的资产信息，并向开发人员报告哪些设备与他们最新的代码创作效果最佳，更重要的是，哪些设备与其最新的代码创作效果最差。

对于 OpenTelemetry 用户来说， ECS 对 OTel 的贡献将产生积极影响，这适用于 OpenTelemetry 正在开发的日志记录功能的用户， Splunk 的产品管理总监 Morgan McLean 说。这是因为除了 OpenTelemetry 的收集器代理和语言 instrumentation 之外，该项目最大的吸引力之一是其统一的语义约定，确保每个信号都附有一致的元数据和资源信息， McLean 说。

例如，从使用不同语言编写的服务中捕获的 HTTP 请求的跨度将共享相同的键和值编码，以表示其持续时间、URL、服务名称、主机等等，这样可以"有效地对其进行分析，" McLean 说。

"虽然在 OpenTelemetry 中的 span 和指标已经如此，但我们正在努力支持日志记录，这引入了更多需要专用语义约定的场景，" McLean 说。"通过将 ECS 及其数千个现有约定合并到 OpenTelemetry 中，每个使用 OpenTelemetry 的人都将在各种情况下获得结构良好且一致的日志、跟踪、指标等元数据。这些信号可以被高效地处理、过滤、比较和分析，而无需大量特殊情况逻辑或忽略缺乏预期元数据的信号。"

## ECS 和 OTel

ECS 与 OTel 的集成凸显了 OTel 的影响力以及其创建者的目标，即允许用户将遥测数据合并到一个单一面板中，以进行更全面的可观测性分析。 Grafana Labs的高级产品经理 Cedric Ziel 在总体上描述了 OTel 的这个方面，而没有具体评论 ECS 对 OTel 的贡献，他指出 OpenTelemetry 是一个社区驱动和 CNCF 治理的倡议，旨在将可观测性的数据收集问题通用化。

"OpenTelemetry 的理念是关于应用程序代码的供应商中立 instrumentation ，该项目的目标是消除每当想要倾向于不同的可观测性提供商或同时支持多个供应商时需要更换 instrumentation 的需求。这解决了我们时代的可观测性问题：您需要多个供应商来支持不同方面的需求- 在这方面达成相同的协议和约定是可观测性的终极目标，" Ziel 说道。" OTel 中的变化并不仅仅是一个单一的吸引点：它是一个整体。看到所有信号类型在 instrumentation 库中更可持续地可用是一个持续的努力，让人兴奋不已。

的确， ECS 与 OTel 的集成有助于 OTel 项目朝着与任何可观测性工具或流程的完全兼容和标准化的最终目标迈进。

"自第一天起， OpenTelemetry 一直专注于为云原生系统提供一致、清晰和准确的遥测数据，以赋予开发人员和运维人员可观测性的能力。 ECS 和 OpenTelemetry 语义约定的对齐是这一旅程的又一步，确保高质量和一致的元数据可供最终用户使用，" [Lightstep](https://lightstep.com/) 的开发者关系负责人 Austin Parker 说道。"此外，这一步骤确保 OpenTelemetry 数据将成为由人工智能驱动的下一代可观测性工具的黄金标准，为最终用户提供关于其系统及其状态的更好答案。"


