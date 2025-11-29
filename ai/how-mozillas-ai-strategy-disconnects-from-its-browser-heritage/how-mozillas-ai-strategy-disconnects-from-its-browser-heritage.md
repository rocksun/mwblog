<!--
title: Mozilla AI战略：为何与浏览器初心渐行渐远？
cover: https://cdn.thenewstack.io/media/2025/11/9ac3fbcf-getty-images-ijbq4mx7t0s-unsplashc.jpg
summary: Mozilla.ai致力于开源AI，而非Web。文章质疑Mozilla为何未将Firefox紧密融入AI战略，认为其可能错失Web AI机遇。
-->

Mozilla.ai致力于开源AI，而非Web。文章质疑Mozilla为何未将Firefox紧密融入AI战略，认为其可能错失Web AI机遇。

> 译自：[How Mozilla’s AI Strategy Disconnects From Its Browser Heritage](https://thenewstack.io/how-mozillas-ai-strategy-disconnects-from-its-browser-heritage/)
> 
> 作者：Richard MacManus

上周，Mozilla 基金会总裁 Mark Surman [发表了一篇文章](https://blog.mozilla.org/en/mozilla/rewiring-mozilla-ai-and-web/)，解释了 Mozilla 为何要“为人工智能做我们为网络所做的一切”。他还指出了一份新的[战略文件](https://wiki.mozilla.org/strategy)，该文件“对人工智能和网络的关注程度不相上下”。

Mozilla 新的人工智能中心战略的一部分是一个名为 [Mozilla.ai](http://mozilla.ai) 的衍生初创公司。就在 Surman 的文章发表前一天，我与 Mozilla.ai 的首席执行官 [John Dickerson](https://www.linkedin.com/in/john-dickerson/) 进行了交谈。我的目的是想了解 Mozilla.ai 在谷歌过去几年一直在[忙于定义](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/)的“[网络人工智能](https://thenewstack.io/googles-web-ai-playbook-the-paved-road-vs-the-open-field/)”领域，如果它有任何动作的话，都在做些什么。我惊讶地发现，Mozilla.ai 的大部分活动都*不*与网络相关。

## Mozilla.ai 的使命

Mozilla.ai 已经运营了近三年，但 Dickerson 本人相对较新。大约九个月前，他被引入“重置公司”，正如他所说。这使得 Mozilla.ai 从一个应用研发组织转变为一个商业企业，尽管它是一个公益性公司。Dickerson 表示，他的目标是产生“可持续的收入来源，以支持我们围绕开源人工智能的更大使命”。

Dickerson 解释说，Mozilla.ai 的使命不仅仅局限于开放网络。

> “……这有点像你把 Mozilla 宣言拿过来，然后把它应用到人工智能上，而不是浏览器上。”
> 
> **– John Dickerson, Mozilla.ai 首席执行官**

“我们的使命非常 Mozilla 化，”Dickerson 说。“它只是关于人工智能作为一种方式，以民主化互联网、社交网络中信息的获取，并 […] 推动用户拥有自己的数据、拥有自己的模型和控制权。所以这有点像你把 Mozilla 宣言拿过来，然后把它应用到人工智能上，而不是浏览器上。”

Mozilla.ai 的产品线主要由一系列开源人工智能工具和模型组成。例如，该公司最近发布了 [any-llm](https://github.com/mozilla-ai/any-llm) 的 1.0 版本，这是一个“统一接口，让开发者可以接入任何大型语言模型”。它还在构建 Mozilla.ai Agent Platform，一个面向企业的 SaaS 产品，目前处于私人测试阶段。

## 网络在哪里？

Mozilla.ai 正在构建的产品线中似乎明显缺少的是……网络技术。再次声明，我是在 Surman 的战略文章发布之前与 Dickerson 交谈的，所以我当时并不知道 Mozilla 的使命不再纯粹专注于网络。但我问 Dickerson，网络在 Mozilla.ai 中扮演什么角色。

他提到了 [Wasm-agents](https://blog.mozilla.ai/wasm-agents-ai-agents-running-in-your-browser/)，它能在浏览器中实现人工智能代理，以及他们与 Firefox 团队做的一些工作（例如“摇动以总结”功能）。但他随后重申，Mozilla 现在正在放眼浏览器之外。

“就一般网络而言，我理解人工智能和我们在此的使命的方式是，就像 20 年前、10 年前，浏览器是世界获取信息的方式。现在它不再是获取信息的唯一方式了，对吧？例如，我可以使用我自己的大型语言模型，它将互联网上的大量信息编码进去，我也可以通过它访问（互联网）。因此，当涉及到更高级别的 Mozilla 任务——民主化信息获取和信息控制（你自己的数据）时，它不再仅仅是关于浏览器了，对吗？”

> “……20 年前、10 年前，浏览器是世界获取信息的方式。现在它不再是获取信息的唯一方式了。”
> **– Dickerson**

我理解 Mozilla 正在通过拓宽范围来适应人工智能时代，但这让我觉得奇怪的是，Mozilla 没有利用其近三十年的开放网络专业知识。尤其是在谷歌今年一直忙于推广其网络人工智能产品时，我今年也清楚地看到，网络技术将成为人工智能时代的“[用户界面层](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/)”——看看 OpenAI 最近的举动，先是推出了 Apps SDK（[ChatGPT 内部的网络应用](https://thenewstack.io/openai-launches-apps-sdk-for-chatgpt-a-new-app-platform/)），然后又[推出了 Atlas 浏览器](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/)。

我注意到谷歌提倡“[设备端推理](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/)”以及他们似乎相信大多数人工智能用例很快将在浏览器中处理——部分归功于小型语言模型日益增强的能力。我问，Mozilla.ai 是否在浏览器端人工智能方面做任何工作？

Dickerson 回答说，他提到了 [llamafile](https://github.com/mozilla-ai/llamafile) 项目，这是一个开源项目，Mozilla.ai 最近宣布[正在采用](https://blog.mozilla.ai/llamafile-returns/)它，“以推动本地、隐私优先的人工智能”。

那么 [WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/) 呢，它是谷歌和微软合作开发的模型上下文协议 (MCP) 的一个网络变体？

Dickerson 回答说，他们“没有接触过 WebMCP”，但他提到了 Mozilla.ai 正在进行的一个类似项目，名为 [mcpd](https://www.mozilla.ai/open-tools/choice-first-stack/mcpd)，其网页将其描述为“Mozilla.ai Agent Platform 背后的工具链和运行时层”。其中的“d”似乎代表“declarative”（声明式），因为在该项目的 [GitHub 页面](https://github.com/mozilla-ai/mcpd)上，mcpd 被描述为“一个声明式管理模型上下文协议 (MCP) 服务器的工具”。

他补充说：“我们团队中的很多人都相信，一个充满活力的、仅限浏览器、浏览器优先的代理生态系统即将出现。”

[![Mozilla's choice-first stack](https://cdn.thenewstack.io/media/2025/11/033b829f-mozillaai-nov2025.png)](https://cdn.thenewstack.io/media/2025/11/033b829f-mozillaai-nov2025.png)

*Mozilla.ai 的“选择优先堆栈”。*

## 浏览器在人工智能时代的角色

就代理的用户界面而言，我注意到浏览器在这方面似乎已成为一个关键产品：谷歌[已将人工智能功能添加到 Chrome](https://thenewstack.io/chrome-switches-on-ai-the-future-of-browsing-begins-now/) 中（并承诺将推出更多代理功能），OpenAI 推出了全新的浏览器，Microsoft Edge 现在拥有“Copilot 模式”，Perplexity 和 Atlassian 等公司也拥有[人工智能浏览器](https://thenewstack.io/ai-browsers-dias-chat-based-ui-and-the-future-of-the-web/)。所有这些案例的目标都很明确：浏览器成为代理的大本营。

不用说，作为产品线的网络浏览器传统上是 Mozilla 的强项。事实上，该组织在 1998 年被命名为 Mozilla，[因为它是](https://web.archive.org/web/19990423143752/http://www.mozilla.org/mission.html)“指源自 Netscape Navigator 源代码的网络浏览器的通用术语”。那么，鉴于这一传统，Mozilla 的浏览器 Firefox 在 Mozilla.ai 战略中扮演什么角色呢？

Dickerson 首先指出，如何定义代理仍然是一个悬而未决的问题——例如，每天早上浏览器端代理可以完成邮件摘要，或者它也可以是 Gmail 等产品中的一个常规功能。更重要的是，他还认为浏览器本身——作为代理时代的产品类别——也尚未确定。

“浏览器是一个有趣的概念，对吧？无论你通过什么门户访问信息，其中一些信息是在线上的，那些搞定其中用户界面部分的人 […] 真的将开始主导这个领域。坦白说，我认为还没有任何浏览器完全做到了这一点。”

[![Firefox AI](https://cdn.thenewstack.io/media/2025/11/69889f22-forefox-ai.jpg)](https://cdn.thenewstack.io/media/2025/11/69889f22-forefox-ai.jpg)

Firefox 的新“[AI 窗口](https://blog.mozilla.org/en/firefox/ai-window/)”功能，如果你想要 AI 功能，会打开一个新窗口。

一个公平的观点是，我们尚不清楚一旦代理生态系统成熟，浏览器真正会是什么样子——OpenAI 的 Atlas 在 2025 年是一个足够 slick 的浏览器，但它与 Chrome 的基本范式相同（它本质上只是一个 2000 年代时代的浏览器，带有一个 ChatGPT 侧边栏）。Chrome 的 AI 功能目前也基本上只是基于聊天的。

尽管如此，我仍然惊讶于 Mozilla 没有将 Firefox 更紧密地融入其整体人工智能战略。相反，Mozilla 似乎认为浏览器只是现代互联网中众多类似工具之一。我不确定谷歌和 OpenAI 是否也这样认为——这两家公司都已将浏览器提升为人工智能领域的主要产品。

## 为什么 Mozilla 的人工智能战略可能存在缺陷

上个月，《卫报》[采访了](https://www.theguardian.com/technology/2025/oct/28/firefox-ai-internet-anthony-enzor-demeo) Firefox 的总经理 Anthony Enzor-DeMeo。当被问及 Firefox 的战略时，Enzor-DeMeo 指出，“我们正在缓慢推出 AI 功能，但我们的用户有选择权。他们可以将其关闭。”

在我看来，如果 Mozilla 没有一个超越“嗯，如果你想的话可以关掉”的特定人工智能浏览器战略，它就有被甩在后面的风险。恕我直言，Firefox 中的“摇动以总结”功能并非一项突破性的人工智能浏览器技术。

> 为什么 Mozilla 没有将其自己的浏览器 Firefox 更紧密地融入其人工智能战略？

更根本的是，Mozilla 以其浏览器和对开放网络的倡导而闻名。围绕其核心产品进行构建无疑是明智之举，而不是试图主导一个模糊的“开源人工智能”市场。

虽然 Mozilla.ai 在开源大型语言模型和人工智能工具方面做得非常出色，但我希望看到它更专注于面向开发者和消费者的网络人工智能功能。这是一个非常适合 Mozilla 的市场；如果它选择这样做，我想不出有比它更好的组织可以在这方面与谷歌和 OpenAI 竞争。