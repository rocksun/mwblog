“每个人都在构建智能体，但构建其底层系统的人还不够多，”开源老兵 [Brian Douglas](https://www.linkedin.com/in/brianldouglas/) [上个月](https://www.linkedin.com/posts/brianldouglas_newjob-ugcPost-7442176114288144384-Nh5-/)在 LinkedIn 上宣布他的新公司时写道。

虽然这一主张很难量化衡量，但大多经得起推敲。企业已经在一定程度上[构建并部署智能体](https://thenewstack.io/how-to-build-production-ready-ai-agents-with-rag-and-fastapi/)，但背后的基础设施往往是临时拼凑的——部分是 SDK，部分是云端管道，部分是内部工具。组件都在，没错，但它们尚未整合成为一个连贯的系统。

而这正是 Brian Douglas 和他的首席技术官兼联合创始人 [John McBride](https://www.linkedin.com/in/jpmcb/) 通过 [Paper Compute Company](https://papercompute.com/) 试图解决的问题。这家初创公司正在构建 AI 智能体之下缺失的层级——并且完全基于开源基础。

“当前设置中缺少的是人们在各种不同情况下运行这些东西的信心，” Brian Douglas 告诉 *The New Stack*。“拥有适当的云原生工具来控制生产中的智能体和大语言模型（LLM）——这就是我们目前在市场上看到的巨大活力所在。三个月前我们还没看到这些。”

> “拥有适当的云原生工具来控制生产中的智能体和大语言模型（LLM）——这就是我们目前在市场上看到的巨大活力所在。三个月前我们还没看到这些。”

虽然公司在 3 月正式揭幕，但 Brian Douglas 和 John McBride 已经通过一系列产品发布启动了进程。2 月份，他们[开源了 *Tapes*](https://papercompute.com/blog/introducing-tapes/)，这是一个零侵入的可观测性层，可以在无需更改应用程序代码的情况下捕获并记录智能体活动。

该系统介于 AI 智能体及其推理提供商之间，捕获遥测数据。它包括一个用于拦截和记录流量的代理服务，一个用于查询会话、消息和元数据的 API 服务器，一个用于管理录制并运行搜索的 CLI 客户端，以及一个用于逐步追踪智能体活动的终端 UI。

![Tapes](https://cdn.thenewstack.io/media/2026/04/e2795a69-tapes-1024x600.png)

***Tapes***

紧随其后的是 [*StereOS*](https://papercompute.com/blog/introducing-stereos/)，这是一个经过加固的基于 Linux 的操作系统，旨在隔离的沙箱环境中运行 AI 智能体，让团队对这些系统在生产环境中的行为拥有更多控制权。

![StereOS](https://cdn.thenewstack.io/media/2026/04/43d33af4-stereosgif.gif)

***StereOS***

其目标是解决 AI 智能体的一个核心问题：一旦它们在生产环境中运行，团队往往既缺乏对其行为的可见性，也缺乏对其操作范围的控制。

“Tapes 向你展示发生了什么 —— StereOS 则确保它不会超出应有的范围，” Brian Douglas 在公司 [3 月份的发布博客文章](https://papercompute.com/blog/introducing-paper-compute/)中写道。

Paper Compute [创建了一个 Gmail 智能体演示](https://papercompute.com/gmail/)来展示其工作原理，它使用在 StereOS 虚拟机内运行的 [OpenClaw 智能体](https://thenewstack.io/persistent-ai-agents-compared/)，在严格控制下对收件箱进行分选。它可以阅读邮件并进行分类，但不能删除或发送回复，也无法访问白名单以外的任何外部服务。

与模型的每次交互都会被 Tapes 捕获为完整且可回放的日志——提示词、响应和决策都存储在本地防篡改记录中。当会话结束时，环境被销毁，凭证被清除，但完整的执行历史记录仍可供检查。

## 开源遇上工程与 AI 基础设施

Brian Douglas 是开源界的熟面孔。在担任 GitHub 开发者倡导总监之后，他在 Linux 基金会旗下的云原生计算基金会（CNCF）领导生态系统和开发者体验工作，此前 Linux 基金会[收购了 *Open Sauced*](https://web.archive.org/web/20251117220928/https://opensauced.pizza/blog/opensauced-is-joining-the-linux-foundation)，这是他[创立的开发者洞察平台](https://thenewstack.io/after-github-brian-douglas-builds-an-open-source-startup/)，旨在帮助贡献者发现并参与开源项目。

与此同时，John McBride 此前曾在 Linux 基金会和 Open Sauced（担任首席 AI 工程师）与 Brian Douglas 合作，更早之前他曾在亚马逊云服务（AWS）担任工程师。

Paper Compute 团队最近还[聘请了创始工程师 Matthew Yeazel](https://www.linkedin.com/feed/update/urn:li:activity:7449484145686380545/)，他在 AWS 工作多年，横跨 EC2、Amazon Linux 和专注于容器的操作系统 Bottlerocket。

> Paper Compute 实际上正试图介于开发者工具和核心基础设施之间，其团队凭借构建和大规模运营系统的经验而形成。

这种开源、基础设施和系统工程经验的融合，反映了 Paper Compute 实际上想做的事情：处于开发者工具和核心基础设施之间，拥有一支由具备构建和运营大规模系统经验的人员组成的团队。

“我们知道生产级基础设施是什么样的——智能体理应享有同样的严谨性，” Brian Douglas 说道。

## 理解系统

随着越来越多的团队开始在生产环境中运行智能体，理解这些系统实际在做什么变成了一项挑战。数据确实存在，但通常是不完整的、难以访问的，或者是与构建智能体时使用的特定 SDK 或框架绑定的。

在许多情况下，检查智能体行为的唯一方法是通过平台本身提供的工具——例如 LangChain 及其配套的可观测性工具 LangSmith，它们可以捕获追踪、日志和执行路径，但历史上一直是在它们自己的生态系统内进行的。

Brian Douglas 举了一个简单的例子：当智能体失败时，目标不是事后重建发生了什么，而是已经有一个完整的记录——一个可以直接查询的记录。

“所以，你不需要想知道你是如何到达那里的，你只需与数据交互即可，”他说道。“没有 SDK，没有额外的代码——它就在后台运行。”

这指向了 Brian Douglas 看到的长期价值所在——不在于基础设施本身，而在于它所捕获的内容。他认为，智能体活动生成了一份系统如何运行以及决策如何制定的记录，这本身就变得非常有价值。

“价值实际上更多在于流经智能体的数据，”他说道。

虽然 Paper Compute 还处于早期阶段，但该公司已经开始勾勒围绕其开源项目的商业产品蓝图。

## 按算力付费：一场关于数据的博弈

从本质上讲，Paper Compute 不仅仅是在构建工具，还在努力建立一个在生产环境中运行和管理 AI 智能体的层——涵盖可观测性、执行以及最终的编排。

公司名称本身就反映了这种思路。“你最终会为算力付费（Pay-per compute），” Brian Douglas 说道。他指向了一种模型，即使用情况——以及流经这些系统的数据——成为平台盈利的核心。

这意味着在 Tapes 等工具捕获的遥测数据之上进行构建，将智能体对话转变为可重复使用的“技能”，并利用这些数据来优化模型的部署和运行。

平台的早期版本已经在内部进行测试，团队开始向潜在用户展示该系统。

> 长期来看，该公司的目标是那些需要对 AI 系统运行方式进行更严格控制的团队。

长期来看，该公司的目标是那些需要对 AI 系统运行方式进行更严格控制的团队——特别是在受监管或本地部署的环境中，安全性、合规性和可审计性至关重要。

就 Brian Douglas 而言，他将其与早期的一波基础设施浪潮进行了类比。“大约 13 年前，当云原生基础设施开始成形时，我们有了 Kubernetes，”他说道。“现在我们在 AI 工具领域看到了类似的浪潮。”

例如，Kubernetes 越来越多地被用于编排[重 GPU 的 AI 工作负载](https://www.civo.com/learn/kubernetes-llama-deploy-ai-models-llm-gpu-cluster)，将其为扩展基于 CPU 的应用程序而建立的相同模型扩展到一种新型的计算密集型系统。

与此同时，像 [OpenTelemetry 这样的开放标准正在演进](https://grafana.com/blog/a-complete-guide-to-llm-observability-with-opentelemetry-and-grafana-cloud/)，以捕获来自 LLM 和智能体系统的追踪、指标和日志，为理解这些系统在生产环境中的行为提供了一种更一致、供应商中立的方式。

Brian Douglas 认为，这可能会使生态系统达到类似的成熟点。“通过开源，我们将看到这些工具变得商品化，”他说道。“在接下来的六个月里，我认为我们将看到企业——银行、大公司——准备好规模化应用。”

“但这些工具仍然需要给他们提供在生产中运行智能体的信任，” Brian Douglas 补充道。