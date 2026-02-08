<!--
title: Vercel 的 json-render：迈向生成式UI的关键一步
cover: https://cdn.thenewstack.io/media/2026/01/4b1a7f30-generative-ui.jpg
summary: Vercel推出json-render，旨在实现AI即时生成UI，简化开发。该工具让开发者定义AI护栏，用户通过自然语言描述需求，AI自动生成并渲染JSON。文章指出，前端开发者重心将从UI构建转向代理行为和上下文工程。JavaScript仍具重要性。Vercel将其视为从“前端云”到“AI云”的战略转型，强调未来由token和代理主导。
-->

Vercel推出json-render，旨在实现AI即时生成UI，简化开发。该工具让开发者定义AI护栏，用户通过自然语言描述需求，AI自动生成并渲染JSON。文章指出，前端开发者重心将从UI构建转向代理行为和上下文工程。JavaScript仍具重要性。Vercel将其视为从“前端云”到“AI云”的战略转型，强调未来由token和代理主导。

> 译自：[Vercel’s json-render: A step toward generative UI](https://thenewstack.io/vercels-json-render-a-step-toward-generative-ui/)
> 
> 作者：Loraine Lawson

Vercel 最近发布了一款新的开源工具，名为 [json-render](https://json-render.dev/)，这标志着向生成式用户界面 (UI) 迈进了一步，生成式UI是 Vercel 为AI生成网页界面创造的一个术语。

“如果大型语言模型 (LLM) 不仅仅是生成文本，还能即时为我们提供用户界面，那会怎样？”Vercel 创始人兼 CEO Guillermo Rauch 问《The New Stack》。“我们基本上是将AI直接接入到渲染层。”

他表示，AI 和基础设施很快就能支持[生成式UI](https://thenewstack.io/a-guide-to-generative-ai-for-devops-team-managers/)。Json-render 是这幅拼图中的一部分。

开发者可以使用 json-render 来定义 AI 的护栏，例如 AI 可以使用哪些组件、动作和数据绑定。然后，终端用户可以通过 AI 提示词用自然语言描述他们想要的内容。AI 随后生成 JSON，并随着模型的响应逐步渲染。

Rauch 称其为“颠覆性技术”，因为它绕过了软件生产的步骤。它已作为 Vercel Labs 的一部分进行部署，Vercel Labs 专门用于 Vercel 的实验性项目。尽管它被视为一个早期研究原型，但这项技术已经“非常成熟”，他表示。

Rauch 表示，一位开发者成功地在 Quinn 上运行了 json-render，Quinn 是一个低参数的本地部署开源模型。

“如果你从这里推断，你可以想象这样一个世界：你打开一个网站，UI 就会使用 json-render 为你自发生成，”他说。“把它看作是一个基础设施。”

“它使任何公司都能将 AI 转化为 UI，并能接入到系统中，”他说。“再说一遍，目前它仍处于实验阶段，但如果你想将这种生成式 UI 能力嵌入到系统中，你就会使用 json-render。”

## Json-render 深度解析

根据 Rauch 的说法，Json-render 是一款酝酿了数十年的工具。他赞扬了 Vercel 软件工程师 [Chris Tate](https://www.linkedin.com/in/ctatedev/) 在该工具上的工作，并补充说，json-render 包含了在大型语言模型 (LLM) 出现之前，对生成式 UI 挑战长达 10 年的思考。

Json-render 拥有一套有主见的预定义组件，赋予 AI 自由组合的能力。

“我们不希望 AI 过于创新，以至于改变你的品牌指南，如果看起来不协调，它还会改变你的色彩系统，”Rauch 说。“工程师将负责策划所渲染系统的品牌标识、外观和感觉。”

他补充说，它甚至可以用于按需构建游戏 UI。它与模型和框架无关，因此可以与你选择的 JavaScript 框架一起使用。

Rauch 设想了一个未来网络：用户访问他们喜欢的电商网站时，网站会自动提醒用户过去的订单，更新物流信息，或者提供定制的产品推荐。

“它基本上自动化了程序员（甚至是AI驱动的程序员）创建这些 UI 规则的工作。它只是在数学层面上完成了这一切，”他说。

## 前端开发者该如何准备？

Rauch 相信技术“非常接近”实现生成式 UI——他预测我们今年将看到生成式 UI 的一瞥——所以我问这对前端开发者意味着什么？

Rauch 给前端开发者提出了一个警告：专注于交付代理。

“这可能对企业和开发者来说是一个警钟，如果你不开始交付代理，你可能会错过未来的互联网，”他说。“你可能会被淘汰。你可能无法接入新的协议。”

他指出 [Google](https://cloud.google.com/?utm_content=inline+mention) 最近发布的 UCP（一种电子商务协议）就是一个开发者会想要“接入”的协议示例。

> “我仍然鼓励人们学习使用 JavaScript。但我的建议是，瞄准未来的互联网。尝试部署一个代理。了解这些模型是如何工作的。尝试使用 json-render 进行实验。”
>
> **— Guillermo Rauch，Vercel 首席执行官兼联合创始人**

尽管不再需要开发者来构建 UI，但他们在定义代理行为方面仍然扮演着重要角色。Shopify CEO [Tobias Lütke](https://ca.linkedin.com/in/tobiaslutke) 将此称为[上下文工程](https://www.linkedin.com/posts/mattpaige_the-shopify-ceo-has-done-it-again-coining-activity-7341816822641377281-A6Fm/)。

“工程师将退居幕后，不再过多关注 UI 层，而是专注于代理的行为，确保其拥有正确的数据、正确的上下文，并进行评估，”Rauch 说。“也许行业的下一步将是退后一步，更多地关注那个引擎，而不是‘最后一英里’的 UI。”

那么 JavaScript 呢？Rauch 指出，这种流行的语言在每一代大型软件中都幸存了下来。他预测它也将在这次向生成式 UI 的转变中幸存下来。

“当云计算和无服务器出现时，JavaScript 扮演了核心角色。当服务器渲染发生，渲染回到服务器时，JavaScript 扮演了核心角色，”他说。“现在我们看到了 AI SDK 的情况。今天创建代理最简单的方式又是 JavaScript。”

“我仍然鼓励人们学习使用 JavaScript。但我的建议是，瞄准未来的互联网。尝试部署一个代理。了解这些模型是如何工作的。尝试使用 json-render 进行实验。”

## Vercel 的 AI 长期战略

过去一年，Vercel 发布了多款 AI 工具，包括 AI 云、AI SDK 和 AI 网关。我问 Rauch 这些零散的产品是否构成了一个宏大的战略。

> “Vercel 的第二章将由 token 和代理主导。我们称之为 AI 云。”
>
> **— Guillermo Rauch**

“是的，当然，”Rauch 说。“Vercel 的第一章由页面和像素主导。我们称之为前端云。”

“Vercel 的第二章将由 token 和代理主导。我们称之为 AI 云。因此，AI 云，我实际上在[我的博客](https://rauchg.com/2025/the-ai-cloud)上写过，就是你需要新的服务、新的框架、新的标准这个想法。”

Rauch 补充说，通过 AI SDK，Vercel 创建了许多底层设施，使其能够将模型流式传输到 UI。

“需要提及的一个重要事情是，在过去几年里，我们一直在投资基础设施，从‘一站式’（你访问一个网站，一次性获得所有内容）转向‘你可以随着时间流式传输’的理念，”他说。“这是一项赋能技术。”

他说，公司越来越多地看到 AI 代理部署在其平台或 [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) 上，Vercel Sandbox 允许开发者在隔离的、临时的 Linux 虚拟机中运行任意代码。

“代理需要一个我们可以完全信任它们的地方，”他解释道。“它们可能会犯错，所以我们需要围绕它们的行为创建一个沙盒。”

他补充说，这是 Vercel 从一开始就致力于做的事情的延续，即普及云服务的访问，同时消除所有令人头疼的问题，例如配置。Rauch 将其称为自动驾驶基础设施。

“如果你使用 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 或者 Google Cloud，那就像驾驶一辆手动挡汽车，”他说。“Vercel 就像云计算领域的 Waymo 或特斯拉——完全自动驾驶。”