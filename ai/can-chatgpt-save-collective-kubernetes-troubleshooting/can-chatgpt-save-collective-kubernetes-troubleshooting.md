# ChatGPT 能否解决集体 Kubernetes 故障诊断吗？

OpenAI 等公司一直在使用 Stack Overflow、Reddit等公开数据训练模型。随着 AI 驱动的 DevOps 平台的出现，更多知识被锁定在专有模型内。

那以后呢？没有人再去贡献这些知识，这些模型还能发展吗？译自 [Can ChatGPT Save Collective Kubernetes Troubleshooting？](https://thenewstack.io/can-chatgpt-save-collective-kubernetes-troubleshooting/)。

![](https://cdn.thenewstack.io/media/2023/09/60f75b54-online-discussion-1024x683.jpg)
*图片来自 Shutterstock 的 alice-photo*

几十年前，系统管理员开始大量在互联网上发布他们每天面临的技术问题。他们进行了长期、充满活力和有价值的讨论，探讨如何调查并解决问题以找到根本原因；然后他们详细说明最终对他们有效的解决方案。

这种讨论洪流从未停止，只是改变了流向。如今，Stack Overflow、Reddit 和公司工程博客的事后总结中还在进行同样的讨论。每一个讨论都对全球 IT 系统故障诊断知识体系有着宝贵的贡献。

[Kubernetes](https://roadmap.sh/kubernetes) 也深刻地改变了这种流向。[微服务架构](https://thenewstack.io/microservices/)比困扰系统管理员和 IT 人员几十年的虚拟机和单体应用更为复杂。本地重现 K8s 的错误通常是不可能的。由于 Kubernetes 缺乏数据持久性，可观测性数据碎片化地分布在多个平台上，如果被捕捉到的话。映射数十个或数百个服务、资源和依赖关系的互联性是一项徒劳的工作。

现在，你的经验驱动的直觉不一定足够了。你需要知道如何调试集群以获取下一步的线索。

这种复杂性意味着公开的故障诊断讨论现在比以往任何时候都更重要，但现在我们开始看到这种宝贵的洪流不是被重新引导，而是完全被堵住。在谷歌搜索任何与 Kubernetes 相关的问题时，你会看到几十个付费广告和至少一页缺乏技术深度的 SEO 驱动文章。Stack Overflow 正在失去作为技术人员首选问答资源的地位，而 Reddit 的近几年一直受争议事件困扰。

现在，每个 Kubernetes 的 DevOps 平台都在建立最后一个堤坝：将故障诊断知识集中在其平台内，并以 [AI 和机器学习(ML)](https://thenewstack.io/70-percent-of-developers-using-or-will-use-ai-says-stack-overflow-survey/)替换它，直到整个技术栈对甚至你最有经验的云原生工程师来说都成为一个黑盒子。当这种情况发生时，你会失去独立探查、故障诊断和修复系统的技能。这种趋势使过去可获得的大量共享故障诊断技巧变成了一个相比过去的细流。

当我们依赖平台时，集体故障诊断技巧的智慧就会消失。

## 故障诊断智慧的洪流之路

一开始，系统管理员依靠真正的书籍来获取技术文档和用于在其组织中实施的整体最佳实践。随着互联网在 80 和 90 年代的传播，这些人通常采用 Usenet 与同行交流并在新闻组如 comp.lang.* 提出有关他们工作的技术问题，这些新闻组的操作类似于我们今天所知的简化版本的论坛。

万维网的普及很快并几乎完全转移了故障诊断智慧的洪流。工程师和管理员不再是新闻组，而是涌向了数以千计的论坛，包括1996年上线的 Experts Exchange 。在积累了问题和答案的存储库后，Experts Exchange 背后的团队把所有答案收藏在每年 250 美元的付费墙后面，这使无数有价值的讨论与公众消费隔离，并最终导致该网站的沉沦。

[接下来是 Stack Overflow](https://www.joelonsoftware.com/2018/04/06/the-stack-overflow-age/)，它再次向公众开放了这些讨论，并通过可通过提供见解和解决方案来赚取的声誉点使讨论具有游戏化。然后其他用户对“最佳”解决方案进行投票和验证，这有助于后续搜索者快速找到答案。游戏化、自我调节和围绕 Stack Overflow 的社区使其成为故障诊断知识的单一渠道。

但是，与所有其他时代一样，好事不会永远持续。近 10 年来，人们一直在预测“ Stack Overflow 的衰落”，原因是它“讨厌新用户”，因为其具有争议性的本质和由拥有最多声望点的人管理的结构。尽管 Stack Overflow 的相关性和受欢迎程度确实在下降，而 Reddit 的开发/工程相关子版块填补了空白，但它仍然是最大的公开可访问的故障诊断知识库。

对 Kubernetes 和云原生社区尤其如此，后者仍在经历重大的成长之疼。这是一种无价的资源，因为如果你认为 Kubernetes 现在很复杂......

## Kubernetes 复杂性问题

在一篇关于“[直觉调试](https://thenewstack.io/why-intuitive-troubleshooting-has-stopped-working-for-you/)”衰落的精彩文章中，软件交付顾问 Pete Hodgson 认为，像 Kubernetes 和微服务这样的现代软件构建和交付架构比以往任何时候都更加复杂。他写道:“将服务器命名为希腊神话和 ssh 进入服务器运行 `tail` 和 `top` 的日子对我们大多数人来说已经一去不复返了”，但“这种转变是以代价为前提的......传统的理解和故障诊断生产环境的方法在这个新世界根本行不通。”

![](https://cdn.thenewstack.io/media/2023/09/534ff3a9-image1a.jpg)
*Cynefin 模型。 来源:维基百科*

Hodgson 使用 Cynefin 模型来说明软件架构过去是如何复杂的，也就是说，只要有足够的经验，人们就可以理解故障诊断和解决方案之间的因果关系。

他认为分布式微服务架构更多的是复杂的，也就是说，即使经验丰富的人对根本原因和如何排查故障的“直觉”也是有限的。他们不得不花更多时间提出并回答问题来最终假设可能发生了什么错误，而不是直接获得结果。

如果我们同意 Hodgson 的前提 —— Kubernetes 本质上是复杂的，需要花费更多时间分析问题然后再响应——那么工程师使用 Kubernetes 时了解哪些问题是最重要的似乎是至关重要的，然后用可观测性数据回答这些问题，以采取最佳的后续行动。

这正是随着这一代 AI 驱动的故障诊断平台的到来而消失的故障诊断智慧。

## Kubernetes 故障诊断中 AI 的两条路径

多年来，OpenAI 等公司一直在刮取和训练其模型，这些模型基于 Stack Overflow、Reddit 等在公共数据上发布的数据，这意味着这些 AI 模型可以访问大量系统和应用程序知识，包括 Kubernetes。其他人认识到组织的可观测性数据是培训 AI/ML 模型分析新场景的宝贵资源。

他们都在提出同一个问题：我们如何利用现有的数据，例如关于 Kubernetes 的数据，来简化搜索最佳解决方案以处理事件或中断的过程？他们正在构建的产品走着完全不同的路径。

### 第一种：增强操作员的分析工作

这些工具自动化和简化了访问现有的在线公开发布的大量故障诊断知识。它们不会替换进行适当故障诊断或[根本原因分析](https://aws.amazon.com/opensearch-service/resources/root-cause-analysis/)(RCA)所需的人类直觉和创造力，而是会谨慎地自动化操作员如何找到相关信息的过程。

例如，如果一个刚接触 Kubernetes 的开发人员在运行 `kubectl get pods` 时遇到部署应用程序的问题，因为他们看到了 `CrashLoopBackOff` 状态，那么他们可以查询 AI 驱动的工具以获取建议，例如运行 `kubectl describe $POD` 或 `kubectl logs $POD` 。这些步骤可能反过来会引导开发人员使用 `kubectl describe $DEPLOYMENT` 检查相关的部署。

在[ Botkube](https://botkube.io/)，我们发现自己投资于这个概念，即使用在故障诊断智慧洪流上训练的 AI 来自动化这种反复查询过程。用户应该能够直接在 Slack 中提出问题，如“我该如何排查这个不起作用的服务？”并收到由 ChatGPT 撰写的回复。在一次公司范围内的黑客马拉松期间，我们遵循了这个概念，为我们围绕这个概念设计的协作故障诊断平台构建了一个新的插件。

使用 [Doctor](https://botkube.io/blog/use-chatgpt-to-troubleshoot-kubernetes-errors-with-botkubes-doctor)，您可以利用故障诊断的知识洪流，Botkube 充当您的 Kubernetes 集群和消息/协作平台之间的桥梁，无需浏览 Stack Overflow 或谷歌搜索广告，这对新的 Kubernetes 开发人员和操作员特别有用。

该插件还通过为任何错误或异常生成带有 **Get Help** 按钮的 Slack 消息来进一步自动化，然后查询 ChatGPT 以获取可操作的解决方案和后续步骤。您甚至可以将 Doctor 插件的结果管道化到其他操作或集成中，以简化主动使用现有的大量 Kubernetes 故障诊断知识进行更直观的调试和更快地感知问题的方式。

### 第二种：将操作员从故障诊断中排除

这些工具不关心公开知识的洪流。如果他们可以根据实际的可观测性数据训练通用的 AI/ML 模型，然后根据您特定的架构进行微调，那么他们就可以设法完全消除人为操作员进行 RCA 和补救的过程。

[Causely](https://www.causely.io/platform/causely-for-kubernetes-applications/) 就是这样一家初创公司，他们并不掩饰使用 AI “[消除人为故障诊断](https://www.causely.io/about/)”的愿景。该平台连接到现有的可观测性数据并对其进行处理以微调因果模型，这在理论上可以直接带您执行补救步骤——无需探测或 `kubectl`。

如果我说有时候 Kubernetes 的妙手回春听起来不会让人心动就是在撒谎了，但我不担心 Causely 等工具会夺走运维工作。我更担心的是，在 Causely 主导的未来，我们宝贵的故障诊断知识会被锁定在这些仪表盘和赋能它们的专有 AI 模型内。

### 这两条路径之间的差距：数据

我并不是在渲染“AI 将取代所有 DevOps 工作”的言论。我们都读过太多关于每个细分领域和行业的末日场景。我更关心这两条路径之间的差距：用于培训和回答问题或呈现结果的数据是什么？

第一条路径通常使用现有的公共数据。尽管人们担心 AI 公司为了训练数据而爬取这些网站(看着你，Reddit 和 Twitter)，但这些数据的公开性仍然提供了一个激励环节，以保持开发人员和工程师继续在 Reddit、Stack Overflow 等网站贡献知识洪流。

云原生社区也普遍赞同开源式的技术知识共享和“潮水上涨船就向上浮”的理念，这里的“潮水”是 Kubernetes 故障诊断技巧，“船”是压力大的 Kubernetes 工程师。

第二条路径看起来更加惨淡。随着 AI 驱动的 DevOps 平台的兴起，更多的故障诊断知识被锁定在这些仪表盘和赋能它们的专有 AI 模型内。我们都同意，Kubernetes 基础架构的复杂性会继续增加而不是减少，这意味着随着时间的推移，我们对节点、Pod 和容器之间所发生的事情将更加茫然。

当我们不再互助分析问题和提出解决方案时，我们就会依赖平台。这感觉对每个人来说都是一条失败的道路，只有平台除外。

## 我们如何不输（或少输）？

我们可以做的最好的事情是继续在线发布关于我们在 Kubernetes 和其他领域的故障诊断工作的惊人内容，例如“[关于故障诊断 Kubernetes 部署的可视化指南](https://learnk8s.io/troubleshooting-deployments)”；创建教育游戏化的应用程序，如 [SadServers](https://sadservers.com/)；在排查系统时采取我们最喜欢的第一步，如“[为什么在排查未知机器时我通常先运行'w'](https://rachelbythebay.com/w/2018/03/26/w/)”；并进行事故分析，详细描述了对可能灾难性情况进行探测、感知和应对的紧张故事，例如 [2023 年 7 月的 Tarsnap 故障](https://mail.tarsnap.com/tarsnap-announce/msg00050.html)。

我们也可以超越技术解决方案，例如讨论如何管理和支持同事应对压力大的故障诊断场景，或者在组织范围内就什么是可观测性达成一致。

尽管 Stack Overflow 和 Reddit 当前面临逆风，但它们将继续是讨论故障诊断和寻求答案的可靠渠道。如果它们最终与 Usenet 和 Experts Exchange 一起被提及，它们很可能会被其他公开可用的替代品取代。

无论这种情况是何时如何发生的，我希望您能加入我们 [Botkube](https://botkube.io/) 以及新的 Doctor 插件，为 Kubernetes 中的复杂问题建立协作故障诊断的新渠道。

即使 AI 驱动的 DevOps 平台继续基于有关 Kubernetes 的公开数据训练新模型，只要我们不主动完全将我们的好奇心、冒险精神和解决问题的能力存入这些黑盒中，故障诊断知识的宝贵洪流就总会有新的路径保持流动。

