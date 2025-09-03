
<!--
title: Cloudflare的平衡术：保护内容，推进AI
cover: https://cdn.thenewstack.io/media/2025/09/9783e2cc-fellipe-ditadi-rvy2h0nm0-i-unsplashb.jpg
summary: Cloudflare 推出 NLWeb 和 AutoRAG，助力网站实现 AI 对话功能，同时探索内容创作者补偿机制，旨在平衡内容保护与 AI 发展。
-->

Cloudflare 推出 NLWeb 和 AutoRAG，助力网站实现 AI 对话功能，同时探索内容创作者补偿机制，旨在平衡内容保护与 AI 发展。

> 译自：[Cloudflare’s Balancing Act: Protect Content While Pushing AI](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/)
> 
> 作者：Richard MacManus

今年，Cloudflare 一直直言不讳地支持 AI 时代的网络内容创作者，他们不得不忍受 [LLM 提供商](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) 和 [AI 搜索引擎](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/) 对其内容的全面掠夺，更不用说网络用户的 [访问量日益减少](https://thenewstack.io/google-ai-overviews-and-citations-tips-for-web-publishers/) 了。几个月前，首席执行官 Matthew Prince 宣布 7 月 1 日为“[内容独立日](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)”，并要求谷歌、OpenAI 和 Anthropic 等公司为 AI 爬取向创作者提供补偿。

与此同时，Cloudflare 也在努力将 AI 集成到其内容交付平台中，希望能够惠及发布商。上周末，它 [宣布实施 NLWeb](https://blog.cloudflare.com/conversational-search-with-nlweb-and-autorag/)，这是一种新兴协议，使发布商能够将 AI 聊天集成到他们的网站中。

我们与 Cloudflare 的产品副总裁 William Allen 进行了交谈，了解该公司“让你的网站对人和代理都具有对话性”的目标。

Cloudflare 的倡议有两个方面。首先，[NLWeb](https://github.com/nlweb-ai/) 是微软在 5 月份宣布的一个开源项目，它被宣传为“有效地将你的网站变成一个 AI 应用程序”的一种方式。第二个关键技术是 [AutoRAG](https://developers.cloudflare.com/autorag/)，Cloudflare 的“托管检索引擎，[可以]自动抓取你的网站，将内容存储在 R2 中，并将其嵌入到托管向量数据库中。”

> “因此，当我们看到 [NLWeb] 宣布时，我们立即开始研究它，并说：好的，我们如何让 Cloudflare 客户更容易使用它。”
> 
> **William Allen, Cloudflare 产品副总裁**

Allen 告诉我，将 AutoRAG 视为一种扫描你的网站并将其放入向量数据库的方法，然后你可以使用 AI 模型搜索和与之交互。

AutoRAG 相当新——它在 [4 月份宣布](https://blog.cloudflare.com/introducing-autorag-on-cloudflare/) 为“完全托管的检索增强生成 (RAG) 管道”。 将其与 NLWeb 结合使用非常有意义，因为它允许网络发布商有效地向他们的网站添加自定义 AI 搜索机器人。

“NLWeb 和 AutoRAG 共同让发布商超越搜索框，使网站的对话式界面易于创建和部署，”NLWeb 的创建者兼微软技术研究员 R.V. Guha 在 Cloudflare 帖子的一份准备好的声明中说。

“因此，当我们看到它宣布时，”Allen 在谈到 NLWeb 时说，“我们立即开始研究它，并说：好的，我们如何让 Cloudflare 客户更容易地在他们自己的资产上自行实施它。”

## 是的，有 MCP

与当今几乎所有与 AI 和应用程序开发相关的事情一样，这里面也有一个 [MCP 组件](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)。“每个 NLWeb 实例也作为一个模型上下文协议 (MCP) 服务器运行，”Cloudflare 博客文章指出。我问 Allen 这是否意味着每个发布商都会获得他们自己的 MCP 服务器？

他回答说，NLWeb 为你提供了一个与你的网站进行对话的界面，“但它也带有这些可以通过 MCP 服务器使用的端点。” 他澄清说，是的，“这是一个特定于你的 NLWeb 实例的 MCP 端点。”

换句话说，外部应用程序可以通过该 MCP 连接访问你网站的内容。

## Cloudflare 希望扩展 NLWeb

该博客文章还指出，Cloudflare 正在“积极与微软合作扩展 [NLWeb] 标准，目标是让每个网站都像一个 AI 应用程序一样运行，以便用户和代理都可以自然地查询其内容。” 我问 Allen，Cloudflare 希望在哪些方面扩展该规范？

“采用可能是最大和最重要的事情，”他回答说。“确保它适用于我们所有的客户，能够让客户轻松地添加他们自己的品牌、他们自己的外观和感觉——因此需要一定程度的定制。”

此外，Cloudflare 希望他们的用户能够“无缝地引入你最喜欢的任何 AI 提供商，”Allen 说。

> Cloudflare 希望通过使 NLWeb“让客户轻松地添加他们自己的品牌、他们自己的外观和感觉”来扩展它。

虽然 NLWeb 确实具有很大的潜力（我曾与 Guha 讨论过它，但不幸的是，这是非公开的），但最近有人对其安全性提出了担忧。 上个月，[The Verge 报道](https://www.theverge.com/news/719617/microsoft-nlweb-security-flaw-agentic-web) 了 NLWeb 中的一个安全漏洞，该漏洞允许任何远程用户读取敏感文件。 虽然该漏洞已立即修复，但我问 Allen，Cloudflare 是否正在密切关注 NLWeb 的安全方面。

“当然，你看， [像] 很多这些事情一样，它在标准中还处于非常早期的阶段，”他回答说，并指出 MCP 是另一个正在迅速被采用的全新标准的例子。“当你考虑真正将这些东西投入生产时，你需要非常小心， […] 特别是你的内容。 因此，我们正在启动它，它是一个 beta 版，[并且] 开放标准的优点在于它是透明的、开放的。 其他人可以帮助检查漏洞并找到这些漏洞，然后任何人都可以在那里提交 PR，以确保如果存在漏洞，它会很快得到修补。”

## Cloudflare 的创作者补偿驱动力

扩大对话范围，我问 Allen，Cloudflare 首席执行官 Matthew Prince 在 7 月份的博客中提到的内容创作者补偿项目是否有任何进展？ Prince 一直在就此进行采访，包括上周 [与 Fred Vogelstein 的一次采访](https://crazystupidtech.com/2025/08/30/cloudflares-ceo-wants-to-save-the-web-from-ais-oligarchs-heres-why-his-plan-isnt-crazy/)，他在采访中提到了 Cloudflare 将成为中间人的内容市场。

“我们仍处于非常早期的阶段，”Allen 说。“我的意思是，我们有这种非常激进但简单的理念，即当你作为内容创作者将你的内容放在网上时，当你将你的网站连接到互联网时，你应该决定其他人如何将该内容用于商业目的，对吗？ 因此，你应该掌控一切。”

他指出，他们的一些客户正在利用 Cloudflare 的工具“进行执行方面”（即，阻止 AI 爬虫程序的内容），然后与各种 AI 公司达成自己的交易。

> “……通过我们对按爬取付费的早期实验，我们仍处于早期的私人 beta 阶段，与代理开发人员和其他 AI 公司以及发布商密切合作，以找到那里的适当平衡。”
> 
> **– Allen**

“然后在直接货币化方面，通过我们对按爬取付费的早期实验，我们仍处于早期的私人 beta 阶段，与代理开发人员和其他 AI 公司以及发布商密切合作，以找到那里的适当平衡。”

有趣的是，Cloudflare 似乎同样专注于为 AI 代理开发人员提供使用发布商内容的方式——当然，前提是他们获得许可。 因此，这不仅仅是保护网站和向其中添加 AI。 这也是向 AI 开发人员抛出橄榄枝（只要他们为这些橄榄枝上的肉付费）。

“如果你正在构建一个代理 […] 并且 [你] 想要为 [你的] 用户带来精彩的内容，我们 [Cloudflare] 如何让它变得简单？ 我们如何让你知道，嘿，这个特定的网站上有一些新的、更新的信息，你应该获得访问权限，并使其易于支付。”

因此，Cloudflare 在这里走了一条微妙的路线，试图支持内容创作者，同时也对 AI 技术对网络未来的潜在好处持开放态度。 NLWeb 计划就是这种平衡的一个很好的例子——它为网站发布商提供了一种新型的对话式搜索，同时（通过 MCP 连接）也为外部方访问他们的内容留下了机会。