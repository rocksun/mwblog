
<!--
title: Next.js部署规范简化前端托管
cover: https://cdn.thenewstack.io/media/2025/05/bdbe5393-img_0004.jpeg
summary: Next.js推出新规范简化前端托管！告别厂商锁定，拥抱开源自由。第三方托管商如Netlify、Cloudflare无需再为适配Next.js的私有构建格式头疼。新规范旨在实现框架与基础设施的松耦合，降低维护成本，提升开发者体验，让Next.js在各平台如Vercel一样流畅运行。
-->

Next.js推出新规范简化前端托管！告别厂商锁定，拥抱开源自由。第三方托管商如Netlify、Cloudflare无需再为适配Next.js的私有构建格式头疼。新规范旨在实现框架与基础设施的松耦合，降低维护成本，提升开发者体验，让Next.js在各平台如Vercel一样流畅运行。

> 译自：[Next.js Deployment Spec Simplifies Frontend Hosting](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/)
> 
> 作者：Loraine Lawson

继 Web 托管平台 Netlify [发出呼吁](https://www.netlify.com/blog/how-we-run-nextjs/) 之后，Next.js 即将推出一项新规范，旨在简化基础设施提供商部署开源框架的方式。这项新规范将使由 Vercel 创建和维护的框架与其他框架（如 [Astro](https://thenewstack.io/astro-5-2-brings-tailwind-4-support-and-new-features/)、[Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)、[Remix](https://thenewstack.io/why-some-developers-are-unhappy-with-react-router/)、[SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) 和 [Qwik](https://thenewstack.io/how-to-build-embed-components-with-astro-qwik-and-stackblitz/)）保持一致。

该规范将减少第三方托管提供商（包括 Vercel 的竞争对手 [Netlify](https://thenewstack.io/netlify-makes-preview-servers-available/) 和 [CloudFlare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/)）为完全支持该框架而必须做的工作。托管服务使用这些规范来构建框架的适配器、插件或预设。

托管提供商需要这些适配器来在托管使用框架构建的应用程序时配置和配置基础设施。如果没有这样的适配器，他们必须手动编写一个工具来确保框架按预期运行。

这是在开发人员的视野之外完成的，因此 Next.js 开发人员可能没有遇到这个问题——这取决于他们的提供商。例如，Netlify 已经在幕后设计了一个解决方案。

## 框架和基础设施

[Next.js](https://thenewstack.io/build-a-real-time-bidding-system-with-next-js-and-stream/) 由 Vercel 的 CEO 和创始人 Guillermo Rauch 创建。这导致一些开发人员想知道 Vercel 和 Next.js 是否过于紧密地结合在一起。
这是一个合理的问题，但还应该注意的是，Netlify 之前聘用了 Solid 的 Ryan Carniato，而 SvelteKit 的 Rich Harris 是 Vercel 的员工。最近，TanStack 宣布 Netlify 将成为其官方部署提供商。

Netlify 在 3 月份的一篇文章中犹豫但果断地指出了 Next.js 缺乏规范的问题，尽管它指出 Vercel 一直在幕后与 Netlify 合作以纠正这种情况。问题似乎在于进展的速度。

这篇文章由 Netlify 的框架工作人员软件工程师 Philippe Serhal 和首席产品经理 Elad Rosenheim 撰写，列出了托管服务在使用 Next.js 时遇到的一些问题，并指出该框架没有适配器、预设或插件来与其他基础设施提供商合作。

他们写道：“……Next.js 构建使用私有的、很大程度上没有文档化的格式，该格式可能会发生变化。”“……像 Netlify、Cloudflare、[AWS](https://aws.amazon.com/?utm_content=inline+mention) Amplify Hosting、SST、Google Firebase App Hosting 和 Microsoft Azure Static Web Apps 这样的提供商必须改为从磁盘读取 Vercel 定制的、部分未记录的构建输出，将其转换为自己的格式，然后将其写回磁盘。”

他们特别提到了最近的 [Next.js 安全事件](https://thenewstack.io/researchers-find-next-js-middleware-vulnerability/)，其中包括支持该框架的困难列表，以及它必须在幕后做的工作，以使 Next.js 以与 Vercel 相同的方式运行（同时指出它不必对其他框架这样做）。

Netlify 表示：“其中许多——以及可以说事件响应——都与 Next.js 的维护方式的封闭性有关。但现在每个人都在真诚地努力解决这个问题。”

该帖子补充说，[开源软件](https://thenewstack.io/open-source-development-threatened-in-europe/) 的一个主要好处应该是能够将其移植到不同的提供商。

据 Vercel 产品副总裁 Lee Robinson 称，该规范已经在幕后制定了六个月，Lee Robinson 也是 Next.js 框架的讲师。他同时教授 Next.js 框架。
这始于去年十月，在 Next.js Ship 大会上，我们宣布了一系列针对 [Next.js 开发人员](https://thenewstack.io/introduction-to-vercel-frontend-as-a-service-for-developers/)的改进，这些开发人员正在进行自托管，”Robinson 告诉 The New Stack。“从那时起，我们一直在幕后与基础设施公司合作，为这项工作添加新功能。”

Robinson 说，“诚实的现实”是，与基础设施一起开发一个开源工具是有益的，因为它允许基础设施团队了解事物在实践中是如何构建和部署的。

“我们喜欢这样思考：高内聚，但松耦合。因此，框架和基础设施之间是高内聚的，但理想情况下，是松耦合的，这样你就可以将该框架放在任何你想要的地方，”他说。“即使我们已经有了松耦合，我认为像文档这样的东西给人一种实际上它与 Vercel 紧密相连的印象。”

他补充说，Cloudflare 和 Netlify 缺少适配器也使得“对于那些想要部署到 Vercel 竞争对手的人来说，这是一个令人困惑的故事。”

Next.js 团队同意需要该规范，并开始与 Netlify 和 Cloudflare 合作开发部署适配器 API，他补充说。在幕后，Vercel 也构建了一个适配器来与该框架一起工作。

“这不是一个新颖的想法。如果你看看生态系统中的其他框架——SvelteKit 和其他框架——它们也落在了类似的位置，即有一种与提供商无关的方式来获取框架，并使其在任何基础设施平台上都能很好地工作，”Lee 说。

他同意缺少适配器意味着基础设施公司需要“自己完成大量工作，并对某些部分进行逆向工程”，并补充说 Next.js 团队希望简化该过程。

该规范还解决了开发人员想要的东西：选择他们托管应用程序的位置的能力。

“开发人员在选择开源工具时想知道的是，他们不会被锁定在该工具中，”Robinson 说。“他们可以自由使用他们想要的任何平台。如果他们愿意，他们可以自由地进行自托管或使用服务，并且他们对项目的管理、维护本身充满信心。”

该适配器目前处于“征求意见”阶段，并且在 Netlify 发布帖子后，该团队将其公开。他的计划是在下个月为基础设施平台提供一些东西，他说。

“我们仍在与 Netlify 和 Cloudflare 以及其他想要构建自己的适配器的人合作，或者基本上转换他们已经构建的东西并将其转换为这种新格式，”他说。“最终，幕后发生的事情是，当你将 Next.js 部署到 Netlify 时，他们会自动为你安装此适配器，这基本上就是今天发生的事情。只是[说]遵守此规范对他们来说更容易维护。”

除了解决这个问题之外，Robinson 说他们正在清理文档，删除专门提到 Vercel 的语言，以明确它将在其他平台上工作。