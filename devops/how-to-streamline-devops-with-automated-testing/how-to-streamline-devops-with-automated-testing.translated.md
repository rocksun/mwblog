# 如何通过自动化测试简化 DevOps

![关于如何通过自动化测试简化 DevOps 的特色图片](https://cdn.thenewstack.io/media/2024/09/3ee66063-christopher-gower-m_hrflhgabo-unsplash-1024x682.jpg)
[Christopher Gower](https://unsplash.com/@cgower?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在
[Unsplash](https://unsplash.com/photos/a-macbook-with-lines-of-code-on-its-screen-on-a-busy-desk-m_HRfLhgABo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 上。

在 [DevOps](https://thenewstack.io/devops/) 中，能够快速发布软件至关重要。测试对于发布至关重要，开发人员必须经常且迅速地执行此任务。目标是在发布进入生产环境之前找出并解决错误，对哪些软件可以继续开发或应该完全放弃进行分类。

这就是将 [测试阶段](https://thenewstack.io/what-is-testops-drawing-parallels-to-devops/) 纳入开发流程至关重要的原因。但要正确执行，您需要自动化工具，这些工具取决于应用程序。JUnit 或 Jest 已被证明对代码和组件单元测试有效。Newman 在 API 公共方法方面表现出色。Cypress 在端到端测试 (E2E) 中表现最佳。为了让利益相关者了解情况，TestRail 的报告提供了有关进度的自动更新。

此外，测试不再仅仅是质量保证 (QA) 的领域。工程人员不仅应该参与其中，而且必须共同承担责任。这种结构在立即纠正问题之前，在投入大量时间和金钱之前，可以可靠地提供最佳结果。测试不仅可以推动 [持续软件交付](https://thenewstack.io/continuous-delivery-gold-standard-for-software-development/)，而且使用自动化可以完全消除人为错误。

**概念性思考**

[测试金字塔](https://thenewstack.io/is-the-testing-pyramid-broken/) 是一个用于指导软件开发流程的框架。它包含几个明确针对功能、性能和可靠性的测试层，其有效性因各种原因而受到称赞。

[单元测试](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/) 易于执行，因为它们专注于单个工作单元，无论是方法还是组件。它们成本低廉且易于执行，提供了一种经济高效的方式来保护代码质量。在构建阶段执行这些操作是获得最大结果的最佳方式。

还有集成和 API 测试，它们验证应用程序与系统集成的能力。毕竟，如果无法集成，应用程序将受到严重限制，客户从一开始就会受到阻碍。

然而，最具影响力的还是 UI E2E 测试。这需要完全集成您的系统，从前端到后端，从数据库到网络。它们不仅需要更多时间和维护，而且是所有测试中最昂贵的。您需要特别注意 E2E 测试：[过度配置](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/) 将导致高成本，并颠倒测试金字塔。

通过按此顺序进行测试（从最小的范围扩展到最大的范围），组织可以确保其范围集中在所需领域，并且其成本和范围不会意外地从适当的关注领域扩展，至于谁负责什么，开发人员应该被分配编写单元和集成测试。同时，QA 应该进行 UI E2E 测试。但是，请确保实际的产品所有者提供场景。

**正在开发的案例**

让我们检查一个实现示例，看看现成的工具如何执行测试。在本例中，我们将使用 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS)。

首先，有 AWS CodePipeline 用于完全 [管理持续交付](https://thenewstack.io/managing-compliance-with-continuous-delivery/)，它构建管道，同时协调基础设施和应用程序更新。这与他们的 AWS CodeDeploy、CodeCommit 和 CodeBuild 产品以及 GitHub 等主要第三方操作提供商配合得特别好。这使 AWS CodePipeline 能够提供更强大的功能。

例如，检测选项可以创建与工件源位置绑定的管道，从而简化从功能描述到风险评估的任务。默认情况下启用的禁用转换功能还可以自动链接管道阶段。如果您不想进入下一阶段，请单击“禁用转换”，管道活动将被停止。
AWS CodePipeline allows users to edit pipelines to introduce new stages, provide updates, or eliminate stages. Additionally, the editing page allows you to add actions in sequence or alongside current activities, adding flexibility and enabling pipelines to grow quickly. There is even an approval feature for improved pipeline management, allowing activities to be automatically stopped without specific approval.

**You Can't Cheat Testing**
There are no excuses for releasing applications that have never been tested. Seek out tools that automate processes and eliminate the risk of human error. Also, remember to make [testing a shared responsibility in your organization](https://thenewstack.io/how-the-worlds-top-organizations-test/) and part of your culture.

You can't cheat testing, and you don't want to cheat—you need to pass, or you'll fail miserably. Bulletproof products never miss the opportunity to attract customers and bring higher profit margins.

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
Technology is moving fast, don't miss an episode. Subscribe to our YouTube channel to stream all our podcasts, interviews, demos, and more.