如果问工程师们他们认为使用 AI 节省了多少时间，他们通常会给出乐观的答案。但是，当你将这种情绪与真实的定量数据进行比较时，数字并不吻合。

人们倾向于孤立地思考个人时间节省：“我更快地完成了我的 PR。” 这个 pull request (PR) 可能会在未经审查的情况下等待三天，然后在测试中失败并反弹回来进行修复。结果是整个工程组织效率低下，这会消耗掉所有获得的生产力。

大多数工程组织不需要更快的打字员。常见的工程瓶颈是不可靠的流水线、没有测试策略、糟糕的文档或组织结构——这些都是实现业务价值的常见障碍。你的团队编写代码的速度可能会略微提高，但是除非你[解决这些系统性问题](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness)，否则你永远无法充分发挥 AI 工具的价值。

## “如果我们不使用 AI，我们就会被抛在后面。”

在 AI 出现之前，开发者体验就已经是一个棘手的话题。当我们谈论 [AI 时代的开发者体验 (DevEx)](https://thenewstack.io/how-to-think-about-devex-when-ai-writes-the-code/) 时，让我们首先承认，即使是 [“开发者”的定义也在发生变化](https://www.aviator.co/blog/software-engineering-ai-2027/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-engineering-2027&utm_term=net-new&utm_content=awareness)。它不再是某人从产品团队获得需求并默默地编写代码。相反，他们可能会从 AI 工具生成部分工作的概念验证，或者与使用 AI 来原型化想法的非工程师更流畅地协作。

AI 工具也呈爆炸式增长。感觉每天都有新的东西上市。一方面，这对工程师来说是令人兴奋的：闪亮的新工具、新的工作方式。另一方面，来自领导层的压力，我称之为一种 FOMO（错失恐惧症）。你会看到高管们在想：“如果我们不使用 AI，我们就会被抛在后面。”

## 不要只选择工具，要选择问题

各个组织花费了太多的时间、金钱和精力来关注工具本身。“我们应该使用 OpenAI 还是 Anthropic？Copilot 还是 Cursor？” 我们看到组织采用 AI 工具的方式有两种广泛的模式。

第一种是领导层与某个供应商有关系或者只是个人偏好，因此他们选择一种工具并强制执行。这可能会奏效，但你通常会得到不好的结果——不是因为工具不好，而是因为市场变化太快，集中式团队无法跟上。

第二种模式通常效果更好，是允许早期采用者尝试新工具并找到有效的方法。这使开发者能够自主地改进自己的工作流程，并减少了中央团队详尽测试每种新工具的需求。

比较工具的功能或技术每天都变得不那么重要。你会在争论明年无关紧要的细微差异上浪费大量精力。相反，要专注于你想要解决的问题。你是否试图改进测试？[代码审查](https://www.aviator.co/flexreview?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-4-flexreview&utm_term=net-new&utm_content=awareness)？文档？事件响应？首先确定目标。然后看看 AI 工具（或任何工具）是否真的有帮助。

如果你不这样做，你只会让 DevEx 变得更糟：你将拥有 100 种没人知道如何使用的工具，并且你将无法交付任何真正的价值。

## 复杂性无法消除，只能抽象化

关于没有软件工程师的 AI 未来的炒作很多。但现实情况是，你无法从工程中消除复杂性。你可以将其抽象化，但复杂性仍然存在。

即使这种乌托邦存在，AI 和代理完成所有工作，我们仍然需要创建代理、训练它们、添加新的可观测性级别、实施更好的 FinOps 控制来理解成本和复杂性、管理它们使用的模型，并添加新的治理层来审计导致其决策的推理。

想象一下，你让 AI 代理处理事件响应：它可以收集日志并生成报告。这是一个很好的用例。然后，另一个代理或一组代理可以通过 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 切换功能标志或触发回滚。这听起来很棒——直到出现问题。你是否有严格的审计、控制以及 AI 做出错误决定的应对计划？

[!["This is fine" meme](https://cdn.thenewstack.io/media/2025/07/f65692c0-this-is-fine.png)](https://cdn.thenewstack.io/media/2025/07/f65692c0-this-is-fine.png)

来自 KC Green 的“[On Fire](https://gunshowcomic.com/648)”

这是额外的复杂性。这不是更少的工作；这是不同的工作。

在实践中，AI 工具可能会增加认知负荷，而不是减少认知负荷。你可能正在使用五种不同的 AI 增强型集成开发环境 (IDE)。现在不是 20 个浏览器选项卡，而是 50 个。如果没有周到的集成，你只会让自己的生活更艰难。

## 使用 AI 降低认知负荷

如果你希望你的工程组织从 AI 中获得真正的价值，你必须[识别阻碍人们的浪费和摩擦](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness)，并以同样的方式解决它们——通过拥有一个良好的支持平台（无论你称之为[平台工程还是其他什么](https://thenewstack.io/platform-engineering-vs-devops-misses-the-point/)）。使用 AI 工具改善开发者体验的唯一方法是从平台角度入手，并一遍又一遍地应用这种思维方式。

考虑一下[平台工程](https://thenewstack.io/platform-engineering/)，它不仅将问题抽象化为静态仪表板，还策划了 AI 驱动的层，该层总结了重要的问题。

强调*重要*。现在有一些 AI 站点可靠性工程 (SRE) 工具可以帮助你调查事件，但它们会给你列出 20 件可能出错的事情。从开发者工作流程的角度来看，这没有帮助；开发者需要一个正确的答案，而不是 20 个可能正确的答案。

小心用不透明的 AI 推理取代由人类策划的仪表板。确保你的数据模型足够可靠以支持它。一旦你失去了这种透明度，你就会引入新的风险，例如你的 AI 自信地告诉你“一切都很好”，而事实并非如此。

## 问题不是“你的 AI 战略是什么？”

大约 90% 到 95% 的工程效率低下是由有缺陷的系统造成的，而不是由人造成的。因此，不要只是将 AI 扔到所有事情上，并通过询问人们“它是否为你节省了时间？”来衡量成功与否。相反，要全面地审视你的软件交付生命周期：

* 哪里摩擦最大？
* 哪里工作排队？
* 哪里会发生返工？

只有这样，你才能决定 AI 是否以及如何提供帮助。因为你可能不需要更快的打字员。你需要[更好的系统](https://www.aviator.co/?utm_source=tns&utm_medium=content&utm_campaign=q2-2025-tns-article-2-aviator-home&utm_term=net-new&utm_content=awareness)。