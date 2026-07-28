<!--
title: Kimi K3风波：白宫指控 Moonshot 非法窃取 Fable 5 技术构建模型
cover: https://cdn.thenewstack.io/media/2026/06/e6bf2f29-eva-wahyuni-qn5hziknhlg-unsplash-scaled.jpg
summary: 白宫高层指控中国AI初创公司Moonshot通过非法手段窃取Anthropic公司Fable 5模型数据，用于训练Kimi K3。美方将此视为窃取知识产权，可能导致更严格的API访问限制及出口管制。
-->

白宫高层指控中国AI初创公司Moonshot通过非法手段窃取Anthropic公司Fable 5模型数据，用于训练Kimi K3。美方将此视为窃取知识产权，可能导致更严格的API访问限制及出口管制。

> 译自：[Kimi K3: White House alleges Fable 5 siphoning](https://thenewstack.io/moonshot-fable5-distillation-accusations/)
> 
> 作者：Amanda Caswell

白宫顶尖技术官员 Michael Kratsios 周三指控中国人工智能初创公司 Moonshot 采取欺骗手段，从 [Anthropic 高度先进的 Fable 5 模型](https://thenewstack.io/fable-5-permanent-subscription-access/)中提取数据，并据称利用这些输出结果来训练其新发布的 [Kimi K3 系统](https://thenewstack.io/kimi-k3-open-weight-coding/)。

尽管这些指控尚未得到公开可验证证据的支持，但其本身意义重大。同样值得注意的是白宫对其描述的方式。通过将大规模模型蒸馏定性为对美国技术的盗窃，而非一种竞争性的 AI 实践，美国政府发出了信号：它可能会采取更强硬的回应，从更严格的 API 限制到扩大对先进 AI 芯片的出口管制。

Kratsios 在 X 上的一篇帖子中声称，政府掌握的信息显示，Moonshot 使用了一个专门构建的平台和多种访问方法来规避检测，从而从 Fable 5 中窃取数据。

“旨在窃取美国专有技术并破坏美国研究的大规模、隐蔽的工业蒸馏是不可接受的，” Kratsios 表示。

Kratsios 还指控 Moonshot 采购了配备备受追捧的 Nvidia GB300 AI 芯片的服务器，并将其部署在泰国，“很可能是为了训练其 AI 模型。”

Moonshot、Anthropic 以及白宫科技政策办公室 (OSTP) 未能立即回应 The New Stack 的置评请求。

> “旨在窃取美国专有技术并破坏美国研究的大规模、隐蔽的工业蒸馏是不可接受的。”

## 将蒸馏作为贸易武器

要理解政府的指控，就必须了解当前较小 AI 模型是如何构建的。

简单来说，模型蒸馏是指利用大型、昂贵得多的“前沿”模型所生成的输出，来训练一个规模较小、成本较低的 AI 模型的过程。蒸馏本身是一种常见且被广泛接受的技术实践，用于降低从零开始训练新 AI 工具所带来的极端计算成本。

这里的争议不在于蒸馏的概念，而在于其执行方式。白宫指控 Moonshot 以欺骗手段访问 Fable 5——据称通过 Kratsios 所说的旨在规避检测的访问方法绕过了 Anthropic 的服务条款——并大规模获取专有输出结果。

关键问题仍未得到解答：有哪些具体的遥测数据支持政府的说法？Anthropic 是否在其自身的日志中独立识别或记录了这一活动？

政府的指控并非孤立存在。今年 2 月，Anthropic 公开指控 Moonshot、DeepSeek 和 MiniMax 针对 Claude 开展了协调一致的蒸馏行动，并将大约 24,000 个欺诈账户产生的超过 1600 万次交互归咎于这三家公司。仅 Moonshot 一家就与其中的 340 万次交互有关。

## Kimi K3 引发关注

Kratsios 的指控是在 K3 发布六天后提出的。7 月 16 日，这家中国 AI 初创公司发布了 [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/)，这是一个拥有 2.8 万亿参数的大型模型。Moonshot 将 K3 宣传为全球最大的开放权重 AI 系统，并声称其性能接近 Anthropic 的前沿模型 Fable 5。（完整的权重计划于 7 月 27 日发布，当时尚未公开提供下载。）

这种在能力上的明显接近立即引起了华盛顿的关注。Kimi K3 的发布距离美国政府发布出口管制指令（[迫使 Anthropic 在发布三天后暂时停止了对其 Fable 5 和 Mythos 5 模型的访问](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)，理由是国家安全担忧）大约五周。

Anthropic 从 7 月 1 日开始[恢复了 Fable 5 的全球访问权限](https://thenewstack.io/anthropic-fable-ban-lifted/)，并在 K3 发布前两周多，为获批的美国机构恢复了 Mythos 5。尽管如此，K3 的快速发布表明，中国的开放 AI 生态系统似乎正在以多快的速度缩小与重兵把守的美国系统之间的差距，从而引发了对这一差距如何被弥补的调查。

## 泰国的算力漏洞

Kratsios 关于 Moonshot 在泰国访问 Nvidia GB300 服务器的指控，凸显了美国政策制定者日益增长的担忧。限制芯片出口是一回事；阻止公司在其他国家租用算力则要困难得多。

如果这一说法属实，Moonshot 获得了或远程访问了位于泰国的 GB300 系统。这并不一定构成对美国出口管制的规避；该安排是否违反规则，取决于包括谁拥有这些系统、谁提供计算访问权限以及已获得哪些许可在内的因素。

中国的 AI 公司可能根本不需要将受限芯片带入中国。相反，他们可以租用泰国或中东等地的服务器访问权限，并远程利用该计算能力来运行大规模的蒸馏工作负载。

## 出口管制面临局限

Moonshot 的指控是政府针对涉嫌提取美国 AI 知识产权所开展的更广泛行动中的最新升级。

今年 2 月，OpenAI 警告美国立法者，DeepSeek 正在积极瞄准美国领先的 AI 实验室以复制其模型。此后，美国国务院在 4 月下旬发起了一场全球外交攻势。据路透社看到的一份外交电报显示，国务院试图提醒盟友注意中国公司——明确点名 Moonshot AI——通过大量窃取美国实验室知识产权的行为。

“通过隐蔽、未经授权的蒸馏活动开发的 AI 模型，使外国行为体能够发布在选定基准上看起来表现相当、成本却只有几分之一的产品，但它们并未复制原始系统的全部性能，” 4 月份的电报指出。

> “通过隐蔽、未经授权的蒸馏活动开发的 AI 模型，使外国行为体能够发布在选定基准上看起来表现相当、成本却只有几分之一的产品，但它们并未复制原始系统的全部性能。”

无论这些指控最终是否被证实，它们都可能加速华盛顿已经在讨论中的政策倡议。像 Anthropic 和 OpenAI 这样的美国模型开发商可能会面临收紧 API 访问权限的压力，使企业更难为大规模蒸馏创建代理账户。

商务部还可能通过更直接地针对泰国等国家的远程云服务访问来扩大出口管制，限制他们向中国公司出租 Nvidia GPU 集群的能力。

> 限制芯片出口是一回事；阻止公司在其他国家租用算力则要困难得多。

除此之外，一种情况是政府可能会对它认为参与其中的 Moonshot 或其他组织实施制裁，同时推动盟国更密切地监控其境内的人工智能训练活动，并报告潜在的违反美国出口管制的行为。

目前，科技行业正在等待政府是否会发布技术凭证来支持 Kratsios 的说法，或者这种言论是否仅仅是下一轮 AI 贸易战的借口。