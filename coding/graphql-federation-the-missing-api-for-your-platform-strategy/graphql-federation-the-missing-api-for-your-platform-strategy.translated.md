# GraphQL 联合：平台策略中缺失的 API

![GraphQL 联合：平台策略中缺失的 API 的特色图片](https://cdn.thenewstack.io/media/2024/05/db06e876-platform-1024x558.jpg)

[平台工程](https://thenewstack.io/platform-engineering/) 已成为释放云原生架构中开发人员速度的关键学科。从使用 Terraform 和 Kubernetes 配置和编排基础设施到使用无头 CMS 提供的前端微文案，工程团队正在选择集中式平台来维护其架构的核心组件。这些工具不仅消除了冗余任务，还使产品工程团队能够更快地交付功能、以更少的工作量进行实验，并减少对基础设施的关注，更多地关注业务需求。

自动化基础设施配置和安全策略比以往任何时候都容易。在 ChatGPT 使“
[AI 功能](https://thenewstack.io/ai/)” 突然成为每个应用程序的必需品一年半后，现在出现了无数的“AI 基础设施即服务”公司。但是，云原生架构的关键要素：[API](https://thenewstack.io/api-management/) 呢？

虽然无数工具简化并自动化了
[现代云原生架构](https://thenewstack.io/what-is-the-modern-cloud-native-stack/) 的其他核心组件，但我们仍然依赖于单独的手写后端到前端 (BFF) 来向每个前端提供后端的所有功能。

除非 AI 可以使用 REST 自行编写
[后端到前端的蔓延](https://thenewstack.io/graphql-break-free-of-backend-for-frontend-sprawl/)（可以吗？），如果我们想要减少样板代码并在所有界面中更快地交付功能，我们将需要一个更好的解决方案。

**进入 GraphQL 联合**

对于正在尝试 GraphQL 的个人 API 开发人员来说，GraphQL 似乎是一种减少客户端过度获取和获取不足的新颖方式。但是，当大规模交付时，GraphQL 也为提高工程团队的开发人员速度提供了关键要素。GraphQL 减少了前端和后端之间的摩擦。在大规模交付时，
[GraphQL 联合](https://www.apollographql.com/docs/federation/) 使 API 平台团队能够将任意数量的 API 公开为一个自服务且自文档化的图形，称为“超图”。此超图抽象了 API 复杂性，并将前端与后端解耦，使两个团队都能更快地工作。

它的工作原理如下：

* 后端开发人员将各个 GraphQL API 贡献给超图，该超图将类型及其关系定义为模式。
* 一个称为 [将这些子图模式组合成一个统一模式，可以自动或手动完成。](https://www.apollographql.com/docs/federation/federated-types/composition/) **组合**
* 客户端团队有权从超图中获取所需的所有数据，使用单个端点 - 无论数据存储在哪里。

GraphQL 联合通过以下方式支持更好的平台策略：

* **减少瓶颈以安全地交付更改**：由于 GraphQL [不需要版本](https://www.apollographql.com/blog/why-use-graphql/)，因此团队可以在没有一系列消极攻击性电子邮件或无休止的会议的情况下推出更多功能，以防止重大更改。
* **减少使用 API 的认知负荷**：对于客户端团队，GraphQL 提供了一种声明式查询语言，使客户端团队能够获取所需的所有数据。只需使用 [内省](https://graphql.org/learn/introspection/) 即可查看可用的数据，描述应用程序所需的数据，然后就可以开始竞赛了。
* **减少技术债务**：你知道什么比为单个界面编写后端到前端花费更多时间吗？编写 50 个后端到前端。GraphQL 可以服务于任意数量的应用程序，因此不必为每个应用程序编写或维护 BFF。
* **提高应用程序的一致性**：当类型及其关系在 API 本身中明确定义时，确保跨界面的一致性所需的工作就更少了。
* **抽象现有的 API 复杂性**：GraphQL 通常被视为 REST 的替代品。但 GraphQL 可以愉快地从其他 REST 端点获取数据。它提供了一个定制构建的抽象层，以帮助团队更快地交付功能。

当您考虑平台策略时，请记住它超越了基础设施。后端和前端之间通常存在很多摩擦，您可以使用 GraphQL 轻松解决这些摩擦。下载“
[API 的平台工程](https://www.apollographql.com/resources/platform-engineering-for-apis)” 白皮书，了解为什么 GraphQL 正迅速成为 API 平台团队采用的语言，以提高开发人员效率和速度。 [
YOUTUBE.COM/THENEWSTACK
### Corrected Markdown Text

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们的所有播客、访谈、演示等。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)