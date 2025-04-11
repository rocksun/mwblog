# OTel 与 Elastic 合作，让可观测性更易于访问

![用于：OTel, Elastic 合作，让可观测性更易于访问的特色图片](https://cdn.thenewstack.io/media/2025/01/f74f19ca-otel-elastic-collaborate-make-observability-more-accessible-1024x576.jpg)

目前来看，可观测性工具并非人人都能访问。开放标准在一定程度上简化了互操作性并减少了供应商锁定，但花时间充分理解和采用许多不同的标准本身就是一项挑战。Elastic 希望通过与 [OpenTelemetry](https://opentelemetry.io/) (OTel) 的合作来加速采用，OpenTelemetry 是一个开源的、供应商中立的遥测 API、软件开发工具包 (SDK) 和用于分析软件性能和行为的工具集合。

Elastic 与 OpenTelemetry 的合作在 2023 年加速，当时该公司[捐赠了 Elastic Common Schema (ECS)](https://thenewstack.io/opentelemetry-and-elastic-common-standard-comes-not-too-soon/)，并在 2024 年将 [Universal Profiling](https://sdtimes.com/softwaredev/elastics-donation-of-universal-profiling-agent-to-opentelemetry-further-solidifies-profiling-as-core-telemetry-signal/) 捐赠给了 OTel。“通过捐赠，我们正在帮助减少标准的数量，而不是拥有另一个计算标准，” Elastic Observability 的 OpenTelemetry 产品负责人 Miguel Luna 在接受 The New Stack 采访时解释说。“一旦发生这种情况，我们意识到 OpenTelemetry 是前进的方向，我们决定全力以赴，开始与社区合作。”

它已经全力以赴了。自从捐赠 ECS 以来，Elastic 一直是 OpenTelemetry 的三大贡献公司之一 —— 但 Luna 强调说，它的真正目标是看到 OpenTelemetry 取得成功。

## 标准化遥测数据：为什么重要

OpenTelemetry 为用户提供了一种标准化的方式来检测、生成、收集和导出跟踪、指标和日志。该项目在 [2024 年取得了重大进展](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) —— 并且在 [2025 年已经有很多值得期待的事情](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/)。

从 Luna 的角度来看，用户应该关注的是语义约定和资源属性：“有很多工具可以完成收集指标、日志和跟踪的工作，但并非所有数据都以相同的方式处理。现在，通过语义约定，我们可以就指标、日志或其他信号的名称达成一致，无论你使用什么机制来收集数据。”

通过这种方式，语义约定统一了遥测数据，并为统一的可观测性管道提供了前进的道路。同时，资源属性丰富了这些数据，以便更清楚地了解哪些实体发出了遥测数据。

标准化遥测数据使使用语义约定和资源属性能够将分散的可观测性管道整合到一个统一的框架中。反过来，这有助于为在多样化和异构环境中简化遥测管道铺平道路。

对于害怕供应商锁定的组织来说，这也是一个胜利。通过一致的、统一的遥测数据，你无需每次想要更换供应商时都重新检测你的应用程序。正如 Luna 解释的那样，“你的遥测数据变得更具可移植性。如果你决定要更换到不同的供应商，那么 OpenTelemetry 将允许你这样做。”

此外，语义约定和资源属性提供的统一性有望帮助团队进行调试和性能监控。通过以标准化方式丰富的信号，团队可以使用通用语言来关联不同的日志、跟踪和指标。使团队能够从相同的角度工作和诊断问题，从而简化了调试、监控甚至维护。对于许多组织来说，这与他们目前的方法完全不同。

“如今，大多数公司都在使用供应商的专有收集机制来收集一些信号，但这并不一定能保证以统一的方式来丰富这些信号，” Luna 解释说。虽然以这种方式工作当然并非不可能，但这使得解决问题和维护工作更加费力 —— 尤其是在处理后续更改（例如，构件升级）时。

## 统一的遥测数据驱动可访问性

统一性将简化管道，减少供应商锁定并简化调试活动，但也许最具影响力的将是它对可访问性的影响。根据 Luna 的说法，这是阻碍大多数组织的问题 —— 现在是时候让每个人都能更轻松地访问可观测性了。
“用户不应该关心他们正在观察的实体的遥测的所有细节，”Luna 断言。“用户关心实体；他们关心他们正在观察的事物。但是，当我们强迫他们关心你需要处理、转换和导出的日志、追踪和指标时，我们就设置了非常高的门槛。”

互操作性问题一直是可观测性市场的一大难题，有人推测这是[可观测性被严重低估的原因](https://thenewstack.io/the-looming-crisis-in-the-data-observability-market/)。在许多方面，问题的根源在于，到目前为止，数据处理和收集都是非常专有的。从历史上看，大多数用户都是从供应商的专有数据收集机制中获取遥测数据，这意味着他们有责任理解不同的标准和不同的数据处理方式。

当你放大并仔细观察这个问题时，Luna 说，它比大多数人意识到的还要复杂：“很多人认为，当你提到‘用户’时，它只是一个收集遥测数据的单个人，如果这个人理解这个过程，那么一切都很好。但现实情况却大相径庭。”

在实践中，通常情况下，大多数组织都有集中化的团队负责可观测性，例如，向平台工程团队（Kubernetes 即服务）或 [DevOps 团队](https://roadmap.sh/devops) 提供可观测性即服务 (OaaS)。这就是事情变得棘手的地方。整个平台工程团队不仅需要一种单一、统一的数据收集方式，而且他们还需要一个简单的解决方案来帮助其他团队（在本例中为应用程序团队） democratize（普及）他们的遥测/可观测性数据。

更令人困惑的是，基础设施/平台团队和应用程序团队通常有非常不同的激励机制。毕竟，应用程序团队希望专注于他们的工作——发展和改进他们的应用程序——而不是浪费时间成为可观测性专家。

问题就在这里。多年来，任何想要进行观察的人都需要具备一定的专业知识才能处理遥测数据。但也许潮流正在开始转变。根据 Luna 的说法，这正是 Elastic 正在帮助做出改变的地方。

## OpenTelemetry 采用者仍然面临挑战

如果可观测性的未来是简化和更流畅的用户体验，那么 OpenTelemetry 确实朝着正确的方向迈出了一步——新的 [Elastic Distributions of OpenTelemetry (EDOT)](https://www.elastic.co/observability-labs/blog/elastic-distributions-opentelemetry) 正在提供帮助。

EDOT 的开发旨在增强标准 OpenTelemetry 发行版的功能，并通过 Elastic 为 OpenTelemetry SDK 和组件提供商业支持。Luna 说，EDOT 的真正目标是简化部署和配置，以创建开箱即用的体验，以便任何想要使用 OpenTelemetry 的人都能获得一致的体验。此外，如果他们遇到问题，他们可以从 Elastic 的支持团队获得帮助。这是一个值得注意的进步，但 OpenTelemetry 的采用仍然面临更多挑战。

对许多人来说，最大的障碍是设置和维护 OpenTelemetry 管道。特别是对于那些没有与特定接收器（例如，[Kubernetes](https://roadmap.sh/kubernetes)）进行内置集成的用户，他们必须努力了解如何使用 OpenTelemetry。正如 Luna 所分解的那样，“这些用户可能能够从端点收集遥测数据，但由于收集器不知道数据来自哪里，用户将不得不更多地参与进来。”在其他情况下，可能会有一个接收器可用，但它可能不是特定于技术的；用户将再次需要深入了解 OpenTelemetry，以便将数据转换为与 OpenTelemetry 兼容的信号。

Luna 还指出，OpenTelemetry 具有混合成熟度状态：“收集器是一台经过实战考验的机器，但有一些接收器、处理器和导出器是新贡献的。你需要考虑：这些组件的稳定性如何？它们是否得到适当的维护？”

同样，这就是 EDOT 应该提供帮助的地方。Luna 说，Elastic 已经精心策划了一套稳定、广泛使用的接收器、处理器和导出器。然后，所有 OTel 信号都存储在 Elasticsearch 中，这是一个以原生方式保留 OTel 数据的统一后端。Kibana 通过专用的内容包增强了这一点，为无缝分析提供仪表板和资产。“我们有意识地选择我们要引入的组件。我们还让用户清楚地了解我们如何支持这些组件并为用户提供支持，”他补充道。
尽管如此，即使有了 EDOT 包含的配置，Luna 提醒说，用户仍然需要考虑他们的具体情况，以及哪种级别的支持最适合他们的组织。虽然有些团队使用社区级别的支持就足够了，但其他有更高要求和更严格的服务级别协议 (SLA) 的团队将需要更多的支持。对 EDOT 所做的所有增强和修复都会定期向上游提交回 OpenTelemetry。

## 从目的出发：了解 OpenTelemetry 的影响

对于想要采用 OpenTelemetry 并增强其可观测性实践的组织，Luna 提出了一些建议。

首先要考虑的是你的动机：你为什么要采用 OpenTelemetry？在开始之前明确这一点将帮助你更好地理解为了与 OpenTelemetry 的数据模型保持一致，你可能需要在短期内放弃什么。除此之外，他认为理解语义约定是顺利采用 OpenTelemetry 的关键：“如果你要采用 OpenTelemetry，你应该理解它对你为什么重要，以及你将如何使用它。”

再一次，一切都归结为理解和可访问性。可观测性通常是一个相当不透明的游戏，只有对可观测性的来龙去脉有深刻理解的玩家才能获得真正的优势。这是有问题的，因为它创建了更高的进入门槛，增加了复杂性并促进了供应商锁定。但通过与 OpenTelemetry 的合作，Elastic 正在朝着不同的方向推动行业发展，在这个方向上，可观测性对更广泛的用户来说更容易访问。

*通过开放标准和简化的数据收集，转变你组织的可观测性战略。阅读“实现 OpenTelemetry 原生可观测性的商业价值”以了解更多信息。*

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)