<!-- 
# 超越数字，衡量平台团队的成功
https://www.eficode.com/blog/measuring-success-beyond-numbers-in-platform-teams
 -->

译自 [MEASURING SUCCESS BEYOND NUMBERS IN PLATFORM TEAMS](https://www.eficode.com/blog/measuring-success-beyond-numbers-in-platform-teams) 。

# 第六部分

“平台团队的价值可以通过他们为产品团队提供服务的价值来衡量。” - Skelton， Matthew; Pais， Manuel， Team Topologies 

Dan Grøndahl Glavind 用 CTO 的视角，写了一系列七篇博客来讲述平台工程。

- [第一部分：假如我是 CTO ，我会这样推动平台工程](https://yylives.cc/2023/09/29/if-i-were-a-cto-id-approach-platform-engineering-like-this/)
- [第二部分：建立平台工程组织](https://yylives.cc/2023/10/01/establishing-a-platform-engineering-organization/)
- [第三部分：平台团队如何实现远大目标](https://yylives.cc/2023/10/01/how-platform-teams-can-achieve-ambitious-goals/)
- [第四部分：平台团队成功的箴言](https://yylives.cc/2023/10/01/a-mantra-for-platform-teams-to-succeed/)
- [第五部分：引导平台团队树立产品思维](https://yylives.cc/2023/10/01/navigating-the-product-mindset-in-platform-teams/)
- [第六部分：超越数字，衡量平台团队的成功](https://yylives.cc/2023/10/01/measuring-success-beyond-numbers-in-platform-teams/)
- [第七部分：平台团队的沟通、成就和挑战](https://yylives.cc/2023/10/01/communicating-achievements-and-challenges-in-platform-teams/)

## 传统指标的局限

在评估团队成功时，我们经常看到引入[DevOps研究与评估(DORA)](https://cloud.google.com/blog/products/devops-sre/dora-2022-accelerate-state-of-devops-report-now-out)指标。

对不了解的人来说，DORA指标包括部署频率和服务恢复时间等测量标准，被视为评估DevOps表现的行业标准。

从高层管理向团队强推这些指标，有时会适得其反。

为什么？因为有些团队担心“赤裸裸的指标”。 透明地被测量有一定脆弱性，特别是如果存在不利对比的可能。 坦白地说，没有团队喜欢与其他团队相比，特别是两者之间如比喻苹果和橘子一样。

不同部门都有自己的挑战，例如，DevOps团队与项目管理或[平台工程团队](https://www.eficode.com/platform-engineering)有不同重点。 每个团队都有独特优势。 因此，简单依据指标进行对比可能至少会产生误导，最糟是损害士气。

## 拥有软件交付中的指标

那么，如果自上而下地推行指标的传统方法并不理想，替代方案是什么？关键是平台团队要对自己的测量负责。

- **理解指标**：在采取任何行动之前，团队应该理解某些指标的重要性。 以DORA指标为例，[这篇谷歌云文章](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)对其进行了精彩阐释。 通过理解指标背后的理论依据，团队才能真正接受它们。
- **引入[SPACE](https://www.infoq.com/news/2021/03/space-developer-productivity/)指标**：Nicole Forsgren提出的SPACE代表满意度、表现、活动、社区和进化。 这些指标鼓励对成功采取更广泛的视角，兼顾技术和人文因素。
- **学习意见领袖**：意见领袖像[Abi Noda](https://dl.acm.org/doi/10.1145/3595878)提供洞察，指标如何成为真正的绩效指标，而不是惩罚工具。 智慧在于将测量视为路标，而不是禁行标志。

## 趋势胜过绝对值

如果平台团队一个月内提高部署频率10%，表面看似不错，但没有上下文很难评论。

这就是为什么趋势至关重要。 关注指标的绝对快照不如追踪其随时间的变化趋势。 正是这些轨迹提供了洞察，突出增长领域，展示真正的进步。

### 平台团队的示例指标

以下是评估平台团队效能和找出改进领域时可考虑的指标:

#### 1. 平台采用率:

描述:使用平台的产品团队占全部产品团队的比例。

计算:(使用平台的产品团队数量/全部产品团队数量) x 100。

重要性:更高的采用率可能表示平台的可用性、相关性和效能。 较低可能意味存在平台差距或改进空间。

#### 2. 平均引入时间(MTTO):

**描述**:产品团队从接触到积极使用平台的平均时间。

**计算**:所有产品团队引入时间总和/引入产品团队数量。

**重要性**:更短的MTTO表示平台直观易用且文档完备。 较长可能意味理解或支持材料不足。

#### 3. 平台服务可用性:

**描述**:平台提供的服务可靠性。

**计算**:(总时间 - 宕机时间)/总时间。

**重要性**:高可用性百分比表示平台健壮可靠，对依赖它的产品团队至关重要。

#### 4. 反馈循环时间:

**描述**:用户反馈到平台团队解决的平均时间。

**计算**:所有反馈回复时间总和/反馈数量。

**重要性**:更短反馈循环可能表示敏捷有效的平台团队，持续改进和提升用户满意度。

这些指标为平台团队提供性能和潜在关注领域的初步洞察。 记住关键不仅测量，还要基于这些洞察采取行动，促进成长和改进。

**提示**:[Backstage](https://backstage.io/docs/overview/adopting#kpis-and-metrics.)提供了开发者门户启用相关的指标和KPI，可以提供有价值的洞察。

## 指标不仅是仪表盘上的数字

指标讲述增长、挑战、胜利和学习的故事。 对平台团队来说，它们是指南针。 但记住，虽然指南针提供方向，团队谱写叙事。

将指标视为导航、启发和进化的工具，确保通往成功的道路可以测量且有意义。

这是平台工程系列博客的[最后一篇](https://www.eficode.com/blog/communicating-achievements-and-challenges-in-platform-teams) —— 传达平台团队的成就和挑战。
