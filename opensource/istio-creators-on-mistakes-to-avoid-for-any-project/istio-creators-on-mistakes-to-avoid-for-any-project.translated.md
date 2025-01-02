# Istio 创建者谈避免任何项目可能犯的错误

![Featued image for: Istio Creators on Mistakes To Avoid for Any Project](https://cdn.thenewstack.io/media/2024/12/ec8a85ca-bruce-green-1-1-1024x683.png)

Istio 已成为一个开源项目，它满足了——如果不是全部满足的话——大多数关于开源项目应该是什么样的要求。

除了其众多贡献者来自不同且常常相互竞争的组织、下载量以及次要的GitHub星标外，Istio作为[服务网格](https://thenewstack.io/service-mesh/)的采用也积累了许多赞誉，并为其成为一个非常好的选择提供了许多论据。与[Linkerd](https://thenewstack.io/some-linkerd-users-must-pay-fear-and-anger-explained/)一样，Istio是最受欢迎的开源服务网格之一。

但这并不意味着从[Istio](https://thenewstack.io/ambient-mesh-can-sidecar-less-istio-make-applications-faster/)创建至今，一路走来没有遇到过许多挫折。Istio为云原生环境中的服务网格设定了新的标准，为所有应用程序提供安全、[可观察性](https://thenewstack.io/observability/)和流量管理。然而，Istio的创建者从一开始就难以把握用户社区真正需要什么。在1.0版本发布时，市场营销介入其中，炒作并不一定符合预期——或者至少最初没有达到预期。

考虑到Istio现在是用于可观察性的领先服务网格，其创建者的艰辛和挣扎为我们提供了许多教训，说明在许多情况下不应该做什么——包括可以尽早避免的任何开源项目的错误，特别是对于那些创建者雄心勃勃的项目而言。项目创建者的经验教训在[KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)盐湖城的一次座无虚席的会议上进行了详细描述（我以前从未见过如此长的演讲队伍）。在他们的演讲“[Istio做错了什么：过去七年服务网格的经验教训](https://kccncna2024.sched.com/event/1i7nP?iframe=no)”中，来自Solo.io的Istio共同创建者——Solo.io的CTO [Louis Ryan](https://www.linkedin.com/in/louiscryan/)和gRPC共同创建者以及Solo.io的全球首席现场技术官[Christian Posta](https://www.linkedin.com/in/ceposta)——描述了Istio的成功故事，以及其中的不足之处。

## 愿景与挫折

![](https://cdn.thenewstack.io/media/2024/12/5934b5e1-capture-decran-2024-12-06-185942.png)
KubeCon+CloudNativeCon演示文稿中的一张幻灯片。来源：Solo.io

项目创建之初的一个失误涉及到重点和愿景，以及两者如何兼而有之且并非相互排斥——因为不专注于实现愿景的方法会导致灾难。正如Ryan在演讲中解释的那样，Istio最初是为了“连接、保护、控制和观察”而创建的。

“Istio中较大的问题之一是，这些是目标；这些是愿景，但愿景和重点并非一回事。如果我们专注于其中的一到一点五件事，我认为该项目本来可以避免早期发生的一些失误，”Ryan说。“我对此负有责任：我们有雄心勃勃的目标。我们想做很多事情，有很多实际问题需要解决，但重点也许是项目早期的一个问题。”

在Istio开发的早期阶段，最初有50个CR。“这是一个很大的API表面积和很多功能——用户无论如何都需要数年时间才能完全消化和使用这些功能。更不用说我们一开始就知道他们将如何使用它们，并一次性发布所有功能，”Ryan说。“所以，这是一个漫长而痛苦的教训。我们进行的一些重构显然减少了或更专注于我们如何努力实现这一愿景。”

很快发现，在[Google](https://cloud.google.com/?utm_content=inline+mention)行之有效的方法——Istio最初是在Google的领导下创建的——并不一定适用于其他组织。正如Ryan所描述的，他在Google工作期间参与过“连接、保护、观察和控制”的项目。“我了解它们旨在解决的问题以及它们在Google是如何构建的。但在Google构建这些东西与为截然不同的受众构建它们并不相同，”Ryan说。“对我来说，一个巨大的经验教训是，我了解到在Google内部很重要的事情与对你来说很重要的事情并不相同。”

Istio 1.0版本于2018年7月发布，发布时有很多市场营销、兴趣和很高的期望，但并没有达到预期。
“如果你构建高质量的产品并进行部署，人们就会感到满意。你会得到积极的净结果——他们会推广它，告诉他们的朋友，并公开声明它有多么棒，以及它如何解决了痛点或提供了价值，”Posta说。“不幸的是，Istio 1.0一开始并没有做到这一点。”

下载二进制文件并尝试安装Istio 1.0后，该过程经常失败，Posta说。代理偶尔会启动，但控制平面pod经常自我循环，造成不稳定。文档不足，特别是对于大型集群，它们无法按预期运行。当时宣传的多集群支持也未能实现。这些缺点阻止了获得积极的净推荐值，导致用户感到沮丧和困惑，Posta说。

Istio 1.0缺乏重点，严重加剧了这些问题。Posta说，初始版本中包含的功能——例如连接、安全、控制和观察——非常广泛。“Istio 1.0有很多功能。当我们第一次宣布它时，有很多东西，听起来很令人兴奋，而且[它]是你需要的东西，”Posta说。“尽管功能列表看起来令人兴奋且必要，但使用产品的体验与预期不符。”用户不知道从哪里开始，即使是像流量切换这样的基本功能，“在Istio 1.0中也不是很清楚”。

企业内部的组织孤岛加剧了困难。不同的团队负责网络、安全、基础设施和应用程序开发。这种划分使得不清楚哪个团队应该负责Istio。凭借其跨越网络和安全的混合功能，Istio缺乏自然的拥有者。当时，跨职能团队很少见，平台工程或平台团队尚未成为常见的结构。Posta解释说，这种组织上的模糊性使Istio在企业中没有明确的归属。

回顾我的[@KubeCon_]NA关于[@soloio_inc]的[@christianposta]和Louis Ryan的演讲“Istio做错了什么：过去七年服务网格的经验教训”的笔记后，一个收获是，当目标是多功能团队时，开源项目可能会受到影响。[https://t.co/ed5mTa8igr](https://t.co/ed5mTa8igr)[pic.twitter.com/cvbRQYO85b](https://pic.twitter.com/cvbRQYO85b)— BC Gain (@bcamerongain) [2024年12月11日]

“企业是按照孤岛式结构组织的。他们有不同的团队负责不同的领域：网络是一个团队，安全是一个团队，基础设施是一个团队，应用程序开发人员是一个团队，”Posta说。“当人们最初安装或下载它时，他们会想，‘谁来运行这个？谁来使用这个？’”

向Istio 1.1的转变带来了对可预测和定期发布的 renewed emphasis。采用了季度发布计划，帮助重建信心并建立节奏。从那时起，这个计划基本保持不变，只有很小的偏差，反映了对一致性和改进的承诺，Ryan和Posta解释说。

人们努力让各种供应商参与Istio的开发。一个值得注意的成功是建立了一个治理模型——特别是开放治理框架，Posta说。尽管Istio最初不是开放基金会的一部分，但实施了治理结构以鼓励供应商参与和促进合作。成立了一个指导委员会和一个技术监督委员会，这些委员会的席位根据对项目的贡献程度分配。Posta说，这种基于贡献的模式激励了积极参与项目。

## 未来展望

尽管出现失误和挑战，Istio社区展现了韧性。Posta解释说，在科技行业追求雄心勃勃的目标需要时间，通常需要数年时间。虽然炒作周期可能很快达到顶峰，但有意义的进步需要持续的努力。“Istio的贡献者，其中许多人已经为该项目贡献了近十年时间，证明了这种承诺，”Posta补充道。

用户以前难以使用Istio。Posta说，他们有时仍然不确定他们想要的功能。“现在，我们试图更加专注，并建议用户选择他们在实施中想要成功的一件事，然后继续进行下一步——无论是安全功能、可观察性目标还是流量管理，”Posta说。

“Solo通常几乎每一次参与都始于专注于交付‘渐进式成功’，”Ryan说。“同样的方法也适用于软件交付和开源项目。如果没有重点，如果你试图同时做太多事情，你就会遇到质量问题，”Ryan说。“而且，Istio确实存在质量问题。”

[YOUTUBE.COM/THENEWSTACK](YOUTUBE.COM/THENEWSTACK)
科技发展迅速，不要错过任何一集。订阅我们的YouTube
频道，收听我们所有的播客、访谈、演示等等。 [https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)