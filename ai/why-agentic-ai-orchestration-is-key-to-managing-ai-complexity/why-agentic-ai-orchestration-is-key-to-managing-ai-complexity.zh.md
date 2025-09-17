在过去的四年里，[Orkes](https://orkes.io/?utm_content=inline+mention) 因其能够在单一平台内集成数据和微服务编排而广受欢迎。但其更新的角色——作为一个合适的 Agentic AI 来编排极其复杂的 AI 工作流程 —— 可能会使 Orkes 站在 AI 繁荣的前沿。

根据该公司创始人的说法，基于 Agentic AI 的编排是所有 AI 事物的必要组成部分，从 Anthropic 创建的 AI 模型到组织正在构建的自定义[大型语言模型 (LLM)](https://thenewstack.io/introduction-to-llms)。

Orkes 的联合创始人兼 CTO [Viren Baraiya](https://www.linkedin.com/in/virenb) 告诉我：“如果你想构建 Agent，Agent 需要编排长时间运行的工作流程。这些工作流程需要维护状态。而且，一旦你超越概念验证，你还必须大规模地运行它们。这就是几乎所有框架都在努力的地方。”

## 从 Netflix Conductor 到 AI Agent 编排

Orkes 由 Baraiya、[Dilip Lukose](https://www.linkedin.com/in/diliplukose/) 和 [Jeu George](https://www.google.com/url?q=https://www.linkedin.com/in/jeugeorge/&sa=D&source=docs&ust=1757530028814278&usg=AOvVaw3ruxKxKtC7qqI54xo1Vbdl)（开源 Netflix Conductor 的共同创建者）于 2021 年创立，旨在为 Netflix 的开源工作流程编排平台提供企业支持和功能。

在 Netflix 的创建和控制下，[Conductor 蓬勃发展](https://thenewstack.io/orkes-to-maintain-conductor-project-as-netflix-steps-back/)，成为一种非常成功和流行的方式，通过集成数据和各种自动化堆栈来编排工作流程的自动化。最重要的组件涉及数据服务和微服务的集成。这有助于运营团队将两个管理步骤整合为一个，从而提高了 Orkes 的受欢迎程度。

从那时起，[该项目](https://conductor-oss.org/) 不断发展，将数据和微服务编排统一在一个更加集成和强大的框架下。这不仅仅是另一个所谓的“单窗格”，因为这两个编排领域都代表和自动化管理和修复，正如我将在下面进一步探讨的那样。

这就是 Orkes 的起点。然后，[Agentic AI](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers) 编排加入了战局。

## Agentic AI 系统中的状态管理

LLM 与数据编排的集成已成为现代工作流程编排平台的重要组成部分。2023 年，Orkes 将 LLM 编排集成到其数据和微服务编排平台中。这实际上使 Orkes Conductor Enterprise 成为 AI 繁荣的先驱，通过支持跨各种 AI 和相关服务组件管理复杂的状态工作流程。Baraiya 说，Orkes 的工作为长期运行、可靠和可调试的 AI Agent 工作流程奠定了基础架构，这是后来被称为 Agentic AI 系统的核心。

与大多数框架不同，Orkes 在长时间运行的工作流程中扩展时不会费力地维护状态，他解释说。“规模存在于我们平台的 DNA 中；无需考虑它，它是任何完成工作的副产品。”

[![Orkes AI agentic orchestrator handles security, scalability, observability and auditability](https://cdn.thenewstack.io/media/2025/09/a33f1fa9-orkes-architecture.png)](https://cdn.thenewstack.io/media/2025/09/a33f1fa9-orkes-architecture.png)

来源：Orkes。

拥有合适的 AI Agentic 编排器对于构建任何 Agent 都是必要的。“Agent 本质上是知识、工具和作为控制器的语言模型的总和。编排发生在这些组件之间，”Baraiya 说。“要运行 Agent，需要分布式状态管理。需要工作流程的概念，因为必须协调控制循环和所有内容。还需要调试并准确查看正在发生的事情的能力。”

Baraiya 说，像 OpenAI、Gemini 和 Anthropic 这样的模型提供商提供了一个出色的基础，并且工作流程引擎仍然至关重要。“没有工作流程引擎，在生产环境中运行 Agent 是不可能的，”Baraiya 说。“这就是契合点——成为运行 Agent 的平台。这就是这些 Agent 的运行方式。”

## 人在回路中：建立对 AI 的信任

合适的 AI Agentic 编排器必须能够可靠地大规模管理长时间运行的工作流程。但更重要的是，它必须获得组织的信任，这意味着让[人在回路中](https://orkes.io/blog/operators-loops-waits-human-tasks/)。在 Orkes 的案例中，通过仪表板提供**可观测性**，因此人类可以实时监控与工作流程相关的性能指标。

“让**人**在回路中现在是围绕 AI 实施的一种非常强烈的观点。它很好地融入了维护信任或在使用案例更加严格的情况下建立信任的想法——在这些情况下，依靠 LLM 或大脑来提供合理的建议是不可能的，”Baraiya 说。“任务需要提升到**人**来介入并执行工作流程。这是通过围绕**人**在回路中的工作流程的本机实现来强烈完成的事情。”

> “没有工作流程引擎，在生产环境中运行 Agent 是不可能的。这就是契合点——成为运行 Agent 的平台。这就是这些 Agent 的运行方式。”

但是，一旦将**人**添加到回路中，事情就会变慢。但无论**人**需要多长时间才能做出回应，都必须保持状态，Baraiya 解释说。“一个很好的例子是，Agent 尝试做出决定，但需要用户的确认。虽然典型的程序可能在几秒钟内完成任务，但一旦添加了**人**，这些秒就会变成几分钟、几小时或几天，具体取决于情况，”Baraiya 说。这会产生围绕在长时间运行的作业中维护状态的问题。

实际上，他说，“由于维护长时间运行的状态、合并反馈循环以及围绕它构建整个系统，将**人**添加到回路中……真的很困难。原本应该简单的事情突然变成了一个长期项目。”

作为 AI 控制自动化的推动者，Orkes Conductor 将工作流程与 LLM（例如 Claude、OpenAI GPT-4 和 Google Vertex AI）和 [向量数据库](https://thenewstack.io/top-vector-database-solutions-for-your-ai-project/) 集成。其 AI 编排能力支持“Agentic”工作流程：AI Agent 执行任务，但包括用于监督的**人**工检查点。根据最近的 [Orkes 博客文章](https://orkes.io/blog/scaling-complex-agentic-workflows/)，“这确保了工作流程随着 AI 的动态适应，让**人**参与合规性和治理，因为自动化朝着自主性发展。”

## 通过可观测的 AI 工作流程自动化建立信任

[Gartner 描述了](https://www.gartner.com/doc/reprints?id=1-2LGK9A81&ct=250715&st=sb&utm_campaign=18097788-WEB-CC-304-EN-Gartner-Hype-Cycle-for-Enterprise-Process-Automation-07-2025&utm_medium=email&_hsenc=p2ANqtz--G2vjzhuiOECiiS0YJBnQmsmY2TjZ-BsnUH7R_scd9McmUzblgT9B53Grl26mDjoqxzaJHTDzQ_i3QNOV3QlNC2JzrDA&_hsmi=373295109&utm_content=373295109&utm_source=hs_automation) 企业流程编排工具的业务影响，作为自动化工作流程、识别错误和系统中断以及加速工作流程集成的一种方式。这些工具还支持适应不断发展的后端架构和数字要求。Gartner 将 Orkes 纳入此类别。

今天，在 DevOps 和 IT 的交汇处，Agentic AI 编排工具对流程编排的需求至关重要。这些工具可以帮助公司管理 AI 的复杂性，特别是那些开发 LLM、AI 应用程序和相关系统的公司。

Orkes Conductor 旨在处理 Agentic AI 编排，并通过提供透明度并允许**人**工监督关键决策过程，它是建立对 AI 信任的重要元素，Orkes 的创始人说。

“编排仍然是连接所有事物的基本组件，”Baraiya 说。“统一 IT 系统中的自动化孤岛仍然具有高度相关性，并且编排部分现在已发展成为一个独特的类别。这是 Orkes 的核心贡献，并且这种针对 AI Agent 的编排对于管理 AI 流程至关重要。”