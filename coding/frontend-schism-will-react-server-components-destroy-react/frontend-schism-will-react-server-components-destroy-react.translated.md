# 前端分裂：React Server Components 会摧毁 React 吗？

![Featued image for: Frontend Schism: Will React Server Components Destroy React?](https://cdn.thenewstack.io/media/2024/09/b6631870-react-shatter-1200-1024x576.png)

“有一点我很清楚，React Server Components 会摧毁 React，”Angular 框架的创建者之一，现任 Cloudflare 工程高级总监 [Igor Minar](https://www.linkedin.com/in/igorminar/) 说道。其他人，特别是前端云公司 Vercel，[认为](https://vercel.com/blog/understanding-react-server-components) React Server Components “增强了 React 的基本原理”。那么谁是对的呢？

简而言之，[React Server Components](https://react.dev/reference/rsc/server-components) (RSCs) 是专门在服务器上运行的组件。正如 React 团队在 2022 年 3 月解释的那样，当对这种“新型组件”的稳定支持[在 React 18 中添加](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023)时，RSCs “提前运行，并从您的[客户端] JavaScript 包中排除”。Next.js（由 Vercel 开发，也支持并帮助资助 React 开发）是第一个宣布支持 RSCs 的主要框架，在 [2022 年 10 月发布的 Next.js 13](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/) 中。这个版本的 Next.js 将 RSCs 集成到其新的[App Router 架构](https://nextjs.org/blog/june-2023-update) 中。

## RSC 的优缺点

对于 Next.js 用户来说，RSCs 很有用。YouTuber [Theo Browne](https://www.linkedin.com/in/t3gg/) 最近在 [React Summit 2024 上做了一个演讲](https://gitnation.com/contents/rscs-in-production-1-year-later)，并对 RSC 大加赞赏，他所运营的开发工具公司已经使用 RSC 超过一年了。

“我强烈推荐 Server Components。”

– Theo Browne，YouTuber 和 Ping Labs 首席执行官

“如果你想学习一些新东西，并且不害怕它可能不是下一个大事件，我强烈推荐 Server Components，”Browne 总结道。“老实说，如果这些[RSC]不是我们未来编写软件的方式，我会非常惊讶。”（值得注意的是：直到[本月初](https://www.youtube.com/watch?v=uv179CTAK-w)，Vercel 都是 Browne 广受欢迎的 YouTube 节目的赞助商——他一直对这种关系坦诚相待。）

然而，其他人发现 RSC 的调整更具挑战性。“自 RSC 发布以来，混合客户端/服务器图的思维负担一直是我最大的保留意见，”Vue.js 创建者 [Evan You](https://www.linkedin.com/in/evanyou/) 在 [6 月](https://x.com/youyuxi/status/1805905884746592752) 在 X 上说道。

RSC 的采用还面临其他挑战。其中一个使采用变得困难的方面是，迁移到此模型的应用程序需要支持基础设施，并且——取决于 React 的版本——需要扩展配置和额外的中间件集成，这可能与客户端应用程序可能构建在之上的当前应用程序部署和托管模型不兼容。

RSC 技术“创造了一种延迟的 JS 伏击效应”。

– Alex Russell，微软 Edge 的合作伙伴产品经理

尽管在一些 Next.js 用户中很受欢迎，但 RSC 在其他 Web 开发社区中一直存在争议。在我与 Minar 交谈的同时，我也试图安排时间与微软的 [Alex Russell](https://www.linkedin.com/in/alexrussell/) 谈谈他的“[HTML-first](https://thenewstack.io/from-react-to-html-first-microsoft-edge-debuts-webui-2-0/)”理念。Russell 一直是 [React 的长期批评者](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)，所以我问他他对 RSC 的看法。他通过电子邮件回复了以下解释，说明他为什么不喜欢它们：

“RSC 的 *raison d’etre* [存在的理由] 是减少发送到浏览器的前端代码量，因为这些代码通常是导致 Core Web Vitals 结果不佳的原因。它通过在服务器上运行 React 应用程序中的组件子树来实现这一点，直到开发人员包含一个“use client”指令。此时，服务器会 sort of nopes out 并将该组件下方的树中的所有内容定义为“客户端”，这意味着服务器必须随后发送定义子树中每个组件的所有代码，以及任何依赖项。这会产生一种延迟的 JS 伏击效应。”

![即使使用 App Router，Next.js 在 Core Web Vitals 中的表现也比其竞争对手差；HTTP Archive Core Web Vitals 技术报告](https://cdn.thenewstack.io/media/2024/09/77706bd8-corewebvitals-technology-report-18sep24a.png)
![即使使用 App Router，Next.js 在核心 Web 指标方面也表现不佳，与竞争对手相比；HTTP Archive 核心 Web 指标技术报告](https://cdn.thenewstack.io/media/2024/09/77706bd8-corewebvitals-technology-report-18sep24a.png)
即使使用 App Router，Next.js 在核心 Web 指标方面也表现不佳，与竞争对手相比；[HTTP Archive 核心 Web 指标技术报告](https://lookerstudio.google.com/u/0/reporting/55bc8fad-44c2-4280-aa0b-5f3f0cd3d2be/page/M6ZPC?params=%7B%22df44%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580Next.js%25EE%2580%2580Nuxt.js%25EE%2580%2580Next.js%2520App%2520Router%25EE%2580%2580Astro%25EE%2580%2580Remix%25EE%2580%2580Qwik%22,%22df46%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580mobile%22%7D)

但同样，一些开发者认为 RSC 是一个有用的演进。在 [4 月份的一篇文章](https://thenewstack.io/react-server-components-in-a-nutshell/) 中，Paul Scanlon 在 The New Stack 上写道，RSC 使“数据从组件内部轻松访问”。他认为 RSC“有助于理解应用程序在做什么，因为逻辑、数据和生成的 UI 元素整齐地位于同一个文件中，与追溯 props 并尝试跟踪数据旅程相比，开发人员体验通常更好”。

Igor Minar 喜欢 RSC 的一个功能是更好的数据获取。“这种改进的组件封装，在 RSC 中包括数据获取，是 RSC 的一个积极属性（也许是唯一一个？）我与开发人员讨论的，”他说。“我们应该尝试保留此功能并使其成为更广泛的 Web 开发生态系统中的规范，但要避免 RSC 带来的所有缺点。”

## 起源
回顾 React 团队发明 RSC 的原因是值得的。它们最初是由 React 项目在 [2020 年 12 月](https://react.dev/blog/2020/12/21/data-fetching-with-react-server-components) 推出的，作为 React 的一种提议的数据获取解决方案。其想法是将相关的 React 组件从客户端移到服务器。

“React 之前可以在服务器端执行，尽管效率非常低，”Minar 指出。“RSC 的变化在于一些组件专门在服务器端执行。这是新的。使用 RSC，您必须在服务器端运行（一部分）React 应用程序，而在 RSC 之前，您可以将 React 作为可选优化在服务器端运行，但您可以选择不这样做（并且大多数 React 生态系统都选择了不这样做）。”

正如 React 工程师 Dan Abramov 在 [2020 年 12 月的一段视频](https://www.youtube.com/watch?v=TQQPAU21ZUw&t=46s) 中解释的那样，“这些仍然是普通的 React 组件，但我们将它们称为服务器组件，因为它们只在服务器上执行——它们永远不会被发送到客户端。”

React 服务器组件背后的关键思想是，如果一个组件需要数据获取或执行不涉及客户端交互的任务，那么通常最好在 *服务器* 上处理该组件，而不是作为常规的客户端组件。

到目前为止，这很合乎逻辑。毕竟，这有点像浏览器组件在 1990 年代的工作方式——还记得 CGI、PHP 和 ASP 吗？只是现在，并非所有事情都需要在服务器上完成。React 本身是为了更容易地在客户端上做更多事情而发明的。现在有了 RSC，React 使开发人员能够决定应用程序的哪些部分应该在服务器上运行，哪些部分应该在客户端上运行。

## 现状
那么问题出在哪里呢？好吧，根据 Igor Minar 的说法，开发人员一直在努力实现 RSC。

“React 服务器组件将在 React 社区中造成如此多的痛苦，以至于开发人员将开始寻找替代方案。”

– Igor Minar，Angular 联合创始人，Web 和 OSS 爱好者，现任 Cloudflare
“我个人相信 React 服务器组件会毁掉 React，因为从技术角度来看，它是一种有缺陷、不成熟且与当前 React 生态系统不兼容的技术，”Minar 告诉我。“对于当前的 React 生态系统来说，这是一个巨大的破坏性变化，一个甚至没有完全考虑清楚和正确实现的破坏性变化，它被强加给了 React 开发人员。所以，有趣的是，我认为我的预测是 React 服务器组件将在 React 社区中造成如此多的痛苦，以至于开发人员将开始寻找替代方案。”

微软的 Alex Russell 在他对 RSC 的分析中更关注网站性能。
“能够从 RSC 中获得性能提升的网站，与那些已经拥有 [高管理成熟度实践](https://infrequently.org/2022/05/performance-management-maturity/) 来控制非 RSC React 或 Angular 的网站相同，”他通过电子邮件解释道（引文中链接来自他）。“在这些组织之外，任何不经意的 ‘use client’ 指令，组件层次结构中的任何点，来自任何依赖项，都可能完全拖垮网站性能。”

Russell 对 React 团队最初引入 RSC 的原因持怀疑态度。“我个人认为，RSC（就像 fiber/并发模式）是 React 社区为了适应不断变化的 Core Web Vitals 环境而做出的最小程度的调整，”他说。“RSC 试图避开 (非常宽松的) INP [[交互到下一帧绘制](https://web.dev/articles/inp)] 门槛，或者至少让 React 社区相信，他们不需要离开 React 就能提供最低限度的性能。”

![“具有良好 INP 的来源”；HTTP Archive Core Web Vitals 技术报告](https://cdn.thenewstack.io/media/2024/09/161b97cd-corewebvitals-technology-report-18sep24b.png)
![“具有良好 INP 的来源”；HTTP Archive Core Web Vitals 技术报告](https://cdn.thenewstack.io/media/2024/09/161b97cd-corewebvitals-technology-report-18sep24b.png)
“具有良好 INP 的来源”；[HTTP Archive Core Web Vitals 技术报告](https://lookerstudio.google.com/u/0/reporting/55bc8fad-44c2-4280-aa0b-5f3f0cd3d2be/page/M6ZPC?params=%7B%22df44%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580Next.js%25EE%2580%2580Nuxt.js%25EE%2580%2580Next.js%2520App%2520Router%25EE%2580%2580Astro%25EE%2580%2580SvelteKit%25EE%2580%2580Remix%25EE%2580%2580Qwik%22,%22df46%22:%22include%25EE%2580%25800%25EE%2580%2580IN%25EE%2580%2580mobile%22%7D)

至于 Theo Browne，即使是他——RSC 的粉丝——也承认，仅仅依靠 RSC 并不足以成功地实施这项技术。具体来说，他的公司使用 Next.js [App Router](https://nextjs.org/docs/app)，他在 React Summit 演示中表示，这是“目前在生产环境中安全使用服务器组件的唯一真正方法”。

根据他关于 RSC 的 React Summit 演示附带的常见问题解答，Browne “在性能方面遇到了挑战，尤其是在没有部分预渲染的情况下”，并且“还遇到了开发服务器性能和包中服务器组件与客户端组件集成的問題”。

但尽管在实施 RSC 时遇到了这些问题，Browne 最终还是认可了它们。正如他在 [最近的一段视频](https://www.youtube.com/watch?v=0tvfC9r9lcw) 中提到的（他在 YouTube 频道上回应了我最近关于 [React vs. HTML-first](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) 辩论的文章），Browne 说，“服务器组件允许你无需更新不需要更新的内容，这在差异化方面也大有帮助。”他接着展示了一些通过使用 RSC 实现的酷炫功能。

## RSC 两极分化
“React 19 即将到来，”Vercel 在 [一篇博文中](https://vercel.com/blog/whats-new-in-react-19) 这样写道。RSC 将“作为 React 19 新功能的基础，”它继续说道，并列出了更快的初始加载、代码可移植性和 SEO 等它认为的优势。

然而，如上所述，目前开发人员对 RSC 的体验是两极分化的。RSC 固然带来了一些创新功能——例如封装数据获取——但代价是难以采用，并且（用 Russell 的话说）“延迟的 JS 攻击”。

最大的问题是：这种两极分化会损害 React 最宝贵的东西——它的生态系统和社区吗？考虑到 React 服务器组件即将对 React 生态系统产生的巨大影响，以及早期采用者和专家对它的看法截然不同，监控 React 社区如何采用 RSC 将会很有趣——以及 RSC 是否会促使一些 Web 开发人员寻找更好的解决方案。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，收看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)