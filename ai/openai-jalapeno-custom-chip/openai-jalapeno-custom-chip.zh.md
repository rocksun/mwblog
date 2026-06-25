OpenAI 于周三发布了其首款定制推理加速器 Jalapeño。该芯片由 OpenAI 与 Broadcom 联合开发，并得到加拿大电子制造商 Celestica 的支持，是其多代计算平台战略的第一步。

这家 AI 公司[表示](https://openai.com/index/openai-broadcom-jalapeno-inference-chip/)，Jalapeño 的设计旨在适配所有大语言模型 (LLMs)，并将助力 AI 变得更快、更好、更经济。在这一宏伟使命的背后，OpenAI 毫不掩饰其想要掌控完整 AI 技术栈的渴望，而这正是越来越多 AI 巨头正在追求的目标。

> “凡是认真对待平台战略的公司，都必须认真对待芯片。”

正如消费技术研究公司 Creative Strategies 的首席执行官兼首席分析师 Ben Bajarin 在 [X](https://x.com/BenBajarin/status/2069772012214530302?s=20) 上所言：“凡是认真对待平台战略的公司，都必须认真对待芯片。”

然而，由于公布的技术细节极少，开发者们不禁怀疑 OpenAI 不断扩张的版图究竟是赋能还是限制。

## 跟上节奏，科技巨头们，我们现在都在自研芯片

OpenAI 并非唯一一家涉足自研 AI 芯片的科技巨头。

早在 2016 年，[Google](https://blog.google/innovation-and-ai/technology/developers-tools/10-things-you-may-have-missed-at-google/) 就为其机器学习软件 TensorFlow 设计并制造了定制硬件——张量处理单元 (TPU)。几年后，[Amazon](https://aws.amazon.com/about-aws/whats-new/2018/11/announcing-amazon-inferentia-machine-learning-inference-microchip/) 推出了 AWS Inferentia，这是其首款专门为 AI 和机器学习构建的芯片。[Trainium](https://aws.amazon.com/blogs/aws/amazon-ec2-trn1-instances-for-high-performance-model-training-are-now-available/) 于 2022 年亮相，随后 [Microsoft](https://news.microsoft.com/source/features/ai/in-house-chips-silicon-to-service-to-meet-ai-demand/) 在 2023 年推出了 Azure Maia AI 加速器。虽然目前尚未最终确定，但据 [Reuters](https://www.reuters.com/business/anthropic-weighs-building-it-own-ai-chips-sources-say-2026-04-09/) 四月份报道，Anthropic 也在考虑设计自己的芯片，尽管该公司目前尚未公开做出承诺。

为什么大家都热衷于定制芯片？

这要归咎于算力淘金热，正如 OpenAI 的总裁、董事长兼联合创始人 Greg Brockman 所言，AI 公司对算力的渴求日益强烈——这是一个“算力驱动型经济”。数据证实了这一点；[Stanford 的 2025 年 AI 指数报告](https://hai.stanford.edu/ai-index/2025-ai-index-report)显示，“训练算力每五个月翻一番”。

虽然内部研发定制 AI 芯片并不能完全缓解算力压力，但这确实是 OpenAI 及其科技巨头同僚们扩大计算能力，同时潜在降低成本并减少对第三方供应商依赖的一种途径。

## 令人兴奋的声明，但缺乏证据

OpenAI 在其发布博文中称其新芯片“旨在成为大语言模型（LLMs）的最佳推理平台”。

OpenAI 硬件负责人 Richard Ho 具体指出：

“我们围绕对前沿 AI 模型最重要的内核、内存移动、网络和服务模式优化了架构。根据初步测试，Jalapeño 将高效执行我们最重要的工作负载，接近硬件的理论极限。”

但该公司对任何真实的技术细节守口如瓶。

虽然它声称目前的测试表明 Jalapeño 的性能“大大优于当前最先进水平”，但并未提供基准测试数据来支撑这一说法。相反，它告诉开发者预计“在未来几个月内”会发布一份详细的技术报告。

OpenAI 确实透露的一点是，该芯片的工程样品目前正在其实验室运行机器学习工作负载，包括 GPT-5.3-Codex-Spark。

## Jalapeño 是为了服务开发者，还是为了满足 OpenAI 掌控 AI 技术栈的野心？

OpenAI 毫不掩饰其追求全栈控制的意图。该公司声称，通过这种方式，它将使模型“对用户而言更快、更可靠、更实惠”。

其逻辑大致如下：更好的基础设施意味着更高效的计算，这意味着更好的训练，这意味着更好的模型，这意味着更好的产品，这意味着更多的收入。然后，它解释道，它可以将这些收入再投资于基础设施，从而为每个人提升智能水平。

> 但考虑到该公司披露的芯片规格寥寥无几，开发者们似乎只能静观其变。

因此，Jalapeño 只是 OpenAI 试图掌控整个 AI 棋盘的下一步行动，即超越模型和产品，直接深入到底层基础设施本身。

对于开发者而言，OpenAI 似乎坚定地认为其全栈战略将为每个人带来更好的性能和定价，并最终赋能“任何试图学习、创造或解决难题的人”。尽管如此，值得思考的是：随着 OpenAI 的控制力加强，开发者是否会受制于其生态系统？

OpenAI 在公告中多次重申，它设计 Jalapeño 是为了当前的及未来的大语言模型——涵盖所有模型。但考虑到该公司披露的芯片规格寥寥无几，开发者们似乎只能静观其变。

## 快速构建，前景广阔

OpenAI 选择分享的极少数幕后细节夸耀了其开发速度，声称从设计到制造流片仅用了九个月时间——“我们相信这是高性能先进半导体领域有史以来最快的 ASIC 开发周期。”

该公司将这一快速时间表的部分功劳归功于其自身的模型，这些模型加速了设计和优化流程。

展望未来，Jalapeño 计划在今年年底前在 Microsoft 及其他合作伙伴的数据中心以吉瓦（gigawatt）规模部署。

这仅仅是个开始。OpenAI 暗示了一个即将推出的多代发展路线图，并提出了一个问题：它接下来会寻求掌控什么？