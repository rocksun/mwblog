
<!--
title: 从源头开始，改善 MTTR
cover: https://cdn.thenewstack.io/media/2024/08/02dc7353-improve-mttr-start-at-beginning.jpg
-->

为了减少停机后的平均恢复时间 (MTTR)，您必须首先处理棘手的问题。

> 译自 [To Improve MTTR, Start at the Beginning](https://thenewstack.io/to-improve-mttr-start-at-the-beginning/)，作者 Rita Manachi; David Zendzian。

IT 系统始终面临着恶意或非恶意威胁，以至于安全漏洞已变得司空见惯。举个例子，在我们开始撰写这篇文章时，有消息称 [450 万人受到影响](https://www.darkreading.com/cloud-security/cyberattackers-accessed-healthequity-customer-info-third-party) ，这是最近 HealthEquity 数据泄露事件造成的。

随着我们的云原生系统不断扩展，其分布式特性也使其变得更加复杂。这种复杂性为我们提供了灵活性，但也暴露了更多故障点和入侵点。

成为人为错误、代码编写不当或恶意攻击的受害者，不仅仅是关于直接的业务影响。如果公司无法快速恢复，他们可能会面临 [政府审查](https://apnews.com/article/technology-outage-delta-air-lines-delays-7361e641fe2c656d7fba06e4a0424c6a) 、数十亿美元的罚款甚至法律诉讼。

因此，虽然最近的 [CrowdStrike 灾难](https://thenewstack.io/7-urgent-lessons-from-the-crowdstrike-disaster/) 确实登上了头条，但重要的是其后续影响。这也让我们重新审视了平均恢复时间 (MTTR)，特别是如何缩短从故障或恶意攻击中恢复所需的时间。正如 DevOps 研究与评估 (DORA) 团队所定义的，[MTTR](https://dorametrics.org/how-to-calculate-dora-metrics/) 是“当发生服务中断（如停机）时，您的团队恢复服务的平均时间”。

## 首先解决难题

在改变您的技术方法之前，您必须改变组织的思维方式。从将安全融入您的软件开发生命周期 (SDLC) 开始，从代码到生产再到管理。改变行为比采用新工具或 [平台](https://thenewstack.io/cloud-native-app-platforms-new-research-shows-struggles-and-hope) 难得多，如果没有这种文化转变，您所做的技术选择将毫无意义。

- **停止将安全视为结果**：安全不是单一事物，如今的 [云原生生态系统](https://thenewstack.io/are-custom-cloud-native-stacks-worth-the-security-tradeoffs) 非常脆弱且相互关联。与其设置可能阻碍数周工作的重大检查点，不如在 [整个 SDLC](https://thenewstack.io/dont-shift-security-left-integrate-it-everywhere) 中检查安全，从开发人员开始。
- **拥抱产品思维**：开发人员使用的平台是动态的，需要以这种方式对待它们。这意味着将平台视为需要随着时间推移进行升级、修补和改进的产品。确保将平台工程师、合规架构师和安全专家纳入您的平台交付和策略。正如许多人（包括互联网安全中心）[所说](https://www.cisecurity.org/insights/blog/cybersecurity-is-a-team-sport)，“安全是一项团队运动”。
- **让安全变得容易**：将安全融入您的流程。为开发人员提供自助访问自动更新和修补的应用程序和代码模板、经过批准的开源和商业软件目录、构建包、带有策略控制的 [API 网关](https://roadmap.sh/best-practices/api-security) 等。确保他们能够安全地使用他们喜欢的工具！

## 深入技术细节

您的平台选择对您的安全态势至关重要。寻找支持基于 DevSecOps 的工作模型的安全增强功能和功能。提高您当前员工在 [平台工程](https://thenewstack.io/platform-engineering/) 和 [合规架构](https://tanzu.vmware.com/content/blog/modern-compliance-architect-what-it-is-and-why-you-need-one#:~:text=A%20Tanzu%20Labs%20Modern%20Compliance,to%20regulatory%20and%20industry%20requirements.) 等新学科方面的技能。

**蓝绿部署** 是一种可以减少应用程序停机时间和风险的技术，它运行两个相同的生产环境，一个“蓝色”环境和一个“绿色”环境，其中只有一个环境处于活动状态并提供生产流量，另一个环境处于闲置状态。只有在经过适当测试后，闲置环境才能开始提供生产工作负载。

**金丝雀部署** 是另一种在生产环境中测试新软件或更新可行性的方法。您将新软件或更新的某些部分发送到生产环境，并观察其运行情况。如果一切顺利，您将发布更多部分。它是另一种现代应用程序交付范式的一部分，称为渐进式交付，由 [RedMonk 的 James Governor](https://redmonk.com/team/james-governor/) 几年前提出。[蓝绿部署和金丝雀部署](https://thenewstack.io/primer-blue-green-deployments-and-canary-releases/) 的共同点是，如果出现问题，它们允许您轻松回滚到已知正常版本的软件，而不会造成重大中断。

**测试驱动开发 (TDD)** 对于持续发布稳定且有弹性的应用程序至关重要。要充分利用 TDD，不要只对您添加的内容进行功能测试。您需要在其他所有内容的上下文中测试新部分，因此请确保在您的方法中包含定期模糊测试、混沌测试或故障测试。

**错误处理和监控** 与强大的日志 [监控和可观察性](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) 相结合，可以捕获问题发生时的问题，并限制故障范围。

**基于策略的自动化** 可以改进软件交付和维护流程的多个方面。为了安全地自动化安全的多层，请从各个团队获取输入，包括平台工程安全、合规性以及基础设施和运营 (I&O) 团队。这将有助于使定义自动化流程的策略更加全面，以减轻灾难性停机或减少损失。

## 三个先于四个

在 VMware Tanzu 推出 [四个黄金命令](https://tanzu.vmware.com/content/blog/introducing-vmware-tanzu-platform)（构建、绑定、部署和扩展）之前，有 3R（旋转、重铺和修复）。它们提供了一种简单的方法来查看云原生平台的安全属性。3R 背后的理念是，速度越快，安全性越高。

- 每隔几分钟或几小时旋转一次数据中心凭据。
- 每隔几小时从已知正常状态重新铺设数据中心中的所有服务器和应用程序。
- 在补丁可用后的几个小时内，始终修复易受攻击的操作系统和应用程序堆栈。

3R 仍然是 Tanzu 平台的核心原则，您可以关注我们的博客以了解有关 [Tanzu 和安全](https://tanzu.vmware.com/content/vmware-tanzu-and-security) 的更多信息。

确保从停机或安全漏洞中恢复不会对应用程序开发和交付流程造成破坏，其中涉及多个因素，包括平台选择、开发风格（例如，敏捷、极限、测试驱动）以及组织或文化因素。

与其将安全视为单一结果，不如专注于交付安全的软件供应链；支持以安全为中心的文化；自动化补丁、升级和策略执行；关注策略漂移和监控；并采用其他安全启用结果。
