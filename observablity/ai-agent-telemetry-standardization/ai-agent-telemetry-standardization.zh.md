现代企业软件栈本质上的可组合性赋予了架构自由。软件开发者能够利用组件化和容器化的逻辑来创建优化的代码部署，而这些部署本身可以在横跨[多云实例](https://thenewstack.io/multicloud-architecture-what-i-want-to-see/)的工作负载之间切换。

[智能体功能](https://thenewstack.io/ai-agents-vs-agentic-ai-a-kubernetes-developers-guide/)正享受着同样的移动自由，但非标准化的 AI 智能体遥测却让我们处于“荒蛮时代”。

开发者正在赋予生产环境中的智能体调用多种系统工具、调用 AI 模型连接（包括语言、视觉等大模型和小模型），甚至“改进”用户请求并将工作移交给其他领域特定智能体的能力。

对于系统适应性来说，这都是好消息，但对于智能体遥测来说，这却是一个等待发生的噩梦。

> “当你使用像 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 和 [OpenInference](https://github.com/Arize-ai/openinference) 这样的标准时，你在保留选择权的同时不会失去可见性……即使技术栈发生变化，追踪格式也会保持一致。” —— Richard Young，Arize。

## 为什么智能体遥测至关重要

在更广泛的可观测性领域中，这一级别的遥测让软件工程师能够了解智能体存在于何处、它们有权进行哪些连接以及它们采取了哪些行动。

据 AI 智能体工程公司 [Arize](https://arize.com/) 的合作伙伴解决方案架构技术总监 [Richard Young](https://www.linkedin.com/in/riyoung/) 所说，智能体遥测的挑战不在于集成点存在于何处，他认为“核心在于可移植性”，不仅是智能体的可移植性，还有我们用来衡量它们的遥测标准的可移植性。

“当你使用 [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 和 [OpenInference](https://www.openinference.xyz/) 等标准时，你保留了选择权，同时不会失去可见性。标准化的智能体遥测让你能够更换框架、模型、工具或可观测性后端，而无需每次都重新构建插桩。即使技术栈发生变化，追踪格式也会保持一致，”Young 在[其公司的博客](https://arize.com/blog/agent-telemetry-standards/)频道上写道。

对于 Young 来说，真正的重点不在于点对点的集成，而在于推动建立一个共享的智能体遥测模型。

## Google Cloud 与 Arize AI

在超大规模云厂商上个月发布 [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform) 之后，Arize 与 Google Cloud 达成了合作。Arize AX 企业级智能体开发平台不仅接收来自 Gemini 智能体服务的追踪（软件执行事件历史的时间记录），还将智能体遥测统一在 OpenTelemetry 和 OpenInference 周围。这样做是为了让软件工程团队只需进行一次智能体插桩，就能一致地分析行为，并避免将关键的可观测性数据锁定在单一平台内。

云资源优化公司 [EfficientEther](https://www.efficientether.co.uk/) 的 CEO [Ryan Mangan](https://www.linkedin.com/in/ryanmangan01/) 告诉 *The New Stack*，在任何生产环境的软件部署中，你无法操作你看不见的东西，这对智能体来说更是如此。

“单次智能体运行可能包括请求重写、检索、多次工具和模型调用、重试以及移交，最后才会产生最终答案，”Mangan 表示。“如果没有涵盖每一个步骤的结构化遥测，调试就会变成艰苦的瞎猜，评估也会变得极其困难。”

Mangan 同意 OpenTelemetry 和 OpenInference 等标准至关重要，因为无论是由哪个框架、模型或平台生成的，它们都为开发者提供了一种一致的方式来理解智能体的实际行为。

## Google Cloud NEXT

OpenTelemetry 诞生于 2019 年，由 Google 的 OpenCensus 和 [Cloud Native Computing Foundation](https://thenewstack.io/cncf-kubernetes-is-foundational-infrastructure-for-ai/) 的 OpenTracing 项目这两个方案合并而成。

在 [Google Cloud NEXT 的一场会议](https://www.youtube.com/watch?v=nLH0IqHLxaA)中，Arize AI 创始人兼 CEO [Jason Lopatecki](https://www.linkedin.com/in/jason-lopatecki-9509941/) 和 Google Cloud 产品负责人 [Rami Shalom](https://www.linkedin.com/in/ramishalom/) 深入探讨了企业 AI 智能体在未来道路上需要如何进行监控和改进。Arize 的 Young 引用了这次会议并解释说，可观测性已经“经历过一次这种转变”，当时团队不得不应对相互竞争的追踪标准、供应商特定的 SDK 以及碎片化的插桩。

## 一次插桩，到处路由

这里开始显现的核心结论是：团队需要具备“一次插桩，到处路由”的能力。

云原生可观测性平台公司 [groundcover](https://www.groundcov) 的创始工程师兼现场 CTO [Noam Levy](https://www.linkedin.com/in/noam-e-levy/) 告诉 *The New Stack*，OpenTelemetry 确实已迅速被视为必不可少的东西。但他告诫说，采用标准并不能解决更难的问题：遥测数据实际上是如何在大规模环境下被收集、标准化和信任的。

“接下来的问题不仅是团队是否负担得起向 SaaS 供应商支付存储和解读这些数据的费用，还包括考虑到智能体驱动系统的数据量和隐私需求，该模型是否能站得住脚，”Levy 说。“即便如此，单靠 OpenTelemetry 也无法统一智能体的可观测性。团队仍然必须协调各供应商之间碎片化的遥测，例如 OpenAI 的数据看起来与 Anthropic 不同，这迫使他们构建必须不断适应上游变化的系统。”

Levy 建议这正是 [eBPF 改变基础的地方](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/)。通过在操作系统级别运行，[eBPF](https://thenewstack.io/research-ebpf-not-always-a-silver-bullet-for-network-apps/) 允许团队观察系统行为而无需依赖应用层插桩，直接从软件实际运行的方式中捕捉信号，而不是通过其插桩方式。

> “OpenTelemetry 智能体公约是由 ML 工程师为 ML 工程师编写的，但是……首席信息安全官（CISO）还没有参与到这场对话中来。” —— David Girvin，Sumo Logic。

## 同时生成子智能体

日志分析和云安全信息与事件管理（SIEM）公司 [Sumo Logic](https://www.sumologic.com/lp/brand?igaag=140437100557&igaat=&igacm=18132769092&igacr=782768763076&igakw=sumo%20logic&igamt=e&igant=g&cq_cmp=18132769092&utm_source=google&utm_medium=paid-search&utm_campaign=Google_Search_EMEA_UK-IE_Brand_Core_All_Exact&utm_adgroup=Core&utm_term=sumo%20logic&utm_id=701VK00000KhD8BYAV&gclsrc=aw.ds&&hstk_creative=782768763076&hstk_campaign=18132769092&hstk_network=googleAds&gad_source=1&gad_campaignid=18132769092&gbraid=0AAAAADviF06i7NbW--ctkclkkasHN1aG4&gclid=CjwKCAjwntHPBhAaEiwA_Xp6RkMMuKanZ4TjfE9gI0nWLaRRVKw5uYmT5FBswLEYwk8pPb_9BNIxfhoCQqcQAvD_BwE) 的 AI 安全研究员 [David Girvin](https://www.linkedin.com/in/david-a-girvin/) 告诉 *The New Stack*，汇聚 OpenTelemetry 作为智能体遥测的基础确实非常重要，但更难的问题是，当这些遥测数据大规模进入平台时，团队该怎么办。

“单次智能体运行是一个可管理的转录记录，”Girvin 说。“但如果有一千个智能体都在生产环境中运行，彼此之间进行移交，调用外部工具，点击检索系统并同时生成子智能体呢？那就变成了一个数据问题。”

在倡导更广泛的工具民主化时，Girvin 提醒我们，OpenTelemetry 智能体公约是由 ML 工程师为 ML 工程师编写的，但他警告说，CISO 尚未参与到这场对话中。他说，当安全官员加入时，那些纯粹为了可观测性而进行插桩的团队会发现，他们的遥测数据经不起董事会级别的调查。

## 如何向智能体提问

随着赋予智能体的自主权越来越大，我们现在需要追踪（traces）来展示智能体交付最终输出所遵循的路径。如果没有这一点，软件工程师将难以评估、调试和改进智能体的行动。

这意味着智能体追踪需要回答以下问题：原始用户请求是什么，它是如何转换的；使用了哪些模型、工具和数据源；延迟、幻觉、策略失败或错误检索发生的程度如何；以及哪些智能体代码执行步骤应该进一步分析以寻求改进？

## 智能化前的标准化

本着不要在学会走之前就想跑的精神，业界似乎正在形成一种日益牢固的共识，即需要对智能体行为的衡量进行标准化。当这些措施还包括标准化的测量方法时，我们就能实现具有足够语义细节的结构化智能体遥测，从而支持评估和智能体改进。