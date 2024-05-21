
<!--
title: IBM收购HashiCorp：开发人员、分析师和竞争对手怎么说
cover: https://cdn.thenewstack.io/media/2024/04/967925a7-hashicorp-ibm.jpg
-->

正如人们所料，在 IBM 即将收购 HashiCorp 公司后，公司内部的情绪是复杂的。

> 译自 [IBM Buying HashiCorp: What Devs, Analysts and Competitors Are Saying](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/)，作者 Chris J Preimesberger。

正如人们所料，在公司被 [IBM](https://www.ibm.com/cloud?utm_content=inline+mention) [即将收购](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) 后，HashiCorp 和 OpenTofu 社区对流行的 [基础设施即代码 (IaC) 软件工具 Terraform](https://thenewstack.io/how-to-manage-cloud-services-with-terraform/) 的未来看法不一。

蓝色巨人于 4 月 24 日宣布，将以 64 亿美元（每股 35 美元）收购 HashiCorp，并表示公司在被收购后仍将保持独立。但根据 [其之前在 IT 领域的收购](https://thenewstack.io/red-hat-ibm-acquisition-clash-of-cultures-or-best-of-both-worlds/) 的实际情况，并非所有人都相信这一承诺。

虽然社区中的一些成员对 HashiCorp 在出售前决定采用专有的 [业务源代码许可证 (BSL)](https://thenewstack.io/a-guide-to-leveraging-open-source-licensing/) 来代替标准的 Mozilla 公共许可证 v2.0（截至 2023 年 8 月）表示沮丧和失望，但其他人则认为这是一个让社区掌控并创建自己的项目分支的机会。

记录在案，[OpenTofu](https://opentofu.org/) 是一个 [分叉的开源基础设施即代码工具](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/)，开发为 Terraform 的 [社区驱动型替代品](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/)。它是为了回应 HashiCorp [决定采用](https://thenewstack.io/open-source-in-numbers-the-terraform-license-change-impact-on-contribution/) BSL 而创建的，BSL 将 Terraform 从开源更改为专有的源代码可用。

OpenTofu [现在由](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) Linux 基金会托管，允许用户通过人类可读的配置文件管理云和本地资源。它通过公共注册表支持广泛的服务，并使用状态文件来跟踪资源状态，从而实现计划-应用周期。

## 开发人员怎么说

自然而然，社区成员强烈希望将 Terraform 保留为开源项目。但 OpenTofu 正在迅速流行，2023 年 12 月注册的下载量超过 31,000 次。社区的一部分 [发布了一份宣言](https://devops.com/rebellion-against-changes-to-open-source-terraform-license-mounts/)，呼吁 HashiCorp 撤销最近对管理 Terraform 使用的许可证所做的更改。社区内的一个小组正在积极倡导该项目 [保持开源](https://thenewstack.io/new-research-shows-secure-usage-of-open-source-remains-problematic/)。

一些社区成员对 HashiCorp 在收购前制定的限制表示担忧，例如对 Terraform 在生产环境中使用方式的限制。其他人则对整体举措及其对该平台未来的潜在影响提出了质疑，该平台作为跨云开发平台具有很高的价值。

总体而言，HashiCorp 社区对 [将 Terraform 重新变为开源](https://thenewstack.io/is-community-backed-open-source-software-worth-the-risk/) 的看法是沮丧、失望和对开放式创新和竞争的重新渴望的混合体。

关于 IBM 收购计划的问题目前尚未在 Terraform 社区论坛上公开讨论。在这样的收购过程中，这种情况并不少见。

开发人员 Robert Hafter 在一个 OpenTofu 论坛上说：“Oracle 已正式宣布，他们内部运行 OpenTofu，并已将其 Cloud Manager 服务切换为使用它。我知道还有其他公司对此不太愿意公开，但仍然采取了行动。”因此，OpenTofu 运动似乎正在获得强劲的势头。

## 更多来自开发人员的观点

以下是使用 Terraform 和/或 OpenTofu 的开发人员的更多观点：

“Terraform 多年来一直是 IaC 的事实标准，但 HashiCorp 对代码库的投资令人非常失望，”开发人员 Troy Knapp 在 OpenTofu 论坛中写道。“重要问题被搁置，有效的 PR 多年来未经审查。越来越明显的是，他们的重点在于其云服务，而不是语言本身。一旦 Terraform 被分叉，OpenTofu 中的全职核心维护人员数量是 TF 中人员的 5 倍。长期被忽视的问题开始立即得到解决，路线图不再是黑匣子，而是由社区参与决定的。我主要担心的是，如果 Terraform 重新开源，那么对该语言的投资将回到现状。我希望 IBM 致力于在 [云原生计算基金会](https://cncf.io/?utm_content=inline+mention)中合并 OpenTofu 和 Terraform，并从 [AWS](https://aws.amazon.com/?utm_content=inline+mention)、[Azure](https://news.microsoft.com/?utm_content=inline+mention) 寻求进一步投资。

“如果 IBM 收购 HashiCorp，那么预期许可证将发生变化。但不同的人对不同的费用有不同的预期（或担忧）。有两个选择——恢复原状或采用 GPL（GNU 公共许可证）。前者感觉像是现状，后者不太可能，而且会产生一些有趣的情况。由于 Terraform 作为一个程序是独立的，所以乍一看不会产生太大影响，因为使用 GPL 软件不会用 GPL ‘感染’你，链接和代码重用会。但这意味着 OpenTofu 和 Terraform 由于许可证不兼容而保持分离。关于我自己：我正在开发一个专有的 Terraform 提供程序（插件）。我为一家大型美国上市公司工作，”开发人员 Konstantin 在 OpenTofu 论坛中写道。

“在许可证变更之初，我就知道 HashiCorp 将出售自身，如果你考虑 MongoDB 提起的有争议的诉讼，那么许可证变更是 MongoDB 投资者的建议或有很大关系，但他们不会复制与 Mongo 相同的成功，因为从我的开源经验来看，社区不会上当两次。简而言之，HashiCorp 现在没有发挥空间，OpenTofu 将继续前进并获胜，Terraform 没有基础来支持其以前的发展速度，”开发人员 Hao Wang 在 OpenTofu 论坛中写道。

“我的公司必须决定是否迁移到 OpenTofu。一些人希望在 OpenTofu 取得成功后，HashiCorp 会撤销其决定。作为从业者，我们一直在抑制采用新的 Terraform 版本，以确保我们在管理层对 OpenTofu 做出决定时能够迁移。对于个人项目，我已经完全迁移。迁移到 OpenTofu 的决定不会是公司范围的决定，而是团队/业务部门的决定，特别是由于我的团队不利用任何企业功能，”开发人员 David Gamba 在 OpenTofu 论坛中提出。

## 分析师的观点

“IBM 收购 HashiCorp 可能会引起开发人员的担忧，特别是在开源社区中，他们担心 HashiCorp 服务的公正性和独立性，”Futurum Group 的实践负责人 [Paul Nashawaty](https://futurumgroup.com/analyst/paul-nashawaty/) 说，“虽然此举符合 IBM 对多云解决方案的关注，并增强了该领域的信誉，但存在感知偏见破坏 HashiCorp 吸引力的风险。然而，此次收购也为 IBM 提供了机会，可以利用 HashiCorp 的多云功能来加强其在市场中的地位，并为企业客户提供价值。”

Nashawaty 说，此次收购的影响需要在 IBM、[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 产品组合（[IBM 于 2019 年收购 Red Hat](https://thenewstack.io/turning-blue-ibm-to-acquire-red-hat/)）中得到妥善管理。

“一方面，如果 IBM 保持 HashiCorp 独立且开源，我可以看到产品组合之间的协作是互补的，并允许客户选择 [适合其需求的技术堆栈](https://thenewstack.io/why-cloud-databases-need-to-be-in-your-tech-stack/)，类似于他们今天的需求。另一方面，强制或合并技术堆栈将限制客户的选择，”Nashawaty 告诉 The New Stack。

Constellation Research 分析师 [Dion Hinchcliffe](https://www.constellationr.com/users/dion-hinchcliffe) 告诉 The New Stack，“HashiCorp 是 IBM 首席执行官 Arvind Krishna 在过去一年中进行的一系列收购中的最新一笔，目的是完善他们的云服务，使其更具竞争力，与超大规模厂商竞争。尽管是该领域最酷的公司之一，但 HashiCorp 有时在打入企业销售市场方面遇到了困难。虽然 IBM 无疑会将 HashiCorp 强大的开发者‘街头信誉’作为其自身产品的一个证明点，但 HashiCorp 是否能够在稳健的多云和跨云支持持续变得越来越重要的时刻保持其作为云基础设施软件提供商的公正形象还有待观察。”

Constellation 分析师同事 [ Holger Mueller ](https://www.constellationr.com/users/holger-mueller) 的看法更加直截了当：“HashiCorp 对 IBM 来说毫无意义。服务模式依赖于独立性，而现在它们可能看起来有偏见。而且围绕 [DevOps](https://thenewstack.io/DevOps/) 的服务收入将枯竭。从 IBM 信誉的角度来看，HashiCorp 的多云方面是有意义的。”他告诉 The New Stack。

## 竞争对手的观点

[Sachin Aggarwal](https://silverjacket.mxspruce.com/637bfe22416d7996889c6fe8/l/KDq10LTXaxWAfnSCi?rn=&re=ISbvNmLslWYtdGQ6lGa3dmbpRXakVmI&sc=false)，[appCD](https://silverjacket.mxspruce.com/637bfe22416d7996889c6fe8/l/mvqspjQWISLludQ9X?rn=&re=ISbvNmLslWYtdGQ6lGa3dmbpRXakVmI&sc=false) 的首席执行官兼联合创始人，该公司是代码生成基础设施的开发者，对这对于 [基础设施即代码](https://thenewstack.io/Infrastructure-as-code/) (IaC) 集成意味着什么有以下看法：“基础设施即代码 (IaC) 在推动云技术的广泛采用和扩展方面发挥了至关重要的作用。然而，尽管其意义重大，但 IaC 领域的创新进展缓慢，这一趋势可能会持续到 HashiCorp 与 IBM 集成的影响变得更加明朗为止。在此之前，手动流程的持续存在和 IaC 实施中出现错误的可能性将继续给工程团队带来重大的认知负担。

HashiCorp 在大规模提供真正卓越的 [开发者体验和稳健治理](https://thenewstack.io/dont-sacrifice-developer-experience-for-platform-governance/) 方面面临的历史挑战，对 IBM 在其客户群中寻求将 HashiCorp 的产品货币化和扩展提出了重大的考虑因素。

更多内容即将推出。

