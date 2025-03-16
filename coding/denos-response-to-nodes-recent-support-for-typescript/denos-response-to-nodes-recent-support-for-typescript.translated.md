# Deno 对 Node 最近支持 TypeScript 的回应

![Featued image for: Deno’s Response to Node’s Recent Support for TypeScript](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)

[Node 现在支持 TypeScript](https://github.com/nodejs/node/blob/main/doc/api/typescript.md)，这将使其更符合替代运行时 [Deno](https://deno.com/?utm_content=inline+mention) 和 [Bun](https://thenewstack.io/bun-1-0-ships-as-node-js-and-deno-alternative/)，它们提供原生 [TypeScript](https://thenewstack.io/what-is-typescript/) 支持。TypeScript 允许开发人员定义数据类型，从而支持早期错误检测并防止 [JavaScript](https://thenewstack.io/three-javascript-proposals-advance-to-stage-4/) 中常见的运行时问题。

“基本上，TypeScript 向 JavaScript 添加了额外的语法，以支持与编辑器的更紧密集成，”Node 写道。“[它可以]在编辑器或 CI/CD 管道中及早发现错误，并编写更易于维护的代码。”

根据 InfoQ 的说法，原生 TypeScript 支持是[开发人员最需要的 Node 功能之一](https://www.infoq.com/news/2025/03/node-23-runs-typescript-natively)。它在[去年 8 月作为实验性功能添加](https://nodejs.org/en/blog/release/v22.6.0#experimental-typescript-support-via-strip-types)，但自 1 月以来已默认启用。

TypeScript 为 Node 提供了其他好处，包括静态类型，即变量的类型是已知的，并且在程序执行之前在编译时进行检查。根据 [Deno 博客文章对该新闻的回应](https://deno.com/blog/typescript-in-node-vs-deno)，向 JavaScript 添加类型有助于在项目增长时构建代码。它由 Deno 的创建者 Ryan Dahl 和产品营销经理 Andy Jiang 撰写。

他们指出，它主要处理两个任务：

- 类型检查，以确保您的变量与声明的类型匹配。
- [类型剥离，用于转译](https://nodejs.org/api/typescript.html#type-stripping)。在 TypeScript 中，开发人员可以向其代码添加类型注释，以提高可读性并捕获潜在的错误。

类型剥离是删除这些类型注释的过程，通常在构建过程中进行。它通常在将代码从具有类型注释的语言（如 TypeScript）转换为没有类型注释的语言（如纯 JavaScript）时完成。转译器采用以一种编程语言编写的源代码，并将其转换为另一种编程语言的源代码。

Deno 解释了 [Node](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/) 集成是如何工作的。

“这实际上是将以前由 ts-node 提供的功能直接集成到 Node 中，从而简化了 TypeScript 的执行，”他们写道。“Node 的 TypeScript 支持用空格替换类型注释，从而产生有效的 JavaScript……”

也就是说，Dahl 和 Jiang 指出，这种方法存在局限性，包括：

- 没有内置的类型检查，这意味着仍然需要像 tsc 这样的外部工具。
- 不支持 JSX 或 TSX：“Node 处理 .ts、.mts 和 .cts，但 React (.tsx) 和 JSX 项目仍然需要外部转译器或捆绑器，例如 esbuild、Babel 或 tsc，”他们写道。
- 手动管理 tsconfig.json：“类型检查仍然依赖于通过 tsconfig.json 进行的外部配置，”他们补充道。根据 InfoQ 的说法，Node.js 忽略 tsconfig.json 文件。

他们将此与 [Deno](https://thenewstack.io/deno-creates-board-charter-for-javascript-registry-project/) 如何处理这个问题进行了对比。

“[Deno 通过提供一个具有完全集成的 TypeScript 工具链的单个可执行文件来简化 Web 编程](https://thenewstack.io/ryan-dahl-from-node-js-and-deno-to-the-modern-jsr-registry/)，”Dahl 和 Jiang 写道。“这种方法以最少的配置提供 TypeScript 的优势，从而简化了测试、格式化和编译工作流程。”

[Deno 的 TypeScript](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/) 集成由三个主要部分组成：

- 执行：
[Google 的 V8](https://thenewstack.io/node-js-v8-gets-long-term-support-plus-commitment-google-v8/) 引擎直接执行 JavaScript，但不执行 TypeScript。
- 类型检查：
[Microsoft 的 TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/) 编译器（用 JavaScript 实现）在内部捆绑。
- 类型剥离：SWC，一个用 [Rust](https://thenewstack.io/rust-programming-language-guide/) 构建的高性能解析器，可以有效地剥离类型，而无需运行 JavaScript。

他们补充说，Deno 的工具链支持 TypeScript。

## Nuxt.js 添加惰性水合
[Nuxt.js](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata/) 3.16 版本增加了对原生延迟/懒加载 hydration 的支持，这使开发人员可以精确控制组件何时进行 hydration。Nuxt 是一个构建于 Vue 之上的开源 Web 应用程序框架，Vue 是一个用于构建用户界面的开源 JavaScript 框架。

[懒加载 hydration 可以提高初始加载性能](https://nuxt.com/blog/v3-16)和可交互时间，Nuxt 核心团队负责人 Daniel Roe 写道。

Nuxt 已经提供了 [Islands architecture](https://www.patterns.dev/vanilla/islands-architecture/#:~:text=Thus%20it%20provides%20built%2Din,on%20when%20they%20become%20visible.&text=It%20also%20supports%20lazy%20hydration,the%20hydration%20of%20the%20component)，它定义了页面的哪些部分是静态的，哪些部分是交互式的。懒加载 hydration 旨在控制这些交互式部分何时变为活动状态。两者经常结合使用，因为懒加载 hydration 可以优化各个“岛屿”的 hydration。

此次更新还包括其他功能和性能增强。

例如，Nuxt 通过 `create-nuxt` 简化了框架启动项目，`create-nuxt` 是一个用于启动 Nuxt 项目的新工具。

“它是 `nuxi init` 的简化版本——只有六分之一的大小，并捆绑为单个文件，所有依赖项都内联，以便让您尽快启动，”Roe 写道。

现在，可以使用以下命令启动一个新项目：

```bash
npm create nuxt
```

Nuxt 团队还进行了一些性能改进，例如：

- 将 exsolve 用于模块解析以及 unjs 生态系统的其余部分（nitro、c12、pkg-types 等），这“极大地”加快了模块解析速度，Roe 说；
- 更智能的模块解析路径，优先考虑直接导入以提高效率；
- 消除重复的 Nitro 别名解析，以实现更精简的文件处理，以及
- 通过跳过不必要的解析步骤来简化 `loadNuxt`，从而加快启动速度。

“为了增加一些轶事证据，我在 [roe.dev](https://thenewstack.io/goodbye-saas-hello-ai-agents/) 上的个人网站使用 v3.16 加载速度提高了 32%，而 Nuxt.com 提高了 28%，”Roe 写道。“我希望你也能看到类似的结果！”

## 谷歌推出 Gemma 3，新的 AI 安全检查器

谷歌本周推出了 [Gemma 3](https://developers.googleblog.com/en/introducing-gemma3/)，这是一系列轻量级开放模型。Gemma 3 采用与 Gemini 2.0 模型相同的研究和技术构建。

谷歌 DeepMind 研究副总裁 Clement Farabet 和总监 Tris Warkentin 在周三发布的 [一篇博客文章中介绍了这些模型](https://blog.google/technology/developers/gemma-3/)。

Warkentin 和 Farabet 写道：“它们旨在直接在设备上快速运行——从手机和笔记本电脑到工作站——帮助 [开发人员创建 AI 应用程序](https://thenewstack.io/top-strategies-for-building-scalable-and-secure-ai-applications/)，无论人们在哪里需要它们。”

[Gemma 模型是开源的](https://thenewstack.io/the-open-source-ai-definition-is-out/)，并提供开放权重。Gemma 3 有以下尺寸：1B、4B、12B 和 27B。

随着越来越多的组织开始构建自己的 AI 应用程序和 AI 代理，[较小的语言模型正变得越来越流行](https://thenewstack.io/why-red-hat-thinks-ais-future-is-small-language-models/)。
谷歌还推出了 [ShieldGemma2](https://developers.googleblog.com/en/safer-and-multimodal-responsible-ai-with-gemma/)，这是一个基于 Gemma 3 基础构建的 4B 图像安全检查器。

该帖子称：“ShieldGemma 2 提供了一个现成的图像安全解决方案，可跨三个安全类别输出安全标签：危险内容、性暴露和暴力。”“开发人员可以根据自己的安全需求和用户进一步定制 ShieldGemma。”

学术研究人员可能需要注意，谷歌还提供 Gemma 3 学术计划，该计划允许学术研究人员申请 Google Cloud 积分（每个奖项价值 10,000 美元），以加速他们基于 Gemma 3 的研究。[申请流程本周开放](https://ai.google.dev/gemma/)，并将保持开放四周。

## OpenAI 发布用于构建 AI 代理的开发者工具

[OpenAI 发布了“第一组构建块”](https://openai.com/index/new-tools-for-building-agents/)，以帮助开发人员在其平台上更有效地构建代理。AI 代理被定义为可以独立自动化任务的 AI 支持系统。
过去一年，我们推出了新的模型功能——例如高级推理、多模态交互和新的安全技术——这些都为我们的模型奠定了基础，使其能够处理构建 Agent 所需的复杂、多步骤任务，” OpenAI 团队在宣布这一消息时写道。“然而，客户们表示，将这些功能转化为可用于生产的 Agent 具有挑战性，通常需要大量的 prompt 迭代和自定义编排逻辑，而且缺乏足够的可观测性或内置支持。”

为了支持 AI Agent 的开发，本周该公司发布了一个新的 [Responses API](https://community.openai.com/t/introducing-the-responses-api/1140929)，OpenAI 解释说，它“结合了 Chat Completions API 的简单性和 [Assistants API](https://platform.openai.com/docs/api-reference/assistants) 的工具使用功能，使开发人员能够构建 Agent 的核心逻辑”。

API 中内置的工具包括使用与 ChatGPT 搜索相同的底层模型的网络搜索、文件搜索以及使用与 Operator 相同的底层模型的计算机使用。OpenAI 补充说，这使 AI Agent 能够访问他们所需的有用信息和工具。

还有一个新的 [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk) 用于编排单 Agent 和多 Agent 工作流程，以及集成的可观测性工具来跟踪和检查 Agent 工作流程的执行情况。

欲了解更多信息，开发人员可以观看 [直播视频](https://openai.com/live/)，其中包含一些参与该工具开发的团队成员。

## 纽约时报将 Enzyme 迁移到 React Testing Library

[纽约时报发布了一个小型案例研究](https://open.nytimes.com/how-the-new-york-times-systematically-migrated-from-enzyme-into-react-testing-library-b3ea538d001c#225:%20React%20Router)，讲述了其在将核心站点的 [React](https://thenewstack.io/a-react-based-open-source-tool-for-creating-data-tables/) 库从 React 16 升级到 React 18 时面临的最大挑战。
事实证明，他们面临的最大问题之一是将他们的代码库从 Enzyme 测试实用程序（一种专门为 React 组件设计的 JavaScript 测试实用程序）转换为 [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)。

React Testing Library 是一个流行的 JavaScript 测试实用程序，专注于从用户的角度测试 React 组件。该文章解释说，这两个库在单元测试方面存在重大差异。它详细介绍了纽约时报的升级过程，并包含代码示例，以便开发人员可以看到 [Enzyme](https://enzymejs.github.io/enzyme/) 和 React Testing Library 之间的区别。

## 发现 WordPress 插件漏洞

[Word Fence 发现了一个漏洞](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/all-in-one-wp-migration/all-in-one-wp-migration-789-unauthenticated-php-object-injection)，该漏洞存在于 All-in-One WP Migration and Backup 插件中——根据 [SearchEngine Journal](https://www.searchenginejournal.com/wordpress-backup-plugin-vulnerability-affects-5-million-websites/541952/)，该插件的安装量超过 500 万次。这个高危漏洞已被发现并已修复。
SearchEngine Journal 报道说：“这种漏洞的工作方式是，WordPress 插件在备份恢复期间处理潜在的恶意数据，而没有正确验证它。”“但由于攻击机会有限，因此利用它变得不那么直接。”

[
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
]