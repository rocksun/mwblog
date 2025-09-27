微软推出了由[AI 代理](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/)驱动的新开发工具，旨在显著减少迁移遗留企业应用所需的时间和复杂性。

微软Azure产品管理副总裁 Scott Hunter 告诉 The New Stack，该公司最新推出的产品有助于将更新 [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) 和 [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) 应用长达数月的过程缩短到几天。

## 企业遗留问题

Hunter 表示，[企业IT部门](https://thenewstack.io/agentic-ai-is-the-next-frontier-in-enterprise-operations/)正面临着老旧应用组合带来的日益严峻的挑战。目前，超过37%的企业应用需要现代化。微软本周在[迁移与现代化峰会](https://www.microsoft.com/en-us/events/launch-events/migrate-and-modernize-summit)上宣布了这些功能。

“大多数企业客户都收购过公司，这意味着他们也收购了技术，”负责这项迁移计划的 Hunter 解释道。“他们会拥有一系列.NET和Java应用程序——可能是旧的.NET框架；也可能是一些旧的[Java 8](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/)版本。当我与我的现场和销售团队交流时，平均而言，将其中一个项目迁移到Azure大约需要八个月。”

Hunter 表示，通过推迟关键更新，组织可能会积累安全漏洞和技术债务，同时错过利用现代云功能的机会。

面向开发者的安全平台 Arcjet 公司的首席执行官 David Mytton 告诉 The New Stack，迁移和依赖更新很重要，尤其是在安全更新方面，但它们通常不会为客户带来价值，并且对开发者来说是一个痛苦的过程。

他说：“使用AI加速.NET和Java等语言的迁移非常有意义，因为这些语言的代码要么能编译通过，要么不能，测试要么通过，要么失败。如果存在细微的破坏性变更，比如UI库或边缘用户流程中的变更，这会变得更加困难。基础设施和数据库升级甚至更难。你真的愿意让代理来管理生产环境中的主要数据库版本更新吗？”

## 迁移的代理工作流

他说，微软的方法始于 [Azure Migrate](https://azure.microsoft.com/en-us/products/azure-migrate)，它提供对企业应用组合的全面发现和评估。该工具会自动清点组织基础设施中的应用程序、依赖项、操作系统和框架版本。

Hunter 说：“我们真的想减少客户必须面对的‘前门’数量。我不想走过来对你说，‘嘿，我有20个不同的小工具。你可以把它们都运行起来，一起迁移你的应用程序并让它在Azure中运行。’我真的希望从一个单一的‘前门’开始。”

Hunter 表示，统一平台消除了IT团队协调多个独立工具的需要。Azure Migrate 可以自动生成 GitHub issue，其中包含所选迁移应用程序的完整技术上下文，包括操作系统详细信息、运行时版本和数据库依赖项。

## 开发者中心工作流

迁移过程直接集成了 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 的AI代理和流行的开发环境。开发者会收到结构化提示，他们可以在Visual Studio Code或Visual Studio中使用这些提示来启动代理工作流，从而自动处理大部分技术复杂性。

Hunter 强调说：“这里最重要的是，我们不会擅自替你完成工作。我们构建完整的计划，让你编辑计划，当你准备好时，你告诉它开始迁移。”

AI代理在进行任何代码更改之前会生成详细的迁移计划。开发者可以审查这些计划，修改建议，并根据其应用程序的需求添加或删除特定更新。这确保了开发者在受益于常规任务的自主执行的同时，仍能保持监督。

## 可衡量的省时效果

早期实施显示出显著的生产力提升。Hunter 表示，微软的Xbox团队最近使用这些工具将多个项目迁移到更新的.NET版本，将迁移工作量减少了88%。他还提到，[福特中国](https://finance.yahoo.com/news/ford-establishes-subsidiary-china-090612787.html)在中间件应用现代化过程中，时间投入和工作量减少了70%。

“这一切都是为了优化公司进行这些转型所需的时间，” Hunter 指出。“在许多情况下，公司甚至不会进行这些转型，因为他们害怕这样做。”

AI代理处理复杂场景，包括依赖更新、安全补丁和框架特定的兼容性问题。当代理遇到无法自动解决的问题时，它们会提供详细的分析和具体的手动干预建议。

## 不仅仅是版本更新

该平台通过微软的 [Azure Migrate 应用程序和代码评估工具 (AppCAT)](https://learn.microsoft.com/en-us/azure/migrate/appcat/overview?view=migrate-classic) 扩展了简单的框架升级功能，该工具分析应用程序以寻找云优化机会。AppCAT 是微软用于评估应用程序代码（特别是迁移和现代化到 Azure）的主要工具，它分析 .NET 和 Java 应用程序，以识别将应用程序迁移到云端时可能出现的问题和机会。该工具可识别具体的改进，例如用内容分发网络取代本地文件存储，或更新身份验证方法以提高安全性。

Hunter 解释说：“我们有一个工具可以识别这些问题。例如，如果你正在运行一个.NET应用程序，并且它有一个SQL Server连接字符串，那么当你将其迁移到Azure时，最好不要使用连接字符串，因为那是一个安全风险。”

他说，组织可以通过预构建的[代理工作流](https://thenewstack.io/what-agentic-workflows-mean-to-microservices-developers/)实施这些建议，或根据自己的代码更改创建自定义模式，从而在整个应用程序组合中实现一致的更新。

## 多平台开发支持

Hunter 表示，微软正在将其工具的兼容性扩展到其自身的开发生态系统之外。GitHub Copilot 现在可以在 [JetBrains IDEs](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/)、[Eclipse](https://thenewstack.io/eclipse-theia-the-deepseek-of-ai-tooling/) 和 [Xcode](https://thenewstack.io/start-your-apple-coding-journey-with-xcode/) 中工作，允许开发者使用他们偏好的开发环境。

他表示：“我们希望在开发者所在的地方满足他们的需求。我不想说你必须使用我的某个IDE来完成这类工作。”

微软还扩大了数据库支持范围，最近在现有针对 SQL Server、[Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 和 Sybase 工作负载的功能基础上，新增了 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) 迁移评估。

## 集成运维支持

迁移工具与 [微软的站点可靠性工程（SRE）AI 代理](https://learn.microsoft.com/en-us/azure/sre-agent/overview?tabs=explore) 连接，用于持续的应用程序监控和维护。在迁移和部署后，该平台提供详细的性能分析以及用于扩展和优化的主动建议。

Hunter 描述传统方法时指出：“以前，我只会收到一个寻呼机通知，说出了问题。现在我能得到详细的分析。我甚至可能会得到内存转储。它甚至能告诉我代码问题可能在哪里，并且在我处理问题时，它还提供机会让我实际扩展应用程序。”

## 减少开发开销

这项举措减少了 Hunter 所称的“开发者苦工”——那些阻碍开发团队专注于新功能开发和创新的日常维护任务。

Hunter 解释道：“这一切都关乎开发者苦工。我们如何减少这种开发者苦工？作为一名软件工程师，我不想去做那些事。我想编写新代码。我想构建新应用。”

AI代理处理耗时的活动，如依赖管理、安全更新和兼容性修复，这些任务以前需要资深开发者投入大量手动工作。

## 行业影响

随着Java和.NET应用程序的全面推出，微软正在解决企业软件开发中的一个根本性限制。该平台标志着从手动、资源密集型迁移过程向AI驱动的代理工作流的转变，后者能够高效处理复杂的企业场景。

企业战略集团分析师 Torsten Volk 表示，微软所做的一切都需要根据其比 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 和 [GCP](https://cloud.google.com/?utm_content=inline+mention) 更快地引入云工作负载的目标来评估。

他告诉 The New Stack：“这就是为什么他们拥抱 Linux，收购 GitHub，并大力投资 OpenAI 的原因。现在这些投资很好地结合在一起，GitHub 和 Copilot 精心打包工作负载，以便轻松在 Azure 上线。微软也不关心公司使用什么数据库；他们准备提供任何能让他们更容易上线的工具。推广他们自己的软件远不如让公司上线并让他们沉迷于从应用程序堆栈底部到顶部的许多创收服务重要。当然，AWS 和 GCP 也遵循同样的策略，但微软在企业内部拥有更强大的立足点，因为他们就是从那里起步的。”

与此同时，Constellation Research 的分析师 Holger Mueller 表示，当技术债务负担过高时，“好消息是 AI 可以帮助理解旧代码，并越来越多地帮助翻新，甚至创新旧代码。”

企业不应只是简单地“提升和迁移”（lift and shift）其自动化，而应利用AI和更现代、先进的数据库等创新。

Mueller 说：“这就是微软通过其迁移和加速产品所追求的目标。像往常一样，最终还是由 CxO 们来决定这些产品的价值——以及他们是否希望迁移到 Azure，所有这些迁移工具都指向 Azure。”

Hunter 表示，现在组织可以将应用程序现代化视为一个可管理、可预测的过程，而不是一个需要专门团队和延长工期的重大项目。