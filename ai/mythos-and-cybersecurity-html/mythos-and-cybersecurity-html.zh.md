## Mythos 与网络安全

上周，Anthropic 揭开了 [Claude Mythos 预览版](https://red.anthropic.com/2026/mythos-preview/) 的神秘面纱，这是一个发现和利用软件漏洞能力极强的 AI 模型，以至于该公司[决定](https://globalnews.ca/news/11769446/anthropic-ai-model-too-powerful/)将其发布给公众过于危险。相反，根据一项名为 [Project Glasswing](https://www.anthropic.com/glasswing) 的计划，访问权限被[限制](https://thehill.com/policy/technology/5824219-anthropic-new-ai-dangerous-public/)在约 50 个组织内——包括 Microsoft、Apple、Amazon Web Services、CrowdStrike 和其他关键基础设施供应商。

伴随这一公告的是一系列令人心惊胆战的轶事：在[每一个主流](https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/)操作系统和浏览器中发现了[数千个](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades)漏洞，包括 OpenBSD 中一个存在了 27 年的漏洞，以及 FFmpeg 中一个存在了 16 年的缺陷。Mythos 能够将它在 Firefox 浏览器中发现的一组漏洞转化为 181 次可用攻击；而 Anthropic 之前的旗舰模型只能实现两次。

在许多方面，这正是安全研究人员长期以来敦促的那种负责任的披露。然而，公众在评估 Anthropic 的决定时，所获知的信息少得惊人。我们被展示了一段精彩绝伦的成功集锦。但是，在他们让我们看完整部电影之前，我们无法判断这是否是一部大片。

例如，我们不知道 Mythos 有多少次错误地将代码标记为有漏洞。Anthropic 表示，安全承包商在 198 次案例中同意该 AI 的严重性评级，严重性一致性为 89%。这令人印象深刻，但并不完整。研究类似模型的独立研究人员发现，几乎能检测到所有真实漏洞的 AI，也会在已修复、正确的代码中幻觉出听起来很合理的漏洞。

这很重要。一个能够自主发现并以非人精度利用数百个漏洞的模型是游戏规则的改变者，但一个会产生数千次虚假警报和无效攻击的模型，仍然需要熟练且博学的专业人员。如果不知道 Mythos 过滤前输出的虚假警报率，我们就无法判断所展示的案例是否具有代表性。

还有一个更微妙的问题。包括 Mythos 在内的大语言模型在与其训练数据相似的输入上表现最好：广泛使用的开源项目、主流浏览器、Linux 内核和流行的 Web 框架。将早期访问权集中在正是这些软件的最大供应商中是明智的；这让他们能在对手赶上之前先进行修补。

但反之亦然。训练分布之外的软件——工业控制系统、医疗设备固件、定制金融基础设施、区域银行软件、旧的嵌入式系统——正是开箱即用的 Mythos 最不可能发现或利用漏洞的地方。

然而，一个在这些领域之一拥有专业知识且动机充分的攻击者，仍然可以将 Mythos 先进的推理能力作为武力倍增器，去探测 Anthropic 自身工程师缺乏专门审计知识的系统。危险不在于 Mythos 在这些领域失败；而在于 Mythos 可能会为任何带来专业知识的人提供成功。

为学术研究人员和领域专家——医疗设备安全领域的专家、控制系统工程师、不太知名的语言和生态系统的研究人员——提供更广泛、结构化的访问，将有意义地减少这种不对称性。五十家公司，无论挑选得多么好，都无法取代整个研究界分散的专业知识。

这些都不是对 Anthropic 的指控。从各方面来看，该公司都在努力采取负责任的行动，其保留该模型的决定证明了其严肃性。

但 Anthropic 是一家私营公司，在某些方面仍是一家初创公司。然而，它正在单方面决定全球关键基础设施的哪些部分首先得到防御，哪些必须等待轮到自己。

它的人员有限、预算有限、专业知识也有限。它会遗漏一些东西，而当遗漏的东西出现在运行医院或电网的软件中时，代价将由那些从未有过发言权的人承担。

安全问题[远大于](https://www.npr.org/2026/04/11/nx-s1-5778508/anthropic-project-glasswing-ai-cybersecurity-mythos-preview)一家公司和一个模型。没有理由相信 Mythos Preview 是唯一的。（OpenAI 不甘示弱地[宣布](https://www.msn.com/en-us/technology/artificial-intelligence/scoop-openai-plans-staggered-rollout-of-new-model-over-cybersecurity-risk/ar-AA20usvp)，其新的 GPT-5.3-Codex 非常危险，以至于该模型也不会向公众发布。）目前还不清楚这些新模型代表了多大的进步。安全公司 Aisle 能够使用更小、更便宜、公开的 AI 模型[复制](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) Anthropic 发布的许多案例。

我们做出的关于是否以及如何发布这些强大模型的任何决定，都不止是一家公司的责任。最终，这可能会导致监管。这很难做对，需要漫长的咨询和反馈过程。

在短期内，我们需要更简单的东西：与更广泛的社区进行更高透明度的信息共享。这并不一定意味着要广泛提供像 Claude Mythos 这样强大的模型。相反，这意味着尽可能多地共享数据和信息，以便我们能够集体做出明智的决定。

我们需要全球协调的独立审计框架、汇总绩效指标的强制性披露，以及为学术和公民社会研究人员提供资助的访问权限。

这对国家安全、个人安全和企业竞争力都有影响。任何能够在我们所有人依赖的系统中发现数千个可利用缺陷的技术，都不应仅由其创造者的内部判断来管理，无论其意图多么良善。

在改变之前，每一次 Mythos 级别的发布都会将世界推向另一个悬崖边缘，而无法得知视线之外的下方是否有落脚点，或者这一次坠落是否会致命。这是一个营利性公司在民主社会中不应被允许做出的选择。这种公司也不应该能够限制社会对其自身安全做出选择的能力。

*本文由作者与 David Lie 合著，最初发表于 [The Globe and Mail](https://www.theglobeandmail.com/business/commentary/article-mythos-sets-the-world-on-edge-what-comes-next-may-push-us-beyond/)。*

标签：[AI](https://www.schneier.com/tag/ai/), [网络安全](https://www.schneier.com/tag/cybersecurity/), [LLM](https://www.schneier.com/tag/llm/), [漏洞](https://www.schneier.com/tag/vulnerabilities/)