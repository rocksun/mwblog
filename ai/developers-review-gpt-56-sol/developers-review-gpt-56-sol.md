<!--
title: “让我感到震惊”——“有点过度设计”：开发者亲测 OpenAI GPT-5.6 Sol 的真实反馈
cover: https://cdn.thenewstack.io/media/2026/08/913450e5-dimitar-donovski-scaled.jpg
summary: OpenAI 推出了 GPT-5.6 系列模型，其中 Sol 版本因其强大的推理和复杂任务处理能力受到开发者追捧，甚至有开发者用其攻克了数学难题。尽管其表现令人惊艳，但部分用户反馈它偶尔存在过度设计的问题，在特定任务上仍需结合其他模型使用。
-->

OpenAI 推出了 GPT-5.6 系列模型，其中 Sol 版本因其强大的推理和复杂任务处理能力受到开发者追捧，甚至有开发者用其攻克了数学难题。尽管其表现令人惊艳，但部分用户反馈它偶尔存在过度设计的问题，在特定任务上仍需结合其他模型使用。

> 译自：["It blows my mind”-“It has a tendency to overengineer things a little”: Developers react to road-testing OpenAI GPT‑5.6 Sol](https://thenewstack.io/developers-review-gpt-56-sol/)
> 
> 作者：Adrian Bridgwater

OpenAI 于 7 月初向全球的应用和 API 用户发布了其 [GPT-5.6](https://openai.com/index/previewing-gpt-5-6-sol/) 模型系列。

自发布以来，用户可以在 [三种模型版本](https://thenewstack.io/openai-gpt-56-live/) 中进行选择：Sol 是最强大的版本；Terra 适用于主流用途；Luna 则是日常任务中快速、高效的选项。

## Sol 是明星产品

OpenAI 最初将 GPT-5.6 Sol（命名源自拉丁语“太阳”）定位为更具成本效益且能从“每个 token 中获得更多有效工作”的模型，并配备了公司迄今为止最强大的安全栈。该公司宣布为高风险活动和 [敏感网络请求](https://thenewstack.io/what-the-eus-cyber-resilience-act-cra-means-for-open-source/) 提供更强的保护，并花费了“数周时间寻找弱点”，以压力测试系统抵御现实世界攻击的能力。

然而，尽管进行了所有这些强化，开发者似乎对 GPT-5.6 Sol 的核心功能和解决问题的能力最感兴趣。

位于达拉斯沃斯堡的内容自动化平台公司 [BlogBuster](https://www.blogbuster.so/?utm_source=chatgpt.com) 的 AI 研发负责人 [Russell Twilligear](https://www.linkedin.com/in/russell-twilligear/) 告诉 *The New Stack*，他一直在使用 GPT-5.6 Sol，并将结果与 Anthropic 的 [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) 的性能进行了直接对比。

“Sol 在为我创作内容以及发现 Anthropic 模型所犯错误方面做得更好；这让我感到震惊，”Twilligear 说。

“我正在创建一个包含超过 300 万条目的庞大全国性 [数据库](https://thenewstack.io/databases/)（美国），而 Sol 不断发现并纠正 Opus 所犯的错误。因此，我进行了一个角色互换：我要求 Sol 创建数据库，然后要求 Claude Opus 5 对其进行检查，它并没有真正发现任何错误（只有不会影响结果的超小问题）……所以，目前要弄清楚这个市场中所有界限在哪里是一项挑战，”Twilligear 补充道。

> “Sol 在为我创作内容以及发现 Anthropic 模型所犯错误方面做得更好；这让我感到震惊。”

Twilligear 的对比很有趣，尽管这并不完全是一种传统的同类模型测试。使用一个模型作为生成器，另一个作为审核者，并不一定能说明哪个模型“更好”；但它确实表明，当被委派这些特定的生成或审计工作流时，它们的行为表现不同。

虽然这可能不是模型评估的结论性指标，但它确实为我们提供了切实可行的开发者体验，而这无疑是有价值的。

AI 驱动的战略与技能公司 [Concepts in Success](https://www.conceptsinsuccess.com/) 的创始人、AI 治理和模型评估领域独立研究员 [Joshua Estrin](https://www.linkedin.com/in/joshua-estrin-phd-37861217a/) 博士告诉 *The New Stack*，在他看来，这种数据库比较场景是对开发者体验的一种令人信服的洞察，但他认为“仅凭这一点”还不足以证明一个模型比另一个模型更准确，“除非同时将两个输出与绝对真理进行核对”。

“使用一个模型生成工作，另一个模型进行审核，所测量的东西比整体模型质量要狭窄得多，”Estrin 说。“如果一个模型没有标记出另一个模型数据库中的错误，这可能更多地说明了它被提示或被装备去寻找什么，而不是原始模型是否犯了更少的错误。在宣布赢家之前，我希望两个输出都能与真实情况核对——而不仅仅是相互核对。”

> “我使用了具备超强推理能力的 GPT-5.6 Sol……它在更广泛的问题范围内表现有效，并且在维持长期、严谨的数学搜索方面表现更好。”

## 六个开放的 Erdős 问题

哥伦比亚商学院的博士候选人 [Shouqiao Wang](https://x.com/Qiaoqiao2001) 在 [X](https://x.com/Qiaoqiao2001/status/2080003441821163958) 上发帖解释称，他使用 OpenAI GPT-5.6 Sol “在五天内解决了六个开放的 Erdős 问题”。正如所有中欧近似理论和离散数学的爱好者所知，Erdős 问题是由匈牙利数学家 [Paul Erdős](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s#Erd%C5%91s's_problems) 提出的尚未解决的数学假设和问题。

“我有数学背景，但我所使用的 Codex 工作流不需要深厚的数学知识，”Wang 写道。“[但] 秘诀在于模型选择。我使用了具备超强推理能力的 GPT-5.6 Sol。与早期模型相比，它在更广泛的问题范围内表现有效，并且在维持长期、严谨的数学搜索方面表现更好。”

## GPT-5.6 Sol 的超强推理水平更上一层楼

让我们暂停一下，请注意 OpenAI 将“超强（ultra）”定义为它最高能力的设置，协调多个代理跨并行工作流以更快地完成复杂任务，这意味着多个子代理能够并行处理大问题的不同部分。

继低、中、高、超高和最大级别之后，“超强”级别 [更上一层楼](https://www.youtube.com/watch?v=XuzpsO4ErOQ)，因为它通过消耗更多的 token 来换取更强的结果以及在苛刻任务上更快的产出时间。尽管 [OpenAI 在其最近的产品公告中列出了这六个级别](https://openai.com/index/gpt-5-6/)，但 [该公司的其他页面](https://developers.openai.com/api/docs/guides/reasoning) 指定了六个级别，但从“无”开始并以“最大”结束。尽管有装饰性的标签分类约定，但我们可以推断 Sol 拥有一个六速变速箱。

“然后我将提示词粘贴到 Codex 中，将其设定为目标，并让它运行，”Wang 详细说明。“原因在于 Codex 可以长时间工作，保留完整的科研背景，并使用本地文件，无需进一步交互。你需要保持耐心并给它足够的时间去探索，”他补充道。

> “关于 Sol 5.6，我发现的主要问题可能是它倾向于稍微过度设计。对于某些前端任务，我偶尔还是会跳到 Claude 或 Gemini 去解决较小的问题。”

## 知行合一，预订系统开发者的体验

苏格兰爱丁堡旅游预订系统自动化软件公司 [Viamki](https://viamki.com/en/) 的创始人 [Jean Bustinza](https://www.linkedin.com/in/jean-bustinza/) 告诉 *The New Stack*，GPT-5.6 Sol 现在是他的“首选模型”，而且理由充分。

“有时，在要求它输出任何代码之前，我发现自己会就以前觉得超出这些模型范围的高层任务进行长时间的对话，比如更广泛的架构问题，”Bustinza 说。

他将其比作现实生活中“有点像与高级软件开发人员交谈”（但需要注意它偶尔会说一些完全没有意义的话），Bustinza 热情地表示，总体而言，他从 GPT-5.6 Sol 那里获得的信息和推理极其有价值。

“关于 Sol 5.6，我发现的主要问题可能是它倾向于稍微过度设计。对于某些前端任务，我偶尔还是会跳到 Claude 或 Gemini 去解决较小的问题，”Bustinza 补充道。

## 到底谁赢得了模型竞赛？

如果我们要在模型性能竞争中寻找赢家，那么普遍的共识倾向于“视情况而定”的答案，这取决于个人开发者正在将模型功能应用于什么工作。

我们需要记住，一个人所追求的前沿模型长期自主任务分析，并不一定等同于另一个人的多轮任务完成和复杂的科学网络研究工作负载——更不用说我们还需要考虑每个 token 的成本和性价比。

让我们继续聆听开发者的声音。