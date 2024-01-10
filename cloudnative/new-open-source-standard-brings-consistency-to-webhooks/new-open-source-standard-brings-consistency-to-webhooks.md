<!--
title: 开源标准统一Webhook
cover: https://cdn.thenewstack.io/media/2024/01/75d85ae4-webhooks-1024x683.jpg
-->

Webhook长期以来缺乏标准规范，给接受端的开发者带来编程难题。一个新的开源标准力图改变这种状况。

> 译自 [New Open Source Standard Brings Consistency to Webhooks](https://thenewstack.io/new-open-source-standard-brings-consistency-to-webhooks/)，作者 Loraine Lawson。

Ken Ruf在他的工作中花费了大量时间思考和阅读有关 webhooks 的挑战，这是他在 Svix 公司的工作内容，这是一家“webhooks 即服务”公司。大多数抱怨来自正在接收 webhooks 而不是发送它们的开发人员，他对 The New Stack 这样说。

“我们经常看到人们只是抱怨 webhooks 有多糟糕，”[Ruf](https://www.linkedin.com/in/kenichiruf/) 说。“通过观察大量的讨论，我们的假设是最大的问题是碎片化。所以许多人以如此多的不同方式发送数据，以至于接收数据的人基本上每次当他们想从一个新的来源接收 webhooks 时都必须重新做一切。”

与 [API](https://thenewstack.io/infrastructure-apis-the-good-the-bad-and-the-ugly/) 不同，webhooks 主要用于实时数据和触发自动化工作流程。使用场景包括聊天消息、支付提醒、库存更新、订单状态更改和任务创建事件，如客户登录。使用 webhooks，接收应用程序通过提供源应用程序的 URL 端点来订阅事件。

“[webhooks 充当 HTTP 回调](https://konghq.com/blog/engineering/announcing-standard-webhooks)，使服务能够相互通知事件，”API 网关提供商 Kong 的高级员工软件工程师Vincent Le Goff写道。Le Goff 代表 Kong 参加新的标准指导委员会。“它们的功能类似于 ‘反向 API’，其中不是客户端通过 API 调用向服务发起请求，而是服务主动触发 webhooks 将更新推送到客户端。例如，服务可能会触发诸如 ‘用户已支付’ 或 ‘任务完成’ 之类的事件的 webhooks。”

相反，API 更经常用于双向数据交换，并倾向于涉及一些数据延迟。API轮询就像汽车后座的巴特和丽萨·辛普森——总是问“我们要到了吗”，Ruf 说。webhooks 更安静——更像玛吉，在不过多闲聊的情况下等待到达。他提供的另一个类比是，webhooks 就像有一扇门铃来提醒您客人的到来——您不必不断检查大门，因为当客人到达时，您会收到消息。

“它们非常灵活，”Ruf 说。“真的随时当您想要根据另一个产品或应用程序中的事件触发系统中的工作流程。”

但是直到上个月，webhooks 都缺乏标准的设计方法。对于其 [Webhooks 状态报告](https://www.svix.com/state-of-webhooks/)，Svix 检查了 10 个提供商文档中的 10 个因素，发现这 10 个因素中没有一个具有完全相同的实现，Ruf 说。随着 webhooks 变得越来越普遍，这对开发人员来说是一个问题。

“发生的事情是我有大部分代码，但我必须更改它，因为它们没有这 10 个中的一个，然后因为它们都不同，...我必须一次又一次地更改一点，而不是只需能够为不同的提供商拥有同一端点的不同版本，”他说。“你字面上需要复制大部分内容，然后在这里和那里更改一些内容。”

问题的一个例子: webhooks 自动重试失败消息的频率存在差异。Webhooks 状态报告发现 67% 的服务提供了自动重试，提供的最常见的重试次数为 5 次——大多在 3-10 次重试之间。最佳实践是指数回退，Ruf 说。

这种缺乏标准导致 Ruf 和 Svix 的创始人兼 CEO[ Tom Hacohen](https://www.linkedin.com/in/tomhacohen/) 决定为 [webhooks 创建一套标准](https://www.svix.com/blog/standard-webhooks/)。去年，这对组合成立了一个联盟来实现这一目标。

“我们真正想要做的是让那些大规模发送和接收大量 webhooks 的人参与进来，真正为委员会、为标准本身增加分量，”Ruf 说。

除 Hacohen 外，技术指导委员会成员包括:

- Zapier，一个 Web 应用集成公司;
- [Twilio](https://thenewstack.io/take-advantage-new-twilio-apis-cover-just-telephony/)，一个 Web 通信公司;
- Lob，一个直邮系统公司，也是 Svix 的客户;
- Mux，一个视频流公司;
- [ngrok](https://thenewstack.io/dev-news-django-updates-storybook-7-6-and-node-js-20-beta/)，一个统一的入口平台;
- [Supabase](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/)，开源 Firebase 替代品;
- 以及 [Kong](https://thenewstack.io/neosec-ties-its-api-security-platform-to-kongs-api-gateway/)，一个服务网格和 API 网关，根据 Ruf 的说法，其中内置了一些 Webhook 功能。

上个月，该机构在 [GitHub 上发布了开源标准 Webhook 规范](https://github.com/standard-webhooks/standard-webhooks/tree/main)，并启动了一个网站 [Standard Webhooks](https://www.standardwebhooks.com/)，它提供有关为标准做出贡献、治理机构和开源工具的信息来验证 Webhook 并模拟标准 Webhook 消息。

这些标准将帮助那些必须设置端点的开发人员，他说。采用这些标准将使重用代码变得更加容易，而不是从头开始自定义编码所有内容，Ruf说。

“当您尝试为来自另一个应用程序的新 Webhook 创建新端点时，您可以重用您已经编写的大量 Webhook 代码”，他说。“现在，您基本上需要从头开始编写所有内容。所以标准化的一个好处就是我们试图实现的使人们更容易从各种不同的提供商那里采用 Webhooks。”

[该标准规定](https://github.com/standard-webhooks/standard-webhooks/blob/main/spec/standard-webhooks.md)了其他事项:

- Webhooks 的理想有效负载大小(小于 20kb);
- Webhook 元数据;
- Webhook 标头; 和
- 签名方案。

他还补充说，该标准通过建立最佳实践来设置 Webhook 质量的标准。例如，就目前而言，Webhook 是否触发认证请求取决于个别开发人员。

“现在，人们到处都是，试图从不同的提供商那里接收 Webhooks 真的很痛苦，但我们也想尽可能方便地为人们提供良好的 Webhook 解决方案，因为这也是一个痛点，”他说。

该标准不仅概述了认证应该是 Webhook 流程的一部分，而且它对 Webhooks 的最佳认证方法提供了意见: [基于哈希的消息认证码(HMAC)签名](https://www.okta.com/identity-101/hmac/)。

Ruf 不知道有任何针对 Webhooks 的竞争标准。有[一种称为 Cloud Events 的规范](https://cloudevents.io/)，它以一种通用的方式描述事件数据，但它只简要地涉及了 Webhooks，他说。

“我们阅读了他们的实际标准，我们认为在那里还需要做很多工作。它不够具体，”他说，并补充说他们的目标是提供一个互补的标准，与已经完成的一些工作兼容。

“我们只是试图在他们实现 Webhooks 时让他们这些开发人员的生活更轻松，无论他们是为自己的公司实现它，还是将其发送给他们的用户，或者他们只是试图接收其他人的 Webhooks 来触发他们产品内部的工作流程自动化，”Ruf说。“如果我们能让所有人都采用它，那么它就能使每个人的生活都更轻松。”

