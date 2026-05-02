<!--
title: Cursor 的 600 亿美元豪赌：胜负手不在模型，而在 Harness 调度底座
cover: https://cdn.thenewstack.io/media/2026/04/c29038b1-naila-conita-w84kgrt8fx0-unsplash-scaled.jpg
summary: 本文探讨了 Cursor 从 IDE 向 Agent 调度底座（Harness）的战略转型。作者认为 AI 模型正趋于商品化，真正的竞争力在于如何编排模型。SpaceX 的收购意向进一步验证了该层的价值，建议开发者关注工具的灵活性。
-->

本文探讨了 Cursor 从 IDE 向 Agent 调度底座（Harness）的战略转型。作者认为 AI 模型正趋于商品化，真正的竞争力在于如何编排模型。SpaceX 的收购意向进一步验证了该层的价值，建议开发者关注工具的灵活性。

> 译自：[Cursor's $60 billion bet is on the harness, not the model](https://thenewstack.io/cursor-sdk-harness/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 发展动态，解释它们对于将这项技术投入工作的个人和组织的意义。核心论点很简单：学会使用 AI 的劳动者将定义其行业的下一个时代，而本通讯旨在帮助你成为其中一员。*

---

在过去的两个月里，Cursor 一直在以不同的方式向业界传达一个信息：它不仅仅是一家 IDE 公司。周三，它发布了 [Cursor SDK](https://cursor.com/blog/typescript-sdk)，周四，Cursor 的 Harness 团队[发表了一篇关于 Agent Harness 的长文](https://cursor.com/blog/continually-improving-our-agent-harness)——这些动作共同将多年的内部编排工作打包，并交到了每一位开发者手中。今年 2 月，CEO Michael Truell [发表了一篇文章](https://cursor.com/blog/third-era)，宣布这是 AI 软件开发的“第三纪元”。就在上周，Cursor 宣布了[与 SpaceX 的一项疯狂合作](https://cursor.com/blog/spacex-model-training)，将在 xAI 的 Colossus 超级计算机上训练其下一代专有 Composer 模型。

> Cursor 认为 AI 模型正在成为一种商品，而赢得下一个十年的产品将是围绕它的 Harness（调度底座）。

综合来看，这一信号非常明确：Cursor 认为 AI 模型正在成为一种商品，而赢得下一个十年的产品将是围绕它的 Harness。最有力的确认完全来自 Cursor 之外。谷歌本周告诉 *The New Stack*，它并不关心开发者使用哪种编程工具，无论是 Gemini、Claude Code 还是 Cursor。

## Cursor 正在超越单纯的 IDE 公司定位

数月来，零散的拼图一直在逐渐归位：本周，Cursor 发布了一个 SDK，使这一转变变得明确。当 Cursor 3 在[本月早些时候](https://thenewstack.io/cursor-3-demotes-ide/)发布时，Jani MSV 在 *The New Stack* 上用直白的词汇进行了报道：IDE 现在只是一个后备方案。Agent 启动专用的云端虚拟机（VM），工作数小时，并返回日志、视频录制和实时预览。根据 Michael Truell 的“第三纪元”博文，Cursor 的 Agent 使用量在去年增长了 15 倍以上。

十二个月前，Cursor 的 Tab 自动补全用户数是 Agent 用户数的 2.5 倍。今天，它的 Agent 用户数是 Tab 用户数的 2 倍。在 Cursor 内部，Michael Truell 表示，超过三分之一的内部拉取请求（PR）是由在云端虚拟机中运行的 Agent 创建的。他预计在一年内，“绝大多数”开发工作都将呈现这种形式。

如果 Michael Truell 是正确的（我认为他是对的），IDE 的重要性将会降低，而 Harness 将变得更加重要。这就是为什么在 4 月 29 日，Cursor [发布了公开测试版的 Cursor SDK](https://cursor.com/blog/typescript-sdk)。这是一个 Typescript 软件包（ `npm install @cursor/sdk` ），让开发者可以直接在 Cursor 的 Harness 上构建 Agent，它与模型无关，可以部署在本地或 Cursor Cloud 的专用虚拟机上。

该 Harness 具备代码库索引、MCP 服务支持、子 Agent 以及可观测性钩子。这使 Cursor 进入了与 OpenAI 的 Agents SDK 和 Anthropic 的 Claude Agent SDK 相同的赛道，但其 Harness 已经在其自身用户中进行了大规模应用。Cursor 将 Composer 2 定位为廉价的默认方案——价格为每百万输入 token 0.50 美元，而 Claude Opus 4.6 为每百万输入 token 5 美元——并声称其基准测试性能具有竞争力。但该 SDK 支持你想要的任何模型。

SpaceX 的合作伙伴关系在此基础上落地。Cursor 的博客指出，公司一直受到“算力瓶颈”的限制，现在将“利用 xAI 的 Colossus 基础设施大幅提升我们模型的智能水平”。当 [*Bloomberg*](https://www.bloomberg.com/news/articles/2026-04-21/spacex-says-has-agreement-to-acquire-cursor-for-60-billion) 和 *[TechCrunch](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/)* 报道称，SpaceX 表示将向 Cursor 支付 100 亿美元用于两家公司的合作，或者在今年晚些时候以 600 亿美元的价格直接收购 Cursor 时，这一伙伴关系变得更加有趣。Musk 可能不只是为了买下 Composer 2 的权重。xAI 已经拥有了 Grok 和 Colossus。更具战略意义的资产是 Cursor 的 Harness 及其连接每天实际使用这些工具的开发者的纽带。

## 什么是 Harness，以及为什么它突然成为了最有价值的 AI 层

Harness 是将原始的前沿模型（Claude、GPT、Gemini、Composer）转化为可以在你的代码库中实际执行工作的软件封装器。模型是大脑；Harness 则根据其指令行动，并向大脑提供反馈。

Harness 负责选择模型可以看到哪些文件、文档、提交记录和工具输出。这就是上下文管理，Cursor 的 Harness 团队写道，做好这件事是一个长期的工程项目。Harness 调用工具：终端、linter、MCP 服务器和内部 API。它生成子 Agent，甚至使用不同的模型和不同的提示词来更好地并行规划、编辑或调试。它运行可观测性钩子，并执行安全边界以实现更好的访问控制。它将所有这些缝合进一个循环中，模型在其中不断迭代，直到任务完成。

Harness 的工作看起来像是平淡无奇的工程。Cursor 的团队写道，他们花费“数周”时间逐个模型地调整 Harness，因为每个模型都有不同的优势和怪癖。他们警告“上下文腐烂（context rot）”——即一个错误的工具调用可能会毒害 Agent 随后做出的每一个决定。他们对实际使用情况进行持续的 A/B 测试，观察一个他们称之为“保留率（Keep Rate）”的指标，该指标衡量 Agent 编写的代码中有多少最终留在了提交记录中。这些工作都不会成为基准测试的头条新闻，但它们决定了一个 Agent 究竟是修复了一个工单，还是交付了损坏的代码。

这在软件领域之外也有重要意义：同样的形态将复制到最终部署 Agent 的每个领域。模型是理解法律合同、病人图表或财务模型的部分；而 Harness 是为其提供正确上下文、正确工具、正确边界和正确监督的部分。谁拥有了你所在领域的 Harness 层，谁就拥有了产品。

## 谷歌的“我们不在乎”证明了模型已成为商品

我所见过的来自超大规模云服务商（Hyperscaler）最坦率的言论来自 Google Cloud 的首席宣传官 Richard Seroter。正如 Frederic Lardinois 本周在 *The New Stack* 上[所写的《谷歌并不在乎》](https://thenewstack.io/google-doesnt-care/)，Richard Seroter 说：“现在的开发者忠诚度为零。”谷歌的立场是，开发者使用 Cursor、Copilot、Code 还是 Claude Code 并不重要。

> 谷歌的立场是，开发者使用 Cursor、Copilot、Code 还是 Claude Code 并不重要。

六个月前，谷歌还竞相将 Gemini 植入 VS Code。现在，它显然很放心让 Harness 供应商去竞争，因为谷歌的护城河——搜索、Android、云以及支撑整个技术栈的算力——处于与 IDE 完全不同的层级。当一家拥有前沿模型公司的开发者能够从容使用别人的界面时，它至少承认了界面和基础设施层可能比模型忠诚度更重要。这是我见过的对模型商品化最清晰的表达，而且是由最了解情况的公司大声说出来的。

不仅仅是谷歌。两周前，Jani [在我们的网站上写道](https://thenewstack.io/ai-agent-harness-pricing-split/)，Anthropic、OpenAI、谷歌和微软都同意 Harness 才是产品——他们只是在收费标准上存在分歧。Anthropic 的托管 Agent 定价在模型使用费之上增加了托管 Agent 运行费。Cursor 的 SDK 在发布时对 Composer 2 采取了按 token 计费的方式，其费率仅为 Claude Opus 的一小部分。

模式很清晰：模型供应商正面临着让智能变得更廉价、更具互换性的压力，而 Harness 供应商则在为编排、可观测性以及真正让 Agent 产生生产力的集成工作收费。Anthropic 的企业级 Harness 和 Cursor 的 SDK 都在押注同一个未来：廉价且可互换的智能，以及专有的编排能力。

这对我们其余的人意味着什么，取决于你所处的位置。如果你是一名开发者，你日常使用的模型将不断更迭，而你的 Harness 会变得越来越聪明。少担心哪款模型是本月的“大红人”，多关注你的工具是否设计得能够优雅地切换模型。

如果你是一名 CIO，你的 AI 供应商锁定不应该发生在模型层——它应该发生在 Harness 层，你应该向供应商提出尖锐的问题，了解他们的 Harness 如何处理上下文、工具、可观测性以及模型切换。

如果你在工程领域之外工作，也不要掉以轻心。同样的架构——底层是商品化的智能，顶层是专有的 Harness——即将进入法律、金融、运营、设计和编辑工作。构建这些 Harness 的公司将主导工作的完成方式。