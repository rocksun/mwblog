<!--
title: 代码审查正在消磨你最优秀的工程师
cover: https://cdn.thenewstack.io/media/2026/09/04b2c425-martin-sanchez-21m9ltgr-wm-unsplash.jpg
summary: 文章探讨了 AI 生成代码如何导致工程师陷入无休止的审查压力中。随着审查负担加重和 AI 代码意图缺失，顶尖工程师面临离职风险。作者建议通过将重复性工作自动化、保留决策意图并重塑衡量标准来解决这一瓶颈。
-->

文章探讨了 AI 生成代码如何导致工程师陷入无休止的审查压力中。随着审查负担加重和 AI 代码意图缺失，顶尖工程师面临离职风险。作者建议通过将重复性工作自动化、保留决策意图并重塑衡量标准来解决这一瓶颈。

> 译自：[Code review is burning out your best engineers](https://thenewstack.io/ai-code-review-burnout/)
> 
> 作者：Ankit Jain

我交流过的每一个团队都面临着同样的问题。他们最优秀的工程师——那些最关心代码质量的人——正被淹没在他们无法跟上且并不享受的审查队列中。一些资深工程师抱怨连连，甚至直接[拒绝审查 AI 生成的代码](https://www.reddit.com/r/ExperiencedDevs/comments/1towli9/today_i_announced_that_i_wont_be_reviewing_ai/)。

我运营着一个由资深工程师和工程负责人组成的[社区](https://dx.community/)，他们都将 AI 代码审查瓶颈列为最关心的问题之一。在[一项研究](https://annievella.com/posts/the-software-engineering-identity-crisis/)中，77% 的工程师表示他们现在花在编写代码上的时间减少了，转而将时间投入到审查 AI 的输出上。

## 工作重心从创作转向了验证

采用 AI 程度较高的团队合并了 [98% 更多的 PR](https://www.faros.ai/blog/how-ai-coding-tools-impact-software-engineering)，而审查时间增加了 91%。[工程师们并没有报名参加整天阅读机器生成的 diff 的工作](https://thenewstack.io/survey-engineers-want-to-code-but-spend-all-day-on-tech-debt/)，但这正是工作越来越要求的。

感受最深的是那些并没有抵制 AI 的工程师，而是那些最早采用它、最关心代码质量并建立了团队所依赖的审查文化的人。这些人每天队列里有 15 个 PR，每个 PR 有 400 行代码。

## 为什么审查 AI 生成的代码更难

当同事编写代码时，意图会伴随审查过程。他们可以解释所考虑的权衡、拒绝的替代方案以及在哪些限制条件下工作。即使这些没有写下来，这种背景信息也是可获取的。

> “当 AI 编写代码时，推理过程消失了。审查者只能从 diff 中逆向推导意图。”

当 AI 编写代码时，推理过程消失了。审查者只能从 diff 中逆向推导意图。这是一种本质上不同的认知任务。更糟糕的是，AI 生成的[代码往往能通过简单的目测](https://thenewstack.io/go-language-ai-agents/)。

### AI 生成代码的五种弊端

**看起来合理但有误。** 代码读起来很连贯，逻辑通畅，但边缘情况暴露了错误的假设。这些 Bug 在审查中很难发现，因为它们需要理解代码原本应该做什么，而不仅仅是它现在做了什么。

**过度工程。** AI 模型在海量代码上进行训练，包括企业模式和生产环境加固的架构。当被要求解决一个真正只需要 15 行代码的问题时，模型可能会生成一个 200 行的抽象层，预见了一个没人需要的通用性。

**无视约定。** 模型生成的是良好的通用代码，而不是适合你系统的代码。你的仓库有关于命名、错误处理、日志模式、模块边界的约定，AI 经常忽略它们。

**自信地产生幻觉。** 调用不存在的 API，使用已弃用的方法，编造配置选项。有时会被立即发现，有时只能在生产环境中才发现。

**盲目模仿模式。** 不明就里地复制结构。在不需要重试的地方使用重试逻辑。对总是同步的调用使用熔断器。看起来很全面但无法映射到实际故障模式的错误处理。

共同点是它们看起来像真正的代码，这使得在大规模场景下很难进行审查。

## 如何修复代码审查

答案不是“更努力地审查”或“添加一个 LLM 审查员”。当同一个模型编写并审查代码时，它会共享自己的盲点。如果你添加对抗性智能体和多个步骤，这个过程就会变成一场多步骤工作流的“戏剧”，使工程师变成“机器人保姆”，将时间花在配置和调整过滤器上，而不是创造价值。

有效的方法是在三个方面[减轻审查者的负担](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)：将重复的反馈代码化、保留产生代码的意图，并衡量那些真正防止低质量输出的工作。

### 创建你的 AI 低质量输出登记表

提取你团队最近 100 个 PR 的审查评论。对每一个进行分类：它是确定性的、可以用规则检查的吗？它是可以通过执行测试验证的吗？还是真正的判断性工作？

当团队进行这项练习时，大致比例为：45% 是确定性的，30% 是可执行测试的，25% 是判断性的。四分之三的审查反馈是可以代码化的。

> “四分之三的审查反馈是可以代码化的。每一个反复出现的审查评论都是一个你尚未编写的恒量。”

每一个反复出现的审查评论都是[一个恒量](https://docs.aviator.co/verify/concepts/invariants)，你只是还没把它写出来。“新端点必须具有 OTel 跨度”这不是判断问题，而是一个 AST 检查。写一次，就再也不需要审查员了。将某项内容提升为恒量的测试是重复性：如果你发表过不止一次相同的评论，它就应该被代码化。

### 保留推理轨迹

生成代码的提示词（prompts）和智能体会话包含了意图。大多数团队扔掉了它们。这就像删除了提交消息（commit messages）和 PR 描述，却指望审查员仅从 diff 中重建意图。

在 Aviator，我们围绕这个问题构建了 [Verify](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)。它从提示词和会话中捕获意图，并将其构建为[验收标准：](https://thenewstack.io/ai-codebase-maturity-model/)变更的内容、范围之外的内容以及如何判断其是否有效。工程师在与智能体对话时做出的决策、架构选择、范围界定、行为权衡，都变成了可审查的验收标准。

审查员阅读[验收标准列表](https://docs.aviator.co/verify/concepts/how-verification-works?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness)，并询问：“我们是否在正确的约束条件下解决了正确的问题？”这对资深工程师来说是高价值的工作，而不是在下午 4 点阅读 400 行的 diff。代码实际上是[审查中最不重要的部分](https://www.aviator.co/blog/move-code-review-before-the-code/)。重要的是意图：验收标准、非目标、影响范围。

### 知识共享如何延续

审查员阅读规范和验收标准是在阅读决策，而不是扫描语法。他们在辩论权衡，了解系统是如何演进的，并观察是什么样的约束塑造了当前的方法。这就是知识共享得以延续的地方。如果我们把代码审查前置，[知识共享也必须前置](https://thenewstack.io/ai-code-review-cognitive-debt/)。

### 衡量并奖励验证工作

[31% 的 PR](https://www.faros.ai/blog/ai-software-engineering) 正在没有任何审查的情况下被合并。这是工程师在用行为投票。

衡量 AI 采用率和代码行数生产力的仪表盘永远无法显示资深工程师承担审查负担的工作。它们永远无法呈现为构建防御机制和护栏所付出的努力。如果你只衡量吞吐量和周期时间并感到满意，那么你衡量的是错误的事情。

Annie Vella 一直在[追踪这种转变](https://annievella.com/posts/the-productivity-experience-paradox/)，对象涵盖 28 个国家的 158 名工程师。她的观察是：工程师正在辞职，一些人希望角色能回到过去，另一些人则完全离开了这个行业。向繁重的验证工作转变，正在使这项工作变得令他们不再享受。

> “这些仪表盘没有显示那位花了一下午时间逆向推导意图的资深工程师。它们显示的是吞吐量。而吞吐量看起来很棒，直到那些承担审查负担的人离职为止。”

承担审查负担的工程师不是在抱怨，他们是在离职。一些人离开了去往拥有更好工具的团队。一些人完全离开了工程领域，不是因为他们无法跟上，而是因为工作不再是他们当初签约时想要从事的那种工作了。

追逐代码行数和 PR 合并数量的领导者永远不会预见这一点。这些仪表盘看不到那位花了一下午时间从 400 行 diff 中逆向推导意图的资深工程师。它们看不到在进入生产环境前阻止了错误模式的审查。它们只显示吞吐量。而吞吐量看起来很棒，直到那些承担审查负担的人离职为止。

[修复代码审查流程。](https://www.aviator.co/verify?utm_source=tns&utm_medium=content&utm_campaign=q3-2026-tns-verify&utm_term=net-new&utm_content=awareness) 将重复的内容代码化，保留推理轨迹，并衡量那些真正防止低质量输出的工作。否则，你会看着你最优秀的工程师离开，并纳闷为什么你的 AI 驱动团队交付速度更快了，却出现了更多的问题。