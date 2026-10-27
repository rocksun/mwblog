
<!--
title: AI正在改变Kubernetes：你的平台准备好迎接2027年了吗？
cover: https://cdn.thenewstack.io/media/2026/10/3e349844-logan-voss-r0gpjz0z1c8-unsplash-scaled.jpg
summary: 本文介绍了The New Stack联合HPE出版的新电子书，探讨了AI与智能体如何改变Kubernetes平台建设，并提供了涵盖安全、运维及架构的实用检查清单，助力团队应对2027年的技术挑战。
-->

本文介绍了The New Stack联合HPE出版的新电子书，探讨了AI与智能体如何改变Kubernetes平台建设，并提供了涵盖安全、运维及架构的实用检查清单，助力团队应对2027年的技术挑战。

> 译自：[AI is changing Kubernetes; is your platform ready for 2027?](https://thenewstack.io/kubernetes-agentic-ai-platforms/)
> 
> 作者：Nick Lucchesi

**包括使用智能体AI在内的AI工作负载**，只会增加和改变Kubernetes团队必须回答的问题。仅仅询问Pod是否在运行已经不够了。或者模型生成第一个Token需要多长时间。或者当推理流量激增且没有额外的GPU容量可用时会发生什么。

越来越地，诸如之类的问题正在成为平台问题，与已经熟悉的升级、恢复和安全工作并列。

这就是为什么 *The New Stack* 刚刚发布了 ***[Kubernetes in 2027: Building Platforms for AI, Autonomy, and Scale](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)****,* 这是一本由 Chris J. Preimesberger 撰写、与 HPE 合作推出的新电子书。

[![](https://cdn.thenewstack.io/media/2026/10/3c198509-screenshot-2026-10-26-at-15.38.15.png)](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)

这本电子书从上线*之前*的工作开始——上线之前。我们要求团队在现实负载下对模型服务系统进行压力测试、演练故障，并衡量GPU利用率以外的指标。

它还对智能体进行了清醒的审视。赋予智能体集群访问权限是一个具有重大影响的决定，即使它的任务听起来很常规。

该指南呼吁明确所有者、严格权限、审批关卡，以及将工具调用与其提示任务连接起来的审计追踪。它要求团队评估AI输出质量。当答案错误时，快速的回答带来的安慰微乎其微。

而且这本电子书并未将AI视为忽视平台其余部分的理由。检查点涵盖了跨集群的策略、对Kubernetes之外服务的可见性、升级和恢复演练、运维所有权以及开发者自助服务。

**[检查清单](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)** 详细说明了可能落在团队之家的工作。

你能看出哪些集群遵循了共享的访问和网络基线吗？（谁批准了例外情况？）

还有：当应用程序变慢时，你能超越Pod指标，查看它依赖的数据库、虚拟机、网络或外部服务吗？在下一次升级之前，你是否检查过已移除的API，并练习了恢复集群状态和应用程序数据？

接下来是部署之后的工作：谁来续订Ingress证书？谁来签署容量变更？如果开发者通过服务目录请求环境，它是否带有所有者、审查日期以及查看其成本的方法？

这些是平台团队、应用团队、安全团队和业务团队之间进行对话的实用提示。**[在开始对话之前立即下载电子书](https://thenewstack.io/ebooks/kubernetes/kubernetes-in-2027/)**。