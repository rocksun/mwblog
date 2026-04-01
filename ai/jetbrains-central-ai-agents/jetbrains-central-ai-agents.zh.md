部署[AI编码代理](https://thenewstack.io/crafting-ai-agents-platform/)已不再困难，但了解它们是否正在发挥作用以及防止它们成为企业扩张中又一个不受管理的层级，则是一项挑战。

由这家总部位于布拉格的开发者工具制造商上周发布的[JetBrains Central](https://blog.jetbrains.com/blog/2026/03/24/introducing-jetbrains-central-an-open-system-for-agentic-software-development/)，正是该公司解决该问题的方案。它是一个针对[AI代理工作流](https://thenewstack.io/github-agentic-workflows-overview/)的治理和执行平台。

JetBrains副总裁兼智能体平台负责人Oleg Koverznev在与*The New Stack*的简报中直言不讳地指出，该行业即将重演云投资回报率危机。

他表示：“每个人都知道AI是游戏规则的改变者。但很难证明实施这些系统对企业的投资回报率产生了影响。”

当企业转向云计算时，第一波投资很快就伴随着展示投资回报率的压力，围绕这种压力催生了整个成本管理和可观测性工具类别。JetBrains 比大多数公司更早地将类似的赌注押在了[智能体AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)上。

JetBrains自己在2026年1月对11,000名开发者进行的AI脉搏调查发现，90%的人已在工作中使用AI，66%的公司计划在12个月内采用编码代理。但只有13%的人表示在整个软件开发生命周期中使用了AI。Koverznev在发布帖子中写道：“[代码生成](https://thenewstack.io/the-ai-code-generation-problem-nobodys-talking-about/)成本低廉，不再是瓶颈。真正的挑战在于将结果与意图对齐，同时管理[代理驱动](https://thenewstack.io/how-ai-agents-are-starting-to-automate-the-enterprise/)工作日益增长的运营和经济复杂性。”

## 尚无人提及的协调问题

Koverznev更尖锐的论点并非关于投资回报率衡量——而是关于当代理数量激增到超出任何人能清楚了解运行状况的程度时会发生什么。

他表示：“我们设想未来将会有由人类和代理同事组成的团队。代理和人类之间的协调是一个重要的方面——这个问题正在浮现。”

大多数组织仍在孤立地运行代理。但高德纳（Gartner）预测，到2026年底，40%的企业应用程序将采用AI代理，而目前这一比例不到5%。达到这种规模时，跟踪正在运行什么、成本是多少以及是否达到了预期目标，将成为一个真正的运营问题。

JetBrains Central的解决方案是一个语义层，它聚合了来自代码库、架构、运行时行为和交付基础设施的上下文——为代理提供系统级理解，而不仅仅是提示级指令。

Koverznev说：“为了获得可预测的结果，我们需要为代理提供必要的上下文和理解代码的能力。”

这与[Air](https://thenewstack.io/jetbrains-names-the-debt-ai-agents-leave-behind/) Team相融合，Air Team是一个协作工作区，用于将任务委托给代理并跟踪多步骤工作流，它与Slack、Atlassian产品和Linear集成。论点是，如果代理工作流不与现有团队系统连接，就会在现有系统之上创建一个并行的协调层。

## 开放平台在走向锁定的市场中发挥作用

大多数AI平台供应商都在构建封闭生态系统。JetBrains则反其道而行之，Koverznev对此毫不掩饰。

他表示：“我们不想拥有整个技术栈。我们希望提供系统，让客户选择使用哪些工具、哪些代理——我们赋予他们控制能力。”

组织可以连接任何IDE或CLI，自带OpenAI或其他提供商的API密钥，并通过代理通信协议（Agent Communication Protocol）插入外部代理——例如Claude、Codex或Gemini CLI——无需定制集成工作。一个本地部署选项正在规划中。

Koverznev说：“我们站在巨人的肩膀上。大型语言模型（LLMs）提供了卓越的智能——我们不与此竞争。我们将这一切整合到一个可控的系统中。”

不锁定策略的吸引力取决于其集成的紧密程度，而这个市场并未放缓。然而，JetBrains至少在身体力行。运营高级副总裁[Hadi Hariri](https://www.linkedin.com/in/hadi-hariri/)在一份声明中表示：“我们正日益倾向于代理和AI驱动的工作流，这使得对成本和治理的可见性需求更高。这就是为什么我们已经在内部试用JetBrains Central。”

## 定价：固定治理费，可变执行费

定价分为两部分：针对治理的固定按席位订阅费，涵盖JetBrains和第三方席位，以及按使用量付费的代理执行费。Koverznev提供了一系列定价方案。

他说：“一个开发者每月可能花费100美元。另一个人可以编排数千个代理，花费10万美元。这确实是可能的。”该平台的作用是使这些支出清晰可见，并将其与上市时间、交付成本等结果联系起来。

早期访问计划将于2026年第二季度启动，与有限的设计合作伙伴群体一起在真实世界的代理工作流中测试JetBrains Central。同时，只有当JetBrains在市场围绕其他治理层整合之前实现全面上市，其开放平台策略才能奏效。