<!--
title: Cursor让队友的智能体实现对话
cover: https://cdn.thenewstack.io/media/2026/11/45becf85-mariia-berezovsky-nz3wa499hnm-unsplash-1-1024x576.jpg
summary: 各大AI实验室和编程工具正致力于解决多智能体协作冲突问题。Cursor推出了多人项目功能，允许不同同事的智能体相互直接沟通以协调工作；而Google则推出了Swarm，用于管理单个开发者旗下的智能体集群。尽管这提升了效率，但多智能体协作也面临权限和潜在冲突的安全隐患。
-->

各大AI实验室和编程工具正致力于解决多智能体协作冲突问题。Cursor推出了多人项目功能，允许不同同事的智能体相互直接沟通以协调工作；而Google则推出了Swarm，用于管理单个开发者旗下的智能体集群。尽管这提升了效率，但多智能体协作也面临权限和潜在冲突的安全隐患。

> 译自：[Cursor gets teammates’ agents talking](https://thenewstack.io/cursor-google-multiplayer-swarm/)
> 
> 作者：Paul Sawers

编码智能体非常擅长[并行工作](https://blog.pragmaticengineer.com/new-trend-programming-by-kicking-off-parallel-ai-agents/)：一个编写新的 API 端点，另一个更新测试，而第三个则修复代码库中其他地方的 Bug。然而，它们不太善于了解各自的同行在做什么——将几个智能体放在一个项目上，它们就会重复工作、干涉彼此的更改，并留下一位开发者去应对随之而来的混乱局面。

这就是为什么各大 AI 实验室和编码工具制造商一直在寻找方法来为其智能体舰队带来秩序，尽管它们采用了略有不同的方法。

就在本周，Google 和 Cursor 都推出了旨在防止智能体互相冲突的功能，但规模不同。Google 的 [Swarm](https://antigravity.google/docs/swarm/) 组织了为单个开发者工作的智能体，而 Cursor 的多人 [Projects](https://cursor.com/docs/agent/projects) 则让为不同同事工作的智能体能够相互协调。

## Cursor 让队友的智能体实现对话

Cursor [早在 9 月份就首次推出了 Projects 功能](https://thenewstack.io/openai-cursor-coordinator-agents/)，为开发者提供了一种将较大工作交给协调者智能体的方法，该智能体将其分解为任务并委派给工作者智能体。

然后在周二，这家在 8 月份被埃隆·马斯克的 SpaceX 以 600 亿美元[收购](https://cursor.com/blog/joining-spacex)的公司，为 Projects [推出了多人协作功能](https://cursor.com/blog/projects-multiplayer)。开发者现在可以邀请队友加入项目，每个人都拥有自己的协调者和工作者。

![多人协作登陆 Cursor Projects](https://cdn.thenewstack.io/media/2026/11/7bbd71dd-gify.gif)

*Cursor 协调者在队友的任务之间交换消息。*

每个人的智能体都在同一个任务看板和项目文档上工作，它们的协调者可以直接互相发消息以分享计划、标记重叠部分等等。

> 归根结底，这一切都是为了减少开发者自己必须进行的协调工作。

归根结底，这一切都是为了减少开发者自己必须进行的协调工作。如果一个队友的智能体正在更改数据库架构，而另一个队友的智能体正在构建依赖于它的功能，它们的协调者可以就哪个更改需要先落地达成一致。

就 [Antigravity](https://antigravity.google/) 而言，它是 Google 对标 Cursor 的产品。Google 在这里整合了各种其他的编码工具，将[单独的 Gemini CLI 用户迁移到了 Antigravity](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)，并开始[关闭](https://x.com/julesagent/status/2115883717705261283)其后台编码智能体 Jules。

在 Cursor 推出多人 Projects 的同一天，[Google 在 Antigravity 中推出了](https://thenewstack.io/gemini-4-carbon-swarm/) Gemini 4 Carbon，并预览了其协调编码智能体的方法。该功能被称为 Swarm（风格化为 /swarm），它允许开发者将一个任务交给协调者，协调者随后将其拆分给工作者智能体，并指定一个验证者来检查它们的更改。工作者可以在共享看板上互相发消息，以便在进行过程中协调他们的更改。

例如，一家想要更改其在线结账系统如何验证 Token 的公司可以使用 Swarm 来拆分工作。一个智能体更新身份验证中间件，而另一个智能体更新 Token 验证器。它们可以在独立的 Git 工作树中工作，使用看板就它们的更改如何组合在一起达成一致，并将它们交由验证者进行测试。

![Swarm 智能体拆分并验证 Token 迁移。](https://cdn.thenewstack.io/media/2026/11/131f3ae2-swarmgif2.gif)

*Swarm 智能体拆分并验证 Token 迁移。*

Google DeepMind 软件工程总监 [Varun Mohan](https://www.linkedin.com/in/varunkmohan/) 周二在 X 上表示，Swarm 为开发者提供了一种方便的方法，可以将多个智能体投入到复杂的任务中，并补充说 Google 员工已经在内部使用 Swarm 来承担更大的工作。

Mohan [写道](https://x.com/_mohansolo/status/2120290178267074884?a=YCRGLGGQfIn70qM6izk&s=20)：“使用智能体集群（swarm）带来的优势大得离谱。我们有人使用数百个智能体的集群，仅凭一个提示词就能从头开始构建大型系统和产品。”

Google DeepMind 的技术人员 [Logan Kilpatrick](https://www.linkedin.com/in/logankilpatrick/) [在 X 上表示](https://x.com/OfficialLoganK/status/2120190972495814893?a=oL4-x5gctabWoetNdBY&s=20)，看到智能体集群的输出“真的让人印象深刻”，并且它们为“AI 提供了一个新的扩展维度！”

> “AI 的一个新扩展维度！”

归根结底，这触及了这些公司中每一家如何处理智能体协调的**核心**。

## 当智能体为不同的人工作时

Antigravity 的 Swarm 接受一个开发者的任务，并让处理它的智能体在工作时进行交流。与此同时，Cursor 的多人 Projects 接受来自不同队友的任务，并让他们的协调者跨这些任务进行交流。

这就是 Cursor 产品经理 [Aryaman Khandelwal](https://www.linkedin.com/in/aryamank/) 在[周二的公告](https://cursor.com/blog/projects-multiplayer)中急于指出的区别。

> “到目前为止，多智能体系统只服务于一个人。Projects 是为整个团队构建的多智能体系统。”

Khandelwal 写道：“到目前为止，多智能体系统只服务于一个人。Projects 是为整个团队构建的多智能体系统。”

简单浏览一下 AI 编程领域就会发现其他人是如何处理智能体协调的——包括 Anthropic。其仍处于实验阶段的 [Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) 为致力于共同任务的智能体提供了共享的任务列表和互相发消息的方法。最近，该公司为 Claude Code 添加了[跨会话消息传递](https://code.claude.com/docs/en/cross-session-messaging)，因此可以单独启动的会话可以交换发现或互相警告更改。但这些会话仍然属于同一个开发者。

10 月，[GitHub 将 Copilot 应用中的 Projects](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases/) 置于公开预览阶段，为开发者提供了一种将跨代码仓库的目标交给 Copilot 并将工作分发给智能体的方法。与此同时，AWS 的 Kiro Crew 机器人于[上周发布](https://kiro.dev/blog/crew-bots/)，可以启动多个会话，在它们运行时进行引导并将它们的结果汇总在一起。

另外，Anthropic 和 OpenAI 还构建了队友可以共同使用的智能体。Anthropic 在 6 月[推出了 Claude Tag](https://thenewstack.io/anthropic-claude-tag-slack/)，允许 Slack 频道中的人们委派给共享的 Claude。OpenAI 的 ChatGPT 工作空间智能体于 [4 月宣布](https://thenewstack.io/openai-shared-workspace-agents/)，可供多位同事使用和维护。

然而，社区中的[一些人](https://x.com/geilt/status/2120329106881499296?a=39yIT4-bELHfydq1hRo&s=20) [提出了担忧](https://x.com/avisinghdotdev/status/2120297515379834999)，即让队友的智能体进行对话可能会将一个智能体的错误传播到整个团队，特别是如果每个人的智能体遵循不同的规则，并且智能体可能会请求它不应访问的信息。不过，Khandelwal [回应称](https://x.com/aryamankhawow/status/2120309976052752842)，多人 Projects 允许团队为项目中的**所有人**定义共享规则和技能。在访问权限方面，Cursor 的[文档](https://cursor.com/docs/agent/projects)指出，智能体将来自队友智能体的信息视为不受信任的输入，并在分享个人的私有文件或连接器数据之前进行询问。队友的消息在单独的聊天中处理，Cursor 表示该聊天从不共享机密或凭据。Projects 文档并未说明管理员是否可以根据队友的角色为这些交流设置不同的规则。

另外，最新研究表明，每个用户拥有各自智能体的团队可能会陷入困境。在 [周三发布的一项研究中](https://alignment.anthropic.com/2026/worse-together/)，Anthropic 奖学金计划的研究人员测试了当多个用户各自委派给自己的智能体并且这些智能体共享资源时会发生什么，测试在四个模拟环境中进行，其中包括代码合并队列。在每个环境中，群体的结果都比单个智能体为所有人服务时更差，对于 Anthropic 的 Claude 模型而言，差距大约在 10 到 45 个百分点之间，即使每个用户的智能体可以互相发消息也是如此。随着团队规模的扩大，智能体会陷入停滞、覆盖其他用户的请求，并对其他人想要什么做出毫无根据的声明。一些修复方法有所帮助，例如指派首席智能体或阻止智能体在阅读消息之前采取行动，但哪些方法有效取决于任务。

总而言之，今年发布的这些产品表明，各方都在推动使团队更容易委派工作并跟踪其智能体正在做的事情。通过 Projects 中的多人模式，Cursor 正在解决该问题的一个特定部分。

Cursor 母公司 SpaceXSI 的工程人员 [Parker Smith](https://www.linkedin.com/in/parkersm1th/) 表示，关键其实在于让智能体保持前进，而不会产生不必要的延迟。

Smith [在 X 上写道](https://x.com/parkersmith/status/2120300502260871295?s=20)：“智能体行动迅速，对同行上下文设置阻塞太慢了。多人项目允许你的智能体从你同事的智能体那里获取所需的所有上下文，而无需麻烦你。”

Cursor 的多人 Projects 目前正面向团队账户用户进行测试版公测，而 Google 的 Swarm 则面向 Google AI Pro 和 Ultra 订阅者进行预览。