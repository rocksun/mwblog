
<!--
title: 你的平台工程可能做错了
cover: https://cdn.thenewstack.io/media/2024/05/8ded2ba3-platform.jpg
-->

每个内部开发平台都需要一个合适的后台，在考虑其他任何事情之前，设计和构建后台至关重要。

> 译自 [You’re Doing Platform Engineering Wrong. Probably.](https://thenewstack.io/youre-doing-platform-engineering-wrong-probably/)，作者 Luca Galante。

所以你确信，你的老板也在船上。你们都阅读了最新的 [DevOps](https://humanitec.com/whitepapers/devops-benchmarking-study-2023) 和 [平台工程状况](https://humanitec.com/whitepapers/state-of-platform-engineering-report-volume-2) 报告；你访问了 KubeCon 并与那里的半数供应商进行了交谈。你甚至参加了一个 [执行圆桌会议](https://humanitec.com/events?event-type=Roundtables) 与您所在行业的其他人讨论该主题。决定终于正式了：你正在开始你的平台工程之旅。恭喜！改善 DORA 指标、开发人员自助服务和更快的上市时间的应许之地就在眼前。对吧？

可以，但你需要避开许多平台团队陷入的一些关键错误和反模式。第一个也是最常见的一个：首先构建你的 [内部开发人员平台 (IDP)](https://internaldeveloperplatform.org/) 的前端，而不是专注于后端。如此多的团队只是采用他们当前的 CI/CD 流水线，并在其顶部添加一个 [开发人员门户](https://humanitec.com/internal-developer-portal)。砰，完成了！你的平台工程有一个梦幻般的开端。对吧？

没那么快。这种门户优先的方法存在许多问题，在 Salesforce 构建 IDP 的 Aaron Erickson [强调了最明显的一个](https://platformengineering.org/blog/what-to-build-first-the-house-or-the-front-door)：“构建 IDP 就像建造房屋。你永远不会从前门或窗户开始，而是从地基开始。然后你添加墙壁，最后才是门和窗户。[构建 IDP](https://thenewstack.io/build-your-idp-at-light-speed-with-a-platform-reference-architecture/) 从门户开始就像从前门和窗户开始建造房屋。”

这种方法导致的另一个重大挑战是，随着你的平台工程计划的成熟和范围的扩大，你需要在 IDP 中构建越来越多的逻辑。如果你没有从一开始就正确地做事，例如从平台的后端开始，你会发现自己试图将逻辑塞进你的前端。如果说我们在过去 10 多年中从构建微服务架构中学到了什么，那就是将业务逻辑构建到你的前端是一个大问题，并且违反了 [单一职责原则](https://www.thoughtworks.com/en-de/insights/blog/agile-engineering-practices/solid-principles-how-to-create-a-code-that-is-easy-to-extend-and-maintain-part-1)，其中一个模块“ [应该对一个且仅一个参与者负责](https://search.worldcat.org/title/1003645626)。”这会暴露你的业务逻辑，在使你的前端变得繁重和缓慢的同时创建应用程序漏洞。

这就是为什么每个 [内部开发人员平台](https://thenewstack.io/internal-developer-platform-vs-internal-developer-portal-whats-up/) 都需要一个适当的后端，以及为什么作为一个平台团队，你希望确保在担心其他任何事情之前开始设计和构建它。

那么如何设计后端？你基本上有两个选择。

## 选项 1：基于流水线的后端 (CI/CD+IaC)

这是许多 [从平台工程开始的团队](https://thenewstack.io/this-is-why-infra-teams-should-care-about-platform-engineering/) 经常默认的。它通常是以前 DevOps 和基础设施团队的遗留，将 CI/CD 流水线与基础设施即代码 (IaC) 设置相结合。

在其基本形式中，用户（应用程序开发人员）在逐个环境的基础上工作，使用针对每个环境的单独配置文件定义应用程序和基础设施配置。然后，CI/CD 流水线使用每次 git 推送执行对这些文件的更改。在更高级的设置中，开发人员可以用更抽象的方式描述更改，然后通过嵌套流水线将这些请求转换为单独的流水线运行。

### 优点和缺点

这里的优势非常明显：大多数团队仍然习惯于这种类型的工具链和流程。这也意味着业内构建和维护基于流水线的系统的技术人才库相对较大。

缺点是流水线是一个启动停止系统，它不是设计为内置高级逻辑的。因此，与我们之前讨论的前端优先方法类似的论点适用。虽然简单的逻辑（例如环境进度和签核）非常适合流水线系统，但任何超出此范围的内容（例如开发人员与你的基础设施交互）都无法很好地扩展。

例如，假设开发人员请求 AWS S3 存储桶用于其工作负载。您自然希望您的 IDP 为每个环境创建单独配置的存储桶，在部署前运行策略检查并将机密注入到容器中。为此，基于流水线的后端将呈指数级增长，并且很快变得难以维护。

结果是，流水线后端通常被保持在最少的业务逻辑，因为任何更高级的东西都会变得过于庞大且复杂。这会导致不良的平台设置，无法管理应用程序的完整生命周期，并且无法在您的组织中推动标准化。它们还难以审核且难以使用（没有 API 优先，没有多个接口等）。

## 选项 2：基于图的后端（平台编排器）

平台编排器是一个位于 CI 系统之后的平台后端。它读取声明性抽象请求（例如，开发人员希望为其工作负载使用 Postgres 数据库，并将其部署到暂存环境）。它解释请求的上下文（在本例中为 environment=staging），并将其与平台团队设置的规则进行匹配。然后，它输出一个可执行资源图，该图可由编排器或现有的 CD 解决方案直接部署（由 ArgoCD 同步到集群）。

基于图的方法非常灵活，并允许高级逻辑。如果开发人员请求新的依赖项（例如向工作负载添加 Redis 缓存），则该图将自动扩展。如果平台团队将 Redis 从 Vx 更新到 Vx+1，则该图将自动重建，并且在下次部署时使用较新版本。

这种架构方法使平台团队可以对每个环境使用资源类型的相同定义。坚持这个示例，在“暂存”上下文中所有类型为“Postgres”的资源都以完全相同的方式进行配置，生命周期得到管理，并且任何配置偏差都会自动恢复到标准。平台编排器还应该具有部署流水线功能，以管理环境进程和其他自动化。

### 优点和缺点

基于图的后端满足了良好架构设计的全部要求。它们将抽象的开发人员请求转换为可执行配置文件，这些配置文件遵循明确的黄金路径和规则。这通过设计自动推动标准化，跨越所有工作流和团队。它们是 API 优先的，并具有多个接口（CLI、UI、基于代码的，例如 Score）。它们带有基于角色的访问控制和单点登录，并且允许自动签署、机密注入、策略检查等，使 IDP 真正为企业做好准备。

另一方面，它们是新的，需要转变思维方式，特别是对于习惯于流水线思维的现有基础设施团队。此外，基于图的后端只有在规模上才有意义。如果您是一个较小的团队（少于 50 名开发人员），那么采用更简单的流水线优先后端方法可能更适合您。

## 结论

Gartner 预计到 2026 年，[80% 的企业将开展平台工程计划](https://humanitec.com/platform-engineering)。很高兴看到如此多的团队了解内部开发人员平台的潜力。但您需要正确地进行，否则您的平台计划最终可能会产生比解决的问题更多的问题。

