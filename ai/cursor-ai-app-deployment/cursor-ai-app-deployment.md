<!--
title: Cursor推出全托管应用部署功能，直面Lovable与Replit的竞争
cover: https://cdn.thenewstack.io/media/2026/11/0daf82eb-philip-oroni-xv2kgdto9ii-unsplash-scaled.jpg
summary: Cursor推出全新的全托管应用构建与部署功能，利用云端智能体帮助用户将AI生成的应用直接发布到可共享的线上链接，无需手动配置底层基础设施，从而直接切入Lovable和Replit的市场赛道。
-->

Cursor推出全新的全托管应用构建与部署功能，利用云端智能体帮助用户将AI生成的应用直接发布到可共享的线上链接，无需手动配置底层基础设施，从而直接切入Lovable和Replit的市场赛道。

> 译自：["Most apps never make it off localhost": Cursor takes on Lovable and Replit with fully managed app deployment](https://thenewstack.io/cursor-ai-app-deployment/)
> 
> 作者：Paul Sawers

AI 编码智能体无疑让把一个创意变成可运行的应用变得更加容易。然而，将应用程序从本地机器转移到真实用户手中仍然是一个障碍，需要经历从托管和数据库配置到关键安全检查等必不可少的底层基础设施步骤。

Cursor 是一家在 8 月份被 Elon Musk 的 SpaceX 以 [600 亿美元](https://uk.finance.yahoo.com/news/spacex-completes-record-60-billion-131413932.html)[收购](https://cursor.com/blog/joining-spacex) 的 AI 编码平台，它在周四发布的一条 X 帖子中[承认了这个问题](https://x.com/cursor_ai/status/2118458629091426304)。

该公司指出：“智能体让编写代码变得更容易，但大多数应用从未真正离开过 localhost。”

为了解决这个问题，Cursor [正在引入](https://cursor.com/changelog/build-live-apps)新的[应用构建和部署功能](https://cursor.com/docs/cloud-agent/apps)，旨在将 AI 生成的应用从开发阶段推向可访问的线上共享 URL，而用户甚至无需亲自考虑底层的基础设施。

> “智能体让编写代码变得更容易，但大多数应用从未真正离开过 localhost。”

## 构建于云端智能体之上

这项新功能围绕[云端智能体](https://cursor.com/cloud)构建，Cursor [去年推出了](https://cursor.com/blog/cloud-agents)这一功能，作为开发者远程运行多个 AI 编码智能体的一种方式，无需让他们的笔记本电脑保持开启状态。当时，该公司强调了它们修复 bug、处理较小编码任务以及实现某些复杂功能的能力。

通过最新更新，这些相同的智能体现在可以将应用程序一路推向部署，处理使其他用户能够访问它们所需的关键步骤。不过，该功能仅通过云端智能体提供，这意味着它不能与在本地运行的智能体一起使用。

用户首先通过自然语言描述他们想要构建的应用程序，Cursor 会像往常一样管理代码生成和开发过程。

![1. Prompt Cursor as usual](https://cdn.thenewstack.io/media/2026/11/ce19aa68-gif1.gif)

*1. Prompt Cursor as usual*

从那里开始，智能体创建应用程序并设置底层项目，包括使其运行所需的必要组件。

![2. Cursor's agent builds the application](https://cdn.thenewstack.io/media/2026/11/9632b6e7-gif2.gif)

*2. Cursor 的智能体构建应用程序*

应用程序准备就绪后，用户可以在决定是否点击发布之前预览结果。

![3. Preview the app before publishing](https://cdn.thenewstack.io/media/2026/11/38bbe001-gif3.gif)

*3. 发布前预览应用*

发布使应用程序能够通过一个线上 URL 被访问，允许用户与同事或其他用户分享，而无需自己配置托管服务。

![4. Share the app via a live link](https://cdn.thenewstack.io/media/2026/11/7005f0ac-gif4.gif)

*4. 通过线上链接分享应用*

值得注意的是，有两种入门方式。从头开始构建应用程序的用户将自动在 [Cursor Origin](https://cursor.com/origin) 上创建一个新的代码库，这是该公司[在 8 月份推出的基于 Git 的代码托管平台](https://thenewstack.io/cursor-origin-github-alternative/)，作为 GitHub 的以智能体为中心的替代方案。

或者，用户可以从现有的 GitHub 代码库部署应用程序。这意味着已经有应用程序在开发的开发者可以使用 Cursor 的云端智能体来准备和发布它，而无需将代码迁移到 Origin 或手动设置部署基础设施。

从 Cursor [自己的示例](https://cursor.com/changelog/build-live-apps)来看，该功能似乎主要面向需要创建内部业务应用的员工，例如销售仪表板、入职培训程序、客户演示和开发者门户。因此在这方面，对于有工具构思但缺乏技术能力来自己运行它的非开发者来说，这可能是一个福音。

当然，该功能并不局限于业务应用。一个胸怀大志的氛围编程者同样可以轻松创建一个社区足球联赛追踪器或互动家庭假期规划器。由于个人订阅者可以公开发布应用，这些创作可以与任何拥有链接的人分享。

## 底层技术：托管、数据库与安全

当 Cursor 在 8 月份[推出预览云端智能体项目并将其发布到线上 URL 的功能](https://cursor.com/changelog/start-from-scratch)时，它实际上已经开始缩小这一差距。然而，用户仍然需要连接他们自己的 Vercel 账户。

![Cursor's earlier app-building feature, introduced in August 2026.](https://cdn.thenewstack.io/media/2026/11/1b2de6db-gif5.gif)

*Cursor 早期应用构建功能，于 2026 年 8 月推出。*

最新版本取消了这一要求，同时引入了各种新的智能特性。

在幕后，Cursor 现在负责多项基础设施需求，包括托管、数据库和身份验证。

在托管方面，Cursor 会为每个团队或个人订阅者自动创建一个专用的、与其他客户隔离的账户。虽然 Cursor 的公告没有指明底层的托管服务提供商，但 Vercel 在 X 上的[另一篇回应中透露](https://x.com/vercel/status/2118464668444557411)，该新功能构建在其 [Vercel for Platforms 基础设施](https://vercel.com/for/platforms)之上。这基本上允许用户部署应用程序，而无需创建自己的 Vercel 账户或亲自配置托管。

如果应用程序需要数据库，Cursor 会使用 PostgreSQL 提供一个，而私有和团队应用程序则受到 Cursor 现有登录系统的保护。个人订阅者也可以使其应用公开可访问。

应用程序可以连接到外部服务（例如公司数据库或数据仓库），用户提供必要的凭证。Cursor 表示，这些机密信息是分开管理的，这意味着 AI 智能体永远看不到它们的实际值。

接下来是棘手的安全问题。当用户选择发布应用程序时，Cursor 表示它会在允许其上线之前运行“一系列确定性的和智能体的安全检查”。这些检查包括对暴露的凭证、机密和敏感文件的强制性检查，以及旨在识别更严重漏洞的 AI 驱动审查。

然而，目前尚不清楚这些自动化检查能够多么可靠地识别更复杂的问题，例如错误配置的数据库权限或应用级访问控制。对于考虑将 AI 生成的应用连接到敏感内部系统的组织来说，这是一个重要的考量因素，在这种情况下，额外的安全审查仍然是明智的。

这种担忧也有先例。去年 5 月，[Semafor 报道称](https://www.semafor.com/article/05/29/2025/the-hottest-new-vibe-coding-startup-lovable-is-a-sitting-duck-for-hackers)，两名 Replit 员工检查了 1,645 个由 Lovable 构建的应用，发现其中 170 个暴露了敏感信息。这些问题涉及错误配置的数据库 permissions（权限），突显了保护通过 AI 工具创建的应用的难度。Lovable 表示，它[随后推出了](https://lovable.dev/blog/secure-vibe-coding)进一步的安全检查，以在应用发布前识别潜在漏洞。

## Cursor 进军 Lovable 和 Replit 的地盘

当然，Cursor 正在进入已被 [Lovable](https://lovable.dev/) 和 [Replit](https://thenewstack.io/replit-shopify-storefront-integration/) 等公司占据的领域，这些公司允许用户通过自然语言提示词创建和发布应用程序。

虽然 Cursor 的最新公告强调了内部业务工具，但 Lovable 和 Replit 传统上吸引的是更广泛的、有抱负的应用创作者受众。尽管如此，重叠是显而易见的，Cursor 进军部署领域的举动已经引起了开发者的注意。

> “Cursor 刚刚杀入了 localhost 的墓地。”

一位软件工程师[在 X 上写道](https://x.com/thecsguy/status/2118482491900076141?a=XUyRWnUp9QtfP70Fq5E&s=20)：“*cursor 刚刚杀入了 localhost 的墓地*”，呼应了 Cursor 关于永远走不出本地开发的 AI 生成应用程序的自身讯息。

这也与 [Grok Build](https://grok.com/build) 存在有趣的重叠，特别是考虑到 SpaceX 在 8 月份收购了 Cursor。

SpaceXAI 在 7 月份[推出了 Grok 的 Build 模式](https://x.ai/news/grok-build-mode)，然后[在次月](https://x.ai/news/grok-build-for-everyone)将其扩展到所有 Grok 计划。该功能允许用户直接在 Grok 对话中创建应用、游戏和网站，然后将其发布到可分享的 grok.me 链接。

这与 Cursor 的最新产品有些相似，尽管 Cursor 是通过其成熟的编码环境和云端智能体来切入的，并且更加强调商业应用和托管基础设施。

这种重叠并没有被忽视。一位 X 用户[回应 Cursor 的公告时问道](https://x.com/amsultan2010/status/2118459411437895889?a=fRQ4Odh-YGNBjve3A58&s=20)：“*所以 cursor 现在是在正式取代 grok build 吗*？”

目前没有迹象表明 Grok Build *正在*被取代，但这两款产品现在覆盖了一些明显相似的领域，引发了关于 SpaceXAI 未来打算如何区分它们的疑问。

对于想要体验 Cursor 新功能的人来说，它适用于启用了云端智能体的*所有*付费 Cursor 计划。

随着部署日益成为 AI 编码体验的一部分，Cursor 的最新举动可能会给专用的应用构建平台带来进一步的压力，因为针对专业开发者的工具与针对有抱负的氛围编程者的工具之间的界限正在不断缩小。