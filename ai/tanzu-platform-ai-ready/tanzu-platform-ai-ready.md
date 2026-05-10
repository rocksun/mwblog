<!--
title: Tanzu 平台的 15 年先发优势，助力企业把握 AI 契机
cover: https://cdn.thenewstack.io/media/2026/05/1bc878fb-allison-saeng-zvzuz5o5vsw-unsplash-scaled.jpg
summary: 本文探讨了 AI 时代下企业平台建设的挑战。Tanzu 平台凭借 15 年在集成化能力、治理与安全性方面的积累，为企业提供了成熟的 AI 应用基础，避免了 DIY 平台的复杂性与风险。
-->

本文探讨了 AI 时代下企业平台建设的挑战。Tanzu 平台凭借 15 年在集成化能力、治理与安全性方面的积累，为企业提供了成熟的 AI 应用基础，避免了 DIY 平台的复杂性与风险。

> 译自：[Tanzu Platform's 15-year head start meets the AI moment](https://thenewstack.io/tanzu-platform-ai-ready/)
> 
> 作者：Cora Iberkleid

2011 年，Marc Andreessen 发表了著名的观点：[软件正在吞噬世界](https://a16z.com/why-software-is-eating-the-world/)，预言每个行业都将被软件驱动的竞争对手重塑或取代。这一构想加速了一个平台重塑时代的到来。

六年之后，Nvidia 的 Jensen Huang 延伸了这个比喻，预测 AI 模型将取代人类编写的代码：“[软件正在吞噬世界，但 AI 将吞噬软件](https://www.technologyreview.com/2017/05/12/151722/nvidia-ceo-software-is-eating-the-world-but-ai-is-going-to-eat-software)”。

近十年过去了，这一预言正带着显而易见的紧迫感变为现实，而新的需求也正在放大许多企业在最初选择基础设施时所面临的局限。

> “当 AI 以季度为单位重塑你的行业时，现在是构建自主平台的时机吗？”

这是一个值得深思的问题：当 AI 以季度为单位重塑你的行业时，现在是构建自主平台的时机吗？

## 跑道更短，筹码更高

上一轮数字化转型给了企业大约十年的时间来摸索如何更快地交付软件。搞砸了的公司最终会被收购、颠覆或削弱——但“最终”通常足够长，足以让他们纠正航向。AI 则没有提供同样的缓冲空间。模型改进的速度、用例的广度，以及具备 AI 能力与缺乏 AI 能力的公司之间的竞争差距，都在以大多数企业 IT 周期无法吸收的速度扩大。

与此同时，搞砸的代价也更高。AI 部署不仅仅是运行另一个应用。它是一个潜在的载体，可能导致提示词注入、PII（个人身份信息）泄露、未经授权的模型访问、影子支出、合规风险以及声誉损失，其规模是前几代企业软件所未见的。在 AI 领域行动最快的组织，也是在治理方面思考最深的企业——因为两者并非处于对立状态，而是同一个问题的两面。

每个企业现在都需要大致同时完成三件事：

*   **为每位员工提供 AI**，作为基础赋能——就像电脑和互联网接入成为标准配置一样。
*   **将 AI 融入外部产品**，以提升交付给客户的价值。
*   **将 AI 嵌入内部流程**，以改变公司的运营方式，而不不仅仅是产出内容。

而且，所有这三点都需要在治理、[可观测性](https://thenewstack.io/observability-every-engineers-job-not-just-ops-problem/)和安全保证下完成，让合规官能够放心地签字通过。

这就是挑战所在。最大的障碍在于确定这三者之下承载的是哪种平台。

## 似曾相识的模式

对于任何自 2011 年以来一直关注企业平台市场的人来说，这一决策的形式会感到非常熟悉——因为我们以前经历过。

Cloud Foundry 于 2009 年在 VMware 构思，并于 2011 年作为开源 PaaS 正式发布。在过去的十五年里，它以三个连续的名称——Pivotal Cloud Foundry、VMware Tanzu Application Service 以及现在的 VMware Tanzu Platform——在企业规模的生产环境中商业化运行。

在那段时间里，它悄然积累了一套集成能力，这些能力在其他任何地方都很难完整地汇集在一起：

*   基于容器的运行时隔离（比 Docker 早两年）
*   简单的 `cf push` 代码部署体验
*   以应用为中心的 Web UI，使平台立即可用
*   一个无需开发人员编写 [Dockerfiles](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/ "Dockerfiles") 即可生成加固运行时镜像的构建系统
*   一个具有自动凭据注入和轮换功能的自助服务市场
*   TLS 终止和路由
*   多租户组织和空间
*   将工作负载定向到特定的 CPU 池
*   GPU 支持的服务
*   自愈功能
*   针对 CVE 响应的自动化虚拟机重建（Repaving）
*   平台本身的零停机升级

至关重要的是，它在本地运行的方式与在任何公有云上运行的方式完全一致——这种多云和混合云的姿态，大多数平台又花了十年时间才赶上。一个小型的运营团队就可以提供精湛的开发人员体验，并管理数千个企业级应用，无论这些应用是部署在本地还是跨多个云。

与此同时，从几年后开始，Kubernetes 运动也在平行推进。Kubernetes 采取了截然不同的哲学：它不提供集成平台，而是提供可以组合成平台的原语。这是一个合理的赌注。它培育了一个巨大的生态系统，对于有特定需求和工程能力来满足这些需求的组织，它提供了 Cloud Foundry 那种更加固化（Opinionated）的模型所不具备的灵活性。

但组合是有代价的，而且代价会不断累积。构建自己的开发人员平台意味着组装——并持续维护——一整套堆栈，包括工作负载调度、入口（Ingress）、服务网格、多租户、IAM、机密管理、服务目录、策略执行、可观测性和面向开发人员的 UI——每一部分都有自己的生命周期、自己的 CVE、自己的供应商和自己的升级节奏。平台团队在壮大，集成面增长得更快。

走这条路曾有正当理由。灵活性很重要；避免[供应商锁定](https://thenewstack.io/want-to-escape-vmware-exit-with-platform-engineering/)很重要；针对特定工作负载的定制也很重要。在处于萌芽状态的市场中，内部构建确实是正确的选择，这也是为什么在 Cloud Foundry 出现之前的 2000 年代初期，平台都是在内部构建的原因之一。

但到了 2010 年代中期，经济格局发生了转变，然而行业还是倾向于这种 DIY 的本能。这值得追问原因，而且没有单一的答案：掌控感比依赖感更安全；构建比购买更具战略意义；平台团队的重要性随着其管理的覆盖面积成比例增加；而组装的成本累积得足够缓慢，以至于会被误认为是正常的运营支出。

企业中的等效案例是，某家公司在 2010 年决定构建自己的 CRM 而不是采用 Salesforce。当时的理由通常很充分：灵活性、控制力，以及避免对供应商的依赖。十年后的结果是，一个系统只实现了 Salesforce 70% 的功能，成本更高，并且消耗了本该花在实际业务上的工程周期。这些决定在当时是可以理解的，而在事后看来则是显而易见的。

## 经过验证的基础，现为 AI 而生

这就是故事转折的地方，因为过去十年的教训并不是为了证明 Cloud Foundry 的正确性。它比这更有用：**正是那些让 Cloud Foundry 难以通过 DIY 效仿的集成工作，使得 Tanzu Platform 在今天处于拥抱 AI 的绝佳位置。**

企业负责任地部署 AI 所需的能力并非从根本上是全新的。它们是任何成熟应用平台所需的能力，只是应用于一类新的工作负载：

*   一个**治理层面**，由平台工程师（而非单个开发人员）决定哪些模型获准共享使用。
*   一个**服务市场**，开发人员可以像绑定任何数据服务一样，绑定到经过批准的 AI 模型、MCP 服务器和向量数据库。
*   一种**凭据机制**，在运行时注入模型 API 密钥，并在不更改代码的情况下进行轮换。
*   一个**抽象层**，隐藏私有托管 AI 模型与主要云提供商之间的差异，使开发人员不会硬编码供应商选择。
*   对每一个模型和 [MCP 服务器](https://thenewstack.io/build-mcp-server-tutorial/)交互进行**可观测性和审计日志记录**，因为你无法治理你看不到的东西。
*   **限流和中间件**，以控制支出并执行使用策略。
*   一个**网关**，用于将 AI 流量路由到内部或外部模型，并将敏感信息保留在企业边界内。
*   **部署灵活性**——在私有云本地或跨公有云——以便根据合规性要求将 AI 相关的应用、服务和数据保留在相应位置，并能在不同环境间迁移而无需重新设计。

这些基础能力构成了今天 Tanzu 平台的 AI 愿景。特别是三个版本标志着转折点：Tanzu Platform 10.0，在市场中增加了 AI 服务方案；10.3，促进了 MCP 服务器的共享；以及 10.4，引入了智能体基础（Agent Foundations）。

[**10.0 — AI 服务**](https://blogs.vmware.com/tanzu/broadcom-announces-the-general-availability-of-vmware-tanzu-platform-10-making-it-easier-for-customers-to-build-and-launch-new-applications-in-the-private-cloud/)。**AI 服务**（最初作为 GenAI Tile 发布，后更名）通过市场公开获批模型，因此开发人员可以使用他们已经熟悉的 `cf create-service` 和 `cf bind-service` 流程。AI 服务器提供用于限流、可观测性和审计日志记录的中间件，并与第三方工具集成以满足额外需求（如 PII 过滤）。模型可以私有托管在基础架构内（在基于 CPU 或 GPU 的基础设施上），也可以通过云提供商访问，所有这些都在一致的 OpenAI 兼容 API 之后，因此应用在切换模型时无需重构。平台工程师负责策展出现在市场中的内容；开发人员则可以自助访问已获批的内容。

[**10.3 — 共享 MCP 服务器**](https://blogs.vmware.com/tanzu/tanzu-platform-10-3-delivers-the-ai-native-engine-for-developer-velocity-and-platform-control/)。新的**服务发布**功能自动化了开发人员将任何应用（包括 MCP 服务器）转化为服务方案的过程，具备服务实例生命周期能力以及在内部路由后保护后端应用的网关。平台运营商保留通过市场批准并公开任何新服务方案的能力。

[**10.4 — 智能体基础（Agent Foundations）**](https://blogs.vmware.com/tanzu/introducing-tanzu-platform-10-4/)。智能体基础结合了早期版本的功能与三个新贡献，以支持智能体（Agentic）应用。**Agent Buildpack**（技术预览版）向非开发人员开放了智能体编写功能，将智能体和技能描述（以自然语言编写）转化为运行中的智能体，并可选择绑定到模型、工具和其他平台服务。**MCP Gateway** 服务允许开发人员将 MCP 服务器绑定到网关实例，为智能体提供集中的发现和访问点；网关通过内部路由保护平台上的 MCP 服务器，并为平台上下的 MCP 服务器附加可验证的 OIDC 身份，以便自主操作可以追溯到发起操作的最终用户。最后，增强的**可观测性仪表板**按网关、模型、应用、空间或组织跟踪智能体工具调用和模型消耗，并提供成本归因的费用展示（Showback）。

从成熟的 Tanzu 平台部署到生产级 AI 应用之间的差距确实很小，因为平台在多年前就已经完成了最困难的部分。而对于现在被要求在尚未稳定的堆栈之上添加 AI 层的 DIY 平台来说，情况并非如此。

## 现在不是构建自主平台的时机

企业将 AI 转化为组织内实用能力的窗口期非常窄，而将这个窗口期浪费在平台重建上的代价比以往任何时候都要高。能够实现这一转型的平台，是那些在 AI 让这些能力成为标配之前，就已经完成了艰苦、枯燥、不起眼的集成工作的平台——包括凝聚态的开发人员体验、受管的服务访问、默认的可观测性、零停机运营以及每一层的安全性。

Tanzu 平台完成了这些工作。坚持了十五年。在“我们应该用 LLM 搞个原型”与“我们已将其在适当治理下投入生产运行”之间，如果平台治理、可观测性和自助式开发人员体验是系统的属性而非仍需构建的东西，那么这段距离会更短。

> “现在使用 Tanzu 平台的理由并不是因为它一直是正确的。理由是，市场终于步入的时刻，恰好与平台准备就绪的时刻相吻合。”

现在使用 Tanzu 平台的理由并不是因为它一直是正确的。理由是，市场终于步入的时刻，恰好与平台准备就绪的时刻相吻合。

### 更多资源

*   “[为什么你的 DIY Kubernetes 堆栈无法在智能体 AI 时代幸存](https://blogs.vmware.com/tanzu/why-your-diy-kubernetes-stack-wont-survive-the-era-of-agentic-ai/)”，Oren Penso，《The New Stack》，2026 年 3 月。
*   “[使用 Tanzu 平台构建企业级 MCP 服务器市场](https://blogs.vmware.com/tanzu/building-an-enterprise-mcp-server-marketplace-with-tanzu-platform/)”，Corby Page 和 Brian Kirkland，Tanzu 博客，2026 年 1 月 23 日。
*   “[通过 VMware Tanzu 平台 AgentFoundations 让企业级智能体变得简单安全](https://blogs.vmware.com/tanzu/enterprise-ready-agents-made-simple-with-vmware-tanzu-platform-10-4/)”，Camille Crowell-Lee，Tanzu 博客，2026 年 4 月 15 日。