# Astro：从静态网站生成器到 Next.js 竞争对手的旅程

![Astro 从静态网站生成器到 Next.js 竞争对手的旅程的特色图片](https://cdn.thenewstack.io/media/2024/03/70ae1f09-nasa-gywfpvi2jzm-unsplash-1024x677.jpg)

在 Netlify 最近的开发者调查中，Astro 是 [增长最快的 Web 框架](https://thenewstack.io/web-development-in-2023-javascript-still-rules-ai-emerges/)，无论是使用率还是满意度。虽然它仍然落后于当前占主导地位的框架 Next.js，但 Astro 因其 [更简单的 Web 开发方法](https://thenewstack.io/keep-it-simple-frameworks-netlify-ceo-praises-astro-remix/) 而受到赞扬。

[Astro](https://astro.build/) 的吸引力之一在于它并不声称自己是 Web 开发的瑞士军刀。在它的主页上，Astro 谦虚地宣称自己是“面向内容驱动网站的 Web 框架”（尽管不那么谦虚的是，Astro 还表示它“为世界上最快的网站提供支持”）。

## 较少的 JavaScript

Astro 的一个突出特点是它不像其他流行框架那样使用大量 JavaScript。它“默认情况下无 JS”——这意味着 Astro 组件不会在客户端渲染，而是“在构建时或按需使用服务器端渲染 (SSR) 渲染为 HTML”。

即使你不想完全放弃 JavaScript，许多开发者也在采用 *减少* JavaScript 的方法来构建网站。在 [The New Stack 的教程](https://thenewstack.io/how-to-use-astro-with-a-sprinkling-of-react/) 中，Paul Scanlon 解释了他如何将他的个人网站从 React 框架迁移到 Astro，“并加入了一点 JavaScript”。这得益于 Astro 的“岛屿”架构。[Astro 的文档](https://docs.astro.build/en/concepts/islands/) 将“岛屿”定义为“页面上的任何交互式 UI 组件”，并邀请开发者将岛屿视为“漂浮在一片静态、轻量级、服务器渲染的 HTML 海洋中的交互式小部件”。

关键在于，正如 Astro 所说，一个岛屿消除了“将整个网站作为单个大型 JavaScript 应用程序（也称为单页应用程序或 SPA）进行水化和渲染”的需要。

岛屿也意味着对 React 的需求减少，React 是流行但 [经常被过度使用](https://thenewstack.io/2023-web-tech-check-in-react-performance-pwas-ios-browsers/) 的 JavaScript 库。正如 Scanlon 在他的帖子中所说，“React 很棒，但你的网站每一页都需要它吗，还是只需要在网站周围的几个“岛屿”中？”

## Astro 现在可以与任何主流 Web 框架媲美

开发者喜欢 Astro 的原因在于其方法的明显简单性，但随着每个新版本的发布，它都在增加更多功能。

[Astro 3.0](https://astro.build/blog/astro-3/) 于 2023 年 8 月底发布，具有图像优化和对视图转换 API 的支持。[Astro 4.0](https://astro.build/blog/astro-4/) 于 12 月发布，具有新的“开发工具栏”，并 [宣称](https://twitter.com/astrodotbuild/status/1732104305673634140)“构建速度提高 80%”。

在最近在 CFE 上的一次演讲中，运营着流行 [YouTube 频道](https://www.youtube.com/@JamesQQuick) 的 JavaScript 开发者 James Q Quick 指出，大多数人开始使用 Astro 是因为它被称为“静态优先”框架——换句话说，它非常擅长生成静态 HTML 页面（当然，这是内容网站的基础）。但是，Quick 说，Astro 可以做得更多。

他说：“Astro 可以做几乎所有像 Next.js 和 SvelteKit 等主流框架可以做的事情。” “它非常强大，非常灵活，非常简单。”

在 1 月份的*Modern Web*播客的 [一集中](https://www.youtube.com/watch?v=2RL21V48Xqg)，Quick 解释了 Astro 如何成为一种下一代 Gatsby。他的个人博客之前在 Gatsby 上，他开始将其迁移到 Next.js，这是他在工作中花费大量时间使用的框架。但在此过程中，他试用了 Astro，并很快被开发者体验所吸引。因此，他放弃了 Next.js，而是将他的网站迁移到了 Astro。

然后，当 Astro 开始添加更多服务器功能以赶上 Next.js 提供的功能时，Quick 更加印象深刻。

他说：“我喜欢他们 [Astro] 从仅仅是静态优先转向真正首先实现那种体验 [然后] 转向服务器的转变。” “我敢打赌，他们将继续在服务器上添加特性和功能，但他们会考虑到出色的开发者体验，因为他们已经通过他们已经完成的所有其他事情证明了这一点。”

Quick 说，最终，Astro 在功能上将与 Next.js 媲美。

## 集成

Astro 的另一个卖点是它的
## 集成

[集成](https://docs.astro.build/zh-cn/guides/integrations-guide/)与 UI 框架，如 React、Vue、Svelte 和 Solid。这意味着你可以引入你在其他框架中编写的组件。Astro 还集成了 Tailwind 和 MDX 等工具，“只需几行代码”。

“我不知道为什么其他框架不包含这个；对于你经常要做的事情，Astro 集成了可以做这件事的功能，”Quick 在他的 CFE 演示中说道。他补充说，“Next.js 并没有真正拥有这个——他们只有 NPM 包。”

Scanlon 在 Astro 中使用了 React 集成，以便为他的网站制作一个交互式联系表单。但他的网站的其余部分是纯静态的。“我认为这种逐步选择加入或退出 React 的方法提供了一个很好的折衷方案，”他写道，“它将允许你解决迁移问题，而无需深入细节并重构每个组件。”

## 对 SEO 更好？

Astro 的优点在于它介于 Eleventy 和 Hugo 等框架的静态网站生成器方法，以及 Next.js、Vue 等的完全 JavaScript 世界之间。你可以使用 Astro 采用 HTML 和 CSS 优先的方法，但“轻松地”在 Astro 中“点缀”JavaScript（正如 Scanlon 所说）。

Astro 的创建者 Fred K. Schott 也 [最近建议](https://twitter.com/FredKSchott/status/1744842592905552227) 当 Google 退出“众所周知的及格指标（首次输入延迟或 FID）并采用更困难的东西（交互到下一次绘制或 INP）”时，框架的性能将会下降，[特别是对于](https://thenewstack.io/astro-creator-new-web-metric-will-hurt-js-framework-sites/)基于 Nuxt 和 Next.js 构建的网站。

1 月底， [Google 宣布](https://developers.google.com/search/blog/2023/05/introducing-inp) INP “将于 2024 年 3 月 12 日取代 FID 成为核心网络指标的一部分”，因此我们将在下周了解 Astro 网站与 Next.js 相比的表现如何。

无论如何，如果你是一位正在寻找减少对 JavaScript 依赖的方法的开发人员，那么 Astro 非常值得一试。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。