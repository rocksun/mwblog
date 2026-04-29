<!--
title: Lovelace 结束隐身状态：其上下文引擎声称可提升 AI 调查能力 1000 倍
cover: https://cdn.thenewstack.io/media/2026/04/c29b6e8b-ayush-kumar-haze_fmq4-k-unsplash-1.jpg
summary: 前 Google Cloud AI 主管 Andrew Moore 创立的 Lovelace AI 推出 Elemental 引擎，利用大规模知识图谱解决高风险领域的调查性问题。该引擎可将 Token 消耗降低千倍，准确率超 99.5%，助力金融和国防精准决策。
-->

前 Google Cloud AI 主管 Andrew Moore 创立的 Lovelace AI 推出 Elemental 引擎，利用大规模知识图谱解决高风险领域的调查性问题。该引擎可将 Token 消耗降低千倍，准确率超 99.5%，助力金融和国防精准决策。

> 译自：[Lovelace emerges from stealth with context engine that claims 1000x AI investigative power](https://thenewstack.io/lovelace-ai-context-engine-elemental-andrew-moore/)
> 
> 作者：Darryl K. Taft

[Andrew Moore](https://www.linkedin.com/in/andrew-moore-016b751/) 花了二十年时间观察[企业 AI 项目](https://thenewstack.io/turning-ai-experiments-into-enterprise-impact-lessons-learned/)在最关键的测试中失败。不是那些演示，也不是聊天机器人，而是那些最难的问题——即需要在海量数据环境中连接数百万个点进行调查的问题，在这些环境中，一个错误的答案可能会导致巨额损失、丧失自由甚至失去生命。

现在，前 Google Cloud AI 主管、前[卡内基梅隆大学计算机学院](https://www.cs.cmu.edu/)院长、以及 [美国中央司令部（US CENTCOM）首位 AI 顾问](https://press.lovelace.ai/articles/us-centcom-hires-dr-andrew-moore-one-of-worlds-leading-experts-on-ai-ml) Andrew Moore，带着 [Lovelace AI](https://press.lovelace.ai/about) 及其旗舰产品 [Elemental](https://press.lovelace.ai/) 结束了隐身状态。Elemental 是一款[企业级上下文引擎](https://www.tabnine.com/blog/introducing-the-tabnine-enterprise-context-engine/)构建工具，旨在解决他所认为的高风险 AI 部署不断失败的核心原因。

“在我的职业生涯中，我一直被一个简单的问题驱动：当错误的代价是灾难性的时候，我们如何利用先进的智能来帮助人们做出正确的决定？”Andrew Moore 在公司的发布声明中表示。“AI 在调查背景下具有非凡的潜力——但前提是它能明确地帮助人类做出更好的决策。”

## 调查性问题带来的挑战

Andrew Moore 表示，他将大型语言模型擅长的领域与它们始终表现不足的领域做了明确区分。总结任务、对话查询和基础研究都行得通。但他称之为“调查性问题”的领域则完全是另一回事。

“一家大型银行负责贷款的人可能会问：‘今天的某些新闻是否有理由让我担心，我同意的贷款中某些抵押品看起来不太可靠？’”Andrew Moore 在接受 *The New Stack* 采访时说。“为了回答这个问题，你的[大型语言模型（LLM）](https://thenewstack.io/llm/)必须查看并触及数百万条信息。”

他在简报中提到，同样的问题也出现在国家安全领域。Andrew Moore 描述了一名海关检查员试图从每周进入港口的数千艘船只中确定哪些最有可能隐藏武器或涉及人口贩运——这个问题需要近乎实时地汇总并交叉引用海量的行为、货物和所有权数据。

Andrew Moore 认为，当前的 LLM 会在这一类问题上卡壳，因为它们被迫低效地搜索海量数据墙，在缺乏可靠推理所需的结构化上下文的情况下消耗大量的 Token 和时间。标准的[检索增强生成（RAG）](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/)虽然有所帮助，但作用有限。

“RAG 非常有效，但对于许多调查性问题，你确实需要对数百万份源文档进行信息汇总和搜索，”Andrew Moore 告诉 *The New Stack*。“这就是区别：RAG 让我们能处理数百份；而多 TB 级别的上下文引擎让我们能处理数百万份。”

## Elemental 的功能

Elemental 位于智能体（Agent）和数据之间，预先计算并缓存数十亿个事实——Andrew Moore 目前最大的部署规模包含 5500 万个实体和超过 20 亿个事实——并将其转化为他所称的“上下文引擎”：一个保存在内存中的结构化知识图谱，随时准备配合调查查询完成每一步推理。

“在推理发生时，Elemental 已经创建了这个信息宝库，随着调查查询进行推理步骤而随身携带，”Andrew Moore 在初次简报后的书面回复中表示。“那个信息宝库就是上下文引擎。”

Andrew Moore 声称，结果是使用 Elemental 的智能体在处理复杂的调查任务时，所需的 Token 数量仅为 GPT 和 Gemini 等领先模型的千分之一——这种 1000 倍的降幅直接转化为经济效益。他说，客户可以以标准大模型处理一次调查的成本，运行一千个并行调查。Lovelace 还声称实体准确率超过 99.5%，中位查询延迟为 20 秒，即使是触及数百万个源事实的查询，其 99 分位延迟上限也仅为 60 秒。

Elemental 的公开发布还引入了 [YottaGraph](https://github.com/Lovelace-AI)，这是 Lovelace 的专利知识图谱，预计到第二季度末将扩展到一万亿个互连事实。YottaGraph 使企业能够用实时全球情报丰富内部数据——包括卫星转发器数据、新闻馈送、情报报告、法律文件、传统结构化数据库——并统一到一个实体空间中。

此外，Andrew Moore 认为，幻觉问题已在架构层面得到解决。

他在书面回复中说：“我们的上下文引擎直接解决了这个问题，方法是尽可能减少在语言模型那种出色但黑盒的嵌入空间中工作，而尽可能多地在上下文引擎的直接实体和链接模型中工作。”

系统的每一次推理都附带指向源材料的引用，Andrew Moore 表示，这是由其客户所处的监管和法律环境驱动的、不可逾越的设计要求。“生成的最终答案在呈现给用户之前，会根据所有源事实进行核对，”他说。

## 渔船案例

Andrew Moore 提供了一个系统按预期工作的具体案例。Elemental 正在监控异常的海事活动，当时它检测到约 200 艘船在几小时内从特定地点出发——这种突发的激增通常会触发警报。

“起初，当上下文引擎看到这种情况时，它准备发出警报称出现了大问题，”Andrew Moore 在书面回复中说。“然而，因为它在双重检查中还可以访问新闻，它意识到今天该地区捕鱼季开始了，并且与前一年行为的佐证显示这是一个标准事件——因此，虽然值得评论，但不至于在半夜叫醒人们。”

Andrew Moore 说，正是这种上下文修正——对人类专家来说显而易见，但对缺乏足够依据的 AI 系统来说历来是不可见的——定义了“提供帮助的 AI”与“制造新麻烦的 AI”之间的区别。

## 巨大的转变

“天哪，这太酷了，”Futurum Group 的分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 在听闻 Lovelace 的消息后告诉 *The New Stack*。“严肃地说，这一举措反映了目前企业引入数据和 AI 智能体方式的巨大转变。简而言之，Lovelace 承诺的是简化目前构建上下文流水线那种极其复杂且混乱的方法，那些流水线不一致、不可扩展，而且经常出错。相反，Lovelace 提供的是你可以称之为结构化关系图的东西，也就是所谓的知识图谱。”

他解释说，这些图谱与语义层协同工作，正变得相当重要，微软和 Google 等公司也在推行相同的方向，甚至做到了自动数据增强。例如，当数据进入 Google Cloud Storage 时，Google 可以自动识别实体并构建它们相互关联的图谱，从而有效地将意义和上下文合并为单个实体。

“Lovelace 新产品的有趣之处在于，它将通常混乱的数据摄取和实体映射管道整齐地打包成一个自动化流水线，”Brad Shimmin 告诉 *The New Stack*。“对于在错误猜测代价高昂的领域部署 AI 的数据领导者来说，结论非常明确：是时候超越基础搜索数据库，探索自动化的、有引用支撑的知识结构了，因为即使是最渴望工作的 AI 智能体也需要坚实的事实基础才能做好工作。”

## 市场与竞争

Lovelace 并不是唯一追求可引用、可验证 AI 输出的公司。[Perplexity](https://www.perplexity.ai/)、[Google NotebookLM](https://notebooklm.google/) 以及越来越多的企业搜索供应商也提出了类似的主张。Andrew Moore 的答案是规模。“处理数百份文档时的验证是一回事，”他在书面回复中说。“当你拥有数十亿个事实时，情况就完全不同了。你必须在核心基础设施中设计数据血缘（data lineage），以便在那种规模下运行。”

Andrew Moore 估计 Lovelace 在技术上领先竞争对手六个月，而在更难复制的“诀窍（knowhow）”上领先 18 个月——即在安全关键环境中实际部署 AI 的组织和监管经验。他说，公司已经与政府客户进行了 18 个月的实验，并与金融机构进行了 6 个月的实验，所有这些都在保密协议（NDA）下进行。

Lovelace 成立于 2023 年，拥有 25 名工程师，规模似乎比其雄心壮志要小。Andrew Moore 并不在意。“我们大部分的开发工作都是由数千个智能体组成的团队完成的，”他在简报中说。

采访 Andrew Moore 是一件愉快的事情，他在针对后续问题的书面回复中也进行了深入探讨。

## 伦理问题

从技术层面看，Andrew Moore 对安全关键性的界定是真诚的。Elemental 专为物理隔离（air-gapped）、本地部署而构建，无数据外泄，每次推理都有完整的血缘，并在任何答案触达用户前根据源事实进行验证。该系统旨在满足受监管行业的证据标准。

但 Andrew Moore 对这项工作边界的立场则不那么明确。当被直接问及 Lovelace 是否存在无论技术保障如何都不会承接的工作类别时——这个问题是由[当前五角大楼领导层的 AI 监管方法](https://thenewstack.io/pentagon-anthropic-model-orchestration/)引发的——Andrew Moore 说：“我们所做的一切都必须遵守我们运营所在国家的法律。我们绝对愿意也有能力在任何安全关键行业工作。”

这个回答设定的是法律底线，而非伦理底线。这与像 [Anthropic](https://www.anthropic.com/news/statement-department-of-war) 这样的 AI 供应商形成对比，后者[发布了明确的禁止使用政策](https://thenewstack.io/perplexity-computer-vibe-coding-openai-anthropic-pentagon/)，并公开谈论将生存风险作为部署决策的约束条件。对于 Andrew Moore 来说，护栏似乎是过程——严谨的工程、经过验证的血缘、保持问责制的人类决策者——而不是禁令。

他还表示，AI 需要遵循与军事官员为目标决策辩护时相同的证据标准。

Andrew Moore 的创业故事明确了对国家安全的关注。“我在卡内基梅隆大学的职位意味着我做了大量的政府工作，在那里，我被坏人（包括流氓国家）利用人工智能恶意对付西方的可能性所震撼，”他在书面回复中说。他在 CENTCOM 的顾问角色强调了他认为 Lovelace 所构建的产品最迫切的应用场景。

公司以 [Ada Lovelace](https://thenewstack.io/2025-the-year-of-the-return-of-the-ada-programming-language/) 的名字命名——她是世界上第一位计算机程序员，Andrew Moore 指出，她也是一位“严肃的概率论者”，花费了大量精力思考如何理性地组合不确定的证据。她还曾试图通过以此博彩来维持生计。“我把这称为，”Andrew Moore 在书面回复中说，“用行动实践你的诺言。”