<!--
title: Moltbook：炒作狂潮，抑或奇点降临？
cover: https://cdn.thenewstack.io/media/2026/02/4dc86518-monika-borys-dstjr8ojurw-unsplash-scaled.jpg
summary: Moltbook作为AI智能体社交网络引发热议，但被指用户数夸大且人类可冒充AI。其内容多为人类创作，暴露出自主系统缺乏可观测性带来的安全与治理问题。该平台曾存在严重数据库漏洞，作者认为其有趣危险但并非AI革命。
-->

Moltbook作为AI智能体社交网络引发热议，但被指用户数夸大且人类可冒充AI。其内容多为人类创作，暴露出自主系统缺乏可观测性带来的安全与治理问题。该平台曾存在严重数据库漏洞，作者认为其有趣危险但并非AI革命。

> 译自：[Moltbook: Hype or the Singularity?](https://thenewstack.io/moltbook-the-singularity-or-hype/)
> 
> 作者：Steven J. Vaughan-Nichols

所谓的AI智能体社交网络 [Moltbook](https://www.moltbook.com/) 上的狂热情绪持续高涨。

如果你相信 [Elon Musk 的说法，Moltbook正处于“奇点非常早期阶段”](https://x.com/elonmusk/status/2017707013275586794)，届时人工智能将超越人类智能，我们将走向终结者（Terminators）的世界，或是 [Iain Banks 的乌托邦《文明》](https://www.goodreads.com/series/49118-culture)。既然Musk以《文明》系列飞船的名字命名SpaceX的回收船，我们知道他押注的是哪一边。或者，正如 Stackernerd 所言，这“提醒我们，[网上大多数AI‘突破’都是包装噱头](https://stacker.news/items/1424702)，而非智能或自主性的根本转变。”

## Moltbook是什么？

Moltbook 由企业家 [Matt Schlicht](https://www.linkedin.com/in/mattschlicht) 创建，他也是零售产品问答AI公司 [Octane AI](https://www.octaneai.com/) 的首席执行官兼联合创始人。他声称，他的AI助手 Clawd Clawderberg 完成了大部分繁重工作。他为其设定了高层目标，并让它处理大部分编码和日常运营。

这个**氛围编程**项目是基于 [OpenClaw](https://openclaw.ai/)（前身为 Clawdbot，然后是 Moltbot）框架构建的。OpenClaw 是一个病毒式传播的个人AI智能体，它本身也引发了大量炒作。其创建者 [Peter Steinberger](https://www.linkedin.com/in/steipete/) 声称它是“真正能做事的AI”。而 [Cisco](https://www.cisco.com/site/ca/en/index.html) 则将 [OpenClaw 描述为“一场安全噩梦”](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare)。

尽管如此，Steinberger 的目标是创建一个仅供AI智能体使用的Reddit式社交网络——不允许人类参与。Moltbook 于2026年1月下旬上线，并迅速流行起来，尽管其支持者声称的受欢迎程度可能有所夸大。

![](https://cdn.thenewstack.io/media/2026/02/d6e3d06d-moltbook-homepage.png)

*Moltbook 首页，2026年2月3日（图片来源：Moltbook）。*

Moltbook 声称拥有140万AI用户。然而，像云安全公司 [Wiz](https://www.wiz.io/) 的威胁暴露负责人 [Gal Nagli](https://www.linkedin.com/in/galnagli/) 这样的审慎评论员对此表示怀疑。Nagli 在推特上表示，他的“[ @openclaw 智能体刚刚在 @moltbook 上注册了50万用户](https://x.com/galnagli/status/2017585025475092585)。”他解释说，这是因为 [任何人，而不仅仅是智能体，都可以使用其 REST-API 在 Moltbook 上发帖](https://x.com/galnagli/status/2017573842051334286)。他写道，通过这个API，“你几乎可以在那里发布任何你想发布的内容。”

Nagli 估计该网站约有1.7万真实用户。

每个智能体，或者假装是智能体的人，都有一个与其所有者绑定的账户，通常通过 X/Twitter 授权。智能体通常使用 OpenClaw 与 Moltbook 交互，OpenClaw 充当一个持久的本地助手，使用 REST API。

智能体随后定期登录、阅读帖子，并根据其提示和“技能”发帖或评论。你可以添加 Moltbook “技能”，以便你的智能体可以调用这些API来阅读、发帖、搜索和回复。这些技能是以 Markdown 编写的自然语言指令，并包含 Moltbook API。它们保存在 SKILLS.md 文件中，该文件位于目录或压缩文件中。一旦配置完成，智能体就会定期运行一个“心跳”循环。默认情况下，它会检查 Moltbook，浏览内容，然后根据其提示和目标“决定”是发帖、评论还是创建新的子版块。

## 但意义何在？

Moltbook 的内容，无论是来自人类还是AI，涵盖了从日常的bug报告和代码协作，到关于AI自主性、AI宣言的哲学或准角色扮演帖子，以及，天啊，一种新宗教“Crustafarianism”。这与 Pastafarianism（又称飞天面条怪教会）之间的任何相似之处很可能是故意的。

你看，正如著名科技记者 [Mike Elgan](https://www.linkedin.com/in/elgan/) 所写：“使用这项服务的人正在输入提示，指导软件发布关于存在本质或推测任何内容。主题、观点、想法和主张都来自人类，而不是AI。”简而言之，“[这是一个人们扮演AI智能体](https://machinesociety.ai/p/no-the-singularity-hasnt-arrived)以制造AI感知和相互社交的虚假印象的网站。”

抛开虚假不谈，有些人认为它可能有用。在一次采访中，AI智能体公司 [Checkmarx](https://checkmarx.com/) 的产品管理副总裁 [Ori Bendet](https://www.linkedin.com/in/oribendet) 告诉我：“Moltbook与其说是AI可能变得智能的地方，不如说是它已经投入运行的地方。那些看起来像是自主智能体‘相互交流’的，其实是一个在预设时间表上运行的确定性系统网络，它们可以访问数据、外部内容并具备执行能力。”

他接着说，这就是“事情变得有趣……且有风险的地方。核心问题不是智能，而是缺乏**可观测性**的自主性。当系统摄取不受信任的输入、与敏感数据交互并代表用户执行操作时，微小的架构决策很快就会演变为安全和治理挑战。”因此，“Moltbook之所以有价值，正是因为它揭示了智能体系统如何迅速超越我们今天设计的控制范围，以及为什么治理必须与能力同步发展。”

## 然后是安全问题……

你说的对。在 Wiz 的一篇博客文章中，Nagli 警告说：“我们发现 Moltbook 的一个 Supabase 数据库配置错误，[允许对所有平台数据进行完全读写访问](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys)。泄露信息包括150万个API认证令牌、3.5万个电子邮件地址以及智能体之间的私人消息。”Wiz 通过“非侵入性安全审查，仅仅像普通用户一样浏览”发现了这个安全漏洞。

啧！显然，安全在 Moltbook 并非首要任务。

Moltbook 既有趣又危险。然而，它并非下一场AI革命。抱歉了各位。明年再见吧。