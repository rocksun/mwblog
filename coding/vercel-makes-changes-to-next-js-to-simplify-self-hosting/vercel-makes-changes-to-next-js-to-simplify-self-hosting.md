
<!--
title: Vercel修改Next.js以简化自托管
cover: https://cdn.thenewstack.io/media/2024/11/c805612f-delba-de-oliveira-at-next.js-conference.jpg
-->

Next.js 15 提供了对自主托管的新核心支持和文档；团队表示，新的缓存 API 也即将推出。

> 译自 [Vercel Makes Changes to Next.js To Simplify Self-Hosting](https://thenewstack.io/vercel-makes-changes-to-next-js-to-simplify-self-hosting/)，作者 Loraine Lawson。

Vercel产品副总裁Lee Robinson在十月旧金山举行的Next.js大会上表示，Next.js团队对Next.js核心进行了改进，并发布了新的文档，这将使前端开发者更容易自主托管Next.js。

“我们之前就有关于如何自主托管的文档和示例，但说实话，它们在一些特性上缺乏深度，例如缓存和图像优化，以及如何在部署到多容器设置时使用Next.js，”Robinson说。“有很多东西你需要配置。”

他补充说，Next.js通过Next.js 15简化了默认缓存处理器的配置，以便开发者可以利用内存缓存并定义一个使用任何所需适配器的自定义缓存处理器。

Robinson还宣布了一个新的[Next.js GitHub社区](https://github.com/nextjs)，它将成为模板、部署示例、社区适配器和其他资源的聚集地。

另见：[OpenNext 正在努力使 Next.js 真正可移植](link)

他补充说，团队改进了关于自主托管的文档。他们还制作了一个新的视频，其中介绍了Robinson [向开发者展示如何进行自主托管](https://www.youtube.com/watch?v=sIVL4JMqRfc)，包括将其部署到虚拟专用服务器（在本例中，是带有[Docker](https://thenewstack.io/docker-overhauls-simplifies-subscription-plans/)的4美元VPS）和配置所有功能。他说，视频还讨论了开发者可以进行的一些权衡和配置。

Robinson和其他人作为大会主题演讲的一部分，概述了为支持自主托管和其他改进而对Next.js进行的更改。

## `Use Cache`, `CacheTag` 和 `CacheLife`

`Use cache` 是一个新的缓存API。Vercel的DX工程师在主题演讲中将其介绍为一种使Web应用程序更快的方法。“`use cache`使用进程内内存缓存，”她说。“这意味着它从内存中启动，但随后你可以根据你自己的架构进行配置，以便将来，如果你愿意，可以将缓存托管在任何地方。”

在这种模式下，“缓存现在完全是可选且明确的，”她补充道。

她补充说，开发者可以在数据获取函数中使用`use cache`，只要这里的输入值相同，它就会被重用。这使得“在你的应用程序中使用缓存实际上非常便宜，”她说。

使用过app router的人应该熟悉`unstable cache` API，但`use cache` API有所不同。

“你可以将`use cache`视为`unstable cache`的继任者，”她说。“虽然`unstable cache`非常擅长缓存[JSON数据](https://thenewstack.io/working-with-json-data-in-python/)，但`use cache`可以缓存React渲染的任何内容，也就是任何可序列化的内容。”

![Vercel产品副总裁Lee Robinson与其他四位Next.js团队成员一起主持Next.js大会的小组讨论。](https://cdn.thenewstack.io/media/2024/11/b82d1adf-leerobinson-next.js-leads-panel.jpg)

从左到右：Vercel的Lee Robinson、Delba de Oliveira、[Sebastian Markbåge](https://www.linkedin.com/in/sebmarkbage/)、[Josh Story](https://www.linkedin.com/in/gnoff/)和[Jimmy Lai](https://www.linkedin.com/in/laijimmy0/?locale=en_US)讨论Next.js的改进。照片由Loraine Lawson拍摄。

她说，这允许开发者将其与fetch、数据库客户端或端点一起使用——甚至在组件本身内部使用。

还有两个用于重新验证的新API，重新验证是一种用于确保网页上显示的数据是最新的和准确的技术，即使底层数据源可能已更改。`CacheTag`可用于按需重新验证，而`cacheLife`可用于基于时间的重新验证。

她说，Next.js还将具有缓存配置文件，这些配置文件以秒、分钟、小时和天的普通英语描述缓存。缓存配置文件集成在框架缓存层中，“因此，希望你不再需要过多考虑不同的缓存层和网络边界。”缓存配置文件也可以自定义。

“因此，我们使用此API的目标是减少重新验证带来的决策疲劳，”de Oliveira说。

观察当今Next.js的功能，一旦这些API可用，开发者将不再需要某些东西。她特别提到了`unstable cache`，还包括路由配置选项，例如动态、fetch、缓存和重新验证，fetch扩展，如next revalidate和next tags，以及全局过期时间配置选项。
她说：“总的来说，这些API希望能确保你不用记住很多信息。”“总结一下我们讨论的内容，我们使用异步服务器组件为动态路径动态获取和渲染数据。我们使用[Suspense](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)来利用流式传输。如果我们想预渲染某些内容，我们使用缓存，然后使用`cacheTag`中的`cacheLive`来重新验证和配置该缓存。就是这样。”


## Next.js核心改进

Robinson说，[Next.js的其他改进使其更容易自行托管](https://nextjs.org/blog/next-15-rc2#improvements-for-self-hosting)。

他说：“以前，Next.js使用基于WebAssembly的图像优化库，虽然这安装速度更快，但不幸的是，当你在服务器上自行托管时，它会消耗更多内存。”“我们不太喜欢这种权衡。”

相反，Next.js切换到[Sharp](https://sharp.pixelplumbing.com/)，这是一个用于处理图像的高性能[Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/)库。

他说：“Sharp的好处是它安装速度快且内存效率很高。”“因此，使用Next.js 15，我们会自动为你安装Sharp。对于我们的自托管用户，你可以同时获得两全其美。”

另一个改进是更新默认的缓存控制头，以便更容易覆盖默认值，他指出这以前很难做到。

Robinson解释说，团队还简化了在Next.js 15中配置默认缓存处理程序的方法，以便开发人员使用内存中缓存并定义自定义缓存处理程序，这样你就可以使用你自己的[Redis](https://thenewstack.io/redis-users-want-a-change/)（一个流行的开源内存数据存储）或使用任何你想要的适配器，这应该会带来更快的响应时间和更低的服务器负载。

他说，增强的缓存功能与传统的Pages Router和新的App Router都兼容。它支持所有Next.js缓存功能，例如[ISR（增量静态再生）](https://nextjs.org/docs/canary/pages/building-your-application/data-fetching/incremental-static-regeneration)和`use cache`，他补充道。虽然它默认为内存中缓存，但他表示，程序员如果愿意，可以将其更改为持久化到存储中。

最后，Next.js还将支持[Node.js运行时](https://thenewstack.io/node-js-22-release-improves-developer-experience/)用于中间件。

他补充道：“这里最后一点是，在你的配置中，你还可以有一些新的选项来完全自定义你自己的设置、你自己的[CDN结构](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/)的缓存，你基本上可以根据自己的需要进行配置。”“我们使用Next.js的目标是真正提升整个生态系统，并将我们的研究成果与大家分享。”

值得注意的是，Vercel的首席执行官[Guillermo Rauch一直对CDN持批评态度](https://x.com/rauchg/status/1836759912711586210)。

Robinson承认，Next.js与在[Vercel](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/)的基础设施上试用功能同时进行构建，这使得“框架和基础设施之间具有高度的凝聚力”。然而，他补充说，他们在部署到现实世界时，目标是在两者之间实现松散耦合。

他说：“我们对Next.js的期望是成为一个强大而易于使用的框架，用于网络上的下一个百万或十亿[应用程序](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/)。”“它应该易于上手，足够灵活以适应你的需求，并且足够强大以支持你应用或业务需求的任何级别的雄心。”
