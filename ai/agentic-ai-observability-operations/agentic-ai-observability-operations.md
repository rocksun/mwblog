<!--
title: 可观测性中的代理式AI：加速根因分析进程
cover: https://cdn.thenewstack.io/media/2025/01/f74f19ca-otel-elastic-collaborate-make-observability-more-accessible.jpg
summary: 本文探讨了代理式AI如何通过自动化数据聚合、深度分析与任务处理，革命性地提升IT运维与可观测性效率，加速根因分析过程，并助力企业实现运维数据的平民化与智能化。
-->

本文探讨了代理式AI如何通过自动化数据聚合、深度分析与任务处理，革命性地提升IT运维与可观测性效率，加速根因分析过程，并助力企业实现运维数据的平民化与智能化。

> 译自：[Agentic AI in observability: accelerating root cause analysis](https://thenewstack.io/agentic-ai-observability-operations/)
> 
> 作者：TNS Staff

生成式AI和代理式AI的不断发展、前景和应用，正持续推动全球企业IT领域发生剧烈变革，涵盖从运维和基础设施到软件开发、业务管理等各个方面。

但在代理式AI和AI产生最深远影响的领域中，或许要数尚处于成熟期的IT运维和可观测性领域。在这里，企业正在获得关于其业务应用程序如何在整个IT环境和基础设施中运行的关键洞察。

当与传统的监控工具和可观测性平台集成时，代理式AI可以通过加速从系统日志、追踪和可观测性指标中聚合及分析关键数据，从而增强并彻底改变可观测性和IT运维。这使得针对系统问题的根因调查能够比仅依靠现有工具和人工工程师更深入、更快速且更彻底。

当集成到可观测性系统中时，代理式AI使工程师能够搜寻整个IT生态系统（包括微服务、服务器和数据库）中的海量数据和依赖关系。工程师可以利用这些数据，结合内部组织数据和用例，运用统计和机器学习方法对系统属性、模式和问题进行深入分析，从而揭示关于系统问题的新见解。

## 代理式AI目前如何助力可观测性

[**Thaddeus Walsh**](https://www.linkedin.com/in/thaddeuswalsh/) 是 [**Elastic**](https://www.elastic.co/?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc) 的首席解决方案架构师，他告诉 *The New Stack*，“代理数据是一个加速器。”

“之所以说是加速器，是因为我不需要盯着20页的日志行，也不需要运行特定的分析流程来熟悉问题发生前正常的日志信号是什么样的，” Walsh 说道。

> “代理数据是一个加速器……因为我不需要盯着20页的日志行，也不需要运行特定的分析流程来熟悉问题发生前正常的日志信号是什么样的。”
> — Thaddeus Walsh, Elastic 首席解决方案架构师

利用代理式AI，耗时的机械性任务可以外包给自主代理，它们完成任务的时间仅为人工工程师所需时间的一小部分。

Walsh 表示，当AI代理加入到可观测性工具中时，IT团队就获得了支持其业务关键工作的强大盟友。

Walsh 指出，驾驭AI力量的关键在于首先了解你的数据、数据的检索方式，以及你的流程和接口是如何工作的。所有这些对于确保你选择的工具完全符合公司的任务和关键业务 [工作流](https://www.elastic.co/elasticsearch/workflows?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc) 至关重要。

## 代理式AI如何为SRE团队和可观测性演进

对于站点可靠性工程师（SRE）来说，代理式工作流和AI可观测性工具可用于加速根因分析（RCA）调查、相关的代码和系统调查，并快速交付经过批准的、自动化的操作，从而提供有价值的见解和修复方案。

“我可以要求一个代理去查看网络数据，并告诉我目前是否有迹象表明问题与网络有关，” Walsh 说。“工程师可以完成自己的工作，然后告诉代理去查看来自其他代理的反馈。工程师可以并发执行这些工作，这在时间上更高效，同时也允许代理在通知人工操作员时保持一致性。”

Walsh 认为，这是将代理引入流程，以指导人工操作员在不断扩大的调查中下一步该做什么的自然第一步。

Walsh 表示，随着代理被直接内置到平台中，能够以极少的人工干预常规、持续且准确地推动根因和运营调查，这些工具的未来演进将更加强大。“我们还没有完全达到那个阶段，但我认为行业将在未来24个月内实现这一目标。”

## 代理式AI在哪些方面提供更深层的可观测性

代理式AI功能的加入也正在推动企业用例中可观测性工具和平台的广泛创新，例如：

* **在 [DevOps](https://www.elastic.co/observability/devops?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc) 中调试和改进应用程序性能。** 通过使用这些工具，企业可以统一并消除破坏性的数据孤岛，将指标、日志和分布式追踪关联到一个单一的可观测性管道中，帮助工程师识别瓶颈并更快速地简化根因分析。
* **紧密集成业务和运营数据以改善系统和生产力。** 这为工程师提供了分析运营中所有业务数据的关键能力，以确保其安全性、质量和准确性。
* **减少过敏的运营警报数量。** 这使得安全工程师能够专注于已验证的真实威胁，而不是那些提供虚假和欺骗性线索的良性“噪音”——这些噪音旨在制造破坏性混乱，以转移工程师的注意力并实现更具破坏性的攻击。
* **加强 [AIOps](https://www.elastic.co/observability/aiops?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc) 和 AIOps 可观测性。** 使用代理式AI工具使广泛且具有启发性的分析和洞察的获取变得平民化，同时显著提升了工程师大规模识别和排查问题的能力。

利用代理式AI赋能的可观测性工具，企业还可以增加更多的权力和控制，以更好地管理其复杂的微服务架构，观察订单管理等流程的实时数据，跨多个孤岛跟踪和处理业务数据，更早发现异常系统问题，并改善其云原生和混合环境（包括 [Kubernetes](https://www.elastic.co/observability/kubernetes-monitoring)）的运营。

## 如何开始在可观测性中使用代理式AI

Walsh 建议，一个简单的入手点是创建一个代理，当服务宕机时，它会自动设置警报和工单，或者自动向工程师发送消息。

“你可以定义如何做出该决定，然后将其下放给代理，”他说。“通过实现一个在发生事故时担任沟通指挥官角色的代理，你可以实现极大的噪音削减。”

他说，可预测的、重复性的操作也是代理式AI可以改善可观测性的地方。“代理式AI带来了将人类特征带入流程的能力。”

> “通过实现一个在发生事故时担任沟通指挥官角色的代理，你可以实现极大的噪音削减。”

Walsh 说，另一个例子是当收到大量警报，报告了数百个必须进行调查和评估的事故影响时。“我不想收到400封带有离散小信号的邮件。我想要看到这些信号的总结。而且我希望被告知我已经检查过哪些信号。”

Walsh 认为，代理式AI在这些流程中的价值在于它的响应性和始终在线。“警报开始出现，代理立即采取行动。”

## 下一步：可观测性数据的平民化

通过将可观测性的速度和效率与代理式AI的力量相结合，企业获得了更深入的洞察、更准确的实时响应等等。

虽然可观测性数据长期以来一直是锁定在业务单一领域的 SRE 和 IT 运维团队的专属，但这种模式正在改变。

现在 [代理式AI和生成式AI使](https://thenewstack.io/elastic-agentic-observability-enterprise-adoption/) 开发人员、DevOps工程师、应用程序所有者、安全分析师和业务利益相关者能够直接获取可观测性数据，用通俗语言提问，并获得真实答案，而无需成为专家。

***另请参阅：** [大多数企业将在两年内将根因分析交给AI代理](https://thenewstack.io/elastic-agentic-observability-enterprise-adoption/)*

“这些是迈向明天可观测性能力的必经之路，” Walsh 说。

在 [Elastic 最近与 Walsh、高级首席解决方案架构师 Brad Quarry 和 TNS 主持人 Alex Wilhelm 举办的网络研讨会](https://www.elastic.co/virtual-events/beyond-the-sre-democratizing-observability-data-with-genai?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000q2MD2IAM) 中了解更多关于可观测性平民化的信息。