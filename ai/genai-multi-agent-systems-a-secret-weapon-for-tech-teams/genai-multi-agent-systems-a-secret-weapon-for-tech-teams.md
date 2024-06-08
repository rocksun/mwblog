
<!--
title: GenAI多Agent系统：技术团队的秘密武器
cover: https://cdn.thenewstack.io/media/2024/05/548c0dd3-synthetic-8597464_1280.jpg
-->

多 Agent 生成式 AI 系统可以极大地增强和加速构思、设计和测试新产品。

> 译自 [GenAI Multi-Agent Systems: A Secret Weapon for Tech Teams](https://thenewstack.io/genai-multi-agent-systems-a-secret-weapon-for-tech-teams/)，作者 Dan Kraemer。

如今，许多开发人员和产品团队使用 [生成式 AI](https://thenewstack.io/ebooks/generative-ai/how-generative-ai-transforms-software-development/) (GenAI) 代理来帮助构建软件或应用程序——真正的创新发生在多 Agent 系统中。就像一个管弦乐队可以演奏出丰富、复杂的交响乐——而独奏音乐家只能在一个维度上发出声音——多 Agent 系统超越了面向任务的角色，真正为开发和战略团队注入了动力。

例如，梅奥诊所、沃达丰和 ADT 等公司的开发人员正在使用 Google 的 [GenAI 代理构建器](https://cloud.google.com/blog/products/ai-machine-learning/build-generative-ai-experiences-with-vertex-ai-agent-builder) 在多 Agent 环境中创建应用程序。对于我将在下面详细描述的多 Agent 系统，开发人员可以制作出功能丰富、高度直观的产品，以低成本和创纪录的时间取悦用户。

多 Agent GenAI 系统与它们听起来很像：一群协同工作的 AI 代理。一个代理执行一项任务，例如编码副驾驶，而多 Agent 系统则结合了多个 [开发任务](https://thenewstack.io/risk-aware-vs-risk-averse-product-development/)——产品构思、设计、测试、客户细分等——它们相互学习以优化创造力和生产力。成功的多 Agent 系统充当开发团队的“数字孪生”，不断生成多个新概念和未来场景。多 Agent 系统不会取代 [开发和产品团队](https://thenewstack.io/engprod-the-secret-of-elite-developer-teams/)，而是增强它们。

构建多 Agent 系统的方法有很多，但有三种流行的方法：

- 集中式，中心有一个代理收集和同化所有其他输出
- 分布式，没有中央控制器，代理在“代理群”中直接相互协调
- 分层式，代理按团队或分层组织

对于 [产品开发团队](https://thenewstack.io/platform-teams-adopt-these-7-developer-productivity-drivers/)，集中式或分层式架构效果最佳，因为它们提供了对流程的更多控制。将每个 Gen AI 代理视为一个人，该人在人类团队中精通一件事。你可以为产品开发过程的每个部分创建一个单独的 AI 代理：产品头脑风暴、客户细分、技术规格、功能、能力等。辐条中心或层次结构末端的中央代理会考虑其他所有代理的所有输出，以“吐出”出色的产品创意。

## 在矢量化数据库中收集数据

现在你已经为多 Agent 框架选择了结构，并为产品构思过程的每个部分构建了多个代理，你需要让代理开始工作。首先，授予选定的代理访问相关知识的外部数据库的权限。为此，你需要从公司中提取大量专有数据：客户细分、产品信息、研究等。你可能还希望提取代理要使用的一些相关外部数据源。

例如，这可能是全球市场趋势、定价报告或公共数据集，还可能包括抓取 Reddit 和其他论坛以获取更多定性的 [消费者行为数据](https://thenewstack.io/3-steps-to-unlock-the-power-of-behavioral-data/)和偏好。为了确保代理可以从一个地方访问所有这些数据，你需要一个代理可以访问的矢量数据库。Pinecone 由于其灵活性和文档质量而成为一个流行的矢量数据库，但市场上有许多选择。

## 为每个代理编写智能提示

下一步是为每个代理创建唯一的提示。这可能需要一些练习和迭代，但开始的最佳方法是决定你希望每个代理遵循的思维框架和角色。例如，你可能需要一个用户研究代理，该代理是将用户研究语境化并 [搜索你的矢量化](https://thenewstack.io/vector-search-is-coming-to-apache-cassandra/)数据库以查找用户引用的专家，这将帮助它了解特定类型的用户。一旦你为代理设定了角色，就创建具有结构的提示。代理应该有关于你希望输出是什么样子的具体说明，直到它返回的示例数量。这有助于你从代理中获得更多收益，并允许它 [与系统中的其他代理更有效地协同工作](https://thenewstack.io/putting-ai-to-work-systems-of-intelligence-and-actionable-agency/)。

提示应该说什么，应该深入到什么程度？即使有无数的机会为你的提示创建结构以塑造理想的输出，公式的这部分也是无限灵活的。基于你对产品开发、商业框架和以用户为中心的设计的知识，创建尽可能动态和具体的提示。

## 让代理协同工作

为了让您的代理以协调的方式协同工作，部署一个用于此目的的工具是值得的。用于连接多个代理的三种流行工具是 [CrewAI](https://www.crewai.io/)、[LangChain](https://www.langchain.com/) 和 [Microsoft Autogen](https://microsoft.github.io/autogen/)。它们各自都有自己的一组优势，因此我们建议查看每个优势并找到适合您项目的解决方案。

一旦您的提示经过微调，您的多代理系统应该开始输出产品设计和场景。您可以通过将多代理系统连接到其他 GenAI 工具（如 Dall-E）来使这些场景变为现实，这些工具可以创建原型图像和动画，以及：[Relume.io](http://relume.io)，它可以在几秒钟内生成 Figma 可导出线框。

## 测试原型

一旦您的多代理系统生成了几个完整的产品原型，就该测试哪些迭代最有可能成功。虽然您可以进行传统的 A/B 测试并收集真实人员的反馈，但您还可以使用另一个代理来创建 AI 驱动角色或“合成用户”来测试不同的[产品](https://thenewstack.io/adding-too-many-features-will-break-your-product-users-and-team/)。合成用户可以高度逼真；您可以通过摄取 CRM、细分数据和行业报告来创建具有目标用户所有特征的 AI 角色，然后要求这些角色（也是 AI 代理）提供反馈，指示他们“思考和行动就像您的角色”。因此，多代理系统可以有力地补充用户验证测试的各个方面。

多代理 GenAI 系统可以极大地增强和加速构思、设计和测试新产品的过程。通过结合来自不同 AI 代理的专业知识，这些代理专注于客户研究、技术规范、原型制作和测试等领域，多代理系统可以快速生成全面的产品概念，以满足特定客户细分市场的需求。借助这些强大的系统，您可以增强团队快速行动和实现创新产品成果的能力。
