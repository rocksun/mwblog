# HashiCorp 将 Terraform 转向商业源代码许可证

和许多其他公司一样，HashiCorp 放弃了最初使其产品起步的开源方法，采用了源代码可获取的商业源代码许可证（BSL）。

翻译自 [HashiCorp Moves Terraform to a Business Source License](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) 。

![](https://cdn.thenewstack.io/media/2023/08/bd308ad2-terraforming-5268447_1280-e1691802429726-1024x751.jpg)

这似乎已经成为一个不太好笑的笑话了。像 [Confluent](https://www.confluent.io/?utm_content=inline-mention)、[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention)、Elastic 和 [Redis Labs](https://redis.com/?utm_content=inline-mention) 这样的公司从一个开源项目起步。他们取得了一定的成功，然后他们或他们的风险投资支持者决定他们的现金收入还不够，于是他们放弃了原来的开源许可证，采用了一种可以从他们的软件中提取更多现金的许可证。最新加入这一行列的公司是 [HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention)，他们将其 [Terraform](https://www.terraform.io/) 基础设施即代码工具和 Vagrant 虚拟机环境构建和管理工具，从开源的 [Mozilla Public License v2.0（MPL 2.0）](https://www.mozilla.org/en-US/MPL/2.0/)迁移到源代码可获取的 [Business Source License (BSL) v1.1](https://mariadb.com/bsl11/)。

## 为何转变？

为什么要这么做呢？HashiCorp 的联合创始人兼首席技术官 [Armon Dadgar](https://www.linkedin.com/in/armon-dadgar/) 解释说：“还有[其他一些供应商利用纯开源模式](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)，以及社区在开源项目上的工作，来实现自己的商业目标，而不提供实质性的贡献回馈。我们认为这不符合开源的精神。因此，我们认为商业开源模式需要发展，以便生态系统能够继续提供开放、免费的软件。”

[在 BSL 下](https://www.hashicorp.com/license-faq#what-is-the-bsl)，Dadger 补充道：“最终用户可以继续复制、修改和重新分发代码，用于非商业和商业用途，但在提供与 HashiCorp 相竞争的产品时除外。”

尽管有这个限制，BSL 在任何形式上都不是开源许可证。不过，正如 RedMonk 的联合创始人和行业分析师 [Stephen O'Grady](https://www.linkedin.com/in/sogrady/) 所指出的那样：“向非竞争许可证的趋势从行业角度来看是有问题的，但我至少欣赏 Hashi 已经明确新许可证不是开源。”

一遍又一遍地听到这个借口，真是令人厌烦。一家公司利用开源开发者的工作来创建他们的程序，然后责怪其他公司使用他们的开源代码（通常是超级云服务提供商）迫使他们放弃开源。

## 并未受到损害

HashiCorp 并不缺钱。在其 [2023 财年的最新年度报告中](https://ir.hashicorp.com/static-files/9475fc23-0944-474d-9e99-34f489ff83bd)，HashiCorp 报告了当前非普遍公认会计原则（GAAP）下的剩余绩效承诺金额为 3.946 亿美元，同比增长了 29%。在2023财年第一季度，该公司还增加了 32 个年度重复收入大于等于 10 万美元的客户。在 2023 年 8 月 11 日，HashiCorp 宣布许可证变更后，该公司的市值为 56.1 亿美元。

当然，一些公司正在使用 Terraform 和其他 HashiCorp 技术提供服务。这是开源的一部分。如果您提供此类服务，例如将 HashiCorp 工具作为托管服务提供或将 HashiCorp 产品嵌入商业解决方案中，HashiCorp 可以对其代码进行商业许可。

## 不开心

竞争对手们依赖 Terraform 来提供自己的产品，他们对这次转变并不满意。[Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 的 CEO 和创始人 [Joe Duffy](https://www.linkedin.com/in/joejduffy/) 将 HashiCorp 的[声明称为“不诚实”](https://news.ycombinator.com/item?id=37082324)。他说：“我们曾多次尝试向 Terraform 提供者上游提交修复补丁，但 HashiCorp 从未接受过。所以我们不得不维护分支。他们很久以前就失去了他们的 OSS（开源软件） 基因，而这次转变只是在他们的棺材上钉上了最后一颗钉子。”

[SUSE](https://www.suse.com/) 发行版架构师 [Richard Brown](https://www.linkedin.com/in/sysrich/?originalSubdomain=de) 带着些许嘲讽地发推说：“我想感谢 [@HashiCorp](https://twitter.com/HashiCorp) 的许可证变更。我从来不喜欢 Terraform，它总是让我们的 openSUSE 镜像构建变得复杂，但这次[许可证变更几乎肯定会阻止我们在我们的 GPL 许可的发行版中发布他们的任何东西](https://twitter.com/sysrich/status/1689882113011597313)，所以我终于可以放松了。”

“如果 HashiCorp 将他们的开源社区发展成一个多样化和广泛的社区，他们本来可以成为云的通用语言，” System Initiative 的联合创始人兼首席执行官 [Adam Jacob](https://www.linkedin.com/in/adamjacob/) 说。“但由于他们没有做到这一点，唯一的合理做法就是从剩下的内容中尽可能多地提取资金。”

