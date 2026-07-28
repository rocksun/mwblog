Anthropic正在引入AI初创公司Mendral背后的团队，以加强Claude的软件工程能力。作为此次收购的一部分，Mendral将停止其托管产品的运营，并协助现有客户进行过渡。财务条款未披露。

## 从 Docker 到 Claude

Mendral 由前 Docker 工程师和 Dagger 联合创始人 [Sam Alba](https://www.linkedin.com/in/samalba/) 和 [Andrea Luzzardi](https://www.linkedin.com/in/aluzzardi/) 创立，该公司致力于构建 AI 代理，以自动化软件开发中最耗时的部分。Alba 曾担任 Docker 的工程副总裁，而 Luzzardi 是 dotCloud（后来的 Docker）的联合创始人，并编写了该平台最早的代码，这使得两人在塑造现代容器化和 CI/CD 领域方面拥有深厚的背景。

在加入 Y Combinator 的 Winter 2026 (YC W26) 孵化营后，该公司专注于诊断 CI 故障、修复不稳定测试、审查依赖项更新以及处理其他重复性工程工作的工具。创始人们表示，该公司代表了他们之前工作的转变。他们不再构建帮助开发人员编写代码的工具，而是构建能够自行完成部分工作的 AI 代理。

> 他们不再构建帮助开发人员编写代码的工具，而是构建能够自行完成部分工作的 AI 代理。

## 三个常驻代理

具体而言，Mendral 通过三个常驻代理运行：一个负责捕捉泄露的密钥并固定安全依赖版本的安全代理（Security Agent）、一个负责缓解不稳定测试的可靠性代理（Reliability Agent），以及一个通过缓存、并行化和修剪缓慢测试来优化构建时间的性能代理（Performance Agent）。

这些代理在 [Blaxel](https://blaxel.ai/) 的持久沙盒中运行，该沙盒提供了隔离的、原生支持代理的计算能力，从待机状态恢复时间不到 25 毫秒，使它们能够安全地运行调查并提交修复程序，而不会损害内部系统。Mendral 从第一天起就一直在使用 Claude，随着 Anthropic 发布更新的模型，该公司扩展了其代理可以处理的工程任务范围。

## 基于前沿模型构建

“Claude 自我们第一次提交代码以来就一直处于幕后，我们亲身体验了这些模型的进步：每隔几个月，一个新的模型就会使我们路线图的一部分变得多余，并使更大的一部分成为可能，”创始人在宣布这一举措的[博客文章](https://www.mendral.com/blog/mendral-team-joins-anthropic)中写道。“对于 Mendral 团队来说，没有比这更好的地方来研究软件工程正在变成什么样子了，”他们补充道。他们将继续直接在 Anthropic 内部实现那些“不是你的产品”的工程任务自动化。

> “Claude 自我们第一次提交代码以来就一直处于幕后，我们亲身体验了这些模型的进步：每隔几个月，一个新的模型就会使我们路线图的一部分变得多余，并使更大的一部分成为可能。”

## Anthropic 的收购模式

Mendral 的专业知识预计将帮助 Anthropic 构建 Claude 的软件工程工具，包括开发人员在 CI/CD 过程中遇到的各类任务。此举继 Anthropic 今年早些时候[收购 Stainless](https://www.anthropic.com/news/anthropic-acquires-stainless) 之后，Stainless 是一家专注于 SDK 生成和模型上下文协议 (MCP) 服务器工具的初创公司，这家 AI 实验室正寻求扩展 AI 代理的能力，并改善它们与外部系统和开发环境安全连接的方式。

在 Anthropic [近期扩展到企业服务](https://thenewstack.io/ust-anthropic-enterprise-ai-stack/)的背景下，将 Mendral 的人才引入公司，标志着其正在更广泛地推动构建大规模企业 CI/CD 流水线所需的原生工具。

此次收购为 Anthropic 提供了旨在解决软件开发中一些枯燥乏味部分的先进技术。

> “对于 Mendral 团队来说，没有比这更好的地方来研究软件工程正在变成什么样子了。”