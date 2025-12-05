[亚马逊云科技](https://aws.amazon.com/?utm_content=inline+mention) 推出了三款 [AI 代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/)，旨在 [软件开发生命周期](https://thenewstack.io/ai-agents-are-finally-starting-to-revolutionize-the-software-development-lifecycle/) 中自主工作。

此举标志着从需要持续人工监督的工具转向能够作为团队成员独立运作的代理。亚马逊云科技在今天的 [AWS re:Invent](https://reinvent.awsevents.com/) 大会上公布了这些被称为“前沿代理”（frontier agents）的代理。亚马逊云科技表示，这三款目前处于预览阶段的代理，很可能只是众多代理中的第一批。前沿代理可以在任何领域或行业创建。

据亚马逊云科技介绍，这三款前沿代理——[Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) 自主代理、AWS 安全代理和 AWS [DevOps](https://thenewstack.io/introduction-to-devops/) 代理——可以数小时或数天无需人工干预地运行，同时处理多项任务，并朝着广泛的目标努力，而不是需要一步一步的指示。

“直到现在，这个领域的许多开发者工具都主要是‘人在回路中’，”亚马逊云科技代理式人工智能总经理/总监 Amit Patel 告诉 The New Stack。“通过这些前沿代理，我们计划让它们能够自主工作，无需开发人员的干预。”

亚马逊云科技表示，[AI 编码助手](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/) 加速了单个任务，但也带来了新的摩擦，因为它要求开发人员充当将工作联系在一起的“人为线索”——在切换任务时重建上下文，手动协调跨存储库的更改，以及将分散在工单、拉取请求和聊天线程中的信息整合起来。

“通过这些前沿代理，我们计划让它们能够自主工作，无需开发人员的干预，”Patel 说。

据该公司称，亚马逊云科技通过观察自己的开发团队在亚马逊规模下构建服务来开发这些前沿代理。出现了三个洞察：团队可以从照看每一个小任务转向指导代理实现广泛成果；速度与可以同时运行的代理任务数量相关；代理独立运行的时间越长越好。Patel 说，公司意识到需要在整个软件开发生命周期（而不仅仅是编码）中具备这些能力，否则就会面临创建新瓶颈的风险。

“你可以把这些代理看作是团队的成员，而不仅仅是开发人员日常使用的工具。”

这些代理的行为就像团队的另一个成员。它们会随着时间学习。它们会记住团队如何处理特定事务、特定问题、错误修复或路线图项目，然后根据这些学习采取行动并提交拉取请求，以便其他团队成员可以审查并接受，Patel 指出。

“随着时间的推移，它会学习，它有记忆。所以它会不断学习，不断进步——就像你把一个初级工程师带到团队中一样，”他说。“随着时间的推移，他们会越来越好，他们会了解团队的工作方式，并适应团队的工作方式，然后他们就能更有效率。”

## Kiro 自主代理：您的虚拟开发者

亚马逊云科技表示，Kiro 自主代理在不同会话中保持持久上下文，并不断从拉取请求和反馈中学习。它能够处理从分类错误到提高 [代码覆盖率](https://thenewstack.io/ai-testing-more-coverage-fewer-bugs-new-risks/) 等任务，单个更改可以跨越多个存储库。

开发人员可以直接通过 GitHub 提出问题、描述任务或从待办事项列表中分配工作。代理独立决定如何完成工作，以提议的编辑和拉取请求的形式分享更改，从而让开发人员保持对所合并内容的控制。

“这个想法是，你可以给它一个简单的任务，比如，监控我的 GitHub 上的问题，一旦出现就解决它们并提交拉取请求，”Patel 解释说。“你可以想象，早上你来上班时，代理在一夜之间已经查看了 10 个不同的问题，提交了 10 个不同的拉取请求，然后你可以决定是否合并它们。”

该代理与存储库、管道以及 [Jira](https://thenewstack.io/why-developers-hate-jira-and-what-atlassian-is-doing-about-it/)、[GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/) 和 [Slack](https://thenewstack.io/slack-takeaways-from-this-weeks-service-outage/) 等工具集成，在工作进展中保持上下文。每一次代码审查、工单和架构决策都会丰富代理的理解，使其随着时间的推移对团队更有用。

## AWS 安全代理：将安全左移

Patel 表示，安全团队面临双重挑战：在整个开发过程中主动识别风险，同时在问题出现时迅速响应。当前的工具通常提供通用建议，而渗透测试耗时过长，无法跟上快速发展的开发团队。

他指出，AWS 安全代理将安全专业知识嵌入整个开发生命周期，主动审查设计文档并根据组织安全要求和常见漏洞扫描拉取请求。组织只需定义一次安全标准，代理就会在审查期间自动跨应用程序验证它们。

“我们对安全代理所做的是，我们实际上将安全代理带入开发生命周期的早期，”Patel 说。“所以，当你完成设计文档，当你开始编码，当你提交第一个拉取请求时，安全代理可以在后台进行查看。”

该代理还将 [渗透测试](https://thenewstack.io/penetration-testing-with-kali-linux-as-a-docker-container/) 从耗时数周的手动过程转变为数小时内完成的按需过程。它返回经过验证的发现以及修复所发现问题的补救代码。如果同时部署多个应用程序，团队可以根据需求扩展代理的数量。

[SmugMug](https://www.smugmug.com/) 是一个面向摄影师的 SaaS 平台，它将 AWS 安全代理添加到其自动化安全产品组合中，以改变其安全测试方法。

SmugMug 的高级软件工程师 Andres Ruiz 在一份声明中表示：“AWS 安全代理帮助捕获了一个现有工具无法捕获的业务逻辑错误，该错误不当地暴露了信息。对于任何其他工具来说，这都是不可见的。但安全代理能够将信息情境化、解析 API 响应并在其中找到意外信息的能力，代表着自动化安全测试的一个飞跃。”

## AWS DevOps 代理：全天候运营

当应用程序宕机时，一切都停止了。现代分布式应用程序——其 [微服务](https://thenewstack.io/introduction-to-microservices/)、云依赖项和 [遥测数据](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/) 分散在多个工具中——使得隔离问题和理解系统行为变得越来越困难。

AWS DevOps 代理通过全天候事件分类、引导式解决方案以及持续改进 AWS、多云和混合环境中应用程序可靠性和性能的建议，实现了亚马逊云科技所说的“更少的警报，更多的睡眠”。

“如果你是亚马逊的随叫随到工程师，并且你的服务出现运营问题，那么大多数晚上你会在两点钟被叫醒，”Patel 说。“如果你有一个代理能够主动处理他们在日志或仪表板中看到的问题，你就能获得更多的睡眠。”

该代理利用其对应用程序架构和组件之间关系的了解，即时响应问题以查找根本原因。它学习跨 [可观测性工具](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/)（如 Amazon CloudWatch、Dynatrace、[Datadog](https://thenewstack.io/is-datadog-becoming-a-platform-engineering-company/)、[New Relic](https://thenewstack.io/new-relics-intelligent-observability-platform-is-ambitious/) 和 [Splunk](https://thenewstack.io/understand-kubernetes-and-containers-with-splunk-observability-cloud/)）的资源及其关系，以及操作手册、代码存储库和 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 管道。

“这个想法是它将持续监控你的仪表板。它将完全访问你所有的操作手册，”Patel 说。“它将能够检测可能导致中断的趋势并采取一些行动来纠正它，而且它会主动完成所有这些工作。”

亚马逊云科技表示，该代理还会分析历史事件中的模式，提供有针对性的建议，以增强可观测性、基础设施优化、部署管道改进和应用程序弹性。

该公司还表示，澳大利亚联邦银行（Commonwealth Bank of Australia），作为澳大利亚领先的综合金融服务提供商之一，服务超过 1700 万客户，在一个复杂的网络和身份管理问题上原型化了 AWS DevOps 代理，这个问题通常需要经验丰富的 DevOps 工程师数小时才能识别。该代理在 15 分钟内找到了根本原因。

澳大利亚联邦银行云服务主管 Jason Sandry 在一份声明中表示：“AWS DevOps 代理像一位经验丰富的 DevOps 工程师一样思考和行动，帮助我们的工程师构建一个更快、更具弹性、旨在为客户提供更好体验的银行基础设施。这不仅仅是关于更快的解决时间——更是关于维护客户对我们的信任。”

Patel 告诉 The New Stack，该代理还将预防宕机。

“它将能够检测可能导致宕机的趋势，并说，‘好的，我在仪表板上看到了这个，或者我在日志中看到了这个，我将采取一些行动来纠正它’，并且它会主动完成所有这些工作，”他说。“所以，实际上，它可能实际上会避免一次宕机，或者如果宕机发生，它也会非常早期地检测到并解决它。”

## 应对整个生命周期

Patel 表示，亚马逊云科技设计这三款代理是为了在整个软件开发生命周期中工作，而不是只解决其中一个部分并在其他地方制造瓶颈。

“我们审视整个生命周期的原因在于，我们想确保我们不仅仅解决其中一个部分，然后在生命周期的其他部分出现瓶颈，”他说。

代理不仅可以从代码或明确指令中学习，还可以通过理解团队的工作方式来学习。与 Slack、Jira 和 GitHub 的集成使代理能够观察团队互动并自动承担任务，而无需被告知执行特定的子任务。

Patel 表示，亚马逊云科技在 2025 年全年都在内部测试这些代理，不同的工程团队将它们作为工作流程的一部分来帮助改进产品。

所有三款前沿代理目前都已推出预览版。早期采用者包括澳大利亚联邦银行、SmugMug、西州长大学和 [Presidio](https://www.presidio.com/)。

## 取代工程师？

尽管 Patel 提到了前沿代理对初级工程师的影响，但他认为这些代理不太可能取代他们，而是会让他们变得更高效。

Patel 说：“如果你的存储库中有 100 个问题，而你没有足够的工程师来处理所有这些问题，并且你需要你的工程师专注于为你的应用程序构建新功能和新的增值能力，那么让其中一个代理在后台查看这 100 个问题并能够提交拉取请求，而你无需担心它们，这实际上对团队来说是一个巨大的生产力提升。”

“它让团队能够专注于客户更感兴趣的、更具增值性的工作，”他补充道。