# 如何使用ETL解决Backstage插件隔离问题

![Featued image for: 如何使用ETL解决Backstage插件隔离问题](https://cdn.thenewstack.io/media/2024/12/451c988b-plugin-isolation-1024x576.jpg)

Backstage是一个流行的构建[内部开发者门户](https://www.getport.io/blog/what-is-an-internal-developer-portal)的框架。开发者经常将其视为充满机遇的领域，因为他们能够自定义正在构建的门户并使其适应其组织的需求。工程师喜欢构建他们拥有的东西，而Backstage承诺拥有软件开发生命周期（SDLC）。

但是[Backstage是一个巨大的项目](https://thenewstack.io/spotifys-backstage-roadmap-aims-to-speed-up-adoption/)，需要在工程组织内部启动，因此[存在一些复杂性](https://www.reddit.com/r/devops/comments/10guddj/backstageio_common_issues_and_pitfalls/)——特别是其插件架构——可能需要一些时间（也许六个月甚至一年）才能显现出来。社区提供的现成插件只能帮助你做到一定程度，这意味着你会发现自己比想象中更快、更频繁地实现自定义插件。

问题是，此时，工程团队将已经投入大量时间来构建他们想要的东西。这时就会清楚地发现，虽然该框架确实可定制，但这种插件的复杂性会带来限制。某些用例将无法完全受益，例如事件管理和标准合规性。

这使得工程师面临一个很大的难题：他们是否应该尝试解决这个插件数据问题，因为他们已经花费了大量时间[构建这个门户](https://thenewstack.io/what-devs-really-want-in-an-internal-developer-portal)？或者他们是否应该尝试寻找另一个没有相同问题的解决方案，放弃他们在构建门户上花费的时间和投资？

这两个选项都不理想。在我们介绍一些替代解决方案之前，让我们先了解问题的核心。

## Backstage的插件问题是什么？

Backstage插件架构的设计使得每个插件都是独立的。这样做的好处是它将门户的不同部分分开，因此您可以[内部开源](https://thenewstack.io/how-to-implement-innersource-with-an-internal-developer-portal)构建门户，支持大量的插件构建者并划分这些构建者的职责。

但是，这种分离是由技术驱动的，而不是由明确定义的用例驱动的，这是不好的做法。门户的真正价值在于其有效服务特定用例的能力。如果门户难以针对这些用例进行工程设计和设置，则其潜力将无法充分发挥。这种方法也违背了[平台即产品](https://www.getport.io/glossary/platform-as-a-product)的理念，而这种理念是[平台工程](https://www.getport.io/glossary/platform-engineering)成功的核心，其中用户被视为客户，因此他们的体验得到了优先考虑和增强。

插件架构也类似于将单体架构拆分成不同的[微服务](https://thenewstack.io/microservices/)。

但是，正如微服务由于扩展而可能难以管理一样，[Backstage插件](https://www.getport.io/blog/top-5-backstage-plugins)也可能难以管理。由于对插件的版本控制和质量了解有限，随着团队中大量工程师积极被鼓励构建新插件，这个问题会变得更加严重。

这可能导致：

- 代码重复，多个插件执行相同操作，这会浪费资源。
- 故障插件导致整个Backstage门户停机。
- 缺乏集中且灵活的软件目录，导致缺乏上下文和可见性，并减慢整个软件开发生命周期。

## 为什么统一的数据模型很重要？

![插件没有集成，因此缺乏开发者所需的上下文。](https://cdn.thenewstack.io/media/2024/12/05177008-backstages-lack-of-central-data-model-inner-image-1024x597.png)

插件没有集成，因此缺乏开发者所需的上下文。

Backstage的社区插件，例如Argo CD和Snyk插件，为用户提供了他们正在寻找的核心信息。Argo CD插件提供了每个服务的部署列表以及生产中的最新版本。同时，Snyk插件提供了每个服务的漏洞列表。

但是，如果您想查看与服务的已部署版本相关的漏洞列表，则需要构建一个新的自定义插件。此插件应查询Argo CD以识别当前生产中的版本，然后将其与该版本的Snyk漏洞数据交叉引用。
这是因为社区插件之间无法互相通信，这意味着开发人员无法获得诸如“我的生产环境中是否存在Snyk漏洞？”之类问题的答案，或者在[Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention) (GCP)插件的情况下，“哪些GCP服务最近的CI部署失败了？”，而无需手动连接这些信息点。

如果没有集成插件，就无法构建一个全面的[事件管理](https://www.getport.io/blog/how-internal-developer-portals-improve-incident-management)视图，该视图整合了来自包括值班工具、最近构建、最后一次CD部署、回滚和GitHub所有权数据等方面的信息。云成本优化和基础设施管理也是如此。

要通过上下文提取实际价值，需要工程师开发定制插件。这需要前端工程师（熟悉[React框架](https://roadmap.sh/react)）和后端或DevOps工程师的时间。随着时间的推移，这些资源成本会累积，版本控制和质量的维护也是如此，在Backstage框架中没有明确的方法来跟踪这些方面。

在处理服务级别目标 (SLO)、标准检查和[记分卡](https://www.getport.io/guide/scorecards)时，问题变得更加明显。在碎片化数据上建立规则本身就很难。以生产就绪为例，您可能希望创建一个检查，以确保所有存储库都使用来自GitHub的信息具有README。然后，您可能希望创建一个第二个检查，以通过从SonarQube之类的工具提取数据来验证测试覆盖率是否达到或超过80%，作为代码质量检查的一部分。在Backstage中实现此目标需要将信息集成到软件目录中，并构建自定义插件来检查和显示每条规则的状态。

Backstage的插件模型具有优点，尤其是在其能够清晰地分离独立插件之间责任的能力方面。但是，这种方法有效地隔离了数据，使开发人员难以实现他们所需的无缝集成。如果不采用或偏好共享数据模型，则该[平台功能不足](https://thenewstack.io/portal-vs-platform-why-you-need-to-think-about-both/)，无法使开发人员有效地访问和利用互连的见解来完成他们的工作流程。


## 开发人员查看插件的理想方式是什么？
开发人员的一个主要挫折是他们必须不断地在不同的工具之间切换上下文。大多数Backstage构建者只是将这个问题从浏览器转移到Backstage，使用Jira、Argo CD和GitHub Actions之类的选项卡。这对开发人员没有实际价值，这意味着他们将继续对必须进行的上下文切换量感到沮丧。

例如，如果开发人员试图在一个由不同的工程团队构建的服务中集成新的API，他们应该能够在一个单一的事实来源中轻松查找和理解信息。

门户构建者应该为每个角色（例如，开发人员、领导者、DevOps、安全人员）创建一个清晰的个性化视图，在一个地方提供开发人员所需的所有必要信息和上下文。这种个性化可能包括根据角色呈现不同级别的抽象。例如，对于Argo CD数据，技术产品经理可能需要一个高级视图，显示正在运行的版本和最新的提交，而站点可靠性工程师 (SRE) 或后端工程师可能需要更详细的系统健康概述。

清晰地查看所有内容可以最大限度地减少干扰，并使开发人员能够在——一分钟内——快速找到他们需要的内容并返回工作。[GitHub的研究](https://github.blog/news-insights/research/good-devex-increases-productivity/)表明，良好的开发人员体验通过促进专注和减少中断来显著提高生产力。门户应该支持他们的流程状态，因为它可以加快开发人员的速度并让他们保持在自己的区域内。速度的提高会导致组织投资回报率的提高。

请看下面的例子。门户不应该在概述中包含基本信息，并且必须查看每个独立插件的选项卡，而应该在一个地方提供所有信息的全面概述。

![Switching from separate tabs for specific plugins to one view with all of the information about all plugins in one place.](https://cdn.thenewstack.io/media/2024/12/391398cf-before-and-after.gif)
从为特定插件的单独选项卡切换到一个包含所有插件的所有信息的视图。
插件也不公开用于检索数据的API端点。这会导致限制，因为您无法从CI/CD管道与数据交互或将其与AI代理集成，从而降低代理的整体有效性。

## 如何修复您的插件架构
让我们从门户网站后退一步，从数据工程的角度考虑插件架构。提取、转换、加载 (ETL) 方法被广泛认为是将来自多个来源的数据整合到统一存储库中的最佳实践。[研究](https://link.springer.com/article/10.1007/s11227-024-06413-1?) 强调了ETL在数据集成中的重要性，支持决策和战略规划。

在本例中，ETL 指的是：

**提取：**从所有不同的开发工具和数据源中提取信息。**转换：**将所有提取的信息转换为一个逻辑数据模型。**加载：**将逻辑数据模型加载到Backstage中，使插件能够确定如何根据不同的角色定制数据呈现方式。

当今的工程组织的数据来自各种来源，包括：

- 源代码管理工具，例如GitHub，[GitLab](https://about.gitlab.com/?utm_content=inline+mention), Azure DevOps等等。
- 云提供商，例如[AWS](https://aws.amazon.com/?utm_content=inline+mention), GCP, Azure。
- CI/CD工具，例如CircleCI、Argo CD、GitHub Actions。
- 云成本、监控和分页工具等等。

通过应用ETL，可以将单个原始数据集转换为组织可以使用和从中学习的格式和结构。有两种方法可以实现这一点。

### 选项 A：利用数据仓库和数据工程
为了克服Backstage的插件数据问题，一种方法是将来自不同来源的数据集中到统一的存储库中。数据仓库作为这种方法的支柱，可以通过Airbyte或Fivetran等ETL工具实现与Jira、Argo CD和GitHub Actions等工具的无缝集成。

此设置通过将信息整合到单个可扩展的存储层中来消除数据孤岛，以便进行转换和使用。

使用像[dbt](https://www.getdbt.com/)这样的数据转换工具可以将来自数据湖的原始数据转换为逻辑的、统一的模型，确保所有数据点的一致性。

![将数据仓库和ETL工具结合起来可以将数据集中到一个存储库中。](https://cdn.thenewstack.io/media/2024/12/45932a29-etl-approach-inner-image-1024x597.png)

将数据仓库和ETL工具结合起来可以将数据集中到一个存储库中。

这个共享模型允许自定义Backstage插件访问和显示集中的见解。开发人员受益于简洁、可操作的视图，这些视图结合了多个数据流，例如部署状态、CI/CD日志和所有权详细信息，而不是导航孤立的选项卡。这种集成将Backstage转变为功能性开发者门户，并提高了生产力和可用性。

为了支持聚合和更复杂的功能，您可以使用所选数据仓库技术的计算字段。

这种方法在建立[记分卡](https://www.getport.io/blog/using-scorecards-for-standards-compliance-a-repeatable-framework-and-examples)和跟踪计划方面存在局限性，因为直接在数据仓库中创建规则并不简单。此外，缺乏可以将数据仓库的输入无缝集成到操作中的自助服务操作是另一个缺点。选项B在解决这两个问题方面可能是一个更好的选择。

但是，选项A仍然为开发人员提供了有意义的价值。通过解决碎片化问题并增强数据协作，Backstage可以成为一个更集成的平台。

### 选项 B：使用专门的开发者数据仓库插件
![Port的Backstage插件统一数据并支持无代码/低代码数据建模](https://cdn.thenewstack.io/media/2024/12/76951da3-ports-backstage-plugin-inner-image-1024x597.png)

Port的Backstage插件统一数据并支持无代码/低代码数据建模。

Port有一个新的[Backstage插件](https://backstage-plugin.getport.io/)，它是为开发者数据构建的，并针对平台工程师的需求量身定制。它结合了专门的开发者数据仓库和无代码/低代码数据建模功能的特性，以整合和集中您的数据。它还可以作为基础，帮助克服与Backstage的独立插件问题相关的其他挑战，例如：

- 与多个工具集成，包括Jira、GitHub Actions和Argo CD。
- 依赖于dbt和SQL等复杂工具来构建数据。
- 难以定义和跟踪对标准的合规性。

## 建议
构建开发者门户很难，但构建一个开发者喜欢的门户则更难。为门户用户提供更多自主权、更好的可见性和更多上下文信息，这可能是门户被广泛采用与未能获得关注、开发者不得不勉强使用或完全避免使用之间的区别。

了解更多关于 Backstage 的 Port 插件信息：[加入 Beta](https://backstage-plugin.getport.io/)，探索[Backstage 替代方案](https://www.getport.io/blog/top-backstage-alternatives) 或[比较 Backstage 和 Port](https://www.getport.io/compare/backstage-vs-port)。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。