本周 AI 开发者工具领域中最热门的讨论始于一份职位描述。

Anthropic 的 [Claude Code](https://www.anthropic.com/claude-code) 负责人 [Boris Cherny](https://www.linkedin.com/in/bcherny/) [表示](https://x.com/rohanpaul_ai/status/2063289804708835412)，他不再直接向 Claude 发送提示词，而是说“我的工作是编写循环”。Peter Steinberger [敦促](https://x.com/steipete/status/2063697162748260627) 开发者设计用于触发代理的循环。本周日，Google 工程师 Addy Osmani [发表](https://addyosmani.com/blog/loop-engineering/) 了一篇文章，为这种模式命名为：**循环工程（loop engineering）**。

名称本身并不重要，重要的是它所揭示的内容。编码代理正在从交互式助手演变为长时间运行的执行系统，OpenAI 和 Anthropic 已经花费数月时间构建了循环的六大基础模块。

## 从操作机器到设计生产线

Osmani 将循环工程定义为“取代你自己作为代理提示者的角色”。其核心是一种编排模式，结合了计划执行、隔离工作区、验证代理和持久内存，将编码代理转化为自主的软件工作者。在过去两年里，与编码代理协作意味着一遍又一遍地输入提示词，而人类既是调度员又是质量把关人。

> 其核心是一种编排模式，结合了计划执行、隔离工作区、验证代理和持久内存，将编码代理转化为自主的软件工作者。

循环颠覆了这种安排，最接近的类比是从操作车床转变为设计车床所在的生产线。循环按计划发现工作，利用第二个代理验证结果，并将状态写入文件，以便明天的运行能从昨天中断的地方继续。它比 Osmani 早期的 [harness engineering](https://addyosmani.com/blog/agent-harness-engineering/) 模式高出一个层级。

## 两款产品中相同的构建模块

循环工程之所以从一种非正式模式演变为命名实践，是因为这些构建模块现在已集成在产品内部，而不再需要自定义脚本。

Osmani 将六个原语对应到 Claude Code 和 Codex 中，且映射几乎完全一致：

| 原语 | 循环中的工作 | Codex | Claude Code |
| --- | --- | --- | --- |
| 自动化 (Automations) | 计划发现与分类 | 带分类收件箱的自动化标签页 | 计划任务, `/loop`, 钩子, GitHub Actions |
| 工作树 (Worktrees) | 隔离并行代理 | 每个线程内置工作树 | `git worktree`, 子代理的工作树隔离 |
| 技能 (Skills) | 编码项目知识 | `SKILL.md` 代理技能 | `SKILL.md` 代理技能 |
| 连接器 (Connectors) | 连接外部工具 | MCP 连接器和插件 | MCP 服务器和插件 |
| 子代理 (Sub-agents) | 将制造者与检查者分离 | 定义在 `.codex/agents/` 中的子代理 | `.claude/agents/` 中的子代理, 代理团队 |
| 内存 (Memory) | 在运行间持久化状态 | `AGENTS.md`, 记忆功能, 或通过连接器连接 Linear | `CLAUDE.md`, 自动内存, 或通过 MCP 连接 Linear |

两款产品都提供了一个 `/goal` 命令，让代理持续工作直到达到可验证的停止条件，Claude Code 还会使用单独的模型来评估结果。通过 [Automations](https://developers.openai.com/codex/app/automations)，OpenAI 让 Codex 用户能够将计划发现作为一流的功能使用。Anthropic 在 4 月为 Claude Code 推出了例程（routines），以及动态工作流。

*The New Stack* 通过让 Claude 编写自己的编排脚本并运行并行子代理，测试了动态工作流。有了这些原语，开发者可以将重复的维护工作转化为计划好的自主工作流，团队可以通过隔离的工作树并行运行代理，而不会破坏主分支。当构建这些工具的人指出这一装配流程已经完成时，病毒式的传播时刻便到来了。

## 验证者是获得信任的关键部分

循环中最关键的设计选择是将编写代码的代理与检查代码的代理分离。一个模型评估自己的输出过于宽容，因此，一个带有不同指令的第二个代理可以捕获第一个代理在推理中犯的错误。Anthropic 在其针对长时间运行代理的 harness 工作中[描述](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)过这种分离。

在 Osmani 的例子中，早晨的自动化流程会整理前一天的 CI 失败案例，并派出一个子代理在隔离的工作树中草拟修复方案，同时由第二个代理对照项目测试进行审查。Ramp 的 [Inspect](https://thenewstack.io/ramps-inspect-shows-closed-loop-ai-agents-are-softwares-future/) 在六个月前就将此形态构建为定制基础设施，它作为原生功能出现在两个生态系统中，表明闭环运行正成为默认设置。

## 成本、正确性和理解债

开发者在不到 18 个月的时间里，从提示词工程转向上下文工程、harness 工程，再到现在的循环工程。2026 年循环的调度层是 cron 等传统调度程序。中间的决策逻辑将两者区分开来：cron 作业运行一个固定的脚本，而循环运行一个读取当前状态并选择下一步操作的模型。

Osmani 比他引发的讨论要谨慎得多，他警告称 Token 成本波动极大，且无人值守运行的循环同样可能在无人值守的情况下犯错。他最尖锐的警告是关于“理解债”（comprehension debt）——当你依赖系统发布你从未阅读过的代码时，这种差距就会扩大。两名工程师可以运行相同的循环并获得截然不同的结果：一个人在理解的工作上推进得更快，而另一个人则完全避开了理解。

## 前路展望

开发者可以从一个单一的计划自动化分类和一个验证子代理开始，以极小的 Token 开销捕获大部分价值。Cursor、Google 的 [Antigravity](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/) 以及 GitHub 新推出的 [Copilot 应用程序](https://thenewstack.io/github-copilot-desktop-app/)都在编排代理，但目前还没有将循环作为其工作单元。

这些平台之间的关键区别在于从模型本身转向了围绕模型的循环，因为调度、验证和内存现在决定了交付内容。循环工程已做好准备，将成为 AI 辅助软件开发的编排层，而谁能让循环定义具备可移植性，谁就将占据领先地位。