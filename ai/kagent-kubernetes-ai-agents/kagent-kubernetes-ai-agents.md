<!--
title: AI智能体将单次请求放大20倍，Kubernetes正加速演进应对挑战
cover: https://cdn.thenewstack.io/media/2026/10/9a261836-getty-images-u0axzkvx1qg-unsplash-scaled.jpg
summary: 本文探讨了AI智能体如何将单个请求放大约20倍并给网络带来压力，以及Kubernetes等云原生技术如何通过架构演进、专用沙箱项目和新型工具来应对这一挑战。
-->

本文探讨了AI智能体如何将单个请求放大约20倍并给网络带来压力，以及Kubernetes等云原生技术如何通过架构演进、专用沙箱项目和新型工具来应对这一挑战。

> 译自：[AI agents turn one request into about 20. Kubernetes is evolving to handle it.](https://thenewstack.io/kagent-kubernetes-ai-agents/)
> 
> 作者：Bill Doerrfeld

**欢迎阅读新一期的** [**Road to KubeCon**](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)，我们将在此倒计时迎接将于11月9日至12日在犹他州盐湖城举行的 [KubeCon + CloudNativeCon NA 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)，并持续追踪云原生和 Kubernetes 生态系统中的有趣动态。

在本期内容中，我们将正式邀请一些关键的云原生参与者接受访谈。我们还将报道 HPE Morpheus Software 的全新 SUSE 验证，以及今年平台工程日（Platform Engineering Day）的亮点。

此外，我们还将了解一个用于将智能体作为 Kubernetes 资源运行的新（ish）CNCF 沙箱项目、关于分配 Kubernetes 合规所有权的探讨，以及一个在实践中 *不应* 使用 Kubernetes 的故事。

## **HPE Morpheus Software 增加 SUSE 验证**

如果您是同时使用 [SUSE](https://www.suse.com/) 的 HVM 虚拟机监控程序（hypervisor）用户，那您就走运了：[HPE Morpheus Software](https://www.hpe.com/us/en/products/software/morpheus-software.html) 现在已正式获得 SUSE 认证，这意味着该虚拟机监控程序现在可以支持 SUSE Linux Enterprise Server (SLES) 16。

*Hewlett Packard Enterprise (HPE) 是 Road to KubeCon 的首席赞助商。* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *帮助 IT 组织在混合、多供应商环境中实现基础设施现代化、简化运维并加速 AI 计划。*

为什么 SUSE 验证很重要？根据 [HPE 的公告](https://community.hpe.com/t5/the-cloud-experience-everywhere/hpe-morpheus-software-earns-suse-certification-expanding/ba-p/7273260)，“操作系统验证在降低部署风险和确保生产环境中的可预测结果方面发挥着关键作用。”这一验证标志着成熟度，并赋予了运维人员更多信心。

这一新进展正值部分企业在混合云资产中艰难平衡、寻找统一方式来管理其虚拟机基础设施之际。

## **平台工程日迎来“智能体化”**

自 2024 年以来，平台工程大会一直与 KubeCon + CloudNativeCon 活动同期举行，今年也不例外。[平台工程日](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/platform-engineering-day/?__hstc=60185074.6ca1230192cfed092778db269d3ad7b2.1791537489880.1792105130187.1792108003203.4&__hssc=60185074.2.1792108003203&__hsfp=81938ec6db9d2925038039e9f02af3cc) 将作为一场同期活动，于 11 月 9 日星期一在 KubeCon + CloudNativeCon NA 2026 期间举办。

正如 [Paula Kennedy](https://www.linkedin.com/in/paulalkennedy/)、[Stacey Potter](https://www.linkedin.com/in/staceympotter/) 和 [Ramiro Berrelleza](https://www.linkedin.com/in/ramiroberrelleza/) 在 [CNCF 博客](https://www.cncf.io/blog/2026/10/09/join-platform-engineering-day-at-kubecon-cloudnativecon-north-america-2026/)中分享的那样：“自成立以来，目标始终很简单：创建一个让平台工程师和从业者能够相互学习的空间。”他们补充说，分享反模式以及解释做出决策的*原因*，与分享成功经验同样重要。

根据 [已发布的议程](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/cncf-hosted-co-located-schedule/?all-sessions=platform-engineering-day)，与会者可以期待融合了终端用户故事、主旨演讲、闪电演讲和小组讨论的丰富内容，其中强烈聚焦于作为内部开发者平台（IDP）的生产者和消费者的智能体。

## **智能体与 Kubernetes 的正式相遇**

AI 顾问兼架构师 [Luca Berton](https://www.linkedin.com/in/lucaberton/) 最近开启了一个有趣的系列访谈 *[Udienza](https://www.udienza.com/)*。“Udienza”在意大利语中意为与平时难以见到的某人会面。剑桥词典将其定义为“与重要人物的正式采访”。
  
到目前为止，Berton 的系列访谈一直坚守这一定义，其中包含与云原生和 AI 基础设施领域领袖的简短对话，包括 [Luca Galante](https://www.udienza.com/episodes/luca-galante)、[Chris Aniszczyk](https://www.udienza.com/episodes/chris-aniszczyk)、[Kat Cosgrove](https://www.udienza.com/episodes/kat-cosgrove)、[Manik Surtani](https://www.udienza.com/episodes/manik-surtani) 等人。

他 [最近的采访](https://lucaberton.com/blog/oss-europe-2026-cncf-bob-killen-daniel-krook-interview/) 邀请到了 CNCF 主管 [Bob Killen](https://www.linkedin.com/in/mrbobbytables) 和 [Daniel Krook](https://www.linkedin.com/in/krook/)。一个核心观点是，Kubernetes 正在成为 AI 的操作系统，并作为构建在其之上的、解决特定问题的一系列更新项目的默认基础层。

他们还承认了智能体带来的全新流量压力，指出单个用户的请求可能会触发大约 20 个智能体请求。此外，智能体期望获得 200 毫秒以下的响应，而一个新的 Kubernetes pod 启动通常需要大约一秒钟的时间。

为了缩小这一差距，他们重点介绍了贯穿整个技术栈的新兴项目，例如用于分布式 LLM 推理的 [llm-d](https://llm-d.ai/)，以及用于大规模智能体部署的运行时 [Agent Substrate](https://github.com/agent-substrate/substrate)。

## **无人愿接手的烫手山芋：Kubernetes 合规性**

“安全团队可以编写策略。安全团队无法合并 Helm chart。”

这是来自 [Reevo](https://www.reevo.it/it/) 的 [Matteo Bisi](https://www.linkedin.com/in/matteobisi/) 在上周五发布的一篇 [CNCF 博客文章](https://www.cncf.io/blog/2026/10/09/who-owns-nis2-and-dora-on-a-kubernetes-platform-team/)中的观点。他切中了一个许多组织都无法给出清晰答案的普遍问题：谁来负责合规性？具体而言，谁来确保 Kubernetes 平台满足诸如 [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) 和 [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) 等欧盟法规的要求？

正如开篇引言所暗示的那样，Bisi 认为云原生运维人员大有可为。他主张创建“可追溯性链条”，允许风险、法务和安全团队定义范围、控制要求和所需证据，然后将特定的产出物、冲刺（sprint）事项和日常运维交接给平台和应用团队。

通过明确各方的职责分工，合规性将不再是一个未解决的瓶颈，而是演变为应对这些框架的攻击计划，同时也为未来的合规框架提供了可复制的交接流程。

*随着 Kubernetes 的不断演进，运行它的团队所面临的要求也在不断提高。首席赞助商* [*HPE*](https://www.hpe.com/us/en/products/software.html) *通过涵盖虚拟化、云管理、可观测性和自动化的软件，帮助团队应对这种复杂性。*

## **在 Kubernetes 上启动智能体正变得司空见惯**

在 Kubernetes 上运行智能体正开始变得像基础设施的其他部分一样平常。[kagent](https://kagent.dev/) 是一个有趣的 CNCF 沙箱项目，它将 AI 智能体作为 Kubernetes 自定义资源运行。一篇新教程展示了这一过程变得多么常规，它使用 kagent 构建了一个能够构建其他智能体的智能体。

来自 [Solo.io](https://www.solo.io/) 的 [Antonio Berben](https://sessionize.com/antonio-berben) 和来自 [Telefónica](https://www.telefonica.com/) 的 Felipe Vicens 在周一发布的 [CNCF 博客文章](https://www.cncf.io/blog/2026/10/12/from-zero-to-agent-builder-running-kagent-on-your-laptop/)中写道：“你只需编写一个带有系统提示词、模型和工具列表的 Agent。应用它之后，控制器就会将其转换为一个运行中的、支持 A2A 通信的 pod。”

该演练是在一台笔记本电脑上通过 [Ollama](https://ollama.com/) 运行本地模型来完成的（kagent 还支持托管提供商，如 OpenAI、Anthropic、Azure OpenAI 和 Gemini），不过作者发现较小的模型很难生成有效的清单。该构建器受到三个工具的白名单限制，在应用任何内容之前需要人工批准，并且使用仅允许其编写 Agent 资源的 RBAC。你可以通过 kagent 的 UI 或其 A2A API 来驱动它。

## **一个关于何时 *不应* 使用 Kubernetes 的故事**

周二在瑞典斯德哥尔摩举行的 2026 年 [Nordic APIs 峰会](https://nordicapis.com/events/platform-summit-2026/)上，[Bauer Media Outdoor UK](https://www.bauermediaoutdoor.co.uk/) 的软件开发人员 [Faith Sodipe](https://www.linkedin.com/in/sodipefaith/) 发表了一场可能会让某些坚定的 Kubestronauts（Kubernetes 爱好者）感到冒犯的演讲。

在题为《你其实不需要 Kubernetes：我们如何在没有基础设施表演的情况下扩展 API 层》的演讲中，Sodipe 将 [基础设施表演（infrastructure theater）](https://www.linkedin.com/posts/doerrfeldbill_nordicapis-activity-7515731670164090880-W34d?utm_source=share&utm_medium=member_desktop&rcm=ACoAAA-8zTABlsmtYe-zC-Uf5z3oD5nm6qXDVVo) 定义为“为了追求规模感的外表而构建，而非为了实际的规模需求”。平台团队往往会构建与生产环境的实际需求不成比例的宏大规模。

Bauer Media Outdoor UK 的数据摄取系统每天处理近百万个事件，并伴有突发流量和可变的有效载荷大小。在这种规模下，更好的系统设计（解决连接池耗尽、缓存击穿和慢查询问题）比沉重的容器编排更为重要。该团队使用 [Docker](https://www.docker.com/) 进行了容器化，但完全跳过了 Kubernetes。

正如 Sodipe 在 [LinkedIn 上的总结](https://lnkd.in/p/gMKy56JF)：“我的信息很简单：解决实际的问题，而不是你假设存在的问题。”

## **厂商观点：AI 编程正在演进平台工程**

既然 AI 编程智能体已经无处不在，平台工程是否变得不那么重要了？[OpenTofu](https://opentofu.org/)（开源 [Terraform](https://developer.hashicorp.com/terraform) 替代方案）的早期推动者之一、内部开发者平台（IDP）[Massdriver](https://www.massdriver.cloud/) 的首席执行官兼联合创始人 [Cory O’Daniel](https://www.linkedin.com/in/coryodaniel) 告诉 The New Stack，编程智能体让平台工程变得更加重要，而非相反。然而，围绕 IDP 的基础设施必须不断演进。

O’Daniel 表示：“我看到的架构转变是从基础设施即代码（IaC）向基础设施即数据（IaD）的转变。”他说，这并不是要取代 Terraform、OpenTofu 或 Git，而是将基础设施表示为一个由资源、依赖关系、所有权、环境和策略构成的可查询图谱。

以这种方式提供服务可以帮助智能体更高效地消费基础设施信息。此外，他表示，既然任何人都可以创建和发布内容，那么比以往任何时候都更需要额外的控制。“护栏正在成为运维部门仅存的唯一控制手段。”

## **关注 Road to KubeCon**

*Road to KubeCon 是由 HPE 呈现的八部分系列报道。在您出发之前，请探索* [*HPE Software*](https://www.hpe.com/us/en/products/software.html) *如何帮助 IT 团队以更低的复杂性实现更多目标。*

Road to KubeCon 将在 KubeCon 召开前的每周五在 *The New Stack* 上与您见面。您可以在 [Road to KubeCon 存档页面](https://thenewstack.io/kubecon-cloudnativecon-na-2026/road-to-kubecon/)上了解最新发布的内容。

本文作者 [Bill Doerrfeld](https://www.doerrfeld.io/) 欢迎社区投稿。您可以通过他的 [联系页面](https://www.doerrfeld.io/contact) 发送您的 PR、简讯、犀利观点或云原生预测。