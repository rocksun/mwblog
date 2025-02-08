
<!--
title: 超越DX：开发者现在必须学习Agent Experience(AX)
cover: https://cdn.thenewstack.io/media/2025/02/44ca9d29-ave-calvar-h5rexzafgdi-unsplashb.jpg
-->

随着像 Bolt、Windsurf 等 Agentic IDE 的兴起，Netlify 首席执行官 Matt Biilmann 表示，我们需要一种新的设计模式：Agent Experience（代理体验）。

> 译自 [Beyond DX: Developers Must Now Learn Agent Experience (AX)](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)，作者 Richard MacManus。

在本月的一篇博文中，Netlify 首席执行官 [Matt Biilmann](https://www.linkedin.com/in/mathias-biilmann-christensen-a5a3805/) 介绍了“[代理体验](https://biilmann.blog/articles/introducing-ax/)”（AX）的概念，他指出“如今，每天有 1,000 多个网站直接通过 ChatGPT 在 Netlify 上创建。”

尽管我知道大多数软件开发人员已经使用 [AI 辅助编码工具](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/)，但我仍然惊讶地发现每天有 1,000 个新网站直接通过 AI 在 Netlify 上创建。这表明了一个更深层次的趋势：开发项目的启动越来越多地通过 AI 自动化——无论是通过像 ChatGPT 这样的聊天机器人（如 Netlify 的情况），还是通过 [AI 代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)。

我与 Biilmann 进行了交谈，以了解更多关于软件开发项目中 AI 自动化趋势的信息。我们还讨论了 AX，Biilmann 表示，AX 是一种相关的开发者模式，已经成为 Netlify 平台的重要组成部分。

## 为什么开发者使用 AI 来启动网站和应用程序？

Netlify 上的大部分 ChatGPT 活动都来自该公司为 ChatGPT 开发的 [插件](https://www.netlify.com/integrations/openai/netlify-chatgpt-plugin-netlify-api/)。描述如下：“只需描述您想要构建的网站，ChatGPT 就会将其部署到 Netlify！”

> “在与 ChatGPT 集成时，我们了解到我们需要为其提供围绕身份验证和移交等的特定流程。”
>
> – Matt Biilmann, Netlify CEO

但是，使用 ChatGPT 创建的是什么样的网站呢？Biilmann 告诉我，主要有两种或三种用例。

“一种是你可以称之为短暂的网站或应用程序 [...] 人们要求 ChatGPT 构建一些显示某些信息或某些数据的东西，或者一张阅读卡，或者一个有趣的幻灯片，或者一个一时兴起的东西——部署它，他们就拥有一个可以分享的 URL，对吧？”

这类似于开发人员使用 [像 Glitch 这样的平台](https://thenewstack.io/glitch-brings-view-source-philosophy-to-react-node-js/) 的方式，所以没有什么真正的新东西。但是 Biilmann 看到的 ChatGPT 的第二个用途是“人们弄清楚如何启动一个新项目”。Biilmann 认为，有经验的开发人员和非专业开发人员都在这样做。

“这[用例]可能会分为两种，其中一种更像是真正的开发人员，他们知道自己在做什么，但希望更快地启动，”他说。“我认为更多的人现在正在走出 ChatGPT，直接使用像 Bolt 或 Lovable 这样的工具，或者真正迎合他们的工具，或者 Windsurf——就是那个级别的工具。”

## Agentic IDE 的崛起

Biilmann 提到的工具只是最近上市的众多（如果找不到更好的词）[agentic IDE](https://generativeprogrammer.com/p/ai-coding-assistants-landscape) 中的几个。[Bolt](https://bolt.new/) 是去年 10 月从 StackBlitz 分拆出来的工具，[Windsurf](https://codeium.com/windsurf) 于 11 月发布（实际上称自己为“agentic IDE”），而 [Lovable](https://lovable.dev/) 于 12 月以当前迭代版本发布（之前是一个名为 GPT Engineer 的开源项目）。所以这些都是非常新的产品——而且这三款产品似乎在最近几个月都增长迅速。

![](https://cdn.thenewstack.io/media/2025/01/5fca8da5-windsurfermain.jpg)

*Windsurf UI，来自 [The New Stack 上 Jack Wallen 最近的一篇教程](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/)。*

还值得一提的是 Replit 和 Vercel，它们都发布了 AI 自动化产品。[Replit Agent](https://blog.replit.com/introducing-replit-agent) 于去年 9 月推出，被描述为“我们能够创建和部署应用程序的 AI 系统”。Vercel 早在 2023 年 10 月就推出了 [v0](https://v0.dev/)，尽管它的定位更像是一个聊天产品（类似于 ChatGPT，但面向前端开发人员），而不是 IDE。

上个月，Matt Biilmann 使用其中一个工具 Bolt 创建了一个新的个人博客。

“[这个博客几乎完全是通过提示构建的](https://biilmann.blog/articles/i-built-a-blog/)，”Biilmann 在他的第一篇文章中写道。“它始于一个 bolt.new 提示，该提示启动了一个部署到 Netlify 的基于 Astro 的简单博客，然后在 Cursor 和 Windsurf 上进行了一些调整。”

这些工具的优点在于，它们使非全职开发人员更容易开发自定义网站或应用程序。正如Biilmann所说，通过使用AI工具，“突然出现了一类全新的开发人员，他们正在学习为Web构建应用”。

## 为AI代理设计

AX的演进之路始于Netlify将其插件与ChatGPT集成。这使他们意识到，代理使用Netlify平台的方式与人类用户不同。

![Status quo before AX](https://cdn.thenewstack.io/media/2025/02/c27569d5-statusquo.png)

AX之前的现状，来自Netlify的Sean Roberts的[一篇文章](https://agentexperience.ax/research/agent-web-and-its-interface/)。

“在与ChatGPT集成时，我们了解到我们需要为它提供一些关于身份验证和移交等的特定流程，”Biilmann说。“项目突然从代理开始，而不是从用户做某事开始——所以你需要代理能够，例如，在用户自己创建帐户之前部署到Netlify。”

但他也指出，AX不一定只是改善AI代理的“体验”——考虑循环中的人也很重要。

“有时这完全是关于如何让代理的体验更好，”Biilmann解释说。“你需要考虑的是如何让代理与人协作的体验更好。”

![](https://cdn.thenewstack.io/media/2025/02/ef6d0ce5-optimal-ax.png)

*根据罗伯茨的说法，最佳的AX流量。*

在[公司博客](https://www.netlify.com/blog/the-era-of-agent-experience-ax/)中，Netlify已经成为Devin、Bolt和Stripe等几个合作伙伴的“代理的部署目标”。但Biilmann表示，让代理自动将其站点和应用程序部署到Netlify仅仅是个开始。

“我们也在深入思考如何改进我们的原语，以便为Cursor或Copilot或任何这些[AI编码工具]编写代码。我只是认为这是一种非常强烈的自然趋势，即所有开发人员都将与编码代理一起构建他们的项目。”

换句话说，AX和代理将成为[Netlify的“可组合Web”平台](https://thenewstack.io/netlify-launches-composable-web-platform-for-enterprise-devs/)的关键部分。

## 开放的代理世界

此外，Biilmann希望看到AI代理出现开放标准，类似于Web标准。

“我们还需要开始围绕……我们实际上将如何使Web对代理更好开展一些行业工作？我们可以提出哪些共享标准，以及代理实际上需要Web提供什么？”

> “人们会带来他们想要使用的代理，而不是你希望他们使用的代理。”
>
> – Biilmann

Netlify一直都是开放Web的支持者——坦率地说，这对他们的业务有好处——现在该公司希望支持开放代理。类似于Netlify对其Web开发工具持有所谓的“[framework agnostic](https://thenewstack.io/why-netlify-is-tech-agnostic-and-its-role-in-jamstack-development/)”的观点一样，它希望拥抱各种不同的代理。正如Biilmann所说，“人们会带来*他们*想要使用的代理，而不是你希望他们使用的代理。”

为了启动这一运动，Netlify在[AgentExperience.ax](https://agentexperience.ax/)上创建了一个网站（为了节省您的搜索查询：.ax是奥兰群岛的域名，奥兰群岛是芬兰的一个自治区）。有点像Netlify在2016/17年为[Jamstack创建的网站](https://web.archive.org/web/20171005081251/http://jamstack.org/)一样，Agent Experience网站列出了一些定义和概念，同时也邀请社区参与。
