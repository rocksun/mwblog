[Anaconda](https://www.anaconda.com/) 是一家为企业提供受控开源软件包和环境的公司，目前已收购了热门的开源代码代理工具 [Kilo](https://kilo.ai/)。

这笔交易发生在一个工业界普遍警惕被单一 AI 提供商锁定的时刻。仅在过去 10 天里，[Palantir 的 Alex Karp 和 Mistral 的 Arthur Mensch](https://thenewstack.io/karp-mensch-ai-lockin/) 就警告称，封闭模型提供商对企业数据和工作流拥有过大的控制权，而微软的 Satya Nadella 也[提出了](https://thenewstack.io/nadella-reverse-information-paradox/)类似的观点。

正是在这样的背景下，Anaconda 将 Kilo 纳入旗下。

Anaconda 于 2012 年在德克萨斯州奥斯汀成立，是广泛使用的同名 Python 发行版和包管理器的幕后公司——这一工具在过去十多年里帮助数据科学家和企业管理 Python 环境，免受依赖项冲突的困扰。它通过说服企业信任内部部署的开源工具来建立业务，并在 2025 年 5 月[将这一理念推向了 AI 领域](https://thenewstack.io/pythons-open-source-dna-powers-anacondas-new-ai-platform/)，推出了一款旨在为企业提供受控、安全的模型与 AI 开发平台。

该产品的发布恰逢一轮 [1.5 亿美元以上的融资](https://www.anaconda.com/press/anaconda-raises-150m-series-c-funding-ai-enterprise)，使公司估值达到约 15 亿美元。

> “目前，大多数企业面临两种错误选择：要么锁定在单一工具和模型提供商上，要么让开发者随心所欲地使用任何工具，却没有任何可观测性。这两种都不是真正的战略。”

[David DeSanto](https://www.linkedin.com/in/ddesanto/) 在 GitLab 担任了六年首席产品官后，于 2025 年 10 月[加入 Anaconda 担任 CEO](https://www.anaconda.com/press/anaconda-names-new-chief-executive-officer)。他向 *The New Stack* 表示，企业最终陷入了两个极端——完全锁定或完全失控。

“目前，大多数企业面临两种错误选择：要么锁定在单一工具和模型提供商上，要么让开发者随心所欲地使用任何工具，却没有任何可观测性，” DeSanto 说道。“这两种都不是真正的战略。”

## 每一个 Kilo 都至关重要

Kilo 于 [2025 年 3 月](https://blog.kilo.ai/p/kilo-code-speedrunning-open-source-coding-ai)发布，由 GitLab 联合创始人兼前 CEO [Sid Sijbrandij](https://www.linkedin.com/in/sijbrandij/) 创立，Jan Paul Posma 担任创始 CEO。Posma 因个人原因于 9 月退居幕后，将职位交给了目前领导公司的 [Scott Breitenother](https://www.linkedin.com/in/scottbreitenother/)。Kilo 的[核心卖点是中立性](https://www.forkable.io/p/kilo-an-open-source-coding-agent)：Kilo 不会强迫开发者绑定某个 AI 实验室的模型，而是让他们接入任何想要的提供商——OpenAI、Anthropic、Google、Mistral 或自托管模型——并随着价格或性能的变化自由切换。该项目在 GitHub 上建立了相当大的影响力，拥有超过 [26,000 个 Star 和 3,000 个 Fork](https://github.com/kilo-org/kilocode)。

持有这种主张的不仅仅是 Kilo。[OpenCode、Cline 和 Aider](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/) 等工具通过位于模型之上，为开发者提供了一种规避不可预测的 Token 账单和供应商锁定的方式，从而获得了关注。值得注意的是，Kilo 本身是 VS Code 的开源 AI 代码代理 [Roo Code](https://github.com/RooCodeInc/Roo-Code) 的一个分支。当 [Roo Code 为了转型为纯云端代理而停止维护其 IDE 扩展](https://thenewstack.io/roo-code-cloud-ides-ai-coding/)时，这引发了一波用户寻找替代品的需求，而 Kilo 将自己定位为承接这些用户的目的地。这种需求是双向的：今年 6 月，Cursor [收购了 Continue](https://thenewstack.io/cursor-acquires-continue-coding/)，这是另一款开源、模型无关的助手，将该类别早期的标杆产品之一并入了一个封闭的商业 IDE 中。

总而言之，这说明了技术栈的这一层竞争有多么激烈。而 Anaconda 正在争取它的一席之地。

## 万亿 Token 的问题

Kilo 的数据在一定程度上解释了 Anaconda 为何想要收购它：超过 300 万开发者每月通过该平台路由近 10 万亿个 Token，覆盖了 60 多家提供商的 500 多个模型。

> “规模不是问题，治理才是。”

对于 DeSanto 来说，这一规模证明了开发者希望拥有选择自己模型的自由。然而，这种证明伴随着企业急于弥补的治理缺口。

“规模不是问题，治理才是，” DeSanto 解释道。“企业 AI 支出的增长速度超过了任何人的核算能力，在数十种工具、工作账号和个人账号中隐形堆积。”

DeSanto 指出了所谓的“[tokenmaxxing](https://thenewstack.io/lanai-token-tuner-tokenmaxxing/)”现象——将 AI Token 使用量视为生产力的指标，而没有任何与使用目的相关的实际关联。DeSanto 表示，如果不加约束，这种习惯会让企业像盲人摸象：消耗了预算却无法判断哪些有效、风险在哪里，或者这一切是否得到了回报。

“大多数企业也完全依赖于单一模型提供商，这种赌注在任何其他对业务至关重要的领域，企业都不会去做，” DeSanto 补充道。

> “大多数企业 […] 完全依赖于单一模型提供商，这种赌注在任何其他对业务至关重要的领域，企业都不会去做。”

## Kilo 的下一步

展望未来，Anaconda 计划将 Kilo 整合到现有的 AI 工作区中，同时保持 Kilo 受欢迎的开发者体验。

开发者将像往常一样在 VS Code、JetBrains 和 CLI 中工作，但背后默认集成了 Anaconda 经过审查的软件包、受控模型和 AI 编排功能。在接下来的 12 个月里，这种集成将进一步深化，将 Kilo 连接到 Anaconda 的编排和治理工具，使项目能够从开发者编写代码到代码在生产环境中运行，无需切换平台，且在每个阶段都适用相同的组织策略。

“我们的愿景是一个统一的平台，构建者无需在速度和治理之间做出选择，” DeSanto 说。

> “企业不想被锁定在单一模型提供商上，开发者肯定也不想。”

DeSanto 将 Kilo 的开源、无锁定模型称为 Anaconda 未来战略的“根本”，作为交易的一部分，Anaconda 接管了 Kilo 的 GitHub 组织和开发者社区的管理权。

“企业不想被锁定在单一模型提供商上，开发者肯定也不想，” 他说。“我们打算在投资其与 Anaconda 平台集成的同时，继续支持 Kilo 作为开源项目。”

Kilo 并不是 Anaconda 正在整合的唯一开源组件。早在 4 月份，[它就收购了 Outerbounds](https://thenewstack.io/anaconda-ai-outerbounds-python-metaflow/)，这是 Metaflow 的幕后公司，Metaflow 是一种源自 Netflix 的编排框架。如果说 Kilo 处理的是编写代码的时刻，那么 Outerbounds 则负责治理代码如何在生产环境中可靠运行——现在这两者都包含在同一个 Anaconda 产品中。

“将这些能力置于一个平台之下非常重要，但更重要的是，它们全部连接为一个无缝、连续的体验，” DeSanto 说。“企业现在拥有了一条通往生产的连续路径，而不是拼凑零散的 AI 工具。开发者可以快速行动，同时提供大规模运营所需的治理、可观测性和控制能力。”"}
我是什么工具？我想了解更多关于这方面的信息。
</h3>
要了解更多，请关注我们的YouTube频道以获取播客、采访、演示等内容。"}
</h3>
Paul 是一位资深的科技记者，报道范围涵盖欧洲及其他地区的重大新闻，近期曾供职于 TechCrunch，报道初创企业、企业应用、大型科技、基础设施、开源、AI、监管等内容。Paul 现居伦敦...

阅读更多来自 Paul Sawers 的文章](https://thenewstack.io/author/paul-sawers/)"}
