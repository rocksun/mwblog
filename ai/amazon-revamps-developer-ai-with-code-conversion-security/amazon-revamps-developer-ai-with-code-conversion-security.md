
<!--
title: 亚马逊用代码转换和安全功能改造开发者AI
cover: https://cdn.thenewstack.io/media/2024/09/4221e1bd-qdeveloper.jpg
-->

亚马逊 Q 开发者，一个经过改进的 AI 代码助手，帮助亚马逊将 30,000 个应用程序转换为 Java 17，并节省了 4,500 年的开发工作。

> 译自 [Amazon Revamps Developer AI With Code Conversion, Security](https://thenewstack.io/amazon-revamps-developer-ai-with-code-conversion-security/)，作者 Loraine Lawson。

亚马逊花费了 50 个开发者日才将一个应用程序从 Java 8/11 更新到 Java 17。凭借其最近发布的 [重塑的 AI 协同程序](https://aws.amazon.com/blogs/devops/reinventing-the-amazon-q-developer-agent-for-software-development/)，[Amazon Q Developer](https://aws.amazon.com/q/developer/)，这家电子商务公司能够在 10 分钟内 [转换类似的应用程序](https://www.youtube.com/watch?v=63KCD7fvu4s)。

该公司表示，一个由五名开发人员组成的团队使用 Q Developer 将 30,000 个生产应用程序从 Java 8 或 Java 11 转换为 Java 17。该公司补充说，这节省了超过 4,500 年的开发工作，并从性能改进中每年节省了 2.6 亿美元。

Amazon Q Developer 是 [Code Whisperer](https://thenewstack.io/decoding-amazons-generative-ai-strategy/) 的重新设计版本，Code Whisperer 于 4 月合并到 Q Developer 中。

## Q Developer 作为编码伙伴

亚马逊生成式 AI 应用程序和开发者体验总监 [Srini Iragavarapu](https://www.linkedin.com/in/isvas/) 表示，Amazon Q Developer 的设计并非仅仅执行代码补全，而是为了支持整个软件开发生命周期。

![Amazon Q 在 IDE 中工作的屏幕截图](https://cdn.thenewstack.io/media/2024/09/66728972-screenshotamazonq.jpg)

*来自 [Amazon Q Developer 视频](https://youtu.be/U0ZSldhbWs8) 的屏幕截图。*

“我们不是从编码的角度或开发的角度来看待它，”Iragavarapu 告诉 The New Stack。“我们实际上将其视为一个完整的软件开发生命周期，开发人员从‘我计划我的项目，我了解需要做什么，获取需求，我实现它们，我部署它们，对它们进行故障排除，然后维护它们’开始。”

他说，Q Developer 能够编写测试、优化代码、调试云计算和 AWS 资源。它可以使用描述性的 [自然语言提示](https://roadmap.sh/prompt-engineering) 构建新的应用程序功能。用户还可以与 Amazon Q 一起迭代计划，审查潜在的代码建议并要求改进。

他还补充说，它还通过执行 [代码安全扫描](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security.html) 并向开发人员更新潜在的安全问题，帮助开发团队“左移”。该公司声称，Amazon Q Developer 在大多数流行的编程语言的检测方面已经超越了领先的公开可比工具。

亚马逊希望 Q Developer 的功能与另一位软件开发人员一样，在您编码时为您提供帮助。例如，对于一个不熟悉的仓库，开发人员要么阅读文档，要么询问高级软件工程师或同事它是什么。

“您可以做的一件事是询问 Q，您能解释一下这个特定函数在做什么吗？所以它实际上是在查看这个函数，”他说。“它逐行地进行。感觉就像你身边坐着一位开发人员，和你聊着所有这些事情。”

当然，它还会生成代码建议，并且超越单行补全，提供进一步的编码建议。

## Q 堆栈

除了 Q Developer 之外，亚马逊还提供 Q Business，它专注于业务角色和内部数据。

Q 解决方案有三个层。底层包括两个定制芯片，AWS Trainium，它经过微调以训练模型，以及 AWS Inferential，它经过微调以进行推理。底层还包括 Sagemaker，亚马逊的基于云的机器学习平台。Sagemaker 构建、训练和部署机器学习和生成式 AI 模型。

> “同样，我们希望使其具有交互性。把它想象成你正在与一个配对程序员一起编码，”
>
> — 亚马逊生成式 AI 应用程序和开发者体验总监 Srini Iragavarapu

中间层由工具和预训练的基础模型组成，用于构建和扩展由生成式 AI 驱动的应用程序。它建立在 Bedrock 之上，Bedrock 是亚马逊的生成式 AI 平台。他说，Bedrock 集成了各种大小和功能不同的大型语言模型 (LLM)，包括 Anthropic 的模型、亚马逊自己的模型和 Llama 模型，供客户构建应用程序。

顶层是 Amazon Q Business 和 Q Developer，它们是内置生成式 AI 的应用程序，不需要任何特定的机器学习专业知识。

## 亚马逊：不使用企业数据进行训练

Iragavarapu 说，亚马逊不会存储或使用任何客户数据来改进企业版本的底层服务。[免费层](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-free-tier.html) 为开发人员提供了一个选择退出任何代码收集的选项。

“与传统的 AI 服务不同，在传统的 AI 服务中，您必须选择退出才能说‘请不要使用我的任何数据’，而作为客户，在这种情况下，在专业版中，您甚至不必选择退出，因为我们根本不会存储任何数据，”他说。“在我们踏上这段旅程时做出的第一个决定是，我们很快意识到代码以及与软件相关的任何内容都是每个客户都希望能够使用和提供的知识产权。因此，我们说，让我们不要利用客户提供给我们的任何服务，只进行响应，而不是使用或存储任何内容来改进我们的服务。”

## 理解他人的代码
Q Developer 解决的一个痛点是分析一个代码库以确定代码的实际功能。Copilot 也能做到这一点，但与 Copilot 不同的是，Q Developer 会回答开发人员可能对代码库提出的问题。例如，如果代码库使用 DynamoDB 或开发人员不理解的其他内容，开发人员还可以提出后续问题，例如为什么使用它。

“我们的想法是，这是一个多步骤推理系统，它结合了我们通过 Bedrock 获得的大型语言模型，以及程序分析和我们在亚马逊构建应用程序数十年积累的丰富经验，”他说。

## Q Developer 的工作原理

亚马逊使用 SWE-bench 来评估其模型。SWE-bench 是一个基准数据集，旨在评估 LLM 在解决现实世界软件工程 (SWE) 问题方面的能力。它是一个 GitHub 问题与相应拉取请求的集合，提供了一个数据集，帮助研究人员确定 LLM 在理解、分析和生成代码解决方案方面的能力。

![屏幕截图显示了审查和接受或拒绝 Amazon Q Developer 代码的能力。](https://cdn.thenewstack.io/media/2024/09/8c07ca18-dev-agent-08_amazon.png)

*[亚马逊博客](https://aws.amazon.com/blogs/devops/reinventing-the-amazon-q-developer-agent-for-software-development/) 中的屏幕截图显示了审查和接受或拒绝 Amazon Q Developer 代码的能力。*

在 SWE-bench 的排行榜上，截至 2024 年 5 月 9 日，亚马逊 Q Developer 在精简版中解决了 20.33% 的问题。自首次评估以来，亚马逊已使用其他 LLM 更新了 Q，并收集了有关开发人员喜欢和不喜欢的内容的反馈——包括来自其约 80,000 名开发人员的内部反馈，以及来自外部用户的反馈。

在内部，AWS 进行了一项生产力挑战，发现使用 Q Developer 的开发人员成功完成任务的可能性高出 27%。亚马逊还报告称，Q Developer 在执行多行代码建议的助手领域拥有业界最高的代码接受率，BT 集团最近报告称他们接受了 Q 37% 的代码建议，澳大利亚国民银行报告称接受率为 50%，据公司发言人称。

他们收到的反馈之一是，很难判断该工具更新了什么。现在，Q Developer 提供了有关其实际执行操作的持续状态，这很重要，因为它可以修改多个文件并创建新文件，他补充道。

“同样，我们希望使其具有交互性。把它想象成你正在与一个配对程序员一起编码，”他说。“在这种情况下，如果我接受它，它实际上会获取代码，然后开始执行它。相反，你也可以说提供反馈并重新生成。”

## 开发人员需要了解的内容

到目前为止，Q Developer 支持 [15 种编程语言](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/faq.html)：

1. [JavaScript](https://thenewstack.io/free-javascript-from-legal-clutches-of-oracle-devs-petition/)
2. [TypeScript](https://thenewstack.io/typescript-5-5-faster-smarter-and-more-powerful/)
3. [Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/examples-python.html)
4. [Java](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-code-generation/examples-java.html)
5. C#
6. [Go](https://thenewstack.io/golang-how-to-use-the-go-install-command/)
7. [Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/)
8. [PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)
9. Ruby
10. [Kotlin](https://thenewstack.io/how-to-handle-platform-specific-dependencies-in-kotlin-multiplatform/)
11. C
12. C++
13. Shell 脚本
14. [SQL](https://thenewstack.io/sql-nosql-and-vectors-oh-my/)
15. Scala

它还支持基础设施即代码语言和工具，包括 [TerraForm 的 HCL](https://thenewstack.io/terraforms-best-practices-and-pitfalls/)（HashiCorp 配置语言）和 CDK（云开发工具包）。

目前，AI 代理提供免费层和付费企业层，企业层允许管理员为组织内的所有开发人员启用该工具，并提供有关可访问代码的管理员控制。

“我的一些朋友一直问我，‘等等，一定有陷阱。是免费增值模式吗？你想要从中得到什么？’ 真的什么都没有。它是免费的。任何人都可以使用它，安装它，”Iragavarapu 说。“我们的想法是，我们希望让开发人员能够构建应用程序，使用生成式 AI，并为客户想出创造性的问题解决方法。”

要开始使用，开发人员需要拥有 AWS Builder ID 或属于已设置 AWS IAM Identity Center 实例的组织，该实例允许他们使用 Amazon Q。要使用 [Amazon Q 开发人员代理在 IDE 中](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html)，请先安装 Amazon Q 扩展，该扩展适用于 JetBrains、Visual Studio Code、Visual Studio（预览版）和 macOS 上的命令行。
