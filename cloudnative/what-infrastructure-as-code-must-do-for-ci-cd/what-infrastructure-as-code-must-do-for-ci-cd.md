# 基础设施即代码在 CI/CD 中必须具备的功能

翻译自 [What Infrastructure as Code Must Do for CI/CD](https://thenewstack.io/what-infrastructure-as-code-must-do-for-ci-cd/) 。

在 Pulumi 的虚拟用户大会上，演讲者深入探讨了哪些 IaC 功能能够最大程度地提升快速软件开发的效益。

![](https://cdn.thenewstack.io/media/2023/06/b65da64b-continuous-delivery-1-1024x576.jpg)
*Image by [Rowan Freeman](https://unsplash.com/@rowanfreeman?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) from Unsplash*

[基础设施即代码（IaC）](https://thenewstack.io/infrastructure-as-code-modernizing-for-faster-development/)的使用可以通过命令行在各种环境中以一致且高效的方式进行基础设施的规划和部署，非常适合 [CI/CD](https://thenewstack.io/ci-cd/) 。通过在生产流水线中应用 IaC ，组织报告称提高了生产效率并实现了资源节约。

然而，并非所有的 [IaC](https://thenewstack.io/infrastructure-as-code-evolution-and-practice/) 解决方案都是相同的。潜在的 IaC 用户应仔细审查特定解决方案是否真正能改进 CI/CD 流程以及如何改进。

一个 IaC 解决方案应该为 CI/CD 提供以下功能：

* 自动化的规划和部署。
* 不可变的版本控制，即使用单一代码库创建和删除基础设施。
* 在整个 CI/CD 过程中进行测试。
* 设置策略的能力。
* 管理[安全性](https://thenewstack.io/security/)的能力。

基础设施即代码提供的不变性在 CI/CD 中非常重要。企业管理协会（EMA）的分析师 [Torsten Volk](https://www.linkedin.com/in/torstenvolk) 告诉 The New Stack ，它之所以具有重要地位，是因为它确保了一致性、清晰的审计路径以便于回滚、统一的安全和合规性控制，以及整体的效率。

在 [PulumiUP 虚拟会议](https://www.pulumi.com/pulumi-up/)上，讨论的重点是适用于 CI/CD 的合适 IaC 解决方案应该提供哪些功能以及为什么。这是 Pulumi [每年一度的用户大会](https://thenewstack.io/pulumi-new-features-for-infrastructure-as-code-automation/)，于 6 月 15 日举行。

## 灵活的编程语言选择

Pulumi 在基础设施即代码（IaC）方面的方法似乎有助于其快速增长的采用率。根据 EMA 的数据，尽管竞争对手 Terraform 声称在市场份额上几乎是 Pulumi 的 10 倍，但 Pulumi 的市场份额增长速度约为 Terraform 的 2 至 3 倍。

Pulumi 提供选择编程语言的灵活性是关键所在。例如，今天许多用户不幸地仅限于在部署中使用 YAML ，这本不应该是这样的；开发人员不应被限制在一种语言上。

另一方面， Pulumi 声称支持所有主要编程语言，因此提供了更多的选择自由和更直接的方式来为 CI/CD 和一般情况下进行基础设施规划。

“ Pulumi 是你喜欢的语言中的 IaC - 对于熟悉 IaC 的人来说，可能有使用其他使用特定领域语言甚至标记语言（如 YAML 或 JSON ）的工具的经验，通常这对于入门来说是可以接受的，”  Pulumi 的首席执行官兼创始人 Joe Duffy 在 PulumiUP 的主题演讲中说道。“但特别是当我们扩展到现代云架构时，问题就开始显现出来了。”

因此，Pulumi 采取了不同的方法：使用你喜欢的编程语言，无论是 JavaScript 还是 TypeScript 、 Python 还是 Go 。 Pulumi 的核心是多语言的。这意味着你可以利用编程语言的丰富功能来表达你的基础设施即代码。

在 Pulumi 的情况下，Duffy 说，采用基础设施即代码并不意味着你的组织必须放弃在 GitHub 或 GitLab 上进行拉取请求等与 CI/CD 集成的操作。

Duffy 说：“如果你已经在 GitHub Actions 上进行 CI/CD 或在 GitLab Pipelines 上进行 CI/CD ，你只需利用现有的流程进行改变，将其从应用程序交付变为基础设施交付。当然，还可以与 Docker 和身份提供者（如 Okta ）集成。”“结果就是，云计算从枯燥乏味变成了高效率 - 你可以在更短的时间内完成更多的工作，而且也更有乐趣。”

Duffy 表示，生产力的提高可以“实际上是数量级的改变”，并补充说 Pulumi 可以在不到 15 行代码的情况下部署 Amazon Web Services 上的弹性 Kubernetes 服务集群。

他说：“我们不是在谈论 10% 的提升。”“你会感觉自己编码速度更快，完成更多工作，并且在开发环节更加紧密。”

## 基础设施即代码的扩展能力

此外， Pulumi 的目标是帮助公司扩展其业务。虽然使用 Pulumi 很容易入门，但其理念是能够支持跨不同环境部署的 CI/CD 团队。

在这种情况下，基础设施即代码应该包括确保在多云或不同环境中的合规性、标准化和安全性等任务。它应该作为一个统一的接口，简化管理过程，无需使用多个工具或接口。

Duffy说：“也许你已经有了一个开发环境，接下来你会考虑进入生产环境。”“这就是你开始思考标准化的时候。当只是为一、两个或三个开发人员提供基础设施即代码时，情况与在整个团队中采用基础设施代码截然不同。”

在 Starburst Data ，Pulumi 主要用于执行复杂的 CI/CD 工作流程， Starburst 的高级首席软件工程师 Matt Stephenson 在一次会议演讲中表示。

Starburst 的基础设施需求非常复杂而广泛，覆盖了 20 个不同的云区域，并通过不同的云提供商进行部署。在 CI/CD 工作流程中， Pulumi 帮助支持了非常复杂的回滚过程， Stephenson 说道。

他说：“我们希望我们的基础设施是无处不在的和易于接近的。”“我们希望所有的工程师都能够自如地进行更改，以便为他们的产品变更提供所需的基础设施。”

## AI 组件

最近，人工智能展示了在不久的将来如何在使用基础设施即代码进行 CI/CD 时发挥关键作用。

Volk 告诉 The New Stack ：“ AI 集成可以让开发人员选择他们偏好的开发语言，并允许他们以简明的英语来定义目标基础设施环境，然后使用[Chat]GPT自动生成所需的代码来建立环境。”

通过 Pulumi Insights ， Pulumi 广泛使用 ChatGPT 功能。在会议之前，Pulumi 的市场副总裁 Aaron Kao 进行了一次演示，展示了如何使用基本的英语对话命令向 Pulumi Insights 提出查询，并获取有关跨多云环境部署的 Kubernetes 集群等复杂环境中基础设施的可操作信息。

Kao 展示了如何以简单的英语输入请求，例如“我想要一个 S3 存储桶、一个 API 网关和一个 Lambda 函数。我想构建一个动态的无服务器网站。但如果你不知道，就给我一个静态网站放在 CDN 后面。”

结果是，“它会直接生成一个能让你完成 80-90% 工作的程序”， Kao 说道。

毫无疑问，人工智能将在不久的将来对 CI/CD 和基础设施即代码产生重大影响。因此，今天为开发人员提供的基础设施即代码工具应该看起来和感觉上都与以往大不相同。

Pulumi 的首席技术官 Luke Hoban 在会议小组讨论“人工智能与云开发的未来”中表示：“这些系统与我们过去所习惯的软件构建方式不同，我们构建和测试的方法也非常不同。”

他说：“我非常关注这个领域的发展，以及我们如何学习一套新的技能来构建不同类型的软件。”

