
<!--
title: 为何无头浏览器是 AI Agent 的关键技术
cover: https://cdn.thenewstack.io/media/2025/06/77e84897-sung-jin-cho-8cip0y9y8no-unsplashc.jpg
summary: Browserbase CEO Paul Klein IV 认为每个 AI 代理都需要一个无头浏览器作为与传统互联网交互的桥梁。Browserbase 已经转型为“适用于您的 AI 的 Web 浏览器”，并获得了 4000 万美元的 B 轮融资。无头浏览器在 AI 代理中用于信息收集和任务执行，主要有视觉 Web 代理和文本 Web 代理两种类型。
-->

Browserbase CEO Paul Klein IV 认为每个 AI 代理都需要一个无头浏览器作为与传统互联网交互的桥梁。Browserbase 已经转型为“适用于您的 AI 的 Web 浏览器”，并获得了 4000 万美元的 B 轮融资。无头浏览器在 AI 代理中用于信息收集和任务执行，主要有视觉 Web 代理和文本 Web 代理两种类型。

> 译自：[Why Headless Browsers Are a Key Technology for AI Agents](https://thenewstack.io/why-headless-browsers-are-a-key-technology-for-ai-agents/)
> 
> 作者：Richard MacManus

在[本月的人工智能工程师世界博览会](https://www.youtube.com/watch?v=YRGjll7uu5w)上，无头浏览器供应商 Browserbase 的 CEO [Paul Klein IV](https://www.linkedin.com/in/paulkleiniv) 说：“每个 AI 代理都需要一个 Web 浏览器。”

什么是无头浏览器？[简单来说](https://en.wikipedia.org/wiki/Headless_browser)，它是一个没有图形用户界面的 Web 浏览器。直到最近，它们主要用于运行自动化 Web 应用程序测试以及 Web 抓取和屏幕截图。多年来，涌现了三个开源项目来运行这些类型的任务：Puppeteer、Playwright 和 Selenium。Playwright 是最新的——它由 Microsoft 于 2020 年 1 月推出——也是最受欢迎的。

实际上，仅仅在过去一年中，无头浏览器才出现了另一种全新的用例。突然之间，它们已成为一些人（包括 [Microsoft](https://blogs.microsoft.com/blog/2025/05/19/microsoft-build-2025-the-age-of-ai-agents-and-building-the-open-agentic-web/) 和浏览器公司 [Opera](https://www.operaneon.com/)）所谓的“代理网络”的关键组成部分。

[AI 代理](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)是自主软件应用程序，通常负责在互联网上收集信息——然后将这些信息传递给用户，或者根据这些信息采取行动（例如在电子商务网站上购买商品）。事实证明，无头浏览器是这些 AI 代理的理想基础设施。

> “如果我们希望 AI 代理与传统的互联网的其他部分进行交互，他们需要一座桥梁。我真的相信浏览器就是那座桥梁。”
> **– Paul Klein IV, Browserbase CEO**

Browserbase 已经大力转型以利用这个新市场。当该公司于 2024 年 1 月成立时，它将自己宣传为[一家浏览器基础设施公司](https://web.archive.org/web/20240101000000*/https://www.browserbase.com/)。其主要产品是 Puppeteer、Playwright 和 Selenium 的托管服务。现在，仅仅 18 个月后，Browserbase 将自己描述为“适用于您的 AI 的 Web 浏览器”。

本月早些时候，Browserbase 宣布了一轮大规模的 B 轮[4000 万美元融资](https://www.browserbase.com/blog/series-b-and-beyond)，表明无头浏览器现在是一项大生意。在公告帖子中，Klein 提出了以下观察：“浏览的未来是选择性自动化。人类仍然会做那些令人愉快的、以发现为导向的任务。但是重复性的、耗时的工作应该由软件来完成。这就是我们正在构建的。”

## 无头浏览器如何在 AI 代理中使用

在他的 AI 工程师世界博览会演讲中，Klein 强调，大规模地完成自动化浏览器工作是其价值主张的关键。“通过 Browserbase，我们可以让您在云中运行数千个无头浏览器，以供代理控制，”他说。

Browserbase 今年还紧跟另一个巨大的趋势：[MCP 服务器](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)。根据 Klein 的说法，Browserbase 拥有“最受欢迎的浏览器自动化 MCP 服务器”。

[![](https://cdn.thenewstack.io/media/2025/06/f8aeaaa1-browserbase-mcp-server-june25.jpg)](https://cdn.thenewstack.io/media/2025/06/f8aeaaa1-browserbase-mcp-server-june25.jpg)

*Browserbase MCP 服务器。*

他补充说，开发人员选择 Browserbase 的 MCP 服务器的部分原因是，在“不性感的互联网”（他的术语）中有数千个用例，他们的客户没有自定义 MCP 服务器。因此，使用内置 MCP 服务器的无头浏览器（如 Browserbase 所做的那样）是一种有效的解决方案。

“您有 AI 代理和传统的互联网，”Klein 解释说。“你知道，DMV 不会很快拥有 MCP 服务器。我的理发店不会为我打开 GraphQL API 来安排理发，尽管我一直在恳求 John [可能是他的理发师] 这样做。他有更重要的事情要做。因此，如果我们希望 AI 代理与传统的互联网的其他部分进行交互，他们需要一座桥梁。我真的相信浏览器是 AI 与互联网其他部分之间的桥梁。”

他指出，“传统的互联网”上的许多组织不一定拥有 MCP 服务器，但他们可能有一个网站。（编者注：除非他们[只有一个 Facebook 页面](https://mastodon.art/@RMiddleton/114688285464490695)！）

“我认为现在人们使用了很多首字母缩略词，”Klein 继续说道。“你知道，你有 MCP，你有 A2A，你有 OpenAPI。但如果这些都不可用，你可以做一些可能被认为是愚蠢的事情：你只需使用一个网站。而且网站就在那里，有很多。有数十亿个网站。当您的用户将提示您的代理执行某些操作时，您可能并不总是可以使用第一方集成。”

[![](https://cdn.thenewstack.io/media/2025/06/709a6edd-browserbase-just-the-website.jpg)](https://cdn.thenewstack.io/media/2025/06/709a6edd-browserbase-just-the-website.jpg)

*“只需使用该网站。”*

如果像 Browserbase 这样专注于 AI 的公司是可信的，那么将越来越多地由 AI 代理访问您的商业网站，这意味着人类 Web 访问量将相应下降。但是，这些代理究竟是如何为其人类用户获取正确信息的？

Klein 回顾了当前可用的各种类型的 AI 代理以及它们如何控制浏览器。他从过去一年左右率先推出 Web 代理的产品开始——包括 WebVoyager、Adept 和 OpenAI 的 Operator。他将他们的方法描述为：“采用一个模型，然后生成一些代码来控制浏览器，通常通过解析页面上的 DOM、HTML 和 CSS。”

[![](https://cdn.thenewstack.io/media/2025/06/f32cefc8-browserbase-types-of-agents.jpg)](https://cdn.thenewstack.io/media/2025/06/f32cefc8-browserbase-types-of-agents.jpg)

*什么是 Web 代理？*

他继续说道，我们现在所处的位置是，有两种主要的 Web 代理类型。

视觉 Web 代理通常使用无头浏览器来获取屏幕截图“作为模型的上下文”，并且它们“可能会对屏幕截图进行一些标记，以指示要单击哪个框，”Klein 说。

文本 Web 代理“主要使用 HTML 作为模型的上下文”——Playwright 是这种方法中流行的工具。

[![](https://cdn.thenewstack.io/media/2025/06/7d8425b5-browserbase-two-types-of-agents.jpg)](https://cdn.thenewstack.io/media/2025/06/7d8425b5-browserbase-two-types-of-agents.jpg)

*两种类型的代理。*

顺便说一句，Browserbase 有一个名为 Stagehand 的 Playwright 开源框架——适用于 Python 和 Node.js。在最近[与 Brian Douglas 的播客采访](https://www.youtube.com/watch?v=ZHPY5QLIm0o)中，Klein 说 Stagehand 是“Playwright 的超集”，并且它在“Playwright 之上添加了更多 AI 功能”。

Stagehand 是 Browserbase 在 AI 代理方面雄心的关键。在另一次播客采访中，这次[与 Latent Space](https://www.youtube.com/watch?v=YUGItptS5hI) 合作，Klein 将 Stagehand 描述为“用于构建 Web 代理的框架”，其中开发人员可以调用三个 API“工具”：Act、extract 和 observe。

回到 AI 工程师世界博览会的演讲，Klein 说“计算机使用”模型是一种新兴的 Web 代理类型。顾名思义，它是指在 UI 任务和“Web 轨迹”（AI 代理浏览网站时的一种工作流程）上训练 AI 模型。

[![](https://cdn.thenewstack.io/media/2025/06/2402f5ae-web-trajectories-june25.jpg)](https://cdn.thenewstack.io/media/2025/06/2402f5ae-web-trajectories-june25.jpg)

*Web 轨迹。*

## 结论

Klein 指出，目前“在教 AI 如何浏览 Web 方面正在发生很多创新 [...]——而且这东西越来越好。” 当然，如果 AI 代理要不辜负它们的炒作，那么能够有效地自主浏览网站将至关重要。

您可以争论说，对于 Web 发布商来说，他们的内容越来越多地由 AI 代理而不是人类浏览是否是一件好事（这是[我非常关心的问题](https://thenewstack.io/the-future-of-websites-in-the-age-of-ai-and-seo-decline/)）。但是，很难反驳浏览器基础设施是未来 [AI 开发堆栈](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) 的关键组成部分。Browserbase 似乎完全适合这个市场。