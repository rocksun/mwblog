<!--
title: Anthropic 想成为智能体 AI 领域的 AWS
cover: https://cdn.thenewstack.io/media/2026/04/81cd4b15-greg-daines-pxlbhkn9n78-unsplash.jpg
summary: Anthropic 推出了 Claude 托管智能体及持久记忆，旨在从模型开发商转型为 AI 基础设施平台。该产品通过提供安全沙箱和会话管理，降低了企业级智能体的开发门槛，显示其正加速成为智能体 AI 领域的 AWS。
-->

Anthropic 推出了 Claude 托管智能体及持久记忆，旨在从模型开发商转型为 AI 基础设施平台。该产品通过提供安全沙箱和会话管理，降低了企业级智能体的开发门槛，显示其正加速成为智能体 AI 领域的 AWS。

> 译自：[Anthropic wants to be the AWS of agentic AI](https://thenewstack.io/anthropic-agents-managed-aws-claude/)
> 
> 作者：Jessica Wachtel

本月早些时候，[Anthropic](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/) 发布了 [Claude 托管智能体](https://platform.claude.com/docs/en/managed-agents/overview) 的公开测试版。两周后，它又增加了持久记忆功能。从这些以及近期许多围绕 Claude 的发布活动中可以清楚地看出，Anthropic 销售的不只是模型。它现在正在销售大规模运行模型所需的基础设施。

我为你测试了 Claude 的托管智能体和持久记忆。我发现这是一个为熟悉一定开发水平的人员构建的产品。该产品更多是为了满足工程团队当前的需求，而不是为个人开发者设计的测试友好型软件。

## 什么是带持久记忆的 Claude 托管智能体？

托管智能体是一套 API，在交付生产级 AI 智能体之前，开发者过去必须亲自构建这些功能。这就是基础设施的转变。它是内部构建与 Claude 托管智能体提供的 API 之间的对决，后者提供诸如安全沙箱、长时间运行的会话、检查点、凭据管理、作用域权限以及端到端追踪等功能。

其提供的定价模式也反映了基础设施产品的特征。除了标准的 Claude API Token 费率外，托管智能体每会话小时收费 0.08 美元。建立测试的成本很低（但我确实必须在我的 Claude 余额中充值 20 美元），但成本会迅速增加。对于一家每天运行数百个智能体会话的公司来说，这完全是另一种计算方式。

## 我在初步测试中的发现

入门过程正如我所希望的那样：快速且简单。控制台会引导你完成四步快速启动，包括创建智能体、配置环境、开始会话和集成。预置模板处理了大部分设置工作。我在没有编写任何代码的情况下，在五分钟内就运行了一个研究智能体。控制台甚至用平实的英语询问我，该智能体是需要不受限制的网络访问，还是应限制在特定的主机，然后根据我的回答自动配置了环境。

这些预置模板揭示了 Anthropic 认为的真实应用场景。其中包括：一个进行多步网页研究并综合来源的“深度研究员（Deep Researcher）”；一个每周扫描软件博客并编写变更简报的“领域监测员（Field Monitor）”；一个负责分类 Sentry 警报、开启 Linear 工单并运行 Slack 战情室的“事故指挥官（Incident Commander）”；以及一个从 Linear 提取已完成的迭代并在会议前编写回顾文档的“迭代回顾促进者（Sprint Retro Facilitator）”。

所有这些任务都可以在没有人工干预的情况下自主运行。

## 哪些因素让测试变得困难

控制台很快就从[无代码](https://thenewstack.io/no-code-is-dead/)转向了代码。当我测试数据分析模板时，第二个提示要求我使用 [Python](https://thenewstack.io/python/) 代码调用 Files API。虽然这对于使用自主智能体读取真实数据的人来说非常棒，但它很快就让测试过程变得不那么像无代码体验了。同样，对于深度研究智能体，我无法为了妥善测试智能体而获取到我想要的研究内容。当我发出一个详细且复杂的查询时，系统超时了。它返回了我通过简化查询请求的数据，但结果感觉与 Claude 聊天应用太相似了，所以我没有进一步调查。这进一步证明了托管智能体是为大规模交付产品的工程团队准备的真实基础设施。

Anthropic 提到的公司有助于说明完整的情况。[Notion](https://www.notion.com/product) 使用它来并行运行数十个任务，同时团队在输出上进行协作。[乐天 (Rakuten)](https://www.rakuten.com/) 在一周内就跨工程、产品、销售和财务部门部署了各个领域的专家智能体。[Asana](https://app.asana.com/) 构建了 AI 队友，在 Asana 项目中与人类并肩工作。[Sentry](https://sentry.io/welcome/) 在一个流程中就实现了从标记 Bug 到可评审的修复。对于大规模生产部署而言，[Claude 托管智能体已经成为了基础设施](http://claude.com/blog/claude-managed-agents)。

上周，Anthropic 增加了持久记忆，这让智能体能够在不同会话之间学习和改进。例如，处理客户文档的智能体现在可以记住上周学到的内容，而无需在提示词中重新刷新该主题。你可以在 Claude 中看到这一点，因为它现在在聊天之间提供持久记忆。

## 为什么这很重要

对 AI 基础设施产品的一个常见批评是供应商锁定。你的智能体运行在 Anthropic 的云端，通过 Anthropic 的基础设施处理你的数据，并且依赖于 Anthropic 不更改定价或弃用 API。

但更有趣的战略问题是 Anthropic 究竟在做什么。该公司已经制造了 [Cursor](https://thenewstack.io/cursor-agents-developer-workflows/)、Claude Code 和许多其他开发者工具所基于的模型。现在，它正在构建位于这些模型和生产部署之间的基础设施层。如果该层成为开发者交付智能体的默认方式，Anthropic 将不再仅仅是一个模型提供商，而会变得更接近于[智能体 AI](https://thenewstack.io/beyond-scripts-the-shift-from-automation-to-agentic-ai/) 领域的 [AWS](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/)。

那是一个规模大得多的业务。从过去三周发布的产品来看，Anthropic 正在迅速行动以占领这一领域。