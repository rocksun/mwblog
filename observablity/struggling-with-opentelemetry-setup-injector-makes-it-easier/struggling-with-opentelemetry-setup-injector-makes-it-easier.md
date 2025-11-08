
<!--
title: OpenTelemetry 配置难？Injector 助你轻松上手！
cover: https://cdn.thenewstack.io/media/2025/11/9fbe49be-view.jpeg
summary: OpenTelemetry已成业务战略。Splunk捐赠Injector实现零代码检测，简化OTel实施，助企业加速采纳、深化业务洞察。2026年将推自动发现。
-->

OpenTelemetry已成业务战略。Splunk捐赠Injector实现零代码检测，简化OTel实施，助企业加速采纳、深化业务洞察。2026年将推自动发现。

> 译自：[Struggling With OpenTelemetry Setup? Injector Makes It Easier](https://thenewstack.io/struggling-with-opentelemetry-setup-injector-makes-it-easier/)
> 
> 作者：Morgan McLean

Splunk 年度《[2025 年可观测性状况报告](https://www.splunk.com/en_us/campaigns/state-of-observability.html)》的最新发现表明：OpenTelemetry 已从行业标准发展为一项业务战略。该项目已超越收集和传播可观测性数据的标准，它赋予用户灵活性和精细度来控制其数据，从而积极影响收入、运营利润和品牌形象。该项目还有助于加强人工智能的采用过程。

当组织采用 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 进行标准化时，他们正在[收集更丰富的数据](https://thenewstack.io/how-to-make-opentelemetry-better-in-the-browser/)，并为更好的生成式 AI (GenAI) 成果奠定基础。

[![OpenTelemetry 的益处超越了可观测性实践。](https://cdn.thenewstack.io/media/2025/11/06df76bf-image1a-1024x875.png)](https://cdn.thenewstack.io/media/2025/11/06df76bf-image1a-1024x875.png)

然而，尽管 OpenTelemetry 增长迅速并能够带来积极的业务成果，但对于某些组织而言，其[实施过程可能令人望而却步](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/)。虽然该项目的早期采用者必然完全拥抱云原生和分布式架构，但对于许多组织而言，由于对传统系统进行检测的困难，OpenTelemetry 的[实施工作](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/)有时是一个障碍。显然，社区仍有许多工作可以做，以使 OpenTelemetry 更易于实施且更直观，从而使所有组织都能获得其益处。

Splunk，以及 [Google](https://cloud.google.com/?utm_content=inline+mention)、Microsoft 和 LightStep（现为 ServiceNow），是 OpenTelemetry 最著名的贡献者之一，如今，Splunk 对该项目的最新捐赠——OpenTelemetry Injector——延续了这一传统。

简而言之，OpenTelemetry Injector 的捐赠使实施变得异常容易，并扩大了 OpenTelemetry 对拥有多样化基础设施的组织的影响范围和易用性。它为运行在 Linux 主机上的流行语言编写的应用程序实现了零代码检测，并显著降低了实施的操作负担。

借助 OpenTelemetry Injector，组织可以通过一个简单的步骤捕获其基础设施和应用程序的指标、跟踪、日志和配置文件，而无需更改应用程序代码或启动脚本。通过使检测更简单、侵入性更小，Injector 鼓励拥有现有应用程序且代码更改可能困难或不切实际的组织更广泛地采用 OpenTelemetry。

OpenTelemetry 是整个行业收集机器数据的实际标准。它庞大的集成集、一致的数据模型和语义约定、广泛的信号集、随时随地导出数据的能力、令人印象深刻的数据定制选项以及庞大的社区使其成为全球组织明确的选择。借助 Injector，组织可以更轻松地获得 OpenTelemetry 的所有益处。

此外，它还提供了一种加速项目采用的方法，以便更多组织可以通过增强 Kubernetes 功能并将其上游化的特性来获得其益处。其影响包括：

*   改进的日志规模，有助于减少噪音。
*   用于数据驱动决策的高级指标收集。
*   用于数据操作和路由的复杂管道功能，使数据与组织更相关。
*   支持 Kubernetes 注解和多行日志，以在容器化环境中实现有效且高效的**可观测性**。
*   零代码检测，允许在不更改源代码的情况下实现额外的**可观测性**应用程序。
*   敏感值遮蔽，以提高安全性和隐私性。

最近允许 OpenTelemetry 加速采用的最重要进展之一是自动发现。

自动发现功能将于 2026 年在项目中推出，它是一种零代码检测功能，可检测并收集来自第三方服务（如数据库和 Web 服务器）的信号数据。通过自动发现，收集器会自动生成一个配置片段，您可以对其进行修改并将其整合到现有配置中以检索您的服务数据——从而简化部署、启用高级**可观测性**功能并减少操作开销。

OpenTelemetry 能够提供更深入的业务洞察，例如为组织提供丰富的遥测数据，有助于提供数据上下文，以解决可能被忽视的业务问题，例如客户在线体验中断。现在，随着新的 Injector 简化了设置过程，组织可以更快地实现 OpenTelemetry 的业务优势。

要了解有关 OpenTelemetry 和 Injector 的更多信息，请访问 Kubecon 北美的 OpenTelemetry 观测台。或者您也可以前往现场的 Splunk 展位（#1410）。您可以在 [opentelemetry.io](http://www.opentelemetry.io/) 上找到有关 OpenTelemetry 以及如何参与该项目的更多信息。有关 Splunk 可观测性的更多信息，请访问 [splunk.com](https://www.splunk.com/en_us/products/observability.html)。