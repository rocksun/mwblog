<!--
title: “OpenAI瓦解的开端”：OpenAI放缓模型训练——但并非所有人都买账
cover: https://cdn.thenewstack.io/media/2026/08/5594d8ce-barsrsind-y1xxobukttc-unsplash-scaled.jpg
summary: OpenAI近期宣布放缓模型训练以提升安全性与可观测性，引起行业广泛关注。外界质疑此举不仅关乎技术对齐挑战，可能还受制于财务压力及应对竞争对手崛起（如开源模型）的需求。
-->

OpenAI近期宣布放缓模型训练以提升安全性与可观测性，引起行业广泛关注。外界质疑此举不仅关乎技术对齐挑战，可能还受制于财务压力及应对竞争对手崛起（如开源模型）的需求。

> 译自：["The opening stages of OpenAI's unraveling": OpenAI slows model training -- not everyone is buying the explanation](https://thenewstack.io/openai-training-pause-cybersecurity/)
> 
> 作者：Paul Sawers

今年出现了一种趋势，各大AI实验室都在竭尽全力向世界宣扬其模型有多么强大的“不安全性”。4月，[Anthropic宣布](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/)出于网络安全担忧，严格限制了对未发布模型 Claude Mythos 的访问。6月，美国政府进一步介入，[发布了一项国家安全指令](https://thenewstack.io/fable-5-and-mythos-5-remain-suspended-the-ball-is-in-anthropics-court/)，强制 Anthropic 对所有客户禁用 Mythos 及其同系模型 Fable 5 —— 这一举动遭到了安全界的批评，且政府在[几周后撤销了该指令](https://thenewstack.io/anthropic-fable-ban-lifted/)。

OpenAI 就其自身未发布的模型也发出了类似的警告。8月初，[该公司表示](https://thenewstack.io/openai-astra-cybersecurity-delay/)，其即将推出的 [Astra](https://thenewstack.io/openai-astra-math-cost/) 模型可能已进入其内部安全框架下网络安全风险的“临界”领域，将其转移到具有更严格网络和工具访问限制的隔离测试环境中。在此前几周，刚刚发生了一起[漏洞事件](https://thenewstack.io/openai-huggingface-sandbox-breach/)，一个 OpenAI 代理程序逃离了其测试环境并攻击了 Hugging Face 的系统。

本周，OpenAI 宣布了其在解决安全问题方面接下来的举措。

> “随着模型变得越来越强大，在内部开发和测试它们所带来的风险也在增加。我们的监控、对齐和安全标准必须领先于这些风险。”

在周二发表的一篇[博客文章](https://openai.com/index/pacing-model-development-cyber-capabilities/)中，OpenAI 表示正在加强对模型的锁定 —— 将有风险的代码与互联网和其他内部系统隔离开来 —— 并进行更密切的监控，以在30分钟内捕获潜在的危险活动。值得注意的是，该公司表示，仅此监控系统就可能为其所覆盖的推理计算增加约 20% 的开销。

“随着模型变得越来越强大，在内部开发和测试它们所带来的风险也在增加，”该公司写道。“我们的监控、对齐和安全标准必须领先于这些风险。我们希望花必要的时间来达到这些标准，因此我们暂时放缓了扩展的步伐。”

具体而言，这一放缓过程“包括对旨在部署的‘最新模型’进行为期两周的强化学习暂停”。该公司指出，其“最大规模的计划内前沿强化学习运行仍处于暂停状态”，同时它会先进行一系列更小、更受控的训练和评估轮次。

总而言之，这里有很多值得剖析的地方。那么，OpenAI 在“放缓模型开发”方面到底在说什么，它又影响了哪些模型？

## 哪些 OpenAI 模型受到影响？

深入挖掘这些语言的本质引发了一些关键问题。首先，OpenAI 用过去时（“包括”）描述了其为期两周的训练暂停，这表明它适用于8月初报道的同样的 Astra 放缓。另外，仍处于暂停状态的“最大规模的计划内前沿强化学习运行”，似乎指的是更遥远的其他模型。

> “我们一直表示，如果我们认为模型能力的提升速度超过了安全和对齐的步伐，我们就会采取行动。”

Sam Altman 本人增加了一些背景信息。在最初于 X 上发布的一篇[帖子](https://x.com/sama/status/2089787807611195475)中，这位 OpenAI 首席执行官表示，有必要暂停以使安全和监控达到当今能力所要求的标准。

“模型进步现在极其迅速，我们一直表示，如果我们认为模型能力的提升速度超过了安全和对齐的步伐，我们就会采取行动，”Altman 写道。

在随后的帖子中，Altman 明确了此处具体受影响的模型。

“我们仍然预计很快会推出出色的新模型；这影响的是更长远的发布，”他[写道](https://x.com/sama/status/2089805495783813196?s=20)。

然而，Alex Heath 在《时代周刊》上写道，“大量的 Astra 工作负载仍然处于暂停状态”，恢复工作是分阶段进行的。因此，虽然 OpenAI 最大规模的前沿强化学习运行仍然搁置，但 Astra 本身似乎也尚未完全摆脱放缓的影响。

## 更好的对齐

贯穿此次放缓的主要主题之一是“对齐”（Alignment）。这个短语及其变体（如“已对齐”和“未对齐”）是 OpenAI 博客文章中最常见的词汇之一，出现了16次。Altman 本人在他那篇118字的 X 帖子中三次使用了“对齐”。

为《时代周刊》和他的[个人通讯 Sources](https://sources.news/p/openais-big-slowdown) 报道此事的 Heath 从 Altman 那里得到了额外的评论。Heath 写道，此次放缓并非由单一事件触发，而是由“一系列研究观察结果”触发的，这些观察显示出“不同程度的失对齐”，因为模型能力的增长速度超出了研究人员的预期。

在此背景下，对齐[是指](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/)模型是否按照其开发者的意图行事，并保持对人类监管的响应。这与能力截然不同：一个模型在某方面可能非常有能力，但如果它是通过开发者未批准或无法完全观察到的方式实现的，它仍然可能是未对齐的。

这种区别是周二公告的核心：OpenAI 正在告诉世界，其系统的发展速度超过了其可靠地控制它们的能力，而在行业其他部分追赶上来时，它选择放慢脚步（包括竞争成本在内）是其采取的应对措施。

## 是否有不可告人的动机？

当然，[类似于](https://www.theregister.com/security/2026/05/11/anthropics-bug-hunting-mythos-was-greatest-marketing-stunt-ever-says-curl-creator/5238111)此前的 Anthropic [Mythos 冒险经历](https://thenewstack.io/anthropic-public-bug-bounty/)，OpenAI 公布这一放缓可能还有其他激励因素。

就在 OpenAI 解释其放缓的同一天，《华尔街日报》[报道称](https://www.wsj.com/tech/ai/openais-second-quarter-sales-show-tepid-growth-compared-with-anthropic-5cb42998)，OpenAI 第二季度的运营亏损扩大了30亿美元，达到123亿美元 —— 是其同期额外创造的10亿美元收入的三倍，该收入增长了18%，达到67亿美元。而在同一季度，Anthropic 的收入翻了一番以上，达到116亿美元 —— 首次超过了 OpenAI。

周三，CNBC [报道称](https://www.cnbc.com/2026/08/19/open-ai-ipo-timing-2027-friar.html)，首席财务官 Sara Friar 正着眼于 OpenAI 在2027年进入公开市场，如果“我们的业务持续增长”则会更早。

这些报道并不能明确断定财务压力导致了强化学习训练的暂停。但它们确实提供了一个合理的替代动机：OpenAI 在一个极其资源密集型的行业中面临严重的资金流失，它可能正在寻找削减成本的方法。

网络社区中的许多人也质疑为什么 OpenAI 选择宣布训练暂停。正如一位 [X 用户](https://x.com/Dr_Gingerballs/status/2089816114092245012)所言：“暂停两周？为什么要告诉任何人？谁会为一个大型项目两周的延迟公开发布公告？”

> “OpenAI 瓦解的开端已经开始。”

人工智能研究员兼 OpenAI 的长期批评者 [Gary Marcus](https://www.linkedin.com/in/gary-marcus-b6384b4/) 也发表了意见，他汇总了来自网络各处的一系列评论，以强调并非所有人都买账 OpenAI 暂停训练的理由这一事实。

“正如我在2024年1月（如果不是更早的话）[首次警告过的那样](https://garymarcus.substack.com/p/openais-got-99-problems-and-twitch?r=8tdk6&utm_medium=ios)，OpenAI 瓦解的开端已经开始，”Marcus [写道](https://garymarcus.substack.com/p/breaking-openais-unraveling-has-begun)。“首先，几乎没有人再信任他们了，这对业务来说肯定不是什么好事。”

## 从表面价值来看

AI 安全公司 [BlackFog](https://www.blackfog.com/) 的首席执行官兼创始人 [Darren Williams](https://www.linkedin.com/in/darrenwwilliams/) 认为，正是那些敲响警钟的公司正试图围绕它制定规则 —— 尽管这不一定是件坏事，只要它能带来实验室外部的监管，以及有实际效力的规则。

“OpenAI 和 Anthropic 警告自己的模型背后确实存在合理的安全论据，”Williams 告诉 *The New Stack*。“但这些警告也强化了一种强有力的叙事：制造风险的公司正在将自己定位为应该如何治理这些风险的权威。这并不意味着这些担忧是不真诚的。安全、竞争地位和对监管的影响力可以共存。真正的考验在于这些警告是否会导致独立评估、有意义的控制以及具有真正商业后果的限制。”

> “OpenAI 和 Anthropic 警告自己的模型背后确实存在合理的安全论据。”

与此同时，Stability AI 的联合创始人 [Emad Mostaque](https://www.linkedin.com/in/emad-mostaque-9840ba274/) 公开称赞了 Sam Altman 和 OpenAI，称他倾向于从“表面价值”上看待他们的解释。

“很明显，奇怪且可能危险的事情正在发生，我们的系统还没有为此做好准备，”Mostaque [写道](https://x.com/EMostaque/status/2089807825883009428?s=20)。“前沿以下的模型已经足够胜任以改变生活，所以让我们进行优化。”

从宏观角度看，[IANS Research](https://www.iansresearch.com/) 的教员兼数据隐私咨询公司 Red Clover Advisors 的创始人 [Jodi Daniels](https://www.linkedin.com/in/jodihoffmandaniels/) 表示，Anthropic 和 OpenAI 如此大声疾呼其模型的危险性的一个原因归结于信任和责任 —— 给企业买家以信心，并为未来可能出现的问题提供保障。

“在我看来，对自身大语言模型（LLM）的正面和负面能力保持透明，能让客户在部署时更确信它们是安全的，”Daniels 告诉 *The New Stack*。“这两家公司可能都不想成为对可能给公司或个人造成实际伤害的灾难性事件负责的机构。”

> “对自身大语言模型（LLM）的正面和负面能力保持透明，能让客户在部署时更确信它们是安全的。”

## 中国与开放权重因素

在这一切喧嚣中，房间里的大象当然是中国。或者更准确地说，是中国 AI 公司涌现出的大量超强开放权重模型。

[周一](https://openai.com/index/the-defenders-window/)，OpenAI 总裁 Greg Brockman 概述了公司在 Hugging Face 漏洞事件后正在实施的一系列安全措施，同时也建议所有组织加强安全自动化。然而，他也借此机会警告了 Z.ai 的 GLM-5.3 模型，此前这家中国公司[发布了基准测试](https://thenewstack.io/glm-5-3-post-training-coding/)，显示其在某些编码和漏洞检测指标上优于 Anthropic 的 Fable 5 和 OpenAI 自己的 GPT-5.6 Sol。在 Brockman 看来，如果这些权重被公开，此类模型很可能会“[显著加速威胁态势](https://thenewstack.io/openai-open-weight-glm-5-3/)”。

几天前，Anthropic 首席执行官 Dario Amodei [提出了一个相关的观点](https://thenewstack.io/amodei-open-weights-compute-regulation/)：他说，开放权重发布并不能解决 AI 潜在的权力集中问题 —— 它们只是将其转移到控制最多计算和芯片的一方。

虽然两家公司都没有明确呼吁禁止开放权重模型，但它们对这些模型发出的警告投入的巨大关注表明，OpenAI 和 Anthropic 将开放权重视为竞争威胁，正如将其视为安全威胁一样。

这并不是说 [Moonshot](https://thenewstack.io/kimi-k3-open-weights/)、[DeepSeek](https://thenewstack.io/deepseek-v4-flash-open-weights/)、[Z.ai](https://thenewstack.io/glm-5-3-post-training-coding/) 等公司应该对 OpenAI 目前的困境负责。但它们已经向世界表明，前沿能力不再需要前沿预算。