# 解决中心团队 DevOps 税至关重要

在 [DevOps](https://thenewstack.io/devops/) 文化中，开发人员负责部署和维护支持其编写的应用程序代码的基础设施。虽然许多人将 DevOps 文化的兴起视为生产时间大幅度提高的重大改进，但对于开发人员和支持他们的团队来说，都存在着隐藏的成本。

在 DevOps 中，现在期望开发人员成为以下方面的专家：

- 他们的核心应用程序专业领域（后端、前端）。
- 各种异构云服务及其如何协同工作。
- [基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) 配置和部署。

这些对开发人员责任的改变导致开发人员不堪重负，并以牺牲其他中心团队为代价造成了巨大的噪音。

## DevOps 税

鉴于从本地部署到云服务的转变，中心团队现在存在于 [管理公司云平台](https://thenewstack.io/cloud-management-platforms-need-robust-automated-integration/)。这些团队被称为平台、基础设施、基础设施或 DevOps，负责云平台的稳定性。相反，他们将时间花在支持开发人员上，而牺牲了可用性、可靠性和可扩展性。

中心团队将时间花在两个主要领域：在开发人员 [部署和对配置不当的基础设施进行故障排除或排查](https://thenewstack.io/tutorial-configure-deploy-an-edge-application-on-cloud-native-edge-infrastructure/) 时，为他们提供指导和帮助。

这在整个组织中累积起来。一家大型金融科技公司报告称，每周支持 40 个手动请求，每周数百小时，用于触及关键应用程序的基础设施。

中心团队陷入了单次请求模式，牺牲了他们的未来，以度过每一周。整体正常运行时间、性能和支持服务的强大目录等关键优先事项被忽视。

下游影响包括整体系统退化、配置错误和对性能的影响。这会导致面向客户的停机、停机甚至事故。

## 解决问题的当代尝试

这些影响并没有被忽视，并且有机解决方案已变得流行。其中最值得注意的是 HashiCorp 的 [Terraform 模块](https://developer.hashicorp.com/terraform/language/modules)。模块提供了一种创建基本 Terraform 模板的格式，这为用户在部署云基础设施时提供了一些指导。但是，模块有一些缺点，这些缺点并不立即显而易见。

特别是，Terraform 模块：

- 要求用户了解 Terraform。
- 隐藏了最终可能产生影响的复杂性。
- 不允许对底层 Terraform 进行编辑。
- 没有内置的 UI。
- 通常文档质量很差。

模块是类似的方法，依赖于抽象或修改现有工具，这会导致有限的改进和类似的问题：云稳定性、开发人员痛苦和水下中心团队。

## 需要一种新方法

公司 [需要重新评估他们的 DevOps](https://thenewstack.io/devops-needs-security-champions/) 流程和文化如何影响他们的业务。按现状继续下去将导致 [开发人员生产力下降，而中心团队](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/) 积累了无休止的技术债务。

随着一次性请求继续优先，对可用、可靠和可扩展的云平台的投资将被抛在脑后。想要长期成功并摆脱开发人员税的组织应该：

- 优先考虑关键服务，并放弃对无关紧要服务的支持。
- 专注于关键服务的自动化。
- 使最佳实践易于遵循，并提供黄金模板和合理的默认值。
- 采用可扩展的思维方式，摆脱故障排除的循环。

## 真实案例

当我还在 Netflix 工作时，我们在各个中心团队（安全、平台、网络等）中采用了这种新方法。以下是一些将合理的默认值和自动化嵌入到实际项目中的示例，帮助开发人员避免上下文切换和专业化的需求。

**ConsoleME**: Netflix 的身份和安全团队以前收到过许多关于创建和配置 IAM 的请求。他们创建了一个向导，最终成为一个 [流行的开源项目](https://github.com/Netflix/consoleme)。
**Repokid** [是我在 Netflix 创建的一个开源铺路项目](https://github.com/Netflix/repokid)，用于实现最小权限。它甚至不需要开发人员与之交互。
**Spinnaker**: 这可能是最著名的例子，[Spinnaker](https://github.com/spinnaker/spinnaker) 会自动创建开发人员在应用程序周围需要的一切（VPC、安全组、IAM 等）。
## S3 Slackbot

我们创建了一个 S3 Slackbot，它可以根据开发人员选择的选项自动创建配置正确的 S3 存储桶。这是一个非常成功的例子，我们没有开源。

## 由 Mantis 提供支持的警报和监控

Netflix 基于开源工具 Mantis 创建了一个框架，开发人员可以简单地将其放入他们的代码中，以获得带有自动日志记录的仪表板。

## 结论

虽然 DevOps 文化对软件是其核心产品的企业来说是短期利好，但也导致了中央团队的债务积累，这可能会给依赖可用、可靠和可扩展云主干的企业带来厄运。

公司应该借鉴 Netflix 的例子，采用现代方法。这些方法自动扩展中央团队，而不是期望这些团队随着开发人员基础的线性增长而增长。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。