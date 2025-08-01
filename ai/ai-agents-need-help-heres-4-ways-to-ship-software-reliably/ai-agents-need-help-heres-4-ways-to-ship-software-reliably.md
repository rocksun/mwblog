<!--
title: AI Agents求助：软件可靠交付的四大秘诀
cover: https://cdn.thenewstack.io/media/2025/07/79cfde19-tai-bui-lxg8spogmde-unsplash-scaled.jpg
summary: 本文探讨了在软件交付中应用AI代理的四个原则：限制代理范围，提供可重复沙箱，实现完全可观测性，以及依赖Evals进行可靠性评估。强调了尽早投资Evals的重要性，并指出代理工作流需在严格范围、干净沙箱和透明跟踪中运行。
-->

本文探讨了在软件交付中应用AI代理的四个原则：限制代理范围，提供可重复沙箱，实现完全可观测性，以及依赖Evals进行可靠性评估。强调了尽早投资Evals的重要性，并指出代理工作流需在严格范围、干净沙箱和透明跟踪中运行。

> 译自：[AI Agents Need Help. Here's 4 Ways To Ship Software Reliably](https://thenewstack.io/ai-agents-need-help-heres-4-ways-to-ship-software-reliably/)
> 
> 作者：Sam Alba

*本文是对我在旧金山举行的 [2025 年 AI 工程师世界博览会](https://youtu.be/l65so0OoJeo?si=7RtwVDUnQRwpvbOJ) 上所做演讲的深入剖析。基于我作为 [Dagger](https://dagger.io/) 的联合创始人以及 Docker 的第一位员工在软件交付和代理方面的经验。*

随着 LLM 生成越来越多的代码——从更智能的自动完成到完全自主的编码代理——编写代码的*成本*直线下降。压力随后转移到交付管道，因为每一行新代码在进入生产环境之前仍然必须通过测试套件和代码审查。

软件交付自动化一直是一个瓶颈——这就是我们推出 Dagger 的原因——但现在任何人都可以生成大量不错的代码，因此瓶颈正在收紧。

2025 年 4 月，我们[向 Dagger 工作流添加了原生 LLM 调用](https://dagger.io/blog/llm)。团队现在可以将认知繁重的任务委派给 LLM：强化 Dockerfile 以提高[安全性和效率](https://thenewstack.io/devsecops-tools-that-offer-security-efficiency-and-quality/)、诊断 CI 错误并建议修复（或直接打开 PR），甚至可以端到端地处理未解决的问题。[我们在文档中分享了具体的例子](https://docs.dagger.io/examples)。

让我们来看看大多数团队在嵌入 LLM 时遇到的陷阱——以及如何避免它们。这些经验教训来自软件交付自动化，但适用范围更广。

大多数人首先尝试旗舰模型（GPT-4o、Claude 4、Gemini 2.5…）。这些模型对马虎的提示词很宽容，因此早期的结果会带来“哇”的时刻，并让人相信多代理工作流可以处理复杂的任务。

现实随可靠性而来。当模型发布错误的代码或触发错误的工具时，即使 10 次运行中只有 1 次，信任也会崩溃。你不能将这种程度的差异引入到[发布产品的代码](https://thenewstack.io/agile-coding-production-requires-agile-security/)中。

我们在 Dagger 提炼了四个原则，以保持代理工作流在生产中的可信度。

## 将 AI 代理的范围限制在小型、定义明确的任务中

大型模型让人很想将庞大、开放式的目标交给代理。不要这样做。将每个代理的任务范围缩小到最低限度，并通过*长而明确的提示词*来抵消狭窄的范围，该提示词详细说明了每个约束。

与直觉相反，任务越小，提示词越长。额外的上下文为模型提供了防护栏——并且模型本身可以有效地帮助你完善提示词。

将 LLM 视为*大脑*，将工具视为*手脚*。添加工具让人感觉充满力量，但每个工具都会扩大上下文窗口和随机行为的可能性。更少的工具 → 更小的上下文、更低的成本、更确定的运行。

我经常意识到，我计划作为工具公开的助手调用起来更便宜。示例：在我们的 Dockerfile 优化器中，一个计算镜像层数和总大小的函数在代理启动之前运行；我们将它的输出输入到提示词中，而不是让代理调用它。

需要更大的工作流？链接微代理。一个轻量级的“分流代理”接收请求并委托给专门的子代理，每个子代理都具有极小的范围和工具集。

[OpenAI Agents SDK](https://github.com/openai/openai-agents-python/tree/ad80f788b9a9c37ab76018824073103b88f154d7/examples/agent_patterns#agents-as-tools) 说明了这些模式。

## 为每个 AI 代理提供可重复的沙箱

与人类开发人员一样，代理**永远**不应接触特权环境。他们需要一个隔离的、可重现的工作区——安全、可处置，并且具有直接的状态管理进出。

由于市场上没有任何产品满足这些要求，因此我们构建了 [**container-use**](https://github.com/dagger/container-use/)。它作为 [MCP 服务器](https://modelcontextprotocol.io/introduction) 运行，为任何编码代理（Claude Code、OpenAI Opex、Cursor、Goose）或你自己制作的代理工作流启动容器化的开发环境。

一次处理多个代理？每个代理都有自己的沙箱，因此你可以自由地进行实验，而不会污染本地 git 分支。沙箱是一个[完整的容器堆栈](https://thenewstack.io/webassembly-users-a-mix-of-backend-and-full-stack-developers/)：代理可以在其中运行 shell 命令，并且你可以在任何时候进入终端以检查更改或重放命令。

## 信任需要完全的**可观测性**

透明产生信任；代理也不例外。

在大多数应用程序中，函数级别的**可观测性**是一个“锦上添花”的功能，仍在路线图上。对于代理工作流，它变得*强制性*。否则，LLM ⇄ 工具循环就是一个黑匣子，调试需要回答以下问题：调用了哪个工具？使用什么参数？按什么顺序？在步骤 *n* 时的沙箱状态是什么？

简而言之，你不能依赖于对其工作没有可见性的智能代理。

主要的模型提供商会公开跟踪（例如，OpenAI Traces），但不要附加一个孤立的“AI **可观测性**”堆栈——让[你*现有的*平台](https://thenewstack.io/the-3-paradoxes-of-cloud-native-platform-engineering/) 意识到 AI。这就是我们为什么将完整的 LLM 上下文（系统/用户消息、工具调用）连接到 [**Dagger Cloud**](https://dagger.cloud)：你可以跟踪整个交付管道，无论是 LLM 驱动的还是非 LLM 驱动的。

同样的理念也适用于 [**container-use**](https://github.com/dagger/container-use/)：每个沙箱会话都经过完整的检测，因此代理行为永远不会不透明。

## AI 代理的可靠性取决于 Evals

在所有四个原则中，这一个最重要：为了衡量提示词质量、代理成功率、工具功效和模型性能，你必须尽早投资 **Evals**——*模型评估*的缩写。将 Evals 视为代理的 CI。

模型发展迅速。即使是“完美”的工作流也会漂移，除非你持续衡量它。在以下情况下运行 Evals：

* 工作流代码发生更改，
* 你升级或交换模型，
* 你调整提示词，
* 你修改工具。

频繁运行会暴露一个经济真相：大型、有能力的模型也很慢且昂贵。有了指标，你通常会降级到较小的模型，这些模型虽然功能较弱，但更便宜且（使用正确的提示词）更有效。权衡？这些提示词会变得更长、更细致——这是一个有用的强制清晰的函数。

正如 Dagger 团队的 Alex 喜欢说的那样：**无论模型或框架如何，你都无法超越提示词工程。** 尽早进行自动化 Evals 可以防止你在大型模型的成本——或它们的怪癖——触及瓶颈时拆除一切。

总而言之，[代理工作流释放了非凡的速度和规模](https://thenewstack.io/cloud-native-and-open-source-help-scale-agentic-ai-workflows/)，但前提是它们在严格的范围内、干净的沙箱、透明的跟踪和不懈的 Evals 中运行。遵循这四个防护栏，你将把引人注目的演示变成你可以押注生产的管道——今天和随着模型不断向前发展。