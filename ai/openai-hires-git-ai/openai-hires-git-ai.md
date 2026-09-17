<!--
title: “使命相同，舞台更大”：OpenAI聘请Git AI创始人以验证Codex的投资回报率
cover: https://cdn.thenewstack.io/media/2026/09/00c8f2e0-manaa-graphic-yzdokvgnfhm-unsplash-scaled.jpg
summary: OpenAI聘请了开源工具Git AI的创始人Aidan Cunniffe与Sasha Varlamov。该团队将加入Codex部门，利用其技术帮助企业量化AI编程代理的性能及投资回报率，实现代码生成过程的透明化管理。
-->

OpenAI聘请了开源工具Git AI的创始人Aidan Cunniffe与Sasha Varlamov。该团队将加入Codex部门，利用其技术帮助企业量化AI编程代理的性能及投资回报率，实现代码生成过程的透明化管理。

> 译自：["Same mission, bigger stage": OpenAI hires Git AI founders to help Codex prove its ROI](https://thenewstack.io/openai-hires-git-ai/)
> 
> 作者：Paul Sawers

**OpenAI 聘请了** [Git AI](https://usegitai.com/) 的创始人，这是一款[开源工具](https://github.com/git-ai-project/)，用于跟踪 AI 编写的代码量，并衡量编程代理的性能和成本。

上周五深夜，[Aidan Cunniffe](https://www.linkedin.com/in/acunniffe/) 在 LinkedIn 上发文表示，他和他的 Git AI 联合创始人 [Sasha Varlamov](https://www.linkedin.com/in/sashavarlamov/) 将加入 OpenAI 的 Codex 团队。他们将在该团队工作，致力于为企业提供有关编程代理如何运行以及它们所产生回报的更佳数据。

“使命相同，舞台更大，” Cunniffe [写道](https://www.linkedin.com/feed/update/urn:li:activity:7504340859455246336/)。

虽然整合计划的细节尚不清楚，但 OpenAI 的技术人员 [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/)（负责 ChatGPT 和 Codex 工作）[在 X 上证实](https://x.com/thsottiaux/status/2098569976143806918)，公司希望利用 Git AI 的技术来帮助企业了解 Codex 的影响。

“我们将让企业更容易地看到 Codex 在为个人和团队解决问题时发挥的作用，” Sottiaux 写道。

在周五宣布该交易的另一篇[博客文章](https://usegitai.com/blog/git-ai-is-joining-openai)中，Cunniffe 指出，此次合作反映了双方在衡量 AI 编程工具性能和价值方面的共同关注点。

> “OpenAI 与我们有着相同的信念：用户应该掌握相关数据，以比较模型性能并了解他们所花费的每一个 Token 的投资回报率。”

他写道：“OpenAI 与我们有着相同的信念：用户应该掌握相关数据，以比较模型性能并了解他们所花费的每一个 Token 的投资回报率。”

## 跟踪 AI 生成的代码

对于外行来说，Git AI 是一个开源的 Git 扩展，用于跟踪 AI 生成的代码。每一行代码都链接到生成它的代理、模型和提示词，即使在代码被提交、合并或重写（rebased）后，也能保留变更背后的上下文。

从更广泛的意义上讲，它旨在帮助团队查看有多少 AI 生成的代码最终进入了生产环境、它们被重构的频率，以及在哪些地方消耗了时间和 Token。这些数据随后可用于比较编程代理和模型，并评估在它们身上投入的资金是否产生了有用的输出。

该工具已经支持多种编程代理，包括 OpenAI Codex、Anthropic 的 Claude Code、Cursor 和 Google 的 Gemini CLI，以及包括 Codex Cloud、Claude Web、Cursor Agent 和 Devin 在内的后台代理。

安装后，支持的代理会自动将它们的编辑报告给 Git AI。对于开发者来说，其核心卖点基本上是：“只需提示并提交”——他们可以像往常一样继续使用他们的编程工具和 Git。

![Git AI](https://cdn.thenewstack.io/media/2026/09/765c5718-giffy.gif)

*Git AI*

Git AI 可以展示人类编写代码与 AI 编写代码之间的分配比例，并将每一行代码追溯到生成它的代理。

## 目前为止的故事

事实上，Cunniffe 此前已有过类似经历。他于 2018 年创立了开发者工具初创公司 Optic，该公司围绕 API 开发构建开源工具，后来[在 2024 年被 Atlassian 收购](https://www.atlassian.com/blog/company-news/optic-acquisition)。随后他加入了 Atlassian，担任首席产品经理，负责开发者工具的上市工作。

Git AI 项目始于 Cunniffe 在 Atlassian 任职期间。他和 Varlamov 于 2025 年夏天开始将此作为副业项目，最初试图回答一个看似简单的问题：他们的代码中到底有多少是由 AI 编写的，以及这些代码后续发生了什么？

到 [11 月发布第一个主要版本时](https://usegitai.com/blog/introducing-git-ai)，Cunniffe 公开将 Git AI 描述为一个已经发展成更大规模的“周末项目”。随后，他在 2026 年 1 月离开 Atlassian，将 Git AI 变成了一家公司，围绕该开源项目建立了一个商业业务。

现在，不到一年后，Cunniffe 和 Varlamov 加入了 OpenAI。目前尚不清楚这对 Git AI 作为商业企业意味着什么，但随着两位创始人加入 OpenAI，该独立业务可能会被逐步关闭，而开源项目则会继续存在。

*The New Stack* 已联系 OpenAI，并将在收到回复后更新此报道。

Cunniffe 表示，OpenAI 将继续支持该开源项目。

“我们将继续投资于开源，同时为企业提供他们构建高效软件工厂所需的数据，” 他写道。

这种跨模型独立性在 OpenAI 的管理下最终将如何保持，将是值得关注的有趣事项之一。