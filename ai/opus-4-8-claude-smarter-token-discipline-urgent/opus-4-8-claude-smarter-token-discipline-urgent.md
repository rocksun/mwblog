<!--
title: Opus 4.8 让 Claude 更聪明，但 Token 约束已刻不容缓
cover: https://cdn.thenewstack.io/media/2026/05/68350a84-pablo-merchan-montes-qpow8ip_ezg-unsplash-scaled.jpg
summary: Opus 4.8的推出加速了“Token狂热”时代的终结。面对高昂的AI账单，企业和员工正告别盲目消费，转向精细化、按需选择模型的“Token纪律”时代。
-->

Opus 4.8的推出加速了“Token狂热”时代的终结。面对高昂的AI账单，企业和员工正告别盲目消费，转向精细化、按需选择模型的“Token纪律”时代。

> 译自：[Opus 4.8 Made Claude Smarter. Token Discipline Got Urgent.](https://thenewstack.io/opus-4-8-claude-smarter-token-discipline-urgent/)
> 
> 作者：Matthew Burns

*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 动态，解释它们对于将这项技术投入应用的人员和组织的意义。其核心论点很简单：学会使用 AI 的员工将定义其行业的下一个时代，而本期通讯旨在帮助你成为其中之一。*

---

我需要从一个我无法证实却一直念念不忘的故事开始。[*Axios* 转发了一位 AI 顾问的说法](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)，称某位客户在未能对员工授权设置使用限制后，**单月在 Claude 上花费了 5 亿美元**。Polymarket 借此大肆炒作，[这条推文的浏览量已超过 2900 万次](https://x.com/Polymarket/status/2060034216906068131?s=20)。这个说法是真的吗？[和其他人一样](https://x.com/Austen/status/2060095049992437885?s=20)，我对此表示怀疑。但它正在病毒式传播，而这比它是否属实更重要，部分原因在于本周随着各大公司公布财报，出现了更多类似的说法。几乎每一个这种病毒式的成本爆仓故事，单独来看都是无法证实的，但现在每一个大规模使用 AI 的人都相信，这种版本的事情可能会发生在他们身上。它们共同勾勒出一幅处于紧张状态的泡沫图景。

这次清算 spinners 并不是对 AI 不起作用的宣判，而是对盲目使用 AI 所付出的高昂代价的警示。而这一时刻的标志，正是本周晚些时候推出的 Anthropic 新版 Opus 4.8。Opus 4.8 声称是 Anthropic 迄今为止最聪明的模型，而且似乎也是迄今为止最容易让人“烧钱”的模型。“Token 狂热”（Tokenmaxxing——将消耗 Token 视为拥抱 AI 的荣誉勋章）时代似乎正在走向终结。取而代之的技能是 Token 纪律：在合适的任务上，以合适的用量，使用合适的模型。学会这一流程的员工和公司将会胜出。而那些没有学会的人最终会发现，AI 的预算迟早会从其他地方扣除。

## **Opus 4.8 是完美的缩影：更聪明，但也更容易过度消费**

Anthropic 在[周四发布了 Opus 4.8](https://thenewstack.io/claude-opus-48-release/)，Meredith Shubel 为我们进行了详细梳理——其更新日志比乍看之下更具双刃剑效应。其官方价格与 4.7 相比保持不变，且快速模式的计费现在比以前**便宜了三倍**。而最引人瞩目的功能“动态工作流”（dynamic workflows）允许 Claude Code 规划一项任务，然后在**单次会话中运行数百个并行的子智能体（subagents）**，以执行诸如在数十万行代码中进行从启动到合并的代码迁移等工作。此外，还有一个全新的努力控制（effort control）功能，这样你就可以调节 Claude 的思考强度。Shubel 对该控制功能的定性非常完美：对于担心超出额度限制的速度比预期更快的用户来说，这是防止“AI 变相涨价”（AI shrinkflation）的一种对冲手段。

重新阅读这些功能，并思考每一个功能对你的账单意味着什么。数百个子智能体意味着数百个 Token 计数器同时在运行。动态工作流没有溢价定价，子智能体按照标准的 Opus 费率消耗 Token，这意味着成本随着雄心壮志而水涨船高，而雄心壮志正是 Claude Code 的核心卖点。在[一次病毒式的开发者测试中](https://x.com/grepmoney/status/2060077508759052340)，在最大努力程度下，Opus 4.8 在处理同一个中等规模的 Cursor 任务时，据报道消耗了 **1650 万个 Token，花费了 17.26 美元**，而 GPT-5.5 完成该任务仅消耗了 **5900 万个 Token，花费了 5.57 美元**。同样的任务，成本却高达三倍。

准确地说，这些算账方式并不新鲜。本月早些时候，我指出了 [Ida Silfverskiöld 的详细分析](https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/)，她发现一个未经过优化的智能体每天运行 100 条消息，每月的花费可能达到大约 2490 美元——大约是该智能体经过微调后成本的 25 倍。而 Opus 4.8 将这一门槛提得更高了。

好的一面是实实在在的：Opus 4.8 似乎是迄今为止最强大的 Claude，而且内置的努力调节旋钮是走向 Token 纪律的良好一步。它为工程师提供了一种告诉模型何时不需要深度思考的方法，这本质上是一个成本控制杠杆。坏的一面也显而易见：模型越聪明，工作流越庞大，当原本只需几个子智能体就能搞定、却部署了一整支子智能体舰队时，就越容易在 Token 上超支。这是今年最具决定性的张力。能力在提升，但成本也在增加。

## **“Token 狂热”似乎正在消亡**

几个星期前，大公司内部流行的时尚还是“Token 狂热”（tokenmaxxing）——将原始的 Token 消耗量视为衡量员工在 AI 应用上有多超前的解锁成就勋章。本周，这一时代似乎正在走向终结。我写下这个结论时需要保持谨慎，因为证据仅由少数几个知名案例组成，而非覆盖整个市场的完整数据集。但这些名字分量极重。我的朋友 Jeremy Kahn 本周在 *Fortune* 上[撰文指出](https://fortune.com/2026/05/28/tokenmaxxing-is-dead-companies-didnt-get-the-roi-from-ai-they-wanted-to-see/)：“Token 狂热”直接撞上了古德哈特定律（Goodhart's Law），即当一项指标变成目标时，它就不再是一个好指标。亚马逊在员工开始引导智能体执行毫无意义的任务以攀升排名后，[撤下了其内部的“Kirorank”排行榜](https://www.ft.com/content/b1a62a7f-6df5-4c90-94ce-64ce9c9961b6?syn-25a6b1a6=1)。[Meta 上个月也关闭了其排行榜](https://www.theinformation.com/briefings/meta-shutters-internal-ai-token-leaderboard)。据报道，亚马逊现在转而追踪“规范化部署”，即实际有用的 AI 生成代码。

成本故事还在不断堆积。*Axios* 报道称，[企业正面临 AI 带来的账单休克](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs)：据报道，微软取消了其大部分内部 Claude Code 许可，部分原因就是成本问题；优步（Uber）的首席运营官表示，这项支出“越来越难自圆其说”；而一位首席技术官发现，员工在使用企业级模型来查询天气。[“Token 前利润”（Earnings Before Tokens）](https://x.com/brandonjcarl/status/2060069564281454811)成了一个笑话，就在 Anthropic 宣布以 9650 亿美元估值融资 650 亿美元的同一周，[排行榜纷纷下线了](https://x.com/packyM/status/2060114985775223072)。

我对所有这些故事斩钉截铁的准确性持怀疑态度。在当前使用 AI 的庞大企业群体中，几个 CEO 的表态和[四个泄露的投资回报率数据](https://x.com/AskYoshik/status/2059849267725152285)只是一个极小的样本，我不会轻易对“Token 狂热已死”妄下定论。但这些轶事遥相呼应，而且其方向高度一致，足以让人采取行动。Jeremy Kahn 真正的观点才是我们需要牢记的：“Token 狂热”失败了，因为消耗 Token 从来都不是目的。价值来自于重新设计工作流程，而大多数公司目前都在做着相当于“给日产轿车装上电动机并称其为法拉利”的 AI 傻事。这次清算并不是 AI 的失败，而是市场开始惩罚那些将活跃度与产出混为一谈的公司。这是一个纪律和编排的问题。

## **赢家正在精细化运营，并依靠工程师来选择模型**

在一些公司感到恐慌的同时，那些纪律严明的公司正开始对 AI 支出进行精细化调整。在曝光 5 亿美元账单休克文章的第二天，*Axios* [报道了这场“寻宝”行动](https://www.axios.com/2026/05/29/ceos-ai-cheaper-tokens)。Factory 的首席执行官 Matan Grinberg（其产品能将每个查询路由到能够处理它的最便宜的模型）向 *Axios* 直言不讳地指出：“有很多任务你根本不需要 Opus。”据报道，过去一个月内，Factory 的开源模型使用量相对于闭源模型翻了三倍。Micro1 的首席执行官表示，各大公司正在转向开源模型和定制化的智能体，这些智能体通常既便宜又好用。甚至连面临约 3 亿美元 Anthropic 账单的 Marc Benioff 也在公开期望能有一个智能路由，只把最难的查询发送给最贵的老大模型。在开发端，[Cursor 的 Composer 2.5 现在在基准测试中以极低的成本追平了 Opus 4.7 和 GPT-5.5。](https://thenewstack.io/cursor-composer-benchmarks/)

首席执行官们现在正争先恐后地去做资深用户已经在做的事情：在不同的模型和供应商之间自由切换。没人愿意绑定在单一实验室身上的原因，是害怕一旦被套牢就会面临价格宰割。这就是开源的论点。我们已经报道了让切换成为现实的基础设施：Steven J. Vaughan-Nichols [在我们的网站上撰文介绍了 llm-d](https://thenewstack.io/llm-d-cncf-kubernetes-inference/)——这是来自 IBM Research、红帽（Red Hat）和谷歌云（Google Cloud）的 CNCF 沙箱项目，英伟达（NVIDIA）、CoreWeave、Hugging Face 和 Mistral AI 等也参与了贡献——旨在使任何模型都能在任何加速器、任何云中运行。甚至[混乱的 OpenClaw 风波](https://thenewstack.io/persistent-ai-agents-compared/)也展示了人们对模型可移植智能体的渴望：该项目的全部意义在于，切换模型只需要修改一行代码。对于许多任务来说，开源正在成为明智、理性的选择。

事实上，一些公司已经开始以这种方式运营了：本周我与 Asaf Wiener 呆在一起，他是 Wiz 的校友，也是 AI 原生安全初创公司 [Mate Security](https://mate.security/) 的联合创始人，这是为了下周发布的 *New Stack* 专题人物介绍做准备。他告诉我，在一次推理账单几乎搞垮他的公司之后，Asaf Wiener 将模型选择权下放给了交付功能的人员。Mate 的每一位后端工程师现在都会编写评估，并根据每个工作负载来决定路由到哪个模型，包括在公司自己的 GPU 上运行自托管的开源模型，在他们的内部测试中，这些开源模型有时在成本和质量上都击败了前沿 API。他描述这种转变的方式让我记忆犹新：他的工程师“实际上不再编写一行行代码了。他们是在编排智能体。”这是现在的工作，也是我听过的对成本问题最务实的回答，因为它让做这件事的人对自己产生的成本负责。

你必须把模型当作一个投资组合，而不是一种信仰，并把至少一部分成本决策权推给最接近工作的人。单月在 Claude 上花费 5 亿美元的故事几乎可以肯定是一个神话，但它背后的纪律问题却绝非虚妄。

“Token 狂热”可能正在淡出。无论是员工还是雇用他们的公司，都需要用 Token 纪律来取而代之。