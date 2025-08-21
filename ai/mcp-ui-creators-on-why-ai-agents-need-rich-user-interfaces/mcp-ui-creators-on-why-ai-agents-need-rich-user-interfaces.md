
<!--
title: MCP-UI 创造者揭秘：AI 智能代理为何需要强大用户界面
cover: https://cdn.thenewstack.io/media/2025/08/3b8063b6-benoit-deschasaux-i-cjnhessuo-unsplashb.jpg
summary: MCP-UI是一个开源项目，旨在为AI代理添加Web用户界面组件，它构建于模型上下文协议(MCP)之上。MCP-UI的目标是简化代理交互，并使公司能够在代理消费的新世界中保持其品牌和用户体验。MCP-UI使用iframe实现安全，并提供React和Web Component两种客户端SDK。开发者可以利用它构建自定义代理或将应用程序集成到外部代理中。
-->

MCP-UI是一个开源项目，旨在为AI代理添加Web用户界面组件，它构建于模型上下文协议(MCP)之上。MCP-UI的目标是简化代理交互，并使公司能够在代理消费的新世界中保持其品牌和用户体验。MCP-UI使用iframe实现安全，并提供React和Web Component两种客户端SDK。开发者可以利用它构建自定义代理或将应用程序集成到外部代理中。

