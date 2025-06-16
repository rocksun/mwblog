
<!--
title: 认识Embabel：一个使用Java构建AI Agent的框架
cover: https://cdn.thenewstack.io/media/2025/06/e6fe4da0-java-embabbel.jpg
summary: 还在用 Java 写 AI？快来试试 Embabel！这个 JVM 框架用 GOAP 帮你轻松构建安全 AI 代理，像 Spring 一样，用 Actions、Goals 和 Conditions 搞定 Agent 工作流。拥抱确定性，告别玄学，企业级 AI 开发就靠它！
-->

还在用 Java 写 AI？快来试试 Embabel！这个 JVM 框架用 GOAP 帮你轻松构建安全 AI 代理，像 Spring 一样，用 Actions、Goals 和 Conditions 搞定 Agent 工作流。拥抱确定性，告别玄学，企业级 AI 开发就靠它！

> 译自：[Meet Embabel: A Framework for Building AI Agents With Java](https://thenewstack.io/meet-embabel-a-framework-for-building-ai-agents-with-java/)
> 
> 作者：Russ Miles

AI 代理正在成为工作场所中真正的协作者，[越来越多的开发人员开始构建它们](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)。为了充分发挥它们在你团队中的潜力，AI 代理需要能够追求特定目标并执行工作流程任务，在没有持续人工监督的情况下做出决策并采取行动。它们需要从交互中学习并随着时间的推移调整其行为。并且它们需要做到这一切，同时意识到并专注于你的上下文和你的目标。

为了有用，代理需要平衡大量的安全（安全可靠）集成。这是专用工具和框架开始涉足的战场。

今年 5 月，微软推出了 [Azure AI Foundry](https://thenewstack.io/microsoft-brings-mcp-local-ai-models-and-post-quantum-security-to-windows/)，以帮助你构建（除其他外）上下文感知代理及其工作流程。Postman 有其 [AI Agent Builder](https://www.postman.com/product/ai-agent-builder/)，Open AI 有其 [Playground](https://openai.com/index/new-tools-for-building-agents/)，[Python 生态系统](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/)已经拥有一套丰富的代理构建库和工具，并且专用的 [代理构建工具](https://thenewstack.io/ai-agents/)也在不断涌现和成熟。

但这仍然给我们留下了一个小小的差距……

Java 和 JVM。

## Java 在 AI 代理方面做了什么？

Java 仍然是企业软件开发中的一个重要参与者。构建利用 AI 的企业 Java 应用程序和服务自然会像其他所有开发生态系统一样，看到越来越多的投资。

[Spring AI](https://spring.io/projects/spring-ai) 项目作为 LLM 交互的底层细节之上的强大抽象集，已经迅速获得关注，提供了一套现成的工具，可以将 AI 集成到你的 Java 应用程序和服务中。

但是，直到最近，对于构建基于 JVM 的 AI 代理的专门和重点支持一直有点薄弱。这种情况似乎即将改变，第一个可能是 JVM 的一组新的以 AI 代理为中心的框架：[Embabel](https://github.com/embabel/embabel-agent)。

## 什么是 Embabel？

Embabel 是一个新的开源项目，旨在简化如何在内部创建安全的 AI 代理工作流程，同时充分利用丰富的 Java 生态系统。

正如该项目的创始人 Rod Johnson 在 [Medium 博客文章](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014) 中指出的那样：AI 代理开发需要一种“新的编程模型”和一种“更高级别的编排技术”，以便安全地与现有上下文集成，更好或更便宜的 AI 模型，注入关键的护栏，管理流程执行，并对代理在完成你给它的任务时如何做出选择给予足够的确定性控制。

通过这种方式，代理具有与任何企业代码库相同的许多特征，即多个集成、多种集成风格以及跨多个数据源的编排，这些数据源具有不同的数量、速度、种类、准确性和价值。

Johnson 最初创建了 [Spring Framework](https://spring.io/projects/spring-framework)，以便为企业 Java 提供更好的编程模型。有了 Embabel，现在轮到为 AI 代理编程了。

与 Spring 如何使用基于 [依赖注入](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html) 和 [控制反转](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html) 的新编程模型改变企业 Java 类似，Embabel 旨在创建一个编程模型，帮助开发人员使用通常用于生产代码的相同最佳实践来构建代理，同时仍然允许你的代理追求特定目标、执行工作流程任务并做出自己的动态运行时决策。

## 代理、信任和确定性

确定性和 AI 模型有着一段艰难的历史。当我们构建应用程序时，我们习惯于应用程序行为是确定性的——即，我们的代码，在给定相同的输入和初始状态的情况下，将始终产生相同的输出和行为。

这不是 LLM 的工作方式。LLM 会产生幻觉——有些人会说，人类也会——在一个极端，而在另一个极端，当被赋予对其创造性选择的自由控制时，可以做出令人惊讶但非常有效的结果。
对于简单、基于提示的与人工交互，这种不确定性可能令人烦恼，但仅此而已。但对于智能体来说，它们也在完全闭环 OODA（观察、调整、决定和行动），在没有人为干预的情况下采取行动，结果的确定性变得至关重要。

要建立对智能体工作流程的信任，需要一种探索智能体如何导航其工作流程的确定性的方法。你希望为智能体的工作成果敞开大门，同时确保你保留对工作导航方式的控制权。为此，Embabel 转向了 GOAP。

## 什么是 GOAP，Embabel 如何使用它？

Embabel 智能体开箱即用地使用[目标导向行动规划 (GOAP)](https://www.reddit.com/r/godot/comments/xgrk0g/goap_goaloriented_action_planning_is_absolutely/)，以便能够导航通往已定义目标的可能步骤。在 Embabel 的 GOAP 实现中，目标是一个步骤——一些可执行的代码——具有一组必须满足的先决条件才能执行该目标。

然后是随附的可能步骤，称为行动，它们具有步骤前和步骤后条件，这些条件提示它们是否应该参与到计划的目标路径中。Embabel 在此的一项创新是以类型安全的 Java 代码声明这些条件。

Embabel 会评估智能体中的目标和步骤，规划一条应该能够实现目标的路径，但如果在路径执行过程中的任何时候未满足一组条件，Embabel 将更改其路径。

这方面的一个例子可能是一组与不确定的 LLM 配合使用的步骤的后置条件可能不令人满意，因此可能会选择一个替代步骤，可能使用不同的 LLM，以查看是否可以获得更好的结果（由步骤后条件判断）。

![Embabel 的组件，旨在简化在 Java 中构建 AI 智能体的过程。](https://cdn.thenewstack.io/media/2025/06/f397190f-embabel-components-1024x690.png)

*Embabel 的组件。*

Embabel 编程模型包括：

- **Actions:** 智能体采取的步骤，通常是方法或函数，由 `@Action` 属性指示。
- **Goals:** 智能体试图实现的目标，由 `@AchievesGoal` 属性指示。
- **Conditions:** 在执行操作之前或确定已实现目标时要评估的因素。每次执行操作后都会重新评估条件。
- **Plan:** 实现目标的行动序列。计划由 Embabel 动态制定。Embabel 在每次操作完成后都会重新计划，使其能够适应新信息并观察先前操作的效果。

Embabel 编程模型允许智能体的工作流程由许多可能的步骤组成，这些步骤用 `@Action` 属性分隔，以及一个或多个 `@AchievesGoal` 注释的操作来指示目标。

Embabel 运行时可以根据你指示的关于已定义目标的步骤前和步骤后条件，确定性地导航可能的步骤集合，如果步骤/操作的结果不符合你的需求，则可以选择重新计划。

从[第二篇 Medium 博客文章](https://medium.com/@springrod/ai-for-your-gen-ai-how-and-why-embabel-plans-3930244218f6)描述了 Embabel 如何规划，使用 Embabel 编程模型，你可以“享受一个系统的优势，该系统可以制定[你]从未明确编码的计划，但无需付出将流程控制权交给不透明模型的代价。你的智能体可以在确定性和通过智能体可以采取的无数不同步骤实现目标的新的、更好甚至更便宜的途径的潜力之间取得平衡。

如果你有 JVM 背景，Embabel 提供了一些示例和说明，可以让你快速上手并开始探索为 JVM 构建自己的智能体。Embabel 100% 用 Kotlin 编写，但完全支持使用 Java 开发你的智能体。

## AI 智能体的未来一片光明

构建 AI 智能体还处于起步阶段，Embabel 也处于早期阶段。好消息是，开源领域拥有快速创新的良好记录，并且 Embabel 是开源的，并获得了企业友好的 Apache 软件许可。

你可以期望事情在公共领域发展得非常快，并且在 The NewStack 上，我们预测“许多软件工程师将成为智能体流程作者”。[Prasad Prabhakatan](https://www.linkedin.com/in/prasadprabhakaran)，eSynergy 的人工智能主管告诉我，仅在专业保险和公共部门，“我们看到 30-50% 的 AI 工程工作正在向构建、编排和管理 AI 智能体方向发展。”
他补充说：“我们目前与客户关注的重点是抽象化 LLM 和编排的复杂性，使主流开发人员（尤其是 Java/Spring 和 .NET 工程师）可以访问 Agent 开发。我们正在构建可重用的模式、SDK 和参考架构，使这些团队能够接入 Agent，而无需成为 AI 专家。”

## 有 Agent 故事要分享吗？

您是否正在构建自己的 Agent 并有故事要分享？如果您有兴趣分享您在这个新的 AI 工程方法的实践经验，无论是好的还是坏的，请[联系我](https://www.linkedin.com/in/russmiles/)。