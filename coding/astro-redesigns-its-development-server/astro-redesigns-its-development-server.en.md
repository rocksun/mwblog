Astro — whose [acquisition by Cloudflare](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/) was announced on Friday — on Wednesday released its [first beta of Astro 6](https://astro.build/blog/astro-6-beta/), with a redesigned development server. This release also featured new, built-in APIs for working with content security policies (CSPs), fonts and live content collections.

The new development server leverages [Vite’s](https://thenewstack.io/should-you-go-all-in-on-vite-a-risk-vs-reward-analysis/) [Environment API](https://vite.dev/guide/api-environment) internally, which means Astro can run web applications inside the same runtime developers deploy to, with the same JavaScript engine.

The refactoring also allows Astro to run against real runtimes.

“Development can execute inside the same runtime as production,” Astro CTO [Matthew Phillips](https://www.linkedin.com/in/matthewcphillips) wrote in the company blog post announcing the release.

It also means Astro can support more platforms. Today, it supports [Cloudflare](https://thenewstack.io/cloudflares-balancing-act-protect-content-while-pushing-ai/) Workers. Phillips noted the new runtime unlocks “first-class support for Astro. ” The blog post delves into the Astro Cloudflare integration and the challenges it created before this redesign.

“This change makes Astro 6 more stable for projects on all runtimes, including non-Node.js environments,” Phillips wrote.

## Waku Updates Cloudflare Worker Adapter

Speaking of Cloudflare, the minimalist [React framework Waku announced](https://waku.gg/blog/cloudflare-workers-out-of-the-box) it has updated its [Cloudflare Worker adapter](https://waku.gg/guides/cloudflare).

[Cloudflare Workers](https://thenewstack.io/cloudflare-raises-1-25-billion-for-startups-using-its-workers-platform/) is now part of the default Waku adapter, according to Rob Marcher, principal software engineer at data and analytics firm HundredX.

“This release brings three major changes: automatic adapter selection, static deployment support and a new way to access bindings,” Marcher said.

In upcoming releases, Waku plans to “explore integration with `@cloudflare/vite-plugin` to provide even deeper integration with Cloudflare’s platform features like [Durable Objects](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/),” Marcher added.

## Svelte Releases Patches for Five Vulnerabilities

On Thursday, [Svelte released five vulnerability patches](https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem) across `devalue`, `svelte`, `@sveltejs/kit` and `@sveltejs/adapter-node`. It’s important that developers who use any of those packages upgrade now, advised Svelte core team member [Elliott Johnson](https://www.linkedin.com/in/selliottjohnson/).

The non-vulnerable versions are:

* `Devalue`: 5.6.3
* `Svelte`: 5.46.4
* `@sveltejs/kit`: 2.49.5
* `@svelte/adapter-node`: 5.5.1

“Over the last few weeks, we’ve seen a spate of high-profile vulnerabilities affecting popular tools across the web development ecosystem,” Johnson wrote in a post on the Svelte project’s blog. “While they are unfortunate, it has been encouraging to see the community pulling together to keep end users safe.”

## Benchmarking Bun

Software engineer [Özkan Pakdil](https://ozkanpakdil.github.io/) recently tested JavaScript runtime [Bun as part of his microservices framework benchmarking](https://ozkanpakdil.github.io/posts/my_collections/2026/2026-01-10-bun-microservice-framework-benchmark/).

“A JavaScript/TypeScript runtime competing with [Rust](https://thenewstack.io/rust-programming-language-guide/) frameworks was not something I expected to see,” Pakdil said about the results in his blog post.

Bun is production-ready for high-performance workloads with a 157ms mean response time and 0% failure rate that demonstrate it can handle serious traffic, he wrote.

“If you’re starting a new microservice and your team knows JavaScript/TypeScript, Bun offers an excellent balance of developer experience and performance,” he wrote. “The gap between Bun and [Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) is massive: If you’re currently using Express.js and need better performance, Bun is worth serious consideration.”

He included a comparison chart that shows how Bun performs against Rust-based performers such as [Warp](https://github.com/seanmonstar/warp). Bun held its own, ranking fourth ahead of [Rocket](https://rocket.rs/) and [Golang](https://thenewstack.io/golang-how-to-use-the-go-install-command/).

He also explored what makes Bun so fast, concluding that it’s due to:

* The highly optimized Safari’s JS engine, which outperforms V8 in certain workloads.
* The Zig implementation.
* A native HTTP server, which, he writes, has a built-in server implementation that bypasses he overhead of frameworks such as Express.
* The optimized I/O.
* The lack of transpiration due to the Native TypeScript execution.

## On Building MCP Servers

API management platform Zuplo recently released its “[The State of MCP](https://zuplo.com/mcp-report)” report, which shows progress is being made in standardizing the use of [Model Context Protocol servers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/). More than half of Zuplo’s survey respondents, comprised of “nearly 100 technical professionals with a strong understanding” of MCP, stated that while they believe in MCP’s long-term viability, there is still skepticism about whether it will become the industry standard.

The unique part of the study focused on [people who build](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/) — instead of just use — MCP servers. It surveyed 52 tech pros who have built a MCP server, a subset of the larger survey pool. Of those who have built MCP servers, 58% primarily created MCP wrappers around existing APIs rather than creating a new API or rebuilding existing services for MCP.

The most commonly used frameworks in MCP development, according to the survey findings, are FastMCP (42%) and Anthropic’s SDK (38%). So far, 30% of survey participants said they host their [MCP servers via an API](https://thenewstack.io/api-simulation-reduces-mcp-server-microservices-overload/) or MCP gateway, while 30% are self-hosting.

*—By TNS analyst Lawrence Hecht, who consulted with Zuplo on this study.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)