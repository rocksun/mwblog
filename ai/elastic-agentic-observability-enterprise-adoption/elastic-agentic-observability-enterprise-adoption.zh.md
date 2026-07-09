**几十年来，软件工程师一直是企业的眼睛和耳朵**，他们埋头于海量的日志、可观测性工具、控制台、浏览器标签页及其他应用程序数据中。他们的目标是什么？寻找并修复代码异常与已知稳定安全代码状态之间的模式偏差。

然而，这些由人工驱动的观测往往效率低下，需要大量工程师来处理不断增长的工作负载，并识别各种问题与威胁。工程师必须手动建立假设、调查数据和事故，然后确定最佳的补救方案。

如今，一种更先进的方法出现了。

IT可观测性正在获得强大的新能力。根据Elastic的2026年报告《[可观测性的前景](https://www.elastic.co/resources/observability/report/landscape-observability-report?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000bbCw9IAE)》，[85%的组织以某种形式将生成式AI用于可观测性](https://www.elastic.co/resources/observability/report/landscape-observability-report?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000bbCw9IAE)。预计在两年内，这一数字将达到98%。自生成式AI（GenAI）和智能体AI（agentic AI）引入并发展以来，GenAI的作用正在扩大，帮助企业从反应式可观测性转向更主动、更具适应性的立场。借助GenAI，企业现在可以创建能够自主监控IT系统、解释数据和遥测信息并理解故障原因的AI智能体，从而改善系统和性能。

随着这种从主要依靠人工干预向自动化的转变持续进行，一些引人注目的、节省时间的新用例正在涌现，涉及GenAI对可观测性数据的调查。这些进步旨在服务于核心团队成员，[包括站点可靠性工程师（SRE）](https://www.elastic.co/observability/aiops)和IT运营人员，同时也为企业内的其他业务团队提供了宝贵的新机会，例如[DevOps](https://www.elastic.co/observability/devops)、网络安全、合规和业务线员工。

例如，产品经理可以使用智能体AI和GenAI工具对新版本进行A/B测试，以获取区域和细分层面的转化数据。财务团队可以使用GenAI助手审查与外部服务提供商的服务水平协议（SLA），以快速确定SLA是否得到满足。

## **GenAI对可观测性数据的影响以及AI智能体的帮助**

Elastic的首席解决方案架构师[Thaddeus Walsh](https://www.linkedin.com/in/thaddeuswalsh/)告诉The New Stack，通过转向由智能体管理的[可观测性工具](https://www.elastic.co/?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000bbCw9IAE)，企业可以改变SRE、安全团队、开发人员等的工作方式，将他们从不断管理和保护基础设施的负担中解放出来。

> “我认为这属于注意力经济。如果开发人员不必担心确保应用程序正常运行所需的基础组件，而只需专注于交付功能能力，那对他们来说将是完美的。”

Walsh表示：“我认为这属于注意力经济。如果开发人员不必担心确保应用程序正常运行所需的基础组件，而只需专注于交付功能能力，那对他们来说将是完美的。”

Walsh说，通过引入AI智能体来评估和使用与人类IT工作人员评估相同的遥测信号（包括日志、跟踪和指标），智能体可以自主更改应用程序的配置状态。“那将是一个理想的宇宙，人类永远不需要去触碰它。”

## **那么，为什么可观测性对企业IT团队如此重要？**

有了有效的可观测性工具和生成式AI，团队评估、监控和改进分布式IT系统性能的效果要比使用传统的人工监控方法好得多。这使组织能够在云原生环境的众多数据源中获得更深入的可见性和关键洞察。

Walsh表示，这些工具也有助于根因分析（RCA）调查，即通过评估代码行来识别问题，以便对其进行追踪和纠正。“根因分析调查比运营调查更深入。运营调查可能侧重于如何恢复到稳定状态，而根因分析则在于需要了解问题的起因。”

## **SRE和IT运营通常如何使用GenAI和AI助手**

Walsh表示，今天大部分的AI辅助调查工作仍然是在企业的运营侧完成的，因为技术人员需要了解当前的情况，然后确定最快的补救路径。

“SRE可能正在响应某个系统受到影响的事故，他们需要熟悉背景信息，”他说。“他们还会查看这种故障如何通过原始信号数据表现出来，以及调查中最可能的下一步是什么。他们试图寻找最合理的路径来验证他们的假设。”

---

根因分析调查在历史上最大的挑战之一是，要确定因果关系，你必须能够识别系统或应用程序组件之间的依赖关系。Walsh解释说，不幸的是，大多数相关的文档是不充分的，这使得根因分析在许多情况下非常困难。

Walsh说，文档不足是GenAI可以加强可观测性调查并改进SRE和IT运营人员根因分析的一个关键领域。

## **IT之外的组织用户也能从可观测性数据访问中受益吗？**

当然可以。非传统用户，如销售人员、财务团队、合规人员以及其他非开发人员，可以获得广泛的好处，包括将这些工具整合到他们自身调查中的新机会。

Walsh表示，可观测性平台捕获和评估的所有信息，包括来自日志、指标和跟踪的所有遥测数据，都能提供丰富的新途径，用于阐明客户和业务数据，从而为公司内更广泛的群体开启创新、创收和更好数据分析的新道路。

“用户的第一个障碍是访问数据，第二个是用户必须具备技能和知识，才能将来自可观测性平台的原始信号数据解释为对该利益相关者有意义的形式，”他说。“这是对数据驱动决策的渴望。”

## **IT之外的员工可以使用AI驱动的可观测性做什么？**

Walsh表示，其价值是巨大的。可观测性是一个定义系统生成的遥测数据捕获和分析的领域，所有这些都可以帮助企业更好地讲述他们的故事并做出更广泛的业务决策。

例如，[日志和GenAI](https://www.elastic.co/blog/generative-ai-logs-business-intelligence?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000q2MD2IAM)可以通过提供颗粒度极细的实时可见性和对系统问题的早期预警来帮助改善客户体验，这些问题可能会导致客户离开公司网站转投其他供应商。日志可以在延迟增加、间歇性错误或服务降级升级为大范围中断之前揭示这些细微问题，并且这些信号可以直接映射到服务水平指标（SLI），如响应时间或错误率，以便进行解决。

日志对于保障公司的收入也很重要，因为每一个性能问题、失败的交易或停机事件都给他们的底线带来了财务风险。通过使用GenAI驱动的、基于日志的洞察，公司可以识别哪些问题影响了创收服务、高价值客户或关键工作流程，然后实施调整和修复。

今天的日志不再仅仅是调试的工具。它们是真理的源泉，决策的驱动力，并且越来越多地成为组织的一种竞争优势。

## **组织如何实现AI驱动的可观测性民主化以提升其价值？**

Walsh表示，智能体AI和[AI智能体](https://www.elastic.co/elasticsearch/ai-assistanthttps://www.elastic.co/virtual-events/beyond-the-sre-democratizing-observability-data-with-genai?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc)的力量正在对当今整个行业的企业可观测性产生重大影响，但这些变化仍在进行中。

“我们正处于一个重要的转折点，因为大多数组织仍然依赖人工驱动的流程来执行他们的GenAI可观测性和根因分析调查。在接下来的24个月里，很有可能大多数企业将不再有以人为首的调查。他们将转向以智能体为首的调查，并在其所有系统中实现可观测性和数据访问。”

> “在接下来的24个月里，很有可能大多数企业将不再有以人为首的调查。他们将转向以智能体为首的调查。”

Walsh说，这种在整个企业及其员工中使用AI驱动的可观测性和流程的民主化，将随着公司重组其现有的可观测性生态系统以消除碎片化和孤立系统而成为可能。

“有很多组织正在小心翼翼地尝试AI，但他们没有任何自动化的协调，而且人类必须批准每一步。那会产生大量的摩擦，”他说。

想要了解更多信息？立即观看“[超越SRE：通过GenAI实现可观测性数据民主化](https://www.elastic.co/virtual-events/beyond-the-sre-democratizing-observability-data-with-genai?utm_source=publisher-direct&utm_medium=other-tns&utm_campaign=democratizing-o11y-genai-gc&utm_id=701Vv00000q2MD2IAM)”网络研讨会。