<!--
title: 云原生十年：从CNCF到疫情，再到人工智能
cover: https://cdn.thenewstack.io/media/2025/03/e6a51855-winston-chen-zaktivjw2om-unsplashb.jpg
summary: 云原生十年巨变！从 CNCF 成立到疫情爆发，再到 AI 浪潮，Kubernetes 等技术飞速发展。云原生已成 AI 基础设施底座，并被 AI 赋能，如大规模 LLM 训练、AI 模型编排等。拥抱云原生，决胜 AI 时代！
-->

云原生十年巨变！从 CNCF 成立到疫情爆发，再到 AI 浪潮，Kubernetes 等技术飞速发展。云原生已成 AI 基础设施底座，并被 AI 赋能，如大规模 LLM 训练、AI 模型编排等。拥抱云原生，决胜 AI 时代！

> 译自：[A Decade of Cloud Native: From CNCF, to the Pandemic, to AI](https://thenewstack.io/a-decade-of-cloud-native-from-cncf-to-the-pandemic-to-ai/)
> 
> 作者：Richard MacManus

本周是我在 The New Stack 工作的五周年纪念日。 当我于 2020 年 3 月的最后一周开始工作时，我必须快速适应“[云原生](https://thenewstack.io/cloud-native/what-is-cloud-native-and-why-does-it-matter/)”世界。 什么是 Kubernetes，为什么每个人都在谈论它， “serverless”到底是什么意思，CI/CD 这个缩写代表什么，什么是“微服务”？

这并不是说我是个技术新手——我于 2003 年创立了先锋科技博客 [ReadWriteWeb in 2003](https://cybercultural.com/p/002-the-early-years-of-readwriteweb/) 并一直运营到 2012 年。在 RWW 之后，我继续沉浸在互联网技术（特别是开放网络）中，但我不再关注云计算和 Docker 容器等企业趋势。 所以我完全错过了 2010 年代中期的“新事物”。

## CNCF 于 2015 年成立

但我的前 RWW 同事之一并没有错过。 Alex Williams 在注意到 Docker 和容器技术从根本上改变了企业 IT 之后，[于 2014 年创立了 The New Stack](https://thenewstack.io/happy-birthday-the-new-stack-turns-10-and-judy-retires/)。 然后，当 Linux 基金会 [宣布成立云原生计算基金会](https://www.cncf.io/announcements/2015/06/21/new-cloud-native-computing-foundation-to-drive-alignment-among-container-technologies/) (CNCF) 于 2015 年 7 月 21 日成立时，Alex 和早期的 TNS 团队完美地定位为这场运动的默认媒体公司之一（类似于 ReadWriteWeb 在 2005 年左右 Web 2.0 兴起时在正确的时间出现在正确的地点）。

CNCF 的成立开启了利润丰厚的“云原生”时代，新组织将其定义为“容器打包、动态调度和面向微服务的应用程序或服务”。 Kubernetes 本身[去年 6 月满 10 周岁](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)，是 CNCF 成立时的关键项目。 当时 Kubernetes 被描述为“开源集群调度器”，由 Google 作为种子技术捐赠给该基金会。

![CNCF website 2015](https://cdn.thenewstack.io/media/2025/03/b0ec6c9f-cncf-website-2015.jpg)

CNCF 网站 2015；[通过 Wayback Machine](https://web.archive.org/web/20150905202410/https://cncf.io/)

## 扩展时机

从 2020 年 3 月开始在 TNS 工作几周后，我已经习惯了新的术语和缩写。 我甚至准备好对云原生发表一些看法！ [我在 4 月份的首篇文章](https://thenewstack.io/the-2020s-will-be-about-scale-out-data/) 宣称，如果 2000 年代“是网络发展的时代，2010 年代是计算的时代，那么 2020 年代将见证横向扩展数据的革命。”

横向扩展 *什么*？ 哦，我的意思是“数据层的革命”，我在开篇段落中做了有益的澄清。 实际上，我是从 DataStax 首席战略官 Sam Ramji 那里抄来的，他最近在 TNS 网络研讨会上使用了类似的措辞。 至于“横向扩展”，这是我必须习惯的另一个奇怪的新术语； 它意味着通过添加更多机器来为应用程序增加更多功能。 “当然，横向扩展是我们现在生活的云原生世界的基石，”我明智地补充道。

当然，我是在即兴发挥。 但我也开始明白 2020 年代的发展方向：“数据层”将是未来十年计算的关键。 Ramji 甚至在会议期间提到了 AI 和机器学习。 显然，这是在生成式 AI 几年后爆发之前，但 Ramji 在某种程度上说对了，他说在未来十年里，“有机会让数据变得非常容易、非常易于管理，并为未来的应用程序创建一个游乐场，其中包括 AI 和 ML 应用程序。”

## 2020 年的疫情反弹

我在 TNS 开始工作时另一个值得注意的事情？ 在我的国家（新西兰）因 COVID-19 进入全面封锁状态几天后。 正如你们许多人会记得的那样，2020 年 3 月是 [疫情加剧的时候](https://thenewstack.io/positive-signs-of-a-better-world-to-come/)，导致世界许多地方的封锁。 我们都必须习惯 [在家工作](https://thenewstack.io/the-network-impact-of-the-global-covid-19-pandemic/)（WFH 很快成为一个*新的*流行缩写）。 实际上，The New Stack 已经是一家虚拟公司，而我自己到那时已经在家里工作了大约 15 年。 所以 WFH 对我来说并不新鲜——但对其他数百万人来说却是新鲜事物，因此它突然增加了对云原生技术的需求。

正如 TNS 贡献者 Mark Hinkle [在 2020 年 6 月](https://thenewstack.io/putting-hybrid-and-multi-into-cloud-native/)撰文写道：“当前的经济环境点燃了许多 IT 和应用程序团队积极迁移到云端的火焰。这些举措在 COVID-19 之前就已经在进行中，但现在它们已被加速。”

疫情期间流行的一句口头禅是“数字化转型”，对于企业 IT 部门而言，这通常意味着转向 [云原生技术](https://thenewstack.io/cloud-native/)。The New Stack 的 Lawrence Hecht [在 2021 年 5 月报道](https://thenewstack.io/did-kubernetes-get-a-covid-bounce/)说，“超过三分之二 (68%) 的 IT 专业人士认为，由于疫情，他们 500 多名员工的公司对 Kubernetes 的使用有所增加”（他引用的是 Pure Storage 旗下 Portworx 2021 Kubernetes 采用调查的数据）。

![](https://cdn.thenewstack.io/media/2021/05/494cacb5-pandemic-k8s.png)

即使到 2021 年 3 月，[Zoom 疲劳](https://thenewstack.io/this-cant-be-normal-the-tech-industry-after-a-year-of-burnout/)已经完全出现，但云原生平台仍在继续壮大。那一年有很多关于“多云”的讨论，甚至导致伯克利教授 Ion Stoica（也是 Databricks 和 Anyscale 的联合创始人）提出了一项提案，将云计算变成一种真正的实用工具。他和他的同事 Scott Shenker 创造了“[天空计算](https://thenewstack.io/sky-computing-the-next-era-after-cloud-computing/)”一词——意味着云平台之上的一个层，以实现 Google、Microsoft 和 AWS 等大型厂商的云之间的互操作性。

天空计算只是使云原生技术更易于 **developers** 使用的持续努力之一。近年来，我们还看到了基于 Web 的技术，如 [WebAssembly](https://thenewstack.io/webassembly/what-is-webassembly/) 和 [云开发者平台](https://thenewstack.io/why-cloud-ides-are-shifting-to-a-platform-as-a-service-model/) 的出现。这些进一步加强了云原生工具集并使其大众化（Web 是最终的 [民主互联网平台](https://thenewstack.io/why-developers-should-experiment-with-the-fediverse/)）。

## 2025 年云原生技术发展到了什么程度？

毋庸置疑，在过去的几年里，人工智能彻底改变了云原生生态系统——就像它对其他所有技术领域所做的那样。在 [2022 年生成式人工智能出现](https://thenewstack.io/top-5-internet-technologies-of-2022/)之后，几乎所有的云原生产品现在都集成了人工智能。

CNCF 的旗舰会议 KubeCon [即将到来](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)。看看这个 [预定会议](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/program/schedule/)的示例，了解人工智能对云原生技术的影响：

- Production-Ready LLMs on Kubernetes: Patterns, Pitfalls, and Performance
- Orchestrating AI Models in Kubernetes: Deploying Ollama as a Native Container Runtime
- Optimizing Training Performance for Large Language Model(LLM) in Kubernetes
- A Practical Guide To Benchmarking AI and GPU Workloads in Kubernetes
- AI Pipelines With OPEA: Best Practices for Cloud Native ML Operations

正如 CNCF 首席技术官 Chris Aniszczyk 在他的 [2024 年回顾文章](https://www.cncf.io/blog/2025/01/29/2024-year-in-review-of-cncf-and-top-30-open-source-project-velocity/) 中所说，人工智能主要用于云原生世界中，以“支撑大规模人工智能基础设施”。但它也被用于自动化许多云原生工具——请参阅 [CNCF 最近的这篇博文](https://www.cncf.io/blog/2025/03/24/reimagining-log-management-tools-and-software-the-impact-of-ai-and-genai/)，了解“人工智能驱动的方法如何将日志管理工具转变为‘智能助手’”。

鉴于云原生技术既 *为* 人工智能 *提供动力*，又越来越多地 *由* 人工智能 *提供动力*，可以肯定地说，云原生生态系统已经很好地适应了我们现在所处的 AI 时代。