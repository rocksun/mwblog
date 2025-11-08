
<!--
title: 全栈开发者时间去向大揭秘：前端还是后端？
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
summary: JetBrains调查：全栈开发者后端任务更多；htmx 4.0发布，改进fetch()和继承；Turborepo更新支持微前端；Storyblok与Netlify合作，优化内容到部署工作流。
-->

JetBrains调查：全栈开发者后端任务更多；htmx 4.0发布，改进fetch()和继承；Turborepo更新支持微前端；Storyblok与Netlify合作，优化内容到部署工作流。

> 译自：[Frontend or Backend: Where Full-Stack Devs Spend Their Time](https://thenewstack.io/frontend-or-backend-where-full-stack-devs-spend-their-time/)
> 
> 作者：Loraine Lawson

正在考虑成为一名全栈开发者？请注意：根据 [JetBrains](https://thenewstack.io/exploring-the-jetbrains-ai-assistant-for-visual-studio-code/) 的一项[新调查](https://devecosystem-2025.jetbrains.com/)显示，全栈开发者表示其大部分任务在后端而非前端的可能性是后者的两倍。

2025年的[开发者体验和开发者生产力状况报告](https://lp.jetbrains.com/stateofdevex/)调查了超过6,000名开发者和2,000名技术主管。

此外，调查还发现，85%负责前端的开发者也从事[后端开发](https://roadmap.sh/backend)；这与57%从事[前端开发](https://thenewstack.io/introduction-to-frontend-development)的后端开发者形成对比。

完整的调查报告探讨了公司如何衡量开发者体验（DevEx）和开发者生产力，并考察了开发者对AI和标准生产力指标的看法。

## htmx 发布新 Alpha 版本

[Carson Gross](https://bigsky.software/cv/)，[htmx](https://thenewstack.io/htmx-html-approach-to-interactivity-in-a-javascript-world/) 的创建者，曾承诺永远不会有 htmx 3。他信守诺言，**但**他从未说过不会有 htmx 4。

Gross 本周发布了 htmx 的新 Alpha 版本。[他称之为 fetch()ening](https://htmx.org/essays/the-fetchening/)。

Htmx 是一个 JavaScript 库，允许 Web 开发者使用少量或不使用客户端 JavaScript。相反，它让程序员能够直接从 HTML 属性中访问现代浏览器功能，例如 AJAX、WebSockets 和 Server Sent Events，从而实现动态 Web 应用程序。

Gross 解释说，今年早些时候，他创建了 [fixi.js](https://github.com/bigskysoftware/fixi)，这是一个对 htmx 理念的超极简主义实现。

他写道：“这项工作让我有机会更熟悉 fetch()，尤其是 JavaScript 中可用的异步基础设施。”

他说，虽然 htmx API 是正确的，但他开始思考“也许还有空间进行更剧烈的实现更改，利用这些特性来简化库。”不过他知道，从 XMLHttpRequest 更改为 fetch()“将是一个相当剧烈的变化，肯定会破坏至少一些东西。”

相反，他开始考虑对 htmx 进行一次更新，以添加 fetch()，并可能修复 htmx 积累的一些怪癖。

他写道：“所以，我最终不情愿地改变了主意：将会有另一个主要版本的 htmx。”“然而，为了信守承诺不会有 htmx 3.0，下一个版本将是 htmx 4.0。”

计划进行三项旨在简化的重大更改：

1.  **fetch() 改革。** 他写道，Fetch() 将取代 XMLHttpRequest 成为核心 AJAX 基础设施。“这实际上不会对 htmx 的大多数用法产生巨大影响，只是事件模型会由于 fetch() 和 XMLHttpRequest 之间的差异而必然发生变化。”
2.  **隐式属性继承的漫长噩梦结束。** 他说，这将是 htmx 用户需要应对的最重要的升级。Gross 承认他的“htmx 1.0 和 2.0 中最大的错误是使属性继承成为隐式的。我这样做受到了 CSS 的启发，结果与 CSS 大致相同：强大且令人抓狂，”他写道。因此，他解释说，htmx 4.0 的属性继承将通过 :inherited 修饰符显式而不是隐式进行，如下所示：

    ```html
    <div><button>喜欢</button>  
    <button>不喜欢</button></div>  
    <output id=”output”>选择一个按钮…</output>
    ```

    他写道：“这里 hx-target 属性被显式声明为在封闭的 div 上继承，如果不是这样，按钮元素将不会从它继承目标。”
3.  **本地缓存历史的暴政结束。** “对我们和 htmx 用户来说，另一个持续的痛点是历史支持。htmx 2.0 将历史记录存储在本地缓存中以加快导航速度，”他写道。“不幸的是，DOM 快照通常很脆弱，因为第三方修改、隐藏状态等。他补充说，将历史信息存储在会话存储中还会带来安全问题。”

为此，在 htmx 2.0 发布后，团队经常会建议面临历史相关问题的人完全禁用缓存。

他写道：“在 htmx 4.0 中，历史支持将不再对 DOM 进行快照并将其本地保存。”“它将改为发出网络请求以获取恢复的内容。这是 2.0 在历史缓存未命中时的行为，并且对于 htmx 用户而言，它只需很少的努力即可可靠工作。”

他补充说，相反，将有一个启用历史缓存的扩展，但它将是可选加入而非默认启用。

他继续解释了哪些将保持不变，以及他们将如何支持 htmx 的多年推出计划，该计划于 11 月 1 日开始，并发布了 Alpha 版本。4.0.0 版本应在明年某个时候推出，最终版本计划于 2027 年初发布。您可以在 [GitHub 上的 four 分支](https://four.htmx.org)中跟踪团队的进展。

“总而言之，我们希望 htmx 4.0 的体验会非常像 2.0，但具有更好的功能，并且我们希望，能有更少的错误，”Gross 最后总结道。

## Vercel 的 Turborepo 发布更新，包含微前端代理

[Turborepo](https://thenewstack.io/turborepo-speedy-builds-for-javascript-monorepos/) 团队发布了 [Turborepo 2.6](https://turborepo.com/blog/turbo-2-6#microfrontends)，其中包含对仓库开发者体验的改进。

Turborepo 是一个用 Rust 编写并为 JavaScript 和 TypeScript 优化的构建系统。它于 2021 年被前端基础设施公司 [Vercel](https://thenewstack.io/next-js-in-chatgpt-vercel-brings-the-dynamic-web-to-ai-chat/) 收购。此版本支持以下功能：

1.  [**微前端**](https://thenewstack.io/the-case-for-microfrontends-and-moving-beyond-one-framework/)：开发者现在可以在一个 localhost 端口上创建多个应用程序；
2.  **[Bun](https://thenewstack.io/how-to-build-a-serverless-api-with-bun-and-hono/) 包管理器稳定版**：针对 bun.lock 的精细锁文件分析和修剪。Bun 是一个快速、一体化的 JavaScript、TypeScript 和 JSX 工具包。“这意味着，当您使用 Bun 作为包管理器时，Turborepo 将仅对依赖项发生变化的包进行缓存未命中，”公告指出。“如果您更新了 Web 应用程序的依赖项，您的文档应用程序的任务仍将命中缓存。”
3.  **终端 UI 中的任务列表搜索**：使用“/”更快地聚焦任务。此版本改进了任务搜索，使其成为开发者与大型 Turborepo 交互的基本方式之一。

团队解释说，垂直微前端是一种架构，其中多个应用程序在一个生产域上提供服务，并划分为“区域”。“域的每个路径都由其中一个应用程序处理。”

这会给本地开发带来问题，因为开发者必须运行许多应用程序，而不仅仅是一个。根据 Vercel 软件工程师 [Anthony Shew](https://github.com/anthonyshew) 和 [Tom Knickman](https://github.com/tknickman) 的说法，每个应用程序最终都需要自己的开发命令和要使用的端口。

Shew 和 Knickman 写道：“今天，我们正在发布一个用于本地开发的微前端代理，以便您的所有应用程序可以在一个端口上运行，只需一个命令。”“将 microfrontends.json 文件添加到您的父应用程序中，Turborepo 将自动将 localhost:3024 代理到您其他应用程序的端口。”

虽然 Turborepo 的原生微前端代理旨在用于本地开发，但 Turborepo 与基础设施提供商集成，将微前端架构引入生产环境。

团队写道：“例如，我们设计了 Turborepo 原生微前端代理，使其与 Vercel 的微前端产品协同工作，该产品也于今天发布到通用版本。”“事实上，Vercel 的微前端功能为 Turborepo 原生微前端提供了研究基础。我们与 Vercel 的一些最大客户一起探索了如何在本地和生产环境中构建微前端，现在正在将这些经验从闭源提取到开源。”

他们写道，当开发者将 @vercel/microfrontends 安装到仓库中时，Turborepo 将动态调整本地环境以使用该包提供的代理，从而与生产基础设施深度集成。[微前端功能的文档](https://turborepo.com/docs/guides/microfrontends)已发布。

团队写道：“我们期待与更多提供商合作，在您的整个技术栈中集成无缝微前端。如果您是寻求集成的基础设施提供商，请联系我们。”

## 从内容到 Web：新合作提供一体化工作流

[Storyblok](https://www.storyblok.com/) 是一家面向企业的无头内容管理系统，正与 Web 开发平台 [Netlify](https://thenewstack.io/new-netlify-agents-offer-ai-workflows-for-developers/) 合作，旨在提供从内容创建到 Web 部署的连接工作流。

根据一份公司声明，这对开发者意味着他们可以使用任何他们想要的前端框架，并能在每次发布内容更新时触发自动部署。

Storyblok 首席执行官兼联合创始人 Dominik Angerer 在一份准备好的声明中说：“我们一次又一次地看到——客户在内容方面做得很好，但却难以将项目快速、可靠地大规模推向市场。他们的营销人员要等待数天才能让页面上线，而他们的开发者则在晚上修补服务器或解开部署脚本。”“随着人工智能颠覆内容策略，这些延迟和痛点根本无法维持；这就是我们与 Netlify 合作的原因。它负责幕后的繁重工作：全球托管、边缘交付、缓存、扩展，因此团队可以创建和发布令人惊叹的项目。”

Storyblok 表示，这将“弥合”内容管理与项目部署之间的鸿沟，从而大规模实现更快、更可靠的内容部署时间。

另一个目标是帮助公司减轻人工智能对内容的影响。

Storyblok 在一份新闻稿中表示：“随着消费者越来越多地使用 AI 搜索引擎，公司发现其品牌在线上的可见性和准确性正在受到影响。”“Storyblok 与 Netlify 的合作，将非常有利于帮助品牌在一个高性能、AI 就绪的平台上快速开发、构建和部署其新内容。”