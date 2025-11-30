
<!--
title: 超越脚本：从自动化迈向智能体AI
cover: https://cdn.thenewstack.io/media/2025/11/74fab05c-binary.jpeg
summary: 代理式AI超越传统自动化，通过理解上下文、自主决策，提升系统可靠性、安全性，减少事件解决时间。它逐步建立信任，赋能工程师专注于高价值工作，实现运营的智能进化。
-->

代理式AI超越传统自动化，通过理解上下文、自主决策，提升系统可靠性、安全性，减少事件解决时间。它逐步建立信任，赋能工程师专注于高价值工作，实现运营的智能进化。

> 译自：[Beyond Scripts: The Shift From Automation to Agentic AI](https://thenewstack.io/beyond-scripts-the-shift-from-automation-to-agentic-ai/)
> 
> 作者：Ankush Dhar, Minav Suresh Patel

在过去十年中，工业工程发生了转型。现在几乎每个功能都实现了自动化，从集成、测试到部署和可观测性。但随着云工作负载、分布式[微服务和不断变化的依赖关系](https://thenewstack.io/why-coordinating-microservice-changes-is-still-a-mess/)使系统变得更加复杂，传统自动化已达到其极限。

静态脚本和硬编码的自动化手册在遵循指令方面表现出色；然而，当发生意外情况时，它们就束手无策了。它们无法思考或适应。当流量激增、依赖项失效或[成本意外变化](https://thenewstack.io/ai-code-generations-unexpected-costs-for-dev-teams/)时，一切都可能连锁性地导致故障。没有任何脚本能够预测这些情况。我们已经建立了更快的操作，但我们仍然需要人们来处理任何不按计划进行的事情。

这就是代理式AI的用武之地。代理式系统的工作方式不同；它们理解上下文，思考问题并在安全护栏内做出决策。它们不等待人类命令或预定任务。相反，它们评估情况，设定优先级并采取行动。是暂停、回滚、扩缩还是告警，取决于具体情况的需求。这并非要消除人类监督；它是一种能够思考的智能自动化。

## **从自动化到适应**

实际上，代理式系统充当一个智能层，位于企业现有的自动化堆栈之上：CI/CD工具、Kubernetes集群、云API或事件管理系统。它持续观察延迟、吞吐量、错误预算或成本指标等信号，并将其与期望结果进行比较。当事情开始出错时，它不仅仅是遵循预设规则。它会思考各种选项，预测可能发生的情况，做出安全的举动，并检查其是否奏效。

这种持续的感知-思考-行动循环使组织能够动态地调整操作。例如，管理部署管道的代理现在可以[监控服务健康状况并主动调整](https://thenewstack.io/proactive-monitoring-will-maximize-your-cloud-storage-efficiency/)发布速度，或在延迟趋势超过风险阈值时暂停部署，甚至在用户注意到任何影响之前。

在LogicMonitor最近对代理式AIOps采用情况的[分析](https://www.logicmonitor.com/blog/agentic-aiops-benefits?utm_source=chatgpt.com)中，企业报告平均解决时间（MTTR）大幅减少，并且升级到严重级别的事件减少。同样，ResearchSquare的[一项研究](https://www.researchsquare.com/article/rs-7383044/v1.pdf?c=1757512931000)发现，AIOps的实施可以通过预测性关联和自主修复将MTTR降低多达40%。

同样的模式也延伸到发布管理之外。在大型金融平台中，代理式AI现在通过将[实时使用情况和成本遥测与预算目标对齐](https://thenewstack.io/what-does-ai-cost-no-one-knows/)来支持FinOps决策。思科的[CrossWorks网络自动化白皮书](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/crosswork-network-automation/white-paper-c11-741691.html?utm_source=chatgpt.com)分享说，自适应自动化可以通过主动优化网络资源来降低运营成本和停机时间。

## **代理式AI如何改变可靠性和安全性**

也许最显著的转变发生在事件响应中。传统的自动化手册通常会在正确的领域专家看到警报之前通知多个团队。代理式系统[能够消除这种混乱](https://thenewstack.io/how-ai-and-agents-are-slashing-3-a-m-wakeups/)。通过关联遥测数据、日志和追踪，它们推断出可能的根本原因，安全地运行诊断命令，并向工程师提供建议的修复方案。

它们不是盲目行动，而是利用历史学习来推荐风险最低的修复方案，例如重新启动故障服务或翻转降级的功能标志。它们通过自动识别根本原因并应用低风险修复方案来帮助降低运营成本。

这种方法与领先组织目前大规模实施的方法不谋而合。Hacker News的[一项分析](https://thehackernews.com/2024/09/agentic-ai-in-socs-solution-to-soars.html?utm_source=chatgpt.com)报告了安全运营中心中的代理式AI如何通过自动化遏制和分类来缩短响应时间并降低分析师的认知负荷。在软件运营中，同样的原则也适用，通过将推理和[上下文感知嵌入到自动化中](https://thenewstack.io/automating-context-in-structured-data-for-llms/)，从而缩短响应时间，同时提高置信度和可解释性。

这些益处不仅限于正常运行时间。随着法规和安全要求的收紧，代理式系统越来越多地用于在DevSecOps管道中[强制执行策略即代码](https://thenewstack.io/real-time-policy-enforcement-with-governance-as-code/)。它们可以自动隔离不合规的工作负载，轮换即将到期的密钥或阻止不安全的配置，同时保持每次干预的可审计记录。设计良好的代理式系统不会充当不透明的黑匣子，而是记录每个输入、策略检查和操作，从而为内部审计或外部合规性审查提供完整的可追溯性。

## **通过护栏建立信任**

信任是采用代理式自动化最重要的因素。工程师需要确信自主系统不会采取鲁莽行动或违反变更管理策略。如果没有这种保证，无论技术多么先进，它永远无法赢得组织的信任。

最有效的实施始于受限的“影子”或“建议”模式。在这些早期阶段，代理不执行更改；相反，它观察、推荐并解释其推理。人类操作员审查每项建议，并将其与他们手动操作的结果进行比较。

随着时间的推推移，当代理的建议与实际结果一致且其决策质量提高时，团队会逐步在低风险领域（例如非工作时间回滚、补丁调度或成本优化任务）中允许更多的自主权。

这种循序渐进、基于证据的方法创造了信任的反馈循环。每个成功的行动都成为一个证明点，增强了对更广泛信任的理由。随着时间的推移，代理从被动的顾问演变为可靠的副驾驶，安全透明地处理重复性工作。

[![Figure 1. Building trust through human-in-the-loop agentic automation. Safe autonomy grows as confidence, validation and explainability mature.](https://cdn.thenewstack.io/media/2025/11/93999db1-image1-1024x683.png)](https://cdn.thenewstack.io/media/2025/11/93999db1-image1-1024x683.png)

*图1. 通过人机协同代理式自动化建立信任。随着信任、验证和可解释性的成熟，安全自主性也随之增长。*

这种演变的治理方面同样至关重要。NIST人工智能风险管理框架强调“测量和管理”功能，包括持续监控、验证和记录模型性能，以确保透明度和问责制。同样，欧盟人工智能法案要求对自主系统进行上市后监控和可解释性，为企业自动化应如何受到监督树立了明确的先例。在实践中，这些原则直接适用于软件和工业运营。每个代理式行动都必须是可解释的、可逆的、可审计的。团队必须为允许采取哪些行动、在什么条件下以及如何记录结果建立明确的护栏，以创建一个人类和[智能系统可以安全协作](https://thenewstack.io/collaborative-intelligence-in-multiagent-systems-with-python/)的环境。

随着组织变得成熟，自主性只有在信任、验证和治理指标显示出改进时才会扩展。结果不是“无人自动化”，而是一种具有保证的自动化模型，其中代理式系统自信地行动，而人类则保持舒适的控制。

## **企业如何衡量影响**

尽管公开的基准仍在出现，但行业数据显示，智能自动化已在提高运营可靠性。思科的[CrossWorks报告](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/crosswork-network-automation/white-paper-c11-741691.html?utm_source=chatgpt.com)强调了由于主动扩展和预测性警报而导致的成本和停机时间减少。CableLabs已通过将代理式AI集成到其监控生态系统中，记录了电信现场操作中[响应能力的提高](https://www.cablelabs.com/blog/empowering-field-operations-with-agentic-ai)。

总而言之，这些例子清楚地表明软件运营正在从脚本驱动转向目标驱动。团队不再在故障后对指标做出反应，而是嵌入了从历史中学习并实时适应的智能。MTTR降低和升级减少这些指标不仅代表了一个成功案例，而且是跨行业可重复的模式。

除了数字运营，类似的代理式架构正在制造、能源和物流系统中涌现，其中自主决策循环实时保持正常运行时间并优化成本。工业和软件自动化的这种融合表明，代理式AI正成为现代运营的连接组织，它不仅监控自身，而且持续改进自身。

## **运营的新思维**

代理式AI不会淘汰工程师；它使他们的判断更有价值。目标不是取代人类直觉，而是消除由重复、可预测的工作产生的繁重任务，这些任务会消耗时间和注意力。

通过让系统在定义的限制内进行自我修正，团队可以专注于更高级别的问题：架构、弹性、客户体验。

最先进的软件组织将行为管理视为核心基础设施。当系统学习、人员适应和市场变化时，领导者的职责是保持自动化、意图和结果之间的一致性。过度控制会扼杀创新：控制不足会带来风险。由可解释、可测量的代理式系统支持的平衡是可持续速度的所在地。

下一个运营时代将不再由我们编写多少脚本来定义，而是由我们的系统学习、适应和改进的智能化程度来定义。这不仅仅是自动化；这是进化。