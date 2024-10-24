# 为什么基础设施即代码需要云资产管理

![Featued image for: Why Infrastructure as Code Needs Cloud Asset Management](https://cdn.thenewstack.io/media/2024/10/a7d5ed3d-iac-needs-cloud-asset-management-1024x576.jpg)

基础设施即代码 (IaC) 领域的戏剧性事件仍在继续。如果我们认为在 [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 许可证变更、项目随之分叉以及 [建立 OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/) 之后，一切都会平静下来，然后 [IBM](https://www.ibm.com?utm_content=inline+mention) 收购了 HashiCorp……好吧，再想想。

虽然一些专家会声称：“*Terraform 已死——[输入您最喜欢的 IaC 工具] 万岁*”，但我认为实际发生的事情完全不同，而且更有说服力。最近，我的联合创始人 [Eran Bibi](https://thenewstack.io/author/eran-bibi/) 在 [KubeCon 24 巴黎](https://thenewstack.io/kubecon-europe-webassembly-ebpf-are-huge-for-cloud-native/) 的一个小组讨论中谈到了“*”，我想更深入地探讨一下我所看到的正在发生的事情。* [IaC 的演变——关于开源和所有其他方面](https://www.youtube.com/watch?v=zaJK1YtsfrQ) 我从最近的公告和趋势中得出的一个主要结论是：如果你一直将 [Pulumi](https://www.pulumi.com?utm_content=inline+mention) 主要视为一个编排工具，那么 [其最新公告](https://www.pulumi.com/blog/pulumi-up-2024/) 可能会让你想要仔细看看。

我们一直在敲响“这不仅仅是 IaC——它也是一个完整的云资产管理世界！”的鼓声。当我们看到主要行业参与者验证我们的立场时，这令人兴奋。Pulumi 进入云资产管理领域。欢迎！

随着其定位重新聚焦于自动化、安全和管理，我认为 Pulumi 的转向证明了我们将在不久的将来在许多（如果不是所有）IaC 参与者中看到的转变。云库存、合规性和补救与编排一样重要，而且它们本质上是相互关联的。

Pulumi 的公告不仅仅是新闻。它表明了我们行业的发展方向，这是一个令人兴奋的方向。基础设施即代码和云资产管理的未来实际上是紧密耦合的——它可能会改变我们对当今云舰队规模的未来云操作的思考方式。

## Pulumi 在字里行间中说了什么

HashiCorp 死了吗？

Pulumi 的新愿景中包含了在 HashiCorp 许可证变更和 [被 IBM 收购](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/) 之后，接管竞争对手 HashiCorp。Pulumi 的平台现在包含三个核心产品：

- Pulumi IaC，用于任何编程语言的基础设施即代码。
- Pulumi ESC，用于安全自动化和密钥管理。
- Pulumi Insights，用于云资源和资产的可视化和分析视图。

只有时间才能证明市场是否已经成熟，可以接受来自成熟供应商的新方法，或者可以接受 HashiCorp Vault 的替代方案，但 Pulumi 的举动表明了明确的重点，即将云治理和可视化功能以及 AI 直接集成到基础设施即代码平台中，同时加倍投入开源承诺（有些人认为 HashiCorp 等公司已经放弃了开源承诺）。

Pulumi 的举动强调了我们长期以来知道的几个重要事实：

**云资产管理正在掀起波澜。**当像 Pulumi 这样的大型参与者开始朝这个方向发展时，就像一块巨大的广告牌说：“嘿，这个云资产管理的东西？它很重要。”

**IaC 的价值超越了配置。**基础设施即代码和云资源的编码是一个基本解决的问题。我们现在正在转向更高阶的问题，这不仅仅是部署新的基础设施，而是实际管理已经存在的基础设施（就像最终意识到你需要清理你的车库，而不是多年来只是把新东西塞进去）。

**日益增长的复杂性正在暴露传统云工具的长期问题。**此举证实了云环境正在变得越来越复杂。生态系统充斥着工具，而云运营工程师因选择和理解而感到不知所措，他们将真正推动减少手动工作量和认知负荷。这种复杂性为创新者和快速行动者创造了机会，让他们提供更好、更灵活的云管理工具。

## IaC 供应商仍然做错的地方

要了解如何在快速变化的 DevOps 环境中为变化做好准备并保持团队的敏捷性，你需要认识到你的对手是什么——更重要的是，你需要认识到你可能忽略了什么：

### 1. 多云环境正在增长，而且服务不足
根据我们的 [2024 年基础设施即代码状态报告](https://www.firefly.ai/state-of-iac-2024)，89% 的组织正在使用多云方法。36% 的组织甚至正在考虑扩展其多云基础设施。超过 50% 的组织拥有 10 个以上的云帐户，而另外四分之一的组织拥有超过 100 个云帐户，12% 的组织拥有超过 500 个云帐户。这包括 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention) 云平台 (GCP)、[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 等主要云平台。

尽管 Pulumi 的转向表明朝着正确方向的积极转变，但 IaC 解决方案供应商仍然忽视了云从业人员的多云现实，并继续以孤岛、桶和语言的方式思考云资产管理。随着公司继续将其资产分散到多个云中，能够跨不同提供商管理资源的工具将变得至关重要。

### 2. 云治理需要主动而非被动的方法

仅仅因为治理相关的见解对您来说是可访问的，并不保证您可以主动有效地采取行动来控制您的云。这就是为什么云治理仍然是使用 IaC 的主要挑战和目标之一的原因。真正的治理是关于主动的云控制和保护，而不是被动的洞察收集。

通过在每个阶段都考虑治理，您通常可以防止问题发生。当事件发生时，依靠 AI 自动提供解决方案可以节省时间，因为它可以快速修复问题。

那么，主动治理是什么样的？

**端到端（或代码到云）策略执行：**在流程的每个阶段实施“代码到云”治理：代码、CI/CD*和*云。**主动预防：**提前实施护栏以在违规发生之前捕获它们。**自动修复：**自动修复有两种形式。在主动预防中，护栏会通知用户代码违规并提供修复解决方案，然后再将其投入生产。第二种形式的自动修复侧重于现有的云资源。当您添加策略时，该解决方案会向您显示哪些资源违反了哪些策略，然后为您提供正确的修复方法。- 在 2024 年，
[任何 CI/CD 都能胜过 TACOS](https://thenewstack.io/for-infrastructure-as-code-ci-cd-can-beat-terraform)。
当 Terraform 自动化和协作软件 ([TACOS](https://www.firefly.ai/blog/lets-get-spicy----do-we-still-need-tacos-to-shave-the-iac)) 首次出现时，这些工具提供了一个引人注目的主张，但它们也可能成为云团队的单点故障。如今，TACOS 在现代 [DevOps 堆栈](https://thenewstack.io/2-open-source-ai-tools-that-reduce-devops-friction) 中的相关性正受到越来越多的质疑，尤其是那些已经拥有强大的 CI/CD 管道的组织。

真正的重点应该是赋予您当前的平台处理 IaC 所需的功能。简而言之：我们不需要更多工具或更多碎片化。随着 TACOS 的消亡，整合是您真正简化云管理的方式。

Pulumi 的扩展产品将与现有的 CI/CD 管道更无缝地集成。此外，Pulumi ESC 的引入将增强 CI/CD 管道中的安全实践，特别是在管理秘密和配置方面。这只会进一步推动远离 TACOS 的趋势。

## 云基础设施管理的下一步是什么？

自创建该类别以来，Firefly 一直在云资产管理方面领先并进行教育。现在，Pulumi 最近的战略举措表明，Firefly 正在设定一个标准，随着生态系统成熟，供应商将准备遵循该标准。

随着我们继续看到更多（地震）转变、更多参与者和更多创新，我们还将看到市场上的其他变化——最值得注意的是竞争越来越激烈。无论大小，所有参与者都希望成为下一个 Vault、下一个 Terraform，而且看起来，甚至成为下一个 [Firefly](https://www.firefly.ai/)。

愿我们继续朝着云一切管理的未来发展，愿最好的云工具获胜。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)