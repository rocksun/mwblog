<!--
title: 年度总结：平台工程依然依赖电子表格
cover: https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png
-->

您需要内部开发者平台(IDP)还是开发者门户网站？这取决于您与谁交谈，以及您在平台工程进程中已经走了多远。

> 译自 [Year-in-Review: Platform Engineering Still Run By Spreadsheet](https://thenewstack.io/year-in-review-platform-engineering-still-run-by-spreadsheet/)，作者 Joab Jackson 是The New Stack的高级编辑，负责报道云原生计算和系统运维。他报道IT基础架构和开发超过25年，包括在IDG和Government Computer News任职。在此之前，他是一名自由作家，为《连线》、《MIT技术评论》等刊物撰稿。

我们带着平台工程可以缓解现代开发者面临的复杂性的认识进入2023年，但我们在年底意识到，我们仍需正确设置工具链以支持这种实践。

这是本月早些时候[平台工程门户提供商](https://thenewstack.io/port-platform-engineering-can-be-the-first-step-in-system-automation/)Port发布的[2024年内部开发者门户状况报告](https://www.getport.io/state-of-internal-developer-portals)的重要结论。

![](https://cdn.thenewstack.io/media/15e1300e-port.svg)

该报告源自对100名全职IT专业人员的调查，他们在拥有150名或更多员工的公司工作，包括平台工程师、开发者体验专业人员、平台产品经理和[站点可靠性工程师](https://thenewstack.io/kubecon-lessons-in-disaster-recovery-from-covid-19-and-site-reliability-engineering/)。

调查发现，对新兴的[平台工程](https://thenewstack.io/platform-engineering/)实践有广泛的支持，但受访者在认为将平台工程的优势带给开发者所需的工具方面存在分歧。

一些人需要一个完整的[内部开发者平台](https://humanitec.com/blog/what-is-an-internal-developer-platform)(IDP)，无论是开源的还是商业的。一些人只需要一个门户，为[开发者提供](https://thenewstack.io/self-service-infrastructure-as-code-in-a-dev-portal-with-gitops/)对他们已经可以访问的所有资源的访问。

而在至少35例受访者中，开发者必须查阅电子表格来了解如何访问所需服务。

Port责备使用Excel作为某种原始服务目录的做法。

“使用电子表格不应视为真正的[内部开发者门户](https://thenewstack.io/3-ways-an-internal-developer-portal-boosts-developer-productivity/)，因为它的高度手动性质和缺乏开发者自助服务功能，”报告指出。

调查发现，较小的公司倾向于内部构建目录，而较大的组织正在踢踢商业IDP或门户的轮子。

实际上，研究表明，一个组织的开发者人数越多，它需要一个开发者门户的可能性就越大，TNS分析师[劳伦斯·赫希特](https://thenewstack.io/author/lawrence-hecht/)(Lawrence Hecht)指出。他认为，根据环境和使用的微服务的复杂性，在拥有50名或更多开发者的公司，门户开始成为一个有价值的命题。

## IDP如何驯服云原生复杂性

门户和IDP都是平台工程的物理体现。

![](https://cdn.thenewstack.io/media/2023/12/3122ebe5-red_hat-josh_wood-300x200.jpg)

*Red Hat开发倡导者乔舒亚·伍德(Joshua Wood)。*

就像Kubernetes[简化了分布式系统的工作负载管理](https://thenewstack.io/managed-kubernetes-services-make-k8s-simple-for-platform-teams-and-app-developers/)一样，IDP承诺简化开发者从这个云原生环境中获取所需资源的方式。

“开发者门户的想法现在有一种流通性，”[红帽](https://www.openshift.com/try?utm_content=inline-mention)开发者倡导者[乔舒亚·伍德](https://www.linkedin.com/in/joshix/)(Joshua Wood)上个月在波士顿的[红帽峰会](https://thenewstack.io/red-hat-ansible-gets-event-triggered-automation-ai-assist-on-playbooks/)上在一次技术演示中说。

“我们正在努力使开发者体验更像我们为了获得部署弹性和这些容器编排集群中的大量自动化而做出的权衡复杂性之前，”他解释道。

伍德规定，再次讨论门户(十年前行业小风潮后的短暂时期)是很奇怪的。但鉴于当今新开发者可能进入的复杂环境，它们很快可能变得必不可少。如果不花费无限的时间先针对其环境然后针对最终的生产设置来配置它，他们如何使用Kubernetes等工具？

对许多人来说，设置IDP意味着基于Spotify的Backstage进行构建。

Spotify开发[Backstage](https://backstage.io/)，最初是内部开发，以响应开发者[对某种服务目录的需求](https://thenewstack.io/spotifys-backstage-a-strategic-guide/)。当该公司在2020年开源此软件时，它将该软件包标记为构建开发者门户的开放平台。

工程师这样[描述它](https://engineering.atspotify.com/2020/03/what-the-heck-is-backstage-anyway/)：“Backstage使用单一、一致的UI统一您的所有基础设施工具、服务和文档。所有的！想象一下，如果您的所有工具(GCP、Bigtable、CI管道、TensorFlow Extended和堆栈中隐藏的任何其他内容)都具有相同的、易于使用的界面会怎么样。”

[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)在2022年3月接受Backstage作为一个[完整的孵化项目](https://www.cncf.io/blog/2022/03/15/backstage-project-joins-the-cncf-incubator/)。

Red Hat自己进入这个领域的是[Red Hat Enterprise Hub](https://thenewstack.io/red-hat-readies-developer-hub-a-backstage-enterprise-distribution/)，它在5月作为测试版发布。准备就绪时，它将是一个企业范围的Backstage版本，一个预填充了建议的应用程序链接。

Hub在OpenShift上运行，主要通过Kubernetes API。但Backstage本身不特别针对OpenShift甚至Kubernetes。它也可以[在容器或裸机上运行](https://thenewstack.io/tutorial-install-flatcar-container-linux-on-remote-bare-metal-servers/)。

尽管最终用户将是开发者，但IDP的管理落到平台工程师身上，后者使用它来确保所有最佳实践、常规配置和策略编码都烘焙到IDP中，尽可能减轻开发者填写YAML文件的负担。

伍德说，IDP是一个“您的开发者用来组装代码”的平台。

Backstage基于插件运行，可用于管理应用程序和服务(以及提供仪表板小部件、CI/CD集成、文档生成器等)。应用程序和服务可以打包成目录。模板为服务和应用程序提供公司特定的设置说明。

## 但是，等等，我需要门户还是平台(或两者)？

渴望进一步了解平台工程空间的新手可能会被术语绊倒，许多人想知道IDP中的“P”代表“平台”还是“门户”，这种困惑肯定是由机会主义厂商和信息不足的贸易刊物所鼓励的。

“P”代表平台，尽管您仍然需要某种门户作为界面。

提供企业级IDP及其[Platform Orchestrator](https://humanitec.com/products/platform-orchestrator)的[Humanitec](https://humanitec.com/?utm_content=inline-mention)将IDP[定义](https://www.cncf.io/blog/2023/12/08/internal-developer-platform-vs-internal-developer-portal-vs-paas/)为“由专门的平台工程团队构建和交付的企业平台层，以消除复杂性(而不移除上下文)并启用开发者自助服务。”

![](https://cdn.thenewstack.io/media/2023/12/8ef15ee4-humanitec.png)

门户可以是平台的对外部分，但它本身不是平台，Humanitec的[Luca Galante](https://www.linkedin.com/in/luca-galante/)在帖子中澄清道。

但是，在许多情况下，[一个组织已经有某种平台](https://thenewstack.io/portal-vs-platform-why-you-need-to-think-about-both/)，无论它是否被称为IDP，Port CEO [Zohar Einy](https://www.linkedin.com/in/zohar-einy)在2月的The New Stack上写道。它可能是一个电子表格。它可能是一些可怕的内部构建的服务目录，但组织中某处已经编码了大量的平台工程，并且可能需要或可能不需要实际的全面改造。

“您可能不需要构建一个平台；您只需要使其变得更好。您面临的真正问题是，给定它是平台工程栈中最成熟的元素，您是否应该在平台之上[使用内部开发者门户](https://thenewstack.io/how-to-create-an-internal-developer-portal-mvp/)，”Einy写道。

## 数据显示：平台工程是新的DevOps

然而，更大的图片很清晰，讨论表明平台工程正在获得支持，可能以[DevOps从未实现](https://thenewstack.io/devops-is-dead-embrace-platform-engineering/)过的方式。

回到Port“2024年内部开发者门户状况”调查。它发现100名受访者中有99名表示他们的组织已经开始实施平台工程。

“几年前，我们经常在DevOps调查中看到同样高的水平，但进一步调查发现，他们的DevOps成熟度还很低，”TNS分析师赫希特说。

在这种情况下，实施平台工程的54%是在过去一年进行的。与美国相比(70%对37%)，欧洲受访者在过去一年开始的可能性几乎是两倍。

除电子表格用户外，50%的受访者组织正在使用内部开发者门户，另外35%计划在未来一年内这样做。

“尽管这项研究规模较小，但发现与[2023 StackOverflow开发者调查](https://survey.stackoverflow.co/2023)数据的结果几乎相同，其中47%的微服务用户利用开发者门户或其他中心位置来查找工具/服务，”赫希特指出。

为什么设置开发者门户？最常见的答案是提高软件质量(48%)，其次是46%的受访者提到了开发者生产力。调查显示，由于缺乏平台工程，70%的受访者表示他们每天要花3到4个小时用于非核心工作。另有8%的人说，他们花费的时间甚至更多。

但是，他们节省了多少时间还有待观察。

“几乎所有量化采用平台后实现的潜在节省的研究都集中在公司没有平台之前和之后的比较，”赫希特写道。 “在现实生活中，鲜有真正的无前例情况。”

TNS分析师劳伦斯·赫希特为本文做出了贡献。
