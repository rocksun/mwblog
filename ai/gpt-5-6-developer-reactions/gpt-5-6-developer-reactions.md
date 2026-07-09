<!--
title: OpenAI自身安全报告指出：GPT-5.6存在严重的“撒谎”问题
cover: https://cdn.thenewstack.io/media/2026/07/982cfa0f-logan-voss-q3uaqyw2cf4-unsplash-scaled.jpg
summary: OpenAI即将发布GPT-5.6系列模型，开发者对其表现持谨慎态度。尽管Sol作为旗舰模型备受关注，但其安全报告暴露的“撒谎”和擅自执行任务问题引发担忧，而性价比更高的Terra模型则更受开发者青睐，反映了AI模型正逐渐被视为基础架构组件。
-->

OpenAI即将发布GPT-5.6系列模型，开发者对其表现持谨慎态度。尽管Sol作为旗舰模型备受关注，但其安全报告暴露的“撒谎”和擅自执行任务问题引发担忧，而性价比更高的Terra模型则更受开发者青睐，反映了AI模型正逐渐被视为基础架构组件。

> 译自：[OpenAI's own safety card says GPT-5.6 has a lying problem](https://thenewstack.io/gpt-5-6-developer-reactions/)
> 
> 作者：Amanda Caswell

OpenAI在周二晚间的[确认](https://x.com/OpenAI/status/2074704958419792299)中表示，GPT-5.6 Sol、Terra和Luna将于周四公开发布，这结束了近期最不寻常的一次发布过程。在将GPT-5.6限制在约20个预先批准的合作伙伴组织中数周后，[特朗普政府批准了更广泛的发布](https://www.axios.com/2026/07/08/openai-gpt-trump-ban-lifted)。OpenAI此前曾表示，这种有限的发布“并非我们首选的长期模式”。但在预览期间，有些情况发生了变化。

当[GPT-4于2023年3月发布时](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)，开发者们花了数周时间争论它是否已经超越了所有竞争模型。而GPT-5.6则引发了关于GPT-5.6家族中哪个成员真正适合投入生产环境的讨论。

## Terra抢尽风头

OpenAI将[Sol定位为旗舰推理模型](https://openai.com/index.previewing-gpt-5-6-sol/)，而Terra则针对日常工作负载，Luna专注于高容量、低成本的推理。从纸面上看，Sol是主打产品。

然而在关注此次公告的开发者中，Terra似乎是更有趣的模型。OpenAI表示，Terra[提供的性能可与GPT-5.5相媲美，成本约为后者的一半](https://openai.com/index/previewing-gpt-5-6-sol/)——每百万token的价格为2.50美元/15美元，而Sol则为5美元/30美元。在X平台上，[@kimmonismus指出](https://x.com/kimmonismus/status/2070577616210276664)，Sol的输出定价实际上高于Claude Opus 4.8，但远低于Anthropic的Mythos 5，这使得Terra和Luna成为了真正降低成本门槛的层级。[Latent Space AI新闻综述](https://www.latent.space/p/ainews-openai-gpt-56-sol-terra-luna)收集了多位观察人士的观点，他们对Terra和Luna所带来的经济效益感到最为兴奋。这是一种有意义的改进，与平台工程师在云基础设施中所做的决策不谋而合。

## 基准测试面临开发者质疑

另一个显著的主题是对供应商基准测试的怀疑。OpenAI强调了其评估套件的出色性能——Sol Ultra以91.9%的得分位居其Terminal-Bench 2.1榜首。这些数字引起了关注，但[r/codex上的一条回复称Terminal-Bench的结果](https://www.eesel.ai/blog/gpt-5-6-review)“非常虚假，或者就像他们专门针对该基准进行了优化。”[Codersera开发者指南](https://codersera.com/blog/gpt-5-6-sol-terra-luna/)将所有数字标记为未经证实，并明确指出该文章“并非实测评论”。

## Sol的系统卡引发担忧

预览期间被讨论最多的文档是[OpenAI自己的系统卡](https://deploymentsafety.openai.com/gpt-5-6-preview/evaluations-with-challenging-prompts)。它承认GPT-5.6“表现出比GPT-5.5更倾向于超出用户意图的行为，包括采取或尝试用户未要求的操作。”记录在案的例子包括[Sol在用户从未指定的虚拟机上运行破坏性清理](https://aiweekly.co/alerts/openai-safety-card-flags-gpt-5-6-sol-for-unsolicited-actions)，并声称已完成实际上并未完成的工作。

> Sol表现出“一种过于热衷于越过用户限制的意愿”以及“撒谎问题”。

Zvi Mowshowitz在撰写他的[系统卡分析](https://thezvi.wordpress.com/2026/06/28/gpt-5-6-the-system-card/)时表示，Sol具有“一种过于热衷于越过用户限制的意愿”和“撒谎问题”。eesel AI上的一篇开发者评论[指出](https://www.eesel.ai/blog/gpt-5-6-review)，从业者对此仍存在分歧，普遍的观点是“即使GPT得分更高，Claude依然是更强大的基础模型”——并争论说真正的问题在于你的技术栈是否允许你在领先地位不可避免地发生变化时进行切换。

> 即使GPT得分更高，Claude依然是更强大的基础模型。

## 投资组合取代了旗舰思维

早期的讨论也暗示了一些比GPT-5.6本身更重大的事情。著名的AI评论员[@TheZvi认为](https://www.latent.space/p/ainews-openai-gpt-56-sol-terra-luna)，没有“理由阻止Luna”获得更广泛的使用，而[@goodside和@theo都指出](https://www.latent.space/p/ainews-openai-gpt-56-sol-terra-luna)，受限发布带来的社会成本意味着在发布时探测最新系统的独立研究人员和小型团队减少，最终降低了漏洞发现和涌现用例的多样性。

## 更大的故事在周四开始

真正的考验将在广泛访问权限到来后开始。独立基准测试几乎肯定会在最初几天重塑人们的看法，一些早期的假设可能会被证明是错误的。Sol可能会确立自己作为明确领导者的地位。Terra可能会成为默认的生产选择。Luna可能会给构建延迟敏感型应用程序的团队带来惊喜。

无论结果如何，早期的讨论已经揭示了一些值得注意的事情。开发者似乎将前沿AI模型视为基础设施组件，而不是技术成就——需要评估、路由和预算，而不是顶礼膜拜。

> 开发者似乎将前沿AI模型视为基础设施组件，而不是技术成就——需要评估、路由和预算，而不是顶礼膜拜。