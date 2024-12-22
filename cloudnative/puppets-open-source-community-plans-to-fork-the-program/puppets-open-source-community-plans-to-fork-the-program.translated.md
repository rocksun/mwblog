# Puppet 开源社区计划为该程序创建分支

![Featued image for: Puppet’s Open Source Community Plans to Fork the Program](https://cdn.thenewstack.io/media/2024/12/db89c722-puppet-fork-2-1024x576.jpg)

围绕流行的基础设施即代码 (IaC) 工具 [Puppet](https://puppet.com/?utm_content=inline+mention) 的社区正在为该程序创建分支。

或者，正如社区活动家所说，Perforce 为 Puppet 创建了分支，而社区只是在恢复开源项目。

当在 2005 年创建 Puppet，一个服务器配置和管理工具时，没有人知道什么是 [DevOps](https://roadmap.sh/devops)，因为这个术语还没有被定义。[基础设施即代码](https://thenewstack.io/infrastructure-as-code/) 还要几年时间才会出现。Puppet 将在这两者中成为领导者。然而，[Puppet错过了Kubernetes](https://thenewstack.io/puppet-missed-the-kubernetes-boat-then-perforce-came-along/)，而 [Perforce](https://www.perforce.com/) 在 2022 年收购了 Puppet。

从开源 Puppet 开发人员的角度来看，事情开始出错。现在，社区已经受够了，并且[它决定为 Puppet 创建分支](https://github.com/OpenPuppetProject/planning/discussions/11)。

根据 Puppet 程序员在 [GitHub Ideas 论坛帖子](https://github.com/OpenPuppetProject/planning/discussions/11) 中发布的信息，Puppet 开发人员并没有决定为代码创建分支。不，是 Perforce。

“Perforce 现在正在做的是获取我们协同使用、调试、编写、协作、查看并在数千台机器上部署的开源代码，并将其对付费客户的访问权限关闭，”Beaupré 写道。“因此，我们不是在为 Puppet 创建分支，Perforce 正在为 Puppet 创建分支，”

他指的是 Perforce 11 月 7 日的公告，该公告称：“在 2025 年初，[Puppet 将开始将其团队开发的任何新的二进制文件和软件包交付到一个私有的、强化和受控的位置。](https://www.puppet.com/blog/open-source-puppet-updates-2025) 社区贡献者将根据最终用户许可协议 (EULA) 的条款免费访问此私有存储库以进行开发使用。开源版本的 Puppet 不会有任何许可证更改。”

社区发现这是不可接受的。“他们声称不会更改软件的许可证，但这实际上是一个无关紧要的细节，因为实际上，Perforce 生成的 Puppet 源代码将不再公开可用。”

## OpenPuppetProject 正式上线
如果真的发生这种情况，Puppet 分支将是最近一系列事件中的最新一个，在这些事件中，开源社区在创建该项目的公司宣布计划实施更严格的许可后，为一个流行的项目创建了分支。2023 年 8 月，[HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) 的 [Terraform 的分支被创建并最终命名为 OpenTofu](https://thenewstack.io/will-opentofu-dethrone-terraform-in-iac/)。3 月份，[创建了 Valkey 分支](https://thenewstack.io/valkey-whats-new-and-whats-next/) 以应对 [Redis](https://redis.com/?utm_content=inline+mention) 的许可证更改。

需要说明的是，Puppet 长期以来一直存在两种形式：一种是在 [Apache 许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 下的开源版本，以及基于开源核心构建的商业版本 Puppet Enterprise。

此外，社区不喜欢的是，Perforce 将要求社区贡献者同意最终用户许可协议才能进行开发使用。

“我在这里是因为我管理着 Tor 项目的 100 台机器，”Beaupré 在他的 GitHub 论坛帖子中写道。“Debian 项目、Riseup、Koumbit 和许多其他组织都面临同样的困境。我们不能就这样离开这艘 Puppet 之船。”

一些用户还抱怨 Perforce 对他们的担忧没有给予回应。正如一位在 Mastodon 上使用 GeneBean 句柄的社区成员在 12 月 16 日所写的那样，“今天举行了一次‘市政厅’会议，Perforce 在会议上明确表示，他们将声称自己希望与社区合作，但实际上并没有这样做。” 因此，尽管“[#Puppet](https://fosstodon.org/tags/Puppet) 社区中的我们没有人想要走分支路线，[我们的行动是被 Perforce 的行为所迫的。](https://fosstodon.org/@genebean/113664863697232378)”

到目前为止，社区活动家已经在 GitHub 上创建了一个 [OpenPuppetProject 存储库](https://github.com/OpenPuppetProject)，但它尚未包含 Puppet 源代码的分支。组织讨论正在进行中。根据项目存储库的 README 文件，一家公共利益公司 [Overlook InfraTech](https://overlookinfratech.com/) 正在“赞助和管理”OpenPuppetProject。
尚未为该分支选择名称。一些[建议](https://github.com/OpenPuppetProject/planning/discussions/9)包括Manikin、Dolly，以及我最喜欢的Muppet。

## Perforce的回应

针对社区计划为Puppet创建分支的计划，Perforce的一位代表通过电子邮件向The New Stack表示：

“在过去的几年里，我们看到基础设施自动化领域发生了各种变化，这要求Perforce重新思考我们作为组织应该如何为开源Puppet做出贡献。主要因素包括对合规性的需求增加、企业客户的下游优先事项以及并行直接管理开源Puppet的税负增加。

“鉴于这些因素，我们致力于保持相同的许可证，但将开始将我们团队开发的新二进制文件和软件包交付到一个强化型的面向企业的存储库中。以前，我们也向所有开源用户提供这些资源。为发行版建立一个强化型存储库使我们能够提供一致的企业级安全性和支持，这是我们许多运行Puppet的大型公司一直在要求的。

“这个新的存储库和后续的发行版将在最终用户许可协议 (EULA) 的条款下提供。它允许开发者免费访问我们强化的Puppet发行版（最多25个节点），旨在支持更广泛的生态系统持续使用。上游存储库将保留在原处，并保留Apache 2.0许可证，社区将保留该代码库的共同创作权，由Perforce资助。

“Perforce Puppet将继续寻找并推动与社区的合作和持续沟通，包括市政厅会议，因为我们认识到多年来许多人的重要贡献。我们认为我们在企业方面的投资将创造更长期的需求，并增强对Puppet生态系统的信心，社区将从中受益。”

如果你觉得这只是Perforce最近政策变化的另一种说法，那么你是对的。它确实是，只是对其立场的另一种说法。无论你想把Puppet分支归功于谁——或者责备谁——它都会到来。

Perforce的声明也明确表示，在尊重Puppet的开源根源与理论上使Puppet对商业客户更具吸引力之间做出选择时，Perforce将利润放在首位。该公司的假设是否会使其更有利可图还有待观察。

Perforce收购Puppet时，当时坐在Puppet董事会但不再担任管理职务的Kaines曾在推特上写道，“[坦白说，我不太喜欢收购。](https://x.com/lkanies/status/1513552978371772419)”尽管如此，他还补充道，“但这对Puppet及其员工来说是正确的结果。”

Kaines尚未就这些最新进展发表公开评论，并且尚未回复The New Stack的评论请求。

[YOUTUBE.COM/THENEWSTACK 科技发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)