[Aspire](https://aspire.dev/) 是微软的开源云原生开发平台，现在正式支持 [JavaScript](https://thenewstack.io/introduction-to-javascript/)、[TypeScript](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/)、[Python](https://thenewstack.io/what-is-python/) 和 [Java](https://thenewstack.io/java-developers-get-multiple-paths-to-building-ai-agents/)。

“通过 Aspire 13，JavaScript 和 TypeScript 开发者也能加入进来——我说的可不是那种半生不熟的集成，”微软高级软件工程师 David Pine 在 [微软开发者博客](https://devblogs.microsoft.com/aspire/aspire-for-javascript-developers/) 上写道。“这是对分布式系统中 JavaScript 应用编排的一流、全功能支持。”

该工具此前名为 .Net Aspire，但由于 Aspire 是一个多语言平台，因此去掉了 .Net。

这个代码优先的编排平台用于构建、调试和部署分布式应用程序，例如云原生应用或 [微服务](https://thenewstack.io/introduction-to-microservices/)。

[Aspire 提供了一套精选的组件和工具](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/)，包括一个开发者仪表板。其目标是简化 [云原生应用程序](https://thenewstack.io/the-api-gateway-and-the-future-of-cloud-native-applications/) 的启动、构建和运行。

Pine 解释了如何在三种不同场景下运行 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 代码，包括 [Node](https://thenewstack.io/node-js-24-your-next-big-frontend-upgrade/) 和 [Vite](https://thenewstack.io/how-vite-became-the-backbone-of-modern-frontend-frameworks/)。

## Rust 1.93.0 升级 musl C 库

Rust 本周发布了 1.93.0 版本。主要新闻是它升级了在构建某些 Linux 应用时使用的 musl C 库版本。

根据 [Rust 1.93.0 版本博客](https://blog.rust-lang.org/2026/01/22/Rust-1.93.0/) 的说法，这“应该能让进行网络操作的便携式 Linux 二进制文件更可靠，尤其是在面对大型 [DNS 记录](https://www.cloudflare.com/learning/dns/dns-records/) 和递归名称服务器时”。

这意味着应用程序在 [Kubernetes](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/)、[Docker](https://thenewstack.io/dockers-sets-free-the-hardened-container-images/) 或 DNS 记录庞大复杂的复杂云环境中运行时将更加稳定。

如果您通过 [rustup](https://rust-lang.org/tools/install/) 安装了旧版本的 Rust，可以使用以下命令更新到 1.93.0：

`$ rustup update stable`

## 一场针对实用应用程序的黑客马拉松

您是否正在开发一个特别实用且是实际应用程序——而不仅仅是演示——的副项目？

如果是，您可能需要将其提交到 [实用性证明黑客马拉松](https://hackernoon.com/proof-of-usefulness-hackathon-win-%24100k-from-bright-data-neo4j-algolia-storyblok-and-hackernoon)，该活动每月举行一次，直至 6 月 5 日。根据 HackerNoon 的说法，这是一场“全球开发者竞赛，只奖励一件事：真实世界的实用性”。

这场黑客马拉松的有趣之处在于，它将在未来六个月内每月为 40 多名获奖者提供奖励和认可。每两个月，将为顶尖初创公司提供主要的软件奖项周期。每位参与者还将获得价值 1,500 美元的库存。

该黑客马拉松对个人开发者和新兴初创公司开放。它提供了免费工具，帮助您构建和推广有意义的东西。

虽然欢迎任何技术，但更大的奖项将颁发给使用赞助商技术的人工智能和 [机器学习 (ML)](https://thenewstack.io/ditch-python-5-javascript-libraries-for-machine-learning/) 项目。本周，该网站解释了 [如何参加活动](https://hackernoon.com/how-to-enter-the-proof-of-usefulness-pou-hackathon)，这有些繁琐。

该活动由 HackerNoon、[Bright Data](https://brightdata.com/?utm_content=inline+mention)、[Neo4j](https://thenewstack.io/try-a-neo4j-graph-database-right-here-right-now/)、[Storyblok](https://thenewstack.io/frontend-or-backend-where-full-stack-devs-spend-their-time/) 和 [Algolia](https://thenewstack.io/algolia-takes-app-search-new-places/) 赞助。

## 以您的方式基准测试 AI 模型

[Kaggle](https://thenewstack.io/where-do-data-practitioners-prefer-to-collaborate-github/) 是一个 [Google](https://cloud.google.com/?utm_content=inline+mention) 旗下的在线 AI 开发者社区，最近推出了一项新 [功能，允许您创建自定义基准](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-community-benchmarks/) 来评估 AI 模型。

该功能在其 Benchmarks 平台中被称为 [社区基准](https://www.kaggle.com/benchmarks?type=community)。它可用于设计、运行和共享自定义 AI 模型基准。

以下是它为何重要：AI 发展如此迅速，以至于评估模型性能变得困难，Kaggle 软件工程师 Michael Aaron 和 Kaggle 产品负责人 Megan Risdal 在一篇 [博客文章](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-community-benchmarks/) 中写道。

Aaron 和 Risdal 写道：“不久前，一个静态数据集上的单一准确性得分足以确定模型质量。但今天，随着 LLM 演变为协作、编写代码和使用工具的推理代理，那些静态指标和简单评估已不再足够。”

社区基准的特点包括：

* **自定义任务构建** 允许开发者使用新的 [kaggle-benchmarks SDK](https://github.com/Kaggle/kaggle-benchmarks) 定义用于代码执行、工具使用和多轮对话的任务。
* **最先进的模型访问** 可以在配额内免费对 Google、Anthropic 和 DeepSeek 的模型运行自定义基准。
* **可审计的再现性** 意味着该框架捕获完整的输入、输出和模型交互，用可验证的数据取代了轶事测试。
* **动态排行榜** 让开发者可以将多个任务组合成一个基准，以生成一系列领先模型之间的比较排名。

[Kaggle Benchmarks 仓库](https://github.com/Kaggle/kaggle-benchmarks) 中有 [预构建任务的示例](https://github.com/Kaggle/kaggle-benchbacks/tree/ci/documentation/examples)。