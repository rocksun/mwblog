<!--
title: LLM颠覆SRE手册：运维何去何从？
cover: https://cdn.thenewstack.io/media/2025/11/fe7aacd2-c974-4eab-b18a-a54907fcf587-1.jpg
summary: AI时代SRE面临不确定性新挑战。传统工具失灵，监控需演进，锚定业务指标。目前行业仍在探索，尚无成熟方案。
-->

AI时代SRE面临不确定性新挑战。传统工具失灵，监控需演进，锚定业务指标。目前行业仍在探索，尚无成熟方案。

> 译自：[LLMs Broke the SRE Runbook. Now What?](https://thenewstack.io/llms-broke-the-sre-runbook-now-what/)
> 
> 作者：Sylvain Kalache

可靠性工程师是维持现代软件运行的幕后力量。在确定性系统上磨练了数十年实践后，许多团队正在追逐超越99%正常运行时间的另一个“九”。但AI时代，特别是大模型支持的功能，改变了游戏规则。输出是非确定性的，数据管道不断变化，关键组件如同黑箱。结果，SRE们几十年来掌握的许多工具和惯例不再能完美适用于生产AI。

在SREcon EMEA 2025大会上，我与Cauchy联合创始人Maria Vechtomova共同组织了[MLOps讨论专题](https://www.usenix.org/conference/srecon25emea/presentation/vechtomova-dt)。我们邀请了行业领袖与观众进行对话，讨论可靠性工程师如何驾驭这个AI领域。以下是主要收获。

## SRE们面临新范式

在SREcon Americas 2025大会上，微软公司副总裁Brendan Burns[表示](https://www.usenix.org/conference/srecon25americas/presentation/burns)，Azure通过两种方式审查新模型：一是“大模型作为评判者”策略，即大模型评判自己的输出；二是，更令人惊讶的是，由微软员工提供“赞/踩”反馈。观众笑了，然后在会议期间继续讨论这个话题。对于[习惯于可衡量SLO和客观指标的可靠性工程师](https://thenewstack.io/limitations-in-measuring-platform-engineering-with-dora-metrics/)来说，这听起来令人不安地模糊。这也许是一个关键时刻，向业界预示着[变革即将来临](https://thenewstack.io/2-ways-ai-assistants-are-changing-kubernetes-troubleshooting/)。正如Stanza首席执行官Niall Murphy所说：“SRE们在未来一段时间内，将不得不与这种随机性搏斗。”

对于大多数传统软件而言，[在相同的基础设施上运行相同的代码](https://thenewstack.io/how-to-run-deepseek-r1-on-aws-using-infrastructure-as-code/)会产生相同的结果。对于机器学习工作负载，则无法保证这一点。正如Vechtomova[解释的](https://www.youtube.com/shorts/bgvRu6UbcuE)：“数据的统计特性可能会发生变化，你的模型就会停止运行。新冠疫情期间就发生了这种情况：预测和推荐系统崩溃了，因为我们以前从未见过那种数据。”

尽管AI以各种形式存在已久，但我们正在进入一个新时代。正如Zalando的AI总监Alejandro Saucedo观察到的：“生成式AI/大模型正在将范式从训练转向推理。”训练曾是重心；模型不足以满足大多数应用需求，机器学习工程师专注于解决这个问题。随着大模型现在能够提供近乎神奇的结果，难题已转移到服务时间：推理。SRE们开始登场，被要求迅速从零达到生产级别，通常缺乏成熟的工具或既定的操作手册。

可靠性工程师习惯于确定性系统，例如，状态码（2xx/5xx）可以作为大致的健康代理。由于大模型的输出是非确定性的，通常没有直接的方法来判断AI生成的答案是否良好。

## 监控必须演进

如果你的大模型应用生成新闻摘要，你如何知道今天的输出和昨天的一样好？没有单一、明显的信号。那么，你应该跟踪什么来捕捉质量漂移呢？Meta高级生产工程师Jay Lees主张以业务指标为锚点。对于广告来说，这可能是点击率（CTR）：如果CTR上升，你的AI可能正在改善用户体验；如果下降，则说明出现了某种退步。

大模型将SRE的指标理念推向了更上层。“正确”的唯一可靠仲裁者是业务成果：助手是否解决了问题，用户是否完成了转化，每次会话的收入是否保持不变？这意味着服务所有者必须定义结果层面的SLI和SLO。但结果可能滞后，最佳实践是将其与经典指标结合使用。这种结合既能提供带有[业务影响的真相和速度](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)，又能提供早期漂移信号。

这清楚地表明AI使得可观测性不再是可选项。但正如Honeycomb首席技术官Charity Majors所说，“大多数公司甚至对其非AI工作负载都没有高质量的‘可观测性’。”因此，要么我们面临着通往完善AI可观测性的漫长道路，要么AI成为推动可观测性发展的催化剂。对于那些试图做好的公司，一项[最新调查](https://ethical.institute/state-of-ml-2024.html)发现，在将机器学习模型投入生产时，监控和可观测性是最大的挑战，只有50%的公司拥有某种形式的模型监控。

## 没人完全搞懂

即使我们积极地进行工具部署，当今的实际操作也存在局限性。Anthropic可靠性负责人Todd Underwood直言不讳地指出：“理论上，你可以跟踪和版本化所有东西：数据、提示、嵌入、模型、检索索引以及解释偏差的策略。实际上，这种端到端溯源的级别对于大多数公司来说是繁重且不切实际的。”

理想与现实之间的差距之所以存在，原因在于：环境正在快速变化。Underwood和Murphy，《[可靠机器学习：将SRE原则应用于生产中的ML](https://www.oreilly.com/library/view/reliable-machine-learning/9781098106218/)》的合著者，补充说，撰写这本书的一个挑战是如何跟上变化的速度；他们旨在提出在出版时不会过时的实践。

在与专家小组和观众进行了九十分钟的讨论后，一个主题脱颖而出：没有人完全搞懂。许多工程团队觉得他们在AI方面落后了，但事实是，我们都在驾驶一架仍在建造中的飞机。一些组织走在前列，但很少有成熟的流程、工具和操作手册来大规模运行这些非确定性系统。

目前，MLOps面临的[开放问题](https://spawn-queue.acm.org/doi/10.1145/3762989)多于已解决的答案，这对于科技领域来说并非新鲜事，但其规模是我们很久未见的。正如Andrej Karpathy[指出的](https://www.dwarkesh.com/p/andrej-karpathy)，要“正确”地实现代理应用可能需要十年时间。许多大模型演示已经达到了第一个九——它们大约90%的时间都能正常工作——但在达到生产级可靠性之前，还有许多个九需要攻克。