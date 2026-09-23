<!--
title: OpenAI发布GPT-6 Sol和Luna：Token价格直接腰斩
cover: https://cdn.thenewstack.io/media/2026/02/33c02ff1-img_2596-scaled.jpg
summary: OpenAI于周二发布了全新模型GPT-6 Sol和Luna，作为旗舰模型GPT-6 Astra的补充。新模型的Token价格较上一代降低了一半以上，同时在推理性能、提示词缓存效率以及对齐安全性方面均有显著改进。
-->

OpenAI于周二发布了全新模型GPT-6 Sol和Luna，作为旗舰模型GPT-6 Astra的补充。新模型的Token价格较上一代降低了一半以上，同时在推理性能、提示词缓存效率以及对齐安全性方面均有显著改进。

> 译自：[OpenAI releases GPT-6 Sol and Luna — and cuts token prices in half](https://thenewstack.io/openai-gpt-6-sol-luna-release/)
> 
> 作者：Frederic Lardinois

**OpenAI于周二发布了 GPT-6 Sol 和 Luna**，它们将与 OpenAI 产品线中的旗舰模型 [GPT-6 Astra](https://thenewstack.io/openai-gpt6-astra-benchmarks/) 形成互补。截至目前，暂无 GPT-6 Terra。

## 全新的 GPT-6 定价

最大的新闻是，与上一版本相比，OpenAI 将每百万输入/输出 Token 的价格降低了一半甚至更多。[GPT-6 Sol](https://developers.openai.com/api/docs/models/gpt-6-sol) 的价格为每百万输入/输出 Token 2 美元/10 美元（而 [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/) 为 4 美元/20 美元），[GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) 的价格则为 0.10 美元/0.50 美元（而上一代为 0.20 美元/1.20 美元）。

OpenAI 的一位发言人告诉 *The New Stack*，GPT-5.6 的定价本来就是促销性质的，但对于新的 GPT-6 模型来说，这就是默认价格。

OpenAI 在公告中解释说：“缓存和推理方面的改进使我们能够以更低的成本提供这些模型，我们将这些节省下来的成本直接回馈给用户和客户。”

## 基准测试

正如你所料，新模型相比其 GPT-5.6 的前身有了明显的改进，但在大多数情况下，这种提升并非极端巨大。

例如，在 [Zapier 的 AutomationBench](https://zapier.com/benchmarks)（用于检验模型在业务工作流测试集上的表现）等基准测试中，GPT-6 Luna 比上一版本提升了 5.4 个百分点。

![](https://cdn.thenewstack.io/media/2026/09/6d66096b-screenshot-2026-09-22-at-15.14.57.png)

*图片来源：OpenAI*

在 DeepSWE v1.1 软件工程基准测试中，GPT-6 Sol 的表现基本与 [Anthropic 的 Fable](https://thenewstack.io/how-anthropic-is-bringing-fable-5-back/) 持平（最大努力下为 68.8% 对比 Fable 5 在超高努力下的 69.9%），但成本仅为后者的 20%。Luna 在最大努力下的得分与 Claude Opus 5 和 Fable 5 在中等努力下的得分相似，且成本显著降低。

OpenAI 在其整个公告中都将重点放在了这种成本对比上——特别关注每个任务的价格，而不是单纯的 Token 定价。

![](https://cdn.thenewstack.io/media/2026/09/aedcdb5f-screenshot-2026-09-22-at-15.14.28.png)

*图片来源：OpenAI*

## Anthropic 刷新了对比标准

鉴于 Anthropic [于周二早些时候发布了 Opus 5.5](https://thenewstack.io/claude-opus-5-5-release/)，OpenAI 的对比已经过时了——这就是 AI 时代的常态。Anthropic 也将其 Opus 5.5 的每 Token 定价从 5 美元/25 美元下调至 4 美元/20 美元，但这仍使得 Anthropic 的模型价格是同类 GPT-6 Sol 的两倍。

在其公告中，当将 GPT-6 Sol 与 Opus 5 进行比较时，OpenAI 声称与 Anthropic 的模型相比可以节省大量成本——在大多数情况下这一结论依然成立，但 Anthropic 表示，Opus 5.5在每个任务中使用的 Token 也更少，该公司称，这使得典型工作负载下的成本比 Opus 5 降低了 40%。

值得注意的是，目前还没有人将 Sol 和 Opus 5.5 进行过正面交锋。根据 OpenAI 的 AutomationBench 数据，Sol 在每个任务的成本上可能仍然更便宜，但在 Anthropic 的测试中，Opus 5.5 在共享基准测试中的得分高于 GPT-5.6 Sol。

不过，由于几乎不可能知道一个智能体完成任务需要消耗多少 Token，这些定价变动仍然没有让用户更容易做出预算。

### 提示词缓存

对于构建智能体的开发者来说，缓存方面的变动可能比 Token 价格更重要。OpenAI 表示，它改进了 GPT-6 的提示词缓存，以默认提供更高的缓存命中率，被缓存的输入 Token 可享受高达 90% 的折扣。

另一个积极的变化是，开发者现在可以更改推理努力程度和工具可用性，而不会使缓存失效。通过显式断点，开发者可以选择缓存前缀的结束位置，全新的仪表板和诊断工具则展示了哪些内容被缓存了，哪些没有。

GitHub 表示，在过去几个月里，针对 OpenAI 模型数十亿次请求的统计显示，这些改进使需要重新处理的提示词 Token 比例减少了一半以上。

Anthropic 对 Opus 5.5 采取了类似举措，在每 Token 降价 20% 的基础上，将 Token 计费使用的缓存读取价格降低了 60%。

## 风格变化

不过，模型不仅仅关乎基准测试。借助 GPT-6 Sol，OpenAI 让其模型的回答更加直接，而不是像以前那样采用（已经有所收敛的）更具对话风格的语气。OpenAI 表示：“预计会看到更高的清晰度、更少的行话、更少奇怪的措辞、更少低价值的细节，在不失实质内容的前提下整体回答略微变短。”

![](https://cdn.thenewstack.io/media/2026/09/3055e717-screenshot-2026-09-22-at-08.16.44-1024x441.png)

*图片来源：OpenAI*

### 对齐

鉴于发生了 [HuggingFace 事件](https://thenewstack.io/openai-huggingface-sandbox-breach/)，OpenAI 强调其针对 GPT-6 Sol 和 Luna 的对齐工作也就不足为奇了。

OpenAI 表示，这两个模型在其对齐评估中均比 GPT-5.6 同类模型有所改进，包括减少了对其自身编写代码工作的误导性声明。在内部代码欺骗测试中，GPT-6 Sol 的比率从 10.4% 下降到 1.3%。

当被提供一个故意损坏的搜索工具——并根据它是披露问题还是盲目猜测来评分时，Sol 未能披露问题的比例从 77.5% 下降到 4.9%。

然而，更令人担忧的是，当研究人员要求模型遵守诸如“访问被拒绝”消息之类的显式警告时，GPT-6 Sol 在 64.4% 的运行中仍然试图绕过这些限制，仅比其前身的 68.2% 有所下降。Luna 的改进更大，从 76.5% 降至 42.4%。

OpenAI 表示，这些测试主要涵盖低风险情况，且在运行时尚未使用其产品中使用的完整系统级安全护栏。

![](https://cdn.thenewstack.io/media/2026/09/9b78897a-screenshot-2026-09-22-at-15.12.20.png)

*图片来源：OpenAI*

在一个注入了未经授权指令（包括披露私人信息请求）的模拟留言板中，Sol 在发现该留言板的运行次数中，有 11.3% 采取了指定行动，低于之前的 51.9%。Luna 和 Astra 则没有采取任何行动，不过 OpenAI 指出 Luna 发现留言板的频率也较低。

相比之下，Anthropic 表示 Opus 5.5在其最全面的对齐测试中表现最强，并点名 METR 和 Frontier Design 作为发布前的外部测试人员。Opus 5.5 还自带安全护栏，可重定向请求，将大多数网络安全任务发送给 Opus 4.8，并将 Anthropic 的生物学或前沿 LLM 开发分类器标记的任何内容发送给 Opus 5。

### 可用性

从周二开始，Plus、Pro、Business、Enterprise 和 Edu 用户可以在 ChatGPT Work 和 Codex 中使用 GPT-6 Sol 和 Luna。

免费版和 Go 用户可以在桌面端应用中使用 Luna。

目前这两个模型尚未登陆 Chat。OpenAI 表示，计划在全天逐步推出它们以保持服务稳定，因此它们可能不会立即显示出来。