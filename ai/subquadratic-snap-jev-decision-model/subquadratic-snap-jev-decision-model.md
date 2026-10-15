<!--
title: “从前沿大模型手中抢过工作”：Subquadratic决策模型宣称上下文窗口达Jev的12倍
cover: https://cdn.thenewstack.io/media/2026/10/58f3c5d5-ayush-kumar-8fmoxutzltk-unsplash-scaled.jpg
summary: AI初创公司Subquadratic推出了全新的决策模型SubQ Snap，其上下文窗口高达38,4000个Token，是Jev模型的12倍。该模型基于稀疏注意力架构，旨在通过处理更长的代码库和文档，为智能体提供更强大的决策能力，并减轻前沿大模型的负担。
-->

AI初创公司Subquadratic推出了全新的决策模型SubQ Snap，其上下文窗口高达38,4000个Token，是Jev模型的12倍。该模型基于稀疏注意力架构，旨在通过处理更长的代码库和文档，为智能体提供更强大的决策能力，并减轻前沿大模型的负担。

> 译自：[“Take work away from frontier LLMs”: Subquadratic’s decision model claims 12x Jev’s context window](https://thenewstack.io/subquadratic-snap-jev-decision-model/)
> 
> 作者：Paul Sawers

[Jev](https://jevtypesafeai.com/) 有很多需要解释的地方。自 AI 初创公司 [TypeSafe 在 9 月中旬推出该决策模型](https://thenewstack.io/typesafe-jev-system-one/)以来，整个行业就[充斥着各种替代方案](https://thenewstack.io/openai-decision-models-deployment/)，OpenAI、Perplexity、Cloudflare、[Amazon](https://thenewstack.io/decision-models-system-one/) 以及最近的 [Microsoft 都纷纷加入其中](https://thenewstack.io/microsoft-decision-model-foundry/)。

可以说，决策模型现在非常热门。

现在，总部位于旧金山的基础模型初创公司 [Subquadratic](http://subquadratic.ai) 也加入了这场热潮，推出了 [SubQ Snap](https://subq.ai/introducing-subq-snap) 决策模型。该公司称，该模型在单个请求中可以处理长达 384,000 Token 的文本和图像——达到了 Jev 每个决策 32K Token 上下文限制的 12 倍。

在周一发布的一篇[博客文章](https://subq.ai/introducing-subq-snap)中，该公司表示，Snap 能够处理 100K Token 并在大约一秒钟内返回决策，这可能使 AI 智能体能够在大型代码库、文档和交互历史记录中做出决策，而无需将信息分解为较小的块。

## 为什么更大的上下文窗口很重要

与生成文本和代码的传统大模型（LLM）不同，决策模型专门用于从预定义的答案中进行选择。这可能意味着选择 AI 智能体接下来应该使用哪个工具、识别相关文件，或者确定测试是否通过。

周二，*The New Stack* 报道了 [Workday 如何使用 Jev](https://thenewstack.io/workday-is-using-typesafes-jev-to-build-user-interfaces-on-the-fly/) 为其 Sana AI 助手即时构建用户界面，根据员工的提问选择诸如工资单卡片和日期选择器等预构建组件。

归根结底，吸引人的地方在于速度和成本。这些决策在智能体执行期间频繁发生，将其委派给更小、更专用的模型可以减少对昂贵的前沿 LLM 的依赖。

在电子邮件问答中，Subquadratic 首席执行官兼联合创始人 [Alex Whedon](https://www.linkedin.com/in/alexander-whedon/) 承认，Jev 的到来帮助塑造了 Subquadratic 自己的市场切入点。

> “Snap 的开发受到了 Jev 的启发，因为决策模型高度符合我们的理论。”

“Snap 的开发受到了 Jev 的启发，因为决策 model 高度符合我们的理论，”Whedon 告诉 *The New Stack*。“对于某些问题，决策模型消除了对解码的需求。”

然而，Whedon 认为该技术的潜力远大于决策模型目前所扮演的支持角色，例如评估 LLM 输出或选择哪个模型应该处理任务。

“我们看到了决策模型愿景的真空，”Whedon 说。“当决策模型真正从前沿 LLM 手中接过工作时，它们才变得令人兴奋。”

> “当决策模型真正从前沿 LLM 手中接过工作时，它们才变得令人兴奋。”

尽管这个领域有些拥挤，但 Subquadratic 认为，当做出选择所需的信息超出其上下文限制时，现有的决策模型就会举步维艰。

想象一下，一个编码智能体试图修复大型代码库中的错误。问题可能源自与产生错误的模块不同的模块，而重要的线索可能埋藏在测试文件或文档中。在 32K Token 的窗口下，智能体可能不得不丢弃潜在的相关信息或转向更大的 LLM。Whedon 认为，Snap 的 384K Token 窗口允许它在决定下一步行动之前，一起检查更多的代码库、日志和先前的操作。

Snap 通过 Subquadratic 稀疏注意力机制（[SSA](https://subq.ai/how-ssa-makes-long-context-practical?utm_source=chatgpt.com)）解决了这个问题，这是该公司在 5 月份首次推出的架构，旨在降低处理长输入的计算成本。据 Subquadratic 称，其注意力需求随着上下文长度呈线性增长，而不是像传统 Transformer 那样呈二次方增长。Whedon 认为，无论各大实验室在计算上花多少钱，改进底层算法都很重要；否则，他说，“我们不可避免地会遗漏智能方面的提升。”

Subquadratic 自己的长上下文基准测试表明，Snap 甚至在处理的信息量增加时也能保持准确性。在 RULER 检索基准测试的改编版本中，Snap 在 32K 到 100 万 Token 不等的输入中获得了 96.3 到 99.8 的分数。在测试多文档推理的 Decision LCR 上，它获得了 74.0 分，而 Jev 获得了 48.0 分（Jev 是分块处理文档的）。

Whedon 澄清说，Snap 公布的 384K Token 上下文限制是由于可用计算能力而对公共预览版施加的临时限制。该公司在 100 万 Token 下测试了该模型，但表示公开支持该长度将需要大约 2.6 倍的计算量。

![长上下文决策](https://cdn.thenewstack.io/media/2026/10/e8da6ec0-a.png)

*长上下文决策*（*图片来源：Subquadratic*）

在较短的任务中，Subquadratic 报告称，在 Decision Index 0.2.1 上，Snap 获得了 61.7 分，而 Jev 为 57.9 分。它在 Bespoke Labs 的 Nimble 基准测试中也处于领先地位，准确率达到 82.9%，而 Jev 为 76.0%。

![短上下文决策](https://cdn.thenewstack.io/media/2026/10/88ba63d7-b.png)

*短上下文决策（图片来源：Subquadratic）*

根据 Subquadratic 的测试，在 16 个面向企业的基准测试中，Snap 在 13 个测试中表现优于 Jev，平均得分为 67.6，而 Jev 为 61.6。然而，Jev 在三个测试中表现更好，其中包括 When2Call，该测试评估智能体是应该调用工具、请求澄清、直接回答还是拒绝。

![企业基准测试](https://cdn.thenewstack.io/media/2026/10/8407b562-c-1024x501.png)

*企业基准测试（图片来源：Subquadratic）*

Whedon 确认所有公布的 Snap 结果都是内部产生的，尽管 Subquadratic 已经[发布了其改编的长上下文评估的代码](https://github.com/subquadratic-ai/decision-longctx-evals)，以便其他人可以复现它们。

Snap 也没有出现在最新的 [Decision Index 排行榜](https://huggingface.co/spaces/multimodalart/jev-decision-index)上。Whedon 表示，该基准测试的作者告诉他，当前版本重点关注开源权重模型，Jev 是个例外。最新的 index（目前版本为 0.3.2）还结合了私有测试，这意味着 Snap 公布的 0.2.1 分数无法与较新的结果直接进行比较。

至于为什么该公司将比较重点放在 Jev 上，Whedon 表示它仍然是与 Subquadratic 的企业设计合作伙伴最相关的模型，其次是 [OpenAI 的 Decisions API](https://thenewstack.io/openai-decision-api-luna/)。计划与更新的竞争对手进行比较。

> “在这一类别中，Jev 似乎仍然是需要对标的模型。”

“在这一类别中，Jev 似乎仍然是需要对标的模型，因此能够以高度可推广的方式超越它一直是我们一直在寻找的前沿信号，”Whedon 解释说。

## 更少的胶水代码，更多的上下文

除了基准测试之外，Subquadratic 认为更大的上下文窗口可以简化开发人员构建 AI 智能体的方式。

目前，开发人员经常依靠检索、摘要和分块将大型文档或代码库塞入较小的上下文窗口中。每一步都涉及决定保留哪些信息，这可能会省略后来证明很重要的细节。

Whedon 表示，当材料在其 384K Token 限制内时，Snap *可以*消除其中一些中间步骤，允许智能体在单个请求中检查整个文档或相关文件集合。

然而，他承认在处理更大规模的信息集合时，检索仍然是必要的。

“检索不会消失——企业的语料库远大于 384K Token，你仍然需要一种方法将正确的材料带入窗口，”Whedon 指出。“但现在的窗口已经足够大，检索可以变得粗颗粒度，拉入整个文档或模块，而不是精细修剪的代码片段。这消除了许多脆弱的部分。”

Snap [在公开预览中可用](https://console.subq.ai/)，定价为每百万输入 Token 0.05 美元，输出免费。这意味着处理 100K Token 成本约为半美分，而使用完整的 384K Token 窗口的请求成本约为两美分。

Whedon 解释说，定价反映了旨在选择答案而不是生成长篇响应的模型的计算需求。

> “我们的定价反映了实际成本所在。”

“我们的定价反映了实际成本所在，”Whedon 说。“决策模型不生成文本。它读取输入并返回每个允许答案的概率，因此几乎所有的计算都用于读取，而产生输出对我们来说几乎没有成本。”

## 迄今为止的（Subquadratic）故事

Subquadratic 于 5 月份脱离隐身状态，获得了 [2900 万美元](https://app.dealroom.co/news/note/subquadratic-launches-with-29m-to-build-ai-with-12m-token-context-windows)的种子轮融资，据报道估值为 5.08 亿美元。这家初创公司[先前被称为 Aldea](https://www.linkedin.com/posts/saulramirez_ai-share-7431887568121585664-I-kR/)，由 [Justin Dangel](https://www.linkedin.com/in/justin-dangel-b45aa01/) 和 Whedon 共同创立，后者曾是 Meta 的工程师兼 Tribe AI 的生成式 AI 负责人。Whedon 几个月前接替 Dangel 担任首席执行官，此前他曾担任首席技术官。Dangel 现在担任董事长。

正如 *The New Stack* [在发布时报道的那样](https://thenewstack.io/subquadratic-12-million-context-window/)，Subquadratic 的首款模型 SubQ 因其声称的 1200 万 Token 上下文窗口以及计算效率的大幅提升而备受关注。

6 月份，[该公司发布了](https://subq.ai/subq-1-1-small-technical-report)其早期 SubQ 1.1 Small 模型的更详细基准测试，某些结果得到了数据公司 Appen 的独立验证。在 7 月份接受 *The New Stack* 的[采访](https://thenewstack.io/subquadratic-sparse-attention-no-attention/)中，Whedon 透露 Subquadratic 已经在研究完全摒弃注意力机制的架构。

因此，Snap 建立在该公司现有的稀疏注意力研究基础之上，将其长上下文的野心带入了日益拥挤的决策模型市场。

目前，Snap 声称的性能优势依赖于 Subquadratic 自己的基准测试结果。独立的测试将证明其更大的上下文窗口是否真的能带来更好的决策。