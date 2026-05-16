<!--
title: 云端代码：Conductor 加入远程编程智能体竞争浪潮
cover: https://cdn.thenewstack.io/media/2026/05/cb8b4711-getty-images-fluainycdfy-unsplash-scaled.jpg
summary: AI 编程智能体正从本地终端转向持久化云端环境。初创公司 Conductor 推出云端平台，支持在托管环境中并行运行多个智能体，这标志着 AI 编程正向自动化和大规模协作转变。
-->

AI 编程智能体正从本地终端转向持久化云端环境。初创公司 Conductor 推出云端平台，支持在托管环境中并行运行多个智能体，这标志着 AI 编程正向自动化和大规模协作转变。

> 译自：[Cloud code: Conductor joins the rush toward remote coding agents](https://thenewstack.io/conductor-cloud-ai-coding-agents/)
> 
> 作者：Paul Sawers

**AI 编程智能体正开始摆脱笔记本电脑的束缚。**

最初仅在终端和 IDE 中运行的工具正在迁移到持久的云环境中，在云端它们可以运行更长时间、并行工作，并在开发者关闭电脑后继续执行任务。

最新的案例是 [Conductor](https://www.conductor.build/)，这是一家最近筹集了 [2200 万美元 A 轮融资](https://www.conductor.build/blog/series-a) 的 AI 编程初创公司。该公司凭借一款 Mac 应用获得了关注，该应用充当在工作区本地管理编程智能体的界面。5 月初，该公司宣布推出 [Conductor Cloud](https://x.com/charlieholtz/status/2052832173527650779)，将这些智能体移至托管环境中。

这一转变反映了整个 AI 编程市场的广泛变化。Anthropic 最近 [推出了 Claude 托管智能体 (Claude Managed Agents)](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/)，这项服务允许企业在 Anthropic 的基础设施上运行长寿命智能体，并为通过 [网页和移动端界面](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/) 进行的 Claude Code 会话添加了 [远程控制](https://code.claude.com/docs/en/remote-control) 功能。Mistral [也同样开始推动](https://thenewstack.io/mistral-vibe-cloud-agents/) 其氛围编程智能体进入云端。

在其他地方，开源 AI 编程初创公司 Roo Code [最近宣布](https://thenewstack.io/roo-code-cloud-ides-ai-coding/) 将关闭其 VS Code 扩展及更广泛的 IDE 工具，转而支持 [Roomote](https://roomote.dev/)，这是一种旨在跨 Slack、GitHub 和 Linear 等平台运行的云端自主编程智能体。

因此，Conductor 的最新举措非常符合行业趋势。

## 进入云端：解决“界面挑战”

Conductor 于 2024 年由 Charlie Holtz 和 Jackson De Campos 在旧金山创立，其推出的 Mac 应用让开发者能够在代码库的隔离副本中并行运行多个编程智能体（包括 Anthropic 的 Claude Code 和 OpenAI Codex），审查它们的工作，并将结果合并在一起。

![Conductor Mac 应用演示](https://cdn.thenewstack.io/media/2026/05/028e2ab6-demconducto2gif.gif)

*运行中的 Conductor Mac 应用*

该公司新的云服务（作为早期访问计划的一部分通过邀请提供）将这些智能体会话扩展到托管环境中，在开发者断开本地连接后，这些环境仍会继续远程运行。

> “我认为要达到运行超过三到五个（智能体）的下一个阶段，这挑战在于界面。”

在 [最近的一次视频采访](https://www.youtube.com/watch?v=u2z44EkIEHE) 中，Y Combinator 合伙人 Aaron Epstein 对 Holtz 进行了采访，Holtz 表示他将当前的 AI 编程工具视为一个编排问题，特别是当开发者开始同时运行多个智能体时。

“在我的脑海中，我同时只能管理三到五个智能体，”Holtz 解释道，“我认为我们已经证明了你可以同时运行多个编程智能体，而且它仍然是高效的。但我认为要达到运行超过三到五个的下一个阶段，这挑战在于界面。”

Conductor Cloud 允许开发者在与不同任务和仓库绑定的独立托管工作区中运行编程智能体。随后，开发者可以直接在 Conductor 界面中通过侧边栏的差异视图（diff view）检查这些远程智能体生成的代码更改。

![Conductor Cloud 展示](https://cdn.thenewstack.io/media/2026/05/24a41fda-cloudgif.gif)

*Conductor Cloud*

值得注意的是，托管工作区可能会改变 Conductor 等产品的经济模式。到目前为止，AI 编程的激增主要围绕本地客户端和叠加在基础模型 API 之上的开发者工具。云托管工作区引入了这种可能性：公司不仅可以为协作软件收费，还可以为这些智能体执行的基础设施收费。

Conductor 尚未详细说明 Conductor Cloud 的定价，不过这项托管服务可能会与其现有的本地优先产品并存。其本地产品已经包含一个 [企业版](https://www.conductor.build/enterprise)，该公司称其用户来自 Spotify、Square、Ramp、Linear 和 Notion 等公司。

## 终端的衰落？

AI 编程工具已经改变了软件团队构建和交付产品的速度，而且模型正变得越来越强大。由于编程智能体承担了大量的实现工作，曾经需要仔细划定范围的 MVP 和有限产品目标，现在可以更积极地去完成。

Holtz 则认为，当前这一代工具仍处于这一转变的相对早期阶段。

> “模型将变得聪明 10 倍或 100 倍。它们将能够在无需你干预的情况下运行更长时间。”

“有一件事我们深信不疑，那就是模型将变得聪明 10 倍或 100 倍，”他说道，“它们将能够在无需你干预的情况下运行更长时间。它们将开始让你感觉更像一个人类同事，尽管它们拥有一个与我们截然不同的‘异类大脑’。”

这在一定程度上解释了为什么 Holtz 认为持久化的云端执行对 AI 编程的未来至关重要。如果开发者最终是监督一群长时间运行的智能体，而不是亲自引导每一个步骤，那么将这些系统绑定在单个笔记本电脑会话中就显得毫无意义了。

“我认为这就是我们对 [Conductor] Cloud 感到非常兴奋的原因之一——智能体将能够运行更长的时间，”他说道。

虽然云托管智能体正成为 AI 编程的重要组成部分，但似乎很少有公司准备完全放弃本地开发环境。

[Amp](https://ampcode.com/) 是一家从 Sourcegraph 剥离出来的 AI 编程初创公司，[最近重构了其 CLI](https://thenewstack.io/amp-neo-cli-agents/)，支持远程控制、插件和运行时间更长的智能体会话。本地环境并未消失；更多的是，它成为了开发者用来监控和引导在别处运行的智能体的地方。

Atlassian 也在朝着类似的方向迈进，通过一款 [专为 AI 编程智能体设计的新 CLI](https://thenewstack.io/atlassian-teamwork-graph-agents/) 扩展其企业工具套件的访问权限。其核心思路是让智能体直接导航这些系统——查询工单、拉取请求和项目数据——而不是依赖开发者手动将这些上下文喂给提示词。

因此，整个行业正在呈现出一幅新兴图景：编程智能体正成为在笔记本电脑、终端、浏览器和托管基础设施之间移动的持久系统——开发者将减少亲自编写每一行代码的时间，而投入更多时间在不同环境中监督智能体。