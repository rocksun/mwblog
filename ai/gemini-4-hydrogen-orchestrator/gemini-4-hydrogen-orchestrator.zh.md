![机器人与人类竞赛](https://cdn.thenewstack.io/media/2026/11/ea0c233e-rizki-ardia-p-a6oda-mqu-unsplash-1024x768.jpg)

谷歌于周四推出了 Gemini 4 Hydrogen，并配套发布了一个新系统，改变了编码智能体使用 AI 模型的方式。谷歌没有让功能最强大的模型在整个会话中持续运行，而是将 Hydrogen 与更强大的 Gemini 4 Carbon 进行配对，随着工作的进展在两者之间进行切换。

该公司表示，这种组合在实现与单独运行 Carbon 几乎相同的结果的同时，减少了 24% 的 Token 消耗，并将任务完成速度提高了 19%。

## Orchestrator 如何处理工作

这种切换通过 [Orchestrator](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity) 进行，这是谷歌 [Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/) 开发环境中的一项新功能。其中 Carbon 承担要求更高的推理工作（包括架构设计和调试），而 [Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) 则负责代码更改和测试。

Carbon 可能会遍历代码库以弄清楚如何实现某个功能，然后将实际编码交由 Hydrogen 处理；当某个失败的测试需要重新审视方法时，Carbon 会再次介入，然后将执行权交还回去。

Google DeepMind AI 工程副总裁 [Clement Farabet](https://www.linkedin.com/in/clementfarabet/) 在 [X 上的帖子](https://x.com/clmt/status/2120944361877713308)中称这一组合是“智能体编码的巨大突破”。
  
领导谷歌 Antigravity 团队的 [Varun Mohan](https://www.linkedin.com/in/varunkmohan/) 在[另一篇帖子](https://x.com/_mohansolo/status/2120941094724874380)中表示，将 Hydrogen 与 Orchestrator 和群集（swarms）配对“在内部非常受欢迎”。

## 谷歌的数据何处不匹配

谷歌自身的基准测试报告并不完全一致，因为主要的 [Gemini 发布公告](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)引用了 [Terminal-Bench 4.0](https://www.tbench.ai/news/terminal-bench-4-0)，而 [Antigravity 发布公告](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity)则引用了 4.1 版本。

该公司也没有公布 Carbon 的独立成功率、每个任务的详细拆解，或是关于 Orchestrator 路由决策的足够细节，以证明所报告的效率提升究竟源自何处。

> ……尚未公布 Carbon 的独立成功率……或关于 Orchestrator 路由决策的足够细节，以证明所报告的效率提升究竟源自何处。

## Hydrogen 的得分超过了更昂贵的模型

谷歌将 Hydrogen 描述为“智能体工作流的日常驱动模型”，其输入 Token 价格为每百万 1.50 美元，输出 Token 价格为每百万 7.50 美元，这些费率在其完整的百万 Token 上下文窗口中保持不变。

该模型可通过 [Google AI Studio](https://aistudio.google.com/)、Gemini API 以及 Gemini 应用和谷歌搜索获取。

在 [Artificial Analysis 智能指数](https://artificialanalysis.ai/)上，Hydrogen 在默认的高思考水平下得分为 51，略高于更昂贵的 [Gemini 4 Argon](https://thenewstack.io/google-gemini-4-argon/)（50 分）。将推理力度调至谷歌全新的 xhigh 设置，Hydrogen 的得分可达 54，尽管额外的推理可能会增加 Token 消耗和处理时间。

Argon 是谷歌在 9 月 30 日发布时的旗舰模型，但在 10 月 28 日发布后，[Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) 在大多数已发布的基准测试中超越了它。Hydrogen 领先一分虽然不大，但这又是一个信号，表明谷歌的低成本模型正以多快的速度赶上几周前还被视为前沿性能的水平。

谷歌还声称，在默认设置下，Hydrogen 完成任务的速度比 Gemini 3.8 Flash 快 2.5 倍，其 Terminal-Bench 4.1 得分达到 57%，而 Flash 仅为 18.2%。据该公司报道，虚假声明减少了五倍以上。

> Hydrogen 领先一分虽然不大，但这又是一个信号，表明谷歌的低成本模型正以多快的速度迎头赶上……

## 模型切换的代价

谷歌尚未披露 Orchestrator 是如何决定何时切换模型的，也没有披露这些交接在额外的 Token 和延迟方面付出了什么代价。

目前，Orchestrator 仅限于 Google AI Ultra 订阅用户使用，并计划支持更多模型和订阅层级。Hydrogen 正在向付费的 Antigravity 用户推出，预计将实现[更广泛的可用性](https://thenewstack.io/google-antigravity-ide-extensions/)。

> 谷歌尚未披露 Orchestrator 是如何决定何时切换模型的，也没有披露这些交接在额外的 Token 和延迟方面付出了什么代价。

这篇名为 [Google’s Gemini 4 coding agent now switches models mid-task — and finishes 19% faster](https://thenewstack.io/gemini-4-hydrogen-orchestrator/) 的文章最初发布在 [The New Stack](https://thenewstack.io)。