
<!--
title: 云应用文档质量差让你头疼？打破循环
cover: https://cdn.thenewstack.io/media/2024/08/bbc6373a-files.jpg
-->

活文档随着软件的变更而演变，确保文档始终反映系统的当前状态。

> 译自 [Annoyed by Poor Docs for Your Cloud Apps? Break the Cycle](https://thenewstack.io/annoyed-by-poor-docs-for-your-cloud-apps-break-the-cycle/)，作者 Rak Siva。

内部文档很无聊。它本不必如此——我们都知道它对我们作为工程师的生活方式至关重要——但它就是如此。

两难境地在于我们在文档围栏两边都遭殃：我们不喜欢编写它，当我们收到糟糕的文档时它会激怒我们。你有多久没诅咒过你之前的开发人员，因为他们根本没有文档或提供的文档少之又少？

对我们大多数人来说，文档通常是最后要处理的任务，这意味着很多重要的细节被遗漏了，这些细节本可以帮助新团队成员以及负责维护项目的团队。在几周后你进行了更改或对项目采取了具体的步骤，并且已经转向下一个挑战后，很难回想起来。上一个项目很快就会成为遥远的记忆。

很明显，我们需要在这方面寻求帮助，因此，作为软件工程师，我们理所当然地尝试使用更多软件来解决问题。以我的经验，活动文档是我从未专门要求过的最好的工具之一，通常认为这是理所当然的，但在有文档时总是心存感激。

## 什么是实时文档？

实时文档是一种理念，即文档不断更新，与实际代码库和系统行为同步。它随着软件的变化而进化，确保文档始终反映系统的当前状态。

有了基本最小的工作量，实时文档工具可以做到永远不会有你将项目移交其他团队成员却没有任何文档基础的时候。理想情况下，它为每个项目提供了一个简洁清晰的文档平台，而不仅仅是后期再考虑的事情。

为了帮助构建此技术，让我们来看一些你可能认识的示例，以及他们如何实施一些活文档变体。

## 类型和您之前见过的示例

您可能已经使用生活文档工具并未真正以这种方式考虑它们。 在某些情况下，用于系统的规范还可以作为生活文档的起点。 这些工具有助于确保文档保持准确并与不断发展的代码库保持同步，从而降低文档过时或不完整的风险。

**基于规范的文档化：**

基于规范的文档化注重创建软件组件的详细描述和规范，这些规范通常独立于实现。这些规范可用于确保所有涉众对软件应当如何运作有明确的理解，并且还可用于生成测试，甚至是代码存根。

**基于代码注释的文档：**

基于代码注释的文档包括使用特定注释在源代码中内嵌文档。之后，文档生成工具会处理这些注释，以创建全面的文档。

**[Javadoc](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)**

**用途**：

**用于为 Java 代码编制文档。**

- 可直接从 Java 源码注释生成 HTML 文档。
- 在代码编译时自动更新文档，确保它始终反映代码库的当前状态。

**益处：**

- 以最小的努力将 Java 代码文档保持最新。
- 提供有关代码结构和功能的全面详细信息。

**基于代码的文档：**

基于代码的文档工具分析源代码本身来生成文档。这种方法确保了文档始终与代码保持同步，因为它直接来自代码库。

**[Swagger/OpenAPI](https://swagger.io/docs/specification/about/)**

**用途：**

主要用于 API 规范。

**作为动态文档的工作原理：**

- 根据最新的 API 定义自动生成并更新 API 文档。
- 交互式文档允许开发人员测试和验证 API 端点，确保文档始终与代码同步。

**优点：**

- 确保 API 文档始终与代码同步。
- 增强了前端和后端开发人员之间的协作。

## 优先使用云资源文档

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

**[Nitric](https://nitric.io?utm_content=inline+mention)**

**目的**: 加速云应用程序的开发和部署。

**作为动态文档的工作原理:**

- 自动生成一个规范，该规范通过检查应用程序代码来捕获[运行应用程序所需的架构](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)。 
- 确保资源规范和部署的架构始终与应用程序逻辑保持一致。
- 可以解释为其他文档格式，包括规范的视觉表示。

**好处:**

- 确保应用程序的运行时需求与应用程序代码保持一致。
- 该规范可用于生成[基础设施即代码](https://thenewstack.io/no-terraform-no-iac-are-you-looking-for-disaster/)(IaC)，例如 Terraform，它可以被视为您预期基础设施的蓝图（更多文档）。

**[Terraform](https://www.terraform.io/)**

**目的**: IaC 工具，旨在以一致且自动化的方式定义、配置和管理跨各种云提供商的基础设施资源。

**作为动态文档的工作原理:**

- [Terraform 使用](https://thenewstack.io/terraform-isnt-dead/)声明性语言来指定基础设施的预期状态。这些配置充当基础设施的可读蓝图。
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
