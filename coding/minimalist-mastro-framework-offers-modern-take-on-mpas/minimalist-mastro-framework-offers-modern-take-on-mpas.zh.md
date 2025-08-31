计算机科学家和[前端](https://thenewstack.io/introduction-to-frontend-development)开发人员[Mauro Bieg](https://github.com/mb21)认为，700 行代码出错的可能性不大。

Bieg 告诉 The New Stack：“如果我作为软件开发人员学到了什么，那就是代码行数越少越好。可以出错的东西越少，需要维护的东西也越少。”

这就是 Bieg 创建 [Mastro](https://github.com/mastrojs/mastro/) 的原因，Mastro 是一个现代 JavaScript 元框架，旨在构建多页面应用程序 (MPA)。 他说，它的核心大约有 700 行 TypeScript 代码。 Bieg 说，对于想要采用简化的方法来构建多页面应用程序的初级开发人员和经验丰富的开发人员来说，这是一个很棒的框架。

## 前端开发经验教训

Bieg 在 [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/) 和后来的 [Ruby on Rails](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) 的环境中长大。 他还记得“响应式设计”这个术语何时被创造出来，以及渐进式增强意味着什么。 他尝试过 Angular，但最终选择了 [React](https://thenewstack.io/react-compiler-is-coming/) 来开发具有大量交互性的项目。 对于基本的网站，他仍然使用 Ruby on Rails。

后来，他获得了一个前端团队负责人的职位。 该组织有一个现有的 [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/) 应用程序。

“我想当然地认为，为什么不呢？React 的开发确实很棒，而且如果他们想出如何用它来制作普通网站，我想那也很酷。似乎每个人都在使用它，所以它不会太糟糕。”

他继续说，他亲身体验到了。

“至少对于我们的用例（一份报纸网站）来说，客户端中 99% 的 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 有效负载完全是浪费，”他说。 “我们有一些交互式小部件，比如幻灯片、菜单等，但 React 正在水合的 DOM 中 99% 是完全静态的。”

他最终选择了 [带有 islands 架构的 Astro](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)，因为它允许他们逐步过渡现有的 React 组件，而无需完全重写。 然而，在迁移之前，他离开了公司，成为一家初创公司的首席技术官兼唯一开发人员。

Astro 在那份工作中似乎也很合适。 他将其与 [Solid.js](https://thenewstack.io/solid-js-creator-outlines-options-to-reduce-javascript-code/) 而不是 React 配对。 他发现，Solid 提供了与 React 相同的功能，但性能更高。

> 实际上，你能做到多精简？

“我仍然非常喜欢 Astro，并且钦佩他们出色的营销，将 MPA 和 island 架构重新带回主流 JS 讨论中，”他说。 “但时不时地，我会遇到一些奇怪之处和粗糙的地方，他们在某种程度上将自己设计到了一个死角，现在由于向后兼容性和惯性而卡在那里。”

这让他想知道：实际上，你能做到多精简？你能构建的最简单、最小、维护成本最低的 MPA 框架是什么？它仍然允许开发人员轻松完成 95% 的用例，但复杂性要低得多？

“似乎如果你专注于 MPA，这将允许你删除大多数网站的绑定器，”他说。 “删除绑定器将删除整个间接层，如果出现问题，你需要调试它。”

## MPA 的复兴？

Next.js、[Nuxt](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/)、Astro、SolidStart、[SvelteKit](https://thenewstack.io/dev-news-sveltekit-2-0-state-of-rust-survey-and-ai-on-apple/) 和 [Qwik](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/) 都使用绑定器/转译器，例如 [Vite](https://thenewstack.io/vites-creator-on-a-unified-javascript-toolchain-and-vite/) 或 [Webpack](https://thenewstack.io/airbnb-moves-from-webpack-to-metro-enjoys-shorter-build-times/)，并且除了 Astro 和 Qwik 之外，它们都是 SPA，他在 [去年的一篇博文](https://mb21.github.io/blog/2024/04/13/mpa-no-bundler-javascript-meta-framework-separating-client-server-code.html) 中写道。 *（编者注：SolidStart 和 SvelteKit 被认为是混合框架。SolidStart 可以创建 SPA 和 MPA，而 SvelteKit 采用了一种兼具两者优势的方法。）*

他在帖子中写道：“我希望有一个现代 JS 元框架可以摒弃这两个约定，而是选择优化简单性，并利用浏览器内置功能而不是客户端 JavaScript。”

这一愿景指导了 Mastro 的创建。 Mastro 是一个由[第一性原理](https://addyosmani.com/blog/first-principles-thinking-software-engineers/)构建的 [静态站点生成器](https://thenewstack.io/get-back-basics-static-website-generators/) 和 Web 框架。 它提供了一个简单的基于文件的路由器，一些可组合的函数来返回 HTML 和标准 `Response` 对象。

它构建 MPA，因为对于大多数用例来说，现代浏览器可以比 JavaScript 更好地处理客户端路由，Bieg 认为。

Bieg 通过电子邮件采访告诉 The New Stack：“MPA（终于）迎来了复兴。”

> “我希望有一个现代 JS 元框架可以摒弃这两个约定，而是选择优化简单性，并利用浏览器内置功能而不是客户端 JavaScript。”
> **– Mauro Bieg，前端开发人员和计算机科学家**

Bieg 在 [2023 年的一篇文章](https://mb21.github.io/blog/2023/09/18/building-a-modern-website-ssg-vs-ssr-spa-vs-mpa-svelte-vs-solid.html#single-page-app-spa-vs-multi-page-app-mpa) 中提出了支持 MPA 的理由。 他指出，对于 SPA 来说，其理念是开发人员用前期的页面加载时间来换取以后更好的用户体验。

“页面导航后，你不需要重新初始化所有内容，”他说。 “而且可以说，SPA 的页面转换比浏览器过去拥有的更好。”

所有这些都很好，但自那时以来，浏览器已经得到了改进，并且这种平衡正在从 SPA 转移开来，他认为。

“现代浏览器在页面之间不再有白色闪烁，它们具有后退/前进缓存和服务工作线程以实现离线功能等，”他写道。

他仍然看到了 SPA 的用例——例如，在页面导航期间播放音频或视频，或者以其他方式在 DOM 中保持状态（如光标位置），而这些状态无法轻易地保存在 localStorage 中。

“我的看法是，99% 的网站都应该是 MPA，”他说。 “除非你正在构建下一个 Figma 或 Google Docs，否则在我看来，你最好使用一些交互式 islands 架构来构建 MPA，如果你想润色内容，请使用 CSS 视图转换，并确保你不会破坏浏览器的 [bfcache](https://developer.mozilla.org/en-US/docs/Glossary/bfcache)。”

使用 MPA，开发人员可以从 JavaScript 包大小的减小中获益。

“[他写道](https://mb21.github.io/blog/2023/09/18/building-a-modern-website-ssg-vs-ssr-spa-vs-mpa-svelte-vs-solid)：“让浏览器处理它被构建来做的事情：页面导航、滚动恢复、页面缓存、HTML 流式传输——并且返回 HTML 的 `HTTP GET` 比 [RSC（React 服务器组件）](https://thenewstack.io/frontend-schism-will-react-server-components-destroy-react/) 的 [JSX](https://thenewstack.io/beyond-jsx-rethinking-the-component-model-in-frontend/) 流更容易调试。”

## Mastro 的数据获取、错误处理方法

对于数据获取，Mastro 使用 [标准 fetch 函数](https://github.com/mastrojs/mastro/blob/main/examples/todo-list-server/routes/todo-list.client.ts)，[Deno](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/) 和 [Node.js](https://thenewstack.io/a-backend-for-frontend-watt-for-node-js-simplifies-operations/) 也支持该函数，他说。

它也不固执于错误处理。 他正在考虑有一天在指南、一个单独的模块或一个单独的导出（例如“mastro/result”）中添加一个小的类似 Rust 的“Result”类型和一些辅助函数。

他通过电子邮件说：“我认为没有必要在 Mastro 核心中对此过于固执己见。有些人可以接受处理非类型化的异常，这在 JavaScript 世界中一直是默认设置。”

Mastro 使用 Deno 作为其 [运行时引擎](https://www.pcmag.com/encyclopedia/term/runtime-engine)。

他写道：“我想从一些干净的东西开始，没有 Node 20 年发展的包袱，并尽可能多地依赖该平台。例如，Deno 带有 'Deno.serve'，它接受一个 '(req: Request) => Response 处理程序'，这是一个很棒的简单 API。”

也就是说，[Bun](https://thenewstack.io/dev-news-react-19-bun-comes-to-angular-and-github-ai-fund/) 和 Node.js 兼容性在他的待办事项清单上。

## Reactive Mastro

Mastro 有自己的响应式 GUI 库，名为 Reactive Mastro。 虽然开发人员可以将任何客户端库（如 HTMX 甚至 jQuery）与 Mastro 一起使用，但 Reactive Mastro 是 Bieg 对响应式客户端库的最小化尝试。 他说，它也朝着另一个方向发展：开发人员可以将 Reactive Mastro 与任何 HTML 生成工具（如 PHP、Ruby on Rails 等）一起使用。 他在文档中解释了 [他为什么采取这种方法](https://mastrojs.github.io/reactive/why-reactive-mastro/) 以及它与其他框架的比较。

Mastro 还使用 maverick-js/signals 库来实现信号。

他写道：“Mastro 和 Reactive Mastro 真正共享的是最小化理念（是的，还有 html 模块）。我希望信号能够尽快标准化（他们正在努力），然后我几乎可以将 Reactive Mastro 的大小减半。”

## Mastro 为开发人员提供的功能

Bieg 列出了 Mastro 对 [前端开发人员](https://roadmap.sh/frontend) 的好处：

* 需要理解的东西更少。 他说：“这些函数可以很好地组合在一起，因此你不需要学习另一个函数来做基本上相同的事情。例如，与其他框架不同，Mastro 不关心你通过网络发送 HTML 还是 JSON，你只需给它一个标准的 `Response` 对象，发送 XML 只需四行代码。 顺便说一句，处理程序函数（req: `Request`）”
* 更多控制权。 他说：“Mastro 实际上并没有做太多事情，所以你非常接近底层运行时（例如，用于服务器端 JavaScript 的 Deno，或用于 HTML、CSS 和客户端 JS 的浏览器）。Mastro 从不在你的页面中自动注入任何内容。如果你在你的页面中看到一些奇怪的东西，它可能是一个浏览器扩展，比如广告拦截。”

他写道，如果说在实现 Mastro 时有什么不太简单的事情，那就是基于文件的路由器。

他说：“我只是希望人们能够将 HTML 或 CSS 文件放入 **'routes/** 文件夹' 中，并让 Mastro 像在美好的 Apache/PHP 时代一样为它提供服务。这是一个开始项目的绝佳方式。”

此外，由于 Mastro 非常小，因此它可以快速加载到边缘，如果开发人员加载了太多代码，他们经常会在边缘遇到冷启动缓慢的问题，他说，

他写道：“因为它非常小，你也可以在浏览器中轻松运行它，就像使用 Mastro VSCode for Web 扩展一样，我认为这实际上是第一个完全在浏览器中运行的静态站点生成器。Eleventy 也在努力实现它，但在发布时尚未交付该功能。”

## Mastro：没有臃肿、没有 VC 资金、没有托管

Mastro 可用于构建当今 Web 上的大多数项目，但它也非常适合刚接触 JavaScript 的初学者，他说。 事实上，他编写文档时，实际上是为初学者编写的教程，如果你是 Web 开发老手，可以选择跳过。

使用 Mastro，默认情况下没有绑定器，也没有客户端 JavaScript。 网站上还指出，没有臃肿、没有 VC 资金来“防止最终的恶化”、没有要向你出售的托管服务，也没有“更新跑步机”。

该网站指出：“我们使用该平台和[几乎没有依赖项](https://jsr.io/@mastrojs/mastro/dependencies)，这使我们能够保持事物的小型和低维护性。” 它说“我们”，但实际上现在只有 Bieg。 他补充说，只有 700 行代码，维护起来并不难。

但 Bieg 确实希望获得社区的反馈和建议。

他说：“我希望围绕它形成某种社区，分享食谱、文档，甚至是可以与 Mastro 很好地协同工作的库。目前，我看到这种情况主要发生在 GitHub 问题中，但也许很快就可以开设一个 Discord 或 Discourse 了。现在，我仍处于宣传阶段，看看 Mastro 的哪些方面会引起人们的共鸣，以及它会吸引哪些人群。”