<!--
title: 开发者向AI询问该用什么工具？我们是如何追踪答案的
cover: https://cdn.thenewstack.io/media/2026/10/a2231d4b-aakash-dhage-gjln1wb4wlw-unsplash.jpg
summary: 本文探讨了开发者如何通过AI智能体寻找开发工具，以Webflow为例详细分析了各大AI引擎在推荐CMS时的表现、数据追踪方法以及优化内容以适应AI检索的策略。
-->

本文探讨了开发者如何通过AI智能体寻找开发工具，以Webflow为例详细分析了各大AI引擎在推荐CMS时的表现、数据追踪方法以及优化内容以适应AI检索的策略。

> 译自：[Developers ask AI which tool to use. Here's how we track the answer.](https://thenewstack.io/tracking-ai-tool-recommendations/)
> 
> 作者：Luke Stahl

开发者会向 AI 询问应该使用哪个工具。以下是我们如何追踪答案的方法。

我们向 Claude 询问：“哪些 CMS 平台[支持 MCP 集成](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)？”它进行了网页搜索，并将 Webflow 列在第一组（具有托管 MCP 服务器的无头和 SaaS CMS 平台）的第六位，附带这样一行文字：“一个通过数据 API 管理站点的托管服务器，涵盖页面、组件、CMS 集合和条目、资产、表单以及发布。”

```

Which CMS platforms support MCP integration?

```

![Screenshot of claude response for the prompt "Which CMS platforms support MCP integration?"](https://cdn.thenewstack.io/media/2026/10/75848bbd-image3-1024x875.png)

我们向 Claude 四次提出了相同的问题。那一次是四次中最详细的，所以不要认为它是典型的。在四次回答中有三次，Webflow 都有它自己的要点说明。其中两次回答称该服务器适用于 CMS 集合和条目，另一次则仅表示它涵盖数据 API 和设计器。在第四次运行中，我们只是共享要点中的一个名字，且没有任何描述。在下文中，我们将统计引擎提及 Webflow 的频率。

我们提出这个问题是因为 AI 智能体已经是开发者查找信息的方式之一：在 [Stack Overflow 2026 开发者调查](https://survey.stackoverflow.co/2026)中，近 70% 的受访者表示他们使用 AI 智能体来帮助他们寻找答案。我们想看看当被问及该使用哪个工具时，这些智能体会说些什么。

## AI 为许多问题选出了首选答案

问 Claude 事务性电子邮件应该用什么，[Resend](https://resend.com/) 会排在第一位。问产品分析应该用什么，[PostHog](https://posthog.com/) 会排在第一位。我们没有关于有多少开发者会在第一个名字处停下脚步的数据，但我们宁愿出现在第一个答案中，也不愿默默无闻。

```

What should I use for transactional email?

```

![Screenshot of Claude's response to the prompt "What should I use for transactional email?"](https://cdn.thenewstack.io/media/2026/10/2f3f8a97-image6-1024x770.png)

```

What should I use for product analytics?

```

![Screenshot of Claude's response to the prompt "What should I use for product analytics?"](https://cdn.thenewstack.io/media/2026/10/fcedbcdc-image1-1024x823.png)

CMS 是我们关心的类别，“我需要为我的网站添加一个 CMS”是我们预期问题听起来的样子。我们运行了三次。Webflow 被推荐了一次，在其所在组中排在最后。在另外两次中，它是你可能已经在使用的示例，或者根本没有被提及。Sanity、Payload、WordPress 和 Ghost 在这三次中都出现了。我们的问题是，要成为该类别的默认选择需要付出什么，而我们首先从衡量我们目前所处的位置开始。

```

I need to add a CMS to my website.

```

![Screenshot of Claude response to "I need to add a CMS to my website."](https://cdn.thenewstack.io/media/2026/10/7175f1a4-image7-980x1024.png)

## 我们为什么要追踪它

我们密切关注一个提示词：“哪些 CMS 平台支持 MCP 集成？”在 9 月 25 日至 10 月 19 日期间，它运行了 100 次，在四个引擎中的每一个上运行 25 次。Webflow 在这 100 个响应中出现了 49 次，但不同引擎之间的差异很大，在 Perplexity 上是 25 次中出现 22 次，而在 Claude 上则是 25 次中出现 4 次。

> “当引擎将我们排除在外时，提问的开发者永远不会看到 Webflow，并且我们的网站分析中没有任何记录，因为在任何人访问页面之前问题就已经被回答了。”

当引擎将我们排除在外时，提问的开发者永远不会看到 Webflow，并且我们的网站分析中没有任何记录，因为在任何人访问页面之前问题就已经被回答了。我们没有将这些答案与注册或收入联系起来的引荐数据，因此我们并没有声称存在收入影响。我们可以衡量的是我们是否被提及、我们是如何被描述的，以及引擎使用了哪些来源。

## 我们如何追踪它

我们使用 [Webflow AEO](https://help.webflow.com/hc/en-us/articles/51703818404243-Webflow-AEO-overview)（位于 Insights > AEO 下）。Prompts 页面列出了每个被追踪的提示词及其主题、可见性得分、引用率以及与上周相比的变化。打开一个提示词会显示被追踪的响应数量、自有域和非自有域之间的引用拆分、按平台划分的引用率、被引用的我们的页面，以及你可以导出的响应日志。

![Screenshot of the Webflow AEO.](https://cdn.thenewstack.io/media/2026/10/14838c9f-image2-1024x591.png)

提及率是指 Webflow 在我们追踪的提示词中出现的频率。无论描述正确与否，它都会计算一次提及，因此我们也会对我们审查的响应进行四个维度的评分：是否命名了 Webflow、它被置于哪个层级（官方、社区或未列出）、描述是否准确，以及引擎使用了哪种类型的来源。仪表板的可见性得分在过去 30 天内显示为 47%。我们的 49/100 是指命名了 Webflow 的响应计数，因此这两个数字不会完全匹配。

我们正在从单一提示词转向表述群集。开发者不会输入相同的句子，因此我们将某种意图的几种表述组合成一个群集，并在每个引擎上重复运行每一个表述，然后报告该群集的比率和范围。

每个响应都成为我们日志中的一行。下面是一行的样子：

```

JSON
{
  "date": "2026-10-21",
  "engine": "Claude",
  "prompt": "Which CMS platforms support MCP integration?",
  "mentioned": true,
  "position": 6,
  "listed_total": 18,
  "section": "Site builders and hosted platforms",
  "tier": null,
  "accurate": null,
  "cited_sources": [
    "sanity.io",
    "developersdigest.tech",
    "strapi.io",
    "crox.io",
    "themeisle.com",
    "magazine.joomla.org"
  ]
}

```

我们将 `accurate` 留空，直到有人对照我们的文档检查该描述，这可以防止听起来很自信的回答被算作正确回答。这里的 `tier` 是空的，因为回答从未将 Webflow 标记为官方或社区。

## 四个引擎是怎么说的

这些是 AEO 在同一个早晨追踪到的响应，原话引用。

Claude 在“网站构建器 / 电子商务 CMS”下给 Webflow 了一行：“拥有一个支持 OAuth 的官方[远程 MCP 服务器](https://thenewstack.io/mcp-release-candidate-rewrite/)”，并在被“普遍认为拥有最成熟官方实现”的平台总结中命名了它。这个回答很短，其背后的来源都不是我们的。正如上面四次运行所示，Claude 的回答每次运行都会改变。

ChatGPT 为 Webflow 提供了它自己的专属部分。它将我们标记为“MCP Support: Official”，并表示“Webflow 提供托管的 MCP server”，列出了它可以做什么，并补充说“Webflow MCP 可在其所有 Site 计划中使用，包括免费的 Starter 计划”。它的引用是 [help.webflow.com](https://help.webflow.com/hc/en-us/articles/52536562285203-Webflow-MCP-server-overview)。

![ChatGPT's section for Webflow, labeled "MCP Support: Official."](https://cdn.thenewstack.io/media/2026/10/9e81ede4-image5-1024x456.png)

Gemini 表示 Webflow “可以与 MCP 服务器集成（通常用于 Cursor 等氛围编程环境中）以读取架构、生成集合并自动化数据导入或迁移工作流”。这被解读为第三方集成，而不是我们运送的服务器，它位于 Gemini 的第二层“具有强模块、宿主或社区支持的 CMS 平台”中。它的 14 个引用中没有一个是我们的。

![Gemini's section for Webflow.](https://cdn.thenewstack.io/media/2026/10/7b128075-image8-1024x680.png)

Perplexity 在其开篇列表中命名了 Webflow，并在细分中给出了简短的一行：“MCP 目录中列出了 MCP 服务器”，并指向了一个第三方 MCP 目录 machalliance.org。

![Perplexity's opening list for CMS platforms which support MCP integration, which included Webflow.](https://cdn.thenewstack.io/media/2026/10/4f2b4d5a-image9-950x1024.png)

Webflow 的 MCP 服务器由 Webflow 构建，并且[通过 OAuth 远程运行](https://developers.webflow.com/mcp/reference/how-it-works)，因此那天早上 Claude 和 ChatGPT 的分层是正确的，Gemini 是错误的，而 Perplexity 没有说明。

## 数据显示了什么

在 9 月 25 日至 10 月 19 日期间，Webflow 在对该提示词的 100 个响应中被命名了 49 次。按引擎划分，Perplexity 是 25 分之 22，ChatGPT 是 15，Gemini 是 8，Claude 是 4。Perplexity 的数字最高，但它的回答是四者中最单薄的，因此提及和好回答并不完全是一回事。Claude 命名我们的次数最少，而我们引用的回答是准确的。

> “被提及对我们来说是容易的部分。从我们自己的页面获得正确的描述，才是我们能够影响的部分。”

来源的分配情况也是如此。在 10 月 19 日的响应中，ChatGPT 引用了它列出的每个平台的供应商文档。其他三个引擎则将供应商博客与第三方指南和目录混合在一起。llmcms.org 上的一个指南出现在 100 个响应中 60 个的引用里，而 Webflow 页面（webflow.com、help.webflow.com 或 developers.webflow.com）仅被引用了 6 次，全部来自 ChatGPT 或 Gemini。

被提及对我们来说是容易的部分。从我们自己的页面获得正确的描述，才是我们能够影响的部分。

## 局限性

答案会随着每次运行以及提示词的措辞而改变，因此我们使用上面的单个响应作为示例，使用 100 个响应来计算比率。第一部分中的四次运行是我们自己手动运行的，不属于这 100 次之内。我们手动运行命名 Webflow 的频率高于 AEO 为 Claude 追踪的响应，而我们尚不知道原因。提及率也没有说明准确性，这就是为什么我们要对此进行单独评分。

仪表板将 webflow.com 计算为我们唯一的自有域，因为 [help.webflow.com](https://help.webflow.com/hc/en-us) 和 [developers.webflow.com](https://developers.webflow.com/) 位于不同的项目中。因此，这里的引用份额仅涵盖 webflow.com，提及率不受影响。我们的观点是，这首先是一个认知和文档问题。我们并不声称它能推动收入，在拥有显示这一点的引荐数据之前，我们也不会这么说。

## 你能对此做些什么

下面的每个步骤都映射到我们数据中的某些内容，你可以在你自己的产品上运行所有这些步骤。

**确保引擎可以访问你的文档。** 在你更改任何内容之前，请检查 AI 爬虫是否可以获取它。这会发送带有爬虫用户代理的请求并打印状态行：

```

Shell
curl -sI -A "GPTBot" https://your-docs-site.com | head -n 1

```

为每个爬虫的用户代理重复此操作，然后读取 robots.txt 以及你的 CDN 或防火墙规则，看看是否有任何阻止它们的规则。

**用引擎搜索的词汇来表达。** 我们的 [MCP 文档](https://developers.webflow.com/mcp/reference/overview)指出该服务器[远程运行并使用 OAuth](https://developers.webflow.com/mcp/reference/how-it-works)。我们检查的页面没有说“官方的”或“托管的”，而这些正是引擎答案中的词汇。在主文档页面的顶部放置一个简短的回答块，说明该东西是什么、谁构建的、它如何进行身份验证以及它的成本是多少。例如：“Webflow MCP 服务器是由 Webflow 构建的官方托管服务器。它使用 OAuth 并在所有 Site 计划中可用，包括免费的 Starter 计划。”

**编写汇总所总结的内容。** llmcms.org 上的一份第三方指南出现在我们 100 个响应中 60 个的引用里。阅读引擎引用的指南对你的评价，并修复你自己的文档中的空白，以便下一个总结从你的页面开始。

**在引擎引用的汇总中被提及。** 引擎严重依赖第三方指南和目录，Perplexity 关于我们的一行文字指向了一个第三方 MCP 目录。找到引擎为你所在类别引用的指南和目录，让你的产品在那里被列出或纠正。

**让智能体易于阅读文档。** 我们的 MCP 文档指出，你可以将 [.md 或 /llms.txt](https://thenewstack.io/docsy-linux-foundation-agents/) 追加到页面 URL。检查你的文档是否返回纯文本，版本化 URL 是否指向一个规范页面，以及哪些页面带有 JSON-LD：

```

Shell
curl -s https://your-docs-site.com/page | grep -c 'application/ld+json'

```

以下是在我们的 MCP 概述页面上运行的两项检查：

![Screenshot of checks run on Webflow's MCP overview page.](https://cdn.thenewstack.io/media/2026/10/cff7ffdb-image4-1024x244.png)

200 意味着该页面响应了 GPTBot 请求。数字 1 意味着 HTML 具有至少一个 JSON-LD 标签。0 意味着它没有任何标签，除非脚本在页面加载后添加了它。

**计算你拥有的每一个域。** 如果你的文档位于子域上，请检查你的追踪是否将其视为你的域。

如果你想了解你的团队在所有这些方面的表现，我们的[AEO 成熟度模型](https://webflow.com/blog/aeo-maturity-model)对内容、技术设置、权威性和衡量标准进行了评级。

## 为智能体构建

你的文档现在有两个读者：开发者，以及为他们工作的智能体。对于第二个读者，四个选择最为重要。

**编写工具描述，就像它们是产品本身一样。** 智能体会根据其描述来选择 MCP 工具。“获取用户”对它没有任何帮助。说明该工具做什么、何时使用它、它返回什么以及当没有结果时会发生什么。智能体只能看到描述、架构和先前的响应。当我们发现端点包装器制作成糟糕的 MCP 工具时，我们[围绕基于意图的工具重建了我们的工具](https://webflow.com/blog/designing-apis-for-agents)。

> “你的文档现在有两个读者：开发者，以及为他们工作的智能体。”

**发布对特定问题的回答。** 引擎引用最多的指南在单页上列出了每个平台及其支持的内容。一个准确说明你的服务器涵盖哪些操作、范围和计划的页面，可以为引擎提供引用的内容。

**保持规范最新。** 过时的 OpenAPI 规范破坏智能体的方式与过时的文档破坏人的方式相同，因此在与 API 更改相同的拉取请求（PR）中更新文档。

**给予智能体最小的权限。** 使用有范围限制的密钥和 OAuth，以便智能体做的事情不超过代表它的用户。我们的 [MCP 服务器使用 OAuth](https://developers.webflow.com/mcp/reference/how-it-works)。

## 我们接下来要衡量的指标

我们的基线是上面的数字：按引擎划分的提及率、按引擎划分的准确性以及来源类型。我们将在四到六周内重新运行相同的提示词，并报告范围，而不是单一数字。结果尚未出来，所以我们不能说这些修复中哪一个会改变数字，有些可能不会。

## 在你自己的产品上运行它

选择五个用通俗语言编写的提示词，并在 ChatGPT、Claude、Gemini 和 Perplexity 上分别运行。这些是我们在本文中使用的提示词，并且该模式很容易适应：

* 事务性电子邮件应该用什么？
* 产品分析应该用什么？
* 我需要为我的网站添加一个 CMS。
* 哪些 [类别] 工具支持 [你关心的集成]？
* [你的产品] 与 [竞争对手]，我该选哪个？

使用上面架构中的字段记录每个答案，并在更改任何内容之前写下基线。如果你被命名了，请对照你自己的文档检查层级和描述。如果没有，请查看引擎引用的页面。然后在魔术一个月后再次运行相同的提示词。

如果你不想手动运行此操作，[Webflow AEO](https://webflow.com/solutions/aeo) 会为你追踪提示词（适用于企业版），并且该页面提供对你网站的免费 AEO 评估。

*本文最初于 2026 年 10 月 28 日发布在 [webflow.com](https://webflow.com/blog/track-mcp-ai-visibility)。*