多年来，[React不仅作为UI库占据主导地位](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)，而且还是全栈JavaScript架构的基础。但Remix 3正在颠覆这一局面。它挑战了React应该成为我们开发宇宙中心的观点，而是将Web基础知识重新置于聚光灯下。

Remix 3建立在渐进增强和服务器优先原则之上，[它不仅仅优化了性能](https://remix.run/blog/wake-up-remix)——它还重新定义了我们的构建方式。在一个痴迷于客户端一切的世界里，这个框架提出了一个问题：如果我们不再把React当作框架，而是开始把它当作工具来使用呢？这种转变的影响可能会彻底改变前端架构。

## 一个敢于打破常规的框架

Remix 3不仅仅是一个升级——它是一种声明。多年来，我们一直围绕React构建Web应用程序，构建漂浮在大量样板代码海洋中的交互岛屿。然后出现了试图驯服React过度行为的框架：Next.js简化了路由，[Gatsby优化了静态输出](https://www.gatsbyjs.com/docs/how-to/images-and-media/static-folder/)，Vite加快了开发速度。但Remix 3呢？它将整个以React为中心的心态抛到了脑后。

> 与其将React视为万物围绕的太阳，不如将其视为众多工具之一。

与其将React视为万物围绕的太阳，不如将其视为众多工具之一。这种转变既微妙又巨大。你仍然可以编写React组件，当然，但该框架并不希望你将每一段状态、获取逻辑和布局配置都塞进React运行时。事实上，[Remix故意避免了许多传统的React模式](https://www.dhiwise.com/post/an-in-depth-analysis-remix-vs-react-which-one-is-supreme)，而是倾向于渐进增强、标准Web API和服务器原生思维。

问题不在于Remix 3是否“优于React”。而是：Remix是否标志着[后React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)架构时代的开始？

## 为什么以React为中心的架构成为常态

React赢得前端战争不仅仅是因为JSX或组件。它赢了[因为它为开发人员提供了控制权](https://localazy.com/for/software-developers)和解决同一问题的多种方法。细粒度的状态、作用域组件和位于同一位置的逻辑的舒适性都具有强大的吸引力。但随着React应用程序的成熟，蔓延也随之而来：客户端繁重的代码库、状态库之上的状态库以及整个堆栈中不一致的数据获取策略。

> 开发人员开始构建React优先的应用程序，将浏览器视为二等公民。

像Next.js这样的框架不断发展以进行补偿。它们用约定弥补了React的缺陷：基于文件的路由、SSR和ISR、API路由。但这些仍然是解决React与全栈Web根本不匹配的变通方法。开发人员开始构建React优先的应用程序，将浏览器[视为二等公民](https://stackoverflow.com/questions/64518226/my-create-react-app-is-failing-to-compile-due-to-eslint-error)。客户端包膨胀。加载时间受到影响。交互性以复杂性为代价。

本质上，“React架构”变成了一场在React协调周期下抽象浏览器和服务器的竞赛。Remix 3提供了一条不同的路线——React只是视图层，而不是应用程序宇宙的中心。

## Remix 3的理念：Web标准第一，React第二

Remix 3团队并没有打算取代React。他们[着手修复Web开发人员的体验](https://reactrouter.com/upgrading/remix)。这意味着重新思考数据加载、错误处理、变更、导航和缓存——并以最Web原生方式解决它们。因此，Remix没有发明新的范例，而是大力利用Web已经擅长的东西。

> Remix以设计的方式使用Web平台；而React恰好是你构建UI的方式。

需要加载数据？使用在服务器上运行的加载器。需要改变状态？使用与表单提交相关的操作。导航？它通过增强的链接发生，如果JavaScript失败，这些链接会优雅地降级。Remix以设计的方式使用Web平台；而React恰好是你构建UI的方式。

这种对渐进增强的强调对于性能至关重要，而不仅仅是为了炫耀。使用Remix构建的应用程序[通常感觉更流畅、更具弹性且更易于维护](https://moduscreate.com/blog/remix-what-you-should-know-from-our-experience/)，因为它们较少依赖JavaScript包，而更多地依赖原生浏览器行为。更不用说，SEO和营销表明，使用Remix构建的网站排名更高，并且[与反向链接等信号的交互更好](https://bluetree.digital/backlink-importance-and-benefits/)，仅仅是因为所讨论的架构更“轻量级”。

结论是？Remix不会最小化React；它会重构它，并使其对算法和人类都更具可移植性。

## Remix 3在底层改变了什么

使用Remix 3，架构变得更具声明性和可组合性，但JavaScript绑定更少。路由不仅仅是URL处理程序，而是代码和数据责任的单元。加载器和操作是路由契约的一部分。错误边界的作用域是每个路由。心智模型不是“React组件获取数据”。而是“具有嵌入式逻辑和UI的路由”。

此模型实现了深度灵活性。想要[完全的服务器端渲染](https://thenewstack.io/spas-and-react-you-dont-always-need-server-side-rendering/)？它已内置。想要仅水合你需要的交互性？简单。想要部署到Cloudflare Workers或在边缘运行？Remix 3开箱即用地支持它。这为开发人员提供了逃生舱口，而不会损害框架的核心理念。

> 这是回归瘦客户端——但具有现代DX。

这也意味着更少的依赖项。Remix不会使用SWR或React Query，而是鼓励你让服务器完成繁重的工作。并且当你将逻辑移动到加载器和操作时，你将默认获得SSR、缓存和安全性。这是回归瘦客户端——但具有现代DX。

## 这如何影响组件思维和可重用性

在传统的React架构中，[组件边界通常兼作逻辑边界](https://maybe.works/blogs/react-architecture)。组件可能会获取自己的数据、跟踪自己的加载状态、处理错误并呈现UI。这种自主性非常强大，但在Remix中，不鼓励这样做。Remix鼓励开发人员以路由的方式思考，并将逻辑隔离到服务器端函数中。

这种转变打破了我们已经习惯的一些模式。不再是[将组件包装在useQuery()中并观察它重新渲染](https://www.developerway.com/posts/react-re-renders-guide)。相反，数据在组件挂载时已经存在。这消除了瀑布流和微调器，但需要更慎重的数据模型。

可重用组件仍然有它们的地位，但它们看起来有所不同。它们不再是独立的逻辑容器，而是变成了纯粹的表示。Remix剥夺了组件的数据获取能力；并通过这样做，简化了它们的角色。结果是？更清晰的关注点分离和更快的渲染路径。

## 超越Remix：后React未来的惊鸿一瞥

如果Remix 3成功地推广了这种架构，它可能会激励一代框架不再将React作为默认选择。我们已经看到了早期的迹象。Astro将JavaScript视为可选，[Qwik将水合延迟到绝对必要时](https://thenewstack.io/javascript-on-demand-how-qwik-differs-from-react-hydration/)，而SolidJS完全放弃了虚拟DOM。React不再是最终游戏——它只是一种可能的选择。

> 将这些新兴框架团结在一起的不是反React的立场，而是亲Web的立场。

将这些新兴框架团结在一起的不是反React的立场，而是亲Web的立场。它们愿意重新评估React的假设：一切都需要客户端渲染，JavaScript为王，以及组件应该拥有一切。

从这个角度来看，Remix 3可能是React的统治地位和更加多样化的生态系统之间的桥梁。在这种生态系统中，框架尊重Web平台，拥抱部署多样性，并减少对庞大的客户端包的需求。

## 你应该为了Remix 3放弃React吗？

不，Remix 3也不希望你这样做。Remix建立在React之上。真正的问题是[你的架构是否仍然需要将React视为其基础](https://lobste.rs/s/oowhu2/you_don_t_need_react_for_building_websites)。如果你正在构建一个内容丰富的应用程序、一个混合渲染的应用程序或需要快速加载时间和服务器端逻辑的应用程序，那么Remix 3可能正是你需要的。

但如果你的应用程序已经非常以客户端为中心，一个仪表板、一个游戏或一个具有复杂状态的SPA，那么React繁重的方法可能仍然最适合你。Remix不是万能药；它是一种优先级的转变。

对于习惯了React元框架的团队来说，采用Remix 3意味着要改掉一些习惯。但回报是巨大的：[更快的TTI、更小的包、更简单的逻辑路径](https://otiv.dev/blog/why-remix)以及重新发现Web平台已经多么强大。

## 一个时代的终结——或者只是一个调整？

Remix 3并没有宣告React的终结。但它确实挑战了我们的集体假设，即React应该始终位于我们堆栈的核心。它的架构提醒我们，Web是一个强大而有弹性的平台——而我们已经绕过它太久了。

> Remix 3点燃了前端对话的火焰。

这不仅仅是一种趋势；这是一种重新校准。Remix不会拒绝React，而是将它从不应该做的工作中解放出来。这是否会成为新常态或一种小众理念取决于开发人员下一步的行动。

但有一点是明确的：Remix 3点燃了前端对话的火焰。它不仅关系到我们使用什么工具。它还关系到我们如何看待Web本身。