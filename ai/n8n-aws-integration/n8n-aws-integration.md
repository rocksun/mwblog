
<!--
title: 用 n8n 和 MCP 搭建 AI AWS 基础设施
cover: https://www.clickittech.com/wp-content/uploads/2025/10/How-to-Build-an-AWS-Infrastructure-with-n8n-MCP.png
summary: AI 驱动 AWS 管理，无需 CLI。整合 n8n、MCP、AWS Bedrock，实现安全与成本审计自动化，几分钟完成数周工作。每月成本约 50 美元，赋予 DevOps 工程师超能力。
-->

AI 驱动 AWS 管理，无需 CLI。整合 n8n、MCP、AWS Bedrock，实现安全与成本审计自动化，几分钟完成数周工作。每月成本约 50 美元，赋予 DevOps 工程师超能力。

> 译自：[How to Build an AI AWS Infrastructure with n8n and MCP](https://www.clickittech.com/ai/n8n-aws-integration/)
> 
> 作者：Gustavo Cuevas

管理 AWS 基础设施不再需要掌握无休止的 CLI 命令或 Terraform 脚本。本指南展示了我们如何通过 [n8n](https://n8n.io/) AWS 集成、[MCP](https://modelcontextprotocol.io/docs/getting-started/intro) 和 [AWS Bedrock](https://aws.amazon.com/bedrock/?trk=12e9583c-b3d9-47d2-88c3-24890403ad1d&sc_channel=ps&ef_id=Cj0KCQjwsPzHBhDCARIsALlWNG0jUo4vmx4ZNMGfCQcZTGG3S-eZ9bKnd64PCqJUhcf1IwF-Sfh00lMaAiMxEALw_wcB:G:s&s_kwcid=AL!4422!3!780636715672!e!!g!!aws%20bedrock!23183030539!184407538741&gad_campaignid=23183030539&gbraid=0AAAAADjHtp_yLVKKDJdzYS1iRKcOZTqsp&gclid=Cj0KCQjwsPzHBhDCARIsALlWNG0jUo4vmx4ZNMGfCQcZTGG3S-eZ9bKnd64PCqJUhcf1IwF-Sfh00lMaAiMxEALw_wcB) 构建了一个由 AI 驱动的审计代理，将数月的工作量缩短到几分钟。

无需记忆命令，想象一下您可以用简单的英语向您的基础设施提问。

## 我可以通过与 AI 聊天来管理我的 AWS 设置吗？

任何管理过复杂 AWS 设置的人都深知其中的不易。**AWS CLI、Terraform 或 CloudFormation 的学习曲线**可能非常残酷。但通过 **n8n AWS 集成**，我们用自然语言命令取代了这一切，就像告诉 DevOps 队友该做什么一样。

***阅读我们的博客 [Terraform 与 CloudFormation](https://www.clickittech.com/devops/terraform-vs-cloudformation/)***

**真实案例：**

“对此账户执行全面的安全评估。”
几秒钟内，**AI 审计代理**就会自动执行，无需脚本，没有错误，也没有上下文丢失。

![How does the DevOps Assistant Work diagram from chat_input to DevOps_ Assistant and Slack_Responce](https://www.clickittech.com/wp-content/uploads/2025/10/How-does-the-DevOps-Assistant-Work-986x1024.png)

## 为什么将 n8n 与 AWS 结合用于 DevOps 助手？

真正的创新不是构建 AI；而是消除了像 AI 一样思考的需求。

正如 AI 取代了学习 SQL 语法的需求一样，**n8n + MCP 与 AWS 的集成**用自然语言提示取代了手动 AWS 命令。

* 不再需要记忆 CLI 语法。
* 不再需要对 YAML 或 JSON 感到困惑。
* 只需*用简单的英语执行基础设施操作*。

这一抽象层使非工程师也能使用 AWS，并将高级 DevOps 工作流的速度提高了十倍。

我们证明了企业级 AI 自动化不需要企业级预算。

使用 **n8n（自托管）**和 **MCP**，整个 **AI 审计代理**运行在**单个 AWS T3.large 实例上（约 50 美元/月）**。

**主要统计数据：**

* 每月成本：约 50 美元
* LLM：通过 **AWS Bedrock** 使用 Claude 3 Sonnet
* 编排：**n8n AWS 集成** + Docker
* 环境：自托管 + 可扩展

## AWS 审计代理实际如何工作？

编排准备就绪后，我们构建了 **AWS 审计代理**，它是 DevOps 助手的专业版本，专注于**安全和成本优化**。

它监听来自 Slack 的自然语言命令，通过 **AWS Bedrock** 上的 Claude 3 Sonnet 进行处理，并使用 **MCP 客户端**从以下服务获取真实数据：

* AWS Cost Explorer
* AWS CloudTrail
* AWS Well-Architected Tool
* AWS 定价和 API 客户端

然后它会在 Slack 中生成一份详细报告，突出显示风险、开放端口、IAM 角色和立即行动项。

![diagram of how does the AWS Audit Agent work, from AWS Bedrock, simple memory, AWS Cost explorer and AWS Cloudtrail](https://www.clickittech.com/wp-content/uploads/2025/10/How-does-the-AWS-Audit-Agent-Work-1-986x1024.png)

在一次现场测试中，我们进行了一次全面的安全审计。现场一位高级 DevOps 工程师估计手动执行需要 1 周时间。我们的 AI 代理在**五分钟内**完成了。

这不仅仅是自动化，这是转型。该代理在一个报告中找到了未使用的 IAM 角色，标记了缺失的 MFA，并识别了开放的安全组。

关键教训是：**AI 大脑**（Claude 3 Sonnet）可以互换，但 **MCP + n8n AWS 集成**框架才是实现这一切的基础。

## DevOps 中 AI 的下一步是什么？

这个项目教会了我们比自动化更重要的事情：
AI 并不是取代 DevOps；它正在赋予 DevOps 工程师**超能力**。

通过结合 **n8n 的低代码灵活性**、**AWS Bedrock 的智能**和 **MCP 的模块化设计**，我们现在拥有了下一代工具的蓝图：

* AI 成本优化代理
* 安全合规助手
* 在事件发生前预测事件的监控机器人

由于所有这些都可以在 AWS 上经济高效地运行，它不再是一个概念；它今天就可以部署。

## 常见问题

**构建此 AI AWS 基础设施需要哪些关键组件？**

核心架构依赖于三种主要技术的集成：
**1. 编排和灵活性：** n8n 为工作流提供了低代码灵活性和编排功能（通常是自托管）。
**2. 智能：** 大语言模型（LLM），例如通过 AWS Bedrock 使用的 Claude 3 Sonnet，为系统提供 AI 大脑。
**3. 模块化设计和数据访问：** MCP 客户端促进了与各种 AWS 服务的连接和实际数据访问。
n8n + MCP 与 AWS 框架的集成是使整个自然语言操作成为可能的重要基础。

**AWS 审计代理可以执行哪些具体任务，以及由此带来的性能改进是什么？**

AWS 审计代理是 DevOps 助手的专业版本，专注于安全和成本优化。

当收到自然语言命令（通常通过 Slack 接收）时，代理会使用 AWS Bedrock 上的 LLM 处理请求，并利用 MCP 客户端从 AWS Cost Explorer、AWS CloudTrail、AWS Well-Architected Tool 和 AWS Pricing 等 AWS 服务中获取真实数据。
然后代理会在 Slack 内部生成一份详细报告，突出显示特定风险，包括未使用的 IAM 角色、缺失的 MFA 和开放的安全组，以及立即行动项。在一次现场测试中，AI 代理在 5 分钟内完成了一次全面的安全审计，而一位高级 DevOps 工程师估计手动执行需要 1 周时间。

**部署这种企业级 AI 解决方案的成本效益如何？**

该项目表明企业级 AI 自动化不需要企业级预算。整个 AI 审计代理基础设施运行成本低廉。
该系统（使用 n8n 自托管和 MCP）可以在单个 AWS T3.large 实例上运行，每月成本约为 50 美元。环境是自托管且可扩展的。