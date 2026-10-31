<!--
title: Mistral开源大模型Large 4发布：编程能力领先GLM-5.3一个百分点
cover: https://cdn.thenewstack.io/media/2026/10/c4e85706-resource-database-8y0cqyxbfce-unsplash-scaled.jpg
summary: Mistral AI正式发布开源大模型Mistral Large 4 (ML4)，在编程和网络安全基准测试中以极低成本微超GLM-5.3。高管强调开源权重对企业的重要性，并透露未来将推出适合笔记本运行的轻量化版本。
-->

Mistral AI正式发布开源大模型Mistral Large 4 (ML4)，在编程和网络安全基准测试中以极低成本微超GLM-5.3。高管强调开源权重对企业的重要性，并透露未来将推出适合笔记本运行的轻量化版本。

> 译自：[Mistral’s Large 4 open weights arrive with a 1-point coding lead over GLM-5.3: "There’s nothing you can’t do with this model that you can do with competitors."](https://thenewstack.io/mistral-chonk-coding-model/)
> 
> 作者：Meredith Shubel

**周四，Mistral 在 Hugging Face 上发布了**其前沿开源模型 Mistral Large 4 (ML4) 的权重。

这家法国 AI 公司在三周前刚刚将其提供预览，并表示自那时起，通过强化学习以及与客户和合作伙伴的测试，ML4 得到了显著改进。Mistral 称，现在 ML4 是“世界上最好的开源智能体编程模型”，在网络安全和编程基准测试中击败了 GLM-5.3（尽管在后者上仅险胜），且成本只是竞争对手的一小部分。

> “我们希望处于能够定义前沿的位置。”

从此，这家 AI 公司承诺将继续增长。在由 *The New Stack* 参加的闭门新闻发布会上，Mistral 科学副总裁 [Pierre Stock](https://www.linkedin.com/in/pierrestock/) 称 ML4 仅仅是“一块踏脚石”，并表示：“我们希望处于能够定义前沿的位置。”

## Mistral 科学副总裁不愿生活在一个没有开源权重的世界里

Stock 告诉记者，Mistral 完全支持“开源权重的力量”，称其对于确保业务连续性、透明度和对所有人的可审计性至关重要：“我不愿意生活在一个开源权重不存在的世界里，”他说。

> “我不愿意生活在一个开源权重不存在的世界里，”他说。

回想起 [OpenAI 宣布计划切断 Cursor 对其模型的直接访问](https://thenewstack.io/anthropic-spacex-cursor-compute-openai/)之时，或者当 [美国](https://thenewstack.io/fable-ban-open-weights/) [政府下令 Anthropic 对所有外国国民暂停 Claude Fable 5 和 Mythos 5](https://thenewstack.io/fable-ban-open-weights/) 之时，Stock 对开源权重的支持分量十足——也许这就是为什么他说这种哲学已经融入了这家法国公司的 DNA 中。

> “我们的立场是，AI 将变得像电力一样。”

“我们的立场是，AI 将变得像电力一样。你不会想生活在一个你的邻居或某个垄断集团可以随时切断你电源的世界里。”

Mistral 将开源权重置于其方法的中心。Anthropic 首席执行官兼联合创始人 [Dario Amodei](https://www.linkedin.com/in/dario-amodei-3934934/) 曾 [争辩说](https://thenewstack.io/amodei-open-weights-compute-regulation/)，仅靠开源权重无法解决 AI 权力的集中问题，因为对计算基础设施的访问仍然高度集中。

正如 Stock 所指出的，通过这种方式，“没有人能将其关闭，因为它既可以在你的基础设施上运行，也可以在你信任的基础设施上运行。”

## 编程 + 网络安全 = 最大影响

不过，一个开源权重模型确实需要过硬的实力来支撑，Mistral 表示 ML4 做到了这一点，称其为“西方制造的最佳开源模型”。

为了支持这些说法，该公司指向了 Terminal-Bench 4.0，这是 Artificial Analysis 编码智能体指数（Coding Agent Index）的一个组成部分。根据 Mistral 的数据，[Le Chonk](https://thenewstack.io/mistral-large-4-weights/)（Mistral 对 ML4 的官方昵称）在智能体编程方面被评为全球顶级开源模型，得分为 41%，相比之下 Muse Spark Open 为 6%，Kimi K3 为 21%，并且以微弱优势超过了 GLM 5.3 的 40%。

![](https://cdn.thenewstack.io/media/2026/10/1353f6a4-cybergym-e2e.png)





点击放大图片。*（来源：Mistral）*

“这张图表没有告诉你的是，”Stock 说，“它比竞争对手更高效，”他补充说，Le Chonk 每个任务平均使用的 Token 比 GLM 5.3 少 47%。“这意味着你可以以更低的成本更快地完成工作，”他解释道。

然而，编程能力并不是这家初创公司训练其模型时的唯一焦点。

“我们确实将编程和网络安全确定为两个主要领域，它们可以产生影响并惠及我们的客户，帮助他们利用 AI 转型整个业务，”Stock 在简报中说道。

因此，Mistral 加大了投资以提升模型的网络安全能力。在 Artificial Analysis 网络指数（Cyber Index）的 CyberGym E2E（测试防御性网络安全能力）中，这个法国模型再次超越了许多竞争对手，得分为 79%，而 GLM-5.3 为 29%（尽管 Z.ai 较小的 GLM-5.3 Flash 在同一图表中得分为 74%）。在 Mistral 的对比中，ML4 超过了 DeepSeek v4.1 Flash 1017 的 76%，并与 MiMo-V2.6-Pro 的 79% 持平。

![](https://cdn.thenewstack.io/media/2026/10/e3dafb41-terminal-bench-4.0.png)





点击放大图片。（来源：Mistral）

为此，Stock 解释了 Mistral 的一些客户是如何将该模型投入实际使用的，他们用它来支持自动化渗透测试，其中专门的智能体分析应用程序的日志并测试潜在的切入点。

## 颠覆性的改进，极低的成本

当 [Mistral 在 10 月初公开预览版中推出 ML4 时](https://thenewstack.io/mistral-large-4-weights/)，它是在其欧洲数据中心使用约 3,800 个 Nvidia Grace Blackwell GPU 进行了大约两个月的训练之后发布的。Stock 表示，在过去的三周里，该模型经历了“显著的改进”，他将其归功于团队的强化学习。Mistral 自身的 Terminal-Bench 4.0 得分从预览时的 28% 上升到了 41%。

> “我没有听说有谁能够用这么少的资源做到这一点。”

更值得注意的是，他声称这家法国公司仅用 10 兆瓦的电力就进行了这种强化学习，“这只是所有竞争对手所用资源的一小部分。”

当被追问 Mistral 如何能确信自己比竞争对手更具成本效益时，Stock 告诉记者：“我没有听说有谁能够用这么少的资源做到这一点。”

他还表示，Mistral 的资源效率意味着这家法国初创公司可以在获得正确投资的情况下取得更大进展：“如果你给我们 10 倍以上的资金，那么我们将把这些效率提升考虑进去。”

## Mistral 想要引领前沿

在整个闭门简报中，Stock 一直将 ML4 称为“一块踏脚石”，暗示了 Mistral 对下一步的计划。

有一点是确定无疑的？开发人员可以期待在未来几个月内推出 Le Chonk 的更小版本，Stock 确认道：“将会有模型家族，其中有一个将能够在笔记本电脑上运行。”

Mistral 表示，ML4 可以帮助软件工程师现代化遗留代码库（[OpenAI 最近在 COBOL 迁移方面取得了惊人的飞跃](https://thenewstack.io/penai-cobol-migration-benchmark/)），以及在金融、制造、工业工程和地理空间应用中发挥作用。展望未来，这家法国公司似乎将目光投向了扮演更重要的角色：

“我们认为唯一的出路就是拥有整个技术栈。”