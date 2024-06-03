
<!--
title: Codestral：让 AI 驱动的编码更接近大众
cover: https://cdn.thenewstack.io/media/2024/05/be3c5c01-nicholas-green-npz8akkumdi-unsplash-1.jpg
-->

Codestral 被视为迈向赋予每个人代码生成和理解能力的垫脚石，这是在人工智能创建的应用程序代码工具领域长期竞争中的最新一轮攻击。

> 译自 [Codestral: A Step Closer to AI-Driven Coding for the Masses](https://thenewstack.io/codestral-a-step-closer-to-ai-driven-coding-for-the-masses/)，作者 Darryl K Taft。

[Mistral AI](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) 发布了 [Codestral](https://mistral.ai/news/codestral/)，这是该公司首个专为代码生成设计的代码模型。

Codestral 是一款开放权重生成式 AI (GenAI) 模型，专为代码生成任务设计。根据国家电信和信息管理局的说法，开放权重模型允许开发人员在以前的工作基础上进行构建和调整，从而扩大 AI 工具对小公司的可用性。

Codestral 在 80 多种编程语言上进行训练，包括一些最流行的语言，例如：

- [Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/)
- [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/)
- C
- [C++](https://thenewstack.io/c-23-standard-wont-have-a-key-parallelism-feature/)
- [JavaScript](https://thenewstack.io/javascript/)
- [Bash](https://thenewstack.io/simplify-linux-and-docker-command-lines-with-bash-completion/)

## Codestral 功能

Mistral 展示了测试结果，表明 Codestral 在 Python、[SQL](https://thenewstack.io/how-to-write-sql-queries/) 和其他语言的各种基准测试中优于其他模型。它可以完成编码功能、编写测试，并使用填充中间机制完成任何部分代码。该公司表示，与 Codestral 交互将有助于提升开发人员的编码能力，并降低错误和缺陷的风险。

Codestral 在 [Swift](https://thenewstack.io/apple-highlights-swift-enhancements-at-wwdc22/) 和 [Fortran](https://thenewstack.io/how-john-backus-fortran-beat-machine-codes-priesthood/) 等更具体的编程语言上也表现出色。这种广泛的语言基础确保 Codestral 可以协助开发人员在各种编码环境和项目中工作。

[Tabnine](https://thenewstack.io/code-stays-behind-firewall-with-copilot-alternative-tabnine/) 的研发主管 [Meital Zilberstein](https://il.linkedin.com/in/meitalbensinai) 在一份声明中表示：“作为创建首款以开发者为中心的 [GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 工具的公司的一名研究员，我很荣幸将 Mistral 的新代码模型集成到我们的聊天产品中。我对其性能印象深刻。”“尽管其体积相对较小，但它提供的结果与我们向客户提供的更大模型不相上下。我们测试了几项关键功能，包括代码生成、测试生成、文档、入职流程等。在每种情况下，该模型都超出了我们的预期。”

Codestral 可在 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 上下载，并且可以通过专用端点 (codestral.mistral.ai) 或常规 API 端点 (api.mistral.ai) 使用。

该模型与 [LlamaIndex](https://thenewstack.io/llamaindex-and-the-new-world-of-llm-orchestration-frameworks/) 和 [LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) 等应用程序框架以及 [Continue.dev](https://www.continue.dev/) 和 [Tabnine](https://www.tabnine.com/) 的 [VS Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/) 和 [JetBrains](https://thenewstack.io/jetbrains-launches-ai-code-completion-on-local-machines/) 的 IDE 插件集成。

Continue.dev 的首席技术官兼联合创始人 [Nate Sesti](https://www.linkedin.com/in/natesesti/) 在一份声明中表示：“以前从未出现过速度和质量如此之高的公共自动完成模型，这将成为全球开发人员的变革。”

## 新的非生产许可证

Codestral 根据该公司新推出的非生产许可证进行授权，以平衡开放性和业务增长。

Mistral AI 团队在博客文章中写道：“AI 的开放性受到威胁，围绕 AI 的争论被用来巩固这个高度竞争的行业中现有参与者的地位。”“我们已经发声捍卫 AI 的开放性，并将不懈地继续这样做。”

该团队还写道：“因此，我们很高兴看到我们的社区和合作伙伴使用我们的模型构建高利润产品。虽然这对最终用户来说是个好消息，但有时无法为我们的成功、研究和独立做出贡献。”“这就是我们推出 [Mistral AI 非生产许可证 (MNPL)](https://mistral.ai/licenses/MNPL-0.1.md) 的原因。此许可证允许开发人员将我们的技术用于非商业目的并支持研究工作。它确保那些基于我们的工作开展业务的人以对所有各方公平且可持续的方式开展业务。”

然而，Mistral 将继续以 Apache 2.0 作为模型和代码，因为该公司逐步整合了在 Apache 2.0 和 MNPL 下发布的两类产品。

## 大众代码生成垫脚石

与此同时，Mistral AI 团队表示，Codestral 被视为赋予每个人代码生成和理解能力的垫脚石。

[Jason Bloomberg](https://nl.linkedin.com/in/jasonbloomberg) 表示，Codestral 是在人工智能创建的应用程序代码工具的长期竞争中发出的最新号角，他是 [Intellyx](https://intellyx.com/) 的分析师。他说，如今，此类工具掌握在专业开发人员手中，他们可以正确提示人工智能，然后评估结果代码的质量。

然而，彭博社告诉 The New Stack，“将如此强大的工具交到非技术用户手中，却不会有这些优势，可能会导致质量低劣的代码或可能具有内在质量但仍与其业务目标不符的代码。”“从长远来看，人工智能生成的代码表面上会减少对专业开发人员的需求，导致远离该职业，从而丧失评估人工智能生成代码的整体能力——这对每个人都是不利的。”

至少还有一位行业分析师表示同意。

“又一个 AI 模型，今天是 Mistral 和 Codestral。用于编码的新 AI 模型的创新速度如此之快，以至于想要使用它们的开发人员将花费所有时间来切换到当前最佳模型。”

[Holger Mueller](https://www.linkedin.com/in/holgermueller/) 是 [Constellation Research](https://www.constellationr.com/) 的分析师，他告诉 The New Stack，“但这就是为什么所有大型 AI 供应商都需要拥有一个——利用一次使用模型的粘性，以继续使用它。所有 AI 供应商都在寻找的奖品是 [低代码/无代码](https://thenewstack.io/infrastructure-as-code-goes-low-code-no-code/) 空间——谁以足够好的方式解决了代码生成问题，谁将开启下一个业务自动化时代。”
