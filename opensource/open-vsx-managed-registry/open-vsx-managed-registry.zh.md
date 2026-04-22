[平台工程](https://thenewstack.io/platform-engineering-where-software-defined-storage-fits/)需要某种程度的信任。开发者需要“相信”基础层工具、[库](https://thenewstack.io/ui-libraries-are-dying-whats-next/)和仓库将始终提供充足的服务，且所有服务都已针对必要的权重、锐度和耐用性进行了优化。

为了确保其资源库得到妥善呈现，[Eclipse Foundation](https://www.eclipse.org/)（Eclipse 基金会）周二宣布推出 Open VSX 托管注册表（Open VSX Managed Registry）。该技术代表了开源社区第一个由基金会运营的、针对关键[开发者基础设施](https://thenewstack.io/the-hidden-toll-of-infrastructure-on-developer-productivity/)的托管服务。

## 什么是 Open VSX？

虽然[微软的专有归属](https://learn.microsoft.com/en-us/visualstudio/ide/compiling-and-building-in-visual-studio?view=visualstudio)意味着它在逻辑上拥有 VS Code 市场（VS Code Marketplace），但 [Open VSX](https://open-vsx.org/) 是一个针对基于 VS Code 扩展 API 构建的工具的开源、厂商中立的扩展注册表。Open VSX 代表 Visual Studio eXtensions（Visual Studio 扩展），从这个意义上说，[扩展注册表](https://thenewstack.io/eclipse-open-vsx-registry-offers-open-access-to-vs-code-extensions/)可以被定义为一个中央仓库，供软件开发者搜索（或发布）并安装代码扩展（漏洞修复程序、自动格式化和代码自动补全工具等）或插件。

Open VSX 托管注册表提供了一个由 AI 原生 IDE、云开发环境和兼容 VS Code 的平台组成的生态系统。其中包括 [Amazon 的 Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/)、Google 的 Antigravity、Cursor、VSCodium、[Windsurf](https://windsurf.com/)（一款 AI 原生编程助手）、Ona（构建于 [Gitpod 基础](https://www.linkedin.com/posts/jan-ebbinghaus_big-news-today-were-introducing-onacom-share-7335682100974526467-T7be/)之上）等。商业采用者将获得 99.95% 的[上线时间 SLA](https://thenewstack.io/slo-vs-sla-whats-the-difference-and-how-does-sli-relate/)、服务抵免、定义的各种支持层级，以及针对持续生产规模使用的企业级运营保障。

> “Open VSX 对开发者、开源项目和各种规模的组织保持开放和可访问，但长期的可靠性和安全性并非偶然。” —— Mike Milinkovich，Eclipse 基金会执行董事。

## 平衡开放性与健壮性

执掌该项目的是 Eclipse 基金会执行董事 Mike Milinkovich。Milinkovich 向 *The New Stack* 解释说，这里确实存在一种平衡行为，他团队的方法核心是找到合适的水平，在忠于开源原则的同时，确保资金到位以支持大规模关键基础设施的运行。

“Open VSX 对开发者、开源项目和各种规模的组织保持开放和可访问，但长期的可靠性和安全性并非偶然。这种模式允许我们在保持开放性的同时，确保平台能够在大规模环境下运行并获得信任，”Mike Milinkovich 说道。

随着软件工程师现在使用 AI 驱动的开发工具来加速自动化、推动持续安装并创建日益繁忙的新机器对机器流量通道，扩展注册表已成为值得信赖的、始终在线的基础设施中的高吞吐量元素。

Eclipse 基金会的 CMO Thabang Mashologu 告诉 *The New Stack*，在扩展注册表的演进曲线上有一个重要的进步点需要注意：曾经主要享受社区规模使用的技术，现在需要反映出全球范围内持续的商业平台依赖性。

“Open VSX 托管注册表的首要任务很简单：为依赖它的开发者和项目保持关键开源基础设施的开放、安全、可靠和可持续，”Thabang Mashologu 说道。“广大社区依然可以免费访问，而供应商和企业则受益于弹性且厂商中立的平台，该平台提供他们自信地构建和扩展所需的稳定性和性能。”

Open VSX 现在每月提供超过 [3 亿次下载](https://thenewstack.io/open-vsx-aws-investment/)，日均流量峰值超过 2 亿次请求。该注册表托管了来自 7,000 多个“发布者”（指团队、特别兴趣小组、商业软件工程单位，但主要是个人）的 10,000 多个扩展，随着 AI 原生开发工具和云平台的普及，它将继续快速增长。

## AWS、Google 和 Cursor 已加入

Open VSX 托管注册表的首批客户包括 Amazon Web Services、Google 和 Cursor。这些组织共同表示，他们采用该托管服务是为了确保生产级的可靠性、定义的服务水平以及企业开发者平台的可预测扩展。

在这种规模下运营全球扩展注册表需要对计算能力、带宽、存储、安全运营以及维持可用性和弹性所需的工程专业知识进行大量投资。AI 驱动的开发正在加速这一需求。这些因素再次强调了 Eclipse 基金会强化整体产品的决定。

通过自动化工作流和编程智能体，单个开发者现在产生的基础设施负载可以与数十个传统用户相当，从而增加了流量规模和运营复杂性。该服务专为将 Open VSX 用作商业产品、AI 规模服务或企业开发环境中的关键基础设施的组织而设计；因此，它将运营责任与生产系统的期望对齐。

> ## 自由的代价

个人开发者和开源项目使用 Open VSX 注册表永远不需要付费。发布、搜索和标准开发工作流程保持不变。开源 IDE 和社区项目继续受益于 Eclipse 基金会所称的“慷慨”的免费层级限制。

该团队进一步指出，托管服务通常比自托管同等规模的全球基础设施更具成本效益。在商业层面，它指出组织现在可以在保持厂商中立和透明治理的同时，依靠定义的服务水平。

这里正在发生一种明确的转变。Eclipse CMO Thabang Mashologu 将这一时刻称为 AI 智能体“改变了开发者基础设施经济学”的时刻。

过去扩展注册表通常由人类开发者访问，而现在作为平台工程项目一部分的 AI 智能体需要新水平的机器级流量吞吐量。这很可能支撑了 Eclipse 基金会加强开源社区和商业企业用例的双层策略。