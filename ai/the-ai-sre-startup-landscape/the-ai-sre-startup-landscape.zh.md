*最后更新：2025年8月20日*

AI SRE 领域异常火爆。其前景引人入胜：如果机器能够替你值班会怎样？多家初创公司应运而生，致力于追逐这款产品中的“白鲸”，以至于我们的客户不断询问我，他们应该将哪些公司与 FireHydrant 集成。

[![](https://substackcdn.com/image/fetch/$s_!L8ke!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6763c94a-c3d1-4a93-b383-b66af72322d5_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!L8ke!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6763c94a-c3d1-4a93-b383-b66af72322d5_1024x1024.png)

SRE 这个名字多年来一直饱受诟病。DevOps 团队一夜之间更名为 SRE，希望能以某种方式“做 SRE 的事情”。现在，“AI”又攀附上神圣的 SRE 之名，使其更加混乱。我在这里是为了帮助那些不知所措的人。

让我们明确一点：SRE 是一个涵盖数十项任务的庞大角色。大型科技公司的 SRE 获得丰厚报酬是有原因的：这是一项要求极高且影响范围（无论是成功还是失败）非常广的工作。

以其目前的2025年形式，“AI SRE”包含两件事：

1.  像工程师一样自主调查事件，工程师会打开仪表盘并尝试在日志中找到确凿证据。
2.  通过代码修复或回滚自主修复根本原因来缓解事件。

这些 AI SRE 代理初创公司不包括通知值班工程师、执行事后回顾或为事件创建工作流的功能。这就是“事件管理”和“AI SRE”之间的区别。

我跟踪 AI SRE 初创公司已有数月，我认为这份列表对于希望尝试这项新技术的企业来说可能很有价值。我对于谁是最好的参与者持中立态度——而且我相信每个人都应该假定这个领域在未来两年内会发生巨大变化。

好了，言归正传！

这些 AI SRE 公司专注于 SRE 中“R”（响应）的调查和补救层。他们不构建值班排班、服务目录、事件管理、状态页面或事后回顾——只是专注于帮助工程师更快解决事件的传统、高度集中的产品。

按字母顺序排列：

**网站：** <https://www.causely.ai/>

> Causely 的因果推理引擎能够在大量告警在您的环境中级联时，自动推断出单一的根本原因。该平台会自动发现您的环境，并在数秒内从您现有的遥测数据中提供洞察——无需设置或调优。

**网站：** <https://cleric.ai/>

> Cleric 是首个为应用团队打造的 AI，它能像高级 SRE 一样进行调查，自主调查生产问题并将结果直接发送到 Slack。Cleric 获得了 Zetta Venture Partners 430 万美元的种子轮融资，它通过形成假设并使用您的工具运行实际查询来解决以前从未见过的问题。

**网站：** <https://neubird.ai/>

> NeuBird 的 Hawkeye 是一款由 AI 驱动的 SRE 副驾驶，它将 LLM 的推理能力带入遥测数据，并采用为企业 IT 构建的可靠、安全的 Agentic AI。该公司最近由 M12（微软的风险基金）领投，Mayfield、StepStone Group 和 Prosperity7 Ventures 参投，筹集了 2250 万美元的资金。

网站：<https://phoebe.ai/>

> 更快地排除故障。针对您的技术栈的 Agentic 搜索。调查错误、事件等。

**网站：** <https://resolve.ai>

> 由 OpenTelemetry 的共同创建者打造，Resolve AI 在几分钟内处理所有告警、执行根本原因分析并解决事件。该平台自主运行以处理常见告警和操作，减少升级，并每周为每位值班工程师节省多达 20 小时。

网站：<https://www.sre.ai/>

> “认识您新的 AI 队友，它们学习迅速，行事负责，并且始终如一地交付。”

**网站：** <https://www.tierzero.ai/>

> TierZero AI 自动调查、分类和解决基础设施问题，相信基础设施应该通过提供正确的洞察和预测问题来实现自我驱动。该公司已通过 SOC 2 Type II 认证，并在 Amazon AWS 上托管其生产服务，采取了企业级的安全措施。

**网站：** <https://traversal.com>

> Traversal 的代理会解析日志、指标、追踪和您的代码库，以缩小错误或延迟的根本原因范围，用简单的自然语言取代了泛滥的告警和日志。该团队由来自麻省理工学院和加州大学伯克利分校的计算机科学博士组成，拥有在 Uber、亚马逊、Citadel 和 Mistral AI 等行业领导者工作的经验。

**网站：** <https://vibraniumlabs.ai/>

> Vibranium AI 充当您的 24/7 值班队友，消除告警疲劳，精确定位根本原因，并提供可操作的洞察，以加快事件解决速度。该平台可将平均解决时间 (MTTR) 缩短多达 82%，并包括一个可加入通话并转录讨论的实时 AI 助手。

**网站：** <https://www.wildmoose.ai/>

> Wild Moose 提供快速、高效的根本原因分析，每次事件后都会改进，将部落知识转化为智能自动化，以应对复杂的环境。该平台通过一个从每次事件中学习的系统模型不断提高性能，并通过 API 在几分钟内完成集成。

🕵️‍♂️ 我是否遗漏了您的公司？给我发电子邮件！[robert@firehydrant.com](mailto:robert@firehydrant.com)

大多数可观测性（O11Y）玩家正在试水——或者说一头扎进——这个领域。这完全说得通：*他们拥有无论如何都将用于调查的数据*，所以他们正在这个宝库之上构建代理工作流。

这些都不足为奇：

*   Chronosphere
*   Datadog
*   Dynatrace
*   Honeycomb\*
*   New Relic
*   Splunk

\*Honeycomb 是这个领域的真正思想领袖。[我推荐阅读 Austin Park 的帖子。](https://www.honeycomb.io/blog/its-end-observability-as-we-know-it-and-i-feel-fine) 他们的博客是关于 AI 在软件开发中应用富有思想的文章的宝库。

在过去的五年里，几家事件管理公司应运而生，填补了 PagerDuty 留下的巨大空白——我们都开始利用这个机会。作为一款事件管理和值班工具的 CEO（如果你不知道的话，就是 [FireHydrant.com](https://FireHydrant.com)），我对这个领域有几百万种看法……

以下是我正在关注的一些事件管理初创公司，它们也在其产品中包含了 AI/SRE 功能：

名字都叫“Incident”了，他们当然会构建“AI SRE”功能。Incident.io 在过去的一个月里加入了 AI SRE 竞争，其产品页面标题醒目地宣称“*AI SRE 像您最优秀的工程师一样解决事件*”。

在 FireHydrant 的所有竞争对手中，我最尊重 incident.io。他们的团队和创始人对我以及 FireHydrant 始终保持着优雅，我很好奇他们的 AI SRE + 其他所有功能的平台将如何发展。

附言：我会打败你，Stephen Whitworth 😈

显然，这是其中最老牌的公司。肯定不再是初创公司了。他们也在构建 AI SRE。他们似乎正在利用几年前对 Rundeck 的收购，来巩固其作为自动化调查和补救工具的地位。他们一直在将 Slack 与调查集成，尽管据我们从现场听到的情况来看效果不佳。我还没听说有哪家公司成功使用它——但也许那是因为我只与那些转向 FireHydrant 的公司交流？谁知道呢。

Rootly 不会在[他们的比较页面](https://rootly.com/blog/incident-management-alternatives-in-2025)上列出 FireHydrant（可能是因为我过去几年[公开指责](https://x.com/bobbytables/status/1403090735038189573)他们的次数太多了）。

Rootly 正在构建一个 AI SRE，但很难知道它具体是做什么的，因为他们的截图只是照搬（[字面意义上](https://www.linkedin.com/feed/update/urn:li:ugcPost:7348384201429147649?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7348384201429147649%2C7348389417276858369%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287348389417276858369%2Curn%3Ali%3AugcPost%3A7348384201429147649%29)）该领域其他供应商的产品。

各有所长吧。

许多企业在其产品中都有某种“AI SRE”的 SKU（库存单位）。多家 DevOps 平台和 CI/CD 公司，甚至代码编写编辑器，都已开始涉足 AI 调查和补救领域。为了完整性，值得一提的是：

*   GitLab
*   GitHub
*   Harness

我确信还有更多。如果我遗漏了您的公司，请给我发电子邮件：[robert@firehydrant.com](mailto:robert@firehydrant.com)。

不，并非如此。

哎呀，我要说的是一件让我更兴奋的事情：与下一代 AI SRE 和可观测性工具进行*合作*。**所有这些工具。**

我最近与无数技术领导者交谈过，他们都在说同样的事情：“我们正在考察市场上*所有*的 AI SRE 工具——而且它们都需要与 FireHydrant 集成。”

企业正在寻找适合其特定需求的 AI 代理。由于技术栈的复杂性和设计差异巨大——没有任何一款 AI SRE 会是“一刀切”的工具。企业甚至可能为其需求购买*多种* AI 工具。

所有这些 AI 工具都需要一个地方来检索事件上下文、阅读事后回顾，并在它们力不从心时**呼叫人类**。这就是我们正在构建的平台。

AI SRE 对 FireHydrant 来说是一个真正的机遇。通过让团队将他们的 AI 代理连接到我们的事件管理平台，企业实际上会得到一些有用的东西。FireHydrant 成为 AI SRE 和现实世界之间的连接组织——团队可以将最适合他们的任何 AI SRE 代理接入我们，作为他们的管理和值班层。对我们来说，这样更合理。

我们 FireHydrant 还有其他更让我们兴奋的事情要解决 👀
