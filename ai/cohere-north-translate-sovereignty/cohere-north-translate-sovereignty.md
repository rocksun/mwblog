<!--
title: “机器翻译在大多数语言中仍未成熟”：Cohere推出无需推理的翻译模型背后的逻辑
cover: https://cdn.thenewstack.io/media/2026/09/c6efc3f4-curated-lifestyle-g0lqwchrqdk-unsplash-scaled.jpg
summary: Cohere发布了名为North Small Translate的开源机器翻译模型。该模型采用专家混合架构，通过去除推理过程以提升效率和翻译准确性，旨在为企业提供更具控制力、适合长文档翻译的专业化解决方案。
-->

Cohere发布了名为North Small Translate的开源机器翻译模型。该模型采用专家混合架构，通过去除推理过程以提升效率和翻译准确性，旨在为企业提供更具控制力、适合长文档翻译的专业化解决方案。

> 译自：[“Machine translation is still broken for most of the world's languages”: Cohere builds non-reasoning for a reason](https://thenewstack.io/cohere-north-translate-sovereignty/)
> 
> 作者：Adrian Bridgwater

**企业级 AI 公司 Cohere** 上周[宣布](https://thenewstack.io/cohere-translation-commercial-licensing/)推出 North Small Translate，这是一个支持 50 种语言的专家混合（MOE）开源权重机器翻译模型。

开发者可以根据 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.en) 协议[下载](https://huggingface.co/CohereLabs/North-Small-Translate-1.0)该模型的权重用于非商业用途。Cohere 通过 [Model Vault](https://docs.cohere.com/docs/model-vault) 提供商业授权部署，这是一个由 Cohere 管理的推理环境。Cohere 将该模型定位为其主权 AI 战略的一部分，旨在服务于那些希望对模型运行位置及数据处理方式拥有更大控制权的组织。

North Small Translate 继承了 Cohere 的多语言和翻译基因，包括其 Tiny Aya 和 Command A Translate 模型系列。该公司声称，在各种机器翻译维度上，North Small Translate 的平均表现优于 1T 参数以下的“同等规模开源权重模型”以及基于 API 的翻译模型。

Cohere 联合创始人 Nick Frosst 告诉 *The New Stack*，该模型的效率源于它是一种[非推理模型](https://www.zansara.dev/posts/2026-07-05-reasoning-makes-translations-worse/)，即它依赖于习得的统计模式，无需循序渐进的逻辑处理过程，这意味着它使用的 Token 更少。

## 机器翻译在大多数语言中仍未成熟

“我们花了九年时间扩展一种旨在修复翻译问题的架构，但机器翻译在大多数语言中仍然是失效的，” Frosst 说道。“通用模型可以完成大部分工作，但随后就会遇到瓶颈。企业 AI 在这一领域的下一阶段是更小、更专业，并且能在你自己内部运行。”

> “……机器翻译在大多数语言中仍然是失效的。”

在 Cohere 使用 WMT26 基准进行的评估报告中，该公司表示 North Small Translate 以 83.60 的 WMT26 所有语言基准评分领先，相比之下，Qwen 3.5 397B A17B 为 81.56，GLM 5.2 FP8 为 76.50，DeepL NextGen 为 81.37，Gemma 4 31B 为 79.46，而 Google Translate 为 68.20。

该模型采用专家混合架构，总参数量为 2180 亿，激活参数为 250 亿。Cohere 指出，North Small Translate 的计算和内存占用比其他模型更小。由于并非所有供应商都披露参数数量，这一领域中的一些模型间对比无法完全证实。

## 使用现有解决方案，长文档往往会出错

“机器翻译允许文档自动从一种语言翻译成另一种语言。使用现有的解决方案，长文档往往会出错，” Frosst 说。“Google Translate 在我们的长上下文测试中得分为 21.3，Gemma 4 31B 为 19.4；我们得分为 48.9。例如，一份安全手册第一页看起来还可以，但到了第十页内容就偏离了。另一个风险是文本的去向。一旦你通过第三方 API 处理人力资源政策或监管文档，这些数据就离开了你的场所，这意味着你对数据的控制力必然会降低。”

> “（机器翻译中的）风险在于文本的去向。一旦你通过第三方 API 推送人力资源政策或监管文档，该数据就已经离开了你的场所，这必然意味着你对它的控制力降低了。”

在解释为何该模型能在复杂的企业翻译任务中提供“更强的翻译性能”时，Frosst 表示，该模型可以支持跨越“大量”敏感文档的工作。

除了支持 50 种语言（32 种“高资源”语言 + 18 种其他语言）外，Cohere 团队还解释说，该模型还支持专注于翻译工作流的功能，例如结构化翻译（即 [Markdown](https://daringfireball.net/projects/markdown/) 或 [JSON](https://thenewstack.io/an-introduction-to-json/) 文档）、指令遵循（即推荐语气和格式）以及术语指南（即提供翻译中使用的特定词汇），这些都是模型的一部分。

“North Small Translate 使用多轮工作流，” Frosst 解释道。“模型先翻译，然后检查自己的输出，发现错误并进行修复——这与我们在训练中使用的是同一个循环。我们同时提供这两个版本，因为标准版是一次性翻译，专为大批量设计；而代理版（Agentic version）花费了更多的 Token，在 WMT26 上得分 84.36，对比标准版的 83.60。当文档是合同或安全程序时，这种差异是值得的，但在其他情况下，你可能更倾向于优化效率。”

> “模型进行翻译，审阅自己的输出，发现错误并进行修复。”

## 模型“可控性”驱动语言语气和格式建议

该模型使用了与之前 Cohere 模型相同的架构，但通过训练后改进（包括强化学习和针对机器翻译任务的新数据集）提升了性能。

Frosst 总结道，在翻译模型市场中，生成式机器翻译模型提供了最高的质量和可控性（即建议语气、格式等），但其成本通常远高于商业案例中常用的神经机器翻译（NMT）模型。

North Small Translate 是与 [RWS](https://www.rws.com/) 合作开发的，RWS 是一家在语言技术和服务领域处于领先地位的 AI 解决方案公司。与 RWS 的合作，特别是与其 [Language Weaver](https://www.rws.com/language-weaver/lp/?utm_term=language%20weaver&utm_campaign=TRAN-EMEA-FY26-PAID-gg-branded-all&utm_source=google&utm_medium=paid_search&hsa_acc=2231159122&hsa_cam=23072234561&hsa_grp=189111716551&hsa_ad=801934122649&hsa_src=g&hsa_tgt=kwd-300064526129&hsa_kw=language%20weaver&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23072234561&gbraid=0AAAAADqF18SP0hbwSs9l0dRMDlJoNs73d&gclid=Cj0KCQjwk5nVBhDiARIsAHNGqafiPRsX7yxI16JQE_8BnAuadEfY8k_46ZWLD54CMkVif72wfMZ8sqMaAkyREALw_wcB) 研究与科学团队及语言专家的协作，帮助塑造了模型在整个开发过程中的实际翻译表现。

如上所述，开发者可以免费获取三种量化版本的模型权重以用于非商业用途。对于缺乏所需硬件的用户，还有一个 Hugging Face [Space](https://huggingface.co/spaces) 和 API 可供使用。