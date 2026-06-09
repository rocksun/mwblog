<!--
title: “谁能打造出最令人愉悦的产品，谁就是赢家”：Agent大战拉开帷幕
cover: https://cdn.thenewstack.io/media/2026/06/550c806e-oleg-ivanov-putmwtthtmk-unsplash-scaled.jpg
summary: 本文通过对话Snowflake产品高级副总裁，探讨了企业AI向Agent工作流的演进，介绍了全新Coding Agent“CoCo”如何降低门槛，重塑生产力。
-->

本文通过对话Snowflake产品高级副总裁，探讨了企业AI向Agent工作流的演进，介绍了全新Coding Agent“CoCo”如何降低门槛，重塑生产力。

> 译自：["Whoever builds the most joyous product wins": The agent war begins](https://thenewstack.io/snowflake-coco-agentic-enterprise/)
> 
> 作者：Chris J. Preimesberger

在本周于旧金山举行的 [Snowflake Summit 26 峰会](https://www.snowflake.com/en/summit/)上，对话转向了新的方向。如果说去年的焦点是大语言模型的最初奇迹，那么今年的故事则是关于使用它们的下一步：智能体企业（the agentic enterprise）。

对于企业而言，问题不再是 AI 是否能编写代码，而是如何编排它，以最少的人工监督来构建、部署和管理复杂且数据密集型的工作流。

为了了解 Snowflake 如何将自己定位为 AI 开发领域一切事务的后盾，记者和分析师在活动期间采访了 Snowflake 的产品高级副总裁 [Christian Kleinerman](https://www.linkedin.com/in/christian-kleinerman-a973102/)。

在发布了一套强大的全新开发人员工具的主旨演讲之后，Kleinerman 详细阐述了该公司如何超越简单的代码生成，为企业 AI 创建一个统一的智能体控制平面。

*为求清晰，本次对话内容经过了编辑和删减。*

**问：Snowflake Summit 26 峰会的定义特征是向智能体工作流的转变。当您审视当下的局势时，您是如何向客户定义这种转变的？**

**Christian Kleinerman：** 我们正在步入一个新阶段，在这个阶段中，AI 的价值取决于其自主性和可靠性，而不仅仅是其对话能力。我们的高层目标是简化整个数据生命周期。在过去，从摄取、转换到消费的生命周期是一个手动的、碎片化的过程。今天，我们引入了一种智能体方法，在其中，这些步骤不仅紧密相连，而且被有机地编排在了一起。

> “我们已经看到一些场景，以前需要三个月人工劳动的迁移项目，现在通过智能体工作流在不到五小时内就能完成，而人类只需介入并审查最终输出。”

当我们谈论“智能体企业”时，我们指的是那些不仅能协助生成代码，还能实际构建和部署的工具。我们注意到，当前的开发人员体验经常被“标签页蔓延”所打碎——开发人员为了解决一个问题要在十个不同的应用程序之间来回切换。我们这些新工具的重点是将上下文拉入工作区，让开发人员扮演架构师的角色，而不是手动输入代码的打字员。

**问：这引出了一个大新闻：Snowflake CoCo。你们已经将 [Cortex Code](https://www.snowflake.com/en/product/features/cortex-code/) 重新命名为 [CoCo](https://www.snowflake.com/en/news/press-releases/snowflake-coco-redefines-enterprise-ai-development-as-the-coding-agent-built-for-faster-easier-and-more-powerful-innovation-anywhere/)。这一变化在能力方面代表了什么？**

**Kleinerman：** CoCo 代表 Coding Agent（编程智能体），它是我们处理开发方式的根本性转变。它不仅仅是一个聊天界面；它是一个可以编排数据工作流的编程智能体。

![](https://cdn.thenewstack.io/media/2026/06/ad458303-1590958159395.jpg)

Snowflake 的 Christian Kleinerman

我们在内部学到的是，当你给开发人员提供合适的工具时，生产力不仅仅是提高一个百分点，而是实现飞跃。我们已经看到一些场景，以前需要三个月人工劳动的迁移项目，现在通过智能体工作流在不到五小时内就能完成，而人类只需介入并审查最终输出。

CoCo 现在可以作为原生桌面应用使用，但我们也将其延伸到了开发人员日常工作的场所，例如 [VS Code](https://code.visualstudio.com/) 和 [Microsoft Excel](https://www.microsoft.com/en-us/microsoft-365/excel)。通过在构建者工作的地方与他们对接，我们让他们能够通过简单的提示词在企业数据上实现工作流自动化、开发应用并使 AI 投入运营。我们不仅在努力让编写 SQL 查询变得更容易，也在让交付生产就绪的数据产品变得更简单。

**问：你们还宣布了 [Snowflake Datastream](https://www.snowflake.com/en/product/features/datastream/)。为什么基础设施层对于这种由 AI 驱动的开发愿景如此重要？**

**Kleinerman：** 如果 AI 智能体消耗的数据是陈旧的或被困在孤岛中，你就无法拥有可靠的 AI 智能体。Datastream 是我们针对 [Apache Kafka](https://kafka.apache.org/) 的全新全托管流服务。

对于大多数组织而言，真正的难点在于管理独立流基础设施的复杂性——不同的代理、连接器以及维护开销。借助 Datastream，我们正在消除这一障碍。我们正将实时、持续流动的数据直接引入 Snowflake。这至关重要，因为在沙箱中运行的 AI 智能体与在生产环境中运行的 AI 智能体之间的区别在于其上下文的实时新鲜度。如果你想驱动一个能够做出实时业务决策的 AI 应用，你就需要实时的数据集成。Datastream 让这一切变得无缝。

**问：目前行业内关于“Token最大化（token maxing）”和 AI 预算有很多议论——一些公司由于成本攀升正在缩减对无限制大语言模型（LLM）的访问。您在客户中看到这种担忧了吗？**

**Kleinerman：** 我们听到了这种声音，这是一个合理的担忧。我的回答往往是，缺乏使用度量标准才是真正的问题，而不是成本本身。如果你不追踪你的使用情况，你就谈不上高效，你只是在被动应对。

然而，我们确实看到了客户在使用模型方面的一个趋势。我们一直倡导为特定的工作使用*正确*的模型。你不需要为每一个任务（比如情感检测或基础数据处理）都使用庞大且昂贵的[前沿模型](https://www.iguazio.com/glossary/frontier-model/)。对于这些任务，更小、更高效的模型实际上效果更好。我们认为我们的角色是提供一个环境，让你能够轻松地在不同模型之间进行切换，使用你的专有数据对它们进行微调，并严格管理在你组织内运行的内容。

高效并不是指少做事，而是指更聪明地使用你所拥有的资源。我们正在为开发人员提供优化的工具，而不仅仅是消费的工具。

**问：您刚才提到了“非传统构建者”。这种智能体堆栈是如何改变公司内部软件开发人员的画像的？**

**Kleinerman：** 这对我来说是最令人兴奋的部分。几十年来，构建数据管道或使业务流程自动化的能力一直仅限于少数重度工程团队。借助 CoCo，我们看到分析师和懂数据的业务用户（这些人比任何人都更了解业务逻辑）开始独立创建管道和自动化工具。

当利用 AI 进行构建变得像描述你想要的结果一样简单时，能够为组织 AI 战略做出贡献的人数就会呈指数级增长。我们并不是在取代软件工程师，而是在将这一角色从编写代码的人演变为编排系统的人。

**问：展望未来，您如何看待在这个智能体世界中，诸如 Salesforce 或 SAP 等应用软件厂商与像 Snowflake 这样的数据平台提供商之间的竞争？谁将主导这一过程？**

**Kleinerman：** 这是一个富有洞察力的问题，坦率地说，这仍然是一个处于发展中的故事。你拥有那些对销售流程或审批工作流应该如何运作有着深厚上下文理解的业务流程厂商。然后你又拥有像我们这样的数据平台，它掌握着企业数据的重力中心。

> “我相信，谁能打造出最‘令人愉悦’的产品，谁就是赢家。”

我相信，谁能打造出最“令人愉悦”的产品，谁就是赢家。互联网之所以被接受，并不是因为一份技术宣言，而是因为它让人们能够做到以前无法想象的事情。我们希望成为连接这两者的纽带——将来自那些业务应用的上下文带入我们受治理且数据丰富的环境中。我认为“赢家”最终会是客户，他们将从这些系统最终实现互联互通中受益。