<!--
title: Fable的消亡为“自托管AI模型”提供了最佳的辩护理由
cover: https://cdn.thenewstack.io/media/2026/06/32ee86c5-screenshot-2026-06-18-at-5.06.24-pm-scaled.png
summary: 本文通过Fable模型被政府强制下架的事件，阐述了“访问权不等于所有权”的风险。作者指出，托管模型极易受政策及厂商影响，而GLM-5.2等开源模型不仅性能追平前沿，且具备自主可控性，是企业规避风险的更优选择。
-->

本文通过Fable模型被政府强制下架的事件，阐述了“访问权不等于所有权”的风险。作者指出，托管模型极易受政策及厂商影响，而GLM-5.2等开源模型不仅性能追平前沿，且具备自主可控性，是企业规避风险的更优选择。

> 译自：[Losing Fable made the best case yet for AI models you can run yourself](https://thenewstack.io/losing-fable-open-weight-glm/)
> 
> 作者：Matthew Burns

本周我的群聊里出现频率最高的一句话是三个词，反复出现：“我想念 Fable 了。” 我也是。它新鲜、有趣，感觉像是下一代产品。然而，在它发布三天后，美国政府的一封信就让它下线了。

这个教训比 Fable 本身更深刻：访问权不等于所有权。托管模型可能会消失，可能被实验室关停、被供应商重新定价，或者被商务部的指令强制下线。在 Fable 出现又消失的同一周，Z.ai 发布了 GLM-5.2，其权重开源，用户可以下载、保留并自行运行。失去 Fable 令人心痛，但也比任何基准测试都更能证明开源、可拥有模型的重要性。

## **Fable 状态快速更新**

你已经知道它消失了，所以这是它下线一周后的现状。Anthropic 于 6 月 12 日在全球范围内下架了 Fable 5 和 Mythos 5，以遵守美国的一项出口管制指令，该指令禁止所有外国国民（包括其员工）使用这些模型。关于此事的详细时间线，请阅读 Alex Wilhelm 在 *Cautious Optimism* 上的文章；他在[解释文章中总结道](https://www.cautiousoptimism.news/the-anthropic-fable-mess-explained/)：“（这）真是 Fable 的一次绝佳广告，对吧？” 我的朋友 Zack Whittaker 在 *TechCrunch* 上的解读则更为直截了当，因为 Zack 一贯如此：政府刚刚证明了无论有无法院命令，它都能强制让一家公司的产品下线。

正如 Alex 所指出的，这种情况对 Fable 来说确实是绝佳的广告，但对开源权重模型而言可能更有意义。Janakiram MSV 本周为 TNS 撰文时[写道](https://thenewstack.io/fable-ban-open-weights/)：“任何基于 Fable 5 构建自动化的企业都在一个下午失去了其引擎。” 问题从未出在 Fable 身上。它消失了，而任何基于它构建的人都没有发言权。这有力地证明了你可以自行运行模型的重要性。

## **与前沿技术的差距不再遥不可及**

坦率地说，我也有自己的局限性：我没有像使用 Opus 4.8 或 Fable 那样深入使用过 GLM-5.2。我是在谈论一种炒作，但还没到下结论的时候。不过，这种炒作声势浩大。[Z.ai 的发布文章](https://x.com/Zai_org/status/2066938937344495629)——具备前沿智能、MIT 开源协议权重、百万 Token 上下文——在 X 上获得了 490 万次浏览。Arena 的新 Agent 排行榜将 GLM-5.2 称为[其测得的最强开源权重结果](https://x.com/arena/status/2067341945148719463)，而在其前端编程榜单上，它排名第二，领先 Claude Opus 4.7 29 分，仅次于 Fable 5。正如 Arena 联合创始人 Anastasios Angelopoulos [在推特上所说](https://x.com/ml_angelopoulos/status/2066969005856829824)：“如果你去掉不可用的 Fable，GLM-5.2 (Max) 就是全球前端编程领域排名第一的模型。”

开发者演示令人印象深刻。Together AI 的 Hassan 让 GLM-5.2 和 Opus 4.8 分别[构建一个落地页](https://x.com/nutlope/status/2067313679951941686)，结果发现两者几乎没有区别——除了 GLM 成本为 6 美分，而 Opus 为 49 美分。

你永远应该对此类信息保持谨慎，因为早期的演示会让每个模型看起来都很神奇。但剥离炒作，趋势依然存在。一位将 GLM-5.2 [作为全天代码审查员的开发者表示](https://x.com/jumperz/status/2067289766945513949)，“现在没人会相信开源权重模型还落后 6 到 8 个月了”，并认为它们“距离真正挑战 [OpenAI 的] GPT-5.5 和 [Anthropic 的] Opus 4.8 仅差一次发布”。另一位测试人员指出，GLM-5.2 现在已经超越了 2 月发布的 Claude Opus——这很值得注意：差距只有三到四个月，而不是几年。

一旦前沿模型与开源权重模型之间的智能水平感觉足够接近，价格就会成为决定性因素。而在价格方面，开源权重模型总是赢家。

## **连 David Sacks 也支持自行运行模型**

听听政府的 AI 指导人怎么说。[本周在一长串推文中](https://x.com/DavidSacks/status/2067270499458027832)，David Sacks 为政府针对 Anthropic 的立场进行了辩护，称：“我们正处于倒计时中，直到 Mythos 级别的能力广泛传播，包括传播到非美国/中国模型。” 他是对的。具有讽刺意味的是：那个担心倒计时的政府，恰恰自己加速了这一进程。它将唯一处于前沿的模型——即美国产的模型——从市场上撤下，而就在同一周，最强的开源权重模型由一家中国实验室发布了。Sacks 警告说这种能力会传播到中国和开源模型中。华盛顿的做法只会让开源替代方案更具吸引力。

而且它并没有坐等倒计时结束——禁令实际上正在加速这一过程。Alex Wilhelm [再次在 *Cautious Optimism* 上写道](https://www.cautiousoptimism.news/europe-got-its-ai-excuse/)，这项禁令给了欧洲一个借口，切断盟友对 Mythos 和 Fable 的访问是“给 Mistral、开源权重中国模型以及每一个已经想要借口进行多元化的政府送出了一份大礼”。加拿大总理表示，教训是“建立和多元化”；欧洲领导人则呼吁是时候实现真正的技术主权了。用 Alex 的话来说，美国模型“在全球范围内的价值降低了，因为对它们的需求减少了”——而摆脱它们的最快方法就是开源权重的中国 AI 或欧洲的 Mistral。

这里有一些数字可以说明这种情况的经济性。[工程师 Jeffrey Scholz 发推文称](https://x.com/Jeyffre/status/2067132023576354818)：一个在几台 DGX Sparks 上运行的 7000 亿参数模型，在自己的本地硬件上运行且接近前沿水平，成本约为 20,000 美元，在六到七个月内即可抵消 API 账单成本。Scholz 认为，在三到五年内，大多数 AI 高级用户将实现自托管。入门门槛比你想象的要低：Guillaume Weingertner 2024 年在 *Towards Data Science* 上的演练[让你阅读文章的时间内就能在本地运行模型](https://towardsdatascience.com/how-to-easily-set-up-a-neat-user-interface-for-your-local-llm-1a972da2310e/)。这正是我们几周来一直在探讨的方向。Steven J. Vaughan-Nichols [写过关于 llm-d 的文章](https://thenewstack.io/llm-d-cncf-kubernetes-inference/)，这是一种允许你在任何云上更换任何模型的基础设施。

所以，给出的建议知易行难：调整你的工作流程，使更换模型成为配置更改，而不是重写代码。这就是 OpenClaw 的全部吸引力所在：支持 Agent 的模型是可以更改的。在可预见的未来，团队应该测试开源权重模型，针对实际工作流程对其进行评估，并了解哪些模型可以在自己控制的基础设施上运行。