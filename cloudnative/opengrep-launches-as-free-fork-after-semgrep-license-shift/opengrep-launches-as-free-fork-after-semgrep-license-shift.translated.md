# Semgrep 许可变更后，Opengrep 作为免费分支启动

![Featued image for: Opengrep Launches as Free Fork After Semgrep License Shift](https://cdn.thenewstack.io/media/2025/02/9a2225f8-a-calvar-o5fccjrump0-unsplash-1024x683.jpg)

[Endor Labs](https://thenewstack.io/endor-labs-station-9s-top-10-open-source-security-risks/) 在 Semgrep 描述为长期信任的安全工具的“更新”后，将 [Semgrep](https://thenewstack.io/the-security-tooling-faceoff-open-source-security-vs-commercial/) 分叉为 [Opengrep](https://www.opengrep.dev/)。

Endor Labs 的 CEO 兼联合创始人 Varun Badhwar 告诉 The New Stack，创建 Opengrep 的治理结构是为了维持 Semgrep 不再提供的持续且无限的开源自由使用。

Badhwar 说：“我们试图实现的主要目标是使 Opengrep 成为一个更加中立的场所，确保没有任何一方可以从这样的事情中抽身。第二个目标是带来足够的资本投资，以弥补 Semgrep 因其变更而造成的任何差距。”

此外，Badhwar 表示，Opengrep 的开发人员正在提高性能，增加对 Windows 等平台的支持，启用多文件分析，并解决“Semgrep 故意创建或长期维护的许多差距，以推动用户使用其付费引擎。”

根据文档，Opengrep 基于三个核心原则构建：

- 通过不将基本元数据和新的扫描功能隐藏在登录后面，从而提供更好、更强大的扫描引擎。Opengrep 将向后兼容并支持常见的 [JSON](https://thenewstack.io/working-with-json-data-in-python/) 和 [SARIF](https://sarifweb.azurewebsites.net/) 输出，使您能够采用 Opengrep OSS 并将其集成到您的工作流程中；
- 改进的引擎意味着通过解锁以前仅限专业版的功能，可以实现更强大的社区规则。
- 长期保证未来的改进和功能不会被锁定到特定的供应商。您对 Opengrep 的贡献和 PR 会定期审查并根据优点接受，而不是取决于任何一家公司的商业利益。

对于开发人员，创建 Opengrep 是为了提供：

- 完全访问所有扫描功能，而没有功能限制。
- 与现有工作流程和 JSON/SARIF 输出的向后兼容性。
- 可在任何环境中使用的可移植安全规则。
- 社区驱动的功能开发。
- 通过基金会治理实现长期稳定性。

## 反弹趋势

此举反映了行业趋势，因为当使用条款更改为更具限制性时，流行的开源项目会被分叉。一个值得注意的例子包括 Linux 基金会将 HashiCorp 的 [Terraform](https://thenewstack.io/terraform-gets-ai-boost-in-new-cloud-management-platform/) 分叉为 [OpenTofu](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/)。开源项目 Opengrep 的启动是为了响应 Semgrep 描述为许可更新而非变更的行为。

但是，自 12 月以来，这些更新使得将 Semgrep 用于商业目的的限制略有增加。新的 Semgrep 社区版现在是竞争性软件即服务产品的一部分。

Endor Labs 长期以来一直支持开源计划，并承担着对开源代码应用安全措施的重要任务。Endor Labs 的平台除其他外，可用于审查 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 和其他存储库代码，这些代码通常包含大量漏洞。

[静态应用程序安全测试 (SAST)](https://thenewstack.io/why-you-still-need-dynamic-application-security-testing/) 强制执行代码编辑、提交和集成的代码标准和策略。[Aikido Security](https://www.aikido.dev/), Arnica, Amplify, Jit, Kodem, Legit Security, [Mobb](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), [Orca Security](https://thenewstack.io/orca-security-launches-first-k8s-testing-staging-environment/) 等公司支持 Opengrep 项目并为其做出贡献。像 Endor Labs 这样的公司将提供资源，例如允许其内部工程师兼职从事该项目。Badhwar 说，Endor Labs 还贡献了资金，聘请了两名全职工程师，并且正在“增加几名专门从事 Opengrep 的工程师”。
“我们希望世界各地的应用程序安全团队能够真正依赖这个重要的软件，因为我们的理论是，该引擎最终是一个 Opengrep 引擎。所以，这并不是什么高深的科学，但其价值在于组织和用户能够在这个引擎之上编写自己的规则，”Badhwar 说。“所以，我们真的希望这个引擎如果构建正确并正确扩展，就能成为一种商品……我们将给予人们自由和灵活性来做到这一点，并真正确保这个开放的 Opengrep 引擎的商品，如果你愿意这么称呼它的话，能够得到良好的构建和扩展，以满足全球成千上万人的需求。”

## 新的 Semgrep 世界

根据新的使用条款，Semgrep 用户只能通过其付费或商业产品访问作为社区贡献规则的一部分引入的新功能。从本质上讲，用户将不得不为这些功能付费。此外，其他功能已被转移到付费 SaaS 平台之后。Semgrep 淡化了 SAST 使用的新限制。

在一篇博客文章中，Semgrep 的创始人兼首席产品官 [Luke O’Malley](https://www.linkedin.com/in/dlukeomalley/) 写道：

> 我们正在对 Semgrep OSS 引擎和规则进行一些更新——现在统称为 Semgrep 社区版——以更好地区分它们以社区为中心的免费性质与我们的商业产品，并明确其他供应商不得将 Semgrep 社区版规则用作竞争性软件即服务产品的一部分。
>
> 从今天开始：
>
> - Semgrep 社区版：Semgrep OSS 现在更名为 Semgrep 社区版，反映了其作为免费的、以社区为中心的工具的角色。
> - 规则许可变更：Semgrep 维护的规则现在根据 Semgrep Rules License v.1.0 获得许可，因此它们仅适用于内部、非竞争性和非 SaaS 环境。
> - 输出清理：JSON 和 SARIF 输出中的某些 Semgrep 内部字段现在为我们登录的商业引擎保留。
> - 实验性功能：以前标记为实验性的功能现在是我们登录的商业引擎的一部分。

与此同时，Opengrep 的未来包括与“所有基金会和各种选择”的可能合作和捐赠，“当然都在考虑之中，”Badhwar 说。“我们对来自不同组织的兴趣感到非常高兴，”他说。“我们只是在寻找最佳的长期归宿，在那里它能够继续获得其应得的投资并提供基础。”

当被问及 Opengrep 是否可以作为沙箱项目捐赠给 [CNCF](https://cncf.io/?utm_content=inline+mention) 时，Badhwar 表示，尚未决定该项目是应该成为 Linux 基金会的项目，还是“独立的东西”。“计划是稳定它，在其基础上构建，让社区支持它，然后将其过渡到基金会，”Badhwar 说。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)