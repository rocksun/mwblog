在过去的六年里，[Adam Jacob](https://www.linkedin.com/in/adamjacob/)，[Chef](https://www.chef.io?utm_content=inline+mention) 的最初作者，一直在研究如何解决 Chef 和其他同代基础设施自动化工具的不足之处。

“我们发现，尤其是在大型企业中，结果并没有随着时间的推移而保持稳定，因为自动化本身的复杂性阻碍了它，”Jacob 告诉 The New Stack。

他认为，简化这种复杂性的关键在于自然语言：“我们最初的希望是，我们可以找到一种方法，允许用户用他们自己的语义，用他们自己的话，表达他们想要做什么，然后让系统通过约束来推断他们的意图。”

但直到 [生成式 AI (GenAI) 的蓬勃发展](https://thenewstack.io/generative-ai-is-just-the-beginning-heres-why-autonomous-ai-is-next/)，这一愿景才得以实现。

今天，[System Initiative](https://www.systeminit.com/)，这家 [Jacob 于 2019 年与 Mahir Lupinacci 共同创立的初创公司](https://thenewstack.io/system-initiative-a-devops-makeover-by-ex-chef-adam-jacob/)，宣布了它所称的世界上第一个 AI 原生的基础设施自动化平台。该平台允许工程师直接与 AI 代理以及彼此协作，使用 GenAI 提示来管理基础设施。

通过自然语言提示，平台用户可以盘点资源和关系。该平台将 AI 代理与实时基础设施的数字孪生配对，让用户告诉平台他们想要的结果。然后，该平台的 AI 设计一个解决方案，并在系统真实基础设施的数字孪生上运行模拟。如果解决方案不正确，用户可以在必要时对其进行迭代，并最终批准该解决方案以进行实时部署。

System Initiative 的 CEO Jacob 说：“人们使用它来解决各种问题——进行安全和合规性分析，排除生产中断、性能问题，使用自然语言部署他们的应用程序，并附加所有最佳实践。”

该平台还可以用作自动化帮助台——不仅可以跟踪支持请求，还可以创建可在几分钟内真实实施的模拟解决方案。

当 Jacob 向 TNS 展示自动化帮助台如何工作的演示时，他观察到，“我们正在与一家大型企业客户合作的 [概念验证] 基本上具有完全相同的工作流程，即当人们需要构建云基础设施时，他们所做的就是通过在 Jira 中提交工单来要求云团队构建它。”

他指出，在该企业客户中，“完成其中一张工单的平均时间为 72 天。因此，从‘我想要一些云基础设施’到‘云基础设施完成’需要 72 天。”

## 真实基础设施的数字孪生

System Initiative 公司的公告称，System Initiative 平台与“任何工作流程或触发器”集成：Terraform、[Pulumi](https://www.pulumi.com?utm_content=inline+mention)、GitOps，以及“Jira 工单、GitHub 问题或 Slack 命令，而无需重新架构现有流程。”

Jacob 说，它可以帮助工程团队在堆栈和提供商之间迁移——例如，一个团队可能在 EC2 实例上运行容器，但可以使用该平台迁移到 Kubernetes 或 Elastic Container Service。“它会为你进行翻译，”他说。

他说，这是可行的，因为该平台创建了基础设施的一对一数字孪生，而不是使用服务的抽象。“系统执行此操作的方式是，我们基本上获取他们对其自身服务的描述，为他们建模，然后将其全部拼接在一起，放入一些 AI，以找到他们在规范中未指定但在文档中指定的验证或策略，然后生成人们使用的实际模型。”

Jacob 说，数字孪生“是你正在模拟更改集中进行更改、应用策略和审查的事物。”

“而且由于这些事物是一对一的，我们不仅在性能方面，而且在清晰安全地对系统进行编程的能力方面都获得了显着提高。”

他补充说，目前，该平台仅允许用户部署到 [AWS](https://aws.amazon.com/?utm_content=inline+mention)，尽管与 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure 和 [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform 的集成已在不久的将来的路线图上。

## 轻松协作，完整的更改历史

该公司业务发展和社区副总裁 [Nick “Keeb” Stinemates](https://www.linkedin.com/in/nickstinemates/) 告诉 TNS，System Initiative 的仪表板允许用户实时查看其更改更新实时部署。

他补充说，它是为协作而构建的：“就像你使用 Google Docs 或 Figma 一样，它已内置到系统中，因此你可以与 AI 代理或你的队友无缝协作。”

Jacob 说，System Initiative 平台还允许用户查看全面的活动历史记录。“因此我们可以看到：此组件发生了什么更改的完整历史记录，无论是在此更改集中还是在其他地方？你可以看到所有原始数据。

“这使人们可以非常轻松地完成复杂的更改，并说，‘嘿，我们现在到底要做什么？’”

[![](https://cdn.thenewstack.io/media/2025/08/820bedeb-system-initiative-1024x576.png)](https://cdn.thenewstack.io/media/2025/08/820bedeb-system-initiative-1024x576.png)

System Initiative 仪表板的示例外观——基础设施的各个部分列在左侧，活动列在右侧。

Jacob 建议，创建新平台需要一种新的“AI 原生”方法，而不是遵循以前的基础设施自动化工具的步骤。Jacob 说，以旧方式做事会暴露中间的许多用户体验问题。

他说：“每次你尝试构建以这种方式工作的系统时，你都会遇到我们在遵循传统基础设施自动化的道路时所做的技术决策。”

他说，出现的一些问题包括反馈循环的缓慢以及“安全和合规性规则在最后才出现。即使它们是最关键的事情。”

System Initiative 基础设施自动化平台现在可免费试用 30 天；免费层可用于管理少于 100 个资源的小型生产环境。