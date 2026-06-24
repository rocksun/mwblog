<!--
title: Nx发布Polygraph，直击AI编程代理的瓶颈问题
cover: https://cdn.thenewstack.io/media/2026/06/1511fc25-eduardo-ramos-ihdifq-re3m-unsplash-scaled.jpg
summary: Nx推出了名为Polygraph的服务，通过构建“合成单体仓库”并引入共享记忆机制，解决了AI编程代理在处理跨仓库任务时的协作困境，显著提升了开发效率与上下文感知能力。
-->

Nx推出了名为Polygraph的服务，通过构建“合成单体仓库”并引入共享记忆机制，解决了AI编程代理在处理跨仓库任务时的协作困境，显著提升了开发效率与上下文感知能力。

> 译自：[Nx debuts Polygraph, taking aim at what's stalling AI coding agents](https://thenewstack.io/nx-polygraph-synthetic-monorepo-agents/)
> 
> 作者：Frederic Lardinois

[Nx](https://nx.dev) 是开源 [monorepo](https://thenewstack.io/monorepos-hal-9000-approved-code-management-and-collaboration/) 构建系统的幕后公司，周二推出了 Polygraph。这是一项将多个代码仓库连接成所谓的“合成单体仓库”的服务，[AI 编程代理](https://thenewstack.io/ai-coding-tool-stack/) 可以像处理常规单体仓库一样在其中工作。

在接受 *The New Stack* 采访时，Nx 的创始人指出，虽然代理在单个仓库内可以完成很多工作，但当变更涉及其他仓库或依赖于他人已完成的工作时，它们往往会陷入停滞。Polygraph 通过结合多个仓库以及来自代理追踪的上下文信息，旨在改变这一现状。

联合创始人 [Victor Savkin](https://ca.linkedin.com/in/victorsavkin) 和 [Jeff Cross](https://www.linkedin.com/in/jeffbcross/) 分别担任公司的 CTO 和 CEO，他们曾是 Angular 团队的 Google 工程师。他们告诉 *The New Stack*，Polygraph 最初是 Nx 内部的一个仅供企业使用的功能，但由于其独特性，团队决定将其作为独立产品发布。

目前，该产品在抢先体验期间免费提供。

## Nx 为何构建 Polygraph

正如 Savkin 所指出的，一个快 10 倍的编程代理并不能让工程师的速度提升 10 倍，因为编码只是工作的一部分。根据 Nx 自己的建模，主要独自工作的开发者使用代理式编程工具时，效率提升约 4.3 倍；而在大型组织中，由于开发者花费更多时间进行协作，效率仅提升了 1.3 倍。

> “代理的局限性由它们的自主程度决定。”

“代理的局限性由它们的自主程度决定，”Savkin 说。代理运行几分钟后，就会“无事可做”，并将控制权交还给人类。团队认为这是因为代理只能在它所在的仓库中工作，并且会在会话之间遗忘所有内容。

## 合成单体仓库

Polygraph 首先会分析公司的代码仓库（内部仓库加上它们所依赖的开源包），并利用这些信息构建一个依赖图，显示哪些仓库发布了哪些包，以及哪些 API 是如何被定义和调用的。代码不会被移动，Polygraph 创建的只是它自己的图谱。

> “我的意思是，你可以同时在同一个地方读取所有你想读取的内容，并编写所有你想编写的内容。”

“Monorepo 对某些人来说带有负面含义。它意味着‘大’，”Savkin 说。“我的意思是，你可以同时在同一个地方读取所有你想读取的内容，并编写所有你想编写的内容。” 有了 Polygraph，你现在可以，例如，在一个会话中更改 API 的生产者，而代理可以看到并更新每一个消费者，因为所有的代码对代理来说都是可访问的。

## 每个会话的共享内存

合成单体仓库本身已经非常有用，因为它使代理的工作变得容易得多，但团队认为，共享内存才是将这一切串联起来的关键。

“组织中任何工程师与代理进行的每一次对话都将被捕获，”Savkin 说，“这有点像工作是如何产生的元图谱。” Polygraph 将这些会话关联起来，因此一个新的会话会根据它试图实现的目标（而不仅仅是它触及了哪些文件）来呈现相关的过往工作。他说，目标是建立一个“所有员工都为同一个集体智慧做出贡献”的组织，而不是每次会话都从零开始。

值得注意的是，这种内存是可移植的。Polygraph 可以在另一台机器上重建会话的确切状态，包括仓库、日志和正在运行的代理。

> “他获得了我的状态、我的仓库、我的一切、我的会话、我的追踪记录……这有点像《星际迷航》中的瞬间移动。”

这意味着另一位开发者现在可以轻松恢复该会话。“他获得了我的状态、我的仓库、我的一切、我的会话、我的追踪记录，”Savkin 说。“这有点像《星际迷航》中的瞬间移动。”

## 协调变更

不过，整合代码只是跨仓库变更的一半工作。另一半是交付代码。在一次会话中，Polygraph 会设置受影响的仓库，将变更推送到下游消费者，以便代理在合并前进行验证，然后为每个仓库打开拉取请求（pull request）。

不过，有一个注意事项。拉取请求仍然是分开合并的，因此这不是跨仓库的单一原子提交。

## 对代理持中立态度

Nx 将 Polygraph 称为“元工具（meta-harness）”，因为它围绕着编程代理运行，而不是本身就是一个代理。它目前支持 [Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)、[Codex](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/) 和 [OpenCode](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/)，通过 [agent-to-agent (A2A) 协议](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) 将它们连接在一起，未来路线图中还包括 [Google 的 Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/) 和其他编程代理。

由于会话是可移植的，开发者可以在任务进行到一半时切换模型，这在代理失去灵感或 token 用完时很有帮助。

## 如何开始

在发布时，Polygraph 仅支持 GitHub。Polygraph 命令行工具会检测安装了哪些代理，并将匹配的插件添加到这些代理中。会话可以从 CLI 开始，也可以在像 Claude Code 这样的代理中通过 /polygraph 斜杠命令在任务中途开始。

对于企业而言，Cross 表示还有一个安全优势。一个提示词就可以告诉 Polygraph 找到所有依赖于易受攻击库版本的代码并进行更新，从而打开尽可能多的拉取请求。他说，这可以将 CVE 的响应时间“从几天或几周缩短到几小时内即可完成。”

## 定价

定价将在稍后公布，可能基于使用量，并根据公司索引仓库和创建会话的频率进行计量，提供免费层级，随着仓库数量的增加费用也会相应提高。

Cross 说，Nx 有耐心等待。“我们对让更多人使用它比对超过 Nx 的收入更感兴趣，”他说。