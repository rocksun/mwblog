不满足于用[低成本模型](https://thenewstack.io/deepseek-flash-pro-benchmark/)挑战主流前沿AI实验室，中国AI公司[DeepSeek](https://deepseek.com/)正将目光投向搜索API市场。

周六，该公司宣布通过两个新的API——[Search 和 Fetch](https://api-docs.deepseek.com/guides/search/)，[向外部开发者开放](https://api-docs.deepseek.com/updates/#date-2026-10-17)其内部开发的搜索引擎，允许开发者检索实时网页搜索结果和网页内容，以便在他们自己的应用和智能体中使用。

这两项服务的定价均为每 1,000 次成功请求 0.75 美元，开发者可以独立于 DeepSeek 的 AI 模型使用它们。

此次发布还伴随着 [DeepSeek-V4.1-Flash-1017](https://api-docs.deepseek.com/news/news261017/)，这是该公司[在 9 月份](https://venturebeat.com/technology/deepseek-v4-1-flash-debuts-with-0-003-1m-off-peak-cached-input-rate-and-benchmarks-eclipsing-gpt-5-6-sol-claude-opus-5)发布的 V4.1 Flash 模型的微小更新。

## 为什么 AI 智能体需要网络搜索

大型语言模型 (LLM) 接受过截至某个时间点的训练数据的训练，这意味着它们并不总能回答有关近期事件、更新的文档或任何其他类型的动态信息的问题。通过支持实时网络搜索，模型可以从互联网检索当前信息，从而补充其响应。

对于构建 AI 智能体的开发者来说，这一点尤为重要。例如，一个编码智能体可能需要查阅最新的软件文档、调查最近披露的漏洞，或者以其他方式检查特定库是否已更新。

到目前为止，使用 DeepSeek 模型的开发者有几种方法来提供此功能。他们可以将应用程序连接到第三方搜索服务，或者通过其模型 API 使用 DeepSeek 现有的搜索功能。

事实上，当 DeepSeek [在 8 月份开源其智能体套件（agent harness）](https://thenewstack.io/deepseek-harness-open-source-plugins/)时，它就在其功能中包含了网络搜索。该套件支持可互换的搜索提供商，包括 [Exa](https://exa.ai/)、[Perplexity](https://thenewstack.io/perplexity-agent-api/) 以及 DeepSeek 本身。然而，根据套件文档，通过该套件访问 DeepSeek 的原生搜索需要额外的模型请求，每次搜索都作为对 DeepSeek 模型的单独调用运行，这引入了额外的延迟和 Token 成本。

这些新 API 旨在简化该过程。开发者现在可以直接调用 DeepSeek 的 Search 端点来检索排好序的网页结果（包括标题、URL、片段和摘要），而 Fetch 端点则以 Markdown 格式检索单个网页的内容。

> “两者都不需要单独的模型请求，这意味着开发者也可以将 DeepSeek 的搜索功能集成到由竞争对手的 AI 模型驱动的应用程序中。”

两者都不需要单独的模型请求，这意味着开发者也可以将 DeepSeek 的搜索功能集成到由竞争对手的 AI 模型驱动的应用程序中。

## DeepSeek 开发自研引擎

在过去两年中的大部分时间里，DeepSeek 一直依赖外部提供商来提供网络搜索支持，尽管它当时也在构建自己的搜索引擎。

作为背景，2025 年 3 月，中国商业出版物《每日经济新闻》[报道称](https://www.nbd.com.cn/articles/2025-03-07/3779901.html)，DeepSeek 已集成总部位于杭州的中国 AI 搜索初创公司[博查 (Bocha)](https://bochaai.com/) 的搜索 API。博查的 CTO 翁柔颖指出，在当年该聊天机器人爆发式流行之前，DeepSeek 就一直在使用他们的服务。

与此同时，DeepSeek 自己的[2025 年 2 月隐私政策](https://web.archive.org/web/20261004083012/https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy-2025-02-14.html)也承认其对第三方搜索服务的依赖，并点名微软的 Bing 作为外部 API 提供商的一个例子。

> “在幕后，该公司也一直在为其自身的搜索基础设施奠定基础。”

在幕后，该公司也一直在为其自身的搜索基础设施奠定基础。今年 1 月，彭博社[报道称](https://www.bloomberg.com/news/articles/2026-01-29/deepseek-sets-sights-on-ai-search-and-agents-job-postings-show?utm_source=chatgpt.com)，根据该公司发布的招聘广告，DeepSeek 正在招募工程师来构建多语言 AI 搜索引擎。据报道，其计划中的功能超出了文本搜索的范围，还包括图像和音频。

快进大约九个月后，该公司表示其内部开发的、被称为 DeepSeek Search 的搜索引擎已经每天处理数亿次请求，并维护着一个包含数千亿网页的索引。

根据其[10 月 17 日的更新日志](https://api-docs.deepseek.com/updates/#date-2026-10-17)，该引擎支持多语言搜索，并使用旨在识别搜索垃圾信息、低质量 AI 生成材料以及操纵搜索排名企图的过滤机制。

DeepSeek 相对较少透露其底层架构，或者它是如何构建和维护其索引的。目前也不清楚该公司是否已全面完全替换了其外部搜索供应商。

## AI 搜索市场不断增长

构建搜索引擎绝非易事。它需要具备抓取网页、维护内容索引并对结果进行排 ranked 的基础设施，同时还要随着网络的改变而不断更新这些信息。多年来，这意味着那些为其应用程序想要原始搜索结果的开发者主要转向谷歌和微软这两家拥有自身网络规模索引的公司。

然而，现在越来越多的公司正在投资于它们自己的搜索基础设施，且越来越明确地以 AI 应用和智能体为目标。[Brave](https://brave.com/) 运营着[一个独立索引](https://brave.com/blog/most-powerful-search-api-for-ai/)，包含超过 400 亿个网页，该公司表示这是通过其自身的网络爬虫和其他发现机制维护的。与此同时，AI 搜索公司 Exa 也[开发了自己的爬虫和索引基础设施](https://exa.ai/blog/how-to-build-nextgen-search)。

Perplexity 同样[投资了专有搜索基础设施](https://thenewstack.io/perplexity-agent-api/)，包括构建自己的[抓取和索引系统](https://www.perplexity.ai/en-GB/hub/blog/architecting-and-evaluating-an-ai-first-search-api)。另一个竞争对手 [Parallel](https://parallel.ai/products/search) 表示，它从头开始构建了其搜索基础设施，包括爬虫、索引、查询处理和排序组件。

Cloudflare 也正从另一个角度进入该市场。本月初，[该公司通过其 AI 网关推出了网络搜索 API](https://blog.cloudflare.com/introducing-web-search-api/)，允许开发者通过单一界面访问来自多个提供商的搜索结果。该服务目前处于测试阶段，[使用 Ceramic 作为其默认提供商](https://developers.cloudflare.com/web-search/providers/)，并按每个提供商公布的 API 费率向客户收费，不加收额外费用。

> “就 DeepSeek 而言，它在价格上与现有巨头展开了激烈的竞争。”

就 DeepSeek 而言，它在价格上与现有巨头展开了激烈的竞争，尽管它严格来说并不是最便宜的选择。[Ceramic.ai](https://www.ceramic.ai/) 为 AI 智能体提供基于关键词的网络搜索，在其即用即付计划中[按每 1,000 次查询 0.2,5 美元收费](https://www.ceramic.ai/pricing)。

尽管如此，DeepSeek 每 1,000 次成功搜索 0.75 美元的价格与许多其他公司相比非常有优势，包括 [Parallel 的 Turbo 和 Fast 搜索服务](https://parallel.ai/pricing)以及 [Perplexity 的 Fast Search API](https://docs.perplexity.ai/docs/getting-started/pricing)，这两者的收费都是每 1,000 次搜索 1 美元。同时，Exa [对每 1,000 次即时搜索请求收费 4 美元](https://exa.ai/pricing#endpoint-pricing)，而 Brave 收费[每 1,000 次搜索 5 美元](https://brave.com/search/api/)。其他值得注意的玩家包括 [Tavily](https://www.tavily.com/)（一家面向 AI 智能体的搜索 API 提供商，欧洲 AI 基础设施公司 [Nebius 于 2 月收购了该公司](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform)）。Tavily 在其即用即付计划中[收费](https://www.tavily.com/pricing)每 1,000 次基础搜索 8 美元。

值得注意的是，各种服务在检索能力、结果限制和性能方面有所不同，因此价格不一定完全具有可比性。但它们为 DeepSeek 进军搜索基础设施空间提供了一些有用的基准。

这些替代方案的出现正值谷歌和微软撤下长期存在的搜索 API 产品之际。微软在 2025 年 8 月退役了其 Bing 搜索 API，而谷歌也[对其自定义搜索 JSON API 关闭了新客户的接入](https://developers.google.com/custom-search/v1/overview)，现有用户必须在 2027 年 1 月 1 日之前完成迁移。这两家公司继续通过各自的 AI 平台提供搜索功能，包括面向 Gemini 的 [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/google-search) 以及面向微软 Foundry 智能体的 [Grounding with Bing Search](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools?pivots=python)。这些服务允许在其各自平台内运行的 AI 模型检索网络信息并生成带有引用的答案。

诸如 DeepSeek 的独立 API 为开发者提供了对搜索结果的直接访问权限，他们可以将其与自己选择的 AI 模型和应用程序配合使用。

## 开发者反应与细节

这一宣布在开发者中引发了关于定价的大量讨论，以及这些新 API 是否能提供超越现有搜索集成之外的更多价值。在 Reddit 上，一位用户对价格表示欢迎：“我认为没有任何其他搜索提供商能接近 DeepSeek 提供的价格，”他们[写道](https://www.reddit.com/r/DeepSeek/comments/1x8d4u2/comment/phdnk6n/)。

其他人则质疑这一宣布最终会为那些已经通过第三方工具访问网络搜索的用户带来什么改变。一位 Reddit 用户[指出他们已经在将](https://www.reddit.com/r/DeepSeek/comments/1x8d4u2/comment/phcazlt/) DeepSeek 与可以搜索网络的 [Hermes AI 智能体](https://thenewstack.io/openclaw-hermes-agent-harness/)配合使用。另一位用户回应说，那些已经配置了自己的搜索工具的人可能从新 API 中看不到太多直接的好处。

类似的讨论也出现在 [Hacker News 上](https://news.ycombinator.com/item?id=50138531)，一位开发者在那里[质疑](https://news.ycombinator.com/item?id=50139399)在有诸如 [SearXNG](https://github.com/searxng/searxng) 等免费、自托管替代方案可用时，为什么还需要付费搜索 API。另一位评论者辩称，企业[有额外的要求](https://news.ycombinator.com/item?id=50139481)，并列举了“可靠的延迟、数据处理保证”以及通过搜索查询暴露敏感公司信息的潜在风险。

对于权衡 DeepSeek API 的企业来说，最后一点具有额外的维度。DeepSeek 的[隐私政策](https://github.com/OpenTermsArchive/genai-eu-versions/blob/main/DeepSeek/Privacy%20Policy.md)指出，它在中国收集、处理和存储个人数据，并且通常会保留用户输入，直至账户保持开放状态。然而，Search 和 Fetch 的文档并未说明具体保留搜索查询的时长。

这些讨论突显了个别开发者和企业在成本、可靠性和处理大量请求时的不同需求。虽然 DeepSeek 的定价无疑具有竞争力，但也有一些值得考虑的实际限制。

根据其[API 文档](https://api-docs.deepseek.com/guides/search/)，Search 和 Fetch 请求各自被限制为每个账户每秒五个，尽管单个搜索可以返回多达 50 个结果而不会增加请求价格。DeepSeek 也仅对返回结果的请求计费，因此失败的调用、空搜索和超时都是免费的。

DeepSeek 暂时免除了通过 DeepSeek Harness、Claude Code 和 Codex 在使用其 API 时发起的服务端工具调用的 Search 和 Fetch 费用。然而，这在很大程度上是一项临时安排，将于 10 月 31 日结束，届时标准的按请求计费将生效。根据 DeepSeek 的公告，对独立 API 的直接调用已经是计费的。