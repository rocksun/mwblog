
<!--
title: GraphQL的新超能力：破坏性更改检查
cover: https://cdn.thenewstack.io/media/2024/05/23c277b8-wonder-woman-533663_1280.jpg
-->

了解 GraphQL 的变革力量及其开源和商业工具和库的生态系统。

> 译自 [GraphQL's New Superpower: Breaking Change Checks](https://thenewstack.io/graphqls-new-superpower-breaking-change-checks/)，作者 Eric Murphy。

作为 API 解决方案架构师，从 [REST 到 GraphQL](https://thenewstack.io/graphql-vs-rest-you-really-dont-have-to-choose/) 的演变已成为我设计和 [大规模管理 API](https://thenewstack.io/API-management/) 的方法中的关键转变。REST 及其 [OpenAPI 规范](https://thenewstack.io/openapi-should-be-a-key-part-of-any-organizational-development-strategy/) 长期以来一直主导着这一领域。然而，它提出了许多挑战，尤其是在版本控制和将实际的 API 消费者使用情况与 API 规范保持一致方面。

厌倦了 REST 和 OpenAPI，我与 GraphQL 的旅程始于寻找 API 管理中的敏捷性和精确性。这一探索让我发现了 GraphQL 的变革力量及其开源和商业工具和库的生态系统。

## GraphQL 联合会开启的转型

[GraphQL 查询语言](https://graphql.org/) 多年来已变得非常成熟，它被引入企业 API 管理标志着效率和可扩展性的新时代。GraphQL 联合会彻底改变了我们在微服务架构中处理 API 的方式，使 API 架构师能够构建统一的 [GraphQL 超级图 API](https://www.apollographql.com/supergraph/)。这在企业环境中至关重要，在该环境中，高效管理众多 API 对运营成功至关重要。我曾与拥有 100 多个 GraphQL 微服务并将其合并到单个超级图 API 中的组织合作！

## 破坏性变更检查：改变游戏规则

GraphQL 的“破坏性变更检查”是现代 API 管理的改变游戏规则者。此功能允许 API 开发团队利用来自 GraphQL 客户端的 API 使用情况指标来评估对 GraphQL 架构的任何提议变更的影响。通过持续监控 GraphQL 查询，团队可以跟踪每种类型、字段和指令的使用情况，从而深入了解 API 如何被实时使用。然后，使用 GraphQL API 管理工具，开发人员可以立即获得反馈，了解他们提议的架构变更是否会破坏现有的 GraphQL 客户端。

![](https://cdn.thenewstack.io/media/2024/05/18ccbe1c-ericm.png)

这种使用破坏性变更检查进行的持续监控和测试超出了传统的 API 契约测试。破坏性变更检查确保了向后兼容性，这是维护 API 消费者信任和避免中断的关键因素。将这些检查集成到持续集成 (CI) 管道中可确保在潜在的破坏性变更影响生产环境之前检测并解决这些变更。这种主动方法能够实现快速且安全的 API 演进。

虽然破坏性变更检查很酷，但它在实践中是否有效？答案是肯定的，因为我已为我自己的 GraphQL API 实现了它，并与作为 API 解决方案架构师工作的客户/客户端一起实现了它。最困难的部分不是工具实施，而是每天在本地和 CI 管道中使用破坏性变更检查的流程变更。开发人员通常不习惯严格的 API 测试，而破坏性变更检查是一个新概念。但一旦团队掌握了它，破坏性变更检查就会迅速成为不可或缺的信心构建者，确保在下一个 GraphQL API 版本中继续支持现有的 API 消费者。

## 结论：为什么 GraphQL 代表了 API 的未来

GraphQL 在破坏性变更检查的支持下，使 API 开发团队在动态且快节奏的开发环境中管理 API 生命周期方面比 REST 更有优势。用于管理 GraphQL API 的工具（包括开源和商业工具）提供了全面的解决方案，可深入了解 API 使用情况和开发，从而保护 API 演进过程。

在我学习了 GraphQL 并自己实施了 GraphQL API 管理工具后，我发现很难回到 REST 和 OpenAPI 的旧方法。所以，帮自己一个忙，尝试一下 GraphQL，目标是采用破坏性变更检查等最新工具。它是 API 的未来。
