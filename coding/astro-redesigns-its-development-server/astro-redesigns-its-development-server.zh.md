Astro——其[被Cloudflare收购](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/)的消息于周五宣布——于周三发布了其[Astro 6的首个测试版](https://astro.build/blog/astro-6-beta/)，其中包含重新设计的开发服务器。此版本还推出了新的内置API，用于处理内容安全策略（CSP）、字体和实时内容集合。

新的开发服务器内部利用了[Vite的](https://thenewstack.io/should-you-go-all-in-on-vite-a-risk-vs-reward-analysis/)[环境API](https://vite.dev/guide/api-environment)，这意味着Astro可以在开发者部署到的相同运行时中运行Web应用程序，使用相同的JavaScript引擎。

重构还允许Astro在真实运行时中运行。

Astro首席技术官Matthew Phillips在宣布该版本发布的官方博客文章中写道：“开发可以在与生产相同的运行时中执行。”

这也意味着Astro可以支持更多平台。目前，它支持[Cloudflare](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/) Workers。Matthew Phillips指出，新的运行时“为Astro解锁了一流的支持。”该博客文章深入探讨了Astro与Cloudflare的集成以及在此次重新设计之前所面临的挑战。

Matthew Phillips写道：“这一变化使得Astro 6对于所有运行时上的项目，包括非Node.js环境，都更加稳定。”

## Waku更新Cloudflare Worker适配器

说到Cloudflare，极简主义的[React框架Waku宣布](https://waku.gg/blog/cloudflare-workers-out-of-the-box)它已更新其[Cloudflare Worker适配器](https://waku.gg/guides/cloudflare)。

据数据和分析公司HundredX的首席软件工程师Rob Marcher称，[Cloudflare Workers](https://thenewstack.io/cloudflare-raises-1-25-billion-for-startups-using-its-workers-platform/)现已成为默认Waku适配器的一部分。

Rob Marcher表示：“此次发布带来了三项重大变化：自动适配器选择、静态部署支持以及访问绑定的新方式。”

Rob Marcher补充说，在即将发布的版本中，Waku计划“探索与`@cloudflare/vite-plugin`的集成，以提供与Cloudflare平台功能（如[Durable Objects](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/)）更深层次的集成。”

## Svelte发布五项漏洞补丁

周四，[Svelte发布了针对`devalue`、`svelte`、`@sveltejs/kit`和`@sveltejs/adapter-node`的五项漏洞补丁](https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem)。Svelte核心团队成员Elliott Johnson建议，使用这些软件包的开发者现在升级非常重要。

无漏洞版本为：

*   `Devalue`: 5.6.3
*   `Svelte`: 5.46.4
*   `@sveltejs/kit`: 2.49.5
*   `@svelte/adapter-node`: 5.5.1

Elliott Johnson在Svelte项目博客的一篇文章中写道：“在过去几周里，我们看到一系列高知名度漏洞影响了Web开发生态系统中的热门工具。”“虽然这些漏洞不幸，但看到社区齐心协力确保最终用户安全，这令人鼓舞。”

## Bun基准测试

软件工程师Özkan Pakdil最近在其[微服务框架基准测试](https://ozkanpakdil.github.io/posts/my_collections/2026/2026-01-10-bun-microservice-framework-benchmark/)中测试了JavaScript运行时Bun。

Özkan Pakdil在他的博客文章中谈到结果时表示：“一个JavaScript/TypeScript运行时与[Rust](https://thenewstack.io/rust-programming-language-guide/)框架竞争，这并不是我预期会看到的。”

他写道，Bun已为高性能工作负载做好了生产准备，平均响应时间为157毫秒，故障率为0%，这表明它能够处理大量流量。

他写道：“如果你正在启动一个新的微服务，并且你的团队了解JavaScript/TypeScript，Bun在开发者体验和性能之间提供了极佳的平衡。”“Bun和[Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/)之间的差距巨大：如果你目前正在使用Express.js并且需要更好的性能，那么Bun值得认真考虑。”

他提供了一张比较图表，显示了Bun与基于Rust的性能器（如[Warp](https://github.com/seanmonstar/warp)）的表现。Bun表现出色，排名第四，领先于[Rocket](https://rocket.rs/)和[Golang](https://thenewstack.io/golang-how-to-use-the-go-install-command/)。

他还探讨了Bun为何如此之快，得出结论是由于：

*   高度优化的Safari JS引擎，在某些工作负载下表现优于V8。
*   Zig实现。
*   一个原生HTTP服务器，他写道，它具有内置的服务器实现，绕过了Express等框架的开销。
*   优化的I/O。
*   由于原生TypeScript执行，减少了转译。

## 关于构建MCP服务器

API管理平台Zuplo最近发布了其“[MCP现状](https://zuplo.com/mcp-report)”报告，报告显示在[模型上下文协议服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)的使用标准化方面正在取得进展。Zuplo的调查受访者（由“近100名对MCP有深刻理解的技术专业人士”组成）中，超过一半的人表示，尽管他们相信MCP的长期可行性，但对于它是否会成为行业标准仍持怀疑态度。

这项研究的独特之处在于关注那些[构建](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/)MCP服务器（而不仅仅是使用）的人。它调查了52位曾构建MCP服务器的技术专业人士，这是更大调查池中的一个子集。在那些构建了MCP服务器的人中，58%的人主要是围绕现有API创建MCP封装器，而不是为MCP创建新的API或重建现有服务。

根据调查结果，MCP开发中最常用的框架是FastMCP (42%) 和Anthropic的SDK (38%)。到目前为止，30%的调查参与者表示他们通过[API](https://thenewstack.io/api-simulation-reduces-mcp-server-microservices-overload/)或MCP网关托管他们的MCP服务器，而30%是自托管。

*——作者：TNS分析师Lawrence Hecht，他在此次研究中与Zuplo进行了咨询。*