# REST 在许多 API 使用场景中仍然优于 GraphQL

![REST 仍然优于 GraphQL 用于许多 API 使用场景的特色图片](https://cdn.thenewstack.io/media/2024/10/5e70fd80-douglas-lopes-ehyv_xoz4ia-unsplash-1024x683.jpg)

[Douglas Lopes](https://unsplash.com/@douglasamarelo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/a-laptop-computer-sitting-on-top-of-a-wooden-desk-ehyV_XOZ4iA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上

在过去的几年里，我一直听到 [GraphQL](https://thenewstack.io/is-graphql-over-or-do-we-just-need-to-rethink-it/)——一种用于 API 的查询语言，允许客户端请求特定数据——是 API 的未来。它的炒作来自清晰且引人注目的价值主张。也就是说，它可以帮助您获取所需的确切数据并从单个请求访问多个资源，从而节省您的时间、金钱和带宽。

但是，当您 [开始使用 GraphQL](https://thenewstack.io/why-every-api-strategy-needs-graphql/) 时，您会发现它会产生一整套新的问题，这些问题会压倒其优势。

我将分解这些问题，以便您更好地决定 GraphQL 是否值得在您的集成中使用。我还将重点介绍为什么 REST 今天是更好的选择，并将继续成为领先的 API 标准。

## GraphQL 的缺点

我可以指出使用 GraphQL 的几个基本问题。首先，[GraphQL 经常导致复杂的查询，这些查询会严重](https://thenewstack.io/salt-security-finds-serious-graphql-api-security-hole/) 影响后端性能。这会导致处理时间过长，抵消了 GraphQL 的一项承诺优势——更快的响应时间。深度嵌套的查询甚至会导致服务器宕机，进一步延迟响应。

此外，GraphQL 通常根据请求的复杂性（例如请求的字段或对象的数量）应用速率限制。随着时间的推移，随着您在请求中增加资源，理解和遵循您的速率限制将变得更加复杂。

最后，随着 API 的成熟，其 GraphQL 模式变得更加复杂。成功地驾驭这种不断增长的复杂性不仅从速率限制的角度来看很痛苦，而且当您的团队构建请求时，还会导致代价高昂的错误。

## 为什么 REST 更好并且将继续存在

以下是一些 REST 是集成 SaaS 应用程序的最佳选择的原因。

- REST API 附带标准化的错误代码。
这些代码——包括从 404（未找到）到 500（内部服务器错误）的所有内容——使诊断问题和构建自动解决问题的错误处理流程变得容易。例如，如果您收到 429 太多请求错误，您可以根据响应中建议的等待时间创建自动重试。

另一方面，GraphQL 要求您的工程师考虑错误键中提供的响应。由于这些响应不像 REST 中那样标准化，因此它们更难计划和自动处理。

- 许多工程师都有构建和/或维护 REST API 集成的经验。
各种规模的公司主要使用 REST API。

举个例子：[根据 Gartner 的研究](https://www.gartner.com/en/documents/5551595)，85% 的组织使用 REST API——而 GraphQL 仅被 19% 的组织使用。

鉴于 REST 的流行程度，您的开发人员可能在构建和维护 REST API 集成方面经验丰富且得心应手。找到和雇用具有 REST 工作经验的工程人才也更容易，这使得您的组织更容易随着时间的推移扩展 REST API 集成。

此外，虽然 API 提供商不可避免地会难以让开发人员与他们集成，但以开发人员最熟悉的架构提供 API 将消除采用的一大障碍。

- REST 的开源生态系统比 GraphQL 的生态系统要全面得多。
用于 REST 的各种后端框架和库可以自动生成 OpenAPI 规范。这些工具也以多种编程语言提供，允许您的 [开发人员使用他们最熟悉的语言](https://thenewstack.io/hey-programming-language-developer-get-over-yourself/) 工作。

除了 OpenAPI 之外，您还可以访问各种开源工具来 [管理 REST API 开发的各个方面](https://thenewstack.io/using-a-developer-portal-for-api-management/)，包括验证、安全、监控和测试。

Postman 非常适合测试 REST API；OpenAPI 允许您自动生成 API 文档；REST 框架（例如 Django REST Framework）是为特定 [编程语言](https://thenewstack.io/programming-languages/) 构建的，并提供帮助您高效构建 API 的工具，等等。

这并不是说 GraphQL 不存在工具；只是与 REST 相关的扩展更多，并且支持更好。
## 最后的想法

随着 API 领域的不断成熟，我预计将发布更多 [API 架构](https://thenewstack.io/untangling-enterprise-api-architecture-with-graphql/)，并像 GraphQL 一样受到类似的炒作。这种炒作主要来自那些尚未以有意义的方式利用它们的人，如果有的话。

在竞争的 API 架构能够超越——甚至匹配——REST 对提供者和消费者双方的实用性之前，REST 将继续成为首选。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。