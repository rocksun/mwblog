展望未来，当您运行 [IBM](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434371219;dc_trk_aid=627496700;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$%7BGDPR%7D;gdpr_consent=$%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1?utm_content=inline+mention) 的 Terraform 基础设施即代码 (IaC) 软件时，您将只有一种语言来编写配置：HashiCorp 配置语言 (HCL)。

周一，IBM 旗下的 HashiCorp 公司宣布将不再支持 Terraform 云开发套件 (CDK 或 CDKTF)。尽管现有代码仍将保存在 [GitHub 存档](https://github.com/hashicorp/terraform-cdk) 中，但 HashiCorp 将不再维护或更新该代码，使其几乎无法用于企业。

“不幸的是，Terraform CDK 未能在大规模应用中找到产品市场契合度。IBM 旗下的 HashiCorp 公司已选择将投资重点放在 Terraform 核心及其更广泛的生态系统上，”该网站上的一份说明写道。

IBM 建议，CDK 本身根据 [Mozilla 公共许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) (MPL) 授权，因此用户可以自由地分叉该软件。

然而，该公司鼓励用户使用 [HCL](https://github.com/hashicorp/hcl)，HCL 由 HashiCorp 开发，并根据 Mozilla 公共许可证 (MPL) 授权，最初是为该软件设计的。

## Terraform 坎坷的历史

Terraform 最初由 HashiCorp 于 2014 年发布，是一款允许管理员通过脚本和一组 Terraform 命令（如 `terraform init`、`terraform plan` 和 `terraform apply`）在云端或本地自动化部署 IT 基础设施的软件。输出以 [JSON](https://thenewstack.io/an-introduction-to-json/) 格式呈现。

随着时间的推移，Terraform [已成为](https://thenewstack.io/is-terraform-dead-revive-your-infrastructure-as-code-strategy/) 最受欢迎的自动化 IT 部署软件，尤其是在 [云原生社区](https://thenewstack.io/cloud-native/) 中。

2023 年，HashiCorp [将](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) Terraform 的许可证从开源切换到商业源代码许可证，这激发了用户基于该软件创建了一个名为 [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/) 的开源分支，该分支先被 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) 采纳，后来又被 [云原生计算基金会](https://thenewstack.io/opentofu-joins-cncf-new-home-for-open-source-iac-project/) [(CNCF)](https://cncf.io/?utm_content=inline+mention) 采纳。

2024 年，IBM [宣布](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) 收购 HashiCorp，并于今年早些时候完成了收购。

## Terraform CDK 迁移计划

尽管有人呼吁将 CDK 开源，但 IBM 仍鼓励现有用户采纳 HCL，如果他们尚未这样做的话。

该公司表示：“如果您不使用 AWS CDK，我们强烈建议您迁移到标准的 Terraform 和 HCL，以获得长期支持和生态系统对齐。”

在 CDK 下创建 .tf 文件的 Terraform 用户可以使用以下命令将其转换为 HCL：

```
cdktf synth --hcl
```

在 [亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) 基础设施上使用 CDTF 的用户也可以使用 [AWS 自己的 CDK](https://aws.amazon.com/cdk/)。

## IaC 的局限性

总的来说，基础设施即代码的用户群似乎正因 [IaC 的局限性](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/) 而 [感到不适](https://thenewstack.io/infrastructure-from-code-what-went-wrong/)。

因此，在过去几年中，出现了许多替代 Terraform 的方法，包括 [Adam Jacob 的 System Initiative](https://thenewstack.io/chef-creator-unveils-ai-platform-to-fix-flaws-with-infrastructure-automation/) 和 [Platform Engineering Labs 的 Formae](https://thenewstack.io/kubecon-a-terraform-killer-built-on-apples-pkl/)。

它们指出 HCL 有其局限性，特别是在高度可扩展的环境中。作为一种声明式配置语言，HCL 在提供高级编程构造方面受到限制，许多由此产生的变通方法导致了晦涩的代码。工具也同样有限。

CDKTF 给用户带来的优势是，它允许他们通过自己喜欢的编程语言而非 HCL 来详细说明部署指令。CDKTF 支持 [TypeScript](https://thenewstack.io/what-is-typescript/)、[Python](https://thenewstack.io/what-is-python/)、C# 和 [Go 编程语言](https://thenewstack.io/introduction-to-go-programming-language/)。

这也是 Terraform 的竞争对手 [Pulumi](https://www.pulumi.com?utm_content=inline+mention) 所 [采取](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/) 的方法，即能够在 [多种编程语言](https://thenewstack.io/pulumi-program-the-infrastructure-with-an-actual-programming-language/) 中的任何一种中配置基础设施。

然而，关于通用编程语言是否优于领域特定语言，也存在相当大的争议。批评者指出，Terraform 的用户是管理员，而不是程序员。

## 社区反应

尽管如此，IaC 社区的许多人 [对这一消息反应强烈](https://bsky.app/profile/rawkode.dev/post/3m7ojjj35uc26)。Kubernetes 专家 David Flanagan 指出，仅 TypeScript 的开发套件每周下载量就超过 140,000 次，其他语言社区也有类似的数据。

他认为，很明显，CDKTF 仍然被社区广泛使用。

“你不会因为一个项目没有人喜欢或者没有‘市场契合度’而杀死一个每月 [估计有] 百万用户的项目。你杀死它是因为它没有增加你的利润率，它没有销售企业许可证，”Flanagan 在一段短视频中说。

公平地说，IBM 在收购开源公司并保持开源许可证不变方面有着悠久的历史，[包括](https://thenewstack.io/red-hat-ibm-acquisition-clash-of-cultures-or-best-of-both-worlds/) 基于 Linux 的 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)、专注于 Cassandra 的 [Datastax](https://thenewstack.io/ibm-to-acquire-datastax-to-boost-watsonx-ai-development/)，以及最近基于 Kafka 的 [Confluent](https://thenewstack.io/ibms-confluent-acquisition-is-about-event-driven-ai/)。（然而，关于 IBM 是否会 [将 Terraform 许可证](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/) 恢复为开源，目前还没有消息。）

Flanagan 接着指出，人们可能正在使用 CDKTF，因为他们需要额外的编程能力。“它被称为基础设施即代码，而不是基础设施即 JSON，”他打趣道。

站点可靠性工程师 Liz Fong-Jones 提供了一个更为审慎的回应。

“更温和地说，HashiCorp 已经决定停止尝试通过语言原生 API 与 Pulumi 竞争；他们完全专注于 HCL 作为与 Terraform 合作的唯一方式，”Fong-Jones [在 BlueSky 上写道](https://bsky.app/profile/lizthegrey.com/post/3m7ojmtbtoc23)。

## 我们需要为 IaC 提供编程语言吗？

事实上，其他人认为这可能不是一个坏主意。

Platform Engineering Labs 的联合创始人兼首席执行官 Pavlo Baron 认为 IBM 的举动是合理的。

“IBM 历来擅长优化目标买家。这更像是一个迹象，表明周期右侧没有人想做全面的编程。CDK，包括 Pulumi 采取的方法，专为开发人员服务。开发人员通常不操作基础设施，”他在电子邮件中写道。

“然而，严肃的运维工作发生在周期的右侧。因此，CDK 错过了目标用户，反而服务了错误的用户。所以我理解并支持这一举动背后的逻辑。”