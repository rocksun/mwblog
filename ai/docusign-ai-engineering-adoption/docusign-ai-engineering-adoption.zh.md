![几只手引导着一支超大的钢笔、画笔和铅笔在画架上画一颗心，展示团队协作](https://cdn.thenewstack.io/media/2026/11/83c51965-ghariza-mahavira-5biac69ve_g-unsplash-1024x768.jpg)

**Docusign 在其工程团队中全面推广了 AI 编码工具，期望它们能帮助开发者更快地编写代码并完成更多工作。最初的热情很高，但早期的增长势头随后趋于平缓。**

到 2025 年 6 月，Docusign 遇到了瓶颈。根据其[工程团队的复盘](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it)，49% 的工程师在使用 AI 编码工具，而据报道开发者生产力提升 18% 的增长势头已经停滞。工程师仍然需要时间去实验、需要契合 Docusign 代码库的指导，以及将这些工具融入日常工作的帮助。

Docusign 现在报告称，其全部 1,100 多名工程师都已经接入并积极使用 AI 编码工具。

![Sagnik Nandy，Docusign 首席技术官](https://cdn.thenewstack.io/media/2026/10/5e11eb07-docusign-cto.jpeg)

Docusign 首席技术官 Sagnik Nandy

CTO [Sagnik Nandy](https://www.docusign.com/blog/author/sagnik-nandy) 认为，让人们使用这项技术仅仅是个开始。

“要想取得几次胜利与持续正确地做好这件事之间有着巨大的差异，”Nandy 告诉 *The New Stack*。

Docusign 的应对之策是改变其在工程部门引入和衡量 AI 的方式，从单纯的编码助手转向可重用的智能体和自动化工作流。

## **为什么 Docusign 将目光投向了自己的工程师**

Docusign 没有强制推行 AI，而是成立了一个由 6 人组成的工程 AI 冠军团队（Eng AI Champions），负责制定护栏、分享工程实践并举办研讨会。Docusign 报告称，截至 2025 年 10 月，AI 普及率达到了 65%。随后，该公司通过嵌入各个开发团队的 AI 促进者（AI Multipliers）将这一工作进一步推向深入。Nandy 表示，大约 75 名促进者帮助队友落实共享实践，并将遇到的问题反馈给核心团队。

“他们的任务有两项，”Nandy 解释道，“他们做出的决策和构建的解决方案，必须在自己的团队内部部署，同时要收集反馈，了解哪些行之有效、哪些行不通、还缺少什么。”

Docusign 的[相关文章](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it)显示，在引入促进者后两个月内，[活跃使用率达到了 93%](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it)，而每个开发者更新的代码行数比公司初期增加了约 52%。单凭这一代码量指标，并不能直接证明交付速度或软件质量有同步提升。

Nandy 相信，核心统筹与来自各个团队的反馈相结合，有助于维持该项目的长久运行，他在一次[工程领导力播客](https://sfelc.com/podcasts/best-practices-for-scaling-ai-adoption-across-a-large-org-and-the-trade-offs-you-will-have-to-make-sagnik-nandy-docusign)中也探讨过这种方法。

> “当我与许多同行交流时，发现很多 AI 项目都是开局良好，随后却不了了之。”

“当我与许多同行交流时，发现很多 AI 项目都是开局良好，随后却不了了之，”他说。“我认为我们没有出现这种情况的原因……是因为我们已经拥有了如此丰富的信息和反馈流，人们在根据这些反馈采取行动并重新部署。”

## **教 AI “说 Docusign 的语言”**

一旦工程师们习惯了使用 AI 进行编码，Docusign 便开始审视整个开发工作流。这需要让工具访问其代码库、架构、可观测性和内部实践，以便助手能够结合公司的自身语境来工作。

“我们开玩笑说，我们的解决方案和智能体都会说 Docusign 的语言，”Nandy 说。“它们知道应该查阅哪些内部工具、我们的内部编码护栏和准则是什么、我们做出怎样的系统选择、以及不同信息存放在哪里以便进行区分。”

Nandy 介绍了针对不同工程任务的几种内部工具：用于特定 Docusign 编码工作的 Kody、用于可观测性和事件调查的 Chronicle，以及用于代码感知内部文档的 DocuWiki。Docusign 的[工程博客](https://www.docusign.com/blog/how-we-drove-ai-adoption-across-docusign-engineering-without-mandating-it)还介绍了一种 AI 辅助的代码审查工具，用于在审查期间识别潜在的架构和安全问题。

[Krew 将这些功能整合在一起](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates)，允许团队为重复性任务和更复杂的工作流构建名为 Krewmates 的智能体。

“工程 AI 冠军团队和促进者所做的事情之一，就是识别端到端的工作流，而我们希望改善整个流程，”Nandy 说。

他描述了一个在夜间运行的内部智能体，它会搜索错误日志中的问题并准备好修复建议。

“到了早晨，工程师迎来的会是：‘嘿，这里有一个 PR。这是我们发现的问题，这是修复方案。’这太神奇了。”

在 Nandy 的例子中，Krew 协调工作流，利用了 Chronicle 的可观测性和 Kody 的编码功能。随后，工程师会审查所提出的拉取请求（PR）。

Docusign [给出了另一个例子](https://www.docusign.com/blog/how-we-built-an-autonomous-coding-agent-for-repetitive-engineering-tasks)。对于涉及基础设施配置文件的一项任务，该智能体以一个提交（commit）作为指导，在第一次运行中大约 15 分钟内正确修改了 12 个文件中的 10 个。该公司表示，这一过程以前大约需要耗费工程师一周的时间。在第一次运行时，仍有两个文件需要修正；它并不是在 15 分钟内就能直接完成并获得批准的变更。

## **让成功的工作流可复用**

如果其他人不得不重新创建，那么为一个团队构建的智能体其价值就会非常有限。

Docusign 的 [Krew 编排平台](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates)允许工程师发现、复制和扩展连接到内部系统的 Krewmates。这些智能体可以处理重复性任务、响应触发器，并在需要时让人工介入。

“我们采取了一种非常开放的方法，”Nandy 说。“所有的 Krewmates 对所有人都是可见的。你可以看到它们的被使用频率。复制和扩展它们极其简单。”

经常被使用的 Krewmates 会获得更高的可见度，从而帮助团队找到现有的解决方案，而不是从头开始构建自己的方案。

> “如果某样东西很好，你可以试着教其他 1,000 个人去做，或者你可以让其他 1,000 个人极其轻松地继承它。”

“如果某样东西很好，你可以试着教其他 1,000 个人去做，或者你可以让其他 1,000 个人极其轻松地继承它。而我们选择了后者。”

这种方法还取决于维护这些共享工具、记录变更，并将问题反馈给负责改进它们的团队。Docusign 的 [Krew 团队报告称](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates)，表面上运行成功的任务有时会留下重复的提交或部分输出，这促使他们改进了运行追踪和可观测性。对于采用这种模式的领导者来说，一个持久的工作流需要一个指定的所有者、报告故障的途径，以及对质量和运行成本的定期检查。

## **衡量重要的事情**

Docusign 的采用率数据展示了 AI 普及的广度，但 Nandy 警惕将使用率视作成功的终极指标。

“我们非常关注价值，而不是奇闻轶事或噱头，”他说。“做到这一点的途径就是不断向价值链的上游移动。”

最初，Docusign 衡量的是有多少工程师在使用 AI，接着是他们生成了多少代码。Nandy 表示，接下来的问题涉及团队是否在真正交付更好的成果。

“普及率，那又怎样？……你们做出的成果更多了吗？”他说。“然后你要看功能交付速度。你们发版的速度更快了吗？”

Docusign 还考虑客户满意度和可靠性，特别是更快的开发是否会引入其他问题。

对工程领导者而言，这意味着要检查交付时间、审查延迟、测试、返工和事件调查，而不是仅仅依赖采用率的百分比或 AI 生成的代码行数。

## **速度之前先设护栏**

赋予智能体更多责任并不意味着消除人类的问责制。

“任何 PR，签字背书的个人都要承担责任，”Nandy 说。“没有任何未经审查的代码能进入系统。”

Docusign 表示，其自主编码智能体在提交拉取请求之前会运行测试，合并前需要人工审查、AI 生成代码标签和质量关卡。其[AI 创新原则](https://www.docusign.com/products/platform/ai/innovation-principles)强调了人工监督和保障措施。[Krew 的文档](https://www.docusign.com/blog/every-team-deserves-a-krew-the-platform-behind-docusigns-220-ai-teammates)明确了边界：如果没有人的批准，智能体不能合并拉取请求或采取不可逆转的行动。

Nandy 将 AI 比作链锯：这是一种功能强大、能比传统替代方案完成更多工作的工具，但也需要适当的安全保障。

> “当你拥有链锯时，你需要非常不同的防护装备，否则你会伤到自己。”

“当你拥有链锯时，你需要非常不同的防护装备，否则你会伤到自己，”他说。“把这一点做好至关重要。”

他还警告不要在传统软件能做得更好的地方盲目引入 AI。Docusign 的某些内部解决方案虽然是用 AI 开发的，但作为确定性流程运行，而不需要持续调用模型。

“我经常看到人们把 AI 生搬硬套到那些可能根本不需要 AI 的问题上，”Nandy 说。

## **超越全面推广**

对 Nandy 而言，Docusign 的方法基于五项原则：衡量价值、让成功的解决方案可复用、保持成本和治理的可持续性、建立护栏并融入组织自身的语境。

这些原则共同支持了一种转变：从鼓励工程师尝试 AI 转变为团队可以跨部门维护、衡量和改进的工作流。对于工程领导者而言，切实的下一步是选择一个定义清晰的工作流、就要衡量的结果达成一致、指派所有者，并在扩展之前明确需要人工批准的环节。

给工程领导者的教训是，单靠普及并不能带来持久的成果。团队还需要共享工具、清晰的所有权、工程师反馈以及能够显示工作是否真正变得更好的衡量标准。

更多详情可在 Docusign 的[工程博客](https://www.docusign.com/blog/topics/engineering)以及当前的[工程招聘机会](https://careers.docusign.com/careers-home/jobs/categories/Engineering)中找到。

### *The New Stack* 上的更多 Docusign 相关文章

这篇文章[从 AI 普及走向 AI 运营模式：Docusign 工程团队如何超越工具推广](https://thenewstack.io/docusign-ai-engineering-adoption/)最初发布在 [The New Stack](https://thenewstack.io)。