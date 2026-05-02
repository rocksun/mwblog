OpenAI在周一[宣布其与Microsoft的合作伙伴关系进行重组](https://thenewstack.io/openai-microsoft-partnership-restructured/)后，几乎没有浪费任何时间。这家 ChatGPT 的缔造者现在正将其[模型](https://openai.com/index/next-phase-of-microsoft-partnership/)、编码工具和智能体能力[引入](https://openai.com/index/next-phase-of-microsoft-partnership/) Amazon Web Services (AWS)，并在 [Bedrock](https://aws.amazon.com/bedrock/) 上推出了一系列新的集成——Bedrock 是 AWS 的[构建和部署 AI 应用程序的平台](https://thenewstack.io/mcp-summit-aws-bedrock/)。

对于 AWS 客户而言，这意味着他们现在可以在其现有的云环境中原生访问 OpenAI 的模型和工具，而无需依赖外部 API 或基于 Azure 的服务。这也将 OpenAI 的技术与 Bedrock 上已有的竞争对手模型（如[来自 Anthropic 的模型](https://aws.amazon.com/bedrock/anthropic/)）并列，从而为企业在构建和部署 AI 系统时提供更大的灵活性。

这段长达七年的传奇故事为 Microsoft 和 OpenAI 带来了无数的突破和转折点，两家公司最终都在寻求通往更大灵活性和自由的道路。究竟谁能从这种新的回旋空间中获益最多尚存争议，但 AWS 已经做好了利用这一转变的准备。

但我们是如何走到这一步的呢？

## 故事至今

Microsoft 与 OpenAI 动荡的结合可以追溯到 2019 年，当时 [Microsoft 向这家当时的初创实验室投资了 10 亿美元](https://openai.com/index/microsoft-invests-in-and-partners-with-openai/)，并成为了其独家云提供商。这笔交易让 Microsoft 得以抢先访问 OpenAI 的模型，同时将 OpenAI 的训练和部署堆栈锚定在 Azure 上。随后的投资加深了这种联系，包括 2023 年的一项重大交易，使 Microsoft 的总投资达到[据报道的 130 亿美元](https://www.nytimes.com/2023/01/23/business/microsoft-chatgpt-artificial-intelligence.html)，并获得了 OpenAI 营利性部门的重要少数股权，据信略低于 50%。

这段关系也面临过不少不稳定的时刻。2023 年 11 月，OpenAI 董事会突然罢免了 CEO Sam Altman，促使 Microsoft 聘用了他——结果几天后在内部强烈的反对声中，[Altman 重返](https://thenewstack.io/why-microsoft-has-to-save-openai/) OpenAI。

虽然那一插曲暴露了裂痕，但它并未改变将两家公司捆绑在一起的潜在动力。对于 Microsoft 而言，这在它缺乏同类内部产品时，提供了一条进入新兴大语言模型 (LLM) 市场的路径。对于 OpenAI 而言，它提供了训练日益庞大的系统并接触企业客户所需的算力、资金和分发渠道。

但这种亲密的结合也伴随着权衡。随着 OpenAI 的雄心壮志不断增长，其基础设施需求也在增加，这给 Azure 的容量带来了越来越大的压力，并使该公司在企业分布于多个云提供商的时代，被束缚在单一云平台上。这种压力到 2025 年中期已经开始显现，当时有报道称 [OpenAI 已与 Google Cloud 达成交易](https://www.cnbc.com/2025/07/16/openai-googles-cloud-chatgpt.html)，在 Microsoft、[CoreWeave](https://www.coreweave.com/news/coreweave-announces-agreement-with-openai-to-deliver-ai-infrastructure) 和 Oracle 之外增加了新的供应商，以补充其算力需求——这一举动指向了单一供应商架构中日益扩大的裂痕。

> “我们的客户需求继续超过我们的供应。”

在今年 1 月的 [2026 财年第二季度财报电话会议](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2)上，Microsoft 提到了这种压力，CFO Amy Hood 表示“我们的客户需求继续超过我们的供应”，因为该公司投入了数百亿美元用于 GPU 和数据中心建设，以跟上 AI 工作负载的步伐。

值得注意的是，该公司还透露，其商业剩余履约义务（实际上是其未来签约的云收入）中约有 45% 与 OpenAI 挂钩，这突显了该合作伙伴关系对 Azure 增长的核心作用。

简而言之，OpenAI 不仅是 Azure 需求的主要来源，也是 Microsoft 竞相扩大的容量的主要消耗者。

但或许更重要的是，这也让 Microsoft 在市场转向多模型方法的背景下，过度暴露于单一合作伙伴的风险中。因此，在这一重大新闻发布之前，它已经开始应对这一现实。

## “广泛的模型选择”

在 1 月的同一次财报会议上，Microsoft CEO Satya Nadella 指出了一系列塑造其云战略的更广泛压力，包括对主权日益增长的需求——不仅是数据存储在哪里，还包括谁跨地区和环境控制数据。反过来，这使得 AI 系统构建和部署的灵活性变得至关重要。

> “我们的客户希望在任何工作负载中使用多个模型。”

“这始于拥有广泛的模型选择，”Satya Nadella 在电话会议上表示，“我们的客户希望在任何工作负载中使用多个模型，并根据成本、延迟和性能要求对其进行微调和优化。”

他将此放在软件构建方式更广泛重置的背景下，认为“就像在每一次平台转变中一样，所有的软件都在被重写”，并且“你可以将智能体视为新的应用程序”。

在这种范式中，应用程序不依赖于单一模型；相反，它们根据任务调用不同的模型，这使得模型选择的灵活性成为核心要求。

Microsoft 的回应是将 [Foundry](https://azure.microsoft.com/en-us/products/ai-foundry)（其用于构建、部署和管理 AI 模型及智能体的平台）定位为多模型环境。虽然 Foundry 已经支持包括 [Deepseek](https://azure.microsoft.com/en-us/blog/deepseek-r1-is-now-available-on-azure-ai-foundry-and-github/) 和 [Cohere](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/cohere-models-now-available-on-managed-compute-in-azure-ai-foundry-models/4423428) 在内的一系列模型，但 Microsoft 在 [2025 年 11 月](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/)开始添加 Anthropic 的 Claude 模型，将 OpenAI 的直接对手引入了同一平台。

![Foundry 中的模型选择](https://cdn.thenewstack.io/media/2026/04/d878bce1-recording-2026-04-30-094937.gif)

***Foundry 中的模型选择***

该公司[表示](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2)，已有超过 1,500 家客户通过 Foundry 同时使用 OpenAI 和 Anthropic 的系统，同时还指出 Anthropic 另有 [300 亿美元的算力承诺](https://azure.microsoft.com/en-us/blog/introducing-anthropics-claude-models-in-microsoft-foundry-bringing-frontier-intelligence-to-azure/)。  
实际上，Microsoft 已经在对冲风险——即便在与 OpenAI 保持最深层联系的同时，也在构建一个多模型生态系统。

因此，这种紧张局势为本周的“重置”铺平了道路，两家公司都采取行动放宽了协议条款，并为更灵活的安排打开了大门。

在实际操作中，这意味着结束了 Azure 作为唯一云提供商的独占性，允许 OpenAI 在其他云上运行并提供其模型，同时 Microsoft 保留了在现在的非独占许可下访问 OpenAI 模型的权利，并继续作为主要股东。

这种重置，有效地为双方提供了更多的回旋余地。

## OpenAI 与 AWS 通过 Bedrock 落地深化合作

正如 Microsoft 一直在为灵活性奠定基础一样，OpenAI 和 AWS 也很长一段时间以来一直在做同样的事情。

作为背景，开发者长期以来一直能够通过[调用其公开 API](https://thedeveloperspace.com/how-to-invoke-openai-apis-from-aws-lambda-functions/) 从 AWS 内部使用 OpenAI 的模型。AWS 还通过 [Bedrock 和 SageMaker](https://www.aboutamazon.com/news/aws/openai-models-amazon-bedrock-sagemaker) 支持了 OpenAI [开放权重 GPT-OSS 模型](https://www.forkable.io/i/170464622/the-return-of-openai)的一小部分子集。

但这种“关系”在 [2 月通过一项正式的多年合作伙伴关系](https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment)发生了转变，该合作涵盖了基础设施、企业工具和定制芯片，亚马逊向 OpenAI 投资了 500 亿美元。

这或许是迄今为止最明确的信号，表明无论当时存在什么样的“独占”协议，其基础充其量也是摇摇欲坠的。3 月份有报道称，[Microsoft 正在考虑对亚马逊和 OpenAI 采取法律行动](https://www.ft.com/content/e814f4c3-4fb5-4e2e-90a6-470044436b39?syn-25a6b1a6=1)。

该协议概述了将 OpenAI 的模型和智能体平台引入 Bedrock 的计划，同时开发所谓的“有状态运行环境”，以支持更复杂、长期运行的 AI 工作负载。它还包括一项重大的算力承诺，作为交易的一部分，OpenAI 同意消耗 [AWS Trainium 芯片](https://aws.amazon.com/ai/machine-learning/trainium/)的大规模产能。

最新的公告直接建立在该基础之上。OpenAI 的模型现在正通过 Bedrock 提供，让 AWS 客户能够通过他们已经使用的相同 API、安全控制和治理框架进行访问。Codex（OpenAI 的编码智能体）也被引入了 Bedrock，允许团队在不离开现有 AWS 环境的情况下运行开发工作流。

除此之外，亚马逊还推出了由 OpenAI 提供支持的 Bedrock 托管智能体，以帮助企业部署能够跨内部系统执行多步任务的智能体，而无需自行组建底层基础设施。

这三个组件都处于有限预览阶段，它们共同标志着 OpenAI 工具与 AWS 平台更紧密集成的重大转变。

## 那么……谁才是真正的赢家？

取决于你听谁的，周一宣布的这笔交易中，要么是 OpenAI 赢了，要么是 Microsoft 赢了。

正如投资者兼作家 M.G. Siegler 在 [Spyglass 上的观点](https://spyglass.org/the-openai-microsoft-agi-clause/)，OpenAI 获得 AWS 的支持应该会极大地促进其业务——不仅是针对其死敌 Anthropic，更广泛地说，是在该公司尝试上市的过程中。

但 Microsoft 放弃的东西显然是它已经在失去的东西，OpenAI 之前与 AWS 的暧昧关系就是证明。因此，Microsoft 作为回报获得了真正的让步——新协议允许 Microsoft 停止向 OpenAI 支付收入分成，而 OpenAI 将继续向 Microsoft 支付收入分成直到 2030 年。此外，Microsoft 保留了到 2032 年访问 OpenAI 模型和产品的非独占许可，并且作为 27% 的持股人，无论这些工作负载在哪里运行，它都能从 OpenAI 的增长中获利。

> 现实情况是，无论是 OpenAI 还是 Microsoft，都无法通过任何独占协议得到有效服务，因为两家公司都需要跨多个云、合作伙伴和芯片架构运营，才能在大规模竞争中立足。

现实情况是，无论是 OpenAI 还是 Microsoft，都无法通过任何独占协议得到有效服务，因为两家公司都需要跨多个云、合作伙伴和芯片架构运营，才能在大规模竞争中立足。

在周二于[旧金山举行的 AWS 活动](https://www.youtube.com/watch?v=bhz0F33fc7Y)上，OpenAI CEO Sam Altman 辩称，虽然 AI 将“降低创造新产品的门槛”，但仅有模型是不够的。

“这些系统需要可靠、稳健地运行，需要安全，需要扩展，并且需要适应公司已经开展业务的环境，以及他们已经信任的基础设施，”Sam Altman 表示，他将与 AWS 的联合视为一种在企业所在地满足其需求的方式。

> “[客户]想要最广泛的选择——这意味着他们需要访问最好的前沿模型。”

与此同时，AWS CEO Matt Garman 也从另一个角度表达了类似的观点，指出其客户不希望受到限制其 AI 系统运行地点的限制性协议的束缚。

“当我们与公司交流时，他们总是想要最好的选择，”Matt Garman 在台上说，“他们希望能够在绝对最好的云中运行。当他们审视自己的 AI 应用程序时，他们想要最广泛的选择——这意味着他们需要访问最好的前沿模型。”

虽然可以很容易地为 OpenAI 或 Microsoft 的情况进行辩护，但更有趣的问题是，AWS 是否已悄然成为此处的最大赢家。

在 OpenAI 宣布投入亚马逊云子公司怀抱的大约一周前，[AWS 透露 Anthropic](https://thenewstack.io/anthropic-amazon-aws-investment/) 已承诺在未来十年内向 AWS 投入超过 1,000 亿美元——其中大部分用于 Trainium 芯片——同时亚马逊立即向 Anthropic 投资 50 亿美元，随后还将根据某些商业里程碑追加高达 200 亿美元的投资。

正如 *The New Stack* [在周三报道](https://thenewstack.io/openai-bedrock-trainium-silicon/)的那样，在八天内，AWS 锁定了来自全球两家领先 AI 实验室的重大芯片承诺。这两家在每个基准测试和每个架构决策上都相互竞争的实验室，刚刚在同一个定制芯片路线图上进行了平行的赌注。

> 这两家在每个基准测试和每个架构决策上都相互竞争的实验室，刚刚在同一个定制芯片路线图上进行了平行的赌注。

Anthropic 一直在[强调这一立场](https://www.anthropic.com/news/anthropic-amazon-compute)，宣称它仍然是唯一在所有三大主流云平台（AWS、Google 和 Microsoft）上都可用的前沿 AI 模型。如果这成为行业预期，很难想象 OpenAI 还能坚持多久——特别是如果将这种安排扩展到 Google Cloud 上的更广泛模型可用性，将能弥合这一差距。