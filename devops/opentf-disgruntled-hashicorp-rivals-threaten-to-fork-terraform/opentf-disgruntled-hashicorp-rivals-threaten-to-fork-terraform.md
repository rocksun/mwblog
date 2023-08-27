# OpenTF：不满的 HashiCorp 竞争对手威胁要分叉 Terraform

有趣的是，该团体并未呼吁立即分叉，只是希望"HashiCorp 为开源社区做正确的事情"。

翻译自 [OpenTF: Disgruntled HashiCorp Rivals Threaten to Fork Terraform](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/) 。

![](https://cdn.thenewstack.io/media/2023/08/cba92fc0-opentf.png)

[HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention)，作为基础设施软件提供商，决定[放弃](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)其广受欢迎的基础设施即代码（IaC）工具 Terraform 的开源许可证。在近九年来采用 [Mozilla Public License（MPL）v2.0](https://www.mozilla.org/en-US/MPL/2.0/) 后， Terraform 已转换为非开源许可证 [Business Source License（BSL）v1.1](https://www.hashicorp.com/bsl) 。

因此，一些依赖 Terraform 的服务提供商启动了 [OpenTF 计划](https://spacelift.io/blog/announcing-opentf)，其中包括 [Gruntwork](https://gruntwork.io/)、[Spacelift](https://spacelift.io/?utm_content=inline-mention)、[env0](https://www.env0.com/) 和 [Scalr](https://www.scalr.com/)。

Gruntwork 的 [Yevgeniy Brikman](https://medium.com/@brikis98?source=post_page-----ab0b9ba65bca--------------------------------) 在[一篇博文](https://blog.gruntwork.io/the-future-of-terraform-must-be-open-ab0b9ba65bca)中写道：“我们认为 BSL 许可证是对 Terraform 的毒丸，威胁着整个社区和生态系统。”

他们的目标是什么呢？“[确保 Terraform 始终保持真正的开源](https://opentf.org/)。”有趣的是，该团体并未呼吁立即分叉。相反，他们要求“HashiCorp 为社区做正确的事情：不要继续采用 BSL 许可证变更，将 Terraform 改回真正的开源许可证，并承诺将来始终保持这种方式。”

对于开源爱好者来说，BSL 是不可接受的。

因此，下一步将是分叉传统的 MPL 许可证下的 Terraform。一个基金会，而不是公司，将维护这个分叉版本。

这个基金会名为 OpenTF，将在一个众所周知且广泛接受的许可证下维护代码，这可以让公司信任，不会突然在未来改变，并且不受单一供应商的意愿支配。据推测，这将是 MPLv2 许可证。

基金会还建议，这将是一个社区基金会，而不是商业基金会。在其中，拉取请求将定期、公正地根据其价值进行审查和接受。

## HashiCorp 的竞争对手联合起来

这很重要，因为与 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 的首席执行官兼创始人 [Joe Duffy](https://www.linkedin.com/in/joejduffy/) 所称，"我们多次尝试向 Terraform 提供程序贡献上游修复，但 [HashiCorp 从未接受它们。因此，我们不得不维护分叉版本](https://news.ycombinator.com/item?id=37082324)。"

其他人也同意 Duffy 的看法。在关于 OpenTF 的 LinkedIn 讨论中，IaC 公司 Spacelift 的首席产品官 Marcin Wyszynski 写道："我们认为我们的贡献被接受的机会为零。这非常令人沮丧，因为能够为 Terraform 做出贡献本来会让我们的生活轻松很多。"

在保持与旧代码的向后兼容性的同时，新的计划将采用"对程序员友好的项目结构，鼓励在其上构建，从而实现新的充满活力的工具和集成生态系统。"

与此同时，该团体并不打算设立自己的基金会。根据其 FAQ，"与创立新基金会相比，我们强烈倾向于加入现有的声誉良好的基金会。"

更好的是，正如 Wyszynski 在 Ycombinator 的对话中所说，"尽管我坚信 OpenTF 分支可以为社区带来难以置信的可能性（我可以在这方面继续谈论），但这相当于内战。这不符合社区的利益，我们唯一的兴趣在于继续建设的社区的持续强大。基于我对 Hashi 旗下所建立的东西的巨大尊重，[我宁愿看到一个观念的转变](https://news.ycombinator.com/item?id=37135452)。"

与此同时，作为 DevOps 即服务公司和 OpenTF 的重要支持者，Gruntwork 向其客户保证，他们可以继续使用 Terraform 1.5.5（或更旧版本）与所有 Gruntwork 产品，而无需进行任何更改，因为这些版本仍然基于 MPL 许可证。

展望未来，Gruntwork 将使其产品与 Terraform 的开源版本保持一致，无论是来自 HashiCorp 的恢复版本还是 OpenTF 分支。

此外，已经有一百多家公司和个人签署了支持 OpenTF 的承诺，一旦实现，他们将提供支持。

有兴趣加入的人可以在 [OpenTF 宣言的 GitHub 存储库](https://github.com/opentffoundation/manifesto)上提交拉取请求。正如 Spacelift 的开发者倡导者 Craig Dunn 所写，"[您可以承诺资源、时间和服务来支持这一计划](https://spacelift.io/blog/announcing-opentf)。如果您想支持 OpenTF，请在 GitHub 上为存储库加星，将网站分享到社交媒体上，帮助我们传播这个消息。"