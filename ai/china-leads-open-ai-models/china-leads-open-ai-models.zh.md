大多数AI的焦点都集中在各大实验室推出的最大模型上——Anthropic 的 [Claude](https://thenewstack.io/claude-million-token-pricing/)、OpenAI 的 [GPT](https://thenewstack.io/gpt-54-nano-mini/) 以及 Google 的 [Gemini](https://thenewstack.io/googles-gemini-3-1-pro-is-mostly-great/)。这些系统以越来越大的模型和更长的上下文窗口设定了高端市场的节奏。

然而，一个与这些巨头并行的市场正在形成。开源模型——旨在被下载、适配并在不同环境中运行——在寻求对成本、部署和定制拥有更多控制权的开发者中持续获得采用。

这种活跃度或许在 [Hugging Face](https://huggingface.co/) 上最为明显，它是开发者分享模型、数据集和相关工具的首选平台。它 [功能上非常类似于 GitHub](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)，但专用于AI，使其成为观察开源模型实际使用情况的有用窗口。

直到最近，美国团体，包括 [Meta 的 Llama 系列](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/)，主导着这个生态系统的大部分。但 Hugging Face [在过去几个月](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-3) 持续提供的 [数据流](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment) 表明 [平衡已经发生转变](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment-blog-2)，中国正成为开源模型的主要生产者和使用者。

在其最新报告《[Hugging Face 开源现状：2026 年春季](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)》中，该公司强调了AI模型领域的几项转变——从开发者最常构建的系统，到大型科技公司在生态系统中的作用。但地理上的变化——重心转向中国——最为突出。

然而，这远非一个彻底的过渡：尽管中国在模型本身方面正在取得进展，但这些模型运行所需的基础设施仍牢牢掌握在英伟达手中。

## “DeepSeek 时刻”：中国开源AI的崛起

麻省理工学院和 Hugging Face 联合进行的一项 [研究](https://www.dataprovenance.org/economies-of-open-intelligence.pdf) 于去年11月发布，发现截至2025年8月，中国开发的开源模型下载量约占总量的17%，略高于美国的15.8%——这是中国首次在该指标上领先。但该结果仅限于一年的时间窗口。最新的 Hugging Face 数据表明，这种转变更为显著：中国现在在最近的月度下载量中处于领先地位，并且在过去大约四年累计的总下载量方面也已超越美国。

这种变化首先体现在使用量上。在2025年2月至2026年2月期间，中国模型占据了41%的下载量，而美国为36.5%。

![开源的地理分布](https://cdn.thenewstack.io/media/2026/03/90433d6e-downloadsgeogrpah-1024x576.png)

*开源的地理分布（图片来源：Hugging Face）*

这一转变部分是由 [DeepSeek R1](https://api-docs.deepseek.com/news/news250120) 等模型的病毒式传播推动的。该模型于2025年1月发布后 [风靡AI界](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/)，以更低的成本提供了可与领先系统媲美的性能，并开放了权重供开发者运行和适配。

最终，这 [被证明是中国其他公司的催化剂](https://huggingface.co/blog/huggingface/one-year-since-the-deepseek-moment)。例如，百度在2024年没有在 Hugging Face 上发布任何内容，但在 [2025年](https://finance.yahoo.com/news/baidu-launches-ai-models-touts-093000740.html) 发布了100多个。根据 Hugging Face 的数据，TikTok 的母公司字节跳动和腾讯各自的输出量增长了多达9倍。而此前专注于封闭系统的公司，如 [MiniMax](https://www.minimax.io/)，也 [开始公开发布模型](https://www.minimax.io/news/minimaxm1)。

周三，中国智能手机制造商小米发布了 [MiMo-V2-Pro](https://mimo.xiaomi.com/mimo-v2-pro)，一个万亿参数模型，声称其性能接近领先的美国系统，但成本仅为一小部分，并 [计划在模型稳定后发布开放权重](https://x.com/_LuoFuli/status/2034379957913129140)。

中国发布量的激增也反映在部署数据中。一份来自 [RunPod 的报告](https://thenewstack.io/runpod-ai-infrastructure-reality/) 追踪了其基础设施的使用情况，发现阿里巴巴的 Qwen 模型已超越 Meta 的 Llama，成为部署最广泛的自托管大型语言模型。

同样的情况也出现在 Hugging Face 本身，体现在开发者选择在其基础上进行构建的模型。包括 Qwen 在内的阿里巴巴模型已经衍生出超过10万个派生模型，反映了这些系统被广泛适配和重用的程度。

![Hugging Face 上按组织划分的派生模型](https://cdn.thenewstack.io/media/2026/03/044751aa-derivaites-1024x576.png)

***Hugging Face 上按组织划分的派生模型（图片来源：Hugging Face）***

另一个信号来自开发者对平台上模型的反应。在 Hugging Face 上，“点赞”是一个简单的受欢迎程度信号——显示哪些模型正在吸引注意力。

一年前，最受欢迎的模型主要集中在 Meta 的 Llama 模型，它们占据了前五名中的三个位置。12个月后，中国的 DeepSeek-R1 现在位居第一，同时还有来自美国以外的更广泛的模型组合出现在顶级排名中。

![Hugging Face 上最受欢迎的模型](https://cdn.thenewstack.io/media/2026/03/c1c8f61c-sentiment.png)

*Hugging Face 上最受欢迎的模型（图片来源：Hugging Face）*

可以说，用户情绪已从 Meta 转向了来自中国、德国和英国的更广泛参与者。

## 英伟达与硬件因素

可以说，AI热潮中出现的最大故事之一就是英伟达——这家芯片设计公司曾以其游戏显卡而闻名，如今已能 [充分利用对用于训练和运行AI模型的GPU需求的激增](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/)。如今，英伟达是迄今为止全球市值最高的上市公司，其市值在 [去年曾达到超过5万亿美元的峰值](https://www.cnbc.com/2025/10/29/nvidia-on-track-to-hit-historic-5-trillion-valuation-amid-ai-rally.html)。

然而，硬件只是故事的一部分。英伟达一直在 [向上层堆栈推进](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)，开发自己的软件、模型和工具，旨在塑造AI系统的构建和部署方式——此举是为了将开发者更紧密地绑定到其生态系统中。

在 Hugging Face 上，这种推动也体现在该公司不断增长的代码库数量上。到2025年底，英伟达已 [在该平台建立了超过350个代码库](https://aiworld.eu/story/big-tech-is-all-in-on-open-source-ai-)——超过了任何其他被追踪的组织——反映了其贡献随时间稳步增加。

![英伟达在 Hugging Face 存储库数量中居首](https://cdn.thenewstack.io/media/2026/03/1a0c3ef5-screenshot-2026-03-20-at-11-48-38-state-of-open-source-on-hugging-face-spring-2026.png)

*英伟达在 Hugging Face 存储库数量中居首（图片来源：Hugging Face）*

这种增长很大程度上反映了英伟达近期如何将其影响力从硬件扩展到软件和模型层。这包括其 Nemotron 模型家族以及 NemoClaw 等项目，后者是一个用于AI代理的开源平台。

现实情况是，大多数AI模型仍然设计为在英伟达GPU上运行。尽管对替代硬件的支持正在改善——[包括AMD系统](https://www.cnbc.com/2025/10/08/amd-deal-with-openai-gives-nvidia-a-needed-challenger-in-ai-chips/)，以及 [中国公司开发](https://spectrum.ieee.org/china-ai-chip) 的芯片越来越多——但生态系统的大部分仍然依赖英伟达的架构。

这种依赖性有助于解释英伟达为何在该领域投入巨资。该公司已制定了数百亿美元与AI基础设施相关的支出计划，包括 [据报道未来五年260亿美元的投资](https://www.fool.com/investing/2026/03/12/nvidia-is-making-a-massive-26-billion-bet-on-the-f/) 用于开发开源AI模型，这凸显了其业务与模型使用增长的紧密关系。逻辑很简单：如果这些模型是为英伟达硬件优化的，它们就会增强该公司对AI堆栈的更广泛控制。

与此同时，一些推动开源模型采用的中国公司也在努力减少对美国硬件的依赖。例如，阿里巴巴 [一直在投资](https://www.networkworld.com/article/4049120/alibaba-is-developing-an-ai-inference-chip-amid-us-export-curbs.html) 专注于推理的芯片，旨在在国内数据中心运行开源模型。然而，这些努力仍处于早期阶段，尚未取代现有堆栈。

目前，这留下了一个明显的分界线。在模型层面，Hugging Face 数据显示中国开发者在产出和采用方面都在取得进展。但在基础设施层面，英伟达仍然是这些模型如何运行的核心。

这是一个来自云计算的熟悉故事：少数美国公司控制着大部分底层基础设施，尽管其他公司试图构建替代方案。 [欧洲正在努力](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/900014236/How+the+DIGITAL+Building+Blocks+can+help+bring+EuroStacks+vision+of+European+digital+sovereignty+to+life) 减少对这些提供商的依赖，但 [迄今为止成功有限](https://www.theregister.com/2026/02/20/ditching_aws_euro_stack/)。

同样的担忧现在也出现在AI领域，它位于相同的云层之上。开源模型可能正在野火般蔓延，但归根结底，它们仍然运行在他人的机器上——无论哪个国家在引领潮流。