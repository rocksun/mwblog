**Anthropic 构建了 Claude Duet**，这是一个人工智能助手，可以监控您连接的应用并在后台处理任务，无需主动要求即可决定哪些事情需要您关注。在其 10 月 21 日首次亮相的一周后，这家[正瞄准 IPO](https://thenewstack.io/claude-codes-enterprise-20-to-1/) 的前沿实验室向 *The New Stack* 分享了它是如何测试 Duet 是否正确把握这些优先级的。

Anthropic 开发了内部评估器来评估 Duet 如何对任务进行优先级排序，尽管紧急程度可能具有主观性。当智能体管理电子邮件、日历和 B2B 应用中的工作时，风险随之增加。Duet 可以在其权限范围内运作，但仍然会搞错优先级。

在 [Claude Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/) 的驱动下，Duet 可以准备工作并标记它认为需要关注的项目，而无需等待指令。Anthropic 一直在与自己的员工一起测试这种方法，利用他们的日常工作来观察 Duet 如何处理相互冲突的优先级。

## 测试 Duet 的判断力

“在 Anthropic 将 Duet 用于日常工作后，我们校准了评估器，以评估任务优先级排序的正确性，并在离线状态下针对代表内部使用和早期外部测试的案例运行它们，”公司代表告诉 *The New Stack*。

这些评估器用于衡量 Duet 是否能区分什么值得关注以及什么可以等待，尽管 Anthropic 承认评估这些决策存在困难。

“紧急程度本质上是一个主观的判断，因此我们发现为其构建评估虽然并不完美，但相当有用，”公司代表说。

Duet 可以发现即将到来的截止日期或需要回复的电子邮件等任务，但它并不总是知道哪个任务应该是优先事项，并且该公司承认智能体可能会误解对话或误判紧急程度。Anthropic 的公开推出和支持材料并未说明这种情况发生的频率。

## 测试 Duet 的安全防护

10 月 23 日，即 Duet 首次亮相两天后，Anthropic 发布了对其[安全、隐私和安全防护措施的深入剖析](https://claude.com/resources/articles/claude-duet-safety-privacy-and-security)。Duet 团队负责人 Karan Ahuja 在处理通过消息、电子邮件和公开帖子收到的反馈时，指出了这篇帖子。

Anthropic 将 Duet 中负责执行工作的这部分与检查工作是否符合用户实际要求的那部分分离开来。

“一个独立的自动化检查与每个操作并行运行，该检查基于 Claude Code 中的自动模式分类器并针对 Claude Duet 进行了扩展，”该代表告诉 *The New Stack*。“它评估操作是否符合您的意图。”

由于该检查独立于执行任务的模型运行，Anthropic 表示网页中隐藏的指令无法直接操纵分类器的决策。

Anthropic 表示，一家外部公司对 Duet 进行了渗透测试，但其公开材料并未显示单独的检查在多大程度上可靠地捕获了超出用户意图的操作。相关研究说明了强制执行此智能体范围的难度：研究人员发现，在 Claude Code 测试中[删除定义授权和超出范围操作的提示词部分](https://thenewstack.io/coding-agents-overstep-scope/)会增加超出范围的操作，尽管该研究并未测试 Duet 的独立分类器。

## 限制提示词注入

这种分离旨在减少提示词注入，即嵌入在电子邮件、文档或网页中的恶意指令试图重定向智能体。研究人员已经通过[向流氓智能体留下隐藏消息](https://thenewstack.io/rogue-ai-agent-fleet-tencent/)并观察它们的反应来探索这种风险。Anthropic 的支持材料仍然告诉用户审查草案和批准请求，因为 Duet 可能会遇到提示词注入。

Duet 使用已连接到用户 Claude 账户的应用。断开应用会停止新的访问，但在 Duet 已经存储在记忆中的信息在用户重置之前仍然保留。Anthropic 表示，Duet 从不查看密码、浏览器 Cookie 或登录 Token，也无法将它们保存到记忆中。

Duet 旨在在执行诸如付款或删除项目等操作之前寻求批准。共享私人健康或财务信息需要征得同意，尽管明确要求共享可以算作该同意，而交易证券、在银行账户之间转移资金以及访问其他人的账户则完全属于禁区。

## 摘要，而非监视

用户可以通过其任务列表查看 Duet 已完成的内容和仍在进行的内容，每个作业都有一个单独的页面。他们还可以在智能体工作时为其提供新的指令。

但用户无法看到幕后发生的一切。在研究预览期间，用户无法观看 Duet 在其云浏览器中工作或接管浏览器。用户可以检查其任务活动并批准操作，但他们无法在浏览器步骤发生时对其进行检查。（公开推出和支持材料没有描述跨连接应用撤消已完成操作的方法。）

## 后台工作的成本

Duet 使用与常规 Claude 对话相同的额度，因此后台工作会计入订阅者的计划限制中。它使用多少取决于作业。

“更大的任务，如构建财务模型或演示文稿，将需要更多模型轮次和后台工作，”Anthropic 代表告诉 *The New Stack*。

甚至 Duet 对连接应用进行的常规检查也会计入五小时会话和每周限制中。

这些检查每隔几小时进行一次，而不是连续进行，部分是为了避免用完订阅者的额度。缺点是重要的事情可能会在两次检查之间到达，并且在下一次检查之前被忽视。更频繁地检查会消耗更多资源，而较不频繁地检查可能会让用户等待更长时间才能收到警报。（Anthropic 的公开推出和支持材料没有量化典型订阅者的多少使用量用于后台活动。）

Duet 的研究预览可通过候补名单向美国 Pro 和 Max 订阅者提供。Anthropic 的员工一直在使用它在离开时处理待办事项列表，并在散步时讨论工作负载，尽管 Anthropic 承认智能体在处理订票等消费者任务时没有那么可靠。

随着测试的继续，该公司期望不断调整产品。

[Cyber Security Expert
Step by step guide to becoming a Cyber Security Expert in 2026

Fundamental IT Skills
CTFs (Capture the Flag)
Operating Systems
Networking Knowledge
Certifications
Security Skills and Knowledge
Cloud Skills and Knowledge
Programming Skills](https://roadmap.sh/cyber-security?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=claude-duet-agent-judgment)