> 译自：[MCP-UI Creators on Why AI Agents Need Rich User Interfaces](https://thenewstack.io/mcp-ui-creators-on-why-ai-agents-need-rich-user-interfaces/)
> 
> 作者：Richard MacManus

[MCP-UI](https://mcpui.dev/) 是一个新的开源项目，它提供了一种向 AI 代理添加基于 Web 的用户界面组件的方法。它建立在已经非常流行的 [模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 之上，该协议标准化了代理的 API 访问。

MCP-UI 可能会对互联网行业产生巨大影响。用专业体育术语来说，MCP-UI 具有非常高的上限，因为它甚至可能 [取代对网站的需求](https://thenewstack.io/mcp-ui-aims-to-replace-old-world-websites-with-ai-agent-uis/) ——至少对于某些类别的在线公司而言。这当然是 Web 开发人员和 Web 设计师现在需要理解和评估的技术。

为了了解更多关于 MCP-UI 的细节以及如何开始使用它，我采访了它的两位创建者，[Ido Salomon](https://www.linkedin.com/in/ido-salomon/) 和 [Liad Yosef](https://www.linkedin.com/in/liadyosef/)。两人最近加入了企业 IT 公司 Monday.com，据 [报道](https://www.calcalistech.com/ctechnews/article/rjorfh8wel) 价值“数百万美元”。此前，Salomon 曾是 Palo Alto Networks 的高级工程师，Yosef 曾是 Shopify 的高级工程师（MCP-UI 已经在 Shopify 部署）。

注意：本文将纯粹关注 MCP-UI 的开源项目，因为 Monday.com 尚未准备好讨论他们将来可能如何使用该技术。但是，很快会发布一篇后续文章，其中我将采访两位 Shopify 工程师，了解他们如何实施 MCP-UI——Yosef 也将对此有所贡献。

[![Shopify MCP-UI](https://cdn.thenewstack.io/media/2025/08/c8bd46fd-shopifyblogimage_04dab3e7-5dbf-4887-bd50-062afb3bd8ae-1-scaled.webp)](https://cdn.thenewstack.io/media/2025/08/c8bd46fd-shopifyblogimage_04dab3e7-5dbf-4887-bd50-062afb3bd8ae-1-scaled.webp)

*Shopify [MCP-UI 示例](https://shopify.engineering/mcp-ui-breaking-the-text-wall)。*

## 为什么需要 MCP-UI？

MCP-UI 于 2025 年 5 月 16 日发布——就在几个月前——当时 Salomon 将 v1.0.1 [发布到他的 GitHub 帐户](https://github.com/idosal/mcp-ui/)。我问这个项目的灵感是什么。

首先，Salomon 回答说，当时大多数代理交互都是基于文本的。然后，他解释了构建 MCP-UI 的两个具体动机。

“所以第一个动机是，我们需要一些不同的东西——一些与我们今天从 Web 应用程序中所了解的更相关的 UI 交互[在代理中]，这将使人们更容易访问。”

第二个因素是使在线公司能够在 Salomon 所谓的“这个代理消费的新世界”中保持其品牌和用户体验——他们的身份。

“所以 MCP-UI 是一种处理这两者的方式，”他补充说。“它既是一种将丰富的用户交互添加到这个代理流程中的方式，[也]允许服务器或应用程序真正保持它们在这个新世界中的身份。”

> MCP-UI 能够“将丰富的用户交互添加到[一个]代理流程中，并允许服务器或应用程序真正保持它们在这个新世界中的身份。”
> 
> **– Ido Salomon, MCP-UI 联合创始人**

Yosef 指出，他们已经开始看到像 ChatGPT 和 Claude 这样的代理生成他们自己的一些 UI——例如，如果你搜索住宿，ChatGPT 中的酒店图像——但这还不够广泛。视觉 UI 的某些方面缺失了。

“你有非常复杂的用户交互，或用户流程——比如在飞机上选择座位，或在场地中选择座位，甚至 [...] 复杂的电子商务流程——你不能期望每个代理都自己生成，”Yosef 解释说。“所以，就像 Ido 说的，我们需要一种弥合这一差距的方法。”

## Iframe 和未来移动考虑因素

目前，MCP-UI 适用于基于浏览器的 UI，尽管两人希望在适当的时候添加原生移动工具。目前，MCP-UI 的一个核心特性是它使用 [\<iframe\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)，这是一种在当前 HTML 页面中嵌入另一个 HTML 页面的 HTML 元素。这似乎主要是由于安全原因。在 GitHub 上的 MCP-UI 自述文件中，它指出：“在所有内容类型中，远程代码都在沙盒 iframe 中执行。”

“我认为这是技术上唯一现实的选择，”Salomon 在谈到 iframe 时说。“我认为 MCP-UI 的核心相当简单。它基本上采用了 MCP [父协议] 的构建块——MCP 不仅可以通过文本进行响应，还可以通过可以包含任何内容的嵌入式资源进行响应。所以这个想法是，我如何获取像嵌入式资源这样的东西，并就此嵌入式资源包含某些东西达成共识。然后主机——你知道，ChatGPT，任何东西——都可以渲染它。以及它如何运行基本上任意的代码，这些代码是不安全的，而不会伤害用户。Iframe 是做到这一点的唯一方法。特别是 sandbox iframe 给你带来了额外的优势。”

他补充说，还有其他内容类型——“比如远程 DOM 和一堆其他东西”——它们更复杂并且有自己的安全模型。

> “MCP 不仅可以通过文本进行响应，还可以通过可以包含任何内容的嵌入式资源进行响应。”
> **– Salomon**

我问他们是否正在考虑针对不同的移动操作系统（例如 iOS 和 Android）的实现，以便（例如）ChatGPT 应用程序可以使用 MCP-UI？

“肯定会有不同的实现，”Salomon 说。“我认为在 Web 中，它要简单得多，因为你受操作系统和实际底层引擎的约束要少得多。因此，做一些事情，比如嵌入 iframe 并且可以对 iframe 做任何我们想做的事情要容易得多。对于移动设备，你有很多不同的约束。”

但他承认，移动操作系统实现将是该项目需要的——“因为世界上很多东西都在朝着代理的移动方向发展。”

这并不是所有需要添加到 MCP-UI 的内容。该项目仍然很新，因此像授权和主题这样的事情仍在开发中。

[![MCP-UI demo](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)](https://cdn.thenewstack.io/media/2025/07/3cf7bfe7-mcp-ui-demo.jpg)

*MCP-UI 演示了将 UI 插入到 Claude 3.7 Sonnet 聊天中。*

## 组件：HTML 和 React 选项

MCP-UI 有两种类型的 SDK：客户端 SDK 和服务器 SDK，用于连接到 MCP 服务器。服务器 SDK 目前仅提供 TypeScript 和 Ruby 版本，但 Python 版本正在开发中。

客户端 SDK 提供了“一个 React 组件和一个 Web Component，以便于前端集成”。这对搭档说，Shopify 正在其集成中使用 Web Components，但大多数其他——例如 [Goose](https://block.github.io/goose/blog/2025/08/11/mcp-ui-post-browser-world/) 和 [Postman](https://www.npmjs.com/package/@postman/mcp-ui-client)——正在使用 React。

“实际上，大多数都使用 React，因为 React 实际上是**氛围编程**的事实上的语言，”Salomon 说。“但是，是的，Web Components 只是为了确保每个人都能安全使用，因为这就是目标。”

> “MCP-UI 可以在客户端使用 React 或 Web Components。”
> 
> **– Liad Yosef, MCP-UI 联合创始人**

Yosef 澄清说，Shopify 的用例与其他用例略有不同。

“所以，MCP-UI 可以在客户端使用 React 或 Web Components，”他说。“Shopify 使用 Web Components 作为实际要交付的 UI 内容，这是在这个项目开始之前 Shopify 中已经存在的东西。因此，Shopify 正在开发一些 Web Components 以在第三方站点中使用，[因此]它们是组成 Shopify UI 的天然候选者。”

如上所述，我们将在下一篇文章中更深入地探讨 Shopify 的实现。

## 图形代理会取代网站吗？

所以现在谈到更大的问题，就 MCP-UI 可能如何发挥作用而言。我问这对搭档是否认为具有嵌入式 UI 的 AI 代理会取代某些在线公司（例如电子商务公司）运营网站的需求？

“我们未来的愿景是，复杂的网站和复杂的 Web 应用程序在未来将会有些过时，”Yosef 回答说。“我们今天已经通过文本 MCP 工具看到，人们[谁]将他们的代理或助手连接到某种 MCP，他们不会浏览网站本身，他们只是通过 MCP 使用它。因此，越来越多的应用程序或服务将使用这些碎片化的部分[通过 MCP-UI]公开其界面，是的，它将取代网站的完整体验。”

> “……复杂的网站和复杂的 Web 应用程序在未来将会有些过时。”
> 
> **– Yosef**

很难看不到 MCP-UI 对电子商务企业——以及任何在线交易的企业的吸引力。但是，还有哪些类型的组织会从使用 MCP-UI 中受益？

“我认为肯定是生产力，”Yosef 回答说（也许暗示了为什么 Monday.com 花了大笔钱招募他们）。“这是我们已经可以看到的东西，人们正在使用代理作为助手来提高他们的生产力。因此，连接生产力工具将允许您使用这些丰富的用户界面，并在您自己的聊天体验中进行简化。”

Salomon 补充说，“今天你需要的大部分东西 [...] 大量的 UI 开销，也许，以某种方式使用，一旦你可以询问代理，并让代理只带给你当时需要使用来做出决定的东西，就会变得容易得多。”

## 开始使用

开发人员应该开始尝试 MCP-UI，以了解它如何适合他们自己的用例。

Yosef 解释说，开发人员应该从两种方式考虑使用 MCP-UI。一种是使用客户端 SDK 构建您自己的自定义代理，以便它支持 MCP-UI。另一种是通过服务器 SDK 将您的应用程序集成到外部代理中。

在第二种用例中，您“试图将它[您的应用程序]分解为人们可以通过 ChatGPT 或 Claude 或他们自己的个人助手使用的可用块，”Yosef 说。

无论哪种情况，都要为互联网做好准备，在那里，更多的互动将通过代理发生。Web 不会消失——它是 MCP-UI 的核心——但人们进行交易和在线消费的方式正在发生变化。

“仅 MCP 的应用程序即将到来，”Yosef 声称，这表明一些公司已经开始超越网站和智能手机应用程序。“我们从实际公司那里听说过，实际上已经开始这样思考了。”

为了进一步探索，开发人员应该查看 [项目网站](https://mcpui.dev/) 以获取技术信息，并 [加入 Discord](https://discord.gg/CEAG4KW7ZH) 以与社区联系。