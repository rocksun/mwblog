<!--
title: Kubernetes的单体教训对AI智能体运行环境意味着什么
cover: https://cdn.thenewstack.io/media/2026/10/de419750-growtika-qpkdga-kdik-unsplash-scaled.jpg
summary: 本文回顾了KubeCon前的云原生生态动态，重点探讨了将Kubernetes架构教训应用于构建云原生AI智能体运行环境的必要性，同时涵盖了GPU调度优化、事件检测加速及安全挑战等内容。
-->

本文回顾了KubeCon前的云原生生态动态，重点探讨了将Kubernetes架构教训应用于构建云原生AI智能体运行环境的必要性，同时涵盖了GPU调度优化、事件检测加速及安全挑战等内容。

> 译自：[What Kubernetes’ "monolith" lesson means for AI agent harnesses](https://thenewstack.io/kubecon-agent-harness-koordinator/)
> 
> 作者：Bill Doerrfeld

**欢迎来到新一期的** [**通往 KubeCon 之路**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)，在倒计时迎接于 11 月 9 日至 12 日在犹他州盐湖城举办的 [KubeCon + CloudNativeCon NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 大会之际，这里将为您提供所有关于 Kubernetes 和云原生的最新资讯。

本周，我们将审视智能体运行环境（harness）的现状以及需要演进的方向。我们还将报道 HPE 对 Kubernetes 可观测性的见解、更多科幻般的智能体化 DevOps，以及一个向 Kubernetes 默认调度器展示谁才是 GPU 利用率老大的卓越调度器。

除此之外，还有来自 CNCF 的新闻：今年 ArgoCon 的看点、提升开源项目安全卫生的绝佳机会、Atlassian 缩短事件到指标延迟的技术栈，以及献给 TNS 读者的特别礼物。

## **HPE 在 TNS 上分享 Kubernetes 可观测性技巧**

让 Kubernetes 运行起来只是一个里程碑。明确谁来负责下一次升级、访问请求或失败恢复则是一段持续的旅程。

本周，我们发布了“[一个活着的 Kubernetes 集群仍然可能存在所有权空白](https://thenewstack.io/kubernetes-operations-ownership-governance/)”，这是 Chris J. Preimesberger 撰写的由 HPE 赞助的四部分系列文章的第二篇。它审视了平台团队和应用团队在上线后如何划分职责，从配置漂移、安全策略到升级验证和恢复演练。一个健康的集群并不必然意味着一个健康的应用——而必须有人来填补这个所有权空白。

*Hewlett Packard Enterprise (HPE) 是通往 KubeCon 之路的首席赞助商。* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *帮助 IT 组织跨混合、多厂商环境实现基础设施现代化、精简运营并加速 AI 倡议。*

错过了开篇？[第一部分探讨了 Kubernetes 自助服务](https://thenewstack.io/kubernetes-self-service-platform-teams/)：开发人员如何在无需等待工单队列的情况下获得批准的环境，同时平台团队保留对访问权限、成本和生命周期控制的责任。这些文章共同提出了一个现实问题：如何在明确运营问责制的同时，赋予开发人员更多独立性？

接下来，该系列将转向在 Kubernetes 看起来健康时诊断缓慢的应用，然后转向衡量 AI 推理性能。随着工作负载在通往 KubeCon 的道路上变得更加严苛，这两篇内容都将探讨团队所需的可观测性。

## **CNCF 为 TNS 读者提供 10% 的折扣**

本周，*The New Stack* 的读者将获得来自云原生计算基金会（CNCF）的特别福利。如果您计划前往盐湖城参加 KubeCon + CloudNativeCon NA，在[通过此链接注册](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/?utm_campaign=45192315-KubeCon-NA-2026&utm_source=Media%20Partner%202026)时使用折扣码 `KCNA26MED10`，即可享受门票 9 折优惠。

距离 KubeCon 仅剩 38 天（如果按专栏计算则是四期通往 KubeCon 之路），因此最好尽快行动以注册并规划您的行程。

## **智能体运行环境走向云原生**

智能体“运行环境（harness）”迅速成为了环绕 AI 智能体的一切事物的代名词：上下文、文件系统、子智能体、权限等等。然而，[Stacklok](https://stacklok.com/) 创始人兼 CEO [Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/) 表示，这还远远不够。

在他看来，大多数运行环境过于本地化，专为单个开发人员的笔记本电脑构建。典型的运行环境无法充分扩展以服务数百个会话。会话容易崩溃，并且您无法轻松地在客户端或设备之间迁移体验。

本周，他在 [CNCF 博客](https://www.cncf.io/blog/2026/09/28/the-case-for-a-cloud-native-agent-harness/)上发文，为主张云原生智能体运行环境进行辩护。在他看来，这是一个将智能体循环与其周围的基础设施和服务分离的分布式应用程序。

“Kubernetes 曾向这个行业表明，容器中的单体依然是单体，”他写道。“这个教训同样适用于智能体。”

## **Koordinator 将 Kubernetes 上的 GPU 分配率提升至 95% 以上**

周二发布的一篇[案例研究](https://www.cncf.io/case-studies/zhuoyu-technology/)详细介绍了中国自动驾驶技术公司卓驭科技如何利用 [Koordinator](https://koordinator.sh/) 显著提高 Kubernetes 利用率。Koordinator 是一个用于高效调度微服务、AI 和大数据工作负载的 CNCF 托管项目。

卓驭科技在基于 Kubernetes 的环境中运行自动驾驶工作负载，但遇到了默认 Kubernetes 调度器的性能低效问题，该调度器限制了分配和利用率。通过使用 Koordinator，该团队将 GPU 分配率推高至 95% 以上，整体 GPU 利用率推高至 55% 以上。

该案例研究展示了默认 Kubernetes 调度器中的某些缺陷如何导致启动失败、GPU 利用率低、GPU 闲置以及分布式作业调度问题。它还展示了 Koordinator 在生产环境中表现良好。

## **CNCF 与 OpenSSF 宣布举办为期一个月的挑战赛**

[开源安全基金会](https://openssf.org/)（OpenSSF）与 CNCF 正在联手组织 [Security Slam](https://openssf.org/blog/2026/09/23/security-slam-2026-fall-edition/)，这是一项为期 30 天的挑战赛，引导参与者使用 OpenSSF 项目来改善其项目的安全态势。

邀请所有开源项目参与。正如 [Eddie Knight](https://www.linkedin.com/in/knight1776) 和 OpenSSF 的 [Stacey Potter](https://www.linkedin.com/in/staceympotter) 所写，Slam“现在正利用新工具极大地拓宽参与资格。”

该挑战赛于 10 月 5 日至 11 月 6 日举行。[在此注册](http://securityslam.com/slam26/register)以参与其中，并随着目标的公布进行关注。完成挑战，您或许就能在 KubeCon 的 OpenSSF 展位（#313）领到一个精美的奖品。

## **Atlassian 的云原生技术栈将事件到指标的延迟降至 10 秒以内**

在事故检测和响应中，每一秒都至关重要。周三，Atlassian 高级工程经理 [Deepak Biswas](https://www.linkedin.com/in/dkbiswas/) 在 CNCF 博客上分享了一篇[深入的案例研究](https://www.cncf.io/blog/2026/09/30/from-40-seconds-to-under-10-rebuilding-incident-detection-on-opentelemetry-apache-kafka-and-apache-flink-on-kubernetes/)，展示了 Atlassian 为缩短这些时间所做的不懈努力。

其自动化事故创建系统 AutoHOT 背后的检测平台，在 Kubernetes 上结合了 [OpenTelemetry](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/)、[Apache Kafka](https://kafka.apache.org/) 和 [Apache Flink](https://flink.apache.org/)。运营遥测技术跟踪了服务于数百万租户的 10 多个云产品中的用户操作，每天产生数十亿个事件。

头条说明了一切：他们将事件到指标的*指标*（套娃式地讲）从 40 多秒缩短到了 10 秒以内。

然而，Biswas 很坦诚：“这不是一个完美无瑕的成功故事。”他们仍在致力于微调。例如，回溯率在 8 月份下降到了 64%。尽管如此，对于构建自动化事故检测和响应工作流的其他团队来说，它仍然是一个有用的蓝图。

*随着 Kubernetes 的演进，运行它的团队所面临的需求也在不断变化。首席赞助商* [*HPE*](https://www.hpe.com/us/en/products/software.html) *通过涵盖虚拟化、云管理、可观测性和自动化的软件，帮助团队应对这种复杂性。*

## **Argo CD 4.0 愿景规划启动**

KubeCon NA 将于 11 月 9 日星期一的同期会议日举办 [ArgoCon North America 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/)。这是一个为期一天、拥有双轨的活动，提供关于改进软件交付、管理数据和机器学习管道以及实现渐进式交付的实用想法。

ArgoCon 联席主席 Dan Garfield、Christian Hernandez 和 Katie Lamkin 在[周三的一篇 CNCF 博客文章](https://www.cncf.io/blog/2026/09/30/argocon-north-america-2026-what-to-expect-as-the-argo-community-looks-toward-cd-4-0/)中强调，该活动的举办正值社区开始启动 Argo CD 4.0 愿景规划进程之际。

他们将 ArgoCon（[其日程表在此实时发布](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/#about)）描述为“一个围绕用户当前正在构建的内容以及项目下一步发展方向进行连接的机会。”

## **Cycle 的 DevOps 控制平面充满科幻感**

“如果你几年前告诉我这存在，我会认为‘这是科幻小说，它不应该是真的’，”工程负责人 [Alexander Mattoni](https://www.youtube.com/watch?v=q4T7U32g7xk)在本周的一段[功能发布视频](https://youtu.be/q4T7U32g7xk?si=-mXwRXdDZj1IBGn9)中说道，展示了针对 DevOps 控制平面 Cycle 的[全新远程 MCP 服务器](https://cycle.io/blog/cycle-launches-mcp)。

此项发布基本上意味着 Cycle 用户可以通过兼容 MCP 的 AI 助手和编码工具，使用自然语言跨多云和混合环境来配置、编排和管理工作负载。

这是云原生行业中发布的一系列智能体化功能中的最新一项，这些功能不断抽象 DevOps 并将令人惊叹的功能融入提示词中。昨天的科幻小说正越来越多地成为今天的常态。

## **关注通往 KubeCon 之路**

*通往 KubeCon 之路由 HPE 呈现，是盐湖城 KubeCon + CloudNativeCon North America 的八部分系列文章。在您出发之前，探索* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *如何帮助 IT 团队以更少的复杂性做更多的事情。*

228 个 [CNCF 项目](https://www.cncf.io/)。[最新 Kubernetes 版本](https://kubernetes.io/blog/2026/08/26/kubernetes-v1-37-release/)的 1,754 名独立贡献者。预计 KubeCon NA 2026 将有超过 230 家赞助商和参展商……

云原生生态系统正在蓬勃发展。因此，总有各种事情在发生。

在 KubeCon NA 之前，我们每周五都会在这里的 *The New Stack* 上进行追踪。

这意味着，在我们于展会上会面之前，仍有几期内容和短讯需要撰写。

如果您在云原生领域工作且有有趣的内容想要分享，本系列文章的作者 [Bill Doerrfeld](https://www.doerrfeld.io/) 随时欢迎投稿。您可以通过他的[个人联系页面](https://www.doerrfeld.io/contact)分享新闻、故事想法或引言。

如果您错过了上周关于 [OpenTelemetry 和 Prometheus 互操作性](https://thenewstack.io/opentelemetry-prometheus-observability-interoperability/)的期数，可以在这里补看。

您还可以关注通往 KubeCon 之路的[系列文章归档](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)。