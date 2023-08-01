# Terraform Provider 与 IaC 的崛起

那些已经广泛使用基础设施即服务（Infrastructure-as-a-Service）来管理云资源的工程组织，现在正在寻求通过 Terraform 和其他基础设施即代码（Infrastructure as Code，简称 IaaC ）平台来管理内部部署。

翻译自 [Terraform Providers and the Rise of Infrastructure as a Service](https://thenewstack.io/terraform-providers-and-the-rise-of-infrastructure-as-a-service/) 。

![](https://cdn.thenewstack.io/media/2023/07/c2f45fa8-cloud-computing-g457678229_1280-1024x576.jpg)
*图片来自 Pixabay*

过去一年里，[Firefly](https://gofirefly.io/) 团队一直在研究和分析 Terraform Provider 的采用和使用情况，以便构建支持当今最受欢迎的技术和堆栈的工具。

通过审查数据并绘制不同的趋势，我们发现我们的生态系统正在经历一些引人注目的变化。在这篇文章中，我们想看一些关于 [Terraform Provider 采用](https://thenewstack.io/terraforms-best-practices-and-pitfalls/)情况的统计数据和指标，并根据这些数据推测当前和未来的技术趋势。

简单介绍一下为什么这很重要，在最近的 [2023 年 IaC 报告](http://gofirefly.io/state-of-iac)中发现，90% 的云用户正在使用基础设施即代码（IaC）。Terraform 是由 [HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention) 管理的开源项目，自从诞生以来，它成为了构建基础设施即代码的最流行工具之一，因此它的市场正在成为许多技术战略中不可或缺的一部分。这可以从 [Terraform Registry](https://registry.terraform.io/browse/providers) 中提供的 provider 数量不断增长来看，每年都有数百个（甚至数千个，如果算上那些较小的社区创建的 provider ）新 provider 被添加进来。

对于那些不熟悉的人来说，Terraform 是一款流行的开源工具，它使用户能够以声明式的方式定义和管理基础设施。 Terraform Provider 是插件，允许 Terraform 与各种云提供商、 API、服务和其他系统进行交互，这些系统不是 Terraform 的原生支持。

每个 provider 负责与目标系统的 API 通信，创建、更新和删除资源，并跟踪其状态。 Terraform Provider 由社区和 Provider 公司自己多次维护，并不断添加新的 provider 以支持更多的服务和平台。

## Terraform Provider 基准测试

虽然我们通常认为 DevOps 生态系统是为新兴公司和技术而设计的，但实际上，已经有十多年的实践经验了，这个说法已经不再适用。任何希望在云原生世界保持相关性的技术公司，现在都专注于提供在 DevOps 驱动的世界中所需的服务和工具。

即使是长期存在的技术公司和主导者也明白支持现代云原生堆栈的重要性，从 Splunk、Palo Alto、Dell、Cisco、Juniper 到 ZScaler 等主要行业参与者提供的 provider 数量不断增长，这一点可见一斑。

Terraform Provider 分为三个主要类别：

- 官方 Provider ：由 HashiCorp 团队创建和支持的 Provider 。
- 合作伙伴 Provider ：由官方 HashiCorp 技术合作伙伴创建和支持的 Provider 。
- 社区 Provider ：由社区贡献者创建和维护的 Provider 。（一个流行的例子是 Anton Babenko 的 [AWS Provider 存储库](https://github.com/antonbabenko/terraform-provider-aws)）。

看一下在不同类别中的增长情况，甚至是每个类别中的特定领域 - 无论是监控和可观测性，还是 DevOps 和 DevSecOps 工具，都可以告诉我们很多关于当前 DevOps 和云原生领域的情况。接下来我们将详细解释一些有趣的数据。

## Terraform Provider 采用情况的见解

让我们来看一下现代软件交付的热门领域 - DevOps、身份和 PaaS、CDN，甚至是开源和容器，这些都是被广泛采用来促进云操作的常见工具。

我们将探索 JFrog 的 Artifactory、Heroku（仍然是最受欢迎的 PaaS 解决方案之一）、CloudFlare、作为开源生态系统代表的 Kubectl ，以及已成为当前规模化企业的事实标准的 Okta 等工具。

这些数字令人震惊。从 2022 年 6 月到 2023 年 6 月，这些工具的增长快得惊人。

![](https://cdn.thenewstack.io/media/2023/07/81a85ab1-np1.png)

- [JFrog Artifactory Provider](https://registry.terraform.io/providers/jfrog/artifactory/latest/docs) 一年间增长近 800% ，从 90 万次下载增长到 1400 万次下载。
- [Okta Provider](https://registry.terraform.io/providers/okta/okta/latest/docs) 增长超过 350% ，从 400 万次下载增长到 1740 万次下载。
- [Heroku Provider](https://registry.terraform.io/providers/heroku/heroku/latest/docs) 增长近 500% ，从 120 万次下载增长到 650 万次下载。
- [CloudFlare Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs) 增长从 1600 万次下载激增到 4600 万次下载。
- 最后但并非最不重要的是，[Kubectl Provider](https://registry.terraform.io/providers/gavinbunney/kubectl/latest/docs) （由社区贡献和维护）增长了惊人的 400% ，从 650 万次下载增长到 3270 万次下载。

从这些数字中我们可以得出的结论是，现在在 SaaS 应用程序和平台的编码方面，已经超越了公共云的编码速度，公共云的增长也在不断提高，但增长速度要小得多。随着我们将云管理作为代码进行，工程团队从更大的灵活性、自动化、以及更好的安全性和成本控制、治理和策略管理中获得的好处表明，这些好处不仅局限于我们的 CloudOps 。

工程组织开始意识到，通过将所有内容都作为代码进行管理，可以为所有平台和关键任务应用相同的好处，并以统一的方式在一个地方管理它们，比如代码存储库或云[资产清单管理](https://gofirefly.io/)。随着成本考虑成为云原生工程的重要组成部分，这不仅仅是因为当前的环境，而是作为持续的业务驱动因素，有了统一的资源清单，就可以更高效地扩展云规模。

这意味着，有了代码和资源清单，可以对系统故障之外的系统异常，例如代码与云 SaaS 应用程序之间的漂移检测，应用统一的策略并在违规时发出警报。这不仅仅局限于单个 SaaS 平台、云或解决方案，现在可以在跨云、平台、操作系统和技术堆栈上实现，因为它与底层环境是无关的，可以通过第三方工具实现。

## 对于我们的意义

那些已经广泛使用 IaC 来管理云资源的工程组织，现在下载数百万次的 Terraform Provider ，以使其余的工具和服务能够跟上他们的云。高效的 DevOps 管理的关键在于第二部分 - 运维。如果你的工具和服务被以碎片化的方式管理，那么很难对所有情况有一个全面的把握，很难控制成本，并且很难应用当今所需的策略和安全控制。这给云操作增加了很多摩擦。

DevOps 已经让我们在自动化方面取得了很大进展，我们的 CI/CD 流水线已经使我们能够从代码到云端优化软件交付流程。我们的服务和工具应该能够应用相同的标准，在各种规模上运行和操作代码，现在可以通过编码资源实现这一点。

展望未来，我们可能只会看到这一趋势的增长，因为将所有东西都作为代码进行管理的需求将使我们走向自动化和 AI 成为堆栈的所有部分的标准，因为它们现在是可读的机器语言。这将使流程中的人们能够关注更高级的问题，而不仅仅是管理和维护不同的软件堆栈，并为我们的开发和运营释放下一阶段的增长。