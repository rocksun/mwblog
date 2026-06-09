云网络安全和内容分发网络（CDN）公司 Cloudflare 本周宣布收购 [VoidZero](https://voidzero.dev/)，VoidZero 创始人 [Evan You](https://www.linkedin.com/in/evanyou/) 和 Cloudflare 高级工程总监 [Steve Faulkner](https://www.linkedin.com/in/stevenfaulkner/) 希望向使用其工具的开发者们明确一件事。

“Vite、Vitest、Rolldown、Oxc 和 Vite+ 将保持开源、厂商无关和社区驱动。这一点不会发生任何改变，”两人在[一篇博客文章](https://blog.cloudflare.com/voidzero-joins-cloudflare/)中写道。

VoidZero 以其围绕 [Vite](https://viteplus.dev/) 和基于 Rust 的技术为核心的 JavaScript 开发生态系统而闻名，其工具被广泛应用于前端和后端 Web 应用程序开发。

作为一次*人才收购*（acqui-hire，指以获取人才为目的的收购），VoidZero 的所有团队成员都将加入 Cloudflare。该公司坚持认为，它认识到“更好的互联网是开放的互联网”，而且最重要的工具和框架在设计上就是可移植的。因此，使用 Vite 构建的应用程序可以在任何地方运行，并且未来也将继续如此。

开发者社区对这一消息反应不一。[一些人质疑](https://news.ycombinator.com/item?id=48399142) VoidZero 最初的[投资合伙人](https://grokipedia.com/page/voidzero#:~:text=VoidZero%20secured%20its%20initial%20funding,of%20StackBlitz%20and%20Paul%20Copplestone.)（由全球风险投资公司 Accel 领投，以及数位天使投资人）是否会对这次收购感到满意，而[另一些人则单纯赞美](https://news.ycombinator.com/threads?id=valgaze)创始人 Evan You 及其团队多年来打造的“精美框架/工具”。

[debarshri 态度更为乐观](https://news.ycombinator.com/threads?id=debarshri)，他提醒我们，收购的发生主要有三个原因：产品、人才或业务增长。“在 AI 时代，该领域发生的一些收购是为了人才和产品。在这个案例中，看起来确实如此。Vite 是一个伟大的产品；他们能够建立一支伟大的团队，”他们写道，这表明 Cloudflare 声称致力于工程研发并为 VoidZero 系列项目提供资源的说法是有事实支撑的。

## 厌倦了不得不重构和迁移

持怀疑态度的代表是 [embedding-shape](https://news.ycombinator.com/item?id=48399359)，作为过去十年左右的库/框架/引擎/运行时用户，他们表示自己“基本上避开了”任何与风投投资相关的工具。“最终，这些工具要么会退化，要么会变得太贵，或者直接消失，我实在太厌倦了仅仅因为新主人做了一些糟糕的事情而不得不重构和四处迁移，”他们说道。

[demetris](https://news.ycombinator.com/item?id=48398694) 的讽刺意图则更为明显，他评论说自己很喜欢 Vite，但前提是他没有忘记它存在于项目中。“它把那些让你觉得自己智力不足的事情变得几乎无需配置。这个消息并没有让我感到高兴。今年早些时候关于 Astro 的消息也是如此，”他们写道。

这可能有点言过其实了。Cloudflare 在 [1 月份收购](https://blog.cloudflare.com/astro-joins-cloudflare/)内容驱动的 Web 框架 Astro 被一些人视为积极的一步，其中包括 Yucel F. Sahan，[他写道](https://tailkits.com/blog/cloudflare-acquires-astro/)，他期待“到 Cloudflare 的更好默认部署路径、适配器中更少棱角的更多‘黄金路径’，以及对混合渲染和缓存更清晰的指导。”

正如 Cloudflare 在收购 VoidZero 时重申的那样，“Astro 仍然是开源的，并且仍然可以部署在任何地方。团队仍在推进他们原有的路线图。”

尽管这些承诺不绝于耳，但[开发者 nja 并不买账](https://news.ycombinator.com/item?id=48399612)；他们认为这与 [Cloudflare 收购 BastionZero](https://www.cloudflare.com/press/press-releases/2024/cloudflare-acquires-bastionzero-to-add-zero-trust-infrastructure-access/) 以获取其零信任基础设施访问平台时的套路非常相似，让人感到有些不舒服。

“承诺很快就化为泡影，工具也退化了（我在短短一周内就发现了三个严重漏洞……他们甚至懒得发布更新日志），最后 Cloudflare 给我们发了一封‘嘿，我们实际上将在一个月内关闭这个服务，祝你好运’的电子邮件，导致我们不得不手忙脚乱地重新配置我们所有的基础设施，” nja 写道。

> “我曾见过开源项目被收购，然后目睹承诺被打破。这对我个人而言非常重要……只有当 Web 的底层工具和标准保持开放、可移植和共享时，Web 才能正常运转。我们不会把它变成 Cloudflare 的产品；它的价值在于其框架无关的特性。我的首要目标是确保该项目保持健康、社区驱动，并不断为每个人提供改进。” ——Steve Faulkner，Cloudflare。

## Cloudflare 工程总监：听着，我们明白

Cloudflare 工程总监 Steve Faulkner 告诉 *The New Stack*，团队理解这一切，并且他们“理解”各方表达的“质疑”。

“我也曾见过开源项目被收购，然后目睹承诺被打破。这对我个人而言非常重要，因为我的整个职业生涯都建立在 Web 之上，而只有当底层工具和标准保持开放、可移植和共享时，Web 才能正常运转，” Faulkner 说道。“Vite 现在是现代 Web 开发的基石，这也包括它在 Cloudflare 的运作方式。我们不会把它变成 Cloudflare 的产品；它的价值在于其框架无关的特性。我的首要目标是确保该项目保持健康、社区驱动，并不断为每个人提供改进。”

Faulkner 极力强调自己的观点，并重申了在 Astro 上开展的工作。他说，如果有人需要证据，公司在 Astro 加入 Cloudflare 时也做出了类似的承诺。

“我认为该项目持续推进的方式表明了我们是认真的。我们打算在这里采取同样的方法，大家应该监督我们履行这一承诺，”他说道。

尽管存在这些自卫式的证明，但也有一些开发者认为 Cloudflare 做得没错。为了说明在这个问题上大家的意见究竟有多分歧，[Ocdtrekkie](https://news.ycombinator.com/item?id=48399405) 表示“Cloudflare 确保了互联网的去中心化”，因为它提供了 AWS、Azure 和 Google Compute Engine (GCE) 之外的另一种选择。

“[这] 让你的个人自建托管小盒子或小型 VPS 能够获得与大型服务商同等水平的保护，” Ocdtrekkie 指出。“而且通常情况下，任何你托管在 Cloudflare 上或由其代理的内容，都可以非常简单地迁移到另一个服务商。而构建在 AWS、Azure 和 GCE 服务之上的东西往往会死死受限于这些平台。”

> “这也许是个激进的观点，但我认为目前没有任何一个达到临界用户规模的 JavaScript 工具能够免于被收购。原因在于，这些现代项目通常是以商业项目的形式启动并进行融资的，而这个行业中所有的商业项目最终都会寻求退出，” ——CodingJeebus。

## 如今的 JavaScript 领域，收购正当其时

从更高层面总结 JavaScript “购物车”现状的是 [CodingJeebus](https://news.ycombinator.com/item?id=48398353)，他对此一点也高兴不起来。

“这也许是个激进的观点，但我认为目前没有任何一个达到临界用户规模的 JavaScript 工具能够免于被收购。原因在于，这些现代项目通常是以商业项目的形式启动并进行融资的，而这个行业中所有的商业项目最终都会寻求退出，尤其是那些专注于增长并在生态系统中确立自身地位的项目，”他们写道。

针对当今软件行业可能并不受欢迎的现实，CodingJeebus 认为，那些无私维护驱动整个行业的底层开源包的开发者时代正在走向终结，这主要是因为他们正被那些从一开始就想创业并实现商业化变现的人所取代。

“谁能说这是对是错呢，但我认为这就是大势所趋，”他们推测道。

JavaScript 领域的重大收购包括 [Anthropic 吞并 Bun](https://thenewstack.io/bun-developers-complaints-anthropic/)（这是一款集 JavaScript、TypeScript 和 JSX 于一体的运行时及工具包）。与之类似，[GitHub 收购了 npm](https://thenewstack.io/github-acquires-npm-buying-microsoft-a-presence-in-the-node-javascript-community/)，这让微软更紧密地掌控了针对 Node.js 和 JavaScript 模块的杰出软件注册表。

稍早些时候，Web 开发平台公司 [Netlify 收购了 Gatsby](https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/)（一个基于 JavaScript 和 TypeScript，更具体地说是构建在 JavaScript 用户界面库 React 之上的 Web 交付和内容编排平台）。此外，前端即服务（FaaS）公司 [Vercel 收购了 Turborepo](https://www.businesswire.com/news/home/20211209005455/en/Vercel-Announces-Acquisition-of-Turborepo-Accelerating-the-Speed-of-Web-Development-and-Delivery-by-Eliminating-Complexity-in-Frontend-Codebase-Scalability/)，这是一款针对 JavaScript 和 TypeScript monorepo 的开源构建系统。

## Cloudflare 的后续承诺

鉴于一些开发者在 Cloudflare 收购 VoidZero 之后仍然感到有些紧张，该公司重申其首要目标是“维护信任”，正是这种信任才让 Vite 获得了如此广泛的采用。

为了在支持开源和共享生态系统基础方面用实际行动履行承诺，Cloudflare 正向 Vite 生态系统基金投入 100 万美元，该基金由 Vite 核心团队管理，用于支持维护者和贡献者。

大家都高兴吗？显而易见，情况是“有人欢喜、有人观望、有人反对”。

随着 Cloudflare 直面 [AWS CloudFront](https://aws.amazon.com/cloudfront/)（由于与 AWS 生态系统的原生集成，它对某些团队来说总是首选）、[微软 Azure Front Door](https://azure.microsoft.com/en-us/products/frontdoor) 以及 Akamai 等关键内容分发网络竞争对手，工具的自由度可能会被现有的技术栈版图所掩盖，而后者才是决定谁能最终胜出的长期因素。