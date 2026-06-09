<!--
title: Replit 展示“氛围编程”如何构建专属金融技术栈及盈利之路
cover: https://cdn.thenewstack.io/media/2026/06/dca9fe39-eva-wahyuni-mhnz-swy5sq-unsplash-scaled.jpg
summary: Replit通过集成Shopify、RevenueCat和Visa，为“氛围编程”构建了包含订阅、电商及智能体支付的金融技术栈，助开发者攻克变现难关，打通商业化闭环。
-->

Replit通过集成Shopify、RevenueCat和Visa，为“氛围编程”构建了包含订阅、电商及智能体支付的金融技术栈，助开发者攻克变现难关，打通商业化闭环。

> 译自：[Replit shows how vibe coding is getting its own financial stack — and a path to profit](https://thenewstack.io/replit-shopify-storefront-integration/)
> 
> 作者：Paul Sawers

制作应用比以往任何时候都更加容易，但如何从中赚钱完全是另外一回事。

虽然现在几乎任何人都可以[通过氛围编程](https://thenewstack.io/beginners-guide-to-vibe-coding/)开发出能运行的应用，但将该应用转化为收入来源才是事情变得复杂的地方。这正是 [Replit](https://replit.com/) 一直致力于解决的问题。他们正在悄然为氛围编程应用构建一个金融技术栈，涵盖代理支付、定期订阅以及如今的电子商务店面。

## Shopify 加入对话

最新加入其中的是 Shopify 集成，该功能于[周四宣布](https://replit.com/blog/create-a-custom-shopify-store)，允许用户直接在 Replit 智能体中设计和发布自定义店面，无需任何电商经验。

在一次[演示演练](https://x.com/Replit/status/2062594881625940379?s=20)中，Replit 社区团队成员 [Manny Bernabe](https://www.linkedin.com/in/mannybernabe/) 描述了他想要创建的店铺——在自建案例中，这是一个名为 WormWild 的软糖蠕虫品牌——随后智能体便开始工作，仅凭提示词就生成了自定义店面概念，并规划了产品、品牌形象和布局。

![告诉 Replit 你想创建什么样的店铺](https://cdn.thenewstack.io/media/2026/06/e47e4174-gif1.gif)

*告诉 Replit 你想创建什么样的店铺*

用户唯一需要离开 Replit 的时刻是连接他们的 Shopify 账户。对话中会出现一个请求授权的提示，此时用户将被引导至 Shopify 认领智能体为他们配置的店铺并订阅方案——这会激活付款功能并让店铺做好交易准备。

![将 Replit 与 Shopify 连接](https://cdn.thenewstack.io/media/2026/06/13a88006-gif2.gif)

*将 Replit 与 Shopify 连接*

店铺认领并连接完成后，智能体会继续构建——优化店面设计、添加商品列表，并为发布做好一切准备。

最终呈现的是一个功能完整的 Shopify 店铺，拥有定制设计的前端，可随时接收真实订单。据 Replit 称，整个过程大约需要十分钟。

![进行构建](https://cdn.thenewstack.io/media/2026/06/459d9382-gif3.gif)

*进行构建*

在一篇纪念与 Shopify 建立合作伙伴关系的[博客文章](https://replit.com/blog/create-a-custom-shopify-store)中，Replit 坦言，虽然其用户已经能够交付“真正的软件”，但销售实体产品完全是另一回事——这带来了一系列关于库存、履约、税务合规、物流以及多渠道销售的复杂问题。

> “之前缺少的是一种*为* Shopify 设计店面的方式，且这种方式能够使用 Replit 构建者在其他所有方面都已熟练使用的对话式工作流。”

“Shopify 是这方面的行业标准，为各种规模的零售业务提供支持，”该公司写道。“之前缺少的是一种*为* Shopify 设计店面的方式，且这种方式能够使用 Replit 构建者在其他所有方面都已熟练使用的对话式工作流。”

事实上，Shopify 与氛围编程平台的合作已经扩展了一段时间，已经与 [Lovable 等平台](https://lovable.dev/shopify)、[v0 by Vercel](https://v0.app/) 以及 [Manus](https://manus.im/integrations/shopify-manus) 实现了集成。不过，对于 Replit 来说，Shopify 集成只是围绕变现这一更宏大图景中的一块拼图。

## 构建技术栈

Replit 在创作者变现工具方面的发力始于 4 月，[通过与 RevenueCat 的合作](https://thenewstack.io/replit-revenuecat-help-vibe-coders-monetize/)正式拉开帷幕。RevenueCat 是一个为超过 8 万个应用处理应用内购买和订阅的平台。

该集成允许 Replit 用户使用纯英文提示词向其移动应用添加订阅付费墙和定价层，而 RevenueCat 则在后台处理计费逻辑和应用商店合规事宜。对于首次进行开发的用户（其中许多人从未接触过苹果或谷歌的支付规则）而言，这极大地减少了摩擦。

![集成支付：Replit + RevenueCat](https://cdn.thenewstack.io/media/2026/04/6c4aa6f1-gif2.gif)

*集成支付：Replit + RevenueCat*

随后，在 5 月下旬，[迎来了与 Visa 的合作](https://thenewstack.io/replit-visa-ai-payments/)。Visa 对 Replit 进行了一笔未透露金额的战略投资，两家公司目前正致力于将 Visa 的支付基础设施直接嵌入到 Replit 的开发环境中。

该交易的核心是 Visa 的[可信智能体协议（Trusted Agent Protocol）](https://developer.visa.com/capabilities/trusted-agent-protocol)，这是一种加密身份层，可让商户实时验证 AI 智能体的身份和意图，从而允许智能体在规定的安全边界内代表用户进行交易。

该集成为开发者在智能体构建过程中原生提供了支付构建模块，包括代币化（Tokenization）、身份验证和钱包管理。长远愿景是，AI 智能体能够代表用户自主处理交易——例如更新软件许可证、支付供应商发票，或在数字钱包余额不足时进行充值——无需任何人工干预。

## 金融技术栈之外

简而言之，这三项集成的结合解决了同一个问题的不同层面。RevenueCat 涵盖了经常性收入——订阅、付费墙和定价层。Shopify 涵盖了实体和数字产品的销售。而与 Visa 的交易则更具前瞻性，为 AI 智能体自主进行交易奠定了基础。

> “这三项合作的结合解决了同一个问题的不同层面。”

Replit 表示，其长期野心是成为让任何人都能够在单次对话中完成从创意到运营业务全过程的平台。

然而，开发并变现一款应用是一回事，围绕它建立一家企业又是另一回事。Replit 正在组建的金融技术栈在原理上很好地覆盖了交易层，但运营一家公司更难的要素，如客户获取、营销、分发以及产品与市场匹配度（PMF），依然完全需要由构建者自己来解决。

不过，有迹象表明，Replit 也盯上了这块领地。除了构建应用，Replit [还允许用户构建和部署自主智能体](https://docs.replit.com/build/build-an-agent)——这是一种无需人工干预即可运行任务、连接外部服务并按计划运行的软件。[在 5 月的一次活动中](https://letsdatascience.com/news/replit-demonstrates-agents-powering-saastr-operations-f2652a5f)，SaaStr 展示了在 Replit 上构建的智能体，它们可以担任 AI 营销副总裁和 AI 客户成功副总裁——每月总共只需花费约 250 美元，即可处理赞助商管理、状态报告和客户回复。

Replit 自身也在朝这个方向迈进，推出了旨在处理传统上由专家担任的角色的专用智能体——这包括[全新的 Replit SEO 智能体](https://replit.com/blog/seo-agent)，其作用是扫描已发布的应用以寻找可发现性问题并自动应用修复。

目前，创办一家企业需要的不仅仅是一个提示词，但显而易见，Replit 正在努力弥合这一差距。