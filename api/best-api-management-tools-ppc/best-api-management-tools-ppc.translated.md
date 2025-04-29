## 寻找最佳 API 管理平台和顶级 API 管理工具的比较？

您可能因为搜索了“最佳 API 网关”、“最佳 API 管理平台”、“最佳 API 管理工具”、“顶级 API 管理工具”或类似内容而访问了此页面。不幸的是，当您搜索这些内容时，通常会得到一个供应商比较页面列表（是的，[我们自己也写过一篇](/comparison/gravitee-vs-apigee-0)...但我们认为我们做了一些非常独特的事情，所以一定要看看！），而这些页面通常都带有令人难以置信的偏见。例如，我们经常看到供应商在将自己与其他供应商进行比较时，会在每个框中给自己打上勾，而竞争对手几乎没有任何复选框。

这对像您这样的评估团队来说毫无帮助。这也不诚实，并且没有传达事情的真相：最佳 API 管理平台取决于您的用例和需求……是的，这种逻辑也适用于作为 API 管理解决方案提供商的 Gravitee。

因此，我们做了一些我们希望有帮助的事情：

- 我们为每个顶级 API 管理工具编写了深入的功能比较。这不仅仅意味着我们关注 [Gravitee](/comparison/gravitee-vs-kong) 与 Kong 的比较，例如，还包括我们比较 [Kong 与 Apigee](/comparison/kong-vs-apigee)、[Tyk](/comparison/kong-vs-tyk) 等等。我们对大多数主要的最佳 API 管理工具都这样做。我们为什么要这样做？当您搜索最佳 API 管理平台时，您最终可能会在 Kong 和 Tyk 之间犹豫不决，也许您希望第三方（即不是 Kong 或 Tyk）给您他们的意见。
- 我们撰写此博客作为我们各种 API 管理解决方案比较内容的中心位置，以便您可以进行研究而无需离开此页面。

我们希望您发现这一切都非常有帮助！如果不是，请[联系我们并告知我们。](/contact-us) 现在，开始研究吧！

## 最佳 API 管理平台排名

