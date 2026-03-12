人工智能领域近期的主导趋势一直很明确：[更大的模型](https://thenewstack.io/introduction-to-llms/)、更多数据、更多算力。但随着公司将巨大的计算资源投入到越来越大的模型中，训练和运行这些系统的[成本](https://thenewstack.io/why-agentic-llm-systems-fail-control-cost-and-reliability/)不断上升。正是这种矛盾促使微软的研究人员探索一条不同的路径：通过精心策划的推理数据训练更紧凑的模型，以探究其潜力。

在[上周的一篇博客文章](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/)中，微软描述了 [Phi-4-Reasoning-Vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)，这是一个旨在处理涉及文本和图像的推理任务的多模态模型。目标不仅仅是为语言模型添加视觉理解能力；更重要的是，它探索了在高质量推理数据集上训练的紧凑模型是否能与大得多的系统竞争。

Phi-4-Reasoning-Vision-15B 在宽松的 MIT 许可下以开放权重发布，可在所有常用平台获取，包括 [Hugging Face](https://huggingface.co/microsoft/Phi-4-vision-reasoning-15B)、[GitHub](https://github.com/microsoft/Phi-4-vision) 和微软[自家的 AI Foundry](https://ai.azure.com/catalog/models/Phi-4-Reasoning-Vision-15B)，让开发者可以直接实验该系统并在此基础上进行开发。这种方法反映了微软研究院鼓励围绕 Phi 系列进行外部实验的更广泛努力。

回溯一下，Phi 模型是微软更广泛研究工作的一部分，该公司曾将其称为小型语言模型 (SLM)。该系列始于 [Phi-1](https://huggingface.co/microsoft/phi-1)（约 13 亿参数）和 [Phi-2](https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/)（27 亿参数），随后是一系列更大的模型，包括 [Phi-3](https://huggingface.co/collections/microsoft/phi-3) 和 [Phi-4](https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/)，每个模型大约有 140 亿参数。参数是在训练期间学习到的内部数值权重，通常用作模型大小和能力的粗略衡量标准。

微软没有追求不断增加的参数数量，而是旨在开发相对紧凑的模型，以实现强大的推理性能，同时避免前沿系统所需的大规模训练。

值得注意的是，微软在最新的研究中似乎放弃了“小型语言模型”的标签，因为该术语并未出现在 Phi-4-Vision-Reasoning 的[技术报告](https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model/)中。该模型拥有约 150 亿参数，显著大于最早期的 Phi 系统（参数范围约为 10 亿到 40 亿）。然而，它仍然比竞争对手开发的许多前沿模型小得多，那些模型可以达到数千亿参数。

研究重点也已转向推理和多模态能力，而非模型规模本身，这可能解释了最新版本为何取消了“小型语言模型”的标签。

## 教会小型模型进行推理

该研究的核心提出了一个简单的问题：在不显著增加模型大小的情况下，能教会模型多少推理能力？其中一个关键部分是效率。微软表示，该系统旨在提供推理能力，而无需通常与前沿模型相关的硬件基础设施。

研究人员指出：“我们的模型旨在足够轻量，可在适度硬件上运行，同时在有利时仍能进行结构化推理。”

该团队还强调了系统的训练效率。该模型在约 2000 亿个 token 上进行了训练，借鉴了早期的 Phi-4 推理工作和基础 Phi-4 模型。微软表示，这远少于最近的几个视觉语言模型的数据量——包括 [Qwen2.5-VL](https://huggingface.co/collections/Qwen/qwen25-vl)、[Qwen3-VL](https://huggingface.co/collections/Qwen/qwen3-vl)、[Kimi-VL](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking) 和 [Gemma 3](https://deepmind.google/models/gemma/gemma-3/)——这些模型据称在超过一万亿个 token 的数据集上进行了训练。

这种效率是该项目更大目标的核心，即改善性能与计算成本之间的平衡。

研究人员写道：“因此，与现有模型在准确性和计算成本之间寻求帕累托最优的权衡相比，我们可以提供一个引人注目的选择。”

Phi-4-Vision-Reasoning-15B 通过专注于结构化推理任务的训练方法来应对这一挑战。该模型在旨在教授逐步解决问题的数据集上进行训练，包括需要解释表格、屏幕截图和其他结构化材料等视觉输入才能得出结论的任务。其中一些示例是合成生成的，使用更大的模型生成解释或解决方案路径，供小型系统学习。

目标是生成一个能够遵循多步骤逻辑链并同时解释视觉输入的模型。

该模型还可以根据任务调整其执行的推理量。开发人员可以在优先考虑速度或更深入分析的模式之间切换，从而使同一个模型在某些情况下能够快速响应，或在问题需要时应用逐步推理。微软伦敦首席云布道师 Leon Godwin 表示，这种灵活性使得该系统无需部署不同的模型即可处理更广泛的工作负载。

Godwin [写道](https://www.linkedin.com/posts/leongodwin_azureai-smalllanguagemodels-activity-7435656545402716160-fMOI/)：“杀手级功能是三种思维模式——混合、思考和不思考——开发人员可以在运行时进行切换。”“计算机使用代理需要亚秒级的 GUI 元素定位？不思考模式。需要对图表进行逐步数学推理？思考模式。同一个模型，同一个部署。”

这种组合非常有用，因为许多实际任务都涉及语言和图像。解释可视化内容、审阅文档或导航用户界面都需要将视觉感知与推理联系起来。实际而言，这可能包括回答关于图表的问题、分析屏幕截图或文档，或者生成与提示一起提供的视觉内容的描述。

然而，微软警告称，该模型尚未在高风险领域（例如医疗或法律决策）或涉及金融交易或其他缺乏人工监督的敏感操作的全自主行动中进行评估。

[模型卡](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)警告：“开发人员在选择用例时应考虑视觉语言模型的常见局限性，并在特定下游用例中使用之前，特别是对于高风险场景，评估并缓解准确性、安全性及公平性方面的问题。”

## 为什么多模态推理很重要

随着模型超越纯文本交互，多模态 AI 系统已成为一个主要焦点。许多实际任务都涉及语言和视觉信息——从分析技术文档和仪表板到导航软件界面。通过将视觉理解与结构化推理相结合，Phi-4-Vision-Reasoning 模型能够解释视觉输入并对其应用逐步逻辑。微软强调了诸如分析科学图表、解决视觉数学问题和解释基于图表的指令等场景。

Phi 项目也反映了研究人员如何改进 AI 模型思维的更广泛转变。多年来，该行业严重依赖缩放法则，通过增加模型大小和训练数据来提高性能。但这种方法带来了巨大的计算成本。

微软的工作则侧重于训练策略：使用精选数据集、合成推理示例和更有针对性的训练技术，在不显著增加模型大小的情况下提高推理能力。一种方法是使用更大的系统生成逐步推理路径，然后用这些解释来训练更小的模型。实际上，大型模型充当了更紧凑模型的老师。

这种技术在 AI 研究中变得越来越普遍。与此同时，大型前沿模型仍然占据主导地位，OpenAI、Google 和 Anthropic 等公司继续致力于开发更大的系统。像 Phi 这样的实验反映了这种转变，表明经过精心训练的、参数少得多的模型可能能够处理许多任务，而无需前沿系统所需的巨大计算量。

一些研究人员认为，这种方法可能对 AI 代理特别有意义，因为 AI 代理通常需要执行大量的较小感知和推理任务，而不是依赖于单个大型模型。

AI 研究员兼 [Dair.ai](http://Dair.ai) 创始人 Elvis Saravia 表示，该模型说明了小型多模态推理系统*如何*在实际代理部署中发挥重要作用。

Saravia [写道](https://www.linkedin.com/posts/omarsar_new-research-from-microsoft-phi-4-reasoning-vision-activity-7435691960193105920-0hbQ?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAAKviRMBcX5r1q4mPiPDFxquTiZC0hbfIYQ)：“并非所有代理任务都需要前沿模型。Phi-4-reasoning-vision 展示了 150 亿参数模型所能实现的潜力。”“处理视觉的小型推理模型对于实际代理部署至关重要。”

此外，AI 研究员、工程师兼投资者 Andreas von Richter 表示，微软论文中最有趣的见解很容易被忽略：数据质量在模型性能中的作用可能比架构本身更大。

von Richter [指出](https://www.linkedin.com/feed/update/urn:li:activity:7435691960193105920?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7435691960193105920%2C7436785692069904384%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287436785692069904384%2Curn%3Ali%3Aactivity%3A7435691960193105920%29)：“最大的性能提升并非来自架构或规模。它们来自数据整理。系统过滤、错误纠正和合成增强。”

他还指出，该模型在约 2000 亿个 token 上进行了训练，而一些竞争性多模态系统使用了约一万亿个 token——这表明主要由训练数据决策驱动的显著效率差距。

最后，von Richter 表示，该模型在更简单的感知任务中跳过推理的能力对于代理系统可能尤为重要，因为不必要的推理会增加延迟和计算成本。

他说：“大多数代理管道都浪费算力，强迫对不需要推理的任务进行推理。”

这种方法能否与最大模型的能力相媲美仍有待观察。目前，前沿系统仍在最具挑战性的基准测试中占据主导地位。但它凸显了该领域内日益激烈的争论，即 AI 的进步是来自不断增长的模型，还是[来自更智能的训练方式](https://thenewstack.io/beyond-shift-left-improving-ai-training-data/)。

YOUTUBE.COM/THENEWSTACK

科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、采访、演示等等。

订阅

组
创建于 Sketch。

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg) Paul 是一位经验丰富的科技记者，报道欧洲及其他地区的一些重大新闻，最近在 TechCrunch 工作，报道了初创公司、企业、大型科技公司、基础设施、开源、人工智能、监管等。Paul 目前常驻伦敦…… 阅读更多 Paul Sawers 的文章](https://thenewstack.io/author/paul-sawers/)