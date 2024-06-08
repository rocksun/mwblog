
<!--
title: 前端中的中间件？帮助管理Vercel上Webhook的工具
cover: https://cdn.thenewstack.io/media/2024/05/4c3fc462-gateway.jpg
-->

Hookdeck 提供了一个开源工具，帮助前端开发人员管理异步事件驱动的架构。

> 译自 [Middleware in the Frontend? Tool Helps Manage Webhooks on Vercel](https://thenewstack.io/middleware-in-the-frontend-tool-helps-manage-webhooks-on-vercel/)，作者 Loraine Lawson。

[Hookdeck](https://hookdeck.com/) 的一个新的开源中间件将帮助开发者管理 Vercel 上的异步事件。[Hookdeck Vercel 中间件](https://github.com/hookdeck/hookdeck-vercel) 旨在仅使用三行代码在 Vercel 的系统上运行。

Hookdeck 联合创始人兼首席执行官 [Alexandre Bouchard](https://www.linkedin.com/in/alex-bouchard/?originalSubdomain=ca) 告诉 The New Stack，该中间件增加了对通过 Webhook 向 Vercel 应用程序发出的异步 HTTP 请求进行身份验证、延迟、过滤、排队、限制和重试的能力。

两个用例是处理来自 Stripe、[Shopify](https://thenewstack.io/dev-news-rust-based-slint-matures-and-shopify-cleans-up/) 或 Twilio 等 API 提供商的 [Webhook](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/)，或构建 [异步 API](https://thenewstack.io/api-management-for-asynchronous-apis/)。他说，对于自称为事件网关的 Hookdeck 来说，这是一个自然的扩展。事件网关就像一个软件中心枢纽，用于管理服务之间的事件流，编排通过第三方进入或离开系统的事件。

## Webhook：面向事件驱动架构的网关

“我称 [Webhook 为面向事件驱动架构的网关药物](https://thenewstack.io/webhooks-the-building-blocks-of-an-event-driven-architecture/)，因为对于许多开发者来说，这是他们第一次接触异步编程范例和事件驱动架构问题，”Bouchard 说。“Hookdeck 位于你拥有的……基础设施前面，并摄取这些事件；我们处理管理、排队、错误恢复以及所有安全方面的问题。这意味着我们成为这些事件进出的中心点。”

Hookdeck 将事件网关视为 [API 网关的演变](https://thenewstack.io/shadow-apis-breaking-your-security-the-enroute-api-gateway-could-help/)，但适用于事件驱动的有状态工作流。该公司将其竞争对手视为 [Azure Event Grid](https://thenewstack.io/tutorial-exploring-azure-event-grid-custom-webhooks/)、[AWS EventBridge](https://thenewstack.io/going-serverless-on-aws-lambda-recognize-potential-risks/) 和开源项目 [Convoy](https://getconvoy.io/)。但当谈到 Hookdeck Vercel 中间件时，Bouchard 认为没有竞争对手的产品。

“你不会去找 Shopify 告诉他们，嘿，伙计们，回来半小时后再说——现在，我无法处理这件事，”Bouchard 说。“当你不控制发布者时，你实际上没有任何容错空间。Webhook 只是问题的一个子集。”

## 但为什么要使用中间件？

Bouchard 说，中间件方法非常适合无服务器运行时。他解释说，Hookdeck Vercel 中间件解决了两个问题。第一个问题是它提供了与完整的 Hookdeck 事件网关不同的 Web 开发人员体验。他说，这种方法适用于一小部分上下文，而 [Vercel](https://thenewstack.io/vercel-creating-new-ai-framework-also-rust-and-adobe-updates/) 是尝试该方法的最佳选择。

“Hookdeck 现在是非常声明式的。你必须预先配置所有配置、连接等，然后才能上线，”他说。“中间件的目标是能够偷偷摸摸地做到这一点。因此，基本上，能够说，在此代码中，我现在希望此端点成为我们所说的异步端点——一个请求被延迟、排队、建模等的端点；并且以一种对开发者来说体验非常透明的方式来做到这一点。”

他说，中间件组件允许开发者设置异步端点并为其建立规则和条件。他补充说，该代码在 Vercel Edge 网络上运行，但 Hookdeck 管理实际请求。

“基本上发生的事情是，中间件将接收来自 Shopify 等的 HTTP 请求，例如 Webhook，”他解释说。“它接收一个 Webhook，评估是否应该延迟和排队——如果应该，那么中间件将把该请求转发到 Hookdeck Edge 网络。”

使用中间件，开发者可以管理：

- 队列；
- 限制，用于第三方发送的 Webhook 超过系统处理能力的情况；
- 重试同步 HTTP 请求；
- 延迟，例如，在客户可以在一定时间内编辑订单的情况下使用；
- 过滤器，允许根据有效负载中的数据进行筛选，以允许事件通过或不通过。例如，它将允许使用 Shopify 的开发者仅筛选所有产品更新 webhook，以仅筛选库存中没有产品的 webhook，Bouchard 说。

对于将摄取数亿个事件或任何关键任务的场景，他建议使用 Hookdeck 的核心事件网关解决方案。

## 潜在扩展领域

JavaScript 也是尝试此方法的首选，因为它被广泛使用，但如果进展顺利，Hookdeck 计划也为其他语言开发中间件，他说。

Hookdeck 也正在考虑将该方法扩展到其他提供商。他补充说，代码本身的编写方式使得它的大部分内容可以在 Vercel 的上下文之外使用，尽管有一些开发人员体验考虑因素是特定于 Vercel 的。[Supabase](https://supabase.com/)，[Firebase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/) 的开源替代品，是他提到的一个可能提供商。

“我们在 Supabase 函数之上看到了很多用法，”他说。“那绝对是我们看到并正在考虑的一个。”
