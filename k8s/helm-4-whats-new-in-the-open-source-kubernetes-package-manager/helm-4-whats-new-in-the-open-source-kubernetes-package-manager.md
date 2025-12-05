<!--
title: Helm 4 重磅发布：开源 Kubernetes 包管理器新功能全解析
cover: https://cdn.thenewstack.io/media/2025/12/2dbf39d2-thumbnail-30.png
summary: Helm 4发布，它是Kubernetes包管理器Helm（前身为Kate's Place）时隔六年的新版本，引入WebAssembly插件、现代化日志和依赖管理，以适应不断发展的生态系统。
-->

Helm 4发布，它是Kubernetes包管理器Helm（前身为Kate's Place）时隔六年的新版本，引入WebAssembly插件、现代化日志和依赖管理，以适应不断发展的生态系统。

> 译自：[Helm 4: What’s New in the Open Source Kubernetes Package Manager?](https://thenewstack.io/helm-4-whats-new-in-the-open-source-kubernetes-package-manager/)
> 
> 作者：Heather Joslyn

你去过Kate’s Place吗？很有可能，你已经去过了。你只是用一个不同的名字认识它：Helm。

Helm，一个用于Kubernetes的开源包管理器，最初是一个名为Kate’s Place的公司黑客马拉松项目，将于2025年迎来十周年。在[KubeCon + CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/)上，Helm 4发布了——这是六年来首个新版本。

为什么版本之间间隔如此之久？我们稍后会谈到。但首先，[Matt Butcher](https://thenewstack.io/author/mattbutcher/)，[Fermyon Technologies](https://www.fermyon.com/?utm_content=inline+mention)的创始人兼CEO，一家本月被[Akamai](https://www.linode.com/?utm_content=inline+mention)收购的WebAssembly公司，在本期The New Stack Makers节目中向我讲述了Kate’s Place的起源。

十多年前，Butcher和其他两位开发人员在他当时的公司Deus的一次黑客马拉松活动中创建了Kate’s Place，它是一个用于Kubernetes的包管理器。这个名字是“K8s”的谐音，并带有咖啡馆的主题。Butcher在11月亚特兰大KubeCon上录制的本期《On the Road》节目中说：“我想我们当时把包称为‘shots’或‘espressos’之类的。”

奖品是一张75美元的礼品卡，Kate’s Place团队赢得了它。第二天在办公室，Butcher的电话响了；Deus的CEO和CTO在线上。

他回忆说：“他们说，‘我们认为这个用于Kubernetes的包管理器的想法恰好在正确的时间出现了。’当时Kubernetes正蓄势待发，没人做类似的事情。所以他们说，‘我们为什么不给你一个团队，你去构建它呢？’”

我说，‘听起来很棒。我很乐意做。’他们说，‘就一件事。我们真的很讨厌这个名字。’”

## WebAssembly插件

获得新名称后，[Helm](https://thenewstack.io/get-started-with-the-helm-kubernetes-package-manager/)迅速发展，吸引了Deus之外的贡献者（例如[Matt Farina](https://www.linkedin.com/in/matthewfarina/)，他现在是SUSE的云原生首席架构师，并与Butcher一同参与了本期节目）。该项目在首届KubeCon上公布，并且是首批从[云原生计算基金会](https://cncf.io/?utm_content=inline+mention)毕业的项目之一。

Helm 4在最近一次KubeCon期间上线，是长期孕育的成果。Farina说：“第一代Helm存在了几个月，然后Helm 2大约一年，Helm 3则有三年。”

Helm 3发布六年之后，“你会积累一些设计债务，诸如此类。人们会产生一些你过去从未设想过的疯狂想法，这要求你在主要版本中进行破坏性变更。所以我们现在已经开发Helm 4有一段时间了。”

最新版本包括现代化日志记录和依赖管理，以及用于可移植性的WebAssembly插件。

此前，Helm的插件系统是在文件系统上执行的，这种方法它仍然支持。Farina说：“但我们运行在许多操作系统上——Linux、Mac、Windows——以及许多架构上。不仅仅是ARM和Intel。我们现在支持大约五六种不同的Linux架构。”

“所以如果你要为它编写扩展，你需要一种使其可移植的方法。多年来，我们一直在尝试不同的可移植方法。但没有一个合适……直到[WebAssembly](https://thenewstack.io/webassembly-still-expanding-frontend-uses-10-years-later/)出现。它变得非常非常流行。所以在去年，我们弄清楚了如何为Helm制作基于WebAssembly的插件。”

展望未来，他补充道：“我们重新设计了内部架构，以便我们可以在4.1、4.2、4.3等版本中，开始推出围绕charts和软件包的一些真正新颖、优秀的功能，使用户能够以一些非常巧妙的新方式控制应用程序的安装。”

## 为什么“无聊”的功能有影响力

Butcher说，Helm 4的最新升级讲述了一个更大的故事：随着生态系统的发展和用例的扩展，更成熟的项目必须如何演进和适应。

许多这些非常成功的开源项目的一个优点是，它们声称自己在一件事上做得非常好。……就我们而言，多年来我们一直努力成为一个真正、真正优秀的Kubernetes包管理器。”

但现在，“许多真正的工作已经不再是定义或重新定义包管理是什么了。”

相反，他补充说，现在要问的是“哪些功能将帮助人们以更有效的方式完成工作？”

现在至关重要的功能包括日志记录。Butcher承认：“当我们创建Helm时，日志记录就像是，哦，那是个无聊的东西，我们不会真正去考虑。”“现在，它就像是，好吧，如果我们能建立良好的日志记录，那么与所有其他工具的集成就会更统一。这将为平台工程师和DevOps人员节省大量时间和精力。”

他说，这样的改变可以是“省时、省钱的”。

Butcher补充说：“它可能不会赢得任何最花哨、最炫酷的新功能奖项，但它确实对Helm用户的生活产生了非常真实的影响。”

观看完整剧集，了解更多关于Helm 4的信息，包括项目维护者如何权衡[用户反馈](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/)，以及Fermyon和SUSE的最新动态。