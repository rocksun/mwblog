# OpenNext 帮助 Next.js 迈向真正可移植性

![OpenNext 帮助 Next.js 迈向真正可移植性的特色图片](https://cdn.thenewstack.io/media/2024/10/6b003ee3-james-wiseman-imgcpfimorw-unsplashb-1024x576.jpg)

鉴于 Next.js 是一个用于前端开发的开源 JavaScript 框架，看到一个名为 OpenNext 的相关项目可能会让人感到困惑（甚至有点尖锐）。这个名字可能造成了一些混淆，但该项目的原因是解决 Next.js 作为垂直整合框架所带来的某些权衡——当你考虑到它的历史时，这一点就更有意义了。

现在，Vercel 的首席产品官，负责监管 Next.js 的 [Tom Occhino](https://www.linkedin.com/in/tomocchino/) 曾在 Facebook 担任工程经理，“帮助创建了 React”。“Next.js 诞生于同一时期，旨在为 React 添加一些功能，使其在 Facebook 之外也能很好地工作，”他告诉 The New Stack。

“React 对你的服务器没有任何意见；Next.js 则有。”

– Vercel 首席产品官 Tom Occhino

框架添加的部分功能包括服务器端渲染和数据获取，这显然会产生影响。

“React 对你的服务器没有任何意见，”Occhino 说。“Next.js 则有，所以你可以进行数据获取和服务器端渲染，以及其他所有这些事情。”

Next.js 不仅依赖于服务器基础设施，而且还期望为你定义该基础设施。

“React 对你如何编排服务器和进行服务器端渲染没有意见。嘿，这里有一些原语：想办法按照你想要的方式组装它们。Next.js 说，‘好吧，如果你以这种方式编写代码，以这种方式获取数据，并且以这种方式进行写入，我们可以自动配置任何必要的计算资源，不仅可以部署，还可以扩展你的应用程序。’”

如果该框架定义的基础设施恰好是 Vercel（Next.js 的创建者），开发人员就会得到 Occhino 所谓的“松耦合但高度内聚”。

这为开发人员带来了简便性，即使他们负责编写服务器端 JavaScript 代码以及前端代码，他们也可能更关心应用程序本身的细节，而不是基础设施部署、性能和扩展。托管在 Vercel 上的 Next.js 会自动配置带有 URL 的预览环境，以便与同事轻松协作，甚至处理自动故障转移。这种内聚性还允许 Vercel 打造利用框架和基础设施之间编排的特性。

“当你将 Next.js 部署到 Vercel 时，这些东西显然是经过精心设计，可以很好地协同工作，即使它们是松耦合的。”

– Occhino

“一个即将推出的 [Next.js] 功能是部分预渲染，”Occhino 说。“我们可以预渲染页面的静态部分，然后动态地将页面的动态部分流入。”

应用程序可以由多个云服务组成，例如 Shopify 上的电子商务后端、Salesforce Commerce Cloud 或 Adobe Experience Manager，生成的商品详情页和搜索结果页位于 Vercel 的前端云中。

“你还可以连接到你的 DevOps 团队自行部署的随机 Kubernetes 集群，我们可以创建 Vercel 基础设施与你的后端所在位置之间的安全链接，”Occhino 补充道。

Occhino 将其比作 Android 在 Google Pixel 上运行，或者使用 git 和使用 GitHub 之间的区别：“当你将 Next.js 部署到 Vercel 时，这些东西显然是经过精心设计，可以很好地协同工作，即使它们是松耦合的。”

开发人员不必将他们的 Next.js 托管在 Vercel 上，但这样做显然有优势。

“当然，这两者都可以单独工作，但协同工作时，它们可以很好地协同工作，”Occhino 说。

## 前端、后端和中间层

但并非所有使用 Next.js 的人都想使用 Vercel 的平台，尤其是当他们在不同的云上拥有数据和其他资源时——无论是 AWS、Azure 还是 Cloudflare。出于合规性和采购原因，大型组织可能会有规定哪些云服务可以使用的政策。小型初创公司希望专注于设计他们的产品，而不是考虑他们是否会被出口费用击中。

“你可以构建最花哨、最酷的托管平台，但你无法通过采购团队，”SST 团队成员 [Dax Raad](https://www.linkedin.com/in/thdxr/) 指出，该团队启动了 OpenNext 项目来帮助支持他们使用 AWS 的客户。“一旦你进入那个世界，使用更多 AWS 比使用新事物要容易一千倍。”

“前端和后端的耦合对于 Web 开发人员来说是一个尚未解决的问题，而且是一个有争议的问题。”

– RedMonk 高级分析师 Kate Holterhoff

### 翻译者回应

### EDITOR'S RESPONSE
“前端和后端的耦合对于 Web 开发人员来说是一个尚未解决的问题，而且是一个有争议的问题，”RedMonk 的高级分析师 [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/) 补充道。“开发人员正在积极寻找方法来通过微前端、岛屿架构和 React 服务器组件等方法来导航服务器/客户端两步，但尽管我们已经从 PHP 时代走出来了，但以一种既高效又交互的方式集成应用程序仍然存在很多问题。”

由于它不仅仅是像 React 这样的客户端方法，Next.js 具有一个服务器运行时，它会自动配置缓存控制和图像优化等功能。事实上，Next.js 有两个运行时：一个基于 Node.js 的运行时用于渲染应用程序，以及一个边缘运行时，它具有有限的 Node.js 功能（旨在运行在资源更少的较小服务器上，但由于它们分布在网络边缘靠近主要人口地区，因此延迟更低。边缘运行时处理路由规则，例如重定向，Vercel 称之为“中间件”。这两个运行时之间的差异 [让一些开发人员感到沮丧](https://github.com/vercel/next.js/discussions/46722#discussioncomment-6715038)，他们希望在其他平台上运行 Next.js 应用程序，例如 AWS Lambda 或 Cloudflare Workers。

“实际上，当应用程序打包时，它会对应用程序施加一些约束，”Cloudflare 产品总监 [Brendan Irvine-Broque](https://www.linkedin.com/in/brendanirvinebroque/overlay/about-this-profile/) 解释道。这些约束使自托管 Next.js 比你想象的更难。

“是的，如果你擅长回到运行所有内容的 Docker 容器的旧世界，你可以托管它 [Next.js]。”

– Netlify 首席执行官 Mathias Biilmann
Next.js 文档建议在 Node.js 服务器上自托管（这可能不适合你的用例，并且不会给你无服务器环境的优势）或在 Docker 容器中自托管。后者的说明 [相当简短](https://nextjs.org/docs/pages/building-your-application/deploying#docker-image)，但 Vercel 的 [Lee Robinson](https://www.linkedin.com/in/leeerob/) 最近发布了 [一个相当全面的 YouTube 视频](https://www.youtube.com/watch?v=sIVL4JMqRfc)，其中包含更多详细信息。

“是的，如果你擅长回到运行所有内容的 Docker 容器的旧世界，你可以托管它，”Netlify 首席执行官 [Mathias Biilmann](https://www.linkedin.com/in/mathias-biilmann-christensen-a5a3805/) 抱怨道。

此外，对于大多数应用程序来说，这将需要 [多个容器](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env) 来实现冗余或扩展，从而增加了额外的复杂性，Raad 补充道。“一旦你有了两个容器，你就会遇到很多事先并不明显的缓存问题，因为你必须实现一个与中央缓存同步的自定义缓存处理程序。而 Docker 容器本身还不够：你需要在它前面使用 CDN，而且你会再次遇到同样的缓存控制问题。”

部分预渲染功能（Raad 指出，这比更简单的 Astro 等效功能要复杂得多，而且 Vercel 可以从单个请求中提供服务）可能在 Docker 容器中工作，“但它在 Docker 容器中的工作方式使该功能毫无用处”。他说，中间件在某些环境中不能很好地工作，开发人员需要自己想办法让图像优化等功能高效地工作。此外，大多数 SST 用户不想使用 Docker；他们想使用像 AWS Lambda 这样的无服务器平台，并使用 CDN。

自托管 Next.js 的部分问题在于，并非立即清楚哪些功能将在哪些平台上工作，哪些功能不会。

“有些功能无法正常工作，还有一些功能并非无法正常工作，而是会导致错误的行为，”Raad 说。

例如，直到最近，Next.js 输出的缓存控制头都是非标准的；Vercel 基础设施中的缓存控制器可以理解这些头，但 AWS 等效项则不能。

“[Next.js] 是一个庞大而复杂的框架，因此当某些东西没有完全正常工作时，并不明显。”

– Dax Raad，SST（启动了 OpenNext 项目）
这种不可预测性是人们对 OpenNext 为什么需要存在感到困惑的部分原因。并非在 Vercel 之外托管 Next.js 不可能；而是结果差异很大，开发人员需要具备 Next.js 专业知识才能知道哪些是可移植的——他们可能直到完成应用程序开发并准备部署它，甚至在它投入生产后才会意识到这一点。
“真正发生的是，你部署了它，看起来它在工作，但几个月后，你会意识到，哦，这个小功能实际上有点错误，或者另一个功能没有按预期工作，”Raad 说。“这是一个庞大而复杂的框架，所以当事情没有完全正常工作时，并不明显。”

在许多方面，Raad 说 OpenNext 与其说是关于代码，不如说是关于自动配置基础设施的文档项目。

“我们不是在分享代码，而是在分享信息，”他补充道。“对于任何半严肃的事情，你都需要发现很多信息。”

其他基于 React 的前端框架——比如 Remix、[TanStack](https://tanstack.com/) 和 Astro——并不期望前端代码对后端有如此强烈的意见。因此，他们完整地记录了在不同平台上进行自托管的选项，包括哪些有效、哪些无效，以及如何编写适配器以使功能在那里运行。Next.js 的开源代码库中仍然存在 [引用](https://github.com/vercel/next.js/discussions/29801) Vercel 用于自己执行此操作的专有代码，而不是有关如何自己执行此操作的全面信息。

这就是为什么 Biilmann（他的公司 Netlify 是 Vercel 的直接竞争对手）将 Next.js 视为“开源和闭源之间的奇怪中间地带”。处理这个问题需要大量反向工程来了解它的工作原理。“我们付出了非常大的努力，以一种与任何其他开源框架截然不同的方式为 Next.js 构建了适配层，”Biilmann 说。他补充说，Netlify 的适配器测试套件偶尔会暴露 Next.js 本身的错误。

“这不是说 Next.js 不是开源的，”Raad 同意。“问题是如何让 Next.js 文档中列出的每个 Next.js 功能在各种环境中实际运行——这些信息只是没有公开。”

这比其他前端框架更重要，因为许多强大的 Next.js 功能依赖于后端基础设施。他不认为这是 Vercel 的恶意或反竞争行为；他认为这只是垂直整合框架的本质。

“Next.js 不像其他框架那样灵活——这就是 OpenNext 存在的原因。”

– Raad
“当他们看到问题时，他们可以纯粹在框架中解决它，或者通过将框架与特定基础设施配对来解决它；当你将它与特定基础设施配对时，你总是会得到技术上更好的解决方案。如果你在未来几年内这样做，他们往往会设计出对基础设施提出特定要求的功能，这是一个自然产生的现象。其他框架不会这样做，因为它们没有平台。”

事实上，Raad 认为这种紧密联系是 Next.js 的优势。“选择 Next.js 的好处是它是唯一一个垂直整合的框架：它们一直整合到基础设施，使它们能够做其他框架无法做到的事情。所以如果你选择 Next.js，你应该选择它是因为你喜欢它，并且你正在接受它。”

权衡是 Next.js 不像其他框架那样灵活——这就是 OpenNext 存在的原因。

“这就是为什么必须有这个其他中立的东西来解决这个问题，”Raad 说。

## 为可移植性记录文档
OpenNext 不是第一个支持开发人员在 Vercel 之外使用 Next.js 的项目。但是，由于单个开发人员创建的工具非常少，只涵盖了他们需要使用的功能，因此 AWS Lambda（例如）经常发现很难跟上 Next.js 的新版本。因此，所有这些较小的项目都被 [取代](https://github.com/sladg/nextjs-lambda) 了 OpenNext 更完整的方法和活跃的社区支持。

事实上，这是该项目灵感的来源之一；SST 之前依赖于现有的开源项目之一来支持 Next.js 12，但 Next.js 13 中的重大变化（Raad 将其描述为“实际上是一个全新的框架”）是现有维护者无法解决的。“当这是一次性努力时，他们往往依赖于一个人。”

OpenNext 的一个动机是 SST 用户想要帮助将 Next.js 运行在 AWS Lambda 上。

– Raad
另一个动机是 SST 用户想要帮助将 Next.js 运行在 AWS Lambda 上的数量之多。“多年来，人们不断来找我们说，‘嘿，你们正在做的事情很棒，但我最大的痛点是我有一个 Next.js 应用程序，我不清楚如何让一些功能在 AWS 上运行’，多年来我们一直说‘是的，这很糟糕！’”

具有讽刺意味的是，SST 团队中没有人是 Next.js 开发人员，但据 Raad 说，“我们必须支持它，因为它非常受欢迎。我们对这个项目没有热情：如果它不需要，它就不会存在。”
像 Google Firebase、Cloudflare Workers、Netlify 甚至 AWS 自身的 Amplify 这样的平台都在为 Next.js 创建自己的（有时是闭源的）集成。这造成了很多重复工作，尤其是 Next.js 中的广泛功能意味着任何适配器都需要足够多的用户来使用所有选项并查看它们是否正常工作。

“感觉很愚蠢，每个人都在单独做这件事，而且没有集中式的努力，”Raad 说。“我们认为我们处于一个不错的职位来做到这一点，因为我们可以用我们的社区来推动这项工作，[社区] 有很多人想要使用 Next.js 和 AWS。”

OpenNext 旨在支持 Next.js 14 的 100% 功能。

OpenNext 于 2023 年 4 月推出，支持大约 70% 的 Next.js 功能；它现在旨在支持所有 Next.js 14 功能，并且完全由社区维护，测试套件涵盖了新 Next.js 版本中的功能。它在耐克等组织中投入生产使用，Raad 估计有数千个生产网站依赖它。

现在 Cloudflare 和 Netlify 正在为他们的平台开发 OpenNext 适配器。Biilmann 将其视为“一个跨竞争合作的地方，这在开源世界中感觉很自然，关于如何构建正确的基础设施，使其能够轻松地在尽可能多的前端平台上运行 Next.js”。

事实上，就在 Next.js 15 发布几天后，Netlify 宣布将[迁移](https://www.netlify.com/blog/netlify-joins-opennext/)其[现有的、全面的开源 Next.js 适配器](https://github.com/netlify/next-runtime/)到 OpenNext 仓库。

开发人员已经可以使用[cloudflare/next-on-pages](https://www.npmjs.com/package/@cloudflare/next-on-pages)将 Next.js 应用程序部署到 Cloudflare Pages，但这只支持 Edge 运行时。[Cloudflare 正在构建的 OpenNext 适配器](https://opennext.js.org/cloudflare) 将 Next.js 输出转换为在 Pages 或 Workers 中运行（或使用[Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/) 在本地运行）。

“实际上，这只是为了满足开发人员的需求，”Irvine-Broque 说。“Next.js 是最流行的框架之一。我们希望确保无论您使用什么框架，您都可以使用 Cloudflare 的其他功能。”

这包括对选项的支持，例如以编程方式与平台原语交互，例如直接从 Worker 进行速率限制。

由于这些适配器现在作为开源项目的一部分而不是平台中的内部代码构建，因此它为更广泛的贡献者群体打开了大门。一家使用 Next.js 的大型 Cloudflare 客户已经计划为 OpenNext 适配器做出贡献，Irvine-Broque 将其归类为“相当 1.0”。它已经支持即将推出的功能，例如增量静态生成（它允许您将静态和按需服务器渲染混合在一起，以用于需要偶尔更新的页面），并且正在进行中间件和部分预渲染的工作。

## 从混乱到协作
OpenNext 背后的不断增长的势头表明了该项目的必要性；虽然各方显然都感到沮丧，但最终的结果是对话，这些对话将使 Next.js 用户和平台所有者更容易使用。Amplify 是这个领域中唯一尚未加入 OpenNext 的重要项目（目前尚不清楚 AWS 为此投入了多少资源），Vercel 也参与其中。

Vercel 已经与 OpenNext 维护者进行了讨论。

“他们一直在与我们的维护者进行讨论，”Raad 说，“这非常有帮助，因为我们的维护者过去不得不反向工程所有内容。”

现在，如果 Next.js 中的某些内容在 AWS Lambda 中不起作用，那么根据 Raad 的说法，“他们可以直接询问团队并获得答案；拥有这条直线非常重要。”

Vercel 的 Next.js 团队还修复了代码中的一些问题，这些问题过去需要 Raad 所谓的 OpenNext 中的黑客攻击。“我认为他们会继续这样做，”他补充道。

他希望这种合作能够随着时间的推移缩小 OpenNext 的范围。“Next.js 本身正在处理其中的一些事情，他们正在谈论将我们文档中的信息移到他们的文档中，使其看起来更像其他框架。”这很可能涵盖在 AWS、Netlify 和 Cloudflare 上部署 Next.js，消除了 Next.js 与 Vercel 关系过于密切的担忧。

但即使 Next.js 中存在错误修复和改进的文档，OpenNext 也可能仍然是必要的，他预计它将过渡到成为基金会的一部分。

“即使他们与我们交谈并提前告知我们更改，也总会有一个追赶动态，OpenNext 会追赶 Next.js 版本，”Raad 警告说。“它永远不会完全弥合差距。”
虽然 OpenNext 的名字可能听起来具有挑衅性，但 Raad 指出，SST 经常建议潜在用户如果可以的话选择 Vercel 以获得简单性，并警告现有的 Vercel 用户迁移到 OpenNext 需要付出多少努力。

“我们一直推荐他们：只是很多只使用 AWS 的公司有规定，你不能使用其他任何东西，因为这会增加合规性和采购负担，所以他们别无选择，我们只能为他们想办法。”

Raad 还指出，Vercel 建议的 Docker 方法可能是 Next.js 使用的重要组成部分，尤其是对于更简单的用途。

Biilmann 同意。“我们为我们的企业客户运行一些最大的 Next.js 属性，”他说。“有很多 Next.js 网站只是在 Docker 容器中运行，在一个 Kubernetes 集群中。”

“如果我们没有在周围建立一些真正的开放治理，这可能会导致 React 的衰落。”

– Biilmann
那些正在愉快地使用该解决方案的开发人员可能不明白为什么 OpenNext 是必要的，但它并不适合所有人，Biilmann 说他看到社区中有很多沮丧，这开始蔓延到 React（Vercel 在那里也做出了重大贡献，因为该项目引入了自己的服务器端功能，例如 React 19 中的服务器函数）。

“如果我们没有在周围建立一些真正的开放治理，这可能会导致 React 的衰落，”Biilmann 警告说。“如果这是方向，感觉能够以开放的方式在任何地方运行它对于整个生态系统来说非常重要，并且拥有真正明确的适配器契约等等变得非常重要。”

提高透明度将有助于 Next.js 与 [Vite.js](https://v2.vitejs.dev/) 生态系统竞争，该生态系统提供可组合的路由器作为基本元素，并承诺支持针对多个环境的代码定位，这正被 Angular 等框架采用。

“一个环境可以是 Netlify 函数，也可以是 Cloudflare worker，也可以是浏览器，也可以是浏览器中的服务工作者，”Biilmann 解释说。“这与框架衍生的基础设施愿景不同。”

他希望 OpenNext 能够为 Next.js 提供更多新功能的机会，并确保它不会与一家公司的成功率绑定。

“如果我们在未来一年真正取得成功，并开始为前端创建一个更健康的开源生态系统，我们将开始看到基础设施和后端开源生态系统中很多真实的东西，”Biilmann 说，这意味着在其他方面竞争的供应商仍然可以合作。“没有理由我们不能将我们投入到维护适配器中的大量资源投入到上游贡献中。”

“我确实希望 Next.js 本身能够从它被部署到很多其他地方的想法中受益。”

– Occhino（来自 Vercel）
Occhino 对 OpenNext 的直接和长期影响同样持积极态度。“至少，生态系统将从中受益。更多人将能够使用 Next.js [因为] 它在更多情况下有效。但我确实希望 Next.js 本身能够从它被部署到很多其他地方的想法中受益。”

“我认为，这些适配器中的一些将有机会影响框架本身，”Occhino 补充道。“但我也对这些适配器的协作以及我们在将它们部署到不同类型基础设施时学到的东西感兴趣。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等等。
](https://youtube.com/thenewstack?sub_confirmation=1)