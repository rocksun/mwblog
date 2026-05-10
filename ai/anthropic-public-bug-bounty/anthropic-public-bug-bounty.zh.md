漏洞赏金计划多年来一直是网络安全的基石，充当着黑客和安全研究人员在恶意行为者利用漏洞之前负责任地披露漏洞的渠道。

因此，Anthropic 正式推出其公开漏洞赏金计划也就不足为奇了。在之前运行了受到严格控制的安全测试计划后，该公司现在向更广泛的研究社区开放了其安全报告渠道。

然而，这一计划的发布恰好发生在 [Anthropic 发布 Claude Mythos 和 Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/) 一个月之后。后者是一项针对特定访问权限的网络安全倡议，围绕一个更先进的前沿模型展开，该公司声称该模型识别和串联软件漏洞的效果远超其目前的公开系统。

Anthropic 并没有广泛发布 Mythos，而是将其访问权限限制在一小部分安全和基础设施合作伙伴中——包括 Amazon、Microsoft、Cisco、CrowdStrike 和 Linux Foundation——并将该项目定位于在更强大的攻击性 AI 工具普及之前，加强防御性网络安全能力。

然而，Anthropic 同时决定扩大公众主导的人类漏洞研究，这在无形中削弱了围绕 Mythos 本身的一些广泛宣传——毕竟，该公司曾竭尽全力强调 Mythos 危险的网络安全能力。

> 新的漏洞赏金计划是一种默认：传统的安全研究——由外部人类研究人员而非仅由前沿模型进行——在发现和修复现实世界的漏洞方面仍然核心地位。

在 Anthropic 的案例中，部分安全社区对验证该公司关于 Mythos 漏洞发现能力和现实世界影响的一些广泛说法表示怀疑。

尽管如此，如果 Mythos 真的代表了 AI 驱动的网络安全的未来，Anthropic 同时启动一个非常传统的、以人为动力的漏洞赏金计划的决定，无疑为这一叙事引入了明显的张力。

## 为 Claude 众包安全

