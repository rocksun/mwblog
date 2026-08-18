<!--
title: 开放模型现状：2026年夏季观察报告
cover: https://huggingface.co/blog/assets/state-of-open-models-summer-2026/thumbnail.png
summary: 本报告分析了2026年上半年AI模型生态。核心发现包括：中国实验室在参数规模上领先并主导前沿，开源重心由模型厂商转向硬件与基础设施公司。小型模型仍是实际应用主力，而Qwen系列凭借生态覆盖成为社区首选基础模型。此外，AI智能体正迅速成为Hugging Face平台的核心用户。
-->

本报告分析了2026年上半年AI模型生态。核心发现包括：中国实验室在参数规模上领先并主导前沿，开源重心由模型厂商转向硬件与基础设施公司。小型模型仍是实际应用主力，而Qwen系列凭借生态覆盖成为社区首选基础模型。此外，AI智能体正迅速成为Hugging Face平台的核心用户。

> 译自：[State of Open Models: Summer 2026 Observations](https://huggingface.co/blog/state-of-open-models-summer-2026)
> 
> 作者：Adina Yakefu, Apolinário from multimodal, Irene Solaiman

在人工智能领域，时间感被严重压缩。在我们半年一度的分析报告——[春季报告](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)发布几个月后，我们观察到了截至今年夏季的一系列新发现。本报告梳理了2026年1月至8月间的这些观察结果，并提供了数据支持。

[![2026年按任务类别划分的Hugging Face数据集累计增长情况，达到一百万个](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/dataset-growth.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/dataset-growth.png)

Hugging Face Hub 上的模型和数据集在每日增长。在此期间，公共模型仓库从243万个增长到296万个，数据集从71.1万个增长到100万个，Spaces 从100万个增长到144万个。底层的分布仍然极端：约85.6%的模型生命周期内下载量不足200次，而1.5%的仓库贡献了99.2%的总下载量。以下所有内容都发生在这种态势之下。

## **1. 前沿领域推进迅速**

过去曾有一条清晰的发展路径：实验室先发布较小的模型，逐渐向顶端规模演进。在2026年，几家中国实验室完全跳过了这一过程。

[![2026年各月中国与美国实验室发布的最大开放模型](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/frontier-ceiling-by-country.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/frontier-ceiling-by-country.png)

**在2026年的几乎每个月，中国实验室发布的最大、性能最强的开放模型都超过了美国实验室同期发布的任何模型。** 中国的月度峰值参数量在7540亿到2.78万亿之间；而美国在7个月中有5个月的峰值保持在1300亿以下，例外是NVIDIA 5月份和6月份发布的5610亿参数的 [Nemotron 3 Ultra](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3)，以及 Thinking Machines Lab 的 [Inkling](https://huggingface.co/collections/thinkingmachines/inkling)。

[![每个实验室都有不同的规模策略](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/lab-size-strategy.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/lab-size-strategy.png)

该图表将实验室分为两个阵营。[Moonshot](https://huggingface.co/moonshotai)、[MiniMax](https://huggingface.co/MiniMaxAI)、[Xiaomi](https://huggingface.co/XiaomiMiMo) 和 [Z.ai](http://Z.ai) 几乎不发布低于700亿参数的模型，因此开发者首次接触它们时，模型往往大到无法在自有设备上运行。相反，[Tencent](https://huggingface.co/tencent) 和 [Alibaba Qwen](https://huggingface.co/Qwen) 则覆盖了从10亿以下到更高参数的全谱系。

两件事使第一个阵营成为可能。构建大型模型不再是竞争优势。Xiaomi 和 [Meituan](https://huggingface.co/meituan-longcat) 今年都突破了万亿参数，而在一年前，它们在开源权重领域还鲜为人知。此外，实验室不再需要发布小型模型来建立影响力，因为社区的量化层会在几天内让大型模型变得可运行，这是我们稍后会讨论的一个依赖项。

这使得规模配置成为一种意图声明，而非能力证明。前沿专属投资组合将一切押注在基准测试排名和 API 需求上。全谱系投资组合则旨在成为开发者标准化的首选家族。两者都是理性的，只是追求的目标不同。

与此同时，美国并未缺席开源。

[![新的本土模型](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/new-homegrown-models.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/new-homegrown-models.png)

今年发布最多新开放模型的两家机构恰好也是硬件制造商：[AMD](https://huggingface.co/amd) 和 [NVIDIA](https://huggingface.co/nvidia)。每一家都发布了超过200个新的模型仓库，远超其他竞争对手，[LiquidAI](https://huggingface.co/LiquidAI) 以约100个位居第三。硬件供应商已经意识到，开放模型是销售芯片的一种方式：一个为你的硬件优化且可免费使用的模型，是证明硬件性能最直观的证据。

当算上小型模型和嵌入模型时——Google、Microsoft、IBM Granite 以及 OpenAI 的旧版视觉和语音模型每年产生数以亿计的下载量——**美国在开源 AI 领域的参与度仍在增长。**

然而，重心已经发生了转移。尽管 Google 和 Meta 是前几年定义了开放模型发布的公司，但它们在新模型发布量上如今已远低于 NVIDIA。Meta 向闭源旗舰模型的转向进一步凸显了这一变化。开源已从模型实验室转向了**硬件和基础设施公司**。

在前沿规模上，情况大不相同。今年美国发布的大多数超过1000亿参数的模型并非新原创模型，而是基于中国模型构建的。在这个规模上，只有少数主要的美国原创模型：Thinking Machines 的 [Inkling](https://huggingface.co/collections/thinkingmachines/inkling) (9520亿)、NVIDIA 的 [Nemotron 3 Ultra](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3) (5610亿)、[Nemotron 3 Super](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3) (1240亿) 以及 Arcee AI 的 [Trinity-Large](https://huggingface.co/collections/arcee-ai/trinity-large-thinking) (3990亿)。

AMD 贡献了许多转换版本，但在此规模上没有原创模型。这项工作仍然重要：它使万亿参数的中国模型能够在美式硬件上高效运行。但这代表了**分发和优化层，而非模型创建**。

与此同时，中国的开放模型正日益针对国产芯片进行优化，这是一种反向竞争，模型围绕特定的硬件生态系统进行设计。

## **2. 关注度 ≠ 采用率**

我们统计了今年下载量排名前25的模型仓库和点赞数排名前25的仓库。**仅有一个仓库同时出现在这两个列表中。**

**[![关注和使用是两种不同的经济体系](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/attention-vs-usage.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/attention-vs-usage.png)**

我们统计的是窗口期内的下载量而非生命周期总下载量，因此没有任何模型因为存在时间长而占优，控制变量后这种分化更加明显。2026年发布的模型中，没有一个进入下载量前25名，而前25名中有13个源自2022年。[all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) 在七个月内被拉取了15.5亿次，仅收获5,156个赞；[Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) 每获得一个赞，大约被拉取60次。

这两个数字记录了不同的行为。点赞意味着某个发布很重要，通常流向前沿模型发布后的几周内。下载则意味着某个东西被接入了按计划运行的流水线，并随着时间推移在小型、稳定的模型上积累。点赞是阅读领域热点的有效工具，而下载则是阅读当前依赖关系的工具。将两者互为代理是我们观察到的关于 Hub 的报道中最常见的错误，包括我们自己早期的工作。同样的鸿沟也出现在发布者层面。

[![谁在下载什么](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/downloads-by-lab-and-model-size.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/downloads-by-lab-and-model-size.png)

中国的前沿实验室是 Hub 上唯一重型模型占据下载量主流的账号。MiniMax 2026年几乎所有的下载量都来自700亿参数以上的模型，Moonshot 占比88%，DeepSeek 占比55%，Z.ai 占比39%。没有任何大型美国账号呈现这种特征：Google、Microsoft 和 IBM Granite 在2026年的下载量中，700亿参数以上模型几乎为零，NVIDIA 和 Meta 分别仅占14%和9%。

这种差异在总下载量中体现得更为明显。Moonshot 的纯前沿投资组合在一年内录得3700万次下载，而 Qwen 跨模型规模的广泛发布策略达到了20.45亿次（按声明参数计算的仓库，若包含所有仓库则为20.61亿次），大约是前者的55倍。从2.4万亿参数的 Qwen 3.8 Max 到270亿等小型变体，该家族的持续扩张显示了其对不同使用场景覆盖的专注。

时间也起着重要作用。大多数模型在发布后使用量会急剧下降，随后进入长期稳定的尾部阶段。模型的采用率很大程度上在最初几个月内决定。

这有助于解释为什么今天的下载量往往不是由最新发布驱动的，而是由一小群随着时间推移已成为基础设施的模型驱动的。

## **3. 开放权重正在改变价值积累的方式**

如果前沿模型是授权业务，你会期望最大的发布版本带有最严格的条款。然而，以下数据揭示了不同的情况。

[![许可证并非商业模式](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/model-licenses-by-region-and-size.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/model-licenses-by-region-and-size.png)

在今年超过200亿参数的178个中国模型发布中，59%采用 Apache 2.0，22%采用 MIT，**且完全没有一个带有非商业限制条款。**

DeepSeek 和 Z.ai 以纯 MIT 协议发布了7000亿到1.65万亿参数的模型。中国实验室对最大模型的许可方式与最小模型一样宽松，且比美国实验室对其模型的许可方式更为宽松：在美国同等规模范围内，29%使用 Apache 或 MIT，41%受定制条款限制，30%没有声明。

无论这些发布的目的是什么，显然不是为了授权收入。权重以目前最宽松的条款免费提供。回报必然来自其他地方：**API 和云业务、硬件和平台定位，或生态系统地位本身。** 例如，Z.ai 和 Kimi 的估值指向了一种有效的开源策略，即在社区中获得牵引力和增长机会。然而展望未来，行业可能会转向从开源采用中获取更清晰的商业化路径。

## **4. Qwen 已成为社区的基础模型**

一个模型的生态地位不仅由其自身的发布决定，还由社区在其基础上构建的程度决定。如上所述，Qwen 是一个获得关注和采用的例外。

[![按组织划分的Hugging Face衍生项目](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/derivatives-by-organization.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/derivatives-by-organization.png)

来自 Hugging Face 的数据

以此衡量，Qwen 已成为开放模型生态系统中最大的基础之一。基于 Qwen 的模型在 Hub 上现在占据了 **151,448 个衍生项目**，是 Meta 总足迹的2.6倍，专门针对 Llama 仓库的4.7倍。Google 以82,506个衍生项目紧随其后。第三大来源是 Unsloth，一个发布量化和准备好微调的构建版本的社区账号，其中许多进一步扩展了 Qwen 生态系统。

在2026年的前七个月中，Qwen 衍生项目以每天约 **180–210 个新仓库**的速度增长，这表明采用率不仅仅是由个别发布驱动的。Qwen 已成为开发者决定微调和部署什么模型时的默认工作流程的一部分。

几个因素促成了这一地位。**首先是连贯性。** Qwen 保持了定期的发布节奏，持续更新其模型家族，而不是依赖偶尔的旗舰发布。**其次是覆盖范围。** 它发布了跨越多种规模和用例的模型，使开发者无论需要小型本地模型还是大型部署模型，都能留在同一个生态系统中。**第三是开放性。** Apache 2.0 许可减少了修改、再分发和商业使用的阻力。

这些因素相辅相成。广泛的模型家族吸引了更多开发者；更多开发者创建了更多衍生项目；而这些衍生项目使生态系统对未来的用户更具吸引力。

这一地位很大程度上是由社区构建的。**151,448 个衍生项目**代表了其他开发者所做的下游工作，而非 Qwen 本身产出的发布。即使在 Hub 上 **28,531 个 Qwen 模型的 GGUF 转换版本**中，Qwen 自己也仅发布了54个。

## **5. 小型模型仍是实际层面的基石**

在声明了参数数量的模型中，10亿参数以下的模型占据了历史总下载量的83%，而1000亿以上的模型仅占1%。仅限定在2026年积累的下载量情况也没变：3%的流量流向了700亿参数以上的模型。这是3月份的发现，且保持得非常稳固，原因与之前相同：小型模型是唯一能在开发者实际拥有的硬件上运行的模型。

[![下载量依然属于小型模型](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/downloads-by-model-size.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/downloads-by-model-size.png)

那么，万亿参数的模型是如何触达用户的呢？通过 llama.cpp。

2月，ggml 团队[加入了 Hugging Face](https://huggingface.co/blog/ggml-joins-hf)，该项目保持完全开源、社区治理并保持相同的技术方向。改变的是，本地推理领域最重要的项目现在拥有了持久的资源支持。

[![2026年 Hub 上的 llama.cpp](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/llama-cpp-hub-growth.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/llama-cpp-hub-growth.png)

上限随 llama.cpp 而移动。7月份的快照包含了约2840亿参数的 DeepSeek-V4-Flash 和约2.8万亿参数的 Kimi-K3 的 GGUF 构建版本。本地推理过去意味着笔记本上的80亿参数模型。现在它意味着跨越几台消费级机器运行的万亿参数混合专家模型，这是前沿领域一年前没有的替代路径，也是前沿优先发布策略能够可行的原因。

[![人们在本地实际运行的内容](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/local-downloads-by-model-family.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/local-downloads-by-model-family.png)

这条路径运行在 Qwen 之上：每月3960万次 GGUF 下载，几乎是 Gemma 的2080万次的两倍，是 Llama 的750万次的五倍以上。Llama 的差距不是供应问题，Llama 衍生的 GGUF 仓库数量略多于 Qwen。相同的货架空间，只有五分之一的流量。

模型仓库在这七个月内增长了21.5%。其周边的几样东西增长速度快了几倍。

[![运行时层增长最快](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/runtime-layer-growth.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/runtime-layer-growth.png)

声明 gguf 库的仓库增长了464%，lerobot 增长了194%，Apple 的 mlx 增长了148%，而 transformers 和 peft 增长了16%，diffusers 增长了21%。模型核心的增长大致符合平台平均水平。决定模型能在哪里物理运行的层——本地推理格式、Apple 芯片、机器人控制栈——的增长速度是平均水平的3到7倍。

在十大模型家族中，这些模型的背后实验室发布了极少的官方 GGUF 转换。然而，GGUF 版本往往是开发者在本地运行模型时使用的版本。在发布时提供官方转换、记录量化选择并签署制品，所需付出的额外努力是有限的。与其内部维护此工作流程，实验室可以与现有的生态系统贡献者（如 Unsloth）合作。这样做将缩小模型创建者测试的权重与更广泛社区采用的版本之间的差距。

## **6. 智能体成为新用户**

我们在3月份写不出这一部分，因为当时的工具不存在。[agent-usage](https://huggingface.co/datasets/huggingface/agent-usage) 数据集于7月发布，记录了编码智能体在通过 huggingface_hub 或 hf CLI 调用 Hub 时发送的 agent/<name> token——搜索模型、推送数据集、运行任务、创建 Spaces。我们第一次能够看到 Hub 接收到多少智能体流量以及来自哪些套件。

[![智能体调用 Hugging Face Hub](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/agent-hub-traffic.png)](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/state-of-open-models-summer-2026/agent-hub-traffic.png)
Claude Code 在7月以44.4%的占比领先，但单月数据掩盖了真实发现：它在4月份占比67.8%，5月份占比6.4%，而 Codex 从10.4%稳步攀升至20.8%。这是一个没有既定胜者的市场，一个发布或一个默认设置的改变可以在一个月内改变一半的流量。

第二个发现是未注册行。7月份近四分之一的智能体标记流量来自数据集尚未命名的套件，而在5月份这一数字为59.8%。在4月到7月之间，出现了十几多个新的客户端标识符。新进入者出现的速度比任何注册表命名它们的速度都要快——这本身就是发现。

我们今年花了大部分时间为这类阅读者（而非仅仅是人类浏览器）构建功能。论文于3月开始提供机器可读的 Markdown。4月带来了[作为一级数据集类型的智能体追踪数据](https://huggingface.co/changelog/agent-trace-viewer)，并在每个 Gradio Space 上添加了 agents.md 端点，以便智能体可以读取 Space 的 API 并直接调用它。7月带来了我们 MCP 服务器上的 [hf_fs 工具](https://huggingface.co/changelog/mcp-improvements-jul-26)，通过单一接口在短短一千多个 token 内暴露仓库、存储、文档和论文，并附带用于安全执行的可附加沙箱。同样的整合发生在协议层，MCP 移入了 Linux 基金会的 Agentic AI Foundation。

然后，在7月，智能体不再仅仅是阅读者，而是成为了入侵者。据我们所知，第一例由自主智能体主动发起持续入侵的记录发生在我们的平台上。当我们的团队试图使用闭源前沿模型来分析捕获的攻击代码时，其安全护栏拒绝了这项工作。最终，分析工作是在我们自己的基础设施上运行的量化开放模型 GLM-5.2 上完成的。我们发布了一份[披露信息](https://huggingface.co/blog/security-incident-july-2026)和完整的[技术时间线](https://huggingface.co/blog/agent-intrusion-technical-timeline)。

## **展望未来**

与春季报告相比，权力的地理重新平衡继续加速。虽然美国的开源模型继续存在，但几种中国前沿模型的竞赛也在社区中引起了强烈关注。这些前沿模型上的许多点赞指向了最让社区兴奋的事物，以及利用这种关注度进行估值的公司的增长机会。

然而，AI 竞赛不仅是短跑，也是马拉松。像 llama.cpp 这样的工具帮助在本地部署大型模型，但广泛的模型家族及其采用仍然是关键，以构建开发者、发布者和未来用户之间的正向反馈循环。将模型嵌入基础设施并成为生态系统的一部分，可能最终通向商业上稳健的终局。

最后，随着智能体首次成为 HF hub 上的第一大用户，下一份报告看起来可能会有很大不同。

正如在 AI 领域，几个月的时间就能重塑生态系统。

---

### **方法论说明**

本分析基于2026年前七个月在 Hugging Face Hub 上观察到的活动。

本报告中使用的指标，包括下载量、点赞数、衍生项目和模型发布，代表了生态系统活动的不同方面。它们不应被解释为衡量模型质量、商业采用或整体市场份额的直接标准。

下载量表明了 Hub 生态系统内的使用情况，但它们没有捕获 API 使用、私有部署或通过其他渠道分发的模型。

点赞反映了社区的关注和兴趣，而衍生模型则提供了开发者在现有模型基础上构建程度的信号。

由于开源 AI 的采用发生在许多渠道，Hub 活动应被视为生态系统发展的一个视角，而非 AI 市场的完整衡量指标。