## 平台工程：什么是“好”？

![平台工程的特色图片：什么是“好”？](https://cdn.thenewstack.io/media/2024/04/24accaaa-steps-1024x561.png)

为了改善开发人员体验，越来越多的组织希望通过平台工程来减少繁琐工作，专注于创收功能和创新。

平台工程带来了两大主要好处。第一个是引入了自助服务功能，允许组织中的人员尝试新的软件。第二个是纳入了自动化基础设施运营，确保在管理良好的环境中进行实验。

这些好处非常显着，以至于 [Gartner](https://www.gartner.com/en/articles/what-is-platform-engineering) 估计，到 2026 年，80% 的大型软件工程组织将建立 [平台工程](https://thenewstack.io/platform-engineering/) 团队。但炒作的背后是什么？

### 什么是平台工程？

平台工程方法补充了 [DevOps](https://thenewstack.io/devops/)。该“平台”是一个内部环境，创建为开发人员构建和运行软件（例如应用程序、工具和工作流）的空间，且该环境安全且合规。

平台工程的主要目的是在降低安全性和可用性风险的同时，有效地扩展开发人员的工作。开发人员平台解决了大规模开发可能带来的巨大成本和复杂性。这些成本最常见的原因是开发人员为每个项目（甚至项目中的各个测试用例）启动单独的环境。另一个好处是，由于能够自动化在统一平台中工作的操作流程，因此能够大规模工作的可能性增加了。

为了使这种方法取得成功，必须在同一平台内部署软件。表面上看，这可能使平台工程方法看起来像是对生产力的限制，但它实际上可以释放开发人员的创造力，并显著减少日常繁琐工作。

### 构建与购买：组织如何实施？

平台工程要取得成功，必须正确实施平台。由于组织对其平台需要定制化，因此不可能简单地购买现成的产品。同时，有大量的点产品和开源项目可用于解决在生产中部署和运行软件时出现的无数基础设施、CI/CD、安全性和其他“待完成工作”。

这意味着组织反而需要对其购买的产品或已采用的开源软件进行一些工程工作。但问题是：自己设计多少才是合适的？平台工程可能会分散对业务目标的注意力，而不是推动这些组织与众不同之处。

解决此问题的办法是让组织构建尽可能精简的平台。平台工程团队不应从头开始构建；平台应构建在其他平台之上。组织不希望其软件团队完成所有工作，从插入服务器到交付产品，他们当然不应期望平台工程团队从头开始完全实施平台。

相反，这些团队需要在巨人的肩膀上构建。为了推动这种方法，组织应尽可能多地购买平台即服务 (PaaS) 和软件即服务 (SaaS) 工具，并将这些工具捆绑在一起以构建一个完成且可行的平台。维护、集成和更新最基本的平台体验的工作已经足够多了。这包括构建内部工程师将使用的界面和 API，这可以减轻供应商锁定。

在此模型中，每个组织的平台都是定制构建的，但它位于现有、受支持、可购买的工具之上。通过这种方法，组织可以摆脱构建与购买的两难境地，并专注于微调其平台以满足其组织的需求。

### 它要成为常态，需要发生什么？

许多组织在采用 DevOps 时遇到了困难，因为角色和职责似乎令人难以承受。如果开发人员负责其堆栈中的所有内容，每天都在生产中，他们可能会陷入无法提供业务价值的繁琐工作中。但传统的架构和运营团队通常不会衡量开发人员的效率，因此开发人员只能提交工单并等待。

平台工程要取得成功，需要组织的全面支持。为了为内部用户构建更好的体验，需要消除孤岛。平台工程需要自己的团队才能成功；它不能仅仅被视为 IT 的延伸。
**平台工程：超越操作变更**

除了操作变更之外，平台工程还要求开发团队在文化上发生转变，除了各个功能之外，还要优先考虑可用性和安全性等非功能性需求。平台应帮助将正确的事情变成容易的事情，但精益平台团队及其用户（软件开发团队）之间应分担责任。

与组织对其工作流程进行全面改革时的情况一样，半途而废是不够的。如果没有组织中每位开发人员的全力支持以及高级团队成员的支持，企业将无法成功实施平台工程。

**为什么开发人员应该关心？**

对于大型软件工程组织来说，拥有庞大而复杂的技术堆栈很容易。这会使维护成为一场噩梦，并导致漫长、缓慢的发布周期和压力重重的中断。采用平台工程用一个精简得多的堆栈来换取复杂性，移除不重要或繁琐的部分。决策者必须不怕停用工具或关闭他们不需要的环境——甚至在开发人员信任他们正在使用的平台后自动化此过程。事实上，自动化可以使停用成为平台生命周期的一部分，将其纳入现有流程以节省时间和金钱。

平台工程方法还可以为开发人员以及基础设施和运营团队节省大量时间。这些团队可以消除开发人员的整个类别的例行请求。平台团队自动化例行、重复的任务，例如启动新环境、管理基础设施、创建和配置存储库以及处理 CI/CD 管道以平滑开发周期并减少繁琐工作。

开发人员可以通过将工作卸载到平台来节省时间和工作量，这可以提供将现有应用程序迁移到平台的主要动力。随着开发人员的生产力提高，这些好处还可以为企业带来可观的成本节约，从而无需额外的承包商和人员扩充服务。

**面向未来的平台工程**

最终，平台工程的目标是鼓励开发人员（无论其团队或职能如何）使用平台，而不是在平台之外进行试验。在完全实施工具链和工作流的此设置框架内工作时，开发人员可以专注于编码，而无需担心基础设施。这极大地减少了他们的日常工作量，让他们能够蓬勃发展，而不仅仅是生存。

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。