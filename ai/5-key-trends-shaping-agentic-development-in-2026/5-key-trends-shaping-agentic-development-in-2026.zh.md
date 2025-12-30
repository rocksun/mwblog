在过去一年对代理式开发的回顾以及展望2026年的过程中，我研究了一些[塑造LLM服务](https://thenewstack.io/from-agi-hype-to-engineering-reality-the-future-of-llms/)的趋势。在这篇文章中，我将重点关注新一年AI开发工具的预期。

正如Cory Doctorow在他的[Reverse Centaur总结](https://pluralistic.net/2025/12/05/pop-that-bubble/#u-washington)中所指出的，科技公司总是希望成为“成长股”——因此，他们必须不断证明存在一个具有尚未开发潜力的新愿景。这与仅仅改进现有产品的团队背道而驰——天知道公司股票被标记为“成熟”是多么糟糕。但2026年真正*应该*关注的，是改进开发者们正在努力掌握的大量新事物。

## 1. 改善模型上下文协议（MCP）的可见性和管理

由于模型上下文协议（MCP）已迅速成为代理与外部工具交互的公认方式，因此必须投入更多精力来控制MCP服务器——无论是通过集中管理还是更清晰的仪表板。虽然开发者们享受着连通性带来的改进工作流程，但对这些连接的管理却有些随意。MCP的成功似乎跨越了不同部门，因为非技术人员也希望他们的代理请求能够与Slack等工具通信。这些内部连接某种程度上回答了“我的业务中正在发生什么？”的疑问。这意味着开发者们将忙于设置MCP服务器。

如果一个组织中将有大量活跃的MCP服务器，那么对其管理将变得越来越重要。人们通过MCP做的事情越多，出现的问题也越多。

## 2. 支持资深工程师的并行任务执行

今年我研究了两款明确支持并行运行任务的应用程序（[Conductor](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/)和[Verdent AI](https://thenewstack.io/first-look-at-verdent-an-autonomous-coding-agent-from-china/)）——即有效地定义一个任务，然后让LLM在后台执行它，同时开始一个新任务。虽然你通常可以要求任何Agentic CLI在后台运行任务，但在2026年，更多的应用程序将支持将并行运行作为一种工作流程。

关于执行这些任务有一点需要注意：为了在相同的代码库上工作，目标代码需要被隔离。这通常意味着为每个任务创建一个新分支，然后将代码放入一个新的文件夹中，这就是git worktrees所做的。然后你再将工作合并回主分支。所有这些git操作多少有些违背“氛围编程”的说法——但正如我所指出的，LLM工具将始终倾向于对资深开发者最有用。

也只有拥有扎实经验的开发者才能迅速评估一项更改是否足够安全，可以委托给代理……或者不能。而且，资深开发者已经习惯了全天候的中断，在这种情况下，中断来自于代理在不同时间完成任务。

## 3. 明确Agentic CLI与桌面应用程序的角色

当我们首次看到[Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)在终端会话中运行时，它立即让开发者能够用英文指令定义任务。因此，就有了代理命令行界面（Agentic Command Line Interface，CLI）这个术语。这与使用VS Code等IDE形成了鲜明对比。

Claude Code用TypeScript和React构建，可以在任何终端shell中运行，使其能够共享一个即时环境，并在与项目相同的目录中启动。这让许多开发者感到舒适。此后，已经发布了不少类似的CLI应用程序。在同一提示符下传递shell命令的能力（在[Warp](https://thenewstack.io/warp-code-gets-closer-to-an-emacs-for-the-modern-ai-era/)中实现得最简洁）有助于减少应用程序切换的摩擦。

但许多桌面版本也已发布，例如[Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/)，它提供了在MacOS或Windows上精炼的UI优势。例如，你可以获得漂亮的文件和文件夹视图，以及对请求和响应UI组件的更多控制。从企业角度来看，管理桌面应用程序也更容易一些。然而，桌面应用程序与CLI版本究竟如何比较，仍然可能不清楚。

在2026年，我预计所有主要供应商都将更清楚地说明他们将如何支持其LLM产品的CLI和桌面版本。每个版本可能拥有不同的社区，但不应将它们视为独立的实体。

## 4. 整合付费服务和代理驱动的商业

代理如何成功请求付费服务——即代理驱动的商业——迟早会出现。目前还没有对这方面的强烈需求，但最终代理将需要在后台调用付费服务——或在调用者没有明确支付计划的任务中使用更昂贵的模型。我们大多数人同时对“机器对机器经济”持怀疑和接受态度。如果自主权必须止步于收银台，那它就没有意义。今年可能会有各种尝试来解决这个问题；特别是对于可以使用多个模型的产品。对于那些运行本地LLM，只希望在更深层任务中调用云LLM的开发者来说，尤其如此。

## 5. 解决AI开发中VS Code分支的挑战

[微软Visual Studio Code分支问题](https://thenewstack.io/agentic-coding-and-the-weakness-of-extensions-for-ides/)必须得到更密切的关注。我们已经看到不少非微软应用程序实际上是VS Code的内部克隆——[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/)就是一个早期例子。虽然在VS Code内部使用扩展模型不足以支持LLM，但分支也有其局限性。在不那么安全的独立市场中寻找其他扩展的问题可能仍然存在。在某些方面，微软成功地占领了市场，使得竞争者要么加入，要么碎片化。当谷歌推出自己的VS Code分支[Antigravity](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/)时，我内心并没有崩溃，但它确实再次将整个问题推向了高潮。

太多的产品团队将VS Code分支视为速战速决的胜利，却从未真正问过自己是否有认真计划买自己的房子——还是永远租房。然后他们忘记了租赁合同阻止他们在墙上钉钉子。但在2026年，很可能会有新的方法来规避这个问题。

## 结论

今年是代理式AI工具，特别是Agentic CLI的爆发之年，我预计2026年将是巩固这些成果的一年。开发者们不需要被说服LLM能实现什么，但他们需要被说服现有的产品能够长期可靠地支持他们的工作流程。