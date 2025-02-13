
<!--
title: 开发者如何使用快速增长的AI编码工具Bolt
cover: https://cdn.thenewstack.io/media/2025/02/65d91009-getty-images-uyefhxjj4xs-unsplashb.jpg
-->

StackBlitz 曾经是一个基于浏览器的 IDE，但现在已经转向一个名为 Bolt 的 agentic IDE。我们与它的 CEO 聊了聊开发者们是如何使用它的。

> 译自 [How Developers Are Using Bolt, a Fast Growing AI Coding Tool](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)，作者 Richard MacManus。

上个月，StackBlitz 正式更名为 Bolt，一个基于 AI 的在线 Web 应用程序构建器，它之前是一个 [云开发环境](https://thenewstack.io/stackblitz-launches-codeflow-and-announces-figma-investment/) (CDE)。 为什么突然转型？[Bolt](https://bolt.new/) 在市场上众多其他 [AI 编码工具](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/) 中表现如何？ 我与 CEO Eric Simons 进行了交谈，以找出答案。

Simons 承认，推出 AI 开发者工具使 StackBlitz 免于大多数硅谷初创公司的命运。“如果我们没有弄清楚如何改变公司的发展轨迹，我们就会开始解散公司，”他说。

根据 Simons 的说法，StackBlitz 有“很多开发者在使用它，而且 [...] 我们在向企业销售，但它不是风险投资规模。” 他说，CDE 工具 StackBlitz 在“进入市场的七年后”的年度经常性收入 (ARR) 不到一百万美元。 因此，他们需要做些什么，特别是考虑到过去几年 [AI 辅助编码](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/) 的突然兴起。

“所以 Bolt 就像我们在账面上拥有的最后一个实验，在我们开始考虑出售公司或……其他什么之前，”Simons 说。

![](https://cdn.thenewstack.io/media/2025/02/effaa861-stackblitz-to-bolt.jpg)

*从 StackBlitz 转向 Bolt*

Bolt 于去年 10 月推出，并且在运营的头几个月里似乎出现了显着的增长。 Simons 说，Bolt 在短短两个月内“完成了 2000 万美元的 ARR”——“而且从那以后我们一直在增长。”

根据上个月 [X 上的一个帖子](https://x.com/ericsimons40/status/1882106925795696674)，Bolt 现在拥有 200 万注册用户。

## 其他 CDE 也已转向 AI 编码

事实证明，StackBlitz 并不是唯一一家最近转向 AI 开发工具的 CDE 公司。 12 月，CodeSandbox（我在 2022 年 11 月 [介绍过的一家 CDE](https://thenewstack.io/the-race-to-be-figma-for-devs-codesandbox-vs-stackblitz/)，在我介绍 StackBlitz 几周后）被一家资金雄厚的风险投资公司 [AI Together 收购](https://codesandbox.io/blog/joining-together-ai-introducing-codesandbox-sdk)。 它立即推出了一款新产品 CodeSandbox SDK，它允许你“以编程方式启动 (AI) 沙箱”。

“CodeSandbox 于 2017 年作为 React playground 启动，”该公司在其 X 帐户上 [评论道](https://x.com/codesandbox/status/1867233573037572437)。 但尽管在 2024 年增长到令人尊敬的 450 万月活跃用户，但它在 AI 领域看到了更大的机会：“随着世界进入 AI 时代，我们发现我们的 VM 沙箱是执行代理工作流程的完美解决方案。”

我在 2022 年介绍的另一家 CDE Gitpod，于 [去年 10 月](https://www.gitpod.io/blog/introducing-gitpod-flex) 发布了其基于 AI 的产品：Gitpod Flex，被描述为一个“自动化平台”。 其中一项自动化功能是配置“LLM 驱动的代理工作流程”的能力。

> “…早在 5 月，我们就对 Sonnet 3.5 有了一个先睹为快的了解，我当时想，哇，这将改变这里的一切，因为它实际上输出了非常好的代码。”
>
> – Eric Simons, StackBlitz / Bolt CEO

Simons 告诉我，Bolt 的想法大约在一年前产生的，当时 [生成式 AI 的炒作](https://thenewstack.io/more-than-an-openai-wrapper-perplexity-pivots-to-open-source/) 迫使几乎所有硅谷公司将 AI 集成到他们的产品中。 StackBlitz 的核心一直是其专有的 WebContainers 技术，该技术 [已被描述为](https://blog.stackblitz.com/posts/introducing-webcontainers/) 允许你“创建在几毫秒内启动的完整堆栈 Node.js 环境”。 所以最初的想法是将它与 ChatGPT 结合起来。 Simons 从去年年初开始讲述了这个故事。

“我们当时正在使用 OpenAI 的模型，但它们还不够好，无法实际输出良好的工作代码 [...] 只是没有大量的错误。 所以我们把这个想法搁置了。 然后早在 5 月，我们就对 [Claude] Sonnet 3.5 有了一个先睹为快的了解，我当时想，哇，这将改变这里的一切，因为它实际上输出了非常好的代码。 所以我们最终批准了这个项目。 它 [后来变成了 Bolt] 于 7 月开始，然后在 10 月推出。 从那以后，它就像野火一样蔓延开来。”

## 开发者如何使用 Bolt

CDE 基本上是一个基于浏览器的 IDE。因此，在当今的环境下，从基于浏览器的 IDE 过渡到*具有 AI 功能*的基于浏览器的 IDE 是非常有意义的。但这不仅仅是像第一波 AI 编码产品那样，用 AI 生成的建议来辅助开发者——GitHub Copilot、Cursor、Tabnine 等等。Bolt 承诺几乎完全接管 Web 应用程序或网站的编码。

在我自己的测试中，我能够使用 Bolt 中的一个默认提示启动一个全新的 Astro 博客（Netlify 首席执行官 Matt Biilmann [也做了同样的事情](https://biilmann.blog/articles/i-built-a-blog/)）。

![](https://cdn.thenewstack.io/media/2025/02/e500d52f-bolt-screenshot-feb25.jpg)

*Bolt截屏*

在一两分钟内，Bolt 就为 Astro 博客创建了一个完整的存储库，然后我将其免费部署到 Netlify。好吧，这个过程与在 GitHub 上克隆一个项目没有太大区别。但是，我随后能够使用 AI 聊天界面对我的 Astro 博客进行一些定制的更改，Bolt 似乎处理得很好。一路上出现了一些错误，但 Bolt 修复得还不错。

不过，我只是一个业余开发者。我很好奇 Bolt 上专业开发者的使用模式。他们是否在 Bolt 中启动应用程序，然后将代码移动到像 VS Code 这样的完整 IDE 中来完成它？

首先，Simons 指出，他们一半以上的用户都像我一样——不是专业开发者。“他们是 PM [产品经理]、设计师、企业家等等。”在谈话的后面，他说大约 60-70% 的 Bolt 用户是“非技术人员”。

> “在开发者案例中，很多人都在使用它作为一个疯狂快速的、从零到一的脚手架工具，用于生成 UI 设计、原型等等。”
>
> – Simons

但在实际开发者方面，Simons 已经确定了几种使用模式。他说，有时开发者会在 Bolt 中构建他们的整个应用程序。他还看到了著名 AI 专家 Andrej Karpathy（OpenAI 的创始人之一）所说的“[vibe coding](https://x.com/karpathy/status/1886192184808149383)”。

Simons 解释说：“开发者开始让 AI 构建东西，然后你只是坐在那里，点击‘接受更改’或类似的东西。”

但是 Bolt 用户也在 Bolt 和他们常用的 IDE 之间来回切换。

Simons 说：“在开发者案例中，很多人都在使用它作为一个疯狂快速的、从零到一的脚手架工具，用于生成 UI 设计、原型等等，然后将其带到 Cursor [或] VS Code 中继续工作。然后你把它带回 Bolt […] 添加主要功能，或者其他什么。”

## 替代 Figma？

在我上次于 2022 年 10 月采访 Simons 时，他将当时的公司比作 Figma——这家公司出人意料地构建了一个“[浏览器中的 PhotoShop](https://www.sequoiacap.com/article/dylan-field-figma-spotlight/)”应用程序，[Adobe 差点以 200 亿美元收购了它](https://thenewstack.io/adobe-buys-figma-what-does-this-mean-for-web-standards/)（该交易在受到欧盟和英国监管机构的压力后[后来被取消了](https://www.theverge.com/2023/12/18/24005996/adobe-figma-acquisition-abandoned-termination-fee)）。Simons 在 2022 年告诉我：“StackBlitz 非常类似于 Figma 为设计所做的事情的开发类比。”

他想表达的是 StackBlitz 在浏览器中完成了一切，[就像 Figma 一样](https://thenewstack.io/the-race-to-be-figma-for-devs-codesandbox-vs-stackblitz/)。与 StackBlitz 几年前的宣传相比，Bolt 最吸引人的地方在于，Figma 的比较现在已经被彻底颠覆了。

Simons 在本月早些时候的 [一条推文](https://x.com/ericsimons40/status/1882106931479031841) 中声称：“我们已经进入了一个新时代，用代码制作可用的原型比在 Figma 中设计它们更快。”

> “你传统上会在 Figma 中做的事情来制作原型，[…] 用代码做更快。”
>
> – Simons

在我们目前的讨论中，Simons 稍微缓和了这种立场（也许是因为 Figma 是 StackBlitz 的投资者）。但他仍然坚持认为 Bolt 至少取代了部分原型设计过程。

“你传统上会在 Figma 中做的事情来制作原型，[…] 用代码做更快。这实际上是更好的方法，因为它很真实，你知道吗？而且你实际上可以玩玩它，对吧？”

这完全有道理。当你可以用文字向 Bolt 描述你希望你的应用程序是什么样子时，为什么还要费心设计一个原型用户界面呢？

## Token 成本

应该注意的是，虽然你可以免费启动 Bolt，但你很快就会发现自己需要购买“tokens”才能继续开发你的项目（我的 Astro 博客就是这种情况！）。“Pro”帐户（1000 万个 tokens）的定价为每月 20 美元起，最高可达每月 200 美元（1.2 亿个 tokens）。但是，目前还不完全清楚一个项目需要多少个 tokens。[Bolt 的 Reddit 社区](https://www.reddit.com/r/boltnewbuilders/) 对此的看法差异很大。

![](https://cdn.thenewstack.io/media/2025/02/149f951b-bolt-pricing.png)

Bolt的一些用户正在采取混合方法——同时使用Bolt和他们的完整IDE——这可能部分是由于成本原因。这位用户在[Reddit](https://www.reddit.com/r/boltnewbuilders/comments/1iex3lt/comment/maekb67/)上评论道：

> “没有理由使用Bolt来创建整个项目。我让Bolt创建框架并获得正确的样式，然后我将项目带到VSCode或Current并在那里完成它，使用DeepSeek、OpenAI、Claude。”

无论如何，Bolt是开发人员（专业或业余）可以考虑的另一种潜在的AI助手工具。现在有很多这样的工具，例如[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)、Devin和[Solver](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/)。所以你应该尝试其中的一些，看看哪一个最适合你。
