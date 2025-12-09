
<!--
title: Linux基金会主席：AI热潮远非泡沫
cover: https://cdn.thenewstack.io/media/2025/12/ed0470df-jim-zemlin-oss-japan-2025-2.jpg
summary: Jim Zemlin认为LLM或处泡沫，投资巨大且能耗高。开源在模型和软件层具关键作用，缩小差距，提升效率。它将定义未来AI技术栈，推动代理AI发展，防止供应商锁定。
-->

Jim Zemlin认为LLM或处泡沫，投资巨大且能耗高。开源在模型和软件层具关键作用，缩小差距，提升效率。它将定义未来AI技术栈，推动代理AI发展，防止供应商锁定。

> 译自：[Linux Foundation Leader: We're Not in an AI Bubble](https://thenewstack.io/linux-foundation-leader-were-not-in-an-ai-bubble/)
> 
> 作者：Steven J. Vaughan-Nichols

TOKYO — Jim Zemlin在周一[日本开源峰会](https://events.linuxfoundation.org/open-source-summit-japan/)的主题演讲中表示，“人工智能可能没有陷入全面泡沫，但大型语言模型[LLM]可能正是如此。”

为什么？Zemlin首先指出，惊人的投资数字占据了头条新闻。他提到，摩根士丹利估计，[从现在到2028年，将有3万亿美元用于人工智能数据中心](https://www.morganstanley.com/insights/podcasts/thoughts-on-the-market/ai-investing-credit-markets-andrew-sheets)，其中[亚马逊](https://aws.amazon.com/?utm_content=inline+mention)、[谷歌](https://cloud.google.com/?utm_content=inline+mention)、[Meta](https://about.meta.com/?utm_content=inline+mention)和[微软](https://news.microsoft.com/?utm_content=inline+mention)等超大规模公司约占总数的一半。

“这比许多小国的国内生产总值还要多的投资，”Zemlin告诉听众，并强调大多数企业，甚至大多数国家，都无法在这种资本密集型基础设施建设中有效竞争。

他说，更关键的是[与人工智能加速推理工作负载相关的能源需求](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/)。他引用了谷歌推理量同比增长50倍的数据，特别是[谷歌的人工智能使用量](https://techcrunch.com/snippet/3009919/usage-of-googles-ai-is-skyrocketing/)，从2024年4月的9.7万亿个token攀升至2025年4月的480万亿个token以上。

此外，他还回应了AWS总裁Andy Jassy的观点，即[当今人工智能增长的最大制约是电力](https://www.businessinsider.com/amazon-tumbles-ceo-andy-jassy-aws-cloud-ai-growth-concerns-2025-7)。Zemlin认为，人工智能热潮本质上是关于物理基础设施、GPU、能源和数据中心的故事，而不仅仅是算法、模型和软件。

然而，尽管存在这种硬件密集型环境，Zemlin表示开源的真正影响力在于其他地方：在模型和软件基础设施层。

具体来说，仅在过去一年中，来自中国（如[DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/)）的[开放权重模型](https://techcrunch.com/snippet/3009919/usage-of-googles-ai-is-skyrocketing/)就缩小了与商业前沿模型之间的性能差距。Zemlin补充说：“我们还看到这些开放权重模型被用于提炼出更小的行业特定模型。”例如，他提到了针对[Llama 3](https://www.llama.com/)的[TinyLlama](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)和针对[BERT](https://huggingface.co/docs/transformers/en/model_doc/bert)的[DistilBert](https://huggingface.co/docs/transformers/en/model_doc/distilbert)。

## 人工智能经济学

开放权重模型和蒸馏技术的结合改变了人工智能领域的经济学。根据Zemlin的说法，“开源大体上赶上了美国的前沿模型和专有模型。[开放权重模型](https://thenewstack.io/nathan-lamberts-atom-project-seeks-american-open-source-ai-models/)通常落后三到六个月。”

这对于经济高效的人工智能工作来说已经足够好了。Zemlin引用了Linux基金会首席经济学家Frank Nagle的话，他最近量化了这种不匹配。根据Zemlin的说法，Nagel的分析显示，尽管[开放模型价格大幅下降，能力几乎相当](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5767103)，但闭源模型仍占据95%的收入，导致每年在专有系统上额外支出约248亿美元。

因此，“我认为我们没有陷入人工智能泡沫，”Zemlin说。“但我们可能正处于LLM泡沫之中。”

随着企业开始优先考虑高效、经济的部署，他预测2026年将迎来由开放生态系统主导的“性能和效率时代”。

## PARK会是新的LAMP技术栈吗？

Zemlin还强调了他称之为PARK技术栈的出现：[PyTorch](https://thenewstack.io/why-pytorch-won/)、AI、[Ray](https://github.com/ray-project/ray)和Kubernetes。（[Ray是一个开源的分布式计算框架](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/)，用于简化人工智能和机器学习[ML]工作负载的扩展。）他认为，这一人工智能时代将定义未来的技术栈，就像LAMP技术栈定义了早期网络时代一样。他声称，PARK已经迅速成为大规模人工智能部署的默认平台。

他将这一时刻与Linux内核的演变进行了比较，全球开发者社区的集体压力反复推动了各种硬件的效率提升。在人工智能领域，[vLLM](https://docs.vllm.ai/en/latest/)和[DeepSpeed](https://github.com/deepspeedai/DeepSpeed)等开源工具现在正从GPU中榨取更多性能，降低功耗并减少每个token的成本。

“这正是开源真正擅长的地方，”Zemlin说。“改善每个token的价格和每千瓦的价格。”这也是开源软件有助于降低人工智能硬件基础设施不断增长的电力成本的地方。

Zemlin随后转向新兴的“代理（Agentic）”人工智能层，即自主规划、推理和行动的系统。Zemlin描述了一个仍处于萌芽阶段但正在围绕开放协议迅速形成规范的技术栈，包括[模型上下文协议（MCP）](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)和[Agent2Agent（A2A）](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)服务器的早期部署。

虽然目前只有少数组织在生产环境中使用MCP，但Zemlin表示2026年将迎来一波真正的企业自动化浪潮：多代理工作流、学习型编排、验证框架以及确定性系统和非确定性系统的新融合。

“代理（Agentic）人工智能不需要由模型大小决定，”他强调。“关键在于你如何架构解决方案。”

## “人工智能还没有发生太大变化”

Zemlin在主题演讲结束时强调，尽管炒作不断，“人工智能还没有发生太大变化。”他认为，改变它的是开放协作。

他说，开源可以防止供应商锁定，提高信任度和透明度，并为即将到来的可互操作人工智能系统时代提供“通用连接器”。他说，从训练到推理再到编排，Linux基金会打算与全球研究实验室和行业合作伙伴一起，成为这项工作的中心枢纽。

“我们非常非常激动能成为这个世界的一小部分，”他说，并承诺将有重大公告即将发布。