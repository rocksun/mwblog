<!--
title: AI辅助更新依赖项保证正常运作
cover: https://cdn.thenewstack.io/media/2024/01/240511f4-infieldlogo-1024x410.png
-->

初创公司Infield通过持续监控和汇总的升级数据，为开源组件的安全管理提供逐步指导

> 译自 [AI-Assisted Dependency Updates without Breaking Things](https://thenewstack.io/ai-assisted-dependency-updates-without-breaking-things/)，作者 Susan Hall 是 The New Stack 的赞助商编辑。她的工作是帮助赞助商为他们提供的内容获得尽可能广泛的读者群。她自The New Stack创立之初就为该网站撰稿，也为其他网站撰稿......

大家都想要保持软件的更新，但担心改变一件事会打破另一件事，所以那些项目就会堆积起来。然后就是压倒性的 backlog，情况只会越来越糟。

这是纽约初创公司 [Infield](https://www.infield.ai/) 正在利用 AI 和数据来解决的问题。

“我们希望帮助软件工程团队保持所有开源依赖的更新，我们正在通过为他们提供所需的所有信息来避免在升级时破坏生产环境来做到这一点，因为开发人员让所有这些升级悬而未决的头号原因是他们担心会出问题......我会通过做这个升级来破坏生产环境......但如果我就这样放着不管，它不会坏掉，”联合创始人兼首席执行官 [Steve Pike](https://www.linkedin.com/in/stephen-pike-53992419/) 说。

Infield 的解决方案涉及对[开源组件](https://thenewstack.io/organizations-only-somewhat-confident-in-open-source-components/)的建议更新进行持续监控，以及提供逐步指南来达到理想状态的工具，这可能涉及以特定顺序更新各种子组件以避免问题。

## 复杂的网络互联

根据应用程序安全供应商 [Synopsys](https://www.synopsys.com/software-integrity.html？utm_content=inline-mention) 的数据，平均软件应用程序包含 [500 多个开源组件](https://www.synopsys.com/software-integrity/resources/analyst-reports/open-source-security-risk-analysis.html)。虽然大公司可能有专门的团队来保持组件更新，但大多数公司没有，维护软件需要工程师从核心产品和新功能的工作中抽身出来。

Infield 最近宣布的 300 万美元种子轮投资方 Foundation Capital [这样说](https://foundationcapital.com/investing-in-infield/):

“[现在任何软件解决方案中开源软件占据了70-90%](https://www.linuxfoundation.org/blog/blog/a-summary-of-census-ii-open-source-software-application-libraries-the-world-depends-on)，每个组件都需要定期更新以提高安全性、性能和可靠性。然而，[85%的代码库中包含的组件比实际版本落后4年以上](https://news.synopsys.com/2021-04-13-Synopsys-Study-Shows-Uptick-in-Vulnerable-Outdated-and-Abandoned-Open-Source-Components-in-Commercial-Software)。此外，许多依赖项依赖于额外的包，形成传递或链式依赖。[如果不仔细管理](https://thenewstack.io/effective-strategies-for-open-source-supply-chain-management/)，更新一个依赖项有时会打破整个链。这个复杂的互联网络的技术术语是'依赖地狱'。”

Infield 将其视为一个数据问题。

“我们知道这些升级以前已经做过，但当人们去做的时候，他们实际上是第一次做。” Steve Pike 说，并补充说，公司在隔离中都在重造轮子。

“他们是个小宇宙，然后他们就再也不去考虑它了。所以我们正在收集所有关于开源依赖项及其升级的非结构化信息。”

这可能是一个变更日志，维护者关于代码本身变更的笔记，或者 GitHub 或互联网其他地方的其他社区生成的内容，以及来自 Infield 用户经验的数据。他们经常回滚吗？安全进行此升级是否需要对代码进行更改？Infield 还维护自己的未记录不兼容性数据库。

“因此，所有关于这些升级的数据，我们都在存储、结构化，然后在您开始升级时主动向您提供。” Steve Pike 说。

Tech 行业发展迅速，别错过任何一个精彩节目。订阅我们的 YouTube 频道，观看我们的所有播客、访谈、演示等内容。
立即订阅

## 采取数据中心视角

联合创始人 Steve 和 [Allison Pike](https://www.linkedin.com/in/swihartpike/) 在 SevenFifty 相遇，这是一家通过整合来自 1000 多家酒精饮料批发商的数据，为餐厅制作产品和价格数据集的科技创业公司。Steve 撰写了最初的代码并成为 CTO，而 Allison 担任 COO，销售数据产品并与数据工程师合作。从那以后，他们创建了 Syndetic，将其描述为“数据集的 Shopify”，并通过 Y Combinator。但新冠疫情影响导致封锁。

正如 Allison Pike 所说，“我们从未能享受大多数 YC 公司可以享受的演示日。我们被困在山景城。”

但这对夫妻团队筹集了足够的资金来维持 Syndetic 的运营，而 Steve 开始接受咨询工作，主要为技术债务公司保持软件更新。从这种经历中产生了以数据为中心来维护开源依赖的观点。

他们的第三位联合创始人 [Andrew Lenehan](https://www.linkedin.com/in/adlenehan/) 之前是 AppNexus(现在属于微软)的产品经理，并共同创立了 Roster，后来成为 Punchcard，这是一种用于营收团队的数据探索工具。

Allison Pike 说，使用数据来改进升级管理只能说得通。

“这是AI的一个有趣应用，因为最近关于AI的很多文章，或者可以说是自ChatGPT推出以来，一直在讨论将AI应用于代码本身。变更日志真的很有趣，因为它是一个由人类编写的文档，也就是维护开源项目的维护者，但它是代码。所以它在GitHub仓库中，但它是一个由人编写的文本文档。所以你可以更详细地了解。”

所有这些信息都进入了一个大型语言模型(LLM)，用于定义从A点到B点的更新策略的最佳策略，该公司称之为升级路径。根据该公司的说法，这可以为像保持Ruby on Rails的所有内容都是最新版本这样的大型项目节省几个月的时间。

首先，您将Infield Web应用连接到GitHub中的代码库，它会扫描您的代码以确定底层依赖项，然后该技术会推荐您的代码库安全升级所需的步骤。这可能涉及将子组件更新到中间版本，而不是最新版本，以避免下游中断。

“一旦你积累了100个待升级的候选项，你可以使用我们的数据来优先考虑它们，”Steve Pike说。“所以我们向你展示有关风险的信息——如果不升级此依赖项，你会面临什么风险？——以及工作量。进行升级会涉及多少工作？是否有重大更改或您项目中的其他包需要先升级，这些包正在阻止此升级？”

"因此，您可以运行过滤器将这两者相互对比，找到例如，我可以清除一打过时的依赖项而不触发任何破坏性更改。因此，只要我的测试通过，我可能可以在一个拉取请求中完成这些操作。但是还有其他高风险的事项，实际上存在重大的破坏性更改。因此，这需要更多的是一个项目。”

Allison Pike认为，像[Snyk](https://thenewstack.io/snyk-seeks-to-sharpen-distinction-between-low-priority-and-urgent-security-alerts/)这样的现有解决方案往往专注于发现安全漏洞，或者像[Dependabot](https://www.infield.ai/post/the-limitations-of-dependabot)一样，给用户留下一个任务列表，但缺乏为其特定系统定制的上下文信息。几年前，我曾写过一家欧洲公司[Depfu](https://thenewstack.io/automated-dependency-management-with-depfu/)，它利用自动化每次仅发送不超过七项任务，以避免用户感到不知所措。

[全自动的依赖管理](https://www.cosotateam.com/post/automating-dependency-updates-the-big-debate)也有其批评者，包括顾问[Gerald Benischke](https://www.linkedin.com/in/gerald-benischke-9811b663/?originalSubdomain=uk)在这篇博文中[反对它](https://beny23.github.io/posts/automatic_dependency_updates/)。Infield采用更加人为辅助的方法。

虽然Infield可以自动检测破坏性更改，依赖于每种语言或框架的检查器和包管理器，但它不自动执行实际的更新。如果需要代码更改，用户可以自行操作，或者依赖于Infield的托管服务来完成。最初面向Ruby on Rails，它最近增加了对JavaScript/TypeScript和Python的支持。TypeScript和JavaScript共享相同的包管理器。
