<!--
title: 通过去中心化测试提升开发速度
cover: https://cdn.thenewstack.io/media/2024/01/661cb5cf-moving-traffic-microservice-testing-1024x684.jpg
-->

将测试工作前置，是消除过度依赖集中式测试造成的低效问题的最佳途径。

> 译自 [Improve Developer Velocity by Decentralizing Testing](https://thenewstack.io/improve-developer-velocity-by-decentralizing-testing/)，作者 Nočnica Mellifera (她/她的)在转入开发人员关系之前是一个开发人员，已经有 7 年的经验。她擅长容器化工作负载、无服务器和公共云工程。Nočnica 一直是开放标准的倡导者，并就......发表过演讲和研讨会。

正如我在最近的[一篇文章中](https://yylives.cc/2024/01/14/we-need-a-new-approach-to-testing-microservices/)讨论过的那样，集中化测试会干扰开发者的速度。在以[微服务为导向的模式](https://thenewstack.io/microservices/)中，集中化测试已成为发布流程中的一个“瓶颈”，因为开发代码和管理生产操作已经被有效地民主化并且它们的功能被隔离在更小的团队中。问题不在于工具本身。事实上，现代测试工具赋予团队惊人的能力，可以检测到以前会由最终用户发现的问题。问题在于太多问题没有在最终端到端(E2E)测试和验收测试之前被发现。

这可以理解，因为现代微服务之间的相互依赖以及对外部 API 的依赖使得模拟代码如何在生产环境中运行变得比以往更加困难。虽然预生产测试阶段应该只检测到罕见的、新出现的故障，但现在这个阶段往往是您第一次明确了解代码是否可用的地方。我还记得分段测试阶段曾经是运行代码最可靠的地方，因为那里只运行经过良好验证的版本——我们没有生产环境的规模问题。但是从阅读 Reddit  [r/qualityassuranc](https://www.reddit.com/r/QualityAssurance/)e 和 [r/softwaretesting](https://www.reddit.com/r/softwaretesting/) 论坛中表达的[关注](https://www.reddit.com/r/devops/comments/16carej/how_many_environments_is_enough/)来看，对许多团队来说，分段已经变得非常不可靠，因为许多版本由缺陷延迟。

## 集中化测试减缓开发者速度的 6 个原因

集中化测试可能会显著[阻碍开发者的速度](https://thenewstack.io/7-reasons-why-developer-experience-is-a-strategic-priority/)。让我们来分解与这种方法相关的问题。

- **在分段环境上进行批量部署**: 当几个团队或微服务的代码更改被批量打包并部署到分段环境时，会产生瓶颈。这种方法延迟了新代码的集成，如果出现问题，很难确定是哪个更改导致了问题。

![](https://cdn.thenewstack.io/media/2024/01/f303d99f-decentralized-testing.png)

*这就是批量处理正在迅速成为常态的原因。*

- **测试频率和提交冻结**: 如果批量测试的频率不高，且在此期间新提交被禁用，这会导致反馈循环的显著延迟。开发人员必须等待更长时间来查看他们的更改在准实时环境中的表现，这减缓了整体开发流程。

- **端到端测试**: 当端到端测试仅由 QA 团队进行时，它通常会变成黑盒测试。不了解底层系统的工作方式意味着不太可能彻底测试失败的可能点。虽然端到端测试至关重要，但仅依靠 QA 团队进行此类测试可能会在开发和测试之间产生脱节。

- **错误报告和解决流程**: 发现错误时，需要正式提交错误报告，然后开发人员必须重现并修复这些错误。此流程本质上比较缓慢。提交、分配、重现、修复然后重新测试错误所需的时间可能相当可观，特别是如果错误难以捉摸或间歇性出现。此外，正如上面提到的黑盒问题，运行测试的工程师只能描述行为，而不了解底层系统。这为错误报告流程增加了摩擦。

- **功能验收测试过晚**: 当功能验收测试发生在开发周期后期时，可能会导致陡峭的延迟。如果在此阶段收到反馈或需要更改，则可能需要开发人员大量重新工作。这不仅会延迟当前功能的发布，还会影响其他功能的开发计划。

- **累积延误和士气下降**: 这些延误会积累，导致更长的发布周期。这不仅会通过延迟上市时间影响业务，还可能降低开发团队的士气。开发人员通常更喜欢快速的反馈循环，并希望尽快在生产中看到他们的工作成果。

虽然我认为列出这些缺点很重要，但我不认为任何人明确支持“高度集中化测试”或“只在分段/测试环境上进行测试”。没有人刻意破坏开发人员单元测试和端到端测试的可靠性，但模拟每个开发人员的生产集群的复杂性产生了这种结果。(我之前的文章详细描述了这个系统的演变。)

## 如何再次去中心化测试

我们想要做的是向左移动测试: 让现实的测试可以直接在[拉取请求(PR)阶段开始](https://thenewstack.io/the-struggle-for-microservice-integration-testing/)，而不是等待在一个独立团队使用我们的代码时再进行测试。在 [Uber、DoorDash](https://www.signadot.com/blog/how-uber-and-doordash-enable-developers-to-test-in-production) 和 [Lyft](https://www.signadot.com/blog/large-engineering-teams-testing-on-k8s) 等团队，平台工程师已经建立了让开发人员在更现实的环境中更早地测试的工具。在这些公司，解决方案不是调整一个所谓的“开发人员环境”，而是给所有用户访问一个与生产状态非常接近的共享集群。

具体来说，这些平台工程师正在使用[请求隔离](https://www.signadot.com/blog/transforming-kubernetes-developer-environments-the-shift-to-request-level-isolation)来让一个服务的单个测试版本(或者如果需要的话是一组服务)与集群交互而不与其他人的实验相冲突。在 Uber，这个系统称为 SLATE，它隔离测试服务，让它们与特殊标记的请求进行交互，而其余部分依赖生产服务。(是的，这允许 Uber 工程在生产中进行测试，但它有大量的安全保护措施。)

![](https://cdn.thenewstack.io/media/2024/01/78409487-uber-slate-architecture.png)

然而，无论如何实现，这个系统都可以让开发人员在复制过程更早的阶段就针对集群的其他依赖项测试他们的代码。在过去的几年中，这个能力实际上只对具有大型专门平台工程团队的企业团队开放。使用像 [Signadot](https://www.signadot.com/docs/overview) 这样的服务，大型团队可以使用一套标准工具来隔离请求，以实现请求隔离并向左移动测试。

这也可以在组织内导致文化转变: 被授权更早地运行端到端和验收测试，开发团队可以集成之前集中在 QA 团队中的专业知识。随着他们帮助产品工程师测试更多更准确的东西，我们甚至可能会看到 QA 工程师向左转移。

## 去中心化测试的 5 个好处

用于开发人员实验的请求隔离系统需要大量的技术投入，而不仅仅是部署几个开源软件包那么简单。它还需要与 CI/CD 工具集成。这不是本文的重点，但我提到它是因为在您开始这个旅程之前，这些好处值得列出。

针对准确依赖项的更早测试:与尝试复制集群的某个版本不同，具有请求隔离的共享集群允许每个团队独立地使用其他团队工作的最新、稳定版本进行测试。

白盒测试:由开发测试他们编写的代码，他们可以更快地理解可能导致问题的原因，并且他们对什么发生了变化的了解使得他们更容易知道测试的重点。

测试可以跨类型进行:功能测试和非功能测试可以同时运行，例如验收测试与监控内存泄漏、CPU 使用率和性能测试一起运行。

开发人员可以根据需要对 PR 进行分组:像 Signadot 这样的服务允许您选择多个 PR 共同处理。因此，如果团队 A 和团队 B 有同步的更改，两者可以在 QA 参与之前一起测试。

无需提交错误:这个软性、无形的好处实际上是对开发人员生产力的最大提升之一。在不需要手动记录每个问题并将其发送给另一个团队的情况下，最初编写该功能的开发人员可以立即着手修复该错误。

将更准确的集群置于开发人员手中的更新的去中心化测试方法具有许多优势，这些优势可以带来更好的开发速度和一个更快乐的团队。

## 目标不是“修复”测试，而是逐步改进质量

虽然实施像请求隔离这样的系统需要投入，但与对代码测试和运行的集群架构或环境进行更改相比，它有一个巨大的优势:可以递增地采用。想一想:在生产环境之前，每个工程团队都有一个高度准确的集群，但他们不希望通过将实验代码推送到服务来破坏它。通过请求隔离和智能请求路由，可以在此集群中测试 PR，即使只有您的团队可以访问此类系统。您的实验不会破坏底层集群，因此小组可以在向整个团队展开之前先试用此系统。

## Signadot 如何提供帮助

Signadot 允许您独立验证每次代码更改。通过连接到源代码控制中的 PR，每个 PR 都可以在集群内获取一个请求隔离的空间，以测试此新版本将如何与集群的其余部分进行交互。

如果您想了解更多信息，分享反馈或与已经使用请求隔离来加速开发人员工作流程的惊人社区见面，请加入 [Signadot Slack 社区](https://signadotcommunity.slack.com/ssb/redirect#/shared-invite/email)与团队联系。
