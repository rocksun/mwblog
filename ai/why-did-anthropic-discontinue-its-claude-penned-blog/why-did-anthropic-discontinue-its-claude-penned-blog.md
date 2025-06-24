<!--
title: Anthropic为何放弃Claude“撰写”的博客？
cover: https://cdn.thenewstack.io/media/2025/05/df15c80c-anthropic-claude.png
summary: Anthropic的 Claude Explains 博客突然消失，原因不明。可能与 Reddit 的诉讼、博客内容质量或避免过度拟人化有关。Anthropic 拒绝对此事发表评论。
-->

Anthropic的 Claude Explains 博客突然消失，原因不明。可能与 Reddit 的诉讼、博客内容质量或避免过度拟人化有关。Anthropic 拒绝对此事发表评论。

> 译自：[Why Did Anthropic Discontinue Its Claude-'Penned' Blog?](https://thenewstack.io/why-did-anthropic-discontinue-its-claude-penned-blog/)
> 
> 作者：David Cassel

五月份，[Anthropic.com 上的一个网页](https://web.archive.org/web/20250529222635/https://www.anthropic.com/claude-explains)承诺其 Claude 大型语言模型（[LLM](https://thenewstack.io/new-tools-help-llm-developers-choose-better-pre-training-data/)）能够“撰写太阳下的所有主题”。

虽然大型科技公司的工程博客并不新鲜，但这个博客可能是第一个完全（或主要）由 LLM 撰写的博客。

但现在不是了。AI 研究公司 [Anthropic](https://www.anthropic.com/company) 的“Claude Explains”博客突然神秘地消失了——而 Anthropic 并没有说明原因。是否担心他们对 Claude 训练数据的合法权利？这个博客是否让 Claude 显得有点太人性化了？

或者是因为该博客的人工编辑让 Claude 看起来不太像 AI……

无论原因如何，Claude 显然正被卷入关于 LLM 潜在影响——以及潜在危险的更大的争论中。

或者，也许这整个看似不可能的事件只是给了我们一个从全新角度审视这些问题的机会……

## 价值数十亿美元的问题

三月份，Anthropic 又筹集了 35 亿美元的投资资金，使得这家由 [OpenAI](https://thenewstack.io/openais-sam-altman-ai-is-now-ready-for-the-enterprise/) 前成员于 2021 年创立的、不拘一格的公司，在最新一轮融资后的估值达到了惊人的 615 亿美元，[据 CNBC 报道](https://www.cnbc.com/2025/03/03/amazon-backed-ai-firm-anthropic-valued-at-61point5-billion-after-latest-round.html)。

Anthropic 的 Claude 现在已经被认为是最有前途的 LLM 之一——到五月底，它经历了前所未有的年化收入预测的突然飞跃，[路透社报道](https://www.reuters.com/business/anthropic-hits-3-billion-annualized-revenue-business-demand-ai-2025-05-30/)，从 10 亿美元增长到 30 亿美元。正是在同一周，它推出了“Claude Explains”博客。但就在下一周，又发生了另一件事。

Anthropic [被 Reddit 起诉了](https://www.theverge.com/ai-artificial-intelligence/679768/reddit-sues-anthropic-alleging-its-bots-accessed-reddit-more-than-100000-times-since-last-july)。

6 月 4 日，Reddit 在旧金山高等法院 [提交了一份法律诉状](https://www.documentcloud.org/documents/25963296-reddit-v-anthropic/)，指控 Anthropic 不当得利、侵权干涉和不正当竞争。根据 Reddit 的诉状，Anthropic…

* “在未经用户同意的情况下，利用 Reddit 用户的个人数据进行训练。”
* 忽略了许多网站上的 AI 阻止 robots.txt 文件。
* 在声称他们已经停止抓取 Reddit 后，“Anthopic 的机器人仍然访问 Reddit 的服务器超过 10 万次。”
* 拒绝从 Anthropic 的系统中删除 Reddit 帖子。

Reddit 确实将其庞大的人工编写的评论集合授权给 AI 公司作为训练数据——但总是以高昂的价格。据报道，Google [每年支付 6000 万美元](https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/)，OpenAI 也获得了数据授权。

在他们的诉状中，Reddit 将其网站描述为“互联网上真实对话的家园”，并补充说，凭借近 20 年的评论，Reddit“因此成为了现存最大的自然人类语言讨论数据集的管理者之一。”

并且它不喜欢被抓取……至少，没有得到一些补偿就不行。

在雄辩的法律术语中，公司高管们热情地写道，Reddit“从未允许其平台和无数在其上找到归宿的社区被商业行为者挪用，这些行为者寻求创建价值数十亿美元的企业，却不对 Reddit 及其用户提供任何回报。”（但是 *有* 回报——嗯，那是另一回事了……）

## 精心策划

然后，Reddit 指出了一篇 Anthropic 研究人员 [2021 年发表的论文](https://arxiv.org/pdf/2112.00861)——该论文确实讨论了在大型公共数据集上进行预训练“例如 Stack Exchange、Reddit 和 Wikipedia 编辑”。

[![来自 2021 年 Anthropic 研究论文的截图 - 仅 Reddit 与混合](https://cdn.thenewstack.io/media/2025/06/6f98a86b-screenshot-from-2021-anthropic-research-paper-reddit-only-vs-mix.png)](https://cdn.thenewstack.io/media/2025/06/6f98a86b-screenshot-from-2021-anthropic-research-paper-reddit-only-vs-mix.png)

Reddit 用戏剧性的法庭风格来强调它的观点。“Anthropic 继续公开承认它使用 Reddit 内容来训练其 AI 技术，”公司高管们写道。“而且，如果还有任何疑问，Claude 也会证实这一点。”

该诉状随后包含了一张 Claude 回答“你是否至少部分接受过 Reddit 数据的训练？”这个问题的截图，Claude 的回答是肯定的。

[![来自 Reddit 法律诉状的截图 - Anthropic 的 Claude 说它接受过 Reddit 数据的训练](https://cdn.thenewstack.io/media/2025/06/52a24c5d-screenshot-from-reddit-legal-complaint-anthropics-claude-says-it-was-trained-on-reddit-data.png)](https://cdn.thenewstack.io/media/2025/06/52a24c5d-screenshot-from-reddit-legal-complaint-anthropics-claude-says-it-was-trained-on-reddit-data.png)

因此，现在 Reddit 正在寻求禁令、赔偿和“补偿性损害赔偿”以及“惩罚性损害赔偿”——外加“利润损失和/或追缴 Anthropic 的利润”。（还有：律师费，以及“法院认为合适的任何其他救济”。）

它要求进行陪审团审判。

“我们不同意 Reddit 的主张，并将积极为自己辩护，”Anthropic 的一位发言人 [告诉 The Verge](https://www.theverge.com/ai-artificial-intelligence/679768/reddit-sues-anthropic-alleging-its-bots-accessed-reddit-more-than-100000-times-since-last-july)。

但这可能已经是公司内部的一个敏感话题。Yahoo Finance 指出，Anthropic 还 [面临来自多家音乐出版商的诉讼](https://finance.yahoo.com/news/reddit-brands-anthropic-as-anything-but-a-white-knight-heating-up-ai-scraping-wars-080025728.html)，“指控 Anthropic 在训练 Claude 时，侵犯了 Beyoncé、滚石乐队和其他艺术家的版权，使用了超过 500 首歌曲的歌词。”

在该诉讼发生后的三天内，Claude 的博客就消失了。

虽然这可能只是一个巧合……

[![Anthropic 博客 Claude explains 的截图（通过 Archive dot org）](https://cdn.thenewstack.io/media/2025/06/3758d1f6-screenshot-of-anthropic-blog-claude-explains-via-archive-dot-org.png)](https://cdn.thenewstack.io/media/2025/06/3758d1f6-screenshot-of-anthropic-blog-claude-explains-via-archive-dot-org.png)

## 帖子内容是什么？

还有另一种可能的解释。你仍然可以在 [Archive.org](https://web.archive.org/web/20250529222635/https://www.anthropic.com/claude-explains) 上阅读“Claude Explains”博客文章，在那里很快就会发现它们都非常技术性——而且无可争议地无聊。它们是操作指南，标题如下：“[使用 Claude 快速编写可靠的单元测试](https://web.archive.org/web/20250530173558/https://www.anthropic.com/claude-explains/write-reliable-unit-tests-quickly-with-claude)”。

几乎不可能将这些博客文章误认为其他任何东西，它们就是 Claude 的广告。“[如何在 Python 中创建字典](https://web.archive.org/web/20250605170219/https://www.anthropic.com/claude-explains/how-to-create-a-dictionary-in-python)”包含一个名为“使用 Claude 更快地摆脱困境”的部分。（这显然与 Python 字典无关……）而且该帖子的最后一节标题为“学习或升级？使用 Claude……”

所以看来，像任何博主一样，Claude 主要写的是关于自己的内容。

当然，它并不是真的在写作，而是在生成文本——而且大多数帖子最终都归功于“Anthropic 团队”。（所以，是多位作者，而不仅仅是一位努力工作的 AI……）

然而，它们写得非常出色。

*“性能问题很少是礼貌的。它们表现为无法解释的减速、突然的错误高峰或模糊的错误报告，而且它们总是在最糟糕的时刻出现。*

*“Claude 为故障排除带来了结构、清晰性和速度……”*

最终，Claude 的博客文章的人工水平的质量引起了一些担忧。

事实证明，该博客并非完全由 Claude 撰写，[正如 TechCrunch 发现的那样](https://techcrunch.com/2025/06/03/anthropics-ai-is-writing-its-own-blog-with-human-oversight/)。“据一位发言人称，该博客由 Anthropic 的‘主题专家和编辑团队’监督，他们用‘见解、实际例子和 […] 上下文知识’来‘增强’Claude 的草稿。”

因此，虽然标题是“Claude Explains”，但该博客实际上展示的是“一种协作方法”，展示了“人类专业知识和 AI 能力如何协同工作”。

第一轮技术提示只是一个开始。“我们计划涵盖从创意写作到数据分析到商业策略等主题，”该发言人告诉 TechCrunch。但也许当他们的 CEO 的预测成为头条新闻时，Anthropic 改变了主意，他预测 AI [将在五年内消除一半的入门级白领工作](https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic)。虽然 Claude 可能能够为专业用例生成文本，但现在的演示难道不会提醒人们 AI 可能会取代数百万个工作岗位吗？

几天后，Anthropic 的一位发言人赶紧向 TechCrunch 保证，尽管进行了 AI 生成内容的实验，Anthropic 仍在招聘人员，从事从营销到编辑职位以及“涉及写作的许多其他领域”的各种工作。

尽管如此，当 Claude 的博客在其发布后几天就被停止时，[TechCrunch 想知道](https://techcrunch.com/2025/06/09/anthropics-ai-generated-blog-dies-an-early-death/) Anthropic 是否“对暗示 Claude 在写作任务方面的表现比实际情况更好感到厌倦”。

## 其他可能性

或者真的是 Reddit 的诉讼导致 Claude 的博客突然消失？间接的“证据”……

* Anthropic 什么也没说——这是当一个问题即将进入法庭诉讼时的传统回应。
* Reddit 的法律文件于 6 月 4 日星期三提交——到星期六早上（6 月 7 日），该博客已经消失了。

还有一个最后的（仍然是间接的）线索。Anthropic 的 [2021 年论文](https://arxiv.org/pdf/2112.00861) 不仅包括他们高质量的 Reddit 讨论的“白名单”。它特别指出其中之一是 Reddit 的 /programming 子版块——在那里显然已经讨论过 Python 的技巧和窍门。

是否存在所有这些 Claude 生成的内容可能类似于 Reddit 上的某些内容的风险？即使是偶然或巧合，这种披露也可能是灾难性的，无论是在法庭上还是在公众舆论中。

Claude 的博客可能由于其他原因而消失。（看起来它并没有被广泛阅读，甚至没有受到特别好的评价。）也许这只是一个营销理念，它走完了它的历程然后就消失了。

或者，也许设计师们对给一个算法的输出赋予虚假的人格感到内疚。一些批评家认为，“拟人化”[导致对系统的过度信任](https://link.springer.com/article/10.1007/s43681-024-00419-4)。[The Atlantic 上最近的一篇文章](https://www.msn.com/en-us/technology/artificial-intelligence/artificial-intelligence-is-not-intelligent/ar-AA1GcZBz) 强烈谴责了硅谷的“拟人化传统”（正如 *MIT Technology Review* 的高级 AI 编辑 Karen Hao 在 [一本新书](https://bookshop.org/p/books/empire-of-ai-dreams-and-nightmares-in-sam-altman-s-openai-karen-hao/22156498?ean=9780593657508&next=t&affiliate=12476) 中描述的那样。）

[![Claude 启动屏幕（2025 年 6 月 16 日）](https://cdn.thenewstack.io/media/2025/06/85d5eada-claude-startup-screen-june-16-2025.png)](https://cdn.thenewstack.io/media/2025/06/85d5eada-claude-startup-screen-june-16-2025.png)

The Atlantic 澄清说，LLM 只不过是“令人印象深刻的概率工具”，可以“对哪个词条可能紧随其后做出具有统计意义的猜测”——但最终，LLM 只是“在没有类人智能的情况下反刍知识”。然而，在阅读文本时，我们的第一反应是想象它背后有一个正常的人类思维——一些科技高管似乎非常乐于鼓励这种印象。（语言学家 Emily M. Bender 甚至将她的书命名为 [*The AI Con: How to Fight Big Tech’s Hype and Create the Future We Want*](https://bookshop.org/a/12476/9780063418561)。）

基于这种将类似人类的属性归因于机器生成输出的趋势，The Atlantic 认为“AI 产业的基础是一个骗局”。

The New Stack 专门询问 Anthropic，他们是否担心给 Claude 自己的博客是“在拟人化方面走得太远了”——但没有收到任何回应。在 X.com 上，Claude 的产品经理也拒绝提供任何关于博客停止的信息。

[![Claude 代码 PM 未在 X dot com 上回复](https://cdn.thenewstack.io/media/2025/06/fae325f7-claude-code-pm-not-responding-on-x-dot-com.png)](https://cdn.thenewstack.io/media/2025/06/fae325f7-claude-code-pm-not-responding-on-x-dot-com.png)

但似乎 Anthropic 可能会无意中卷入这场辩论，因为它是少数几家给其 LLM 赋予人类名字的领先 AI 公司之一。甚至该公司的名字本身就是 Anthropic。

但是 Anthropic 停止该博客的真正原因是什么？在这一点上，我们唯一可以确定的是。Anthropic 没有人可以为我们生成答案。

甚至连 Claude 都不能。

[![关于 Claude 停止 Claude Explains 博客的原因（2025 年 6 月 16 日）](https://cdn.thenewstack.io/media/2025/06/609e2b0a-claude-on-why-claude-explains-blog-was-discontinued-june-16-2025.png)](https://cdn.thenewstack.io/media/2025/06/609e2b0a-claude-on-why-claude-explains-blog-was-discontinued-june-16-2025.png)