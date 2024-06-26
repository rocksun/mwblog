# 使用端到端的事件驱动的自动化来应对事件

翻译自 [Fighting Incidents with End-to-End Event-Driven Automation](https://thenewstack.io/fighting-incidents-with-end-to-end-event-driven-automation/) 。

正在为高 MTTR 和过多的工作而苦苦挣扎？采用爬、走、跑的策略实现自动化，以实现更好、更快的事故响应。

![](https://cdn.thenewstack.io/media/2023/04/5ff59f95-shutterstock_2-1024x567.jpg)

今天的技术团队面临的事件数量是前所未有的，他们承受着巨大的压力。公司希望保护收入和客户体验。各行业的客户对数字化客户体验有很高期望值。他们希望快速、无缺陷和高可用性，并且对服务中出现问题容忍度极低。[根据普华永道（PWC）的数据](https://www.pwc.com/us/en/advisory-services/publications/consumer-intelligence-series/pwc-consumer-intelligence-series-customer-experience.pdf#page=9)，三分之一的客户会在一次糟糕的体验后停止与他们喜爱的品牌开展业务。

负责保持这些服务可用的团队被警报噪音淹没。响应者对于解决事件所需的信息以及该信息位于何处感到困惑。而查找此信息，加上为每个事件完成相同的手动、重复性任务意味着他们浪费了太多时间。

为了缩短故障解决的平均时间（MTTR）并保持客户和响应团队的满意度，组织需要利用自动化。但这不是一次性的事情，也不是可以在一个迭代中完成和扩展的。这是对更好的事件响应实践的承诺，包括要克服挑战和经历各个阶段。

## 我们从客户那里听到的有关自动化的挑战

从我们与客户合作，从小型初创公司到财富 100 强公司，以帮助推动更好的事件响应最佳实践，我们听到了采用自动化的最常见挑战。

以下是前三名：

**太忙于救火**：当事件来得快时，所有团队都会觉得他们被拉入了危机模式。他们无法足够快地解决问题以完成分配的工作，更不用说解决改进事件响应的举措了。

**不买账**：各行各业的领导者都在研究如何成为市场上最具竞争力的公司，以及如何以尽可能低的成本做到这一点。如果对组织的底线没有切实的好处，那么像精心设计自动化这样的长期计划可能会让人分心。

**无法扩展**：一些组织正在努力部署自动化，但遇到了绊脚石。他们无法扩展。一些团队为他们的服务构建了详细的自动修复。其他人仍然坚持做手工工作。没有标准化。

当这些挑战在组织中发挥作用时，可能是采用爬、走、跑的方法来创建和部署自动化的时候了。

## 如何采用爬、走、跑的自动化方法

第一步是确定谁是团队的一员以及您计划执行的级别。让组织接受自动化的最佳方法之一是从一个小型试点团队开始，自动化一些容易实现的成果，以改善特定团队、小组或服务的日常工作。与其他团队共享该自动化并查看采用范围。这将激发人们对建立更多自动化的兴趣，帮助草根倡议取得成功。而且，有了更好的 MTTR，您更有可能获得高管的支持，并获得经过验证的结果并减少对客户的影响。

### 爬

如果事件流对您的团队来说太过压倒性，请从源头开始控制。朝着更好的事故响应自动化前进始于两件事：抑制和暂停瞬态警报。与其他形式的自动化相比，这些相对容易执行。此外，它们立即帮助响应者节省时间并减少警报疲劳。

抑制是用于阻止事件向响应者发送通知的一种方法，这些事件已知几乎没有价值。根据 AIOps 客户数据，50% 的噪音压缩来自抑制。通过针对团队不需要了解的那些事件实施广泛规则，抑制可以减少事故的数量。

例如，PagerDuty 的开发团队会抑制事件，直到到达一定数量的事件，此时他们会关闭抑制并允许 Event Orchestration 开始创建事件。

暂停通知功能允许用户暂停创建事件一段预定义的时间。一旦该时间到期，事件将正常创建。此自动化最适用于具有明确定义条件的事件标记。例如，某公司可以暂停某些高CPU使用率事件 5 分钟，仅在高CPU持续/持久时才创建事件。

### 走

一旦您降低了环境中的噪音并且您的团队发生的事件减少了，就该使用适当的数据使这些事件更容易解决。您可以通过丰富事件、警报和事件（incident）来做到这一点。

事件增强可以通过确保响应者拥有与上下文相关的信息来加快分类速度。团队可以规范事件数据，使整个组织内的事件看起来都一样。这对于网络运营中心（NOC）或其他 L1 响应团队尤其有帮助，他们希望在处理进来的事件时保持一致性，并且没有时间学习支持的数百个团队的细微差别。

警报增强功能更深入一层。一旦事件正式成为警报，响应者可以定义创建警报的严重程度。这确保通知被路由到正确的升级策略，节省了响应时间。

对于被分组为事件的警报，事件增强功能允许用户在初始创建时定义事件的优先级和备注。这意味着当一个事件是 P1 时，您更加确定所有人都需要参与，而不是P4，您不需要因此打断晚餐。对于任何值班人员来说，这是一种提高生活质量的改进。备注还可用于填写知识库文章、内部维基或提供有关响应者如何进行操作的信息。

### 跑

这次旅程的最后一步是自动修复。作为 L0 响应者，事故会通过自动化解决。不需要人类干预。实现这一点的方法之一是使用可以在事件创建时触发的 Webhooks 。或者您可以调用其他形式的自动化，无论是通过 PagerDuty 还是其他供应商提供的。虽然有些组织可以独立达到这种复杂程度，但构建此自动化很困难，并且将其扩展到整个组织可能会带来许多挑战。事实上，这就是人们求助于 PagerDuty 的主要原因之一。在此阶段进行合作可以帮助减轻负责开发其自己的自动化或负责创建整个组织范围内它的网站可靠性工程团队所面临压力问题

## 希望在您的技术生态系统中实现全局范围的自动化？

无论您是刚刚开始自动化之旅的爬行阶段，还是已经在运行自动修复，PagerDuty AIOps 都可以帮助您以更快的速度解决更少的事件。我们的新功能 Global Event Orchestration 可以帮助您在最复杂的技术生态系统中创建和扩展自动化。如需更多信息，您可以参观我们的产品或注册我们的网络研讨会。