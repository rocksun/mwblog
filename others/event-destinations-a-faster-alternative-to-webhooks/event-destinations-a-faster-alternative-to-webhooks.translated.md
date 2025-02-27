# 事件目标：比 Webhook 更快的替代方案

![事件目标：比 Webhook 更快的替代方案的特色图片](https://cdn.thenewstack.io/media/2025/02/1ba83ce4-eventdestinationsalternativetowebhooks-1024x683.jpg)

Webhook 应用广泛，但也并非没有挑战。例如，缺乏[广泛采用的标准](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/)，这意味着没有通用的重试、超时、身份验证或有效负载格式方法。

Webhook，Atlassian[定义](https://developer.atlassian.com/server/jira/platform/webhooks/)为“基于 HTTP 的用户定义回调”，会为发布 Webhook 的[API](https://thenewstack.io/api-governance-using-patterns-from-paypal-netflix-and-more/) 平台和构建摄取 Webhook 的应用程序的开发者都造成性能瓶颈，导致高昂的运营和基础设施成本。

为了解决这些弱点，周一启动的一份最新宣言提出了一种名为事件目标的替代方法，它提供了一种比 Webhook 更具可扩展性、更快的替代方案。

“[事件目标倡议网站](https://eventdestinations.org/)”指出：“Webhook 是最低公分母。它们提供了惊人的覆盖范围，但在规模上缺乏能力。如何将 Webhook 的覆盖范围与其他事件范例的功能结合起来？答案是事件目标。”

## 什么是事件目标？

事件目标是一套处理事件的新方法的指南，但你也可以将其视为一种新兴模式。[Hookdeck](https://hookdeck.com/) 的开发者关系主管 [Phil Leggetter](https://www.linkedin.com/in/leggetter/?originalSubdomain=uk) 解释说，事件目标是事件生产者可以发送事件的[端点或系统](https://hookdeck.com/blog/event-destinations)，同时允许开发者直接使用他们熟悉的工具。

Leggetter 于周一启动了网站[EventDestinations.org](https://eventdestinations.org/)，作为解释该方法和指南的中心。还有一个[GitHub 仓库](https://github.com/hookdeck/event-destinations/blob/main/specification.md)，它提供了网站的源代码和事件目标的更详细规范。

在线支付处理平台[Stripe 首次引入了事件目标](https://docs.stripe.com/event-destinations)，但它也被[Twilio](https://www.twilio.com/docs/events/event-streams/sink-resource) 和[Shopify](https://shopify.dev/docs/apps/build/webhooks/subscribe/get-started?deliveryMethod=pubSub) 使用，并由事件网关 Hookdeck 支持。

Leggetter 解释说：“你可以传递 Stripe 平台事件——支付、你希望你正在构建的应用程序从 Stripe 平台消费的事件——不仅通过 Webhook，也不仅通过 Stripe 的 HTTP 请求通知，还可以直接传递到 Amazon EventBridge。”

实施指南规定，它必须支持至少两种类型的事件目标，其中一种必须是 HTTP Webhook，因为它们使用广泛且简单。

![图表显示事件目标可以发送到 HOOKDECK AMAZON EVENTBRIDGE GCP PUB/SUB KAFKA RABBITMQ](https://cdn.thenewstack.io/media/2025/02/0636cd67-event-destinations-1-2.png)

由 Phil Leggetter 通过[EventDestinations.org](https://eventdestinations.org/) 提供

但第二种类型可以从其他流行的事件目标中选择，例如[消息队列或事件](https://thenewstack.io/choosing-between-message-queues-and-event-streams/)总线。支持的事件目标类型的示例包括：

- 消息队列（例如，[AWS SQS](https://aws.amazon.com/sqs/)、[RabbitMQ](https://thenewstack.io/rabbitmq-is-boring-and-i-love-it/)）
- 事件总线（例如，[Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)、[Google Cloud Pub/Sub](https://cloud.google.com/pubsub)）

文档指出：“此要求确保实现可以满足开发人员的不同用例、集成需求和偏好。”

## 客户的需求

Leggetter 说，从 API 平台构建者的角度来看，事件目标消除了巨大的负担。

Leggetter 说：“它实际上减轻了他们的负担，因为其他目标类型的成功交付率会更高，从而无需排队和管理重试。他们知道更高比例的事件将被 Amazon EventBridge 或 GCP Pub/Sub 成功摄取，因为这些都是高度可用、快速的可靠摄取事件的服务。”

此外，这也是客户的需求，他补充道。
“我们观察到，API 平台供应商希望以不同于仅使用 Webhook 的方式交付，以减轻其基础设施方面的负担，同时提供更好的[开发者体验](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/)——减少客户需要管理的基础设施，”他说。

## 早期采用者
Stripe、Twilio 和 Shopify 都允许开发者将事件直接发送到支持的事件目标，其中包括消息队列和代理，例如 AWS Simple Queue Service (SQS)、GCP Pub/Sub、Hookdeck 和 RabbitMQ，以及分布式流平台[Kafka](https://thenewstack.io/shift-left-meets-kafka-testing-event-driven-microservices/)。

Stripe 的事件目标实现允许开发者根据自身需求选择最佳目标，Webhook 只是其中一种选择。

“通过增强现有的 Webhook 功能并引入新的目标类型，开发者可以按照自己的节奏进行过渡，保持向后兼容性并充分利用两者的优势，”宣言中指出。

对于 Shopify、Twilio 和 Stripe 等事件生产者来说，这提高了效率，并降低了与公共 HTTP 端点相比的失败率和重试交付次数。

事件目标网站称，这为高吞吐量场景解锁了性能提升。

“智能重试逻辑、改进的可交付性和可扩展的基础设施最大限度地减少了资源消耗，降低了运营成本，同时确保了任何规模下事件交付的无缝性，”网站指出。

事件生产者必须支持一组事件目标工作准则：

- 允许两种事件目标类型，包括 Webhook；
- 自动交付重试，采用指数退避；
- 用于创建、更新和删除目标的 API；以及
- 目标故障警报。

## 开发者的益处
“这种 DX 演变对每个人都有帮助；开发者获得了更强大、更易于使用和维护的工具，”宣言中指出。“开发者在[采用开发者](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)平台方面更加成功和快速。”

具体来说，该网站概述了开发者以下益处：

- 更轻松的集成，因为开发者不再需要设置、管理和扩展 HTTP 端点；
- 降低认知负荷，因为重试、安全性和性能处理方面的标准化使开发者能够依靠一致且可预测的事件交付；
- 内置的可扩展性，因为随着系统规模的扩展，高效的协议、批处理和久经考验的弹性基础设施确保事件交付保持可靠，即使在高吞吐量下也是如此；
- 通过消除对 API 网关、负载均衡器、HTTP 消费者和其他基础设施组件的需求来减少维护开销；以及
- 可预测的行为和标准化的事件预期——消息总线处理超时、重试和安全问题。

“这种演变不仅仅是解决痛点——它还为构建事件驱动型应用程序的开发者解锁了新的可能性，”宣言中指出。“通过优先考虑互操作性、安全性和效率，事件目标代表了创建赋能所有人的开发者体验的下一步。”

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)