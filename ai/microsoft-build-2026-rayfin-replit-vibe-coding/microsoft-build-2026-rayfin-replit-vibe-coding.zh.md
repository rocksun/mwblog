[氛围编程](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/)让构建应用程序变得前所未有的简单。然而，将这些应用程序投入企业级生产环境仍然是个难点。这正是微软通过在 [Build 2026](https://news.microsoft.com/build-2026/) 上发布的全新开源 SDK 和 CLI [Rayfin](https://github.com/microsoft/awesome-rayfin) 所要解决的差距。

Rayfin 让开发人员和 [编程智能体](https://thenewstack.io/ai-coding-agents-level-up-from-helpers-to-team-players/) 能够完全用代码定义应用程序后端——包括数据模型、业务逻辑和访问策略——并将其直接部署到 [Microsoft Fabric](https://thenewstack.io/microsoft-fabric-goes-all-in-on-real-time-data-intelligence/)。微软表示，这样做的结果是，应用程序在进入生产环境时就已经具备了安全性、合规性，并与企业数据资产进行了整合，而无需开发人员手动配置基础设施。

氛围编程平台提供商 [Replit](https://replit.com/) 是独家首发合作伙伴。Replit 总裁兼 AI 负责人 [Michele Catasta](https://www.linkedin.com/in/pirroh/) 简单地描述了这种合作关系：[Replit Agent](https://docs.replit.com/references/agent/overview) 可以使用 Rayfin 在代码中定义后端，然后将其部署到 Fabric，从而使应用程序数据保存在客户的 Fabric 数据资产中。Catasta 告诉 *The New Stack*，一旦 Rayfin 发布，Replit 将在内部将其用于生产，随后将进行更广泛的企业推广。

Replit 创始人兼 CEO [Amjad Masad](https://www.linkedin.com/in/amjadmasad/) 在微软提供的一份声明中，用更犀利的语言表达了这一主张：“Rayfin 为我们的用户解锁了一种全新的开发模式。智能体编写代码，Fabric 快速且安全地发布代码。通过合作，我们正在为开发人员提供他们从未拥有过的东西：一条从创意到企业级生产的路径，其时间衡量单位是小时，而不是月。”

与 Replit 的合作并不是企业级吸引力的唯一信号。Catasta 还指出，Replit 最近宣布的 [与 Visa 的合作](https://thenewstack.io/replit-visa-ai-payments/)（涉及用于智能体商业的可信智能体协议），正是 Rayfin 旨在支持的企业级势头的有力证据。

## Rayfin 的功能

Rayfin 通过基于 GitHub 的工作流运行。开发人员（或代表他们构建的智能体）描述要构建的内容，Rayfin 就会生成一个企业级后端，包括数据库、身份验证和相关服务，并直接将其输出到应用程序代码中。部署到 Fabric 会将这些组件转化为一流的平台构件，并通过 Fabric 的目录进行治理和发现。应用程序数据会自动落入 [OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview)，并立即供 Fabric 的分析、实时智能和 AI 引擎使用。

其安全模型是架构式的，而非外挂式的。在设计上，数据绝不会离开客户的 Microsoft Fabric 租户。每个服务组件都是 Fabric 中的一个独立构件，受平台治理控制。Catasta 将这视为企业买家最核心的关注点。他说，随着企业使用场景的增加，首要因素就是安全性——具体来说，就是 AI 生成的应用程序在生产环境中的安全性。

## 与 Supabase、Neon 和 PlanetScale 的对比

最显而易见的对比是与现有的后端即服务（BaaS）平台——[Supabase](https://thenewstack.io/how-supabase-is-building-its-platform-engineering-strategy/)、[Neon](https://thenewstack.io/neon-branching-in-serverless-postgresql/)、[PlanetScale](https://thenewstack.io/planetscale-more-monitoring-connections-and-regions-for-the-database-service/)。这些平台在底层也提供托管的 [PostgreSQL](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)，并加速早期阶段的开发。Catasta 从每个平台在应用程序生命周期中所扮演的角色进行了区分：那些平台加速了“第一天”（开发阶段）。而 Rayfin 旨在确保应用程序能够成功进入生产环境。

他说，更大的区别在于范围。Supabase 及其同类产品是用于构建应用程序的后端即服务解决方案。而 Fabric 是一个端到端的分析和数据平台，将数据工程、集成、仓储、数据科学、实时智能和 Power BI 整合到了一个单一的 SaaS 产品中。

Rayfin 的价值主张正是基于这种区别：开发人员无需拼凑各种服务，而是获得了一个已经是企业数据平台一部分的后端，并且从第一天起就支持运营和分析工作负载。

可移植性是一个合理的问题。Rayfin 采用代码优先模式并且开源，支持自托管。但它默认是 Fabric 原生的，Catasta 对此非常直接：Rayfin 针对部署到 Fabric 进行了优化。企业级的安全性、治理和数据集成方案都依赖于该部署目标。

## 面向人群

目标用户是企业团队，而不是独立开发者。Catasta 明确表示：Replit 在企业市场正展现出强劲的势头，而 Rayfin 旨在加速这一势头。这一宣传契合了企业软件买家所熟知的一种紧张关系——AI 编程工具带来的生产力提升是真实的，但首席信息安全官（CISO）对未经审核的 AI 生成代码在生产环境中运行的担忧也同样真实。Rayfin 正是将自己定位在这两者的交汇点上。

Microsoft Fabric CTO [Amir Netz](https://www.linkedin.com/in/amirnetz/) 在 Build 大会期间接受 *The New Stack* 简报时也表达了类似的观点：“你不能让任何人在企业中随意构建全栈应用。我们希望确保的是，当人们进行构建时——我们也乐见于此——他们能够以一种对组织而言安全、合规且有保障的方式进行部署。”

Rayfin 目前已作为开源软件提供。拥有 Fabric 订阅的客户可以使用部署到 Microsoft Fabric 的功能。