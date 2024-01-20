<!--
title: Grafana 努力纠正可观测性的历史遗留问题
cover: https://cdn.thenewstack.io/media/2024/01/8d9195ea-capture-decran-2024-01-05-203244-1024x767.png
-->

新推出的Grafana工具，如自适应指标和成本管理中心，可以帮助组织更好地处理可观测性数据的泛滥。

> 译自 [Grafana Seeks to Correct Observability’s Historic ‘Terrible Job’](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/)，作者 B. Cameron Gain 是ReveCom Media的创始人和首席分析师。他对计算机的痴迷始于20世纪80年代初，当时他在当地的视频游戏厅破解了太空侵略者控制台，以25美分的价格玩了一整天。然后...

时局越来越艰难。IT部门面临着[通过可观测性更好地理解数据](https://thenewstack.io/rethinking-observability/)、优化成本以及做出更明智的商业决策等压力。同时出现了[大量的遥测和各种可观测性工具](https://thenewstack.io/observability-in-2024-more-opentelemetry-less-confusion/)以便解析这些数据。与此同时，IT 团队正面临裁员和安全压力，这些压力还因安全漏洞导致的解雇甚至罚款而加剧。

正如 [Grafana Labs](https://grafana.com/) 的 CEO 兼联合创始人 [Raj Dutt](https://www.linkedin.com/in/radutt/) 在11月于伦敦举行的 Grafana 每年一次的用户大会[ObservabilityCon 2023](https://grafana.com/about/events/observabilitycon/2023/)开幕主旨演讲中所说，“宏观经济形势的变化确实以相当大的方式影响了我们的产品战略。”

Dutt指出2023年对许多人来说从宏观经济角度来看是“充满挑战的一年”，因为基础设施成本以及资金本身已经变得“更加昂贵”，而估值正在下降，“成长不再是唯一的目标”。

“我认为整个可观测性领域——包括Grafana Labs——在历史上实际上在客户价值与支付费用之间的对齐方面做得相当糟糕”，Dutt说，同时指出应用程序和基础设施生成的“爆炸式数据量”。

## 可观测性跟不上数据

换句话说，数据量和成本几乎是指数增长的，而数据和可观测性平台通常提供的价值，至少在许多情况下，并没有跟上。“这种关系一直困扰着我们的思考，特别是在过去一年半的时间里，”Dutt说。

“这是我们产品战略背后的一个重要原因，包括诸如自适应OpenTelemetry、自适应指标和自适应日志等功能。”

在这种背景下，令人欣喜的是，在11月于伦敦举行的Grafana年度用户大会[ObservabilityCon 2023](https://grafana.com/about/events/observabilitycon/2023/)及随后的与Grafana开发人员、工程主管、开发者关系人员和其他Grafana团队成员的交谈中，可以看出他们集体意识到了这些压力，并且正在努力提供更多价值。

Grafana保持了其历史贡献，确保与各种可观测性开源工具兼容，尤其体现在它与[OpenTelemetry](https://thenewstack.io/splunk-opentelemetry-and-the-future-of-observability/)的紧密集成上。

此外，Grafana继续支持开源项目，特别是[Prometheus](https://thenewstack.io/30-pull-requests-later-prometheus-memory-use-is-cut-in-half/)，并继续推出新的项目，比如最近推出的[Grafana Beyla](https://grafana.com/docs/grafana-cloud/monitor-applications/beyla/)(一个[eBPF](https://thenewstack.io/how-ebpf-streamlines-the-service-mesh/)自动插桩工具，详见下文)，以及与[Cilium](https://cilium.io/)的集成，用于利用eBPF进行可观测性和安全性。

与此同时，Grafana在没有大幅提价或意外取消功能的情况下，继续为Grafana Cloud企业版提供更多功能，而某些云提供商确实这样做过(这里不具名指责)。

Grafana的开源政策和支持形成了对比，因为最近一系列针对开源模式的审查或反对传统开源理念的趋势。这包括HashiCorp、MongoDB、Elastic等公司从纯开源许可转向提供软件。此外，还有Red Hat去年决定不再公开RHEL(Red Hat企业Linux)源代码。

## Grafana自适应

所有这些遥测数据都在云上，或者更常见的情况是，分布在多云和本地操作中。Grafana Labs的CTO Tom Wilkie表示，AI和边缘计算的激增也极大地促成了数据的增加。

具体来说，Grafana在ObservabilityCon上正式发布了针对Grafana Cloud的[成本管理中心](https://grafana.com/blog/2023/11/14/grafana-cloud-cost-management-tools-for-metrics-logs-and-more/)，以解决成本管理问题。

Wilkie解释说，它使用户能够访问诸如自适应指标及其UI等功能。此外，还有一个导出程序，允许将日志导出到S3存储桶以实现扩展保留。

基数管理工具也可用，使用户能够识别驱动遥测使用的团队、命名空间和服务。此外，账单使用组有助于收费流程，Wilkie说。“所有这些功能都集中在成本管理中心，为用户提供一个集中平台来访问、评估和管理成本。” Wilkie说。

仅在需要时获取所需的遥测数据量，并以您希望的方式进行可视化，这一点至关重要。为此，Grafana在去年ObservabilityCon 2022期间在纽约推出了[针对Mimir的自适应指标](https://grafana.com/blog/2023/05/09/adaptive-metrics-grafana-cloud-announcement/)。Wilkie说，自那以来，数百个客户已经使用它节省了数亿美元的云和数据存储成本。

“这正在成为Grafana Labs的一种基本和独特的策略，使您实际上只需要存储回答查询所需的数据量，完全自动化并实时自适应。随着您提出不同的查询，我们最终会存储不同量的数据，”Wilkie说。“短期来看，这降低了人们的账单，但从长远来看，我们认为这更能与价值保持一致。”

Wilkie说，Grafana现在正在开发Grafana自适应日志，将在其他领域使用的相同技术应用于日志记录。该项目还处于早期阶段，目前被归类为研究项目，但“团队一直在积极地开展工作，并尝试了两三种不同的技术，结果令人印象深刻，”Wilkie说。在Grafana与Wilkie称之为“三个重要客户”的测试结束后，有趣的是看自适应日志在可用时如何发挥作用来限制日志数据的过度生成。

## OpenTelemetry和eBPF

需要跨栈层和网络的可见性。对于全面堆栈可见性，[eBPF](https://thenewstack.io/what-is-ebpf/)通过使用钩子从基于Linux内核跨栈为其应用的应用程序扩展。与此同时，OpenTelemetry通过提供标准化接口来促进不同可观测性工具的集成。

[Myrle Krantz](https://de.linkedin.com/in/myrlekrantz)在她的主旨演讲中谈到，Grafana Labs的工程总监，用户可能会发现使用OpenTelemetry SDK具有挑战性。如果您使用诸如C++或Go之类的编译语言，Krantz说，就可能如此。或者，您有一个组件，您没有代码，您正在您的环境中部署它。

或者，您可能有一个以混合版本使用的组件，这使得不可能选择特定的OpenTelemetry SDK，Krantz说。“如果这些场景中有任何一个对您有共鸣，仍然有一个解决方案可以帮助检测您的应用程序，”Krantz说。

Grafana在ObservabilityCon上宣布推出Beyla，它集成了eBPF并利用OpenTelemetry传输协议“允许您装饰应用程序和内核调用，跟踪它们，然后将该数据发送到云中”，Krantz说。它当然是开源的，在Apache许可证V2下获得许可。

“所有这意味着您今天可以部署Beyla，几乎不受您从我们的解决方案中使用的其他部分的影响。因为它是eBPF，所以不需要额外的代码——只需要一个命令来部署它，”Krantz说。“它适用于Kubernetes集群、Docker容器和裸机。最重要的是，它在检测否则无法获得可见性的方面实现了所有这些，正因为它建立在eBPF之上。”

## 机器智能

![](https://cdn.thenewstack.io/media/2024/01/d9e833e8-capture-decran-2024-01-05-194739-1024x415.png)

委婉地说，LLM和AI将在未来影响可观测性工具和实践是一种委婉的说法。然而，这种影响的程度和机制有待观察。可以假设可观测性，包括警报和可操作的见解，将由AI编排，提供卓越的商业洞察。但同样，确切的机制尚未被揭示。

在ObservabilityCon期间，Grafana概述了其对LLM和AI开发的总体方法，公开预览推出了[Grafana LLM应用程序](https://grafana.com/grafana/plugins/grafana-llm-app/)。这个应用程序提供了在Grafana中集中访问LLM的另一种方式。这种便利化的结果在未来几个月将很有趣。同时，正在开发生成式AI和LLM应用程序。

在ObservabilityCon的演示中，Grafana Labs的高级工程总监[Marc Chipouras](https://www.linkedin.com/in/chipouras/)展示了这些生成式AI和LLM应用程序可以如何开发。此外，就Grafana中的AI开发而言，最近对[Asserts.ai](https://www.asserts.ai/)的收购预计将是Grafana AI开发的一个小部分或重要部分。Asserts的目的与这种扩展一致，提供对指标数据进行更简单和更自主的分析。Asserts简化了这种语境化，对人类来说是一项复杂的任务。

在不久的将来，Grafana Cloud用户将能够从使用Asserts中受益，后者是为帮助用户使用AI查找指标数据(或如Grafana所述“语境化”指标数据)而创建的。它专门扫描Prometheus指标中的标签，并自动发现应用程序和基础设施组件以及它们之间的连接方式。

“我们想要做的是将生成式AI整合为一种工具，以使您及您的开发人员和朋友能够在Grafana中使用它，”Chipouras说。
