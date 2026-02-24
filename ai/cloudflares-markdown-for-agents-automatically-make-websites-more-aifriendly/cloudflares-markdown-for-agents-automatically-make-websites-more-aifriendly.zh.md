[Cloudflare](https://www.cloudflare.com/)，这家备受推崇的安全和内容分发网络公司，推出了一项名为“[适用于代理的 Markdown](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)”的新功能，它可以在AI代理请求网页时，自动将网页从HTML转换为Markdown——将token使用量削减高达80%。

为什么？大型语言模型（LLM）不能读取HTML吗？当然可以，但从模型的角度来看，HTML是昂贵的噪音。

典型的网页包含诸如div等HTML格式，以及脚本和其他负载，所有这些都变成了模型必须“付费”读取的token。LLM根本不在乎文本周围的这些标记。最终，这只会消耗额外的token。

情况有多糟？Cloudflare自己宣布这一消息的博客文章，如果以HTML形式呈现，将达到16,180个token。而使用Markdown，则只需3,150个token。这节省了80%的token使用量。这是推理成本上的实际节省。

## 从HTML到Markdown

Cloudflare通过在边缘实时进行HTML到Markdown的转换来处理这个问题，适用于任何启用了“适用于代理的 Markdown”功能的网站。当客户端包含一个`Accept: text/markdown header`时，[Cloudflare会从源站获取原始HTML，将其转换为Markdown](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/)，并提供转换后的内容，而不是完整的网页标记。该公司表示，像[Claude Code](https://code.claude.com/docs/en/overview)和[OpenCode](https://opencode.ai/)等流行的编码代理已经发送这些头部信息，这意味着许多现有的AI工具可以立即利用这一功能。

为了使内容更易于机器处理，Cloudflare添加了一个`x-markdown-tokens`响应头部，它暴露了token计数，允许代理确定文档是否适合其上下文窗口或是否必须分块。转换后的响应还包括一个`content-signal`头部（`ai-train=yes, search=yes, ai-input=yes`），表明发布者默认允许AI训练、搜索索引和代理使用。

Cloudflare表示，未来的版本将允许网站所有者在当前默认设置之外，自定义这些内容信号策略。

![](https://cdn.thenewstack.io/media/2026/02/698c144a-cloudflare-markdown-headers.png)

Cloudflare对Markdown请求的响应（图片来源：Cloudflare）。

“适用于代理的 Markdown”依赖于标准HTTP内容协商，使用Accept头部来区分人类流量和AI爬虫或其他纯文本客户端。AI代理可以通过发送`Accept: text/markdown`（通常与text/html一起）来请求Markdown，而常规浏览器访问则继续接收正常的HTML页面。Cloudflare的边缘“即时”执行转换，无需对站点模板、CMS设置或单独的Markdown端点进行任何更改。

## 开始使用

Cloudflare的Pro和Business计划客户可以在Cloudflare仪表板的AI Crawl Control部分启用此功能，其中“适用于代理的 Markdown”显示为一个专用开关。通过Cloudflare API也可以使用相同的功能。

对于使用[Cloudflare for SaaS](https://www.cloudflare.com/saas/)的SaaS提供商，可以通过仪表板“快速操作”开关为所有自定义主机名开启Markdown转换，或者使用自定义元数据和配置为每个主机名选择性启用。

Cloudflare将Markdown定位为AI代理的事实上的通用语。Cloudflare远不是唯一一家发现为代理和机器学习使用Markdown优势的公司。

## Markdown替代方案

例如，荷兰互联网企业家和[WordPress](https://wordpress.org/)开发者Joost de Valk拥有一个[WordPress](https://wordpress.org/)插件“[Markdown Alternate](https://github.com/progressplanner/markdown-alternate)”，它也适用于代理。他写道，他的方法和Cloudflare可以协同工作。“一个WordPress网站可以[使用Markdown Alternate进行丰富的、支持WordPress的Markdown，带有专用URL](https://joost.blog/markdown-alternate/)和完整的元数据，而Cloudflare的功能则为网络上的其他所有网站提供了基线。该插件为您提供控制和深度；Cloudflare为您提供广度和零工作量。”

还有更直接的竞争程序，例如[Fasterize EdgeSEO（AI机器人的Markdown）](https://www.fasterize.com/en/blog/ai-bots-seo-why-converting-your-html-pages-to-markdown-could-change-the-game/)。这是一个边缘服务，可以为已知的AI机器人动态地将HTML页面转换为Markdown，而无需单独的.md URL。在这个领域，Cloudflare的另一个竞争对手是[Firecrawl](https://www.firecrawl.dev/)。这是一种商业“AI网络数据API”，它为LLM使用抓取、刮取和标准化网站。

对于构建消耗网络内容的AI驱动工作流的团队来说，某种形式的HTML到Markdown转换正迅速成为必需品。Cloudflare的边缘原生方法降低了进入门槛：网站所有者只需轻拨开关，每个页面即可为代理所用。