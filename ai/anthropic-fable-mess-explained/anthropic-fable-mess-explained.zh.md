The [Anthropic-Mythos-Fable 故事](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) 从上周五开始就成为了热门话题，其进展速度之快，稍不留神就会错过重点。以下是我对事件经过、各方评价的个人观点。

我的结论是：Anthropic 在这件事上大部分处理是正确的，这对 Fable 来说简直是一场绝佳的广告。

## **时间线**

**2月/3月：** Anthropic 与国防部因公司 AI 模型的使用问题[产生争执](https://www.anthropic.com/news/statement-department-of-war)；Anthropic [希望对其技术的使用方式设定一定的限制](https://www.anthropic.com/news/statement-comments-secretary-war)。随后的冲突导致 Anthropic [被称为供应链风险](https://www.anthropic.com/news/where-stand-department-war)，在理论上限制了政府对其模型的使用，同时也限制了政府承包商获取这些模型。

**4月7日：** Anthropic 推出了新的模型系列 Mythos。在发现 Mythos 擅长发现并利用新型网络安全漏洞后，Anthropic 发起了“[Glasswing 项目](https://www.anthropic.com/glasswing)”，为关键技术公司提供获取工具的途径，以便它们在更大范围发布前加固自己的软件。

**4月16日：** 据报道，白宫[正在致力于](https://www.bloomberg.com/news/articles/2026-04-16/white-house-moves-to-give-us-agencies-anthropic-mythos-access?embedded-checkout=true)让机构可以使用 Mythos 的版本。

**4月30日：** Anthropic 希望扩大可以访问 Mythos 的群体数量；据报道，白宫[反对这一举措](https://www.wsj.com/tech/ai/white-house-opposes-anthropics-plan-to-expand-access-to-mythos-model-dc281ab5)，担心增加更多的合作伙伴会导致 Anthropic 计算资源受限，从而限制美国政府对该模型的访问。

![](https://www.cautiousoptimism.news/wp-content/uploads/sites/3/2026/06/image-22-1024x409.png)

**6月2日：** Anthropic [宣布](https://www.anthropic.com/news/expanding-project-glasswing) Glasswing 项目的首批 50 家合作伙伴通过使用 Mythos 发现了超过 10,000 个严重的软件漏洞。该公司将 Glasswing 项目扩展到 15 个国家的 150 个新组织。Anthropic 还承诺正在努力“安全地发布 Mythos 级别的能力供通用访问”，但补充称，防止模型网络能力被滥用的“高度稳健的防护措施——这些防护措施我们（以及据我们所知，所有其他 AI 开发人员）尚未开发出来。”

**6月9日：** Anthropic [宣布并发布了 Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)，这是一款旨在降低网络安全和生物相关风险的“Mythos 级”模型。该公司在发布说明中表示，已经为 Mythos (Fable) 构建了足以进行“通用发布”的防护措施。当时，Anthropic 表示，它通过使 Fable 5 的护栏“比理想状态更严格”来“优先考虑安全性”。

* 一些用户发现 Fable 5 在某些用例（主要是生物相关查询）中的限制非常严格，以至于几乎无法使用。
* Fable 5 还具有蒸馏保护和严格的 30 天数据保留政策，Anthropic 声称这将有助于“防御复杂和新型攻击（包括新的越狱攻击和跨多次请求的攻击），并帮助[其]识别和减少误报。”
* 在此节点上，针对 Anthropic 的主要投诉是它太谨慎了；通过将 Mythos 保密并仅发布该模型的安全导向版本（Fable），它制造了一个[双层 AI 市场](https://www.cautiousoptimism.news/anthropic-just-added-a-velvet-rope-to-the-ai-club/)。人们不喜欢这样！

Anthropic 在 6 月 9 日 Fable 发布之前，“[此前已多次通知政府](https://www.axios.com/2026/06/13/anthropic-amazon-white-house)”其发布日期。

**6月10日：** Anthropic [发布了两个框架](https://www.anthropic.com/policy-on-the-ai-exponential)，旨在解决高级 AI 开发及其经济影响问题。这些论文呼吁“政府采取行动和监管——这些监管旨在仔细设计以防止政府越权并保护创新”，包括在“模型构成此类风险时”，允许政府“拥有法律授权来阻止或威慑其部署。”

**6月11日：** 据报道，亚马逊的 Andy Jassy [告诉政府](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578)，其研究人员发现了一种方法，可以让 Fable 5 “提供[其]可能被用于辅助网络攻击且本应被限制的信息。”（至少还有五家其他公司[也对此表示附和](https://www.axios.com/2026/06/13/anthropic-amazon-white-house)，这使得它不再仅仅是亚马逊的问题，尽管它是关键参与者。）

**6月12日：** 白宫高级幕僚和行政领导层开会讨论了这一情况，然后通过电话将 Anthropic CEO Dario Amodei 加入了对话。（据 [Politico 报道](https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519)，这次通话持续了 1.25 小时，公司表示在此期间提供了其他高管；关于为何花了这么长时间才接通 Amodei 的电话存在分歧。我们可以跳过这些戏份，专注于重要的事情。）

**6月12日（续）：** Amodei [将此问题视为](https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519)一种误解，并辩称报道的“绕过”并没有“构成与更广泛的‘越狱’相同的风险。”白宫“敦促”Anthropic “自愿移除该模型并与政府协调以解决漏洞。”Amodei 要求更多的“时间和信息，但他没有做出撤下模型的承诺。”

* Politico 报道称，据白宫高级官员透露，财政部长 Scott Bessent “直接告诉 Amodei，他正在做出一个‘错误的决定’。”

**6月12日（继续）：** 在未能与 Anthropic 达成协议后，特朗普政府对 Fable 5 和 Mythos 5（这两个是已发布的 Mythos 级模型版本，具有不同的安全限制）实施了出口管制。

* Anthropic [回应](https://www.anthropic.com/news/fable-mythos-access)称，“暂停任何外国国民（无论是在美国境内还是境外，包括在 Anthropic 工作的外国国民）对 Fable 5 和 Mythos 5 的所有访问的出口管制指令”意味着它必须“突然禁用我们**所有**客户的 Fable 5 和 Mythos 5，以确保合规。”（强调为原文所有。）

## 好人 Anthropic，论点

Anthropic 构建了一个新的、更强大的 AI 模型，它认为该模型具有独特、新颖的网络相关能力。它希望在模型引发网络安全风险之前采取行动，因此迅速组建了一个领先的技术公司团体，并为他们提供了补贴性的早期访问权限；政府在发布前对 Fable 的防护措施进行了红队测试……

***这是摘自《Cautious Optimism》的内容，这是一份专注于技术、商业和权力的*** ***温和乐观*** ***出版物。*** ***阅读关于 Anthropic 的支持和反对论点，以及 Alex Wilhelm 的观点，请访问 [Cautious Optimism](https://www.cautiousoptimism.news/the-anthropic-fable-mess-explained?utm_source=The+New+Stack&utm_medium=referral&utm_campaign=Article+Excerpt)。***