[托管在 HackerOne 上](https://hackerone.com/anthropic/?type=team)，新的漏洞赏金计划允许外部研究人员报告 Anthropic 开发的软件和系统中的漏洞，奖励根据通用漏洞评分系统 ([CVSS](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System)) 确定。CVSS 是一个按严重程度对软件安全缺陷进行排名的行业标准框架。

事实上，这一举措标志着 Anthropic 早期漏洞披露工作的演进。2024 年 8 月，该公司[启动了一个更常规的](https://hackerone.com/anthropic-vdp/policy_versions?change=3737764&type=team)漏洞披露计划 (VDP)，主要作为安全发现的报告和分流渠道。该早期的 VDP 页面现在会将研究人员重定向到新的漏洞赏金计划，Anthropic 指出未来的报告应通过更新后的系统提交。

新计划涵盖了 Anthropic 拥有的广泛资产，包括 Claude.ai、Anthropic API、Claude Code、官方桌面和移动客户端、内部基础设施、SDK 以及 Anthropic 开发的 MCP 集成和 Chrome 扩展。某些类别仍被排除在外，包括影响第三方 MCP 服务器的漏洞、归档的开源存储库、社会工程攻击以及低严重性的信息性发现。

值得注意的是，Anthropic 还将 Claude Code 纳入了涉及未经授权的命令执行、隐形工具使用和权限绕过的关键漏洞范围——这些风险在自主编码代理的兴起中正变得日益重要。

这远非 Anthropic 首次邀请外部研究人员探测其 AI 系统的安全边界。除了 2024 年的公开 VDP 之外，[该公司还推出](https://www.anthropic.com/news/model-safety-bug-bounty)了一个仅限邀请的“模型安全”赏金计划，以发现通用越狱方法和绕过 Claude 防护措施的方法。Anthropic [随后扩展了这些努力](https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program)，通过第二个 HackerOne 倡议，旨在针对与化学、生物、放射性和核 (CBRN) 滥用场景相关的提示词，对其次构性分类器 (Constitutional Classifiers) 进行压力测试。

早期的这些计划更多侧重于探测前沿 AI 系统本身的行为和安全边界。

Anthropic 周四[在 X 上宣布新计划](https://x.com/AnthropicAI/status/2052466175540629965)时表示，在正式发布之前，它已经对该倡议进行了一段时间的测试。

“我们已经在安全研究社区内私下运行了该计划，他们的发现加强了我们的产品，”该公司写道。“现在任何人都可以报告漏洞并获得奖励。”

## 对 Mythos 的怀疑与日俱增

在该计划发布后，似乎并非所有人都被 Anthropic 关于 Mythos 的宏大叙事所说服。

社交媒体上的一些用户公开质疑 Anthropic 关于先进 AI 驱动漏洞发现的说法与同时启动非常传统的人类主导漏洞赏金计划之间的矛盾。“*所以，Mythos 是一个神话 (myth)*，”一位用户[写道](https://x.com/glinsec_com/status/2052617943410753941)，而另一位[问道](https://x.com/quantumaidev/status/2052466625044263213)：“*我以为你们已经让 Mythos 在做所有这些事情了？*”

虽然随机在线评论者的反应很难被视为权威的安全分析，但这些言论仍然触及了围绕 Mythos 建立起来的更广泛的怀疑潜流。

## 基准透明度遭到抨击

在 Mythos 向世界展示后不久，AI Now Institute 的首席 AI 科学家 [Heidy Khlaaf](https://www.linkedin.com/in/heidy-khlaaf/) [公开质疑](https://x.com/HeidyKhlaaf/status/2041591737563394442?s=20)了 Anthropic 推出 Mythos 的几个方面，特别是在基准测试透明度和评估方法论方面。

Khlaaf 认为，Anthropic 没有披露与企业和关键基础设施环境中已广泛使用的成熟静态分析和安全工具的充分比较。她还指出缺乏详细的误报指标，许多安全研究人员认为这是评估漏洞发现工具在实践中是否真正有用的最重要指标之一。

她进一步质疑，Mythos 表面上的成功在多大程度上仍依赖于幕后大量人类专家的验证。

“这并不是说 AI 工具不能增强安全工程，”Khlaaf [写道](https://x.com/HeidyKhlaaf/status/2041591751891177486?s=20)。“它可以，但那些试图使现有工具和工程师过时的说法是不诚实的。”

安全咨询公司 [FlyingPenguin](https://www.flyingpenguin.com/) 的总裁 [David Ottenheimer](https://www.flyingpenguin.com/about/) 在[另一份分析](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/)中提出了类似的担忧，认为 Anthropic 的 Mythos 叙事模糊了漏洞发现、可利用性、基准测试和现实世界安全影响之间的重要区别。

Ottenheimer 还批评了他所描述的围绕 Project Glasswing 和 Mythos 的封闭验证循环，即 Anthropic 的技术文档和发布材料在很大程度上互为引用，而没有来自外部合作伙伴的大量独立验证。

> “这个安全故事全是营销，基本上没有证据。”

“这个安全故事全是营销，基本上没有证据，”Ottenheimer 写道。

Ottenheimer 还指出，AI 安全初创公司 [AISLE 的一份报告](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)发现，小型、廉价的开源权重模型可以复制 Mythos 大部分旗舰级的漏洞分析——其中一个模型只有 36 亿个活动参数，每百万个 token 的成本仅为 0.11 美元。

## 人类研究人员依然必不可少

另一方面，有证据表明 Mythos 的能力可能超出了营销炒作。英国 AI 安全研究所 (ASI) [发布了一份评估](https://thenewstack.io/claude-mythos-preview-simulation/)，显示 Claude Mythos Preview 模型可以自主完成多阶段网络攻击模拟，并能以之前前沿模型难以企及的成功率解决专家级的夺旗赛 (CTF) 挑战。

在一次受控评估中，ASI 表示 Mythos 成为第一个成功完成 32 步模拟企业网络接管（从侦察到利用再到横向移动）的模型。在 10 次尝试中，该模型平均完成了 32 个所需步骤中的 22 个，表现明显优于 Anthropic 之前的旗舰系统。

与此同时，ASI 也警告不要过度解读这些结果，并指出测试发生在受控环境中，没有在经过加固的企业网络中发现的许多防御措施、主动监控系统和现实世界的约束。

“我们不能肯定 Mythos Preview 是否能够攻击防御良好的系统，”该研究所写道。

无论人们选择如何解读 Mythos 和 Project Glasswing，Anthropic 在 HackerOne 上的新举措或许揭示了神话之下更接地气的一面：即使在 AI 网络系统能力日益增强的时代，该公司仍然认为让普通人类研究人员用老方法去寻找其产品的漏洞具有价值。