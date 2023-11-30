<!--
title: Amazon Q，理解AWS和商业文档的AI
cover: https://cdn.thenewstack.io/media/2023/11/518afc99-aws-reinvent23-swami-keynote-10-1024x557.png
-->

亚马逊云创新负责人本·施赖纳设想，亚马逊Q可助中小企业快速上云

> 译自 [Amazon Q， a GenAI to Understand AWS (and Your Business Docs)](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/)，作者 Joab Jackson 是《新栈》的高级编辑，负责报道云原生计算和系统运营。他报道 IT 基础设施和开发超过 25 年，包括在 IDG 和 Government Computer News 的工作。在此之前，他是......

亚马逊网络服务拥有如此复杂的云服务阵列，该公司本身现在承认它需要一个 AI 助手来获得最佳使用。

周二，在公司位于拉斯维加斯的年度 [Re:Invent](https://reinvent.awsevents.com/) [用户大会](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/)上，AWS 推出了 [Amazon Q](https://aws.amazon.com/q/pricing/)，这是一个基于生成式 AI 的智能助手，旨在[弄清楚](https://aws.amazon.com/blogs/aws/introducing-amazon-q-a-new-generative-ai-powered-assistant-preview/)可用的 AWS 工具的调色板，甚至帮助业务用户理解手头的数据。

## Amazon Q 提供 AWS 专业知识

![](https://cdn.thenewstack.io/media/2023/11/fce5eea0-aws-ben_schreiner-300x200.jpg)

*Ben Schreiner，AWS 业务创新负责人，认为 Amazon Q 将对那些可能没有专业知识充分利用 AWS 的小企业产生重大影响。*

在许多情况下，Q 可以以重大方式帮助 AWS 的潜在用户，AWS 业务创新负责人 [Ben Schreiner](https://www.linkedin.com/in/schreiner/) 在接受采访时指出。

“AWS 是为建设者而建的，是由工程师为工程师建造的，它很棒。对于那些可能没有这种背景的人来说，或者没有开发人员可以利用的人来说，它可能令人生畏，” Schreiner 说。

Scheiner 的办公室通过使用解决方案库和其他工具帮助中小企业充分利用 AWS。与企业或大型公司不同，大多数较小的组织没有大量的开发人员或运营人员。因此，像 Q 这样的工具可以帮助他们提高云使用的水平，Schreiner 说。

“‘怎么做’是最难的部分，”Schreiner 说。使用 Q，“我不需要知道如何做到这一点，我只需要知道如何提出问题。”

## 开发人员和分析师

AWS 期望两组 Q 用户：[开发人员](https://aws.amazon.com/blogs/aws/amazon-q-brings-generative-ai-powered-assistance-to-it-pros-and-developers-preview/)和[分析师](https://aws.amazon.com/blogs/aws/amazon-q-brings-generative-ai-powered-assistance-to-it-pros-and-developers-preview/)。

对于开发人员，Q 从 IDE 中提供了一种会话式界面，可以引导用户完成启动[服务](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/)的所有步骤。新手可以从一般提出问题(“构建无服务器 API 的 AWS 无服务器服务是什么?”)到高度具体化(“我计划创建每天 10 万次请求的无服务器 API。每个请求都需要查找数据库。哪些服务最适合这种工作负载？”):

![](https://cdn.thenewstack.io/media/2023/11/9058beb5-console-1-1024x522.png)

您还可以要求它为特定工作负载建议最佳资源，例如运行 Web 服务器的[最佳实例](https://thenewstack.io/amazon-s3-express-one-zone-introduces-near-real-time-object-storage/)是什么。您应该使用哪种最具成本效益的 [Gravitron 实例](https://thenewstack.io/kafka-benchmarking-on-aws-graviton2-graviton3-and-amd/)来训练模型？Q 会做出计算。

Amazon Q 也可以帮助调试 AWS 服务。为什么 AWS Lambda 函数与 Amazon DynamoDB 表不互动？Q 将在其广泛的 AWS 服务知识库中进行一些查找......

![](https://cdn.thenewstack.io/media/2023/11/813c4a3c-resolve-2-4-1024x960-1.png)

此服务现已在 [Amazon CodeCatalyst](https://aws.amazon.com/codecatalyst/) 中提供预览，并作为 [Visual Studio](https://thenewstack.io/visual-studio-2022-and-net-6-finally-arrive/) 的插件提供，并将很快扩展到各种 IDE。

## Amazon Q for 业务用户

Q 也可用于 [QuickSight](http://aws.amazon.com/quicksight/q)，Amazon 的业务分析工具，提供帮助执行一些更常规的业务管理任务。

例如，它可以从一组数据创建项目，编写执行摘要，甚至在 AWS 的措辞中，构建叙述。

在 Amazon QuickSight 仪表板上使用自然语言，用户可以要求围绕一组数据构建一个故事。Q 将从所选可视内容中提取数据洞察和统计数据，然后总结数据对业务的潜在意义，甚至建议特定目标的想法。

![](https://cdn.thenewstack.io/media/2023/11/3a11cffb-2023-qinquicksight-rev-2-1024x327.png)

Q 的[定价](https://aws.amazon.com/q/pricing/)起价为业务套餐的每月 20 美元和开发者版的每月 25 美元。
