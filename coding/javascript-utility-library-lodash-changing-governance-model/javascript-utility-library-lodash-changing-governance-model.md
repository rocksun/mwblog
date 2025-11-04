
<!--
title: Lodash治理模式巨变：JavaScript工具库的未来走向
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
summary: Lodash将转型社区治理；Next.js新增缓存、开源Evals；TanStack Start黑客马拉松进行中；Deno Deploy重建；Vercel发布工作流开发工具包、代理调查。
-->

Lodash将转型社区治理；Next.js新增缓存、开源Evals；TanStack Start黑客马拉松进行中；Deno Deploy重建；Vercel发布工作流开发工具包、代理调查。

> 译自：[JavaScript Utility Library Lodash Changing Governance Model](https://thenewstack.io/javascript-utility-library-lodash-changing-governance-model/)
> 
> 作者：Loraine Lawson

在 [Ulises Gascón](https://github.com/ulisesgascon) 看来，[Lodash](https://github.com/lodash/lodash) 的情况正在发生变化，[项目正在开启新篇章](https://blog.ulisesgascon.com/the-future-of-lodash)。Gascón 是 Express 技术委员会成员、[Node.js](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) 核心贡献者和发布者，以及 TC39 代表。

Lodash 是一个流行的开源 JavaScript 实用工具库，为常见的编程任务提供实用、高效和一致的函数。它简化了与核心 JavaScript 数据结构（如数组、对象、数字和字符串）的交互。根据 [OpenJS 基金会](https://openjsf.org/) 的数据，超过 930 万个实时网站使用它，其中包括全球前 10,000 个网站中的三分之一，npm 每周下载量超过 25.7 亿次。

Lodash 所属的 OpenJS 基金会表示：“自 2012 年以来，Lodash 一直是 JavaScript 开发的基石，影响范围巨大。”“它出现在前端和后端代码、云函数、CMS 平台、构建工具和 CI 流水线中。”

文章指出，许多开发者也“通过 React、webpack 等框架间接依赖它，这使其成为一个关键的数字基础设施，但并非总是得到积极维护”。

问题在于它一直由一个人维护：[John-David Dalton](https://www.linkedin.com/in/john-david-d/)。Gascón 表示，未来，该项目将过渡到更可持续的模型。

Gascón 写道：“为了让 Lodash 长期保持活力，我们需要分散决策权和维护工作量。”

他写道，第一步将是建立一个技术治理结构，类似于技术指导委员会，共同承担责任并寻求基于共识的决策。

该库还将考虑弃用主库的一些“变体”，恢复持续集成系统并改进安全模型。

Gasćon 说，该库团队还将“采用基金会的 CNA […] 来处理事件并请求 CVEs [常见漏洞和暴露]，通过 GitHub Advisory 改进报告渠道，并在事件响应计划中记录安全发布流程，就像其他项目已经做的那样。”

本月，[Sovereign Tech Agency 已委托开展工作](https://openjsf.org/blog/sta-supports-lodash) 以支持 Lodash 的过渡。

## Next.js 的新变化

当 Next.js 前端程序员停止开发服务器时，他们所有的工作都会被丢弃，开发者必须在一个新的开发会话中从头开始。为了解决这个问题，Next.js 推出了一项针对开发的新的文件系统缓存测试版功能。

Vercel 首席执行官兼 Next.js 创建者 [Guillermo Rauch](https://www.linkedin.com/in/rauchg/) 表示：“它通过利用文件系统，即久经考验的可靠的文件系统，将 [Turbopack](https://thenewstack.io/next-js-13-debuts-a-faster-rust-based-bundler/) 的内存任务跟踪扩展到完整的服务器重启。”“这对于生态系统中最大的项目来说将特别棒。”

该框架还准备通过开源其 Next.js evals 来更好地服务 AI 代理。这是一个许多[框架都在努力解决](https://thenewstack.io/new-open-source-tool-from-angular-scores-vibe-code-quality/) 的问题——如何让大型语言模型 (LLM) 在纠正常见错误的同时反映框架的最佳实践。

Rauch 说：“Next evals 是一个公开基准，它跟踪最新的模型和编码代理在构建 Next.js 方面的表现如何。”“这是对生态系统的一项投资。”

## TanStack Start 黑客马拉松正在进行中

[TanStack Start](https://thenewstack.io/tanstack-introduces-new-meta-framework-based-on-its-router/) 将向其[黑客马拉松获奖者](https://www.convex.dev/hackathons/tanstack) 提供 14 万美元的现金、奖品和积分。

一等奖将获得 5,000 美元，外加 10 万美元的 Cloudflare 积分；与 TanStack 创建者 [Tanner Linsley](https://www.linkedin.com/in/tannerlinsley) 的办公时间；TanStack 商品和贴纸包；CodeRabbit 积分和周边；3 个月免费的 FireCrawl 增长计划；6 个月 Convex Pro；Netlify 积分；以及 Convex 周边。

二等奖将获得 3,000 美元，外加 2.5 万美元的 Cloudflare 积分；CodeRabbit 积分和周边；3 个月免费的 FireCrawl 增长计划；Netlify 积分；以及 Convex 周边。

最后，三等奖将获得 2,000 美元，外加 5,000 美元的 Cloudflare 积分；CodeRabbit 积分和周边；3 个月免费的 FireCrawl 增长计划；Netlify 积分；以及 Convex 周边。

您可以在公告页面找到评委名单和可用资源。构建要求相当简单。应用程序必须在 10 月 29 日或之后启动。它必须使用 TanStack Start、Convex、CodeRabbit、Firecrawl 和 [Cloudflare](https://thenewstack.io/cloudflare-for-ai-helps-businesses-safely-use-ai/)。

该团队在公告中写道：“构建一些能够真正展示 TanStack Start 在丰富交互性、实时更新、服务器流、协作工具、全栈路由以及使用 Convex、CodeRabbit、Firecrawl、Netlify、Autumn 和 Cloudflare 进行 RPC 方面的能力。”

活动于周四开始，持续到 11 月 17 日，申请提交截止时间为太平洋时间中午 12 点。获奖者将于 11 月 24 日公布。[注册现已开放](https://luma.com/tanstackstarthackathonv1)。

## Deno Deploy 重建

据 Denoland 开发者关系主管 [Phil Hawksworth](https://github.com/philhawksworth) 称，Deno Deploy（一个用于构建、部署和扩展现代 Web 应用程序和边缘函数的无服务器云平台）已从头开始重建。[Deno 是一个 JavaScript 运行时](https://thenewstack.io/deno-2-0-angular-updates-anthropic-for-devs-and-more/)。

Hawksworth 补充说，更新版本已经过早期访问计划，现已可以使用。

新版本中包含的更新有：

*   集成的 CI/CD，因此您可以在 Deno Deploy 内部或您自己的 CI/CD 上运行您的构建。
*   使用数据变得容易，这意味着开发者可以从 [KV](https://deno.com/kv) 开始，然后在必要时轻松升级到完整的数据库。
*   Postgres。“我们简化了将第三方数据库提供商的数据库链接和配置到您的应用程序的方式，使其符合开发者使用代码的方式，”Hawksworth 写道。“我们的数据库集成在幕后做了一些工作，为您的每个开发和生产环境创建数据库实例。这意味着您可以为您的某个应用程序配置或分配一个数据库，并为每个环境获得独立的数据库。”
*   更多指标，所有应用程序都提供开箱即用的数据和分析支持。它还通过内置的 OpenTelemetry 支持自动可观测性。

另一个目标是使 Deno Deploy 更容易试用，为了支持这一点，Deploy 现在会根据您的项目代码自动应用集成和预设。

## Vercel 发布工作流开发工具包和代理调查

上周，Vercel 举办了 Next.js 大会，发布了关于 [Next.js 框架如何演变](https://thenewstack.io/how-next-js-got-its-snappy-client-navs-back/) 的消息。

这家前端基础设施公司还推出了一款新的 [Vercel 工作流开发工具包](https://vercel.com/blog/introducing-workflow)，这是一个用于构建持久、可靠和可观测应用程序和 AI 代理的 TypeScript 框架，这家前端基础设施公司表示。它现在[已作为开放测试版发布](https://vercel.com/changelog/open-source-workflow-dev-kit-is-now-in-public-beta)。

Vercel 在其新闻稿中表示，它引入了一种用于长时间运行代码的新执行模型。开发者可以在普通异步函数中使用两个声明性指令来表达持久性应该存在的位置：

*   `use workflow` ; // 定义持久性工作流边界
*   `use step` ; // 定义具有持久性和重试的原子工作单元

Vercel 指出：“这个模型让开发者能够编写能够经受重启、部署和故障的代码，而无需管理队列、调度器或数据库。”

WDK 消除了手动配置队列、数据库或重试的需要。Vercel 澄清说，它不是一个作业调度器或队列库，而是一个“用于可靠、可恢复执行的代码级原语”。

其主要功能是：

*   代码优先的持久性：“直接在代码中声明您的逻辑应如何持久化，”Vercel 解释道。“工作流会自动保存进度、重试失败并从上次成功的步骤恢复。”
*   熟悉的开发者体验：这些指令集成到开发者已经编写的代码中，无需 YAML 文件、状态机或编排服务器。
*   框架定义的基础设施：部署到 Vercel 时，平台通过框架定义的基础设施自动预配所有必需的基础设施。
*   开源和可移植：工作流可以配置为在不同环境中执行。
*   专为长时间运行、可靠的系统而设计。

该公司还推出了 [Vercel 代理调查](https://vercel.com/changelog/vercel-agent-investigations-now-in-public-beta)，这是一个新的智能监控系统，可自动检测应用程序中的问题，进行根本原因分析，然后提供行动补救计划以更快地解决事件。它也已提供公共测试版。