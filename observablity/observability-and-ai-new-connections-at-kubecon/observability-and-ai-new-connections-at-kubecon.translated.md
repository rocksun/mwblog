# KubeCon 大会：可观测性和 AI 的新连接

![KubeCon 大会：可观测性和 AI 的新连接特色图片](https://cdn.thenewstack.io/media/2024/12/20bff831-observability-ai-1024x576.jpg)

盐湖城——在[KubeCon + CloudNativeCon 北美大会](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)上，许多产品新闻和讨论中都暗流涌动着一个主题：[AI](https://thenewstack.io/ai/) 如何与许多已有的技术相连接。

例如：[可观测性](https://thenewstack.io/observability/) 公司[New Relic](http://newrelic.com/?utm_content=inline+mention)和[思科旗下的 Splunk](https://www.splunk.com/en_us/products/observability.html?utm_content=inline+mention)的公告。

New Relic 宣布其[用于 Kubernetes 的全新一步式可观测性](https://newrelic.com/platform/kubernetes-pixie)正式可用，该产品可自动将应用程序性能监控 (APM) 与 Kubernetes 部署连接，无需任何额外配置。该产品收集遥测数据（它提供对[Prometheus](https://prometheus.io/)和[OpenTelemetry](https://thenewstack.io/new-relics-opentelemetry-and-open-source-commitment/)的原生支持），并通过仪表板显示基于该数据的 AI 驱动的见解。

New Relic 的高级开发者关系总监在 KubeCon 大会上告诉 The New Stack，其好处在于可视化更容易。

“我们通过一步式可观测性所做的是，基本上消除了所有这些麻烦，”  说。“因此，您可以开箱即用地深入了解您的 Kubernetes 环境，以及部署到集群中的应用程序。”

它是如何工作的？“我们将拥有我们自己的容器，它将处理所有拉取或自动检测应用程序的工作。

“通过为您的基础设施层添加 New Relic，您已经可以开箱即用地获得这些功能。因此，现在您无需实际增强任何配置，它只会将其作为一种旁调用来运行，然后将所有数据整合在一起。”

![New Relic 的 ](https://cdn.thenewstack.io/media/2024/12/db777591-jemiah-sius-300x260.jpg)
New Relic 的  。(来源：Heather Joslyn)

在后续电子邮件中，详细介绍了该“容器”的工作方式：“在 Kubernetes 中，Mutating WebHook 会拦截将 Pod 部署到节点的 API 请求。它会根据指定的配置修改 Pod 规范，以使用独立的 newrelic-mutate-pod 添加 NR init 容器和环境变量。在建立 Pod 后，New Relic APM Agent 会无缝集成到用户 K8s Pod 中的应用程序中。”

在 KubeCon 大会上，Splunk 宣布其综合[可观测性](https://thenewstack.io/observability/) 产品组合的一些新功能正式可用。其中，Splunk Observability Cloud 的标签聚光灯功能现在具有 AI 增强功能，可以更细致地了解跨应用程序和最终用户体验中出现的常见问题，从而实现更快的故障排除和更好的事件解决。

思科的[AppDynamics](https://www.appdynamics.com/?utm_content=inline+mention)  指出，传统上服务于较旧的遗留系统。“目前，在我们 Splunk 可观测性部门中，重点在于与 AppDynamics 的集成，以及能够将人们在 AppDynamics 中非常喜欢的功能（如业务事务和快照结果等）带到 Splunk 可观测性中，供希望在那里使用它们的客户使用，同时增加我们对更多平台的 AppDynamics 的通用支持。”

## 减轻告警疲劳

对 AI 功能的投资是整合 Splunk 和 AppDynamics 产品的一部分。几乎每个人（97%）[在 10 月份发布的一份报告中接受 Splunk 调查的人](https://www.splunk.com/en_us/form/state-of-observability.html)表示，他们使用 AI 和机器学习驱动的系统来增强可观测性操作。这比 2023 年研究版本的 66%有所上升。

深入研究数据后，在可观测性解决方案中肯定还有更多使用 AI 的空间。55% 的 Splunk 受访者使用 AI 和 ML 驱动的工具来完成调查并确定问题的[根本原因](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/)。

Splunk 报告基于 2024 年 5 月和 6 月对 1850 名 IT 专业人员的调查。
AI可以帮助解决的一个痛点是告警疲劳。在Splunk十月发布的一项调查中[https://www.splunk.com/en_us/form/state-of-observability.html](https://www.splunk.com/en_us/form/state-of-observability.html)，57%的参与者表示他们将告警疲劳与可观测性解决方案联系起来。

过去，McLean表示，他曾担任值班工程师，他理解这种痛苦。

“告警疲劳非常残酷，”他说。“半夜被吵醒，你的手机开始疯狂震动，你看着它，也许很重要，也许不重要，你需要坐下来注册并决定这是否应该忽略或需要立即采取行动。

“一些组织对此有良好的规范，但这需要大量的体力劳动和流程来不断更新和修剪你的告警，以确保它们有效。我们可以做很多事情，我们正在投资Splunk来改进这一点，”

## OpenTelemetry的下一步是什么？
McLean也是[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)的联合创始人，这是一种收集可观测性数据（指标、日志和追踪）的标准化方式。他表示，OpenTelemetry[性能分析信号](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/)的普遍可用版本发布，原计划于2024年底发布，现在可能会推迟到2025年中。

“在[OpenTelemetry](https://opentelemetry.io/)或任何类似的标准中，有很多工作是在指定行为方面进行的，”他说。“这不是代码，而是人们用人类语言书写。”

除了OTel的收集器代理之外，它还必须从使用[Java](https://thenewstack.io/java/)、[Python](https://thenewstack.io/python/)等语言的应用程序中捕获数据。

“所有这些都必须保持一致的行为，因为如果其中一个决定以不同的方式捕获数据，其形状与所有其他数据不同，你就无法处理它，”McLean告诉The New Stack。“你需要获得一致的数据。因此，性能分析方面仍然有一些规范工作正在进行。”

![Morgan McLean, of Splunk, a Cisco Company.](https://cdn.thenewstack.io/media/2024/12/b10e83b6-morgan-mclean-300x254.jpg)
Morgan McLean，Splunk（思科公司）

将这些规范纳入OTel协议的大部分工作已经完成，但他表示，这项工作尚未完成。特定语言的实现仍然需要最终确定。

“许多剩余的工作是让我们的Java支持与内置的Java性能分析进行通信……这些都不是特别困难，但我们必须在每种语言上都这样做。”

议程上的另一件事：最终确定整数的语义约定。正如McLean提到的，团队正在创建规范，以确保OTel性能分析在不同语言中的工作方式保持一致。

“我们不仅需要这些实现保持一致的行为，还需要它们生成的数据具有完全相同的标签和属性等，这样你才能获得一些强大的分析，”他说。“这方面有很多工作正在进行。这可能被认为是一种枯燥的工作，但它确实非常关键。”

McLean表示，将性能分析信号引入开源OTel将帮助更多组织利用性能分析并降低成本，从而将一项潜在的利基功能推向主流。

“Splunk提供性能分析产品，”他指出。“许多可观测性供应商也这样做，但这通常只是产品的一小部分。”

他打了个比方：“分布式追踪在真正成为主流之前已经存在多年了，它成为主流的一个重要原因是开放性。如果你让它易于使用，性能分析也是类似的。”

去年一月，TNS预计[OpenTelemetry的支持和采用](https://thenewstack.io/opentelemetry-and-observability-looking-forward/)将在2024年继续。

- 在Splunk的研究中，58%的参与者表示他们的主要可观测性解决方案依赖于OpenTelemetry。这与我们的预期相符。
- 然而，
New Relic和[Enterprise Technology Research](https://etr.ai/)十月发布的一项[研究](https://newrelic.com/resources/report/observability-forecast/2024)提供了更为悲观的景象，只有10%的1700多名受访IT专业人员表示他们使用集成了OpenTelemetry的开源解决方案。
至于OTel路线图上更远的目标，McLean提到了服务遗留系统。“OpenTelemetry即将进入大型机，”他说。“有一个工作组正在研究这个问题。我们正在添加对IBM z/OS、IBM Z Linux的支持。”
目标是帮助那些已经使用 OpenTelemetry 的“大型金融机构、航空公司及其他公司”——在其 Kubernetes 集群、[虚拟机](https://example.com)以及大部分现代基础设施上——这些公司仍然依赖于遗留系统，使用现代的而非特定于大型机的可观测性工具来捕获所有数据。McLean 说，那些遗留工具无法让这些组织全面了解其整个系统。

## AIOps：衰落还是重新包装？
然而，来自 New Relic 和 Splunk 的新数据也指出了 AI 在可观测性领域的未来的一些担忧：

- 在 Splunk 的调查中，只有 34% 的受访者表示他们的组织可以使用 AI/ML 解决大部分警报。然而，Splunk 发现，已经采用可观测性的公司更有可能达到这一里程碑。
- 20% 的 Splunk 研究受访者广泛使用 AIOps 工具。
- New Relic 的报告发现，其调查参与者中 24% 使用 AIOps 功能，低于 2023 年同一研究中的 41%。
- 这种下降可能是对[AIOps 的坏名声](https://thenewstack.io/sres-wish-automation-solved-all-their-problems/)的回应，而[AI 驱动的可观测性](https://thenewstack.io/ai-powered-observability-picking-up-where-aiops-failed/)的重新包装更能体现实际的使用模式。
在给 TNS 的后续电子邮件中，New Relic 的 Sius 解释了人们部署 AIOps 功能下降的原因：“下降可能归因于 AI 技术的快速发展，新的创新，如[大型语言模型 (LLM)](https://thenewstack.io/supercharge-aiops-efficiency-with-llms/)，正在重塑人们对‘AI’的定义。”

“2023 年，大多数人可能将 AIOps 视为一个涵盖广泛应用的总称。但随着过去一年 AI 的显著进步，2024 年的受访者对 AIOps 标签的理解可能大相径庭，更加具体。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。