<!--
title: Agentic AI和平台工程：如何结合
cover: https://cdn.thenewstack.io/media/2025/04/d688f5d6-ai-agents-platform-engineering-2.jpg
summary: 告别 Kubernetes 技能焦虑！🚀 Agentic AI 平台 Kubiya 赋能平台工程，用 AI Agent 大幅提升 SRE 效率，MTTR 缩短至 30 分钟，事件减少 80%，成本降低 20%。Open Policy Agent 加持，安全合规无忧，DevOps 团队效率起飞！
-->

告别 Kubernetes 技能焦虑！🚀 Agentic AI 平台 Kubiya 赋能平台工程，用 AI Agent 大幅提升 SRE 效率，MTTR 缩短至 30 分钟，事件减少 80%，成本降低 20%。Open Policy Agent 加持，安全合规无忧，DevOps 团队效率起飞！

> 译自：[Agentic AI and Platform Engineering: How They Can Combine](https://thenewstack.io/agentic-ai-and-platform-engineering-how-they-can-combine/)
> 
> 作者：Jennifer Riggins

在 [Kubernetes 推出十多年后](https://thenewstack.io/how-the-kubernetes-community-celebrated-its-10th-anniversary/)，即使容器编排器的采用率飙升，技能差距仍然存在。

对于需要 K8s 来扩展的企业来说，这是一个大问题。对于 [Sebastian Kister](https://www.linkedin.com/in/sebastiankister/) 来说，[Kubernetes](https://thenewstack.io/kubernetes/) 已经成为计算的公共交通。

“Kubernetes 使自动、大规模以及最安全和可靠地提供计算能力成为可能——这对于我们以前拥有的许多其他技术来说并非如此，” Kister 说，他是汽车制造商 [Audi](https://www.audi.com/en/company/) 的容器能力中心、平台和运营团队的产品团队负责人，也是其他企业的转型顾问。

但这并不意味着 Kubernetes 变得更容易使用。

“挑战尤其在于使用它的人的技能，”他说。“市场使得很难找到真正的高级 [对 Kubernetes 有深刻理解的人](https://thenewstack.io/talent-shortages-shouldnt-kill-your-cloud-native-journey/)。”

最近，当他的一个团队想要添加 12 个新集群时，问题达到了顶峰，[站点可靠性工程](https://thenewstack.io/google-sre-site-reliability-engineering-at-a-global-scale/) 团队回应说：我们需要时间来寻找和雇用更多的 SRE。

随着 Kubernetes 周围的所有自动化设施到位，Kister 对扩展的如此多障碍感到惊讶。面对这些长期存在的复杂性、漏洞和事件，Kister 转向了 [AI](https://thenewstack.io/ai/)。

六个月前，Kister 采用了 [Kubiya ](https://www.kubiya.ai/)agentic AI 平台来支持安全响应，正如他所说，“实时、上下文感知和持续更新”。这种对 agentic AI 的采用不仅使他合作的一家企业从风险接受转变为积极、智能的补救——它还减少了团队摩擦并阻止了互相指责。

## Agentic AI 辅助非对称扩展

像最近的大多数公司一样，Kister 的 [平台工程](https://thenewstack.io/platform-engineering/) 和运营团队感到在预算缩减和流程僵化的情况下扩展的紧迫压力。

“我们无法足够快地招聘，并且大规模地教育初级人才太慢且不可预测。市场几乎不可能吸引顶尖人才，”Kister 说。

“我们必须找到另一种方法——一种不依赖稀缺资源的非对称扩展方式。”

Kister 旨在利用 [AI 代理](https://thenewstack.io/ai-agents/) 来消除繁琐的工作和事件修复，将高级开发人员从运营任务中解放出来，并将所有开发人员从注意力漂移中解放出来。他着眼于 agentic AI 平台，在这些平台上，可以对 AI 代理进行特殊任务的培训，以消除重复性任务，并将重点更多地转移到功能、创新和使用该平台的项目的启用上。

## 构建一支非常具体的 AI 代理军队

利用 AI 代理的计划不是为每个用例部署一个 AI 代理。

它甚至不遵循涵盖 80% 工程师的用例的常见 [平台工程](https://thenewstack.io/platform-engineering/) 实践。目前，Kister 的团队正在优先考虑围绕运行时安全性、可靠性和事件修复的 AI 代理用例，这些用例会影响所有工程团队。

Kubiya 具有“agentic 原生”[内部开发者平台](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/)，用于可编程代理，这些代理被配置为充当软件开发团队的专用 SRE AI 代理士兵。开箱即用有 200 个 AI 代理用例，但与所有平台工程计划一样，组织可以使用针对特定用例的自定义代理在其基础上构建。

Kubiya 在该公司的 [Red Hat OpenShift](https://www.openshift.com/try?utm_content=inline+mention) 集群中运行，跨其环境进行扩展，并集成在其 [身份和访问管理 (IAM)](https://thenewstack.io/10-best-practices-for-building-a-robust-iam-strategy-in-2024/) 和 [基于角色的访问控制 (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/) 策略中，并具有所有生产就绪的安全性和合规性护栏。

“我们拥有完全的可见性和控制权，并且我们相信这些代理会准确地执行他们应该做的事情——不多也不少，”Kister 说。

与其他仍在努力解决[幻觉](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/)问题的AI Agent平台不同，Kubiya增加了可编程性和可预测性控制，因此即使开发人员要求AI Agent执行超出范围的操作，它也会将响应限制为仅限于工具调用和授予它的权限。

该范围非常特定于它有权访问的策略或环境。它是[Open Policy Agent](https://thenewstack.io/the-open-policy-agent-journey-from-sandbox-to-graduation/)强制执行的，因此可以在本地或气隙环境中使用。

Kister说：“它不是软件即服务。它是你经过特殊训练的海豹突击队，每天每夜，全天候24/7都在那里做这项工作。”他补充说，这极大地促进了企业的弹性。

此外，通过依靠Kubiya内部的SRE来创建AI Agent劳动力，他的一些客户的平台团队能够在不增加另一项培训（或者像他所说的那样“一个庞大的团队”）的情况下扩展该技术，以学习这些新兴技能。

Kubiya拥有一个完整的AI平台，允许组织在其之上构建或引入自己的AI Agent，以用于生产就绪的用例。它还提供了一个企业版本，其中包括本地部署、大型语言模型的选择和服务协助，Kister的团队依靠这些来避免增加另一个技能差距。

他说：“我购买了一个AI‘平台工程师’，以在生产级环境中部署Agent工作流程。然后，随着需求的扩展，我们可以利用这种非对称的方式将我们的劳动力扩展到新的业务领域。”

“目前，由于我没有人员或知识来进行横向扩展，因此我使用他们预构建的AI Agent存储库来增强我的团队在运行操作方面的努力，而无需三思而后行。”

## 衡量AI Agent平台的成功

一项工程策略的好坏取决于它的衡量标准。

Kister说，在Kubiya之前，常见的漏洞和暴露（CVE）会出现在Jira中，被视为例行任务——尽管它们绝非如此。

他说：“该积压工作延迟了响应并暴露了风险。借助Kubiya，我们自动化了关键任务操作——随叫随到的处理、实时补救和运营转移——使我们的顶级开发人员摆脱了上下文过载，从而可以专注于创新。”

在短短六个月内，大规模的安全性得到了证明：

- 平均修复时间（MTTR）从8小时缩短到30分钟。
- 每周修复时间从64小时减少到4小时。
- 由于主动的、AI驱动的故障排除，事件减少了80%。
- 工程师的重复请求减少了80%。
- 通过识别不必要运行的失败部署，云基础设施成本的年度运行率降低了20%。
- 合规性审计和安全检查现在只需一半的时间即可生成。

Kister说，该项目使团队的价值主张翻了一番，因为工具成本仅增加了10%，所有这些都由他专注的小团队管理。

## AI Agent帮助开发人员沟通

Kubiya不仅消除了一些最大的技术挫折，而且还消除了很多的人际关系挫折。

Kister说：“这个小Agent会与你的初级开发人员交谈，它可以提供见解，而且我们消除了互相指责的情况”，因为如果某些东西不符合标准，平台将不允许部署它，并且开发人员确切地知道原因。

开发人员只需与AI Agent进行对话，询问：这里发生了什么？你的建议是什么？他说，将来，他的团队还将测试使补救措施更加自动化。

现在，“80%的故障排除已经不在话下，因为它通过AI，通过坐在那里的小Agent立即变得清晰，”他说。“你问它，这里发生了什么？它就像：你有没有根本原因？是的，它会告诉你根本原因，你就知道发生了什么。”

许多这些[核心开发人员生产力指标](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/)是成本的渠道，因为它减少了工程师花费在寻找出错原因的挫败感上的时间，并将这些时间重新分配给更快地创建新功能。

借助Kubiya的新AI Agent平台，Kister的团队——及其内部开发人员客户——可以解锁可观测性，非对称地扩展构建，并真正以更少的资源做更多的事情。或者，更好地说：用他拥有的团队做更多的事情。