<!--
title: AWS、Upstage和Ollama就决策模型API达成一致，OpenAI尚未加入
cover: https://cdn.thenewstack.io/media/2025/12/26e80981-decisions123-1024x683.jpeg
summary: AWS、Upstage和Ollama等厂商采纳了System One决策模型API标准，实现了生态兼容与代码级可移植性，而OpenAI则推出了自己的专有方案，引发了关于AI决策模型标准制定权的竞争。
-->

AWS、Upstage和Ollama等厂商采纳了System One决策模型API标准，实现了生态兼容与代码级可移植性，而OpenAI则推出了自己的专有方案，引发了关于AI决策模型标准制定权的竞争。

> 译自：[AWS, Upstage and Ollama agree on a decision-model API. OpenAI hasn’t signed on.](https://thenewstack.io/decision-models-system-one/)
> 
> 作者：Janakiram MSV

**AWS 的新决策模型有一个熟悉的地址。** 10月1日发布的 [Strands Decider 2B](https://thenewstack.io/aws-strands-decider-model/) 是一个基于阿里巴巴 Qwen3.5 构建的开源权重模型。但当将其作为服务器运行时代替它响应的地址是 `/v1/systemone`——这与初创公司 TypeSafe AI 两周多前随 [Jev](https://thenewstack.io/typesafe-jev-system-one/) 一起推出的端点完全相同。

在不到三周的时间里，决策模型从一家初创公司的实验变成了一个全新品类。OpenAI、Upstage、Perplexity 和 Cloudflare 提供了托管决策模型，而 AWS 和独立开发者则在 Hugging Face 上发布了开源权重。标准化速度最快的是 TypeSafe 的模式（Schema）——即请求和响应的结构——即便供应商使用自己的 URL 和端点发布它也是如此。

LLM 开发者曾见证过类似的过程。OpenAI 的 Chat Completions API 成了 LLM 的默认接口，因为有太多的提供商克隆了它。OpenAI 后来推出了 Open Responses，这是一个基于其 Responses API 的开放规范。这段历史表明这是一种可能的发展轨迹，而非尘埃落定的结局。

## 决策模型的返回结果

决策模型接收应用程序的状态（例如客户消息和相关策略）以及一组带类型的提问。它返回结构化答案，每个选项都附带一个概率，并且它绝不编写散文、代码或关于其推理的解释。TypeSafe 借用了心理学家丹尼尔·卡尼曼（Daniel Kahneman）普及的用于快速、直观判断的术语，将 Jev 称为“系统一（System One）”模型。

系统一 API 将每个决策简化为三种问题类型。选择题（Choice）从列表中选择一个选项，评分题（Score）将输入置于有序的评分标准中。是非题（Noul）返回判断是非条件成立的概率，开发者可以在一个请求中混合使用这三种类型。

Jev 还返回一个置信度值，团队经常将其误认为是答案正确的几率。TypeSafe 的[文档](https://docs.typesafe.ai/confidence)解释说，置信度衡量的是概率分布的集中程度，并建议团队根据自己的数据设置阈值。校准是通过多次决策来衡量的，因此高置信度永远不能保证单个答案是正确的。

可以将决策模型视为 AI 应用程序中的 `if` 语句。LLM 可以对支持工单进行分类，但它需要生成 Token 才能做到这一点，并且其确信度报告较为松散。决策模型在极短的时间内向应用程序传递一个可用于进行分支判断的概率。

## 让 Jev 在智能体中大放异彩的三个模式

决策模型与 LLM 协同工作。LLM 负责规划、编写和调用工具，而决策模型则处理智能体在这些步骤之间做出的许多小型判断。

想象一下处理退款请求的支持智能体。LLM 为客户起草一份通俗易懂的回复。对决策模型的单次调用即可选择队列、对客户的沮丧程度进行评分，并评估退款政策是否适用。在 Jev 推出几天内，就涌现出了三种模式。

### 将请求路由到正确的模型

[OpenRouter](https://openrouter.ai/typesafe) 于 9 月 25 日推出了 Jev Router，为每个传入的请求选择模型和推理工作量。决策模型充当调度程序，为需要它们的请求保留昂贵的 LLM。

[Strands Decider](https://github.com/strands-labs/strands-decider) 存储库发布了一个示例，该示例挂钩到 Strands 智能体的 `before_tool_call` 事件中。它将天气工具的调用门控在两个是非决策上，因此智能体询问用户具体是哪个城市而不是靠猜。AWS 报告称，在模型未见过的简短分类任务中，置信度在 0.9 或更高的答案在大约 95% 的情况下是正确的。

### 在决策模型失败时进行回退

Maxim AI 的 Bifrost 网关在 Jev 无法访问时将决策[路由](https://www.getmaxim.ai/bifrost/blog/typesafe-system-one-models-and-new-v1-decisions-endpoint)到 LLM。它通过提供商的 Responses API 模拟决策，并返回与 Jev 相同形态的答案。

这些模式展示了这一抽象层为何如此有用。随着竞争对手的效仿，TypeSafe 的 API 成为了一种共享契约。

## 系统一契约的传播方式

第一批采用者直接实现了 TypeSafe 的端点。Upstage 通过系统一模式提供 [Solar Decide](https://openrouter.ai/upstage/solar-decide) 服务，Ollama 在 0.35 版本中[添加](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models)了明确基于 TypeSafe API 的 `/v1/systemone` 端点。Strands Decider、Jared Palmer 的 Kev 以及 Zefan Cai 社区构建的 Open-Jev 都暴露了相同的接口，本地运行时如 Ollaya 和 SGLang 也是如此。

第二组保持语义不变并更改地址。OpenRouter 对 Jev 的原生接口是其自己的 Decisions API。它还提供了一个兼容 TypeSafe 的路由，因此现有的 SDK 客户端只需更改基础 URL 即可切换提供商。据报道，Venice 通过其自己的贝塔决策端点[提供](https://pexon-consulting.de/blog/venice-api-jev-decisions-privacy/) Jev。Perplexity 的 Decisions API 支持相同的选择题、是非题和评分题类型，尽管它使用了不同的路径。

在大型供应商中，OpenAI 仍然是个特例。它在 [DevDay 上发布了基于 GPT-6 Luna 专用版本构建的 Decisions API](https://thenewstack.io/openai-decision-api-luna/) 来回应 Jev。该服务仍处于限量预览阶段，没有公开的模式或定价。

实际结果是代码级别的可移植性。一旦更改了基础 URL，TypeSafe 的 SDK 就可以针对任何实现系统一 API 的服务器运行。因此，根据该契约编写的应用程序可以从托管的 Jev 迁移到本地的 Strands Decider，而无需重写其决策逻辑。服务器在选项限制、计算置信度的方式以及答案质量上仍然存在差异，因此切换仍然需要进行测试。

简而言之，TypeSafe 正在赢得模式（Schema）之战，而端点之战仍在继续。

## Chat Completions 先例的启示

OpenAI 的 Chat Completions API 提供了最接近的先例。vLLM、Ollama、OpenRouter 和其他数十个服务器克隆了它，直到它成为调用 LLM 的默认方式，而不管是谁训练了该模型。OpenAI 后来将其自身平台迁移到 Responses API。2026 年 1 月，它推出了 Open Responses，这是一个基于该设计的开放规范，并将 OpenRouter、Hugging Face、LM Studio、vLLM、Ollama 和 Vercel 作为发布合作伙伴。Simon Willison [指出](https://simonwillison.net/2026/Jan/15/open-responses/)，他更喜欢基于 Chat Completions 的标准，正是因为许多产品已经克隆了它。

这一先例为决策模型带来了两点启示。首先，语义形态在任何正式治理之前就已经传播开来，正如系统一现在所经历的那样。其次，定义这种形态的公司最终必须将其开源。否则，生态系统就会走向兼容的变体，例如 OpenRouter、Venice 和 Perplexity 已经在运行的决策路径。

差异与相似之处同样重要。Chat Completions 标准花了好几年时间才确定下来，涵盖了消息角色、流式传输和工具调用，所有这些都有大量应用程序代码的支持。系统一涵盖了三种问题类型，推出不到一个月，这使得它很容易被克隆和分叉。如果 TypeSafe 将系统一发布为开放规范，它可以遵循 Open Responses 的路径。如果 OpenAI 发布不同的模式，该品类将拥有两个相互竞争的契约。

## 托管、开源权重与混合模型

托管服务提供按 Token 计费的托管端点，而开源权重模型在团队自己的硬件上运行，并将敏感的应用程序状态保留在网络内部。Jev 仍然是托管端的参考实现，尽管 TypeSafe 尚未透露其规模或基础模型。Upstage 在 Solar Mini 4 上构建了 Solar Decide，这是一个拥有 350 亿总参数和 30 亿活跃参数的混合专家（MoE）模型。

Perplexity 通过混合方法跨越了这两个阵营。它于 10 月 1 日发布了带有 Apache 2.0 权重的 pplx-decider 和托管 API，随后于 10 月 6 日发布了 1.1 版本。新的[模型卡](https://huggingface.co/perplexity-ai/pplx-decider-v1.1-27b)报告决策指数（Decision Index）为 61.56，高于之前的 56.4。Perplexity 将大部分提升归功于解除因果掩码（causal mask）以及在更多数据上进行训练。

大多数基于解码器的早期开源实现都使用 Qwen3.5，包括 Strands Decider、较小的 Open-Jev 模型以及前三个 Kev 尺寸。生态系统已经在该基础之外扩展开来，Kev-27B、Open-Jev-27B 以及基于 Qwen3.8 构建的 Perplexity 模型，还有 Convai Innovations 基于 ModernBERT 编码器构建的 Laya。Palmer [报告称](https://aiweekly.co/alerts/jared-palmer-ships-kev-an-apache-20-jev-style-decision-model-family-built-on)将 Kev 移植到 Qwen3.5 在 H100 时间上花费了大约 95 美元。

许多开源实现完全避免了自回归解码。它们用一个小型读出头（readout）替换了语言模型头部，该头部可以在一次传递中对可用选项进行评分。AWS 报告称，在 RTX 3090 上，具有 1.9 亿参数的 Strands Decider 平均每个问题耗时 115 毫秒。

下表反映了截至 2026 年 10 月 7 日的市场情况。

| 模型 | 制作方 | 部署方式 | 权重 | 基础模型 | 规模 | API | 已发布的评估（来源） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Jev 1.13 | TypeSafe AI | 托管（TypeSafe, OpenRouter, Venice） | 闭源 | 未公开 | 未公开 | 系统一（原生） | JevBench v1.5.4，排名第三，72.13 |
| Decisions API | OpenAI | 托管，限量预览 | 闭源 | GPT-6 Luna | 未公开 | 自有 API，模式未公开 | 未发布 |
| Solar Decide | Upstage | 托管（Upstage, OpenRouter） | 闭源 | Solar Mini 4 | 35B MoE, 3B 活跃 | 系统一 | 未发布 |
| pplx-decider v1.1 | Perplexity | 托管与自托管 | Apache 2.0 | Qwen3.8-27B | 26B | 自有 Decisions API | Hugging Face 决策指数，61.56 |
| Strands Decider 2B | AWS | 自托管 | Apache 2.0 | Qwen3.5-2B | 1.9B | 系统一 | AWS 在 JevBench 公共集上运行，0.723 |
| Kev | Jared Palmer | 自托管 | Apache 2.0 | Qwen3.5, Qwen3.8 | 0.8B, 4B, 9B, 27B | 系统一 | 作者测试集，Kev-9B 为 0.837（锁定测试）；Jev 0.857 对比 Kev-9B 0.812（开发集） |
| Open-Jev | Zefan Cai | 自托管 | 已发布适配器和决策头（MIT 代码） | Qwen3.5, Qwen3.8 | 2B, 9B, 27B | 系统一 | 作者在 JevBench 公共子集上的运行结果，27B v1.1 为 85.28%（231 个中的 197 个） |
| Laya | Convai Innovations | 自托管 | Apache 2.0 | ModernBERT | 322M 至 421M | 系统一 | JevBench v1.5.4，已追踪但尚未公开排名 |

评估列将独立基准测试与供应商和作者的测试集混合在一起，因此它并未形成单一的排行榜。Florian Standhartinger 和贡献者在 MIT 许可证下维护 [JevBench](https://benchlm.ai/decision-models)，这是最接近中立评分的标准。其 v1.5.4 排行榜追踪了 112 个决策系统，将 Jev 排在第三位，落后于 blockbrain 的 Cygnet 和开源权重的 Winnow-12B。

## 可靠性问题

决策模型直接对其答案采取行动，这提高了对鲁棒性的要求。南加州大学的一名研究人员[发现](https://arxiv.org/pdf/2609.30243)，优化器可以重定向 508 个最初正确的 Jev 决策中的 61.4%。它的做法是添加简短、看起来很自然的上下文，将模型推向选定的错误答案。该搜索每个项目最多使用 64 次接受的评估，成功添加的内容的中位长度为 31 个字。

这个数字是对抗性针对性翻转率（targeted-flip rate），而不是普通上下文导致 Jev 失败的概率。尽管如此，同一研究中的开源 Qwen 模型翻转率为 72.6%，这表明弱点在于该品类本身，而不是某个特定的供应商。平台团队应将置信度阈值视为多种控制手段之一，尤其是当应用程序状态包含用户提供的文本时。

## 共享契约的经济学

在 OpenRouter 上，Jev 的价格为每百万输入 Token 0.042 美元，不收取输出费用。Perplexity 将其托管的 v1.1 模型定价为每百万输入 Token 0.02 美元。这使得路由或策略检查比同等的 LLM 调用便宜得多。自托管的开源权重模型用基础设施和运营成本取代了按 Token 收取的 API 费用，这种权衡有利于每小时做出数千次决策的流水线。

对于企业而言，共享契约带来了第二个好处。治理和采购团队可以批准一种集成模式，然后随着准确性、价格和数据驻留要求的变化来更换后端。这赋予了企业客户比不兼容端点市场更强的谈判地位。

同样的契约使供应商的接口商品化。TypeSafe 现在必须在模型质量和校准方面取胜，因为开发者可以通过编辑 URL 用 Strands Decider 或 Kev 替换 Jev。OpenAI 和 Perplexity 面临着不同的压力，因为专有模式要求开发者编写集成代码，而生态系统的很大一部分已经不再需要这些代码了。

## 决策模型的下一步是什么？

系统一已经成为决策模型领先的互操作性契约，获得了来自 AWS、Upstage、Ollama 和开源社区的线兼容（wire-compatible）实现。一旦发布，OpenAI 的模式将决定该品类是巩固为一个契约还是分裂为两个。

决策模型正在成为 LLM 旁边一个便携、廉价的判断层。开发者是否信任它来把关实际行动，将较少取决于 API 的融合，而更多地取决于校准和鲁棒性。团队围绕这些概率构建的保障措施同样重要。