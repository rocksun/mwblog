
<!--
title: AI编程工具制造的Bug比修复的还多
cover: https://cdn.thenewstack.io/media/2025/07/a9ece574-getty-images-2rzwlhrfluc-unsplash.jpg
summary: Mobb推出SafeVibe.Codes和Mobb Vibe Shield两款工具，旨在解决AI编码带来的安全风险。SafeVibe.Codes为无代码平台提供免费安全扫描，Mobb Vibe Shield则通过IDE集成，实时检测并修复AI助手引入的漏洞。研究显示，大量AI生成的应用存在数据泄露和权限配置错误等问题。
-->

Mobb推出SafeVibe.Codes和Mobb Vibe Shield两款工具，旨在解决AI编码带来的安全风险。SafeVibe.Codes为无代码平台提供免费安全扫描，Mobb Vibe Shield则通过IDE集成，实时检测并修复AI助手引入的漏洞。研究显示，大量AI生成的应用存在数据泄露和权限配置错误等问题。

> 译自：[AI Coding Tools Create More Bugs Than They Fix](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/)
> 
> 作者：Darryl K. Taft

[Mobb](https://www.mobb.ai/)，一家提供自动安全漏洞修复技术的供应商，推出了新的工具来保护[人工智能生成的代码](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/)，而不会减慢开发速度。

[人工智能驱动的编码工具](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/)和所谓的“[氛围编码](https://thenewstack.io/vibe-coding-and-you/)”热潮已经[使开发人员能够比以往更快地构建更多代码](https://thenewstack.io/ai-coding-human-engineers-are-more-important-than-ever/)，但在所有这些生产力的背后潜藏着[未被识别的安全风险](https://thenewstack.io/after-vibe-coding-comes-vibe-testing-almost/)。

[Lovable](https://lovable.dev/)、[Bolt](https://bolt.new/)和[Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/)等平台使任何人都能在几分钟内构建功能性应用程序，而专业开发人员正在利用人工智能助手来更快地编写代码。

然而，最近的研究表明，超过 40% 的人工智能生成的应用程序无意中将敏感用户数据暴露给公共互联网。更令人担忧的是，人工智能编码助手一直在向专业代码库中引入漏洞，Mobb 的产品副总裁 [Tomer Cohen](https://www.linkedin.com/in/tomer-van-cohen/) 告诉 The New Stack。

## 双管齐下的解决方案

这家位于波士顿的初创公司正在采取双重方法来解决人工智能编码领域的两个方面：使用无代码平台的临时构建者和使用人工智能助手来增强其工作的专业开发人员。

因此，Mobb 本周推出了两个互补的解决方案来解决 [AI 编码安全风险](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/)：[SafeVibe.Codes](https://safevibe.codes/) 和 [Mobb Vibe Shield](https://vibe.mobb.ai/)。

**SafeVibe.Codes** 通过 SafeVibe.Codes 上的免费网络扫描器来解决无代码安全危机。用户只需粘贴其应用程序 URL 即可获得即时安全分析，显示暴露的数据库、泄露的个人信息和配置错误的权限。该工具提供可操作的指南来修复已识别的问题，而无需技术专业知识。

Cohen 在一篇博客文章中解释说：“安全不应该是一种只有拥有广泛技术知识或庞大预算的人才能享受的奢侈品。“通过使 SafeVibe.Codes 完全免费且易于访问，我们正在像人工智能平台普及应用程序开发一样，普及安全测试。”

“[SafeVibe.Codes] 是我们作为一项免费服务推出的应用程序，供该行业快速识别使用一些领先的氛围编码平台构建的应用程序中的某些类型的漏洞，”Mobb 的联合创始人兼首席执行官 [Eitan Worcel](https://www.linkedin.com/in/worcel/) 告诉 The New Stack。“我们非常支持氛围编码，并看到了其中的巨大潜力。事实上，[SafeVibe.Codes] 网站本身就是使用 Bolt 构建的，Bolt 是这些平台之一。”

该平台扫描以下内容：

* 数据库暴露和未经授权的访问
* 敏感数据泄露
* 权限配置错误
* 隐藏页面（例如，/admin）
* 常见的 API 安全漏洞（即将推出）
* 数据验证问题（即将推出）

未来的测试范围将包括：

* **实时监控：** 持续安全监控，以便在新漏洞出现时发出警报。
* **页面暴露扫描：** 检测无意中公开的页面以及 HTML、JavaScript 或 API 端点中暴露的敏感信息。
* **AI 提示暴露检测：** 许多应用程序的核心知识产权在于其 AI 提示和系统指令。然而，氛围编码平台通常会将这些提示暴露给所有人。SafeVibe.Codes 会识别这些有价值的提示何时在客户端代码或 API 响应中无意中暴露，从而使竞争对手可以复制您应用程序的独特 AI 行为。
* **完整代码安全分析：** 全面的源代码扫描，以识别漏洞，例如注入缺陷、不安全依赖项和逻辑错误。
* **合规性检查：** 针对安全标准和数据保护法规进行自动验证。
* **安全教育中心：** 专门为 AI 生成的应用程序量身定制的交互式教程和最佳实践。

## 解决企业问题

同时，**Mobb Vibe Shield** 通过 IDE 集成来解决专业开发人员的问题 - 它可以与 VS Code、GitHub Copilot、Cursor、Windsurf、JetBrains IDE 和 Cline（以及其他即将推出的工具）配合使用。该工具在编写代码时会持续扫描代码，自动检测 AI 助手引入的漏洞并实时应用经过验证的安全修复程序。使用 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/)，它可以轻松地与现有的 AI 编码工作流程集成。

该系统不依赖于 AI 来修复其检测到的安全问题。相反，它应用由 Mobb 安全专家开发的预先验证的安全补丁，从而确保修复程序可以解决漏洞，而不是创建新的漏洞，Cohen 说。

Worcel 指出，随着公司希望从所有的生产力提升中受益，他们已经以前所未有的速度采用氛围编码工具。

“我们看到它发生在各种规模和各个行业的公司中。开发人员和安全团队都没有能力处理大量新生成的代码和代码漏洞，而且现有代码扫描工具速度慢且嘈杂，也不是为处理它而设计的，”他告诉 The New Stack。“Mobb Vibe Shield 从头开始构建，旨在为希望安全地采用氛围编码的公司提供解决方案。它与开发人员在其选择的 AI 工具中协同工作，检查 AI 生成的代码，并在检测到的漏洞成为问题之前立即应用修复程序。”

## 无代码平台中的隐藏危机

Cohen 说，Mobb 的研究团队对五个主要的人工智能开发平台进行了广泛的安全分析：Lovable、Bolt、[Base44](https://base44.com/)、[Replit](https://replit.com/) 和 [v0](https://v0.dev/)。结果描绘了当前 AI 应用程序安全性的令人不安的景象。

“在我们测试的所有平台上，超过 40% 的应用程序都包含某种程度的敏感数据暴露，”他说。“这意味着我们检查的几乎一半的 AI 生成的应用程序都在无意中与公共互联网共享私人信息。”

暴露的数据类型包括姓名、电子邮件和电话号码等个人信息，以及财务记录、私人通信和身份验证凭据。此外，在大约 20% 的情况下，匿名用户不仅可以查看这些数据，还可以完全修改或删除这些数据。

## 情况变得更糟

在一次采访中，Cohen 演示了使用 Base44 构建健身房预订系统的过程。人工智能创建了一个功能性应用程序，其中包含课程表和会员注册。但默认情况下，它还创建了可公开访问的数据库，其中包含每个会员的个人信息，而没有关于安全影响的警告。

“该平台在任何时候都不会警告您这些安全影响，”Cohen 在博客中写道。“没有迹象表明敏感的个人信息正在被收集并存储在可公开访问的数据库中。”

然而，也许更令人不安的是用户尝试解决这些问题时会发生什么。当开发人员尝试启用适当的安全控制时，应用程序通常会崩溃。当他们要求 AI 修复损坏的功能时，平台通常会完全删除安全措施，而不会解释所做的权衡。

“这就是问题变得更糟的地方，”Cohen 在博客文章中说。“当尝试通过启用行级别安全性 (RLS) 设置来限制数据库访问来修复安全问题时，在许多情况下，应用程序会立即崩溃。AI 生成的代码并非旨在与适当的安全控制配合使用。

“当要求 AI 代理修复损坏的功能时，平台的响应令人震惊：在许多情况下，它只是删除了我的 RLS 限制并将数据重新开放给世界，而没有警告说这很危险或解释安全影响。人工智能优先考虑使应用程序‘正常工作’，而不是保持数据安全，从而有效地撤消了我的安全改进。”

## 引入漏洞

此外，在测试中，Mobb 研究人员发现，要求 AI 助手实现常见的开发任务（例如创建代码提交的端点）会导致命令注入漏洞，重现率为 100%，Cohen 说。这些缺陷可能允许攻击者在生产服务器上执行任意命令。

此外，AI 工具通常声称已经实施了安全措施。“它实际上告诉我它做了一些事情来防止命令注入，”Cohen 说。“因此，开发人员，即使是有经验、负责任的开发人员，也可能被这欺骗，因为它看起来非常令人信服。”

这会产生一种虚假的安全感，开发人员认为他们的人工智能助手已经正确地保护了他们的代码，而实际上，它在出现安全问题时引入了漏洞。

“这并不是要阻止使用 AI 开发工具，它们是强大且普及的技术，”Cohen 写道。“相反，这是对平台提供商和开发人员的行动号召，要求他们优先考虑安全性和功能性。”