开玩笑的！我们不做排名，因为当最佳 API 管理工具取决于您的用例时，排名没有意义。因此，我们只是编制了一个最佳 API 管理解决方案列表，并将它们按不特定的顺序放在这里（虽然[我们确实包括了 Gravitee](#Gravitee)，而且我们真的认为我们至少值得一看！）

### 在此比较中我们包含了哪些 API 管理工具？

虽然有很多 API 网关和 API 管理解决方案，但我们将列表缩小到 6 个（并且我们会随着时间的推移添加更多，所以请留意）：

- Kong
- Tyk
- Apigee
- Mulesoft
- Azure API Gateway
- AWS API Gateway

#### 我们如何决定此 API 管理解决方案列表

是的，我们当然对我们选择的解决方案列表有偏见……它们只是我们听到最多的解决方案！如果您希望我们[研究](/contact-us)其他 API 管理软件解决方案，请告诉我们！

## 最佳 API 管理平台：Kong API 管理解决方案

Kong 广为人知，被认为是首屈一指的企业 API 网关和 API 管理解决方案之一。正如我们在 [Kong 比较页面](/comparison/gravitee-vs-kong) 中指出的那样，我们认为 Kong 提供了“..相对成熟的企业网关和 API 管理解决方案”。在考察他们的优势时，他们最显着的优势（与其他 API 管理解决方案相比）是他们在平台中包含了服务网格产品。如果您是一个决心让一个供应商提供 API 管理工具和服务网格工具的团队，那么 Kong 至少值得一看。但是，我们了解到，现在大多数寻找服务网格的组织都[开始在 Istio 上进行标准化](https://istio.io/latest/about/service-mesh/)；换句话说，Istio 可能已经“获胜”。

如果您像大多数组织一样，您可能不需要一个同时提供服务网格和 API 管理解决方案的供应商（也许您只需要一个可以支持您现有服务网格解决方案的 API 管理平台，例如 Gravitee 的）。在这种情况下，Kong 可能不是您的最佳选择。但是，以下是我们列出的 Kong API 管理的优缺点：

## Kong API 管理平台的优点 | Kong API 管理平台的缺点 |
|---|---|
| 一家拥有品牌知名度的老牌供应商 | 根据您选择的定价和包装层级，Kong 可能会随着您的扩展而变得非常昂贵 |
| 除了 API 管理之外，还提供服务网格 | Kong 对服务网格的关注导致对 API 管理的重视程度降低 |
| 提供您用于基本 API 管理用例所需的大部分功能 | Kong 不提供对将事件和消息代理公开为事件 API 的强大支持，例如 |
| [将 IAM 作为 API 安全策略的一部分](/platform/access-management)（我们推荐），您将不得不购买单独的解决方案，例如 Okta |

## 顶级 API 管理工具：Tyk API 管理解决方案
Tyk 是一个比 Kong 更新的参与者，但已经获得了一些关注，主要是因为他们早期采用了围绕 GraphQL 的服务。有一段时间，Tyk 可能是市场上最先进的 GraphQL API 管理解决方案。然而，[其他解决方案已经开始赶上](/blog/graphql-capabilities)，而且 GraphQL 实际上并没有像人们想象的那么流行。由于这种关注，他们在构建一些更“核心”的功能来支持 OAS 方面起步较晚，更不用说事件 API 了。

也就是说，Tyk 是一个现代化的 API 管理解决方案，具有相对强大的云产品。您可以在[此处](/pricing/tyk-api-management)了解更多关于该云产品的[结构、定价和打包方式](/pricing/tyk-api-management)。目前，Tyk 提供了传统 API 管理解决方案所需的大部分功能。但是，它们确实缺乏一些用于更现代用例的功能，例如支持异步 API、事件 API 和联邦 API 管理。以下是我们列出的 Tyk API 管理的优缺点：

## Tyk API 管理平台的优点

*   一个相对成熟的供应商，具有品牌知名度

## Tyk API 管理平台的缺点

*   [一些其他现代供应商可以做到；](/platform/streaming-proxies)虽然他们确实为 Kafka 用例提供了一些支持，[将 IAM 作为 API 安全策略的一部分](/platform/access-management)（我们推荐），您将不得不购买单独的解决方案，例如 Okta

## 最佳 API 管理工具：Apigee API 管理解决方案

Apigee 是这个领域的早期进入者，他们早期的成功[导致了谷歌的收购](https://cloud.google.com/blog/products/gcp/google-to-acquire-apigee)。这次收购对 Apigee 团队来说是件好事，但通常被认为对 Apigee 客户来说不太好。我们将在下面的优缺点表中介绍这次收购的一些典型缺点。

抛开收购后的问题不谈，Apigee 被广泛认为是合适的企业 API 管理解决方案。虽然他们没有做太多工作来为现代 API 管理用例提供新的支持（例如[支持事件和消息代理](/platform/streaming-proxies)），但他们专注于创建一个平台，使您能够相对快速地公开、发布和货币化 API 产品。这可能是选择像 Apigee 这样的解决方案的首要优点，尽管[其他供应商也为此用例提供解决方案](/blog/incentivizing-api-providers-and-consumers-through-api-monetization)。

在我们深入了解 Apigee API 管理的优缺点之前，重要的是要指出 Apigee/Google 的云战略以及它如何影响使用和/或关注 Apigee 的团队。Apigee 的最新版本，具有最现代的功能和创新，要求您在 Google Cloud 环境中部署和托管 Apigee。您不能使用其他云提供商。也就是说，如果使用 Apigee 的旧版本，则可以使用其他云解决方案。对于想要实施混合云和多云战略的现代团队来说，这是一个问题。

总而言之，让我们深入了解 Apigee API 管理的优缺点。

## Apigee API 管理平台的优点

*   一个非常成熟的供应商，具有品牌知名度
*   为 API 产品化提供相对强大的支持
*   [按需付费和基于订阅的定价](/pricing/apigee)可能具有吸引力，

## Apigee API 管理平台的缺点

*   Apigee 的创新速度不如其他一些较新的 API 管理供应商。对于支持 GCP 之外的其他云供应商的 Apigee 版本尤其如此
*   Apigee 的开发者门户比许多其他解决方案更难使用和设置（更多详细信息请参见[本页上的部分](/comparison/gravitee-vs-apigee)）
*   [但定价结构可能看起来很复杂](/pricing/apigee)。Apigee 还会惩罚需要支持大量 API 消耗的团队，因此随着您扩展 API 计划，它可能会变得非常昂贵。[其他供应商](/api-management-buyers-guide-event-native)已经超越了他们。您可以在我们的[深入 Apigee 功能比较页面](/comparison/gravitee-vs-apigee)的“API 网关和 API 管理控制台”部分找到更多详细信息。[将 IAM 作为 API 安全策略的一部分](/platform/access-management)（我们推荐），您将不得不购买单独的解决方案，例如 Okta

## 最佳 API 管理平台：AWS API Gateway
AWS Gateway 代理流量，并且可以控制对 API 的访问。但是，您只能通过编写 Lambda 函数（需要特定的 AWS 技能）或使用 API 使用计划中数量有限的设置来实现。[他们的定价也一直是个问题](/pricing/aws-api-gateway)，因为他们的收费几乎完全基于 API 消耗和 lambda 函数执行。我们已经帮助许多组织[从 AWS 迁移](/migration)，每年节省数百万美元，同时仍然获得更强大的 API 管理支持，例如预构建的开发者门户、[预构建的网关逻辑](/plugins)和授权、[对事件 API 的支持](/platform/streaming-proxies)等等。

同样重要的是要注意，AWS API Gateway 解决方案仅提供对 REST API、HTTP API 和 Websocket API 的有限支持，这使得许多使用不同 API 和协议的组织无法获得解决方案。

也就是说，您将获得启动 API 管理实践所需的一些基本功能。以下是我们列出的 AWS API Gateway 的优缺点：

## AWS API 管理工具的优点

## AWS API 管理工具的缺点

大多数团队至少在某些地方使用 AWS，并且 AWS 使您可以轻松地将积分用于 AWS API Gateway 解决方案 | AWS 强制您使用 AWS 云，因为他们的主要产品是 AWS 托管的。对于想要自托管网关或想要混合部署模式的团队，不建议使用 AWS

提供创建 API 代理的一些最基本的功能 | AWS 不提供预构建的、供应商管理的

由于企业 API 管理实践所需的大部分网关逻辑都与 Lambda 函数相关联，因此您被迫：

- 编写这些函数，这可能很复杂
- 按执行付费，这可能会变得 *非常* 昂贵

[基于消耗的定价](/pricing/aws-api-gateway)可能很有吸引力 AWS API Gateway 的[按需付费和基于消耗的定价](/pricing/aws-api-gateway)对于希望在保持成本下降的同时进行扩展的组织来说，具有很大的局限性。例如，在从 AWS 迁移时，我们为大型企业降低了 60% 以上的成本。

[深入的 AWS API Gateway 功能比较页面](/comparison/gravitee-vs-aws)。

## 最佳 API 管理平台：Azure API 管理工具

Azure 提供了一个朴实无华、平淡无奇的 API 网关和管理解决方案。该解决方案包括基本的 API 网关和 API 管理功能，如策略配置和应用、服务转换等。与其他主要由云提供商提供的解决方案（如 AWS Gateway）一样，主要优势在于您可以将 API 管理和 API 网关解决方案与您的云配置供应商捆绑在一起。就我个人而言，我们经常觉得这种好处被夸大了，我们建议选择一家真正精通 API 管理的供应商。也就是说，以下是选择 Azure 作为 API 管理工具的优缺点：

## Azure API 管理工具的优点

## Azure API 管理工具的缺点

如果您已经在使用 Azure 云服务，则可以将该支出用于 Azure API 管理工具 | 与 AWS 一样，您需要使用 Azure 云服务

提供创建 API 代理的一些最基本的功能 | Azure API Gateway 并不以功能丰富而闻名，不建议用于更复杂、更现代的 API 管理用例。有关更多信息，请查看我们的

虽然 Azure API Gateway 工具支持一些 WebSocket 和 GraphQL 用例，但它们不支持其他现代用例，例如[将事件和消息代理资源公开为 API](/platform/streaming-proxies)

Azure API Gateway 的按需付费和基于消耗的定价对于希望在保持成本下降的同时进行扩展的组织来说，具有很大的局限性。

[API 设计器](/platform/api-designer)。

## 最佳 API 管理平台：Gravitee

我们将最好的留到了最后（开玩笑...记住，最好的是基于 *您的* 用例）！

Gravitee 是一个功能齐全、全生命周期的 API 管理解决方案。我们将把深入的功能解释留给我们的完整指南[Gravitee 平台](/everything-gravitee)，但这里有一个快速快照，介绍了我们认为我们擅长的地方以及与此页面上的其他供应商的不同之处：
**我们专注于构建市场上最强大的全生命周期 API 管理解决方案。** 例如，虽然我们可以与您的服务网格产品协同工作并对其进行补充，但我们选择不构建我们自己的服务网格产品，这使我们能够为 API 生命周期的每个阶段创建最强大的 API 管理解决方案。

**我们是事件原生的。** 这意味着我们不仅为同步 REST API 提供原生支持，还为事件 API 提供原生支持，将事件和消息代理公开为 API，以及使用 AsyncAPI 规范的异步 API。 没有其他人为异步和事件 API 用例提供这种级别的支持。

**我们提供任何其他 API 管理平台中最先进的安全性。** 因为我们提供了数十个[预构建策略](/plugins)（其中许多是面向安全的）、简单的[通过计划进行访问控制的机制](https://documentation.gravitee.io/apim/guides/api-exposure-plans-applications-and-subscriptions)以及[功能齐全的身份和访问管理解决方案](/platform/access-management)，没有人提供如此多的预构建、供应商管理和“即用型”API 安全功能。

也就是说，每个解决方案总是有缺点的（就像有优点一样！）。 这是我们的列表：

## Gravitee API 管理平台的优点

## Gravitee API 管理平台的缺点

| 优点