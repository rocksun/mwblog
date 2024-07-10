
<!--
title: Kubernetes丛林中的隐形黑客猎杀
cover: https://cdn.thenewstack.io/media/2024/07/8bc09b6e-cncf-security.jpg
-->

让日志分析成为您 Kubernetes 安全探险之旅的指南。

> 译自 [Hunting the Stealth Hacker in the Kubernetes Jungle](https://thenewstack.io/hunting-the-stealth-hacker-in-the-kubernetes-jungle/)，作者 Steven J Vaughan-Nichols。

西雅图 —  在 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 上个月举办的 [CloudNativeSecurity 大会](https://events.linuxfoundation.org/cloudnativesecuritycon-north-america/) 上，来自云和软件即服务 (SaaS) 安全公司 [Mitga](https://www.mitiga.io/about/about-us) 的安全专家 [Stav Ochakovski](https://www.linkedin.com/in/stav-ochakovski) 和 [Ariel Szarf](https://www.linkedin.com/in/ariel-szarf-89b024197/?originalSubdomain=il) 讨论了他们如何使用日志在 [Kubernetes 环境](https://thenewstack.io/Kubernetes) 中追踪威胁行为者。

毕竟，正如 Ochakovski 所说，攻击者很可能已经潜入了你的基于云的 [Kubernetes 集群](https://thenewstack.io/managing-kubernetes-clusters-for-platform-engineers/)。事实上，Ochakovsk 评论道：“问题不在于 Kubernetes 环境中是否存在威胁行为者，而在于它在哪里。”

他们认为，你不能对云安全掉以轻心。这是因为，随着越来越多的组织将他们的 [Kubernetes 集群迁移到云](https://thenewstack.io/using-prometheus-to-monitor-kubernetes-clusters-running-cloud-foundry/)，被可扩展性和托管服务的承诺所吸引，他们往往在不知不觉中为精明的攻击者打开了大门。

Ochakovski 和 Szarf 生动地将现代威胁狩猎描述为一场高风险的“找瓦尔多”游戏。因此，他们认为，即使你没有看到攻击者的迹象，你也应该积极地寻找他们的踪迹。

毕竟，“有时，恶意行为者会成功地入侵环境，而不会触发检测服务，”Szarf 说。

他们的方法既系统又直观。它从选择关于潜在攻击向量和动机的具体假设开始。例如，攻击者可能会针对云存储桶中的敏感数据。

下一步是建立一个潜在攻击指标列表，然后对环境中的任何可疑活动进行彻底调查。任何异常都可能是敌人靠近的信号。

如何发现这些异常？仔细查看 [你的 API](https://thenewstack.io/API-management/) 服务器日志、调度程序日志、控制器管理器日志、审计日志和 Kubernetes 的身份验证器日志，以及云特定的日志，例如 [Amazon Web Services 的 CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)。

## 你的 Kubernetes 集群如何被入侵

演讲者们走过了一个假设场景，攻击者获得了对 Kubernetes 集群的持久访问权限，并利用它作为跳板访问敏感数据。

他们强调了三个需要关注的关键指标：从外部帐户创建对集群的持久访问权限、来自未知来源的 [连接到集群](https://thenewstack.io/simplifying-cluster-connectivity-with-istio-service-mesh/) 以及对敏感云资源的意外访问。

Ochakovski 和 Szarf 强调了从 [Kubernetes 生态系统和云提供商](https://thenewstack.io/kubernetes-autoscaling-q-a-with-fairwinds-cto-andy-suderman/) 启用和收集相关日志的重要性，以便找到这些攻击的无声先兆。这些日志是 [安全团队可以追踪](https://thenewstack.io/observability-is-shifting-left-following-security-and-ops/) 的足迹，以发现潜在的威胁。

“如果我们想让你从这次演讲中带走一个关键的要点，那就是问正确的问题，”Ochakovski 总结道。这种观点概括了有效威胁狩猎的本质——一种积极主动、好奇的心态，它假设威胁的存在并积极地寻找它们。

简而言之，仅仅寄希望于最好的结果是不够的。组织必须积极主动地 [寻找威胁](https://thenewstack.io/5-ways-to-automate-threat-hunting/)，并配备合适的工具、知识，以及最重要的，正确的、怀疑性的问题。

如果这听起来很偏执，那么，正如谚语所说，“如果他们真的想对你下手，那就不叫偏执。” 而且，当涉及到 [公共云上的 Kubernetes 集群](https://thenewstack.io/private-vs-public-cloud-how-kubernetes-shifts-the-balance/) 时，攻击者真的想对你下手。


!