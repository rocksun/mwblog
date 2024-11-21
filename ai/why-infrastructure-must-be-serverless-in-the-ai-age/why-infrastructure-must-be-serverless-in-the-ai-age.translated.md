# 为什么在人工智能时代基础设施必须是无服务器的

![人工智能时代为什么基础设施必须是无服务器的专题图片](https://cdn.thenewstack.io/media/2024/11/8699427a-arian-darvishi-wh-rpfr_3_m-unsplash-1024x682.jpg)
Photo by [Arian Darvishi](https://unsplash.com/@arianismmm?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-using-laptops-wh-RPfR_3_M?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

[Replit 的新 AI 代理](https://blog.replit.com/introducing-replit-agent)将编写您的代码，然后配置、调配、构建和部署该代码，只需*几秒钟*。您可以在 VS Code 加载所有扩展程序之前，从自然语言描述到已实现的、可运行的应用程序。

如果一个 AI 代理可以在几秒钟内构建和部署一个应用程序，那么几分钟的时间来启动资源就太长了。如果一个 AI 代理每小时可以启动和关闭数千个这样的应用程序，那么每个数据库 10 美元的成本就变成了极高的开销。突然之间，我们从一个开发人员团队部署单个应用程序变成了单个开发人员部署一组应用程序，所有应用程序都在 AI 代理的指导下工作。

这种方法改变了对开发的看法，并要求对基础设施有新的认识。传统的基础设施对于代理工作流程来说太慢、太永久且太复杂。基础设施的未来需要即时的、无服务器的和简化的工具——这就是必须构建的内容。

## AI 代理基础设施的核心需求

AI 代理的运行规模和速度使得传统的基础设施管理在技术上和经济上都不切实际。良好的“代理体验”将强调三个核心特性：

### 简易性

任何[代码和集成](https://thenewstack.io/why-infrastructure-as-code-needs-cloud-asset-management/)都需要简单。这个世界将建立在简单的 API 调用而不是 IAM 策略和多步骤配置之上。考虑启动一个新的 RDS 实例：VPC、安全组、规则、子网组和 IAM 角色。每个步骤都需要多个 API 调用、选项的考虑和故障排除。

[DevOps 工程师](https://thenewstack.io/ai-coding-human-engineers-are-more-important-than-ever/)了解这些依赖关系，并且可以在出现问题时进行调试。AI 代理需要一切第一次和每次都能完美运行。这种复杂性不仅仅是进入的障碍；它是自动化的障碍。这就是在 Neon 上启动数据库所需的：

![](https://cdn.thenewstack.io/media/2024/11/6a2bcdf0-unnamed.png)

来自[@neondatabase/toolkit](https://github.com/neondatabase/toolkit) SDK 的代码示例

三行代码即可配置数据库，一次 API 调用，即可立即使用。这不仅仅是更好的开发者体验——这是使 AI 代理能够访问基础设施的唯一方法。这种简易性还有助于两个因素：

* **成本：**更多步骤 = 更多成本。代理进行的每个 API 调用都会消耗令牌，而[复杂的基础设施操作](https://thenewstack.io/codiac-kubernetes-doesnt-need-to-be-that-complex/)可能需要数十次调用。简单的 API 不仅仅是更易于使用；它们从根本上来说在大规模情况下更经济。
* **安全性：**尽管 AWS RDS 设置非常安全，但您不能将您的根密钥交给机器。现代基础设施需要进行沙盒化和自包含，并具有清晰的边界，让代理可以自由地进行实验，而不会危及生产系统。

### 即时性

上面的代码可以在一秒钟内启动一个新的数据库，供代理使用。

在代理驱动的世界中，传统的基建时间线需要修改。代码创建速度曾经是开发中的速率限制因素，但是当 AWS RDS 实例需要 10 分钟来配置时，该基础设施就变成了速率限制因素。

转向即时性模型与人工智能一样，开启了无限可能。代理驱动开发的核心原则是可处置性。代理可能会创建一个应用程序，对其进行测试，并在几分钟内将其丢弃。基础设施需要匹配此生命周期——在需要时立即启动，并在不需要时同样快速地消失。代理应该能够在[传统数据库](https://thenewstack.io/columnar-storage-a-developers-key-to-real-time-analytics/)启动所需的时间内构建和销毁一个一次性应用程序。


### 短暂性

这也引出了可处置应用程序的关键组成部分——短暂性。传统方法假设应用程序是永久的，因此它需要永久的基础设施。

并非如此。看看开发人员如何使用 Vercel 的 [v0](https://v0.dev/)，这是一个用于从文本提示生成应用程序的开发工具。您无需在线搜索“抵押贷款计算器”，而是可以要求 [v0](https://v0.dev/chat/ObNYNZmQCoJ?b=b_rOkttQVXY8h) 为您创建一个：
这有效。它不需要基础设施，但这可能是下一步。最重要的是，用户可以在单个会话中使用 AI 构建大量内容。绝大多数内容会被丢弃且不再使用，但有些内容可能会被共享并转化为长期存在的应用程序。这是工具的未来——你使用 AI 和 AI 代理精确构建你想要的东西，并留下一串废弃的替代方案。

这需要一个可以缩放到零的基础设施。当资源未被使用时，其成本应降至零。有了这种能力，一次性应用程序的经济效益将会实现。想象一下，一家公司在使用 AI 构建的过程中每小时启动数十个数据库。谁来删除未使用的数据库？谁来决定哪些数据库未使用？

当基础设施能够真正缩放到零时，它将启用新的开发模式。代理可以自由地尝试不同的方法，并行测试多个解决方案，而无需担心清理或持续成本。这消除了开发过程中的经济限制——你不再需要仔细考虑每个新数据库或服务的成本影响。

结果是一个资源真正可丢弃的开发环境。创建你需要的内容，根据需要使用它，并在完成后让它消失。这不仅仅是更高效——这是使代理驱动的开发在大规模上经济可行的唯一方法。

## 更简单、更快、更便宜——选择三个

在六个月内，我们已经从 [Cognition AI 的 Devin AI 程序员](https://www.cognition.ai/blog/introducing-devin) 的演示发展到 Replit 的 AI 开发人员/DevOps 代理在实际工作中运行。明年这个时候的 SOTA 会是什么样子？

没有人知道，但很清楚什么样的基础设施会让我们到达那里。该基础设施必须从人类开发人员转移到作为构建者的 AI 代理。但创建良好的 AgentEx 也将使我们构建良好的 DevEx，因为更简单、更快和更便宜也适用于循环中的人类。这种良性循环——AI 代理的改进为人类创造了更好的工具，反之亦然——将加速 [开发人员构建和部署软件](https://thenewstack.io/go-big-or-go-home-what-github-learned-building-copilot/) 的方式的转变。

*本文是 The New Stack 贡献者网络的一部分。对影响开发人员的最新挑战和创新有见解吗？我们很乐意听取您的意见。填写此表格或发送电子邮件至 mattburns@thenewstack.io 与 Matt Burns 联系，成为一名贡献者并分享您的专业知识。*

[YOUTUBE.COM/THENEWSTACK

技术发展迅速，不容错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)