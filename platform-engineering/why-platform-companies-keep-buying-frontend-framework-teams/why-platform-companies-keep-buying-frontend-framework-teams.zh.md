上周晚些时候，全球云平台 Cloudflare [收购了 Astro 背后的公司](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/)，Astro 是[领先的前端框架](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/)之一。这遵循了一种模式：流行框架被平台公司收归旗下——或者至少获得它们的财务支持。

这一趋势或许始于2021年，当时 [Vercel 聘请了](https://thenewstack.io/vercel-and-svelte-a-perfect-match-for-web-developers/) Svelte 的创建者 Rich Harris。同年，WordPress 供应商 [Automattic 收购了](https://thenewstack.io/frontity-and-the-future-of-wordpress-as-a-dev-platform/)一家名为 Frontity 的 React 框架公司。2022年，全球电商公司 [Shopify 收购了 Remix](https://shopify.engineering/remix-joins-shopify/)。2023年，[Netlify 收购了 Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)。2024年，静态网站生成器 Eleventy [加入了 Font Awesome](https://www.11ty.dev/blog/eleventy-font-awesome/)。2025年，[Vercel 收购了 NuxtLabs](https://thenewstack.io/creators-of-nuxt-js-and-nitro-join-vercel/)，该公司是 Nuxt 背后的力量。同样在去年，[Figma 收购了 Payload](https://www.figma.com/blog/payload-joins-figma/)，一个有前景的（[虽然有些不同寻常的](https://thenewstack.io/introduction-to-payload-a-headless-cms-and-app-framework/)）应用程序框架。

而现在，我们看到 Cloudflare 收购了 Astro 网页框架的创建者 The Astro Technology Company。那么 Cloudflare 想要一个前端框架做什么呢？

## Cloudflare 想要什么

在[宣布收购 Astro 时](https://blog.cloudflare.com/astro-joins-cloudflare/)，Cloudflare 没有透露太多——它主要只是重复了 Astro 的口号：“内容驱动的网站”。

但不难看出，此次收购如何补充了 Cloudflare [“帮助构建更好的互联网”的使命](https://www.cloudflare.com/en-gb/about-overview/)。是的，这是一个相当模糊的使命宣言。但在过去一年中，该公司清楚地表明了[其对独立网站的支持](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/)，因为世界各地的在线创作者都在努力应对 AI 公司免费“吸取”他们的内容，以及（并非无关地）[搜索推荐流量枯竭](https://thenewstack.io/google-ai-overviews-and-citations-tips-for-web-publishers/)的问题。

去年，首席执行官 Matthew Prince 宣布7月1日为“[内容独立日](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)”，并要求 Google、OpenAI 和 Anthropic 等公司为 AI 抓取向网站创作者支付报酬。Cloudflare 还为网站运营商提供了各种工具，以防止 AI 机器人使用他们的内容。但 Cloudflare 也没有逃避 AI。它正在谨慎地试验旨在帮助网站创作者的特定 AI 技术——例如推出 [NLWeb](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/) 的一个实现，这是一个新兴协议，使发布者能够将 AI 聊天整合到他们的网站中，这种方式实际上可能会增加流量，而不是减少流量。

> Cloudflare 之所以被 Astro 吸引，部分原因在于它为网页开发者提供了 React 框架之外的一个可行替代方案。

Cloudflare 始于2009年的内容分发网络（CDN），因此它一直痴迷于网络速度。我认为，说 Cloudflare 被 Astro 吸引，部分原因在于它为网页开发者提供了一个[可行的 React 框架替代方案](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)，这并非过于简单化。React 框架以创建臃肿、JavaScript 密集且（是的）缓慢的网站和应用程序而臭名昭著。另一方面，Astro 奉行“默认零 JavaScript”策略，这——加上其[“岛屿”架构](https://thenewstack.io/how-astro-and-its-server-islands-compare-to-react-frameworks/)——通常能显著提升网站速度。

许多开放网络倡导者——包括我在内——认为 React 对网络的长期健康发展不利。因此，通过支持 Astro，Cloudflare 绝对是在“帮助构建更好的互联网”。（请注意，Astro“支持所有主流 UI 框架”，因此您可以在 Astro 中使用 React；但是，还有许多更好的选择可用）。就 Fred Schott 而言，Astro 创始人 Fred Schott 在[他的声明帖中](https://astro.build/blog/joining-cloudflare/)明确表示，“Astro 将保持免费、开源和 MIT 许可。”他补充说，Cloudflare 的支持将使他的团队不必担心业务建设，而是“开始100%专注于代码，共同致力于推动网络发展。”

## 框架收购出错时

公司收购框架（或者至少雇佣维护它们的人）的最大风险是，公司的优先事项会发生变化，支持会逐渐减少。

Netlify 于2023年2月收购 Gatsby 的案例提供了这方面的深刻教训。当 Netlify [宣布此次收购时](https://www.netlify.com/press/netlify-acquires-gatsby-inc-to-accelerate-adoption-of-composable-web-architectures/)，它承诺“将权力掌握在开发者手中”，并“致力于成为 Gatsby 开源项目的优秀管理者”。但到同年9月，联合创始人 Kyle Mathews 和 Sam Bhagwat 都[离开了 Netlify](https://blog.xavie.mirmon.co.uk/farewell-gatsby-its-been-one-heck-of-a-ride-cd18b91b0020)，并且似乎不再为 Gatsby.js 框架做贡献。

由于 Gatsby.js 是开源的，您可以在 GitHub 项目中追踪社区的反应。2023年11月，有人询问[该项目是否已停止维护](https://github.com/gatsbyjs/gatsby/issues/38696)。Netlify 首席执行官 Matt Biilmann [回复称](https://github.com/gatsbyjs/gatsby/issues/38696#issuecomment-1817064739)，“Gatsby 将继续存在，我们不会让它退役。”不过，他承认，“Gatsby 不再是流行的热门新框架”已是公开的秘密。他的意思基本上是，Netlify 将把 gatsby.js 保持在维护模式。

该评论串的其余部分充满了开发者推荐转向 Astro 或 Next.js 等其他框架。2024年8月，丹佛的开发者 Justin Carroll 在该项目中开启了另一个 GitHub 讨论，题为“[GatsbyJS 正式消亡了吗？](https://github.com/gatsbyjs/gatsby/discussions/39062)”他指出，“仓库中有‘修复’提交，但没有大的开发”，并补充说，“我一直热爱 Gatsby，并用 GatsbyJS 建立了一个非常成功的小副业，但我感到被抛弃了，我想要一个了结。”

Netlify 软件工程师 Philippe Serhal [回复说](https://github.com/gatsbyjs/gatsby/discussions/39062#discussioncomment-11337756)，他提到了 Biilmann 9个月前的评论。他写道：“从那时起没有改变，我们也没有改变这种做法的计划。”他补充说：“我相信当前有限的开发水平（安全修复、有限的依赖更新、易于解决的错误修复和性能改进、解决即将到来的第三方 API 弃用等）与我们所传达的信息是一致的。”

你必须赞扬 Netlify 清晰的沟通，尽管这些信息被埋藏在几个 GitHub 讨论串中。然而，Gatsby 框架不再是新开发项目的可行选择，这是不争的事实。开发者根本不再关心它。在其余的评论中，Astro 似乎比 Next.js 获得了更多作为 Gatsby 替代品的推荐——这表明 Astro 在当时越来越受欢迎。

## 赞助路线风险更小

尽管 Cloudflare 收购了一家公司 (The Astro Technology Company)，但有时公司可以通过雇佣主要维护者（通常是框架的创建者）或以某种方式赞助他们来影响框架。通常，这种情况发生在只有一个人控制项目时——就像 Harris 的 Svelte 和 Leatherman 的 Eleventy。

有时，公司与项目维护者之间的这种合作关系会成功；去年3月，TanStack 的创建者 Tanner Linsley 与 [Netlify 建立了合作关系](https://tanstack.com/blog/netlify-partnership)，并一直持续到今天。但有时它们并不成功。Leatherman 也为 Netlify 工作了几年，包括[从2022年2月起](https://www.zachleat.com/web/eleventy-oss/)仅为维护 Eleventy 而获得报酬。但他于[2023年中期离开 Netlify](https://www.zachleat.com/web/eleventy-side-project/)，并独立运营 Eleventy 一段时间，直到2024年9月加入 Font Awesome。

对于社区和维护者而言，雇佣或赞助方式的好处是，管理框架的人通常会保留对它的控制权。因此，Leatherman 离开 Netlify 后，按照自己的意愿继续他的项目。同样，我们可以假设 Linsley 和 Harris 也有这种选择。但如果出于某种原因，Astro 的主要维护者 Fred Schott 辞去了 Cloudflare 的工作，会发生什么呢？这尚不清楚，因为尽管 Astro 仍然是开源的，但 Schott 和那些留在 Cloudflare 的维护者之间现在可能会出现冲突。

希望 Cloudflare 和 Astro 的“联姻”永远不会走到那一步，但当公司收购流行框架背后的公司时，这是一个不可否认的风险。这也是为什么当这种情况发生时，开源社区通常会感到不安。