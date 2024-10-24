
<!--
title: LLo11yPop：英伟达和Grafana正在开发用于可观测性的LLM
cover: https://cdn.thenewstack.io/media/2024/10/1534875f-llo11ypop-nvidia-and-grafana-work-on-an-llm-for-observability.png
-->

两家公司正在创建多个项目，旨在让工程师更好地了解 AI 模型训练的进展，并解决其他可观察性痛点。

> 译自 [LLo11yPop: Nvidia, Grafana Working on LLM for Observability](https://thenewstack.io/llo11ypop-nvidia-grafana-working-on-llm-for-observability/)，作者 B Cameron Gain。

纽约——虽然没有正式宣布，但英伟达高级工程经理在 [ObservabilityCON](https://grafana.com/events/observabilitycon/) 上的主题演讲中描述了英伟达与 [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) 合作的几个 AI 项目。

这些项目包括两家机构开发 AI 训练，以更好地了解模型性能和一致性。另一个项目利用遥测数据为 [大型语言模型](https://thenewstack.io/llm/) 和 AI 应用程序创建 [可观测性](https://thenewstack.io/observability/) 接口。

正如 Erickson 在 9 月 24 日的主题演讲中所述，英伟达依靠 Grafana Cloud 来提供可观测性支持。


> @nvidia 的 @AaronErickson 在 #ObservabilityCON 上表示，英伟达依靠 @grafana 来“了解训练过程的遥测数据”。
> 
> — BC Gain (@bcamerongain) 2024 年 10 月 3 日

其中一个更有趣的项目——名为 [LLo11yPop](https://developer.nvidia.com/blog/optimizing-data-center-performance-with-ai-agents-and-the-ooda-loop-strategy/)——是一个用于可观测性的 LLM。英伟达正在开发一个 LLM，该 LLM 在 Grafana 的支持下设计，可以用来询问诸如“给我展示一个作业失败的图表”或“昨晚问题的五个最可能原因是什么？”或“哪些集群需要维护？”之类的问题。

 Erickson 在主题演讲中告诉与会者：“现在还处于早期阶段，但我们开始使用在不同专业领域训练的多个 LLM 从数据中心获取答案。这是一个令人难以置信的概念，我们对它的可能性感到兴奋。我们相信，随着时间的推移，这种 [代理](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 以及更多代理的加入，将使我们能够解决各种问题。”

## 遥测数据用于检查 LLM 训练状态

英伟达还与 Grafana 合作开发了一个由 Grafana 主导的 [用于训练可观测性的应用程序](https://github.com/grafana/ai-training-o11y?tab=readme-ov-file#readme)；英伟达是 Grafana Labs 的设计合作伙伴。

 Erickson 表示，英伟达作为 Grafana 的客户，“对于我们想要实现的目标至关重要：能够真正了解训练过程的遥测数据。”

“想象一下，你正在尝试构建一个基础模型或对模型进行大规模调整。你需要了解：模型是否收敛？训练是否在进行？在更低级别上，GPU 性能是否稳定？温度是否正常？所有这些对于评估你是否在这些训练运行中进行了良好的投资至关重要。”

此外， Erickson 在主题演讲中表示：“我们的一个关键信念是，除非这个系统以真相为基础，否则它将无法正常工作。LLM 的查询结果必须得到实际数据的支持，例如 Grafana 仪表板中显示的内容。我们知道 LLM 并不完美——[它们确实会产生幻觉](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)——因此我们希望利用它们来动态构建仪表板。

“你应该能够提出一个问题，获得一个仪表板链接，然后深入了解全球数据中心的状态，包括我们拥有 GPU 的所有云提供商和大陆。”

Grafana Labs 首席技术官 [Tom Wilkie](https://www.linkedin.com/in/tomwilkie) 告诉我，除了英伟达之外，Grafana 还与几家 AI 公司合作，“推动我们能够使用这两种技术监控、学习和生成的内容的界限。”

“我们目前与英伟达的合作将有助于为运行和监控 GPU 基础设施的人员以及构建和训练在 GPU 上运行的模型的人员提供更有用的可观测性。这项基础工作可以从当今的模型中产生许多更可靠的输出，并且随着模型性能的提高，其准确性和对用户的价值应该会不断提高。”

## 幕后是什么？

基于英伟达 NIM（英伟达推理微服务）技术的 NIM 检索代理是英伟达正在构建的系统的构建块。NIM 也可以被描述为为大规模 LLM 部署提供优化的推理微服务。

这些代理从 Grafana 等来源收集数据以回答问题。这些问题来自经过训练的分析师代理，他们了解不同应用程序如何在数据中心运行。在使用多 LLM 复合模型的架构设计中，针对 GPU 集群管理的观测代理框架，代理管理观测框架的编排和任务执行。这些由所谓的 OODA 循环进行编排——观察、定向、决策、行动。

“循环驱动代理提出问题，识别问题所在，并采取行动，例如打开 Jira 票证或致电 [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention)”，Erickson 告诉 The New Stack。

当然，调试至关重要，因为如果没有适当的观测工具，应用程序和网络修复可能需要数周甚至数月的时间，他说。

“如果它们失败，那就是毫无理由地浪费大量资源，”Erickson 说。“这就是为什么拥有这种洞察力非常重要的原因，我们很高兴成为设计合作伙伴，帮助构建这种能力。这种合作使我们能够实现目标，并帮助其他在 GPU 上运行训练作业的客户。”


> @nvidia 的 @AaronErickson 回忆起在适当的观测成为现实之前那些可怕的半夜页面，在上周纽约的  #ObservabilityCON 期间。@grafana
> — BC Gain (@bcamerongain) 2024 年 10 月 3 日


## “我们当中谁没有幻觉过？”

在演讲中，Erickson 在担任一家未具名“观测公司”的工程副总裁期间，并没有那么怀旧。

“想象一下，每天早上 6 点醒来，负责帮助你的 CEO 在早上 8 点之前了解前一天晚上发生的事情，”他说。“我的例行公事是阅读 Slack 的回滚，打电话给主管和 [[独立贡献者](https://thenewstack.io/tech-works-how-to-get-promoted-without-becoming-a-manager/)], 并追踪处理事件的人员。

“我必须收集信息，例如哪些客户受到影响，哪些区域受到影响以及可能的根本原因。我们需要所有这些来编写事件报告并通知客户。在六个月的云迁移过程中，这种情况每天都会发生——那段时光并不愉快。”

LLM 并不完美，或者至少现在还不完美。所有 LLM 中频繁出现的幻觉是人们最常提到的失败之一。但同样，人类也会产生幻觉。

“你遇到了一起事件，第二天早上，一位高级领导询问发生了什么，”Erickson 说。“我们当中谁没有幻觉过一点来填补空白？如果你持怀疑态度，问问你的开发人员。这种情况经常发生。

“这启发我思考：使用 [GPT-4](https://thenewstack.io/30-non-trivial-ways-for-developers-to-use-gpt-4/)，我们可以将人类问题转换为查询语言，例如 [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/), 或者我们与 Grafana 一起使用的任何东西，来找出昨晚发生了什么。作为一名工程师，这使我能够从一个粗略的想法开始，提出后续问题，并更接近于合理的因果关系——虽然它可能并不完美，但人类也不完美。”
