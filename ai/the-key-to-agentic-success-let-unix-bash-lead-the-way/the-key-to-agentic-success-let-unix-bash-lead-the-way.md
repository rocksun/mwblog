<!--
title: 智能体成功秘诀？BASH就够了
cover: https://cdn.thenewstack.io/media/2026/01/5180edc0-sofia-gazarian-ikhl2gz1sqw-unsplash-scaled.jpg
summary: AI代理架构应化繁为简，回归Unix哲学。Vercel和Anthropic实践显示，赋予LLM基础BASH工具而非复杂预设，能显著提升效率、成功率，减少资源消耗，让模型自主思考。
-->

AI代理架构应化繁为简，回归Unix哲学。Vercel和Anthropic实践显示，赋予LLM基础BASH工具而非复杂预设，能显著提升效率、成功率，减少资源消耗，让模型自主思考。

> 译自：[The Key to Agentic Success? BASH Is All You Need](https://thenewstack.io/the-key-to-agentic-success-let-unix-bash-lead-the-way/)
> 
> 作者：Joab Jackson

代理构建者发现，有时代理完成工作最简单的方法是给它一些Unix工具，然后“让它自己发挥”。

Vercel最近的一个项目发现，剥离大量元数据，转而给模型一个BASH shell并允许其访问数据，反而产生了卓越的结果。

另一组开源开发者发现，一个简单的BASH while循环和一些独立的时间就足以执行复杂的任务。

“模型越来越智能，上下文窗口也越来越大，所以也许最好的代理架构几乎就是没有架构，”Vercel软件总监Andrew Qu写道。“如果BASH就是你所需要的一切呢？”

## 让LLM来思考

Vercel为员工[构建](https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval)了一个文件代理，用于从其[内部数据存储](https://thenewstack.io/kepler-openais-internal-agent-platform-for-synthesizing-data/)中获取答案。这个名为d0的代理可以回答数据团队通常会遇到的问题：

![Screenshot](https://cdn.thenewstack.io/media/2026/01/0c3a12dc-vercel-d0-ai.jpg)

Vercel的d0正在工作，回答问题。

为此，d0必须将自然语言查询转换为针对各种YAML、Markdown和JSON文件的SQL查询。

“当d0运行良好时，它能使公司内部的数据访问民主化。当它出现故障时，人们就会失去信任，转而回到Slack上向分析师求助，”Andrew Qu在[一篇关于d0的十二月博客文章](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)中写道。

当公司启动这个项目时，它投入资源确保代理拥有所需的所有支持，包括提供专用工具、大量的提示工程、[大量元数据](https://thenewstack.io/how-canva-keeps-its-image-metadata-fresh/)和充足的上下文管理。

“它……有点用。但它很脆弱，速度慢，并且需要持续维护，”Andrew Qu写道。

因此，工程团队尝试了相反的方法：没有给代理配备大量上下文和工具，而是将其简化为单一功能，即执行[BASH命令](https://thenewstack.io/how-to-create-your-first-linux-bash-script/)的能力。它获得了直接访问文件的权限，并可以使用`grep`、`cat`、`ls`等命令查询文件。

公司发现，d0立即变得更容易管理，使用的资源更少，并且准确率更高。

“这一切都通过‘少做’来实现，”Andrew Qu写道。

## Unix哲学

也许Andrew Qu和团队所学到的并非那么反直觉。

[Unix哲学](https://cscie2x.dce.harvard.edu/hw/ch01s06.html)是一种简洁的哲学：构建复杂系统的最佳方式是通过基本组件的模块化。

每个工具都应该只做一件事，并把它做好，而且工具应该易于组合成更大的工作流。它们都应该是基于文本的，因为文本是通用的接口。

[BASH](https://thenewstack.io/how-to-create-your-first-linux-bash-script/) (Bourne Again SHell)是这种方法的接口，允许用户使用简单的管道命令将程序链接起来，将一个程序的输出作为另一个程序的输入。

通过这种简单的哲学，Unix（及其分支Linux）几十年来一直用于管理服务器及其运行的复杂工作负载；也许它也能管理AI工作。

## 更少输入带来更好的结果

Vercel的d0v2移除了代理所需80%的辅助信息。

这个名为[bash-tool](https://www.npmjs.com/package/bash-tool)的BASH引擎作为一个NPM包运行，并于本周早些时候[开源](https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval)。

它通过[AI SDK](https://ai-sdk.dev/)在Claude Opus 4.5上运行，该SDK获得了一个[Vercel Sandbox](https://vercel.com/sandbox)用于上下文探索。请求处理和可观测性通过[Vercel Gateway](https://vercel.com/ai-gateway)完成，而Next.js API路由是使用[Vercel Slack Bolt](https://vercel.com/academy/slack-agents)构建的。

数据被索引到一个立方体语义层中，这是一个中间件软件，它聚合数据源，使它们可以通过单个API访问，或者在这种情况下，通过SQL查询访问。

考虑到立方体的单一工作是对不同数据源进行语义转换，它也符合Unix哲学。

d0不需要很多额外的上下文，因为语义层通过维度定义、度量计算和连接关系已经提供了所需的大部分数据。

“我们过去在构建工具来总结已经清晰可见的内容。Claude只需要直接读取它，”Andrew Qu写道。

下表总结了从旧设计到新设计的改进：

| 指标 | 高级（旧） | 文件系统（新） | 变化 |
| --- | --- | --- | --- |
| 平均执行时间 | 274.8秒 | 77.4秒 | 快3.5倍 |
| 成功率 | 4/5 (80%) | 5/5 (100%) | +20% |
| 平均token用量 | 约102k token | 约61k token | 减少37% token |
| 平均步骤数 | 约12步 | 约7步 | 减少42%步骤 |

## 回顾

回想起来，Andrew Qu的团队过度设计了代理提示。他们是在重复造轮子。

“`grep`已经有50年历史，但它仍然能完全满足我们的需求。我们过去在为Unix已经解决的问题构建定制工具，”Andrew Qu写道。

模型很智能，并且[一直在变得更智能](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning/)。为它们提供更多工具可能是有益的，但有时也可能造成限制。有时模型可以做出更好的选择。它们的进步速度是你的工具选择无法匹敌的。

“我们过去限制了推理，因为我们不相信模型能够推理。对于Opus 4.5来说，这种限制成了一种负担。当我们不再替模型做选择时，它会做出更好的选择，”Andrew Qu写道。

Vercel首席执行官Guillermo Rauch在X（此前名为Twitter）上[阐述了这一教训](https://x.com/rauchg/status/2008962101784830158)，指出要回归理解[Unix基础知识](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/)，例如文件系统、shell、进程和命令行。

他写道：“不要与模型对抗，拥抱它们所调优的抽象。BASH就是你所需要的一切。”

## “失败即数据”

一家显然与这种哲学保持一致的AI公司正是[Anthropic](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)本身，它是[Claude](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/)系列AI模型的制造商。

最近，该公司发布了一个名为[“Ralph Wiggum”](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)的插件，它基本上是一个BASH脚本，只有一个操作：一个do/while循环。

文档解释说，这个想法是给AI代理一个单独的提示文件，并让它“迭代改进其工作直到完成”。

无需调整提示。相反，所有工作都写入文件并捕获在git历史日志中。Claude通过审查它在文件中的过去工作来改进结果，并持续修改工作直到达到既定目标。

Ralph Wiggum以《辛普森一家》中一个笨拙的孩子命名，其想法是[消除](https://venturebeat.com/technology/how-ralph-wiggum-went-from-the-simpsons-to-the-biggest-name-in-ai-right-now?ref=ghuntley.com)每次大型语言模型（LLM）尝试任务时都需要有人审查其工作的必要性。相反，让LLM自己完成工作，并学会如何自我提升。

“失败就是数据，”其[创建者](https://ghuntley.com/ralph/)、开源开发者Geoffrey Huntley解释道。

![Screenshot](https://cdn.thenewstack.io/media/2026/01/23897145-im-in-danger-ralph-1.gif)

*版权所有：《辛普森一家》。*

尽管采用了简单的暴力方法，Wiggum以最佳的Unix风格，取得了一些显著的成果。

在一次黑客马拉松中，Wiggum技术被用于将一个[网络代理工具](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md)从Python移植到TypeScript。经过一夜运行，研究人员第二天发现了一千多次提交、六个移植的代码库和一个几乎完全功能的程序。

换句话说，据Anthropic称，它以297美元的API成本完成了价值5万美元的合同工作，并在三个月内创建了[一门完整的编程语言](https://x.com/GeoffreyHuntley/status/1944377299425706060)。

Wiggum最适合某些类型的工作，例如定义明确且无需人工干预的工作。

当我们思考AI的未来发展时，有时值得记住的是，复杂性并非总是前进的方向，而一些最好的工具并非是闪亮的新工具，而是早已可用的工具。