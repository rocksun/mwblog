<!--
title: Andrej Karpathy、Google 和 Garry Tan 一致认为 Markdown 是答案，但他们解决的不是同一个问题
cover: https://cdn.thenewstack.io/media/2026/07/61acf43c-getty-images-87hn3jt9vuo-unsplash-scaled.jpg
summary: 本文指出 Andrej Karpathy、Google 与 Garry Tan 虽然出发点不同，却共同选择 Markdown 作为 AI 代理的知识库格式。这标志着竞争壁垒已从 AI 模型转移到企业长期积累的 Markdown 数据资产上，实现了知识的跨模型可移植性。
-->

本文指出 Andrej Karpathy、Google 与 Garry Tan 虽然出发点不同，却共同选择 Markdown 作为 AI 代理的知识库格式。这标志着竞争壁垒已从 AI 模型转移到企业长期积累的 Markdown 数据资产上，实现了知识的跨模型可移植性。

> 译自：[Andrej Karpathy, Google and Garry Tan agree Markdown is the answer, but they're not solving the same problem](https://thenewstack.io/markdown-agent-memory-moat/)
> 
> 作者：Janakiram MSV

今年 4 月，Andrej Karpathy 发布了一个名为“[LLM Wiki”](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)的 GitHub gist 文件，这是一份简短的文本文档，旨在帮助人们使用 LLM 构建个人知识库。其前提是：AI 代理会将它所知的内容保存为链接的 Markdown 文件，以便它可以读取和重写这些文件。因为语言模型不会厌倦维护交叉引用，并且可以在一次处理中触及 15 个文件。这份文档只有几千字，并没有绑定任何产品。

两个月后，Google 将这种直觉变成了一个名为[开放知识格式 (Open Knowledge Format)](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) 的已发布标准。OKF 将组织知识、指标、表格和运行手册打包为纯 Markdown，任何代理无需专有账户即可读取。Google 很谨慎地将其称为 `v0.1`——这是一个起点，而非一个完成的标准。

Y Combinator 的总裁 [Garry Tan](https://www.ycombinator.com/people/garry-tan) 在另一个轨道上率先实现了这一目标。他的 [gstack](https://github.com/garrytan/gstack) 是一个获得 MIT 许可的 Claude Code 设置，在几周内获得了超过 66,000 个 GitHub star，它包含 23 个专业角色，每个角色都是一个 Markdown 文件。没有运行时；没有代码；只有在 10 个不同的编程代理之间运行的散文。

## Markdown 已成为代理读取和写入的基板

三种方法，三种不同的需求，一种共同的解决方案。Karpathy 追求代理记忆，Google 瞄准了 BigQuery 代理中的企业上下文，而 Tan 想要一种从终端召唤工程团队的方法。这三者都转向了同一个基本资源：一个用 git 进行版本控制的 Markdown 文件文件夹。

开发者早已建立了这种做法。[CLAUDE.md](https://code.claude.com/docs/en/memory#claude-md-files) 和 [AGENTS.md](https://agents.md/) 作为代理加载的初始文件，存在于数百万个仓库中。OKF 和 gstack 是这种约定的进化形式——一个专注于代理知道什么，另一个专注于它的行为方式。

这是与代理知识挂钩的 Git 和 JSON 剧本。能够存活下来的格式，是你无需做任何改变即可开始使用的格式。你只需 cat 该文件、克隆仓库，任何你已经在使用的工具都可以解析它。MCP 仍然是代理连接的接口。而 Markdown 正在成为承载内容的核心格式。

## 锁定效应已从模型转移到文件

这里需要观察的重要因素是竞争优势，而非技术细节。两年来，人们普遍认为拥有最好的模型意味着控制开发者。

这种观点现在正在转变。用 GLM 或 Codex 替换 Claude，gstack 仍然可以运行，因为核心智能在进化，但文档没有。

> 护城河正在从模型转移到团队拥有并随时间积累的 Markdown 上。

护城河正在从模型转移到团队拥有并随时间积累的 Markdown 上。一家公司的 OKF 包，包括其运行手册、指标定义和架构决策，设计上就是可在云、模型和框架之间移植的。

这种可移植性正是供应商中立格式存在的原因，也是 Google 的 OKF 值得密切关注的原因。

> 如果没有人为它开发消费者，它就只是 Google 在一个周五发布的一个好想法而已。

我最有可能犯错的地方在于持久性。宣布 Markdown 标准很容易，但要使其可靠却很难。OKF 仅仅是一个带有参考实现的 0.1 草案，而不是一个完整的生态系统。如果没有人为它开发消费者，它就只是 Google 在一个平淡的周五发布的一个好想法而已。

方向仍然由在同一季度内针对同一文件格式的三次单独押注决定。你的下一个代理很可能会从 Markdown 文件夹中解读其上下文，而该文件夹的创建者现在拥有了一个模型供应商无法轻易复制的优势。