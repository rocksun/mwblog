*我是 Matt Burns，Insight Media Group 的首席内容官。每周，我都会汇总最重要的 AI 进展，解释这些进展对于将这项技术投入工作的个人和组织的意义。核心论点很简单：学会使用 AI 的员工将定义其行业的下一个时代，而本通讯旨在帮助你成为其中一员。*

---

AI 竞赛曾经是关于谁拥有最好的模型。本周，它看起来更像是一场关于发电厂、数据中心以及谁能率先获得 GPU 的争夺战。Anthropic 与 SpaceX 的新交易使 Claude Code 的高级用户限制翻倍，但这只是小故事。更大的故事是，Anthropic [刚刚租赁了](https://thenewstack.io/anthropic-spacex-claude-limits/) Elon Musk 位于孟菲斯的 Colossus 1 设施的全部算力。与此同时，Elon Musk 和 Sam Altman 本周出现在联邦法院，Elon Musk 正试图阻止 OpenAI 转型为营利性公司。

让我们记住大局：Elon Musk 与 Sam Altman 共同创立了 OpenAI，而 Anthropic 的 CEO Dario Amodei 曾是 OpenAI 的早期员工，担任研究副总裁。Elon Musk 和 Dario Amodei 后来都离开了 OpenAI，建立了竞争实验室，并亲自公开批评对方。现在，他们为了困扰每一家前沿 AI 公司（包括 OpenAI）的共同事业而合作：算力。

正如 Alex Wilhelm 本周在 *Cautious Optimism* 中所写，[我原以为 Elon 讨厌 Anthropic](https://www.cautiousoptimism.news/i-thought-elon-hated-anthropic/)。也许他确实讨厌，但也有一种可能，即 Elon Musk 更讨厌 Sam Altman，因为在周三，他将自己为 xAI 训练 Grok 而建造的设施中的所有算力都租给了 Anthropic。

Elon Musk 和 Sam Altman 的审判是表面表演，而 SpaceX 的交易才是实招。

## Anthropic/SpaceX 交易暴露了新的护城河

如果你想了解详细情况——新的速率限制、220,000 个 GPU 的规格、开发者的评价——Meredith Shubel 在我们的网站上有[权威解读](https://thenewstack.io/anthropic-spacex-claude-limits/)。我想谈谈这笔交易意味着什么，因为相比之下，速率限制的故事微不足道。

我大多数日子都会运行 Claude 协作环节，最近，我在下午早些时候就会达到限制（这迫使我不得不去吃午饭）。解决方案从来不是简单的频率微调，而永远是容量。Anthropic 的 Colossus 1 交易让他们[获得了整个设施的使用权](https://x.com/eliebakouch/status/2052066609896808473)——超过 300 兆瓦的电力和 220,000 多个 NVIDIA GPU。根据 [Aakash Gupta 的计算](https://x.com/aakashgupta/status/2052072411894563142)，加上他们最近的其他算力交易，Anthropic 现在拥有大约 15 吉瓦的承诺容量，相当于 1100 万户家庭的用电量，正排队为 Claude 运行。在同一份公告中还隐藏着一行值得圈出的话：Anthropic 表示已“表达了兴趣”，希望与 SpaceX 合作开发多个吉瓦的轨道 AI 算力容量。

解读这一切的正确方式很简单：算力速度就是核心。Anthropic 的年化收入从 2025 年底的 90 亿美元增长到 [4 月份的 300 亿美元以上](https://www.bloomberg.com/news/articles/2026-04-06/broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic)，[Axios 称其为美国商业史上最快的收入增长](https://www.axios.com/2026/04/13/anthropic-revenue-growth-ai)。还记得 Anthropic 的三月吗？持续的产品发布伴随着持续的宕机。周二的交易让 Anthropic 与八周前还在公开嘲讽 Dario Amodei 关于 AI 意识写作的人达成了合作。这应该能告诉你，目前算力高于一切。

## Dario 和 Elon 刚刚选择了同一阵营

作为笑料，在奥克兰进行的 Elon Musk 诉 Sam Altman 案整周都在上演戏码。[法庭上披露了一封 2017 年的邮件](https://www.technologyreview.com/2026/05/01/1136800/musk-v-altman-week-1-musk-says-he-was-duped-warns-ai-could-kill-us-all-and-admits-that-xai-distills-openais-models/)，Elon Musk 在信中对一位 Tesla 副总裁提到 OpenAI 的领导层时说：“OpenAI 的那些家伙会想杀了我，但这是必须做的。”Brockman [作证说他认为 Elon Musk 在 2018 年的权力斗争中差点对他进行肢体攻击](https://www.nbcnews.com/tech/elon-musk/openai-co-founder-says-feared-musk-physically-attack-rcna343736)。Elon Musk [在证人席上似乎承认](https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/) xAI 通过蒸馏技术使用了 OpenAI 的模型。而且 Elon Musk [在开庭陈述前两天还给 Brockman 发短信商讨和解](https://techcrunch.com/2026/05/04/elon-musk-sent-ominous-texts-to-greg-brockman-sam-altman-after-asking-for-a-settlement-openai-claims/)。我一直无法忘记最后一点。这是他做过的最符合 Elon Musk 风格的事，这说明了很多问题。

有趣的部分在于这场争斗之下正在发生的事情。Elon Musk 共同创立了 OpenAI，并在 2018 年输给 Sam Altman 的权力斗争后退出了董事会。Dario Amodei 曾是 OpenAI 的研究主管，于 2021 年离开并创办了 Anthropic。他们两人随后建立了 Sam Altman 公司资金最雄厚的竞争对手。这三个人多年来一直在公开场合互相批评。还记得 Sam Altman 和 Dario Amodei 在印度的一次大型活动上尴尬地并排站着吗？在 Anthropic 与 DoW 的纠纷期间，Elon Musk 对 Dario Amodei 也出言不逊。但本周，这一切都成为了过去，因为 Anthropic 成为了 Elon Musk 巨大数据中心的核心客户。

这笔交易并非孤例。三周前，[Cursor 宣布正在使用](https://cursor.com/blog/spacex-model-training) xAI 的 Colossus 基础设施训练其 Composer 模型，理由也是 Anthropic 现在描述的同样的“算力瓶颈”问题。我在一周后写了关于 [Cursor 600 亿美元赌注的文章](https://thenewstack.io/cursor-sdk-harness/)：SpaceX 要么需要在年底前向 Cursor 支付 100 亿美元，要么拥有对该公司的 600 亿美元收购期权。将 Cursor 和 Anthropic 放在一起，再加上轨道算力的雄心，SpaceX 显然正在将自己定位为算力层。

## 迷因们看透了

## Claude 的梦境智能体需要 15 吉瓦

看看 Anthropic 的产品路线图，就能理解为什么该公司锁定了 Colossus 并讨论天基数据中心。在宣布 Colossus 交易的周三，[我们报道了 Anthropic 正在扩展托管智能体 (Managed Agents)](https://thenewstack.io/anthropic-managed-agents-dreaming-outcomes/)，增加了三项新功能：梦境、基于结果的评估和多智能体编排。Frederic Lardinois 一直在关注这个故事，这篇文章值得你花时间阅读。

“梦境”是核心功能。这是一个预设的后台进程，Claude 在其中审查最近的工作，寻找跨会话的模式，并将这些观察结果写入其记忆中。该公司表示，这是模拟人类大脑在睡眠期间巩固记忆的方式。Anthropic 告诉 Frederic：“记忆和梦境共同构成了一个强大的自我进化智能体记忆系统。”结果评估功能允许你告诉智能体“好”的标准是什么，并使用一个独立的评分智能体——拥有自己的上下文窗口，不准作弊——来检查工作。Anthropic 表示，仅结果评估一项就在其内部测试中将任务成功率提高了多达 10 个百分点。多智能体编排则允许一个主智能体拆分任务并分配子智能体并行工作。

这三个新功能印证了 SpaceX 的交易。每一个功能都在任务执行期间成倍增加算力消耗。梦境是一个持续的后台工作负载，即使你没有向智能体提问，它也在运行。结果评估在第一次推理之上增加了第二次评分推理循环。多智能体编排从定义上讲就是多个智能体的同时执行。这是整个行业的共同模式——当智能体有更多思考时间、更多评分尝试和更多可咨询的同伴时，他们的工作表现最好。前沿实验室正在从仅仅销售 Token 转向销售持续、并行、环境化的认知。而这需要大量的兆瓦电力。

目前，大多数用户关注的是 AI 模型，这很有道理。但兆瓦电力决定了谁能使用它、使用的频率以及价格。这就是为什么这笔交易很重要。Anthropic 不仅仅购买了速率限制的缓解，更购买了更多的智能体容量和环境化功能的空间。

算力是 AI 高级用户面临的限制因素。我们处于 AI 时代的早期。工具会变得越来越好，这可能意味着每个任务将需要更多的算力，而不是更少。Anthropic 正试图提供重度用户想要的东西：无限制。这笔交易是朝着这个现实迈出的一大步。

悬而未决的问题是谁来买单。公开估计显示，Anthropic 的 Colossus 租赁费用每年高达数十亿美元，而用户端的账单已经很高了。上周在 *Towards Data Science* 上，[Ida Silfverskiöld 拆解了智能体 Token 成本](https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/)，发现一个未经优化的智能体每天运行 100 条消息，在 Claude Opus 4.6 上的月花费约为 2,490 美元——大约是经过调优的相同智能体成本的 25 倍。一旦智能体开始在后台进行梦境和相互编排，计算就会变得更加困难。必须有人来支付这些兆瓦电费。是实验室牺牲利润，是企业接受更高的合同，还是个人看着他们的账单攀升，这是我今后会密切关注的故事。