![描绘智能体集群的插图。](https://cdn.thenewstack.io/media/2026/11/2530ee0a-getty-images-0gfedlukaji-unsplash-1024x683.jpg)

智能体集群（Agent swarms）正风靡一时，各家公司纷纷开始探索如何协调多个 AI 智能体并行处理复杂任务。

仅在过去一周内，[Google 和 Cursor 就先后发布了](https://thenewstack.io/cursor-google-multiplayer-swarm/)相互竞争的多智能体编程方案，而此前包括 Anthropic 在内的多家公司也已有所布局——Anthropic 推出的[实验性 Claude Code 智能体团队](https://code.claude.com/docs/en/agent-teams)功能便允许多个智能体协作完成开发任务。OpenAI 也一直在探索[面向智能体的共享工作区](https://thenewstack.io/openai-shared-workspace-agents/)。

本周二，Replit 宣布推出新产品 [Missions](https://replit.com/missions)，进一步顺应这一趋势。该产品允许用户设定目标、制定预算和审批要求，并部署 AI 智能体集群在数小时、数天甚至数周内持续推进任务。

## Replit Missions 的工作原理

从核心来看，Missions 是一种将复杂项目委托给 AI 智能体的方式，由智能体自行决定如何以最佳方式实现既定目标。用户通过 Replit 所谓的“任务协议（Mission Agreement）”来设定参数，其中明确了成功标准、支出上限以及需要人工审批的操作。

使用时，用户只需在对话中输入 `/mission`，并用自然语言描述目标即可，例如让网站上的每个页面在 500 毫秒内加载完成。

![启动任务](https://cdn.thenewstack.io/media/2026/11/9a01b3db-gif4.gif)

*启动任务*

关键在于，用户无需事先制定详尽的计划，从而赋予智能体充分的自主权，去探索解决问题的最佳途径，并在推进过程中动态调整方法。

Replit 总裁 [Michele Catasta](https://www.linkedin.com/in/pirroh/) 表示，这是一个非常刻意的设计选择，因为要求用户提前规划好每一步反而会限制智能体寻找高效解决方案的能力。

> “那样会迫使人类去操心实现细节，而无法赋予 AI 系统实现复杂目标所需的灵活性。”

“那样会迫使人类去操心实现细节，而无法赋予 AI 系统实现复杂目标所需的灵活性，”Catasta 在接受 *The New Stack* 采访时表示。

随后，另一个独立的 AI 智能体会根据事先约定的成功标准对工作成果进行评估，如有必要会将其退回修改，之后再交由用户审查结果。

![Missions 仪表盘与设置界面](https://cdn.thenewstack.io/media/2026/11/2b62ce61-missions-dash-1024x668.png)

*Missions 仪表盘与设置界面*

这一理念与其他多智能体工具颇有相似之处，例如 Factory [今年早些时候推出的同名产品 Missions](https://factory.com/news/missions)。Catasta 认为，Replit 方案的不同之处在于它如何在一开始就确立用户意图，以及它为智能体提供的控制机制和基础设施。

例如，每个智能体都在各自隔离的云环境中运行，并能访问开发工具、集成服务以及数据库、身份认证和部署等基础设施。

此外，用户必须在任务开始前设定支出上限。Replit 会在每一步核查支出与预算的对比情况，一旦达到上限，便会阻止继续使用付费服务。Catasta 认为，当多个智能体自主运行时，这类控制措施尤为重要。

> “大多数自主运行或多智能体产品都会导致失控的 Token 成本。”

“大多数自主运行或多智能体产品都会导致失控的 Token 成本，”Catasta 说。

## 使命必达

在正式发布之前，Replit 表示已使用 Missions 构建了自家的应用监控平台 Radar。据该公司介绍，智能体在 Replit 工程师的指导下开发了该系统，仅用两天时间、3,000 美元预算便完成构建，并交付了仪表盘、告警以及应用链路追踪等功能。

随后，Replit 故意制造了一次数据库故障来测试该系统，Radar 在 38 秒内识别出问题并发出告警，优于 60 秒的目标。该公司还表示，在另一项为期三小时的测试中，Radar 处理了 2,600 万条活动记录和 440 万条日志条目，且未发生数据丢失。

![Radar 应用监控仪表盘](https://cdn.thenewstack.io/media/2026/11/37e5e756-radar-application-dashboard-view-1024x640.png)

*Radar 应用监控仪表盘（由 Replit 提供）*

尽管 Radar 最初是为 Replit 自用而开发的，但该公司最终计划在进一步提升可靠性并完成代码审计后，以开源许可证向公众发布。

此外，Replit 还在软件优化方面测试了 Missions：利用由 32 个智能体组成的集群，在广泛使用的开源 Python 数值计算库 [NumPy](https://numpy.org/) 的选定工作负载上实现了最高达 19 倍的加速。

![NumPy 性能对比图表](https://cdn.thenewstack.io/media/2026/11/2243869b-numpy-workload-speedups-achieved-by-a-single-agent-a-16-agent-swarm-and-a-32-agent-swarm-using-auto-max-and-auto-power-1024x576.jpeg)

*NumPy 性能对比图表（由 Replit 提供）*

另一个内部案例则是部署了 32 个智能体来改进公司旗下的 AI 演示文稿制作工具 [Replit Slides](https://replit.com/slides)，不同工作智能体分别负责视觉设计与叙事表达的不同方面。

该公司还设想了更广泛的应用场景，包括调研潜在企业客户、准备定制化演示以及优化销售外联工作。

![Replit Slides 智能体集群界面](https://cdn.thenewstack.io/media/2026/11/08541ec1-figure-shows-agent-swarms-working-on-improving-replit-slides-1024x596.jpeg)

*Replit Slides 智能体集群界面（由 Replit 提供）*

## 驾驭智能体集群

虽然让多个智能体并行工作在理论上听起来很美妙，但也可能引发人们对重复劳动、代码更改冲突、成本飙升以及自主系统极难受控等问题的担忧。

为了防止智能体之间相互干扰代码，Replit 借鉴了其现有的一些技术，[例如并行任务（parallel Tasks）](https://docs.replit.com/learn/build-in-parallel)。其沙盒基础设施允许智能体在项目各自的独立副本上工作，然后再合并更改；而当修改发生重叠时，专门的 AI 智能体会负责处理冲突。这套最初为人类开发者协作而构建的系统，如今同样为智能体集群提供支持。

此外，底层 AI 模型的进步也让这种协作变得更加容易落地。

“我们发现，前沿模型在拆分任务和并行协作方面的表现正变得越来越出色，”Catasta 说，“正是因为在过去几个月里，这种行为通过后训练（post-trained）被融入了模型之中，智能体集群才真正开始变得实用。”

![智能体集群协作](https://cdn.thenewstack.io/media/2026/11/67805bb7-gif2.gif)

*智能体集群协作*

归根结底，这种方法的吸引力在于，不同的智能体可以同时攻克复杂问题的不同部分，其完成速度有望远超单个智能体按部就班地工作。Catasta 提到了 [OpenAI 近期在](https://openai.com/index/navier-stokes-solution/)[纳维-斯托克斯（Navier–Stokes）](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness)千禧年大奖难题上的研究——这是一个描述流体运动方程的长期数学难题。据 OpenAI 报告，其动用了约 10,000 个协同工作的智能体来推导拟议的解决方案。

Catasta 认为，攻克这样的问题如果依靠人类可能需要数百年，依靠单个智能体可能需要数年，而协同工作的智能体集群则只需数周。这些时间预估虽然带有推测性质，但它们阐明了同时运行大量智能体的核心逻辑。

“这是因为只要你能让智能体高效协作，通过在隔离环境中并行工作，就能在更短的时间内集中投入更多的算力和推理能力，”Catasta 解释道。

Replit 也看到了为各个智能体分配不同职责的价值，这就像一家公司汇集了不同专业领域的员工。

“这能让智能体将上下文聚焦于问题的某一个特定部分，而不是试图让单个智能体同时管理涉及许多不同子问题的上下文，”Catasta 补充道。

当然，有些任务存在固有的时间限制，增加人手也无法突破——你可以把十个厨师放进厨房，但煮熟一个鸡蛋所需的时间并不会因此缩短。当一个项目没有足够多的独立任务来让庞大的智能体集群保持忙碌时，同样的道理也适用。

> “无论是时间上的加速，还是专业化分工带来的收益，都存在边际效益递减的临界点——你绝不会希望用 500 个智能体去制作一份 5 页的幻灯片。”

“无论是时间上的加速，还是专业化分工带来的收益，都存在边际效益递减的临界点——你绝不会希望用 500 个智能体去制作一份 5 页的幻灯片，”Catasta 说。

因此，合适的集群规模取决于任务的复杂程度和性质。“Replit 经过调优，能够为每项任务建议合适数量的智能体，”Catasta 表示。

此外，人们还质疑自主智能体究竟能在多大程度上可靠地遵守施加给它们的限制。2025 年 7 月，一个 Replit 编程智能体曾无视限制其操作的指令，[删除了](https://www.theregister.com/software/2025/07/21/vibe-coding-service-replit-deleted-production-database/719783)一位客户的生产数据库，这引发了人们对将关键操作委托给 AI 所带来风险的担忧。

Catasta 坚称那起事件“至今仍被误解”，并指出受影响的 Replit 托管数据库可以通过平台的恢复工具还原。他表示，此后公司已经引入了更明确的控制机制，用于规范智能体可以访问哪些集成服务以及哪些操作需要获得许可，并在基础设施层面强制执行这些限制。

“任何不被允许的操作都会被我们的代理服务硬性拦截，”Catasta 说，“由于运行在云端且在企业级应用中十分成熟，Replit 在处理可配置的智能体安全设置以及隔离风险敞口方面具有独特的优势。”

本文最初发布于 [The New Stack](https://thenewstack.io)，原题为《[Replit 智能体集群仅用 2 天、3,000 美元预算就构建了一个应用监控平台，如今正面向客户开放该能力。](https://thenewstack.io/replit-missions-agent-swarms/)》。