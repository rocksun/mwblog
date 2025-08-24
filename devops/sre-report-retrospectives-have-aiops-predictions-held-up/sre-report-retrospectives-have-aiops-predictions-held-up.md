
<!--
title: SRE 报告回顾：AIOps 预测是否经受住了考验？
cover: https://cdn.thenewstack.io/media/2025/08/b93d26f7-srereport.png
summary: 本文回顾了Catchpoint SRE报告对AIOps的预测，指出早期从业者对其价值持怀疑态度，但2024年10月后，因Gartner报告、IBM和诺基亚等公司的行动，AIOps的搜索兴趣激增。报告强调将AIOps分解为组件、关注实际用例和投资培训的重要性，并邀请读者参与2025年SRE调查。
-->

本文回顾了Catchpoint SRE报告对AIOps的预测，指出早期从业者对其价值持怀疑态度，但2024年10月后，因Gartner报告、IBM和诺基亚等公司的行动，AIOps的搜索兴趣激增。报告强调将AIOps分解为组件、关注实际用例和投资培训的重要性，并邀请读者参与2025年SRE调查。

> 译自：[SRE Report Retrospectives — Have AIOps Predictions Held Up?](https://thenewstack.io/sre-report-retrospectives-have-aiops-predictions-held-up/)
> 
> 作者：Leo Vasiliou, Denton Chikura

每年，Catchpoint 都会在其 [SRE 报告](https://www.catchpoint.com/asset/2025-sre-report) 中尝试捕捉全球可靠性社区的脉搏。它调查了全球数百名站点可靠性工程师 (SRE)、可靠性工程师和运营负责人，[以了解该职业的现状：](https://www.catchpoint.com/sresurvey2025?&utm_source=alert_banner&utm_medium=referral&utm_campaign=Content-2025-07-hosted-SRE-Survey&utm_content=survey) 所面临的挑战、使用的工具和塑造实践的趋势。这些报告既可以作为行业现状的快照，又可以作为行业发展方向的指南针。

但关于预测，有一点需要注意：它们有一个令人讨厌的习惯，那就是容易过时。技术不断发展，市场不断变化，三年前看起来具有革命性的东西，今天可能正在某个人的 Kubernetes 集群的角落里积满灰尘。

因此，作为 SRE 报告的作者，我们认为重新审视我们过去的观点，看看它们在残酷的生产环境现实中表现如何，这将是一件引人入胜——或许也有点令人谦卑的事情。

虽然 SRE 报告涵盖了广泛的主题，从混沌工程到监控最佳实践，但在这篇文章中，我们将重点关注 [AIOps](https://thenewstack.io/what-is-aiops-and-why-you-should-care/)，这是 2021 年报告中首次探讨的主题。它已成为 IT 运营中讨论最多、争论最多，有些人甚至认为是变革性的概念之一。那么，那些早期的预测表现如何呢？

## **AIOps：永不消逝的承诺**

让我们从一段历史开始。Garner 在 2017 年创造了“AIOps”一词，将其定义为将人工智能和机器学习 (ML) 应用于通过大数据、分析和自动化 [增强 IT 运营](https://thenewstack.io/why-aiops-failed-and-event-intelligence-solutions-are-different/)。Gartner 将其定位为 IT 运营的未来——一种处理传统监控工具根本无法管理的呈指数级增长的数据量、速度和多样性的方法。

这个承诺非常诱人：想象一下，人工智能系统可以自动检测异常，[在您的整个堆栈中](https://thenewstack.io/devops-embraces-observability-across-stacks-for-llm-era/) 关联事件，在故障发生之前预测故障，甚至无需人工干预即可修复问题。这听起来像是运营的圣杯。最终，我们可以从被动的救火转变为主动的、智能的基础设施管理。

## **我们当时说了什么：SRE 报告对 AIOps 的看法**

### **2021 年：谨慎乐观与冷酷现实相遇**

[2021 年 SRE 报告](https://pages.catchpoint.com/hubfs/Report/Catchpoint-2021-SRE-Report.pdf?_gl=1*jj0tkv*_gcl_au*MzE4OTA3NDc5LjE3NTE0NTAzNDk.) 给予了 AIOps 相当大的关注，反映了我们当时在各处看到的行业热情。潜力是不可否认的——AIOps 有望帮助 SRE 管理不断增加的数据量，并提取可操作的见解，从而改变我们处理监控和事件响应的方式。

但有趣的是：虽然业界对此兴奋不已，但调查受访者讲述了一个不同的故事。SRE 在现实世界中的采用速度出人意料地缓慢。承诺与实践之间的差距很大。

[![监控工具使用情况：2021 年 SRE 报告](https://cdn.thenewstack.io/media/2025/08/ca61e7a0-image2a-1016x1024.png)](https://cdn.thenewstack.io/media/2025/08/ca61e7a0-image2a-1016x1024.png)

监控工具使用情况：2021 年 SRE 报告。

该报告当时的建议是务实的：将 AIOps 分解为各个组件，而不是追逐流行语。不要全盘接受炒作；相反，单独评估特定功能，如异常检测、事件关联或自动修复。该报告还强调了 SRE 团队内部进行 AI 和 ML 培训的必要性，将其定位为一项长期投资，而不是一种快速解决方案。

### **2023 年：情节加深**

[![2023 年 SRE 报告](https://cdn.thenewstack.io/media/2025/08/7c196688-image3-1024x561.png)](https://cdn.thenewstack.io/media/2025/08/7c196688-image3-1024x561.png)

在 [2023 年 SRE 报告](https://resources.catchpoint.com/hubfs/eBooks/SRE%20Report%202023%20Catchpoint.pdf?_gl=1*2gzok6*_gcl_au*MzE4OTA3NDc5LjE3NTE0NTAzNDk.) 发布时，我们有了更多的数据可以利用。我们连续第二年要求受访者对 AIOps 的“收到的价值”进行评分，结果令人大开眼界。

大多数可靠性从业者继续报告说，他们从 AIOps 收到的价值很低或不存在。但真正有趣的是：当我们按组织级别细分回复时，出现了一种有趣的模式。59% 的高管表示他们从 AIOps 收到了中等或高的价值，而只有 20% 的个人从业者表示相同。

请再读一遍。让它沉淀一下。

[![从 AIOps 收到的价值：2023 年 SRE 报告](https://cdn.thenewstack.io/media/2025/08/356c15bd-image4a-1024x781.png)](https://cdn.thenewstack.io/media/2025/08/356c15bd-image4a-1024x781.png)

*从 AIOps 收到的价值：2023 年 SRE 报告。*

我们遇到了一个典型的案例，即做出购买决策的人看到了巨大的价值，而实际在生产中使用这些工具的人却 Largely 印象不深刻。[领导者和从业者之间的认知差距](https://www.catchpoint.com/blog/sre-report-2023-are-we-aligned-yes-no-maybe) 是显而易见的。

该报告的建议仍然一致：不要完全忽略 AIOps，而是将其分解为能够有意义地支持您的可观测性和可靠性运营的特定功能。专注于务实的用例，而不是供应商的承诺。

### **2024-2025 年：转向**

到 2024 年，发生了一些有趣的事情。我们将调查问题从专门针对 AIOps 扩展到了一般人工智能，并添加了关于“未来两年内”的期望的限定语。这种转变反映了快速发展的人工智能领域和生成式人工智能 (GenAI) 的兴起。

正如我们的一位现场贡献者所指出的：“很难知道这是否是另一次人工智能炒作周期，还是前一次炒作周期的加强，但感觉 AIOps（相当缺乏细节）的推广与 GenAI 正在发生的事情之间存在着真正的不同。”

这种区分至关重要：传统的 AIOps 仍然狭隘地专注于现有指挥控制框架内的异常检测和分析——本质上是“一切照旧，只是速度更快”。然而，GenAI 代表着一些根本不同的东西：“更像是与一位非常早期的同事打交道，他需要培训和投资以及不断的审查，但偶尔会非常有价值。”

## **过去是过去，现在是现在：Google Trends 现实检验**

以上就是来自 SRE 一线的看法。但是，您如何在更广泛的市场中实际衡量像 AIOps 这样的东西的采用率呢？虽然有些粗略，但看看 [Google](https://cloud.google.com/?utm_content=inline+mention) 搜索趋势数据总比什么都不做好。

为什么要看 Google Trends？有两个令人信服的理由：

* 首先，它跟踪真实的搜索兴趣，而不仅仅是炒作。Google Trends 显示有多少人正在积极搜索有关某个主题的信息——这是了解市场、专业人士和想要学习或评估的好奇者的一扇直接窗口。
* 其次，它是公正且供应商中立的。与供应商调查或分析师报告不同，Trends 是独立的。它不是由寻求销售或推广某些东西的利益相关者制作的。它反映了来自全球 [数百万用户](https://thenewstack.io/how-to-support-a-million-users-on-your-website-a-success-story/) 的自然搜索行为。

事情变得非常有趣了。

## **AIOps：我们从 Google 搜索趋势数据中学到了什么**

### “AIOps”搜索兴趣的爆炸式增长 (2024-2025)

最引人注目的发现是，从 2023 年底/2024 年初开始，“AIOps”搜索量急剧上升，到 2025 年达到峰值。

[![“AIOps”一词的全球 Google 搜索兴趣随时间的变化（2021 年 8 月 – 2025 年 8 月）](https://cdn.thenewstack.io/media/2025/08/70885b4f-image5a-1024x564.png)](https://cdn.thenewstack.io/media/2025/08/70885b4f-image5a-1024x564.png)

“AIOps”一词的全球 Google 搜索兴趣随时间的变化（2021 年 8 月 – 2025 年 8 月）。

请记住，这发生在我们的 SRE 社区已经得出结论认为 AIOps 提供的实际价值有限之后。

### 亚太地区的区域集中

[![基于全球 Google 搜索量的“AIOps”区域兴趣（2021 年 8 月 – 2025 年 8 月）](https://cdn.thenewstack.io/media/2025/08/75c68404-image6-1024x484.png)](https://cdn.thenewstack.io/media/2025/08/75c68404-image6-1024x484.png)

基于全球 Google 搜索量的“AIOps”区域兴趣（2021 年 8 月 – 2025 年 8 月）。

地理数据显示，AIOps 的兴趣主要集中在：

* 中国（100% 的相对兴趣）
* 新加坡、韩国和香港（13-21% 的相对兴趣）

这表明亚太市场存在不同的 IT 基础设施挑战、不同的技术采用模式，或者可能对 AI 驱动的运营有不同的期望。

### 教育曲线

[![“什么是 AIOps”一词的全球 Google 搜索兴趣随时间的变化（2021 年 8 月 – 2025 年 8 月）](https://cdn.thenewstack.io/media/2025/08/558d1c8b-image7-1024x556.png)](https://cdn.thenewstack.io/media/2025/08/558d1c8b-image7-1024x556.png)

“什么是 AIOps”一词的全球 Google 搜索兴趣随时间的变化（2021 年 8 月 – 2025 年 8 月）。

“什么是 AIOps”的搜索趋势显示出周期性的峰值，而不是持续的增长，这表明人们周期性地发现它，而不是持续地采用它。人们仍在学习 AIOps，而不是实施它。尽管业界讨论多年，但这个概念仍然处于起步阶段。

### **2024 年 10 月的拐点**

但故事真正有趣的地方就在这里。2024 年 10 月，对 AIOps 的搜索兴趣绝对是爆炸性的。

[![全球对“AIOps”的搜索兴趣的拐点——2024 年 10 月](https://cdn.thenewstack.io/media/2025/08/f7df4874-image8-1024x381.png)](https://cdn.thenewstack.io/media/2025/08/f7df4874-image8-1024x381.png)

全球对“AIOps”的搜索兴趣的拐点（2024 年 10 月）。

发生了什么？

### **完美的风暴**

2024 年 10 月为 AIOps 兴趣创造了完美的风暴：

* **Gartner 数字体验监控魔力象限报告（2024 年 10 月 21 日）：** Gartner 首次发布了数字体验监控魔力象限，其中包括作为评估标准的 AIOps 功能。Dynatrace 和 Catchpoint 等公司被评为领导者（是的，无耻的宣传，但我们当之无愧），引起了业界的广泛关注并验证了 AIOps 领域。
* **IBM Cloud Pak for AIOps v4.7 发布（2024 年 10 月 11 日）：** IBM 宣布了一项重大更新，其中包含可用于生产的 Linux 部署功能，这标志着企业已准备就绪。
* **诺基亚的 AIOps 集成（2024 年 10 月 18 日）：** 诺基亚将 AI 驱动的运营集成到其 Altiplano 接入控制器中，这表明 AIOps 正在从传统 IT 扩展到网络基础设施。
* **ServiceNow 的教育推动：** 专门的 AIOps 研讨会和培训，表明供应商正在大力投资于市场教育。
* **多个供应商里程碑：** 从 Motadata 的下一代平台到 Keep 为其开源 AIOps 平台筹集 270 万美元，整个生态系统似乎同时成熟。

这种融合解释了为什么 Google Trends 显示出如此急剧的增长。2024 年 10 月代表着 AIOps 从“新兴技术”转变为“主流企业解决方案”的时刻，多个验证点同时出现。

## 市场实际上说了什么？

这些数字令人印象深刻：[全球 AIOps 市场正在以超过 25% 的复合年增长率扩张](https://www.gminsights.com/industry-analysis/aiops-market)，预计将从 2025 年的 111.6 亿美元增长到 2029 年的超过 320 亿美元。目前，大约 40% 的企业在某种程度上采用了 AIOps，尤其是在受监管和数据密集型行业中，采用率特别高。

但现在的问题是：我们看到的是与从业者现实不符的炒作周期，还是 AIOps 的早期承诺最终正在实现？

## **我们做对了什么（以及我们错过了什么）**

我们 2021 年和 2023 年的建议仍然有效：

* **将 AIOps 分解为离散组件：** 市场在很大程度上验证了这种方法。成功的 AIOps 实施侧重于特定功能——异常检测、事件关联、自动修复——而不是试图一次解决所有问题。
* **专注于务实的用例：** 从 AIOps 中看到价值的组织是那些确定了清晰、可衡量的问题并有策略地应用 AI/ML 工具来解决这些问题的组织。
* **投资于培训：** 我们观察到的最成功的团队已经对其 SRE 团队的 AI 和 ML 素养进行了投资，将其视为一项长期能力，而不是灵丹妙药。

我们可能低估了市场成熟所需的耐心，以及更广泛的人工智能发展（尤其是 GenAI）在使 AIOps 功能合法化和推进 AIOps 功能方面所发挥的作用。

## **书写下一章**

AIOps（以及一般的 SRE）的故事仍在书写中。这就是为什么您的声音在 2025 年 SRE 调查中很重要。每个回复都有助于我们对趋势进行基准测试、发现新兴的最佳实践，并突出显示各种规模的组织中可靠性工作的实际情况。

今年，我们将更深入地研究性能和可靠性建模、混沌工程、可观测性实践、学习和技能提升以及工具战略。该调查是自愿的、匿名的，大约需要 10 分钟，但您的参与所产生的影响是深远的。

因为我们能够准确地反映今天的预测的唯一方法是，如果我们捕捉到全球生产环境中实际发生的真实情况。

[参加 SRE 调查](https://www.catchpoint.com/sresurvey2025?&utm_source=thenewstack&utm_medium=referral&utm_campaign=Content-2025-07-hosted-SRE-Survey&utm_content=survey)，帮助我们书写这个故事的下一章。