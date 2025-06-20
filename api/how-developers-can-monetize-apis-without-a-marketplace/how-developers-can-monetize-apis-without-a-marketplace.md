
<!--
title: 无需市场：API变现的秘诀
cover: https://cdn.thenewstack.io/media/2025/06/b6ecbe0f-postman_mascot_atpostcon2025.png
summary: API 货币化市场增长迅速，预计 2027 年美国市场将达 80 亿美元。常见的收费模式包括基于使用量、订阅和收入分成。实施细节涉及使用 Redis 等技术进行计数和配额管理。技术栈包括计费提供商、API 网关和开发者门户。
-->

API 货币化市场增长迅速，预计 2027 年美国市场将达 80 亿美元。常见的收费模式包括基于使用量、订阅和收入分成。实施细节涉及使用 Redis 等技术进行计数和配额管理。技术栈包括计费提供商、API 网关和开发者门户。

> 译自：[How Developers Can Monetize APIs Without a Marketplace](https://thenewstack.io/how-developers-can-monetize-apis-without-a-marketplace/)
> 
> 作者：Loraine Lawson

[API 货币化](https://thenewstack.io/the-dos-and-donts-of-api-monetization/)预计仅在美国就将在 2027 年达到 80 亿美元。 [Zuplo](https://zuplo.com/) 的一名软件工程师 Adrian Machado 表示，在 AI 驱动的 API 出现后，这个数字可能会更高。 Zuplo 是一个为开发者设计的 [API 管理](https://thenewstack.io/introduction-to-api-management/)平台。

例如，在旅游行业，大约 90% 的收入来自 API，他说道。 Expedia、航空公司、旅游产品——都是通过 API 销售的，他补充道。

“你应该知道的一件事是，API 货币化市场正在增长，仅[在]美国，API 货币化收入将在 2027 年达到 80 亿美元，所以距离现在只有两年时间了——而且随着 AI 驱动的 API 的出现，这个数字可能会更高，”Machado 在本月于洛杉矶举行的 Postman [POST/CON](https://www.postman.com/postcon/2025/) 大会上告诉听众。

这不仅仅是为 API 收费。 还在于通过 API 进行价值交换； 这可以包括间接货币化以及生态系统扩展，他解释说。

“但也有其他一些间接好处，”他说。“其中一些是与你的开发者社区建立联系，并授权他们在你现有平台的基础上构建新功能。 Facebook 就是一个很好的例子，他们构建的游戏生态系统以及许多用户在其基础上构建的功能——例如，Messenger，对于企业而言。”

[API 货币化策略](https://thenewstack.io/apis-are-driving-new-business-models-and-unlocking-revenue-streams/) 还可以帮助支持更大的客户，例如使用你的 API 的企业或政府，他补充道。

“政府来了，他们不想点击你时髦的 Web 门户，”他说。“他们想要一个 API 来与他们现有的系统（如 HubSpot 或其他系统）进行自动化，以促进你平台的自动化。”

最后要考虑的是，你的竞争对手可能已经在制定 API 货币化策略了，他说道。

## API 的收费模式

首先要考虑的是你的 API 货币化模型。 这是业务方面的问题——本质上，是如何为 API 收费。 Machado 表示，开发者有三种选择：

**基于使用量的模型或按次付费。** “顾名思义，这是根据你的消费者对 API 的使用量收费，”他说。“通常，这看起来像 API 调用。”

费率可以基于每个 [API 调用](https://thenewstack.io/sentrys-front-end-performance-monitoring-pinpoints-sluggish-api-calls-and-database-queries/) 的点数或美分，甚至每个 1,000 个 API 调用 1 美元。

“无论是什么，它都是一些固定数量的 API 调用，”他说。“但它不一定是很大的 API 调用。 再次回忆一下，一个 AI 示例。 Token 消耗也是基于使用量的计费。”

类似地，你也可以按数据消耗收费。

“想象一下，你是 Dropbox，有人将 3MB 的文件上传到你的服务器——你将向他们收取存储费用，”他说。“而不是 API 调用，因为他们可以上传一个巨大的文件和非常小的文件。”

然而，这种方法的一个挑战是，无法知道你将从 API 中赚多少钱——可能是 10,000 美元，可能是 15,000 美元，或者可能什么都没有。

**订阅模式。** 与基于使用量的模型相反的是订阅模式。 基本上，你为用户创建存储桶，例如一个可以免费获得 1,000 个请求的层级，一个可以获得 100 万个请求的创业公司层级，然后是企业层级，该层级可能会获得 1 亿个请求。 每个层级收取不同的月费。

“实际上，从基于订阅的计费开始非常困难，”他说。“首先确定这些层级实际上非常困难。 通常，你需要做一点数据科学，才能了解平均使用量是多少，具体取决于组织规模和类似的事情。”

还有百分比费用，这在支付和金融科技领域更为常见。 想想信用卡 API 或加密货币公司，它们对通过 API 的每笔交易收取 1% 或 2% 的费用。

**收入分成模式。** 他认为这种模式并不常见。 在收入分成中，API 提供商和调用 API 的人之间存在合作关系，他们基本上一起赚钱。 这是 Google Adsense 使用的模式。

“例如，你正在调用 AdSense API，他们将获得，比如说，每次广告展示 1 美元，”他说。“例如，他们会给你 50 美分。 所以你们双方都能赚一点钱。”

他说，最常见的两种货币化模式是基于订阅的计费和基于使用量的计费。

他简要提到的一种选择是 **API 市场** 作为货币化的一种手段。 他不赞成，也不鼓励开发者选择该选项。

“首先，他们向你收取的收入分成——我认为，在费用和所有费用之后，他们会收取大约 20% 的收入——本质上只是充当计费提供商，并为你的 API 做一点营销，”他说。“我建议避开它。 没有严肃的企业会在 API 市场上销售。”

## 实施细节

在基于使用量的模型中，开发者基本上按请求数量收费。 它通常使用分布式计数器来实现。 Machado 表示，他使用 [Redis](https://thenewstack.io/redis-is-open-source-again/)，这是一个 NoSQL 内存缓存数据库，用于存储每个 IP 地址的帐户运行。 他使用了托管的 Redis 提供商，但指出它可以自托管。

“很简单，我在这里调用 Redis，”他说。“我只是在第 6 行到第 8 行使用 Redis 的其余部分进行身份验证，然后在第 11 行到第 23 行中有一个简短而非常简单的函数来读取用户。 在我的例子中，我将读取请求的 IP 地址。 但这同样可以是一个作业 Token、一个 API 密钥，任何你真正想根据其收费的内容。”

然后他创建了一个计数器，在第 19 行中可以看到。 这是他放入 Redis 中的密钥，用于唯一标识用户发出了多少个请求。

```js
const REDIS_TOKEN = environment.REDIS_TOKEN;
const redis = new Redis ({
  url:"https://hardy-jennet-24391.upstash.io",
  token: REDIS_TOKEN,
  })
  
  export default async function (requeset: ZuploRequest, context: ZuploContext)  {
    // Get user capabilities
    const user = request.user.sub;
    
    // Increment request count
    const date = (new Date()).getDate();
    const month = (new Date()).getMonth();
    const year = (new Date()).getFullYear();
    const counter = '${user}-${month}-${year}';
    const count = await redis.incr(counter);
    
    return 'The new count is ${count} for counter ${counter}.';
```

“在这种情况下，我查看日、月和年，以便此计数器用于此用户，在此日、月和年，有多少个请求进入，”Machado 说。

他从数据库中获取该日期的值，然后可以回顾并看到它发出了 2,000 个 API 调用。 然后，他使用某种支付网关来相应地收取费用。

“这样做有很多优点，”他说。“它非常灵活。”

在基于订阅的模式中，他现在引入了配额的概念。

“比如说，我将限制你每分钟 10 个 API 请求，一旦你达到这个限制，我就会开始拒绝你，因为我有一个计划，而该计划只允许 10 个 API 请求，”他说。“如果你想获得更多 API 请求，你必须和我谈谈，你必须升级你的计划。”

```js
const REDIS_TOKEN = environment.REDIS-TOKEN;
const redis = new Redis ({
  url: "https//hardy-jennet-24391.upstash.io",
  token: REDIS_TOKEN,
]);

const PLANS = {
  pro:  {
    limit: 10
    }
  }
  
  export default async function (request: ZuploRequest, context: ZuploContext) {
    // Get user capabilities
    const user - request.user.sub;
    const plan - request.user.data.plan;
    const requestLimit = PLANS[plan].limit;
    
    // Increment request count
    const month = (new Date()).getMonth();
    const year = (new Date().getFullyear());
    const counter = '${user}-${month}-${year}';
    const count = await redis.incr (counter);
    
    // Check if they are under quota
    if (count > requestLimit) {
      return HttpProblems.badRequest(request, context, {
        detail: "You are over your quota!"
      })
     }
     
     return 'The new count is ${count} for counter ${counter}. You have ${requestLimit-count} requests left.';
```

该方法允许每个配额周期 10 个 API 请求，因此早期的大部分代码保持不变。 但在这种情况下，他需要找到用户的计划。 通常，这将是开发者将附加的元数据，他解释说——它可能包含在作业 Token 中。 它也可以设置为外部系统，以提取用户的计划是什么。 第 29 行引入了内置的新的配额系统，其中代码检查用户是否超过了其计划的速率或配额限制，他指出。 如果用户超过了，则代码将发回一个名为 retail response 的错误请求。

“这样做有很多优点，”他说。“现在你正在收取固定费用，例如每月 100 美元用于 10,000 个 API 请求。 你知道你明年每月都会有 100 美元，只要用户不取消。 因此，你可以更好地预测和预测收入，这使你的预算、未来、API 开发或其他方面的开发更容易。”

但也有一些缺点。 首先，它更难启动，需要提前了解一些关于使用情况的数据才能建立层级。

对于跨越层级边界的客户来说，它也可能不是理想的选择。 升级一个层级可能不值得，因此他们可能会减少使用你的 API。

## 技术栈

他指出，支持这些模型的最低技术栈是：

* **计费提供商**，例如用于管理你的产品、创建定价表、管理订阅和促进付款的金融科技系统。 他指出，可能的提供商包括 [Stripe](https://stripe.com/)、[Paddle](https://www.paddle.com/) 和 [Apigee](https://thenewstack.io/building-adaptive-apps-like-google-now-with-apis-and-analytics-with-apigee-insights/)。
* **API 网关**，用于跟踪和报告使用情况、强制执行身份验证和授权以及强制执行配额。 他承认自己有点偏见，因为他为 Zuplo 工作，他推荐了 Zuplo，但他指出 [Moesif](https://www.moesif.com/) 加上任何网关和 Apigee 也是其他选择。
* **一个** [开发者门户](https://thenewstack.io/api-governance-and-developer-experience-in-a-developer-portal/)，用于提供良好的开发者体验，开发者可以在其中浏览文档、购买 API 订阅、跟踪使用情况和管理授权。

如果你更喜欢自己构建解决方案，他建议：

* **负载均衡器**。 API 调用可以来自任何地方，因此在你的服务前面放置一个负载均衡器，并确保使用无服务器主机（例如，Lambda）自动缩放以处理高流量。
* **速率限制器 + Web 应用程序防火墙 (WAF)。** 他说，如果你想编写自己的速率限制器服务，[Cloudflare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/) 可以提供 WAF。
* **API 密钥系统**。 他指出，API 密钥提供最佳的 UX，你可以自己编写或使用 [Unkey](https://www.unkey.com/)。