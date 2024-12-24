
<!--
title: 从IaC到云管理：Pulumi的演变历程
cover: https://cdn.thenewstack.io/media/2024/10/0aaf99a0-chuttersnap-tsgwbumanue-unsplash.jpg
-->

该公司多年来一直是基础设施即代码的参与者，但现在正在扩展到包括安全和云管理，作为三足凳的另外两条腿。

> 译自 [From IaC to Cloud Management: Pulumi's Evolution Story](https://thenewstack.io/from-iac-to-cloud-management-pulumis-evolution-story/)，作者 Jeffrey Burt。

[Pulumi](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/)七年来一直在构建其旗舰[基础设施即代码](https://thenewstack.io/infrastructure-as-code-in-any-programming-language/) (IaC)产品，为开发人员和[DevOps](https://thenewstack.io/devops/)团队提供一种更轻松、开源的方式来自动创建和管理其云基础设施。他们可以使用任何他们想要的编程语言，从C#和YAML到Python、[Go](https://thenewstack.io/russ-cox-steps-down-as-tech-lead-of-go-programming-language/)和Java。他们可以将其成果部署到超过170个对他们有意义的云提供商中，包括[亚马逊网络服务 (AWS)](https://aws.amazon.com/?utm_content=inline+mention)、微软Azure和[谷歌云](https://cloud.google.com/?utm_content=inline+mention)平台等巨头。

这对公司来说非常有效，联合创始人兼首席执行官在最近的一篇博客文章中指出，Pulumi的IaC下载量[超过1亿次](https://www.pulumi.com/blog/pulumi-up-2024/)，并且在之前的几周内获得了[HashiCorp](https://thenewstack.io/hashicorps-radar-scans-repos-commits-and-pulls-for-leaks/)的[Terraform](https://thenewstack.io/terraform-isnt-dead/)贡献量的167%和[OpenTofu](https://thenewstack.io/opentofu-amiable-to-a-terraform-reconciliation/)贡献量的300%。

“Pulumi不仅是最强大的IaC技术，而且越来越受欢迎和充满活力，”Duffy写道。

现在，该公司发现自己身处一个正在经历剧变的IaC市场，因为HashiCorp近年来已成为主导玩家，正准备被纳入庞大的IBM体系，[IBM收购该公司](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/)的[64亿美元交易](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/)预计将在年底前完成。此次收购将在已经竞争激烈且不断发展的市场中为Pulumi等供应商创造更多空间。

这是一个巨大且不断增长的领域。根据Fortune Business Insights的分析师预测，全球IaC市场将从去年的9.087亿美元增长到[2030年的33亿美元以上](https://www.fortunebusinessinsights.com/infrastructure-as-code-market-108777)。

该公司将继续发展Pulumi IaC，同时还将提供[Pulumi ESC](https://www.pulumi.com/product/secrets-management/)和[Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/)用于云管理的安全管理产品。Duffy和其他高管过去曾谈到过这些产品，但在最近的PulumiUP虚拟活动中，他们将所有这些产品整合在一起，创建了一个统一的平台，他们表示该平台将满足开发人员的所有基础设施需求。

“这是Pulumi第一次真正作为一个多产品平台推出，”Duffy告诉The New Stack。“我们以我们的基础设施即代码产品而闻名，它是开源的。这仍然是我们正在做的一切的动力。如果没有Pulumi IaC的基础，Insights就不可能实现。现在，我们拥有这三个相互独立但协同更好的产品，它们可以独立采用。我们真的想成为一个值得信赖的合作伙伴。如果您是基础设施副总裁，我们正试图解决您遇到的每一个关键任务问题。”

## 一年多的筹备

这家位于西雅图的公司[首次向业界展示](https://thenewstack.io/pulumi-intros-new-secrets-management-platform-engineering-tools/)了Pulumi ESC（代表“环境、密钥和配置”）——去年，数百家组织参与了公开测试。它现在已正式上市。对于开发人员来说，Pulumi ESC 是一个管理所有环境、密钥和配置的中心位置，它正好位于他们的源代码（例如HashiCorp的Vault、AWS Secrets Manager、Azure Key Vault、[谷歌云](https://thenewstack.io/google-cloud-adds-genai-core-enhancements-across-data-platform/) Secrets Manager、Password1和Pulumi Cloud Secrets）和目标环境（例如相同的 major cloud providers 以及 GitLab、Docker 容器、[Kubernetes](https://thenewstack.io/kubernetes/)、Cloudflare Workers 和 Pulumi 本身）之间。

“它是全自动的。你可以在中心位置定义所有密钥和所有环境，然后开发人员可以访问和组合它们，”他说。“它与现有的密钥存储集成……我们为他们提供了一个标准接口，开发人员可以轻松使用，而基础设施和安全团队可以审核所有访问权限，控制所有访问权限，并在必要时从一个地方撤销访问权限。你无需再关注可能出现密钥的十几个不同的地方。只需访问一个中心位置即可。”


## Pulumi 加强安全功能

在平台内部，Pulumi 的安全产品变得越来越重要，因为越来越多的企业数据和应用程序迁移到云端。Duffy 说，这项工具对大小公司都很重要。

“许多公司最重要的数据和最重要的资产现在都在云端，这意味着它们可能对互联网开放，”他说。“人们不再能够依赖数据中心的物理安全错觉。现在他们必须考虑基于软件的安全。”

这种情况已经持续了一段时间，但在 COVID-19 大流行期间加速了，当时各组织清空了办公室，业务变得高度分散和基于云。然而，即使在这些[左移时期](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), 在很多方面，安全仍然是事后考虑的问题，他说。

“人们开发和交付软件的方式，安全通常是事后考虑的问题，开发人员编写代码，基础设施团队将代码放入云中，然后安全团队追查所有发现的问题，无论是 CVE 和未修补的容器还是可访问互联网的虚拟机，还是云基础设施本身的错误配置，”Duffy 说。“如今许多工具和软件都倾向于假设混乱已经存在，并‘让我们去查找和修复问题’。”

然而，随着向左移的推动以及持续集成和持续交付所推动的加速步伐，企业希望他们的开发人员能够掌控全局并快速迭代，将代码交付到云端，几乎没有障碍和很少的摩擦。代码交付每天进行多次，而不是每季度一次。管理密钥是关键。

“错误的因素之一是密钥，以及确保您最敏感的信息（无论是数据库密码、令牌还是访问您的[帐户]的应用程序密钥）得到安全可靠的处理，”Duffy 说。“为了能够左移，您的开发人员需要一个解决方案，让他们知道所有这些东西都将始终安全。它需要内置其中。它不能是你事后添加的东西。”


## 获取对云基础设施的洞察

[Pulumi](https://www.pulumi.com) 在 2023 年初启动了 Insights，为组织提供对其多个云环境的可见性、智能和控制。与 ESC 一样，Insights 的目标是默认情况下实现安全等功能，但通过云资产和合规性管理服务实现。它不仅帮助开发人员和其他人员了解他们拥有的资源及其位置，而且还为他们提供合规性补救功能、搜索、资源可视化和基于 AI 的洞察。这是 Pulumi 之前工作的一大进步。

“这并非直接在我们擅长的领域内，但……由于我们的基础设施是良好的产品，我们了解所有这些云的全部情况，”他说。“我们说的是，‘如果我们有一种方法可以发现您拥有的所有资源，无论它们在哪里，并将它们引入我们已经拥有的数据模型（包括搜索和 AI 以及所有这些优秀的功能），那么我们将能够提供更好的可见性。’这与我们的策略代码引擎相结合，该引擎已经在为基础设施即代码工作负载执行合规性检查，我们找到了一种方法，可以利用我们所做的所有工作，并将其应用于您运行的任何基础设施。”


## 更好、更强大的 Insights

Insights 的第一个版本包括对 IaC 基础设施的搜索和仪表板，以及将其导出到 Snowflake 的功能。Pulumi 加强了 Insights 2.0，使组织能够将其功能应用于其所有云基础设施，无论其位置如何。它支持近 200 个云，并提供所有云资产的即时清单。Pulumi 内部有完整的透视表、可自定义的报表和仪表板、搜索和 Pulumi Copilot，用于发现云资源并交互式地提出问题。

此功能还利用 Pulumi 的 CrossGuard 策略即代码功能，该功能包括自动化补救措施的能力，因此 Insights 不仅可以提醒安全或合规性问题，还可以通过单击按钮帮助团队修复这些问题。

它探讨了利用人工智能解决问题的能力，以及对某种程度人工干预的渴望，这也是Pulumi一直在努力解决的问题。

“我们讨论了一段时间，因为我们很多人希望所有事情都在CI/CD管道中，并且围绕它有一个软件开发生命周期流程，我们总是遵循这个流程，”Duffy说。“你永远不会点击一个按钮来修复问题。但如果你坐在那里盯着一个安全漏洞，你可能想要一个按钮，上面写着‘去修复它’，即使你之后会有一些工作流程来确保它永久修复，并且其中涉及Jira工单等等。我认为这将成为我们的一个关键差异化因素。”

## Pulumi Kubernetes Operator 2.0

与此同时，本月早些时候，该公司发布了Pulumi Kubernetes Operator 2.0测试版，它使用户能够从Kubernetes环境中部署和管理云基础设施。通过2.0版本的发布，Pulumi解决了影响早期用户的可扩展性和隔离性限制。

Pulumi Kubernetes Operator定义了一个名为`pulumi.com/v1/Stack`的Kubernetes自定义资源，它代表一个Pulumi [stack](https://www.pulumi.com/docs/concepts/stack/)，Pulumi的软件工程师Eron Wright在一篇[博客文章](https://www.pulumi.com/blog/pulumi-kubernetes-operator-2-0/)中写道。Pulumi stack可以使用任何受支持的Pulumi语言（TypeScript、Python、Go、.NET、Java、YAML）编写，并可以在任何受支持的云（AWS、Azure、GCP、Kubernetes和60多个其他云和SaaS提供商）中部署和管理云基础设施。Wright说，Pulumi Kubernetes Operator根据`Stack`自定义资源或其使用的资源的变化触发云部署。

因此，Pulumi Kubernetes Operator使用户能够通过使用直接在其Kubernetes集群中管理的资源来指定其云基础设施的期望状态。该公司表示，修改这些Kubernetes资源将触发对其管理的基础云基础设施的创建、更新和删除。

## PulumiUP Europe

Pulumi将在即将于11月20日虚拟举行的PulumiUP Europe大会上展示这款产品和其他关键产品。

除了产品信息外，Pulumi还将赞助关于平台工程、DevOps和安全等主题的会议。

例如，根据Gartner的预测，到2026年，80%的开发公司预计将拥有内部平台服务和团队来提高开发效率。随着平台工程继续重塑组织管理基础设施的方式，集成DevOps和安全对于构建可扩展、安全的平台至关重要。这包括在将DevSecOps集成到规模化平台时面临的挑战和机遇，以确保开发人员的自主性，同时保持治理和合规性。

## IaC的不足

[StackGen](https://stackgen.com/)，一家生成式[Infrastructure from Code (IfC)](https://blog.stackgen.com/what-is-infrastructure-from-code)公司，于10月30日发布了关于IaC采用面临重大挑战的研究。他们对315名参与者的调查中的主要发现包括：97%的IaC用户报告遇到困难，只有13%的组织实现了IaC成熟度。此外，56%的开发人员表示他们花费超过20%的时间在基础设施管理上。

此外，一些主要挑战包括安全性和可靠性问题（56%的人难以保持一致的配置）。然而，根据StackGen的说法，IfC正在成为一种潜在的解决方案，尽管目前只有22%的人熟悉它。

StackGen将其IfC解决方案定位为通过根据应用程序源代码自动生成基础设施配置来解决这些挑战，并具有内置的安全性和合规性标准。
