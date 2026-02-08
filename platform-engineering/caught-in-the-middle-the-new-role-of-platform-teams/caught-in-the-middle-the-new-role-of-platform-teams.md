<!--
title: 平台团队：夹缝求生与角色重塑
cover: https://cdn.thenewstack.io/media/2026/01/91a1eeca-sign.jpg
summary: 平台团队职责扩大，需处理安全、成本、合规等跨领域问题。他们承担责任却常缺乏决策权，导致结构性矛盾。组织需赋权平台团队，提高其可见性和参与度。
-->

平台团队职责扩大，需处理安全、成本、合规等跨领域问题。他们承担责任却常缺乏决策权，导致结构性矛盾。组织需赋权平台团队，提高其可见性和参与度。

> 译自：[Caught in the Middle: The New Role of Platform Teams](https://thenewstack.io/caught-in-the-middle-the-new-role-of-platform-teams/)
> 
> 作者：Yaron Yarimi

今年早些时候，一家全球性银行的平台团队为开发人员引入了一种新的工作流程，以按需配置云环境。目标是提高交付速度并减少对人工审批的依赖。基础设施顺利推出。几周内，团队开始在 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention) 云平台 (GCP) 和 [Microsoft](https://aka.ms/modelmondays?utm_content=inline+mention) Azure 上启动工作负载。

随后，问题开始出现。

财务部门询问为什么某些环境在高成本区域运行。安全部门标记了缺少加密标签的资源。合规部门询问非生产环境的日志是否按照内部政策存储。数据团队询问平台是否可以集成一个 [AI 代理](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/)来自动检测和修复漂移。

这些都不是事故。没有任何东西发生故障。系统完全按照设计运行。

但每个问题都需要深入了解组织的不同部分。[云配置](https://thenewstack.io/tech-veterans-new-approach-to-eliminate-configuration-hell/)。内部政策。团队行为。[风险暴露](https://thenewstack.io/ai-can-deliver-deployment-aware-risk-analysis-for-kubernetes/)。没有哪个单一群体拥有全局视图。

然而，平台团队仍然被期望给出答案。

## 企业规模下的日常决策

在大型企业中，基础设施工作是按设计分布的。应用团队拥有服务。安全部门定义防护措施。合规部门定义要求。财务部门跟踪支出。基础设施团队管理共享基础。

每个团队都在部分上下文中运作。

平台团队最接近将所有这些连接起来的工作流程。因此，他们被卷入跨多个领域的决策中。

在一个典型的星期里，平台团队可能会被要求解释：

* 为什么工作负载在一个技术上允许但在操作上不鼓励的区域启动。
* 为什么某些资源缺乏成本归属，尽管存在标签标准。
* 当涉及多个身份系统时，访问模式是否符合内部政策。
* AI 辅助的工作流程是否可以像手动工作流程一样进行审计。

这些并非极端情况。它们是规模化、去中心化和持续变化中出现的日常问题。

[![一张示意图，中间的白圈代表平台团队。平台团队周围有五个团队，每个团队都有不同的断开连接的上下文和工具：安全、财务、基础设施、合规和应用。](https://cdn.thenewstack.io/media/2026/01/13444c9b-platform-schematic-1024x848.png)](https://cdn.thenewstack.io/media/2026/01/13444c9b-platform-schematic-1024x848.png)

*来源：env zero。*

## 平台工程不断扩大的作用

平台团队最初的职责是提高交付速度和一致性。随着时间的推移，这项任务已经扩大。

如今，平台负责人需要权衡：

* 安全态势和强制边界。
* [成本控制和效率权衡](https://thenewstack.io/factor-cost-efficiency-into-platform-engineering-for-growth-profitability/)。
* 合规可见性和审计准备。
* 变更和访问管理。
* 在基础设施工作流程中安全使用 AI 代理。

他们不仅在构建系统，还在塑造具有财务、监管和运营后果的决策。

然而，这些期望很少伴随着相应的权力。

## 无结构下的责任

平台团队经常被要求解释他们并未直接导致的结果。他们被期望在不拥有政策、预算或工作负载的情况下提供答案。

这造成了一种结构性张力。

团队有足够的上下文来承担责任，但没有足够的杠杆来设定方向。他们成为未解决问题落脚的地方，仅仅因为他们最接近执行层。

随着每日基础设施事件、环境变化、访问更新、政策评估和 AI 驱动行动的数量增加，这种张力愈演愈烈。工作重心从构建转向跨团队的解释、协调和决策 обоснование。

## 需要改变什么

如果平台团队要继续在这个交汇点运作，组织需要[调整支持他们的方式](https://thenewstack.io/driving-platform-adoption-community-is-your-value/)。

这意味着：

* 使跨环境、团队和服务的权限可见。
* 让平台负责人更早地参与政策和治理讨论。
* 提供记录和解释决策原因而非仅仅记录变更的系统。
* 赋予平台团队在需求冲突或超出容量时拒绝的能力。

这些团队已经充当了协调层。围绕他们的结构尚未跟上。

## 结论

平台工程不再局限于基础设施交付。它已成为一个跨越安全、合规、财务和运营的决策职能。

这种转变并非一蹴而就。随着系统规模的扩大和职责的碎片化，它逐渐显现。

平台团队现在必须在组织的核心运作。认识到这一现实是正确支持它的第一步。