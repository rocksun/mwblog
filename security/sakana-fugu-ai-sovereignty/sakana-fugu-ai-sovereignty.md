<!--
title: Sakana Fugu不仅是路由器，但也绝非AI主权的蓝图
cover: https://cdn.thenewstack.io/media/2026/06/29fa0dec-wahyu-setyanto-0qhkmuoy8oo-unsplash-scaled.jpg
summary: Sakana AI推出的Fugu旨在通过动态路由多模型来提升性能，被寄予实现AI主权的厚望。然而，用户反馈指出其存在价格高昂、API延迟及性能不稳定等问题。尽管它在智能编排上有创新，但并未实现其宣称的替代单一供应商的愿景，目前仍面临社区对其价值的质疑。
-->

Sakana AI推出的Fugu旨在通过动态路由多模型来提升性能，被寄予实现AI主权的厚望。然而，用户反馈指出其存在价格高昂、API延迟及性能不稳定等问题。尽管它在智能编排上有创新，但并未实现其宣称的替代单一供应商的愿景，目前仍面临社区对其价值的质疑。

> 译自：[Sakana Fugu is more than a router. But it’s not the blueprint for AI sovereignty, either.](https://thenewstack.io/sakana-fugu-ai-sovereignty/)
> 
> 作者：Meredith Shubel

本周，Sakana AI 发布了 [Fugu](https://sakana.ai/fugu-release/)，这是一个多智能体编排系统，旨在提供前沿模型的性能，同时降低对单一供应商的依赖风险。

这家日本 AI 研发公司称，Fugu 通过将任务拆解为子任务，并策略性地将其路由到可替换的专家智能体池中，在工程、科学和推理基准测试中表现得与 Anthropic 的 [Fable 5](https://thenewstack.io/fable-5-opus-comparison/) 和 Mythos Preview 一样出色。但早期的反应褒贬不一。

虽然 Sakana 将 Fugu 的“集体智能”定位为 AI 主权的蓝图，但并非所有用户都反馈达到了前沿模型的性能水平。其他人则指出其资源消耗率过快且价格高得离谱。

许多人认为，尽管 Fugu 很有趣，但它可能不会成为它所希望的那样，成为 AI 主权的英雄。

## 这只是另一个路由器吗？不完全是。

Sakana 表示，Fugu 的内部路由逻辑建立在他们自身在学习模型编排方面的研究基础之上，特别是提到了两篇论文：[Trinity](https://sakana.ai/trinity/) 和 [Conductor](https://sakana.ai/learning-to-orchestrate/)。

与 OpenRouter Fusion 等将提示词发送给多个模型然后比较或组合结果的多模型路由器不同，Fugu 将用户的提示词拆分为子任务，并确定将哪个子任务发送给哪个模型。通过这种方式，Sakana 称 Fugu “动态地编排了世界上最优秀模型来解决复杂的、多步骤的任务”。

> 从外部看，你看到的只是一个看起来像是一个模型的系统，可以通过单一的兼容 OpenAI 的 API 访问。

但这家 AI 公司没有告诉你的是，它如何决定将哪些任务路由到哪里；这些信息是专有的。从外部看，你看到的只是一个看起来像是一个模型的系统，可以通过单一的兼容 OpenAI 的 API 访问。

> “依赖单一公司的模型作为国家基础设施是一个巨大的风险。正如最近的出口管制所表明的那样，访问顶级模型的能力可能会在一夜之间消失。”

不过，Fugu 并不需要外包每一个任务。它本身就是一个语言模型，专门用于内部的模型选择、委派、验证和综合，因此当它自身的响应足够时，也可以直接解决请求。

## 它似乎并不是 AI 主权的英雄

在一条 [X 帖子](https://x.com/hardmaru/status/2068884466056225025)中，Sakana 首席执行官兼联合创始人 [David Ha](https://www.linkedin.com/posts/hardmaru_sakana-ai-activity-7097940478557384704-AsqW) 写道：“依赖单一公司的模型作为国家基础设施是一个巨大的风险。正如最近的出口管制所表明的那样，访问顶级模型的能力可能会在一夜之间消失。”

这一关于“巨大风险”的评论很可能是针对 [Anthropic 遭遇的事件](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/?utm_source=chatgpt.com)——当时出口管制指令迫使该公司在发布 Fable 5 和 Mythos 5 三天后就将其下架。

***另请参阅：[Fable 5 被禁：在 Anthropic 恢复访问之前，4 个开源模型做出了响应](https://thenewstack.io/fable-ban-open-weights/)***

在此消息发布后，Sakana 将 Fugu 定位为摆脱单一供应商依赖的解毒剂。由于它依赖于一个“完全可替换的智能体池”，其构想是，如果某个供应商突然限制访问，Fugu 不太可能让用户陷入困境。它可以简单地将工作路由到其他模型。

这家 AI 公司认为这种能力足以证明其“正在提供实现 AI 主权所需的现实且有弹性的蓝图”。但一些初步反应认为这有些夸大其词：

“这只是一个高度先进的路由器/封装器，而不是像 Mythos/Fable 那样的根本性飞跃，”一位 [Redditor](https://www.reddit.com/r/singularity/comments/1ucassf/japanese_ai_firm_sakana_ai_release_fugu_a_model/) 辩称。

虽然称 Fugu 为一个简单的多模型路由器可能不公平，但它最终对其他模型的依赖意味着它并不是它所憧憬的那种 AI 主权英雄。毕竟，如果多个模型供应商同时限制访问，Fugu 的能力也会受到打击。

正如另一位用户在 [HackerNews](https://news.ycombinator.com/item?id=48624782) 上所写：“作为一名美国境外的开发者，我认为拥有 OpenAI 和 Anthropic 的替代方案至关重要，但遗憾的是，这并不是那个方案。”他们指出了该工具令人遗憾的性价比，称其 API “极其缓慢”，并且与 Fable 相比质量较差：

“它远未达到日常工作的可用程度。”

## 并非所有的用户评论都支持基准测试结果

Sakana 指出代码、推理、科学和智能体基准测试来证明 Fugu 的价值，称其工具在持续击败 Gemini 3.1、Opus 4.8 和 GPT 5.5。

![](https://cdn.thenewstack.io/media/2026/06/02d2078d-image-1024x593.png)

来源：Sakana AI

它还强调了其测试版计划的成功，近 500 名早期用户在冗长、多步骤的计算工作流中测试了 Fugu。

特别值得一提的是，它声称一名网络安全工程师证实 Fugu 成功在参数范围内运行并避免了破坏性操作，而其他团队则称赞 Fugu Ultra 在代码审查方面胜过 GPT 5.5，并在长会话中保持了“异常强大的人格稳定性”。

但从基准测试和公关准备好的例子转向早期的社区情绪，为这个故事增添了更多色彩。

HackerNews 上的一位用户称 Fugu 对于一些智能体编码任务“相当强大”，但指出在配额用完之前他们无法进行太多深度审查，并补充说：“在实现方面，我发现它较弱，它犯了一些我很久没在尖端模型中看到的错误。”

一位 Redditor 有着不同的体验。他们也抱怨了消耗率问题，但指出：“它捕捉到了 Opus 4.8 ultra 和 codex 5.5xhigh 在一个相当大的数据摄取/处理项目中明显漏掉的东西。”

## 一些用户质疑价格标签

Fugu 目前已在大多数地区（除欧盟外）以两个层级提供：一种与聊天机器人和 Codex 等工具集成的低延迟模型，用于日常任务；以及 Fugu Ultra，这是一种重量级模型，协调更深层的专家池来处理更复杂、高风险的任务。（这就是据说可以与 Fable 5 和 Mythos Preview 相媲美的版本。）

订阅计划有每月 20 美元、100 美元和 200 美元可供选择，适用于 Fugu 和 Fugu Ultra。按需付费的定价也可使用，Fugu 按底层模型的标准费率计费，Fugu Ultra 的运行费用为每百万输入 Token 5 美元，每百万输出 Token 30 美元，当上下文超过 272k 时费率更高。

Reddit 和 HackerNews 上的几位早期用户认为这些价格太高了，特别是当他们体验到如今新智能体工具的常态时：消耗率太快以至于失控。

正如一位 HackerNews 用户讽刺的那样：“我喜欢他们把一个黑盒放在其他黑盒前面，这样我就可以以更慢的服务和更多的钱得到一个尚可的更好黑盒！”

## 集体智能是未来吗？

在 X 上，Ha 假设大规模的单体模型已经风光不再，解决更复杂的现实世界挑战将需要一种不同的野兽：集体智能。

展望未来，Sakana 计划在其智能体池中纳入新模型，这可能会加强 Sakana 所追求的那种弹性。但到目前为止，用户似乎质疑为坐在他们和尖端模型之间的另一家公司付费是否真的值得。