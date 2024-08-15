# Annoyed by Poor Docs for Your Cloud Apps? Break the Cycle

![Featued image for: Annoyed by Poor Docs for Your Cloud Apps? Break the Cycle](https://cdn.thenewstack.io/media/2024/08/bbc6373a-files-1024x576.jpg)

Internal documentation is boring. It shouldn't be—we all know it's crucial to our lives as engineers—but it is.

The predicament is that we suffer on both sides of the documentation fence: we don't like writing it, and it annoys us when we receive [poor documentation](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/). How often do you curse previous developers for their useless or nonexistent documentation?

For most of us, [documentation](https://thenewstack.io/an-engineers-best-tips-for-writing-documentation-devs-love/) is often the last thing to get done, which means many important details get left out that could help new team members as well as those maintaining the project. It's hard to recall the exact steps or changes you made to a project when you move on to the next challenge in a few weeks. Previous projects quickly become a distant memory.

It's clear we need [help with this](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), so as software engineers, we naturally try to use more software to solve the problem. In my experience, living documentation is one of the best tools I never explicitly asked for, often take for granted, but always appreciate when it's available.

## What is Living Documentation?

Living documentation is a concept where documentation is constantly updated and synchronized with the actual codebase and system behavior. It evolves with the software, ensuring that the documentation always reflects the current state of the system.

With minimal effort, living documentation tools can ensure you never hand off a project to another team member without some form of basic documentation. Ideally, it provides a clear and concise starting point for documentation for every project, not just an afterthought at the last stage.

To help build this technology, let's look at some examples you might recognize and how they implement some variations of living documentation.

## Types and Examples You Might Have Seen

You might already be using living documentation tools without really thinking about it. In some cases, specifications for the system can also serve as a starting point for living documentation. These tools help ensure that documentation remains accurate and synchronized with the evolving codebase, reducing the risk of outdated or incomplete documentation.

**Specification-Based Documentation:**
Specification-based documentation focuses on creating detailed descriptions and specifications of software components, often independent of the implementation. These specifications can be used to ensure that all stakeholders have a clear understanding of what the software should do, and they can also be used to generate tests or even code stubs.

**Code Comment-Based Documentation:**
Code comment-based documentation involves embedding documentation within the source code using special comments. These comments are then processed by documentation generation tools to create comprehensive documentation.

[Javadoc](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)
**Purpose:** Used for documenting Java code.
**How it works as living documentation:**
- Generates HTML documentation directly from Java source code comments.
- Automatically updates documentation when code is compiled, ensuring it always reflects the current state of the codebase.
**Advantages:**
- Keeps Java code documentation up-to-date with minimal effort.
- Provides comprehensive details about code structure and functionality.
**Code-Based Documentation:**
Code-based documentation tools analyze the source code itself to generate documentation. This approach ensures that the documentation is always in sync with the code, as it is derived directly from the codebase.

[Swagger/OpenAPI](https://swagger.io/docs/specification/about/)
**Purpose:** Primarily used for API specifications.
**How it works as living documentation:**
- Automatically generates and updates API documentation based on the latest API definition.
- Interactive documentation allows developers to test and validate API endpoints, ensuring that the documentation stays in sync with the code.
**Advantages:**
- Ensures API documentation is always synchronized with the code.
- Enhances collaboration between front-end and back-end developers.
## Prioritizing Cloud Resource Documentation
由于多种因素，将运行时需求从开发团队传达给运维团队是一项挑战。团队之间技术知识的差距会导致规范不完整或不准确，因为开发人员可能无法完全理解云基础设施的复杂性。

我见过各种形式的应用程序开发团队必须手动填写以传达其需求，虽然这些也可以用作文档，但它们通常不完整或不一致，并且需要会议或漫长的支持票回复才能达成解决方案。

问题是，在这个项目阶段的误解成本极高。它们会导致：

- 资源过度分配导致不必要的财务支出
- 资源和权限分配不足导致更高的运营支出
- 数据泄露和合规罚款
- 停机导致的收入损失和声誉受损
## 开发人员向运维人员伸出橄榄枝
云资源配置的动态文档可以通过提供应用程序运行时需求的透明度和最新信息，充当开发和运维团队之间的桥梁。这通过以下几种方式改善了工作关系：

- 两个团队都可以看到应用程序的运行时需求。
- 最新文档改善了沟通。由于团队成员都拥有单一的事实来源，因此误解的空间更小。
- 规范始终以一致的格式进行传达，这为未来的简化流程（如审查和优化分析）铺平了道路。
## 云资源配置的动态文档
以下是一些支持创建云资源动态文档的工具示例。

[Nitric](https://nitric.io?utm_content=inline+mention)
**目的**: 加速云应用程序的开发和部署。
**作为动态文档的工作原理:**
- 自动生成一个规范，该规范通过检查应用程序代码来捕获[运行应用程序所需的架构](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)。 
- 确保资源规范和部署的架构始终与应用程序逻辑保持一致。
- 可以解释为其他文档格式，包括规范的视觉表示。
**好处:**
- 确保应用程序的运行时需求与应用程序代码保持一致。
- 该规范可用于生成[基础设施即代码](https://thenewstack.io/no-terraform-no-iac-are-you-looking-for-disaster/)(IaC)，例如 Terraform，它可以被视为您预期基础设施的蓝图（更多文档）。
[Terraform](https://www.terraform.io/)
**目的**: IaC 工具，旨在以一致且自动化的方式定义、配置和管理跨各种云提供商的基础设施资源。
**作为动态文档的工作原理:**
[Terraform 使用](https://thenewstack.io/terraform-isnt-dead/)声明性语言来指定基础设施的预期状态。这些配置充当基础设施的可读蓝图。
- 该计划可用于生成可视化或预期部署资源的摘要，包括配置设置。
**好处:**
- 基础设施是透明的，具有对将要部署的资源、策略和权限的人类可读声明。
- 该蓝图可用于其他工具（如静态分析）以帮助使其更强大。
## 人工干预的必要性
我需要明确说明，我并不主张[完全自动化文档](https://thenewstack.io/how-to-use-llms-for-dynamic-documentation/)。动态文档应该补充您现有的实践，并作为开发人员用作全面记录系统的起点。关键是，如果我们可以自动生成可用于驱动软件自动化的规范，我们也可以使用相同的过程来生成准确的规范和文档，然后我们可以通过人工干预来增强其完整性。

## 大型语言模型怎么样？
将生成动态文档的软件与大型语言模型 (LLM) 相结合，可以显着提高文档的质量和相关性。我并不是说将整个代码库传递给 LLM，这将是乏味、昂贵且耗时的。相反，我们将传递动态文档工件。

我们可以使用动态文档和 LLM 设置持续内容增强流程，其中动态文档使技术细节保持最新，而 LLM 通过添加解释、示例和上下文来增强此内容，使其更易于各种受众理解。
从动态内容生成开始，确保系统当前状态的实时更新被LLM用于生成相关且及时的内容，例如基于最新代码更改的用户手册或故障排除指南。由于我们都痴迷于将我们的系统与聊天机器人集成，我们可以将此功能扩展到用户查询和交互式文档，以便LLM实时与用户交互，使用来自实时文档的最新数据回答他们的问题。

## 无需乏味的更好的内部文档

借助可以自动化部分文档的现代工具，我们永远不必成为“那个开发人员”，他会在没有文档的情况下传递应用程序。重要的细节应该由我们的工具自动捕获，并通过LLM轻松阐述，并实时持续提供给下一个加入项目的人。

通过将[Nitric](https://nitric.io/docs/concepts/introduction)添加到您的工作流程中，您可以使用资源规范来弥合开发人员和运营之间的沟通差距，该规范传达了您的应用程序需求。作为奖励，如果您选择将Terraform与Nitric一起使用，您还将拥有一个[Terraform蓝图](https://nitric.io/blog/terraform-providers)，该蓝图记录了您希望基础设施达成的最终状态。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的YouTube频道以流式传输我们所有的播客、访谈、演示等。