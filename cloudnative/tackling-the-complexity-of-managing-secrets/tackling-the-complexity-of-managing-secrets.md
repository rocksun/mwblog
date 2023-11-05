<!--
# 解决密钥管理的复杂性
https://cdn.thenewstack.io/media/2023/11/74938b60-secrets12-1024x683.jpg
-->

了解如何在应用程序和基础设施项目中安全地管理你的密钥。

译自 [Tackling the Complexity of Managing Secrets](https://thenewstack.io/tackling-the-complexity-of-managing-secrets/) 。

多年来，通过与数百名客户的交谈，我们了解到随着公司规模的扩大和复杂性的增加，许多共同的痛点。

最突出的主题之一是配置散乱带来的压力。我们的用户经常分享有数百行配置文件的故事，我们也深知将Pulumi配置复制粘贴到其他数据源中的繁重负担。通过这种手动复制方式管理长期存在的静态密钥，不仅增加了维护工作量，也很容易导致配置偏差，并可能带来安全和运营风险。

[Pulumi 基础设施即代码](https://www.pulumi.com/product/)天生就具有高度可配置性，可以轻松处理像这些环境特定的差异，特别是当只涉及到少数应用程序和环境时。但是，随着组织的增长以及团队、应用程序和部署环境的数量增加，配置数据的数量和管理所有这些系统所需的时间会迅速变得不可控。

## Pulumi ESC 介绍

[Pulumi ESC](https://www.pulumi.com/product/esc/) 为团队提供了一种解决方案，可以从许多来源[汇总密钥和配置](https://thenewstack.io/the-challenges-of-secrets-management-from-code-to-cloud/)，管理称为“环境”的分层配置和密钥集合，并在不同的基础设施和应用服务中使用这些配置和密钥。

Pulumi ESC 与 Pulumi 基础设施即代码紧密协作，以简化配置管理，但也可以独立于 Pulumi 基础设施即代码，作为任何应用程序或基础设施项目的环境、密钥和配置管理解决方案。


![](https://cdn.thenewstack.io/media/2023/11/ba9e6b57-image1.jpg)
Pulumi ESC:我们的设计原则更近一步

让我们深入探讨塑造Pulumi ESC的基本设计原则:

- **分层和可组合**: [环境包含一组密钥和配置](https://thenewstack.io/why-securing-secrets-in-cloud-and-container-environments-is-important-and-how-to-do-it/)，但也可以导入一个或多个其他环境。值可以被覆盖、从其他值中插值和嵌套。这促进了灵活的组合和重用，并避免了复制粘贴。
- **通用密钥集成**: 支持动态配置提供程序，允许 Pulumi ESC 与存储在任何其他提供程序中的密钥集成。组织通常使用 AWS Secrets Manager、Vault、Azure OIDC 和/或 1Password 等，以及许多其他密钥和配置的权威数据源。Pulumi ESC 使用这些工具来改进密钥和配置管理。
- **可审计**: 要查看环境的值，必须“打开”它们，此操作将记录在审计日志中，包括对层次环境贡献的每个值的来源的完整记录。
- **从任何地方使用**: esc CLI 和 Pulumi ESC Rest API 使环境可以从任何应用程序、基础设施提供程序或自动化系统进行访问。在启动时，与 Pulumi 基础设施即代码、本地环境和 .env 文件、GitHub Actions等之间提供了集成。
- **认证和基于角色的访问控制**: Pulumi ESC 代理访问存储在其他系统中的密钥和配置的访问，因此身份验证和细粒度的基于角色的访问控制对于确保贵组织全面访问控制至关重要。Pulumi ESC 使用与 Pulumi 云身份、基于角色的访问控制、团队、SAML/SCIM 和范围访问令牌相同的方式来管理对环境和堆栈的访问。
- **配置即代码**: 环境被定义为YAML文档，可以描述如何投影和组合密钥和配置，集成动态配置提供程序，并计算新配置。
- **完全托管的开源核心**: Pulumi ESC 提供托管云服务 Pulumi Cloud(近期提供 Pulumi Cloud Self-hosted)，以及开源项目 pulumi/esc，其中开发了环境和 esc CLI 的评估引擎。

利用这些功能，Pulumi ESC 为[现代云应用程序](https://thenewstack.io/for-cloud-native-application-security-starts-with-identity-management/)和基础设施提供了独特的配置管理解决方案。Pulumi ESC 可以显着减少管理密钥和配置的复杂性，提供一个集中式解决方案来简化跨多个环境的工作流程。这不仅通过减轻重复密钥和频繁复制粘贴操作的风险来增强整体安全性，还可以显着改善审计性。

通过 Pulumi ESC，得益于详细的审计日志和分层环境，透明度和责任感首当其冲。这可确保组织可以轻松跟踪和了解每个配置的起源及后续修改。

您可以通过 Pulumi 云[控制台](https://app.pulumi.com/)、下载新的 esc CLI 或使用 Pulumi CLI 中的新的 pulumi env 子命令来试用 Pulumi ESC。在预览期间，Pulumi ESC 可供所有 Pulumi 云用户免费使用。

您可以在以下网址了解有关 Pulumi ESC 的更多信息，并立即开始使用:

- [入门](https://www.pulumi.com/docs/pulumi-cloud/esc/get-started)
- [文档](https://www.pulumi.com/docs/pulumi-cloud/esc)
- [开源](https://github.com/pulumi/esc)
- [社区 Slack](https://slack.pulumi.com/)

