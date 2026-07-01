在经过一段[简短的公开预览](https://aws.amazon.com/blogs/aws/modernize-your-workflows-amazon-workspaces-now-gives-ai-agents-their-own-desktop-preview/)后，AWS于周二正式发布了[Amazon WorkSpaces for Agents](https://aws.amazon.com/workspaces/ai-agents/)——请务必不要将其与[Amazon Connect Agent Workspace](https://aws.amazon.com/products/connect/customer/agent-workspace/)混淆。Amazon WorkSpaces是AWS为希望向员工提供虚拟桌面的企业所打造的持久化云桌面服务。WorkSpaces for Agents同样是虚拟桌面，但专门为需要操作云端桌面应用程序的代理（Agents）而设计。

## 代理拥有专属桌面

理想情况下，这意味着代理现在可以直接与企业的传统桌面应用程序进行交互，而无需构建自定义集成或对这些工具进行现代化改造。

AWS此项发布的参考客户是荷兰跨国公司Wolters Kluwer。

“我们的团队在全球范围内管理着复杂的税务、法律和合规工作流程。Amazon WorkSpaces现在让我们能够将AI代理直接植入这些工作流程中——它们可以访问并操作我们员工使用的相同业务应用程序，而我们无需进行任何重构，”Wolters Kluwer工作场所技术总监André Akkerman在今天的公告中指出。“对于我们如何思考自动化，这是一次有意义的进步。”

一旦启用，代理即可在模型上下文协议（Model Context Protocol，简称MCP）的帮助下连接到这些桌面。在此之后，它们可以流式传输会话，并根据需要与桌面应用程序交互。访问权限由AWS的身份和访问管理（Identity and Access Management）服务进行管理，审计能力则由AWS CloudTrail和Amazon CloudWatch处理。

## MCP + 计算机视觉

AWS认为，MCP和计算机使用代理（由于它们必须不断循环分析截图并采取行动，速度仍然较慢）是互补的方法。

AWS目前实现这一功能的方式是：当用户创建服务的主操作系统镜像时，在他们的WorkSpace上安装一个文件系统MCP服务器。有了它，代理就可以通过工具调用来读取和写入文件，而无需经过截图循环。

“正确的设计模式是将每个子任务路由到可用的最高效接口——在存在MCP工具时调用它，仅在没有API覆盖该任务或与图形用户界面（GUI）交互本身就是目标时，才回退到视觉驱动的操作，”该公司在公告中解释道。“这有一个叠加的好处：当大部分工作流程通过MCP路由时，剩余的视觉子任务就会缩小为重点操作——步骤更少、序列更短、故障更少。MCP工具转发使得这种模式能够在WorkSpaces应用程序实例中发挥作用。”

## 人工掌控

随着该服务正式进入通用可用阶段，AWS还增加了人类实时观察代理并在需要时接管控制权的能力。

“如果你观察到代理执行了意外的操作，停止按钮可以直接进行干预，而无需重启会话或回滚状态。当你从开发阶段转向生产环境时，你可以根据任务所需的人工监督程度，决定哪种模式适合每个工作流程，”该公司解释道。

鉴于目前计算机使用代理的速度仍然很慢，没有人愿意长时间监管这些代理，这也不是薪水的合理使用方式。因此，如果某个特定任务现在需要大量的监督，那么这可能不是该工作流程的最佳前进方向。

## 给代理一个身份

通过此次发布，AWS还允许企业使用Active Directory为代理提供一个身份——包括相应的策略、访问控制和审计日志——这些都是公司已经为普通用户所使用的。