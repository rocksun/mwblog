周二，Anthropic 发布了 [Claude Science](https://claude.com/product/claude-science)，这是一款专为科学家设计的新应用程序，可以在 macOS 和 Linux 上本地运行，也可以在远程机器上运行。Anthropic 将其描述为 AI 工作台，“科学家们可以在这里集中进行研究。”

在设计和精神上，它感觉有点像科学家的 Claude Cowork。

目前，Claude Science 正处于测试阶段，主要面向生命科学领域的研究人员，但其名称表明该公司计划随着时间的推移进行扩展。

## 适用于 Claude 的所有付费计划

要使用它，你不必是科学家。它在 macOS 和 Linux 上适用于所有 Claude Pro、Max、Team 和 Enterprise 计划的用户（不过对于 Team 和 Enterprise 计划，必须先由管理员启用）。Anthropic 还为研究实验室提供折扣的 Team 计划。

Anthropic 指出，科学家经常需要在 PubMed、Jupyter、R 和终端等众多数据库和工具之间切换。Claude Science 的承诺是通过将 Anthropic 的先进模型与这些研究人员已经在使用的数据库、平台和工具连接起来，将所有这些整合在一起。

![](https://cdn.thenewstack.io/media/2026/06/341d48c5-claude-science-product-image_01_embargoed-until-tuesday-june-30-2026-10am-pt-1024x629.png)

*图片来源：Anthropic*

与大多数领域一样，科学研究涉及大量实际上并不能推进科学进步的重复性工作。Anthropic 在公告中写道，该工具旨在帮助“研究人员分析文献并执行多步研究，并且以工件为先，允许用户反复修改图表和手稿，直到它们准备好发表。每项输出都带有其制作过程的可审计历史记录，因此科学家可以验证和重现结果。”

## 并非新模型

Anthropic 强调，它并不是为 Claude Science 发布新模型。相反，它由标准的 Claude 模型提供支持。当用户使用该工具时，他们首先与一个通用的协调代理进行交互，该代理可以访问 60 多个数据库和一套相关技能。这些工具还支持任何可以通过 MCP 连接的其他服务。

Anthropic 实际上正在使用来自 Nvidia 新的 [BioNeMo Agent Toolkit](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit) 的技能来连接生命科学模型和库，包括 Evo 2、Boltz-2 和 OpenFold3。

> “专业的科学研究保留在构建它的合作伙伴手中。”

值得注意的是，OpenAI 也正在 [集成](https://nvidianews.nvidia.com/news/nvidia-launches-bionemo-agent-toolkit-giving-ai-agents-the-tools-to-accelerate-scientific-discovery) BioNeMo Agent Toolkit。

![](https://cdn.thenewstack.io/media/2026/06/7b569cc1-claude-science-product-image_02_embargoed-until-tuesday-june-30-2026-10am-pt-1024x629.png)

*图片来源：Anthropic*

正如 Anthropic 所指出的，Claude Science 旨在充当推理层和结缔组织。“专业的科学研究保留在构建它的合作伙伴手中，”该公司解释道。

像 Jupyter notebooks 和类似工具一样，Claude Science 也可以生成视觉效果，包括 3D 蛋白质结构和基因组浏览器轨迹。“用户可以与代理讨论任何细节，在行内对图表和手稿进行标注，以便代理知道要处理什么内容，使其达到发表标准，”Anthropic 解释道。

这些可视化的代码始终可用，它们创建的完整消息历史记录也是如此。

## 连接到高性能计算（HPC）和 Modal

由于 Claude 本身无法确切地运行大型基因组流水线或蛋白质折叠作业，这些工具还可以通过 SSH 或 [Modal](https://modal.com) 账户与现有的高性能计算集群进行交互。Anthropic 认为，这确保了研究人员不必浪费时间编写这些作业并进行故障排除。相反，Claude 将起草一份计划，研究人员对其进行审查，然后 Claude 将其提交给实验室的现有资源。

随后，一个代理会监控该作业及其输出，标记出任何问题。也可以随时分叉会话以尝试不同的方法。

## 竞争

大型语言模型确实非常适合像 Claude Science 这样的服务，Google、OpenAI 和其他公司也在朝着同一个方向努力。

例如，在 5 月份的 I/O 大会上，Google 推出了“Gemini for Science”，它也明确地将其 [标榜](https://blog.google/innovation-and-ai/technology/research/gemini-for-science-io-2026/) 为“桌面上的科学工作台”，将跨越 30 多个生命科学数据库的科学技能及其“AI 联合科学家”假设引擎捆绑在一起。当然，Google 的 DeepMind 在利用 AI 进行生命科学研究方面也有着悠久的历史，并且因此获得了诺贝尔奖。

OpenAI 也曾将科学作为早期关注点，推出了诸如 [Prism](https://openai.com/prism/)（其科学写作工具）和 [GPT-Rosalind](https://openai.com/index/introducing-gpt-rosalind/)（专门为加速科学研究和药物发现而构建的前沿模型）等服务。不过，随着 Kevin Weil 在今年 4 月的离职，OpenAI 解散了其 OpenAI for Science 部门，并关闭了 Prism，因为它将重心转移到了其更多的核心服务（以及 Codex）上。