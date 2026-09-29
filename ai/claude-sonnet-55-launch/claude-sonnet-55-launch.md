<!--
title: Anthropic发布Claude Sonnet 5.5：以半价实现接近Opus的性能
cover: https://cdn.thenewstack.io/media/2026/09/7f2295ce-sonnet-5.5_image.jpg
summary: Anthropic发布Claude Sonnet 5.5，该模型速度提升超30%、任务成本降低达30%，在多个基准测试中性能接近Opus 5.5，现已登陆各大主流云平台。
-->

Anthropic发布Claude Sonnet 5.5，该模型速度提升超30%、任务成本降低达30%，在多个基准测试中性能接近Opus 5.5，现已登陆各大主流云平台。

> 译自：[Anthropic launches Claude Sonnet 5.5 with near-Opus performance at half the price](https://thenewstack.io/claude-sonnet-55-launch/)
> 
> 作者：Frederic Lardinois

**Anthropic于周一发布了Claude Sonnet 5.5**，这是其主力模型的最新版本，也是Claude 5.5家族中的第二款模型（继上周发布的 [Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/) 之后）。

新版本的 [Claude Haiku](https://thenewstack.io/anthropic-launches-claude-haiku-4-5/) 作为该家族中体量最小、价格最实惠的模型，已列入路线图，并将于“未来几周内”发布。

## 速度提升30%，成本降低高达30%

Anthropic表示，新的Sonnet模型生成输出的速度比上一代 [Sonnet 5](https://thenewstack.io/claude-sonnet-5-launch/) 快30%以上，同时将每个任务的成本降低了高达30%。这使得Sonnet 5.5成为该公司迄今为止速度最快的Sonnet模型，正如Anthropic所言，它是“Claude Opus 5.5更快、成本更低的完美补充”。

Anthropic认为，该模型“在范围明确的日常任务、修复Bug以及创建精美的文档、幻灯片和电子表格方面表现最强。”早期测试人员还指出，它“为用户界面增添了精致感，并且能够遵循幻灯片模板来创建只需极少编辑的演示文稿。”

与Opus 5.5一样，Sonnet 5.5的行文也比Anthropic上一代模型更清晰。在Opus 5.5上，该公司承诺提供更清晰、听起来更自然的语气，而Sonnet 5.5现在也具备了这一特质。

## 在多数基准测试中接近Opus水平

Anthropic表示，最大的提升在于编程方面。在测试命令行任务代理的Terminal-Bench 4.0上，Sonnet 5.5的得分为70.6%，高于Sonnet 5的10.3%，并领先于Opus 5.5的66.4%。（该基准测试的维护人员指出，Sonnet 5有时会遇到超时和 Token 限制，这有助于解释其低分。）

在利用真实Cursor编程会话中的任务的CursorBench上，Sonnet 5.5的得分与Opus 5.5相差大约两分。在Cognition的FrontierCode（检查代码更改是否可以在无需人工编辑的情况下合并）上，它在第二高的努力设置下的得分为52.1%，而Opus 5.5为54.4%，OpenAI的GPT-6 Sol为49.3%。

![](https://cdn.thenewstack.io/media/2026/09/d8895bd6-screenshot-2026-09-28-at-19.33.05-1024x417.png)

![](https://cdn.thenewstack.io/media/2026/09/81c5cd65-screenshot-2026-09-28-at-19.39.12-1024x370.png)





Claude Sonnet 5.5基准测试。图片来源：Anthropic。

在知识工作方面，Sonnet 5.5在Artificial Analysis的GDPval-AA上得分为1,844分，该榜单根据模型在44个职业的现实任务中的Elo分数进行排名。这仅比Opus 5.5落后两分，比Sonnet 5领先约400分。Sonnet 5.5还击败了GPT-6 Sol的1,487分。

该新模型在计算机使用和人类最后考试（Humanity’s Last Exam）上也接近Opus 5.5的表现。在关于长视距工作和图像理解的非正式测试中，Anthropic表示它是第一个仅通过截图就能通关《[宝可梦 红](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Red,_Blue,_and_Yellow)》的Sonnet模型。

Anthropic表示，在几个基准测试中，Sonnet 5.5在低或中等努力程度下，以每个任务大约十分之一的成本就击败了Sonnet 5的最佳得分。

尽管如此，该公司表示，Opus 5.5在“需要持续判断力的复杂、开放式工作方面明显更强”。

## 定价与可用性

尽管Anthropic下调了Opus 5.5的价格（输入 Token 每百万4美元，输出 Token 每百万20美元），且OpenAI在同一天将其 [GPT-6 Sol和Luna模型](https://thenewstack.io/openai-gpt-6-sol-luna-release/) 的价格减半，但Sonnet 5.5的定价保持不变，仍为输入 Token 每百万2美元，输出 Token 每百万10美元。缓存读取价格为每百万 Token 0.20美元。

这与OpenAI在Astra之后第二好的模型GPT-6 Sol的标价相同。

不过，由于该模型使用的 Token 数量要少得多（至少根据该公司自己的测算），因此运行它的成本应该比运行Sonnet 5更便宜。

Sonnet 5.5现已在Claude Platform、Amazon Web Services、Google Cloud和Microsoft Azure上架。关闭思考功能运行Sonnet的开发人员在迁移到Sonnet 5.5之前，需要切换到新的 `between_tools` 设置。Opus 5.5 [已经会拒绝](https://thenewstack.io/claude-opus-agent-migration/) 完全关闭思考功能的请求。

## 安全防护

由于Anthropic认为Sonnet 5.5的网络安全能力与Sonnet 5相当，这是第一款采用与Anthropic最强模型相同网络安全防护措施的Sonnet模型。

该公司表示，例行的Bug修复不受影响，但风险更高的网络安全请求将回退到Sonnet 5。这也是第一款配备分类器的Sonnet模型，旨在阻止攻击者 [提取其推理过程来训练他们自己的模型](https://thenewstack.io/moonshot-fable5-distillation-accusations/)。