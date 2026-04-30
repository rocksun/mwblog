<!--
title: AWS 引入 OpenAI 模型，但 Trainium 芯片才是其背后的真正杀手锏
cover: https://cdn.thenewstack.io/media/2026/04/57245e0e-rezza-alam-fv5hjpkgboe-unsplash-scaled.jpg
summary: AWS宣布在Bedrock集成OpenAI的GPT-5等模型。然而，真正的战略重点在于Anthropic与OpenAI均大规模承诺使用AWS自研的Trainium芯片。这标志着AI竞争进入定制芯片层级，AWS借此在推理成本和供应安全上获得了结构化优势。
-->

AWS宣布在Bedrock集成OpenAI的GPT-5等模型。然而，真正的战略重点在于Anthropic与OpenAI均大规模承诺使用AWS自研的Trainium芯片。这标志着AI竞争进入定制芯片层级，AWS借此在推理成本和供应安全上获得了结构化优势。

> 译自：[AWS lands OpenAI on Bedrock, but Trainium is the real story](https://thenewstack.io/openai-bedrock-trainium-silicon/)
> 
> 作者：Janakiram MSV

AWS 终于为那些希望在不离开亚马逊生态系统的情况下使用 OpenAI 模型的开发者缩小了差距。在本周于旧金山举行的一场活动中，AWS 首席执行官 Matt Garman 揭晓了三项重大的 Bedrock 集成——其中最引人注目的是 OpenAI GPT-5 系列的加入——旨在终结开发者在 AWS 基础设施和 OpenAI 顶尖智能之间的艰难抉择。

以下是 Matt Garman 在台上的表述：“在过去的几年里，我们强迫他们为了获得优秀的 OpenAI 模型而不得不去其他地方，他们并不喜欢那样。现在，我认为我们不再强迫人们必须做出那样的选择。”

所有三项新产品目前均处于有限预览阶段，首先是最新的 OpenAI 模型：GPT-5.4 现已可用，GPT-5.5 预计将在未来几周内推出。此外，OpenAI 的编程智能体 Codex 也加入了 Bedrock 阵容，该工具目前每周已有 400 万用户。最后，在 2 月份首次预告的“有状态运行时环境”已正式产品化为由 OpenAI 驱动的 Amazon Bedrock 托管代理（Managed Agents）。

## 没人点明的细节

在活动开始的八天前，即 4 月 20 日，AWS 与 Anthropic [宣布扩大合作](https://thenewstack.io/anthropic-amazon-aws-investment/)。Anthropic 承诺在未来十年内向 AWS 投入超过 1000 亿美元。新闻稿中的措辞至关重要：Anthropic 获得了高达 5 吉瓦（GW）的新容量，用于训练和运行 Claude。

这一承诺涵盖了从 Graviton 到 Trainium2 再到 Trainium4 的芯片。Andy Jassy 在[新闻稿](https://www.anthropic.com/news/anthropic-amazon-compute#:~:text=%E2%80%9CAnthropic%27s%20commitment%20to%20run%20its%20large%20language%20models%20on%20AWS%20Trainium%20for%20the%20next%20decade%20reflects%20the%20progress%20we%27ve%20made%20together%20on%20custom%20silicon%2C%20as%20we%20continue%20delivering%20the%20technology%20and%20infrastructure%20our%20customers%20need%20to%20build%20with%20generative%20AI.%E2%80%9D)中的引言证实了这一点：“Anthropic 承诺未来十年在 AWS Trainium 上运行其大语言模型，这反映了我们在定制芯片上共同取得的进展。”

八天后，OpenAI 的发布同样是一个关于 Trainium 的故事。本周活动所产品化的 2 月份交易，使 OpenAI 承诺消耗约 2 吉瓦的 Trainium 容量，涵盖 Trainium3 和 Trainium4。（据 *The Register* 报道，2GW 的承诺也与[亚马逊剩余的 350 亿美元投资](https://www.theregister.com/2026/04/28/openai_climbs_into_amazons_bedrock/)挂钩，尽管亚马逊的官方文本仅表示第二阶段投资取决于“某些条件”，并未披露具体内容。）

> 两家在每个基准测试、每个架构选择和每个安全理念上都存在竞争的 AI 实验室，刚刚对同一个定制芯片路线图做出了平行的多年期承诺。

两家在每个基准测试、每个架构选择和每个安全理念上都存在竞争的 AI 实验室，刚刚对同一个定制芯片路线图做出了平行的多年期承诺。这两家实验室都不是排他性的。Anthropic 仍在使用[来自 Google 的 TPU 和 NVIDIA GPU](https://www.anthropic.com/news/anthropic-amazon-compute)，而 OpenAI 仍将 Microsoft 作为其主要的云合作伙伴。但 AWS 在同一窗口期内，基于 AWS 设计的芯片所获得的这种平行规模的承诺，是一个值得关注的特定事件。

## 为什么这不同于 Azure 的故事

Microsoft 会通过提醒每个人 [Foundry 同时拥有 Claude 和 GPT](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/) 来做出回应。确实如此，Microsoft 在 2 月份就提出了这一说法。但这种比较在工作负载层面上并不成立。

[Anthropic 自身关于 Foundry 集成的文档](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)显得异常直接。“预览”部分指出，Foundry 上的 Claude 模型运行在 Anthropic 的基础设施上。Foundry 处理计费、身份验证和 Azure 托管的端点，而推理则发生在别处。

相比之下，查看 Anthropic 的 [Bedrock 文档](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)，第一行写道：“Amazon Bedrock 中的 Claude 运行在 AWS 托管的基础设施上，操作员零访问。”Anthropic 的人员无法访问推理基础设施，模型运行在 AWS 的安全边界内。这是一种完全不同的部署模式。

> 与一周前相比，Bedrock 现在对 Claude 和 OpenAI 模型的云原生推理拥有更强的结构化主张。

同样的区别现在也适用于 OpenAI。在 Foundry 上，OpenAI 的推理多年来一直是 Azure 原生的。而在 Bedrock 上，根据数吉瓦的 Trainium 承诺，OpenAI 的推理正在迁移到 AWS 基础设施上。Foundry 的区别对 Claude 而言是真实存在的；对于 OpenAI，现在断言 Bedrock 拥有工作负载还为时过早。但可以肯定的是，与一周前相比，Bedrock 现在对 Claude 和 OpenAI 模型的云原生推理拥有更强的结构化主张。

## 芯片趋同

两年来，云端 AI 的话题一直围绕着模型选择：Anthropic 对阵 OpenAI 对阵 Google；Bedrock 对阵 Foundry 对阵 Vertex。支撑这一切的芯片在很大程度上一直是 NVIDIA 的 GPU，Google 的 TPU 是主要的替代方案，而 AWS Trainium 在 Anthropic 的技术栈中也占据了一席之地。

定制芯片是新的竞争层级。AWS 成功让两家顶尖实验室都承诺了其芯片路线图，而这种架构并非偶然。Anthropic [与 AWS 的芯片设计团队 Annapurna Labs 密切合作](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai)，工程团队“几乎每天都在沟通，从底层优化工作到下一代芯片的高层架构决策”。OpenAI 的承诺也延伸到了未来的 Trainium 世代，包括在 re:Invent 2025 上宣布的 [Trainium3 UltraServers](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-anthropic-meta-partnership-aws-lambda-s3-files-amazon-bedrock-agentcore-cli-and-more-april-27-2026/) 以及正在开发中的 Trainium4。

战略意图显而易见。Trainium 改变了 AWS 上 AI 推理的利润结构。虽然目前大多数工作负载仍由 Nvidia 的 GPU 提供支持，但每一吉瓦迁移到 Trainium 的容量，都意味着 AWS 能比纯粹使用 NVIDIA 芯片捕获更多的芯片利润。Andy Jassy 在最近的股东信中透露，AWS 的定制芯片业务[每年产生超过 200 亿美元的收入](https://www.geekwire.com/2026/openais-models-land-on-amazon-bedrock-one-day-after-microsoft-exclusivity-ends/)。Trainium 路线图不再仅仅是一个研究项目。

对于实验室自身而言，考量因素是供应安全。Anthropic [报告的运营年收入为 300 亿美元](https://www.anthropic.com/news/anthropic-amazon-compute)，高于 2025 年底的约 90 亿美元。算力容量是核心瓶颈。Trainium 能够按计划交付承诺的吉瓦容量。在全球范围内，GPU 的供应依然紧张且竞争激烈。

## 本周发布的内容

Bedrock 上的这三款产品全部运行在 AWS 基础设施内部。

Bedrock 上的 OpenAI 前沿模型继承了 AWS 客户已在使用的[全套企业控制功能](https://www.aboutamazon.com/news/aws/bedrock-openai-models)。包括基于 IAM 的访问管理、AWS PrivateLink 连接性、防护栏（guardrails）、加密、CloudTrail 日志记录以及现有的合规框架。客户可以将 OpenAI 的使用量计入现有的 AWS 云承诺额度中。无需单独采购，也无需新的安全模型。

通过将 Codex 引入 AWS 安全边界，开发者现在可以使用原生 AWS 凭证和基础设施运行 OpenAI 的编程智能体。这种集成确保所有推理都通过 Bedrock 运行，使用成本直接计入现有的 AWS 云承诺。此外，Codex 命令行界面（CLI）、桌面应用和 Visual Studio Code 扩展已更新，以原生支持 Bedrock 端点。

Bedrock 托管代理（Managed Agents）是这三者中在架构上最有趣的。该产品基于 OpenAI 智能体套件（harness）构建，AWS 副总裁 Anthony Liguori 在台上将其描述为 OpenAI 内部使用的运行时、环境和推理 API。

AWS [自身描述](https://aws.amazon.com/about-aws/whats-new/2026/04/bedrock-openai-models-codex-managed-agents/)称该套件“旨在实现更快的执行、更敏锐的推理以及对长时间运行任务的可靠引导”。该套件针对 OpenAI 前沿模型进行了优化。智能体获得了跨会话持久的内存、强制执行权限的身份、编码程序的技能，以及根据任务大小调整的计算选项。AgentCore 提供了默认的计算环境，并在其上层叠了授权执行和可观测性。

与其它智能体平台相比，这是模型与运行时之间更紧密的耦合。这是否能在生产中转化为可衡量的性能提升仍有待观察。

## 诚实的注意事项

在这一框架被过度解读之前，需要指出三点。

两家实验室都运行多云策略。Anthropic [在 2026 年 3 月与 Google 和 Broadcom 达成的交易](https://www.anthropic.com/news/anthropic-google-cloud-tpu)增加了“数吉瓦”将于 2027 年上线的 TPU 容量。Anthropic 在 2025 年 11 月还对 [Azure 达成了 300 亿美元的承诺](https://news.microsoft.com/source/2025/11/anthropic-microsoft-nvidia-strategic-partnerships/)。根据[ 4 月 27 日修订后的协议](https://stratechery.com/2026/an-interview-with-openai-ceo-sam-altman-and-aws-ceo-matt-garman-about-bedrock-managed-agents/)，OpenAI 仍将 Microsoft 作为其主要云合作伙伴，并承诺未来几年在 Azure 上进行大量消耗。5GW 和 2GW 的 Trainium 数字虽然巨大，但并不是两家实验室使用的唯一芯片。

Trainium 在 OpenAI 的训练规模上尚未经过实战检验。Trainium2 已投入生产，Trainium3 于 [2025 年 12 月发布](https://aws.amazon.com/about-aws/whats-new/2025/12/aws-trainium3-ultraservers-generally-available/)，而 Trainium4 尚未投入商用。Anthropic 已经通过 [Project Rainier](https://www.aboutamazon.com/news/company-news/amazon-invests-additional-5-billion-anthropic-ai)（全球最大的 AI 计算集群之一）在 Trainium2 上训练和提供 Claude 服务。我还没有发现 OpenAI 在 Trainium 上端到端训练前沿模型的公开证据。在实现这一点之前，“OpenAI on Trainium”主要还是一个关于推理和容量预留的故事。

此外，AWS 仍将 Nova 作为第一方模型。其中立货架的定位是有限度的。即使 AWS 在芯片层与这两个合作伙伴共同办公，在模型层依然与他们竞争。

## 其他云厂商现在必须回答的问题

Microsoft 拥有 OpenAI 的股份，且仍是其主要云合作伙伴。但 Microsoft 目前还没有像 AWS 那样，在 Microsoft 定制芯片上承载大规模的 OpenAI 训练和推理工作负载。Microsoft 的 Maia 芯片计划虽然存在，但公开记录并未显示有同等级别的实验室承诺。

Google 拥有 TPU 并在其上大规模运行 Anthropic。但 Google 尚未宣布 OpenAI 对其定制芯片有类似的承诺。此外，Google 将 Gemini 作为第一方旗舰模型运行，这使得 Vertex 看起来不像是一个中立货架，更像是一个 Google 化的货架。

> 史上第一次，你可以在 Claude 和 GPT 之间做出选择，而无需在云服务商、运行时或芯片路线图之间做出权衡。

Nvidia 在每一个云端依然是赢家。但最大云服务商的推理利润底线已经发生了位移。每一吉瓦上线的 Trainium 产能，都意味着 AWS 在芯片栈中捕获的价值超过了纯粹使用 NVIDIA 的方案。

对于在 Bedrock 上构建应用的开发者来说，实际的变化比标题所示更加深刻。史上第一次，你可以在 Claude 和 GPT 之间做出选择，而无需在云服务商、运行时或芯片路线图之间做出权衡。Anthropic 和 OpenAI 现在都绑定了多年的 Trainium 承诺，且都拥有与其模型提供商共同设计的托管智能体运行时。锁定是真实的，选择也是真实的，而且它们正同时发生。

称之为芯片趋同。在“OpenAI 登陆 Bedrock”这个标题下的故事是：世界上最具竞争力的两家 AI 实验室，现在已经锚定了对 AWS 设计芯片的多年承诺。正是这一协议促成了今天的产品，而这一协议在一年后依然具有重要意义。