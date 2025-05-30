# 微服务测试缓慢带来的百万美元问题

![特色图片：微服务测试缓慢带来的百万美元问题](https://cdn.thenewstack.io/media/2025/03/65ab1da5-costly-1024x576.jpg)

“我们每月因糟糕的测试流程损失约 50 万美元。” 这句令人警醒的话来自一位平台工程副总裁，在最近一次关于微服务测试挑战的讨论中。 特别令人担忧的是，这并非估计，而是仔细衡量的结果。

他们的组织已发展到 200 多名开发人员，他们跨数十个微服务工作，每位工程师平均每月提交 15 个拉取请求。 表面上看似蓬勃发展的工程组织掩盖了一个严重的生产力损耗：他们的集成测试与 PR 审查过程完全脱节。

这位副总裁解释说：“我们的[开发人员实际上并不等待集成测试完成就合并代码](https://thenewstack.io/the-struggle-to-test-microservices-before-merging/)。” “他们运行基本的单元测试，获得代码审查批准并合并。 然后真正的问题就开始了。”

他们的合并后[集成和端到端测试](https://thenewstack.io/the-struggle-for-microservice-integration-testing/)经常会发现单元测试未捕获的问题。 当发生故障时（经常发生），工程师必须切换回他们已经从心理上转移的代码，诊断复杂的集成问题，并再次完成整个 PR 周期。

“每个调试-修复-合并周期可能会消耗一到两个小时的专注工程时间，” 副总裁继续说道。 “由于工程师经常遇到这些集成故障，我们发现每位开发人员每月因这种碎片化的工作流程而损失约 20 个小时。”

计算结果令人警醒：200 名工程师 × 每月损失 20 小时 × 每小时 100 美元 = 每月损失 400,000 美元的工程生产力。

当我建议采用传统的解决方案，即启动更多环境来缓解瓶颈时，这位副总裁摇了摇头。 “我们已经多次计算过这些数字。 复制环境的基础设施成本将接近我们目前的损失，而无法解决根本问题。”

这次对话概括了现代微服务架构为工程团队带来的困境。 组织采用微服务是为了可扩展性和团队自主性，但最终发现自己陷入了不断增加的基础设施成本和不断下降的开发人员生产力之间。

**内部循环与外部循环**

要理解为什么这个问题如此普遍，我们需要研究工程师所说的开发的“内部循环”和“外部循环”。

内部循环——编写代码、运行单元测试和进行本地更改——通常很快。 工程师可以在几分钟内获得即时反馈。 这种快速循环是开发人员蓬勃发展的地方，可以保持流畅的状态和高生产力。

但是对于微服务，外部循环——与其他服务集成更改、运行完整的系统测试和部署——变得非常慢，通常是 10 倍或更多。

让我们分解一下为什么这个外部循环会成为生产力的杀手：

**集成瓶颈**：一旦代码通过审查和基本单元测试，它就会被合并到主分支中。 只有这样，全面的集成测试才会运行——通常在与数十个其他最近合并的更改共享的暂存环境中运行。

**谋杀之谜**：当[测试在这个环境中失败时](https://thenewstack.io/testing-shortcuts-to-avoid-in-microservice-environments/)，工程师面临着一项侦探挑战。 是他们的更改吗？ 是别人的更改吗？ 是多个更改之间的交互吗？ 自上次成功运行以来，已经合并了数十个提交，因此查明罪魁祸首变成了一项耗时的调查。

**上下文切换惩罚**：当集成失败出现时，工程师已经在心理上转移到新的任务。 切换回调试几小时或几天前编写的代码会产生巨大的认知成本。[研究表明，在上下文切换后，完全恢复注意力可能需要长达 23 分钟](https://www.fastcompany.com/944128/worker-interrupted-cost-task-switching)。

**排队效应**：一些组织试图通过创建严格的暂存环境访问控制来缓解这些问题。 一位工程总监分享说，他们构建了一个自定义 Slack 机器人，用于排队访问暂存环境。 工程师会输入“/staging-queue add”并等待轮到他们——有时需要几个小时。 在星期五，每个人都赶在周末前合并，等待时间可能会延长到四到五个小时。

**涟漪效应**：失败的测试不仅会影响负责的开发人员。 当暂存环境崩溃时，整个团队可能会被阻止。 一次失败的部署可能会破坏多个工作流程。
累积的影响是惊人的。外部循环中一个典型的调试-修复-测试周期可能需要两到三个小时，而内部循环中只需要两到三分钟。由于工程师每周多次进行这些循环，公司通常每周会因这种碎片化的工作流程而损失每位开发人员 8 到 10 个小时。

**传统方法无法扩展**

为什么我们不能通过更多环境来解决这个问题呢？传统的“盒中系统”方法，即每个开发人员在自己独立的云实例中启动整个系统，很快就会因规模而变得过于昂贵。

让我们来计算一下：

对于一个拥有 50 个微服务的系统，开发人员需要一个强大的 AWS EC2 m6a.8xlarge 实例（32 个 vCPU，128 GiB 内存），该实例的成本约为每小时 1.30 美元。每月 24/7 运行此实例的成本为 936 美元，或者每个开发人员环境每年 11,232 美元。要为 50 名开发人员的团队提供专用环境，每年的成本将飙升至 561,600 美元——这仅仅是计算成本，不包括存储、数据传输或托管服务。

这就是为什么许多团队选择数量有限的共享环境，从而造成瓶颈和生产力下降。

**一种现代方法：基于租户的环境**

![封装服务本地和 git 分支版本的沙箱](https://cdn.thenewstack.io/media/2025/03/6e3a63df-image1-1024x588.png)

封装服务本地和 git 分支版本的沙箱。

现代服务网格架构正在改变这个等式：

无需复制基础设施，您可以使用服务网格技术通过在请求级别进行隔离来创建即时测试环境。每个开发人员通过智能请求路由获得自己的沙箱。

以下是转变变得可量化的方面：

*   **基础设施成本**：与复制环境相比，降低了 90%，使得为每个 PR 提供隔离测试在经济上可行
*   **测试范围**：从选择性测试（由于资源限制）到对每个代码更改进行全面测试
*   **集成测试速度**：从合并后（数小时）到合并前（数分钟）
*   **开发人员迭代**：从每天一两次到每天 10 到 15 次
*   **平均修复时间**：从两到三个小时到 15 到 20 分钟
*   **缺陷逃逸率**：降低了 70%（在合并之前发现的问题）

最显著的影响来自于大幅降低临时环境的成本。当测试在规模上变得负担得起时，组织可以从配给测试资源转变为为每个拉取请求提供按需环境。这种测试的民主化改变了开发人员的生产力和软件质量，而不会超出基础设施预算。

副总裁的回应：“所以我们可以为每个开发人员提供即时环境，并且降低成本？”

是的，完全正确！

**这是如何工作的？**

关键的见解是，完全复制环境对于测试微服务是不必要的。通过应用层隔离和智能请求路由，您可以共享底层基础设施，同时保持隔离。

当开发人员想要测试更改时，系统会创建一个沙箱，其中仅包含正在修改的服务。请求根据请求标头动态路由到这些沙箱化的服务，同时对其他所有内容使用共享环境。

**解决数据隔离挑战**

这种方法的一个关键方面是如何处理数据隔离。当工程师第一次听到基于请求的路由时，他们立即提出了对数据层的担忧：“如果我们共享基础设施，并发测试不会相互干扰数据吗？”

这是一个有效的问题，有多种解决方案，具体取决于测试要求：

对于大多数测试场景，共享数据库运行良好。关键是利用通常已构建到微服务架构中的多租户模式。通过使用现有的域模型标识符（`userId`, `orgId`,` tenantId`）对测试数据进行分区，每个测试都可以在共享数据库中自己的逻辑空间中运行。

对于更密集的测试需求，例如模式迁移或数据破坏性操作，可以按需配置临时数据库实例。这些临时数据库仅在需要时启动，并在测试完成后终止，从而提供完全隔离，而无需维护永久的重复基础设施的开销。

最复杂的系统提供了一种混合方法，自动确定何时共享资源足够，何时需要隔离资源。这为开发人员提供了两全其美的优势：共享资源的速度和效率，以及必要时隔离的安全性。

**在生产中得到验证**

这种方法不仅仅是理论上的；它已经在规模上取得了成果。领先的科技公司已经实施了这种模型的变体，并取得了令人印象深刻的成果：
[Uber 构建了 SLATE](https://www.uber.com/blog/simplifying-developer-testing-through-slate/)，用于基于请求的测试流量路由。[Lyft](https://eng.lyft.com/building-a-control-plane-for-lyfts-shared-development-environment-6a40266fcf5e)为其共享开发环境创建了一个控制平面。[Airbnb](https://www.youtube.com/watch?v=RpSVBtyoYCY)实现了请求路由，从而显著降低了测试成本。

这些组织使用[云原生技术](https://thenewstack.io/cloud-native/)和服务网格功能来转换测试，而无需复制基础设施。最先进的实现使用基础设施即代码 (IaC) 在几分钟内部署临时环境——不仅用于测试，还用于原型设计和实验性开发。

业务影响通过技术指标（例如，DORA 框架）和[开发者体验改进](https://thenewstack.io/how-to-understand-and-improve-your-developer-experience/)来衡量。公司通常会看到更快的上市时间、更高质量的版本和显著降低的基础设施成本，从而实现更好、更快、更便宜的软件开发的罕见组合。

**从瓶颈到突破**

传统的合并后集成测试方法在[微服务开发](https://thenewstack.io/microservices/)中造成了不必要的瓶颈。通过[将集成测试左移](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/)——将它们从缓慢的外部循环移动到快速的内部循环中——组织可以从根本上改变其开发过程。

工程师在合并之前针对实际依赖项验证更改，从而在集成问题仍然新鲜且易于修复时发现它们。现代云原生技术（如服务网格和请求路由）使这种方法越来越容易实现，而无需大规模的基础设施投资。

对于在微服务测试方面苦苦挣扎的组织来说，这种转变带来了明显的竞争优势：更高质量的软件、更快的交付周期和更高效的资源利用——所有这些都在改善开发者体验的同时实现。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，即可观看我们所有的播客、访谈、演示等。