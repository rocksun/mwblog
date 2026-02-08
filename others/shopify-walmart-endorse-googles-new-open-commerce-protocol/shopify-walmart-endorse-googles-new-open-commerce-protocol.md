<!--
title: Shopify、沃尔玛力挺谷歌开放商务协议
cover: https://cdn.thenewstack.io/media/2026/01/9af8dd64-ucp.png
summary: 谷歌发布通用商务协议UCP，开放标准，简化AI购物体验。Shopify、Walmart等多家零售商和支付公司支持，旨在推动零售AI协议统一，挑战亚马逊等竞争对手。
-->

谷歌发布通用商务协议UCP，开放标准，简化AI购物体验。Shopify、Walmart等多家零售商和支付公司支持，旨在推动零售AI协议统一，挑战亚马逊等竞争对手。

> 译自：[Shopify, Walmart Endorse Google's New Open Commerce Protocol](https://thenewstack.io/shopify-walmart-endorse-googles-new-open-commerce-protocol/)
> 
> 作者：Steven J. Vaughan-Nichols

零售AI协议标准战日趋白热化。

[谷歌](https://cloud.google.com/?utm_content=inline+mention) 公布了一项新的开放标准——基于 Apache 2 开源许可的[通用商务协议 (UCP)](https://ucp.dev/)。

谷歌的目标是让 UCP 将 AI 驱动的产品发现转化为在其搜索和 Gemini 软件堆栈中实现无摩擦的即时购买。作为“代理商务”的核心管道，[UCP 旨在使 AI 代理](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/)、零售平台和支付提供商能够进行交易，而无需目前导致在线购物碎片化的定制、一次性集成。

在曼哈顿举行的[全国零售联合会 (NRF) 会议](https://nrfbigshow.nrf.com/)上，谷歌将 UCP 介绍为一种开放、可扩展的协议，它为从发现到售后支持的整个购物过程中的代理和商务系统建立了通用语言。

谷歌表示，在其初期部署中，UCP 将很快为搜索的 AI 模式和 [Gemini 应用](https://thenewstack.io/googles-new-gemini-3-flash-rivals-frontier-models-at-a-fraction-of-the-cost/)中的合格产品列表提供原生结账流程，最初面向美国零售商。

## UCP 实现的全新无摩擦购物流程

这远不止是谷歌的单方面行动。谷歌表示，UCP 已得到零售和支付领域 20 多家公司的共同开发和认可，其中包括 [在协议开发中发挥了重要作用](https://www.shopify.com/news/ai-commerce-at-scale)的 Shopify，以及 Etsy、Wayfair、Target、Walmart、Visa 等公司。

新的流程允许用户从会话式查询（例如，要求 Gemini 查找轻便的随身行李箱）直接在同一界面内完成购买，使用通过 Google Pay 存储的支付和配送详情，并“即将支持”PayPal。

谷歌将此定位为一种减少购物车遗弃的方法，同时让零售商作为登记商家保持控制权，包括拥有客户数据和关系。

沃尔玛则全力以赴。沃尔玛总裁兼首席执行官 John Furner 在一份声明中表示：“从传统的网络或应用搜索到代理主导的商务的转变代表着[零售业的下一次重大演变](https://corporate.walmart.com/news/2026/01/11/walmart-and-google-turn-ai-discovery-into-effortless-shopping-experiences)。我们不仅仅是旁观这种转变，我们正在推动它。”

Shopify [发布了自己对该协议的技术说明](https://www.shopify.com/news/ai-commerce-at-scale)，将其描述为允许任何 AI 代理与[其平台](https://thenewstack.io/shopify-announces-biannual-product-and-dev-tool-rollouts/)上的任何商家进行交易。它通过发现和调用商家定义的功能来实现这一点，而不是依赖紧密耦合的集成。

## UCP 作为商家能力的模块化标准

在商业方面，UCP 被呈现为一个模块化、可扩展的标准，商家可以使用它来声明他们支持的功能（如结账、退货或会员），并允许代理动态发现和协商这些功能。UCP 定义了代理、应用程序、企业和支付提供商如何一致地进行身份验证、交换功能和执行交易，而不是为每个代理或平台编写定制的 API。

UCP 通过位于 [Linux 基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention)的 [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) 和 Anthropic 的 [模型上下文协议 (MCP)](https://thenewstack.io/what-is-mcp-game-changer-or-just-more-hype/) 堆栈之上来实现这一点；它标准化了商务工作流程本身。同时，[A2A](https://thenewstack.io/most-developers-call-ai-data-with-apis-and-a2a/) 处理代理到代理的消息传递，而 MCP 则侧重于模型如何访问工具和数据。

因此，UCP 使用 A2A 和 MCP 而非取代它们，为代理提供了一种跨界面执行购物车、结账和售后流程的一致方式。简而言之，UCP 可以将 A2A 视为代理之间的传输和协调层，并将 [MCP](https://thenewstack.io/goodbye-plugins-mcp-is-becoming-the-universal-interface-for-ai/) 视为代理用来获取推动 UCP 工作流程所需的商务数据的机制。

## UCP 的技术架构和网络标准

在底层，UCP 实现依赖于熟悉的网络标准，例如用于账户关联结账的 OAuth 2.0、用于会话创建和完成的表述性状态传输 (REST) 端点以及用于保护卡数据的标记化支付。如果你在本十年从事过零售软件工作，你就会知道这些操作。UCP 电子商务工作流程可以通过 REST、MCP 或 A2A 实现。

大型在线零售商和大型超市的认可为谷歌提供了该标准的早期推广。但该公司也在吸引大量的开发者。它通过开源治理模型和开放规范来实现这一点。鼓励开发者试验结账、嵌入式定制流程和售后更新等功能，并通过 [UCP GitHub 讨论和拉取请求](https://github.com/Universal-Commerce-Protocol/ucp)参与。

在短期内，零售商若要使用谷歌的前端，商家必须拥有一个活跃的 [Google Merchant Center](https://merchants.google.com/) 账户和合格的产品 Feed，然后才能参与由 UCP 提供支持的结账。一旦获得批准，商家需要实现一小组核心 REST 端点来创建、更新和完成结账会话，并可选择嵌入式结账以获得更复杂或高度定制的用户体验。

零售商可以选择访客结账（无需额外身份验证）或账户关联结账，后者使用 [OAuth 2.0](https://thenewstack.io/oauth-2-0-a-standard-in-name-only/) 在其系统和参与代理之间同步个人资料和订单历史记录。订单状态变化通过 Webhook 推送回代理，从而使跟踪、退货和订阅管理等售后支持场景能够通过相同的协议进行。

## UCP 与代理支付协议的对比

谷歌还有另一个电子商务 AI 协议：[代理支付协议 (AP2)](https://ap2-protocol.org/)。区别在于 UCP 是完整的商务工作流程层，而 AP2 是 UCP 可以接入的支付授权层。UCP 编排整个购物旅程，而 AP2 则专注于代理如何发起、证明和结算支付。

UCP 的发布正值谷歌进一步深入 AI 主导的对话式商务，将该协议与“商务代理”等新工具捆绑在一起，后者允许品牌将自己的声音和策略嵌入到谷歌平台上的代理购物体验中。[Google Cloud 也将此举视为更广泛的“代理商务”战略的一部分](https://cloud.google.com/transform/a-new-era-agentic-commerce-retail-ai)。谷歌押注，随着零售商部署自己的代理以及来自不同供应商的消费 AI，标准化、可互操作的协议将是必不可少的。

## AI 商务协议的竞争格局

当然，谷歌并非唯一一家押注于此的公司。其竞争对手包括 [OpenAI 和 Stripe 的代理商务协议 (ACP)](https://developers.openai.com/commerce/) 以及 [ChatGPT 的即时结账](https://chatgpt.com/merchants/)。亚马逊当然通过其紧密耦合、仅限亚马逊的封闭系统代理购物和支付基础设施成为事实上的竞争对手。

谁将获胜？现在下结论还为时过早。然而，谷歌广告（占据所有数字广告支出的约 39%-40%）、重要的在线零售商合作伙伴关系和开源的结合具有强大的潜力。零售业的巨头亚马逊，可能多年来首次在谷歌 UCP 联盟中面临真正的挑战者。