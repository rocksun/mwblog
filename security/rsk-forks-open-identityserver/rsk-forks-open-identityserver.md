<!--
title: IdentityServer4 走向终结，接下来该怎么办？
cover: https://cdn.thenewstack.io/media/2026/06/3a12a894-ghariza-mahavira-scaled.jpg
summary: 由于 IdentityServer4 被商业化并停止支持，Rock Solid Knowledge 通过分叉项目推出了 Open.IdentityServer。该开源版本旨在提供长期免费、受支持的身份认证基础设施，避免开发者陷入商业锁定，并确保项目的持续维护与安全性。
-->

由于 IdentityServer4 被商业化并停止支持，Rock Solid Knowledge 通过分叉项目推出了 Open.IdentityServer。该开源版本旨在提供长期免费、受支持的身份认证基础设施，避免开发者陷入商业锁定，并确保项目的持续维护与安全性。

> 译自：[IdentityServer4 is dead. Here's what comes next.](https://thenewstack.io/rsk-forks-open-identityserver/)
> 
> 作者：Adrian Bridgwater

[开发者们对](https://www.reddit.com/r/dotnet/comments/1isquvd/identityserver4_wiped_from_github_by_duende_team/)身份与访问控制软件公司 [Duende](https://duendesoftware.com/) 在 2022 年 12 月将其开源产品 IdentityServer 商业化，并删除其 GitHub 上的配套文档的行为感到不满。

位于英国布里斯托尔的软件开发公司 [Rock Solid Knowledge](https://www.identityserver.com/) (RSK) 是 IdentityServer 社区的长期贡献者，目前正致力于确保开源身份认证基础设施平台服务能够继续存在。

RSK 决定分叉该项目，并维护一个与原始项目具有相同（且现已扩展）[身份认证技术](https://thenewstack.io/how-do-authentication-and-authorization-differ/)集的开源身份安全产品；新的 [Open.IdentityServer](https://www.identityserver.com/products/openidentityserver) 平台已于周二发布。

## 开源意味着优先考虑采用，而非优先考虑变现

RSK 的创始人 [Andrew Clymer](https://www.linkedin.com/in/andy-clymer/) 告诉 The New Stack，“免费软件并不意味着被放弃的软件”，IdentityServer4 留下了一个庞大的社区，这些社区理应拥有未来。

“Open.IdentityServer 为那些被遗弃的开发者提供了一条现代化的、受支持的路径，而无需他们在第一天就做出商业决策。当采用优先于变现时，[开源才能成功](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/)，”Clymer 说。“Open.IdentityServer 展示了你可以在拥有专业维护、永久免费平台的同时，围绕商业扩展和服务构建可持续的业务。我们认为这对每个人来说都是一种更健康的模式。”

RSK 本月发布的一份宣言指出，Open.IdentityServer 将保持免费和开源。宣言称，商业产品将保持可选状态，并将“资助免费的核心”，但开源社区在项目方向上“将始终拥有发言权”。

> “免费软件并不意味着被放弃的软件。Open.IdentityServer 为那些被遗弃的开发者提供了一条现代化的、受支持的路径，而无需他们在第一天就做出商业决策。当采用优先于变现时，开源才能成功。” ——Andrew Clymer，Rock Solid Knowledge。

该平台基于 Apache 2.0 许可的 IdentityServer4 代码库，为 .NET 应用程序提供了 OpenID Connect 和 OAuth 2.0 框架，支持基于令牌的身份认证、单点登录和 API 访问控制。首个版本 Open.IdentityServer v1.0.0 已于 6 月 1 日发布。

## 为什么 IdentityServer4 被废弃了？

GitHub 上的 [DuendeArchive 页面](https://github.com/DuendeArchive/IdentityServer4) 指出，IdentityServer4 包含“多个已知的安全漏洞和错误”，且文档陈旧。

Duende Software 客户成功主管 [Maarten Balliauw](https://www.linkedin.com/in/maartenballiauw/) 在公司官网上[发表博客](https://duendesoftware.com/blog/20250306-identityserver4-public-again)确认，当 .NET Core 3.1 达到其支持终止日期时，IdentityServer4 便停止了支持，正如 2022 年 12 月所述。

“IdentityServer4 包含几个已知的安全漏洞和错误，同时提供过时的文档和信息，”Balliauw 在去年 3 月发布的一篇文章中写道。

据 Balliauw 称，该存储库多年来一直显示关于这些问题的警告，以及与其 NuGet 包（包含用于在 .NET 应用程序中共享和重用代码的已编译代码和库的 zip 文件）相关的类似标志。然而，Duende 注意到“源代码仍在被克隆”，这意味着这些包仍被开发者使用并投入到生产中。

[Duende IdentityServer Community Edition](https://duendesoftware.com/products/communityedition) 仍然可用，其功能与 Enterprise Edition 相同，供个人、年度预估总收入低于 100 万美元的非营利性公司以及年度预算低于 100 万美元的非营利组织使用。

尽管这看起来令人钦佩，但 RSK 的 Clymer 并不买账。

“这种方法只适用于少数组织和早期初创公司，”他说。“当你的初创业务开始腾飞时，你不想被账单打击，也不想面临向另一个平台进行昂贵迁移的困境。企业需要确定性，而不是大幅度的年度价格上涨。Open.IdentityServer 提供了这种‘永久免费’的承诺；这是我们在[宣言中做出的 pledge](https://www.identityserver.com/products/openidentityserver/manifesto)；这不是一项短期计划，我们在这里是为了投资该平台，保护它并发展它。”

> “只有当开发者团队准备好长期拥有它时，分叉才是可行的……而我们正是这样。”

## 回归开源根源

RSK 对开源纯粹性充满信心；该公司表示，Open.IdentityServer 的推出使 IdentityServer 的核心更接近其最初的开源根源。开源模式为组织提供了一个免费、生产就绪的核心，并辅以可选的商业产品、服务和企业支持。

如果此类情况再次发生，我们应该将这种[对废弃开源项目进行分叉](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/)的做法视为指导其他类似场景的典范吗？在面临专有锁定时，这种方法现在是维持关键开发者基础设施的可行长期战略吗？

“绝对是这样，事实确实如此，”Clymer 确认道。“只有当开发者团队准备好长期拥有它时，分叉才是可行的……而我们正是这样。Open.IdentityServer 不是一个副业项目；它是我们业务的基础，这激励我们保持其安全性、现代化并进行积极维护。”

## 迁移的挫折，还是基础肯定的庆典？

但 Open.IdentityServer 是全新的，因此团队自然对其易用性和平台纯粹性持乐观态度。目前被锁定在 Duende 商业核心许可证中或仍在运行不受支持的 IdentityServer4 的团队可能认为，将现有的 IdentityServer 部署迁移到 Open.IdentityServer 并非易事，主要是因为天下没有免费的午餐。

“我们已经全面且详尽地考虑了这一点，”Clymer 向我们保证。“这非常简单，我们的团队制作了说明视频，展示了软件工程师如何能在不到 10 分钟内完成从 Duende 的迁移。Open.IdentityServer 的模式与 Duende 兼容，因此不需要进行数据库迁移；只需更改 NuGet 包，你就基本完成了。”

Clymer 断言，这些机制使得“非常容易评估”该平台是否适合任何给定的部署。对于新构建的项目，有一个模板可以让开发者在不到 30 分钟内完成启动和运行，并配有一个用于管理配置的 UI。

就开源模式血统而言，RSK 也是 IdentityServer、[OpenIddict](https://openiddict.com/) 和 [Umbraco](https://umbraco.com/flexible-cms/?gad_source=1&gad_campaignid=23799046955&gbraid=0AAAAADL94wSz4HntPz3WxgyLybTIgmmoP&gclid=Cj0KCQjwr4jSBhCSARIsAOX1E-J8ngbjabJcwfWyA6yrqPwe_rUxwT7b6OEZHhlSa8AE_BduxcvIc48aAmDKEALw_wcB) CMS 等生态系统的长期贡献者。

Open.IdentityServer [可在 GitHub 上获得](https://github.com/RockSolidKnowledge/Open.IdentityServer)，Rock Solid Knowledge 在那里维护着公共存储库和文档，并欢迎广大社区的贡献。