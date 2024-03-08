# appCD 通过从代码自动化基础设施来减轻开发人员的负担

![appCD 通过从代码自动化基础设施来减轻开发人员的负担的特色图片](https://cdn.thenewstack.io/media/2024/03/a6a369fe-appcdlogo-1024x407.png)

旧金山初创公司 [appCD](https://appcd.com/) 认为基础设施即代码 (IaC) 未能兑现其炒作，现已开放其所谓的生成式基础设施 *源自* 代码 (IfC) 软件的早期访问权限。

同名软件根据应用程序代码自动生成基础设施，并自动应用操作和安全策略。

其创建者 [Sachin Aggarwal](https://www.linkedin.com/in/sachinyaggarwal/) 和 [Asif Awan,](https://www.linkedin.com/in/asifawan/) 都是连续创业者，曾在云、网络安全和 [MLOps](https://thenewstack.io/what-is-mlops/) 领域创建并出售公司。

Aggarwal 表示，这家公司基于他们在之前创业中吸取的经验教训，对他来说，最近一次是在 Accurics（已被 Tenable 收购），该公司检测并解决 IaC 中的安全风险。

他说，通过与客户交谈，很明显 IaC 的根本 [问题](https://thenewstack.io/a-brief-devops-history-the-roots-of-infrastructure-as-code/) 在于它是手动编写的。

Aggarwal 说：“它需要专业知识，容易出错，而且耗时。”“因此，这个想法诞生了：有没有一种方法，尤其是在我们现在都从声明式世界转向生成式世界的情况下；在这个新世界中，有没有一种方法可以让我们从代码 [本身] 生成基础设施即代码？”

“我认为这里有一个需要解决的问题。我不认为 [基础设施即代码](https://thenewstack.io/infrastructure-as-code-evolution-and-practice/) 已经完成了它的工作。现在是时候进入基础设施供应的下一波浪潮了。”

## 无需更改代码

“[基础设施即代码] 通过机器或机器对机器代码实现基础设施的部署、管理和扩展。这与涉及通过界面和附加软件层工作的传统方法形成对比，”B. Cameron Gain 在 The New Stack 上的“IaC [终极指南](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)”中写道。

他补充说：“通过命令行在各种环境中一致且高效地供应和部署基础设施，IaC 的使用非常适合 CI/CD。”

Aggarwal 认为，这种手动过程是行不通的。而且现有的 IaC 解决方案仍然需要开发人员做太多事情。

在 InfoQ 的一篇文章中，MLOps 工程师 [Claudio Masolo](https://www.linkedin.com/in/cmasolo/) 概述了 [基础设施即代码的四种主要方法](https://www.infoq.com/news/2023/02/infrastructure-code-cloud-manage/)：基于 SDK 的方法，例如 [Ampt](https://getampt.com/) 和 [Nitric](https://nitric.io?utm_content=inline-mention)；基于注释的方法（[Klotho](https://klo.dev/)）；两种方法的组合（[Encore](https://encore.dev/) 和 [Shuttle](https://www.shuttle.rs/) 或 AWS [Chalice](https://github.com/aws/chalice)，它部署使用 Python 中的 AWS Lambda 的应用程序）；以及引入新的编程语言，例如 [Winglang](https://www.winglang.io/) 和 [DarkLang](https://darklang.com/)。同时，[Pulumi](https://www.pulumi.com?utm_content=inline-mention) 和 [AWS](https://aws.amazon.com/?utm_content=inline-mention) 云开发工具包 ( [CDK](https://github.com/aws/aws-cdk)) 基于使用现有语言的想法。

Aggarwal 说：“我们的方法非常简单。”“我们说我们不希望你在代码中进行任何单行更改。不，没有 SDK，没有注释。……我们不会给你提供新的配置语言或新的描述性语言。……如果你正在使用 Terraform，或者如果你正在使用 Helm 图表或 [AWS] CloudFormation，我们将以你的团队习惯看到的语言或代码库为你提供基础设施即代码。”

## 正确的规模和正确的权限

尽管该公司称其软件为“生成式 IfC”，但其引擎基于机器学习，而不是 [依赖生成式 AI](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)。

你将 Java 或 Python 代码（它目前支持这两种语言）检入存储库，appCD 会对该代码进行分析，然后向用户展示它认为适合此代码的最佳基础设施。它支持 AWS 上的 Terraform、[OpenTofu](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/) 和 [Helm](https://thenewstack.io/applying-kubernetes-security-best-practices-to-helm-charts/)，并即将支持 [Microsoft](https://news.microsoft.com/?utm_content=inline-mention) Azure。
“这给了我们两样东西，”阿格瓦尔说。“它允许我们进行适当规模的基础设施建设，因为当您有不同的团队编写 Terraform 代码时，有时会丢失上下文，并且往往会过度配置这些资源。……但更重要的是，我们还为您提供了适当规模的权限。”

通过全面了解此应用程序应执行的操作以及它应与之通信（或不应与之通信）的资源或其他微服务，可以建立适当的权限。

现有工具要求开发人员不仅精通应用程序开发，还精通云基础设施和 IaC。然后是平台工程和安全团队也参与其中的合规性、安全性和操作策略。appCD 认为开发人员不必学习任何新东西。

appCD 工具可以：

**分析**代码以推断 API、服务配置、入口/出口和环境变量。
**可视化**部署架构，使用户能够通过拖放功能进行更改。阿格瓦尔将此图表或拓扑描述为“Figma 满足 HashiCorp 的一种东西”，它可以进行更改，但仍然不需要用户学习底层语言，除非他们愿意。
**生成**基于应用程序推断的云依赖项的 Terraform/OpenTofu 或 Helm 图表，并自动应用 HIPAA、NIST-CSF、PCI 和 GDPR 等法规的标准。还可以添加特定于公司的策略。

“在云中加速部署应用程序的圣杯需要以自动化、安全的方式创建基础设施即代码，并具有最少的权限，并与最佳架构实践保持一致，”Lexmark International 的首席信息官兼首席技术官 [Vishal Gupta](https://www.linkedin.com/in/vishal-gupta-046149/) 说。“appCD 最接近从应用程序代码本身实现这一愿景，并为平台团队带来极佳的价值。”

除了早期访问之外，该公司宣布已获得 600 万美元的种子资金。如果您想试用，它提供了一个 [游乐场环境](https://docs.appcd.io/getting-started/playground)。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。