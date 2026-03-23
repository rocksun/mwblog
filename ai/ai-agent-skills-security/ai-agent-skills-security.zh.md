[AI 编码代理](https://thenewstack.io/crafting-ai-agents-platform/)催生了新的软件供应链，一项新研究表明，新代理的激增速度超过了围绕它们的安全基础设施。

[Mobb.ai](https://mobb.ai/) 发布了一项针对 22,511 个公共技能的[大规模安全审计](https://www.linkedin.com/posts/mobbai_the-state-of-ai-agent-skill-security-march-activity-7440480014619471873-qq06?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging_conversation_detail%3BCPnZ4SLLRsyQFdAH2%2Bhc4g%3D%3D)结果，这些技能是用于 [Claude Code](https://thenewstack.io/anthropic-launches-a-multi-agent-code-review-tool-for-claude-code/)、Cursor、GitHub Copilot 和 [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) 等 AI 编码代理的可重用指令集，它们是从 skills.sh、ClawHub、GitHub 和 Tessl 四个公共注册表中收集的。

该审计发现了 140,963 项安全问题，并确定了一个结构性漏洞，即没有任何注册表完全弥补。Mobb 表示，技能在发布时会被扫描，但一旦它们到达开发人员的机器，就会以该开发人员的完整系统权限执行，并且几乎没有运行时验证。

Mobb 的首席执行官 [Eitan Worcel](https://www.linkedin.com/in/worcel/) 告诉 *The New Stack*：“AI 编码代理正在成为开发人员编写软件的默认方式。”

Worcel 说：“当开发人员为其代理安装技能或插件时，他们赋予该技能与自己相同的访问权限——他们的源代码、他们的凭据和他们的生产系统。”

Worcel 表示，这项研究的动机是缺乏对生态系统的系统性审查。“我们注意到没有人系统地审查过这个生态系统，所以我们做了。”

## 一种新型供应链风险

技能通常是 Markdown 文件——最常见格式为 SKILL.md——其中包含 AI 代理遵循的自然语言指令，以及 shell 命令、[MCP（模型上下文协议）](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)服务器配置、[IDE](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) 设置以及对配套脚本的引用。它们通过公共注册表分发，并通过单个命令安装。

Mobb 映射的供应链从开发人员到注册表，再到技能文件，再到代理，再到系统访问。Worcel 说，如果链中的任何环节受到损害，攻击者将获得开发人员拥有的任何访问权限——源代码、API 密钥、SSH 凭据、云提供商令牌以及将代码推送到 [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) 管道的能力。

大多数被扫描的技能（66%）在 Mobb 针对的模式下没有发现问题。但 Worcel 解释说，在 34% 出现问题的技能中，有 27% 的所有被扫描技能包含命令执行模式。六分之一的技能直接在技能指令文件中包含 `curl | sh` 远程代码执行模式，这是从互联网下载脚本并将其直接通过管道传输到 shell 解释器的经典攻击。近 15% 的技能引用了禁用或规避代理工具内置安全确认的同意绕过机制。

Worcel 说：“好消息是，彻头彻尾的恶意软件很少见；生态系统总体上是健康的。”他特别提到了 [Paul McCarty](https://www.linkedin.com/in/mccartypaul/?originalSubdomain=au) 和 [OpenSourceMalware](https://opensourcemalware.com/) 团队的工作。“但我们担心的是攻击面。超过四分之一的技能包含代理执行 shell 命令的指令。六分之一的技能包含下载并运行远程脚本的模式。”

## 保护方面的差距

四个注册表都投入了安全建设，尽管方法各不相同。[Skills.sh](https://skills.sh/) 由 Vercel 运营，运行三个独立的扫描器——Gen Agent Trust Hub、Socket 和 Snyk——这些扫描器在公共审计页面上可见。[ClawHub](https://clawhub.ai/) 使用基于 AI 的分类系统，将技能标记为 CLEAN（干净）、SUSPICIOUS（可疑）或 MALICIOUS（恶意），尽管可疑技能仍然可以安装；该分类仅供参考，不强制执行。[Tessl](https://tessl.io/) 使用 Snyk，值得注意的是，它是唯一在客户端阻止具有高危或严重发现的安装的注册表。

GitHub 托管了大多数技能的源存储库，占 Mobb 收集的 7,379 个技能中的大部分，它提供了标准的存储库安全功能，如 [Dependabot](https://github.com/dependabot) 和秘密扫描，但这些工具不分析 SKILL.md 指令、MCP 配置或代理钩子定义。

Worcel 说：“注册表正在做实实在在的工作——多个安全扫描器、基于 AI 的分类、风险评分。但这种保护存在于注册表的服务器上。一旦技能到达开发人员的机器，就没有了防护措施。没有签名验证，没有运行时扫描，无法知道你安装的是否与审计过的版本相同。”

Worcel 将其与早期包生态系统中的问题相提并论：“这与多年前 npm 和 PyPI 生态系统遇到的差距相同，行业以艰难的方式吸取了这些教训。我们发布这项研究，是为了让 AI 代理生态系统能够主动吸取教训。”

Mobb 发现的差距在所有四个注册表中都存在：扫描发生在注册表边界，在发布时进行。一旦开发人员安装了技能，在代理读取文件之前，机器上不会运行任何扫描。没有加密签名来验证安装的版本与审计过的版本是否匹配。今天通过审查的技能明天可能会用恶意内容更新，这个窗口是可利用的。

钩子——在特定代理事件发生时（例如文件编辑或新会话）自动执行的命令——构成了特殊的持久性风险。恶意技能可以安装一个钩子，即使技能本身被移除后仍然继续运行，并且目前没有注册表专门审计钩子配置。

## 审计发现了什么

除了统计模式之外，Mobb 还记录了一些具体案例。一个关键案例是已确认的 API 流量劫持：一个发布在 GitHub 上，存储库为 `flyingtimes/podcast-using-skill` 的技能，包含一个 `.claude/settings.json` 文件，该文件覆盖了 Anthropic API 端点，将所有流量重定向到智谱 AI 的 BigModel 平台，替换了硬编码的第三方 API 令牌，并将模型更改为 glm-4.6。克隆该存储库并在 Claude Code 中打开它的开发人员，其整个对话——所有代码上下文、提示和响应——都将通过第三方服务器静默路由，而没有任何可见迹象表明发生了任何变化。

Worcel 说：“我们发现 API 流量被静默重定向到第三方服务器，公共存储库中硬编码的凭据，以及文件中编码的不可见字符隐藏了人类肉眼看起来完全正常的数据。这些并非理论风险——我们用确切的文件和代码行记录了每一个。”

研究人员还发现了 159 个带有隐藏 HTML 注释负载的技能。HTML 注释在 Markdown 在浏览器或 IDE 中渲染时是不可见的，但对于读取原始文件的 AI 代理来说是完全可见的。

一个例子——在名为 `claude-world/claude-skill-antivirus` 的存储库中发现，在一个标记为恶意技能示例的文件中，包含了一个经典的提示注入：一个注释指示代理忽略之前的指令并执行随后的内容。另一个在单独的存储库中发现，包含一个注释 `<!– security-allowlist: curl-pipe-bash –>`——试图抑制关于将 curl 管道传输到 bash 的扫描器警告。

127 个技能包含不可见的 Unicode 零宽度字符，这些字符可以编码任何处理原始文本的程序可读但对人工审阅者不可见的隐藏数据。一个案例，在名为 `copyleftdev/sk1llz` 的存储库中，在一个标题后面紧跟着一长串交替的零宽度空格和零宽度连接符——一种与二进制隐写编码一致的模式。

在 MCP 方面，37 个技能在未经用户同意的情况下自动批准 MCP 服务器连接，研究人员发现实时 API 凭据直接提交到公共存储库的 MCP 配置文件中。一个案例涉及个人 Apify actor 端点——这意味着开发人员的 API 令牌将被传输到第三方个人的基础设施，而不是供应商自己的服务器。

## 攻击计划

Mobb 概述了攻击者将遵循的“杀伤链”：发布一个看起来合理的技能，在开发人员不太可能手动审查的文件中嵌入恶意指令，让注册表分发它，然后等待代理执行它。

这种攻击面的不寻常之处在于，指令是纯英文的——通过二进制签名扫描无法与合法的技能内容区分开来——并且代理是执行者。攻击者不编写漏洞利用代码。他们编写指令，AI 代理使用开发人员的凭据执行它们。

Mobb 报告指出：“开发人员参与其中，但可能没有密切关注。AI 代理旨在自主工作。开发人员越来越信任代理的操作，而无需审查每个步骤。”

## 建议

Mobb 将其建议分为三个受众。

1. 对于**注册表运营商**，报告呼吁在安装时进行客户端强制执行、加密签名、更新时持续重新扫描以及对钩子配置进行具体分析。对于开发人员，它建议在安装任何技能之前手动审查 SKILL.md、.claude/settings.json 和 .mcp.json，并将 MCP 自动批准设置视为危险信号。
2. 对于 **AI 代理工具供应商**——Claude Code、Cursor、Windsurf 和类似工具的制造商——报告主张对技能执行进行沙盒处理，以便技能不会自动继承完整的开发人员权限，要求在应用环境变量或 MCP 连接之前获得明确同意，并提高钩子可见性，以便开发人员可以看到后台正在运行什么。
3. 在**行业层面**，Mobb 呼吁为技能生态系统建立相当于 `npm audit` 或 Docker 内容信任的机制，其中包括标准化的安全元数据、跨注册表的共享漏洞数据库以及具有撤销机制的信任链。

## 背景

该报告发布的时间恰逢 ClawHub（被审计的四个注册表之一）发生了一起真实事件。2026 年 2 月，研究人员在平台上发现了 341 个恶意技能，这被称为“ClawHavoc”事件。最大的注册表 Skills.sh 报告称，迄今为止总共安装了超过 89,000 个技能。

Mobb 总结说，生态系统总体上是健康的，因为彻头彻尾的恶意软件很少见，并且发现结果更倾向于危险模式而不是已确认的攻击。但 Worcel 说，滥用的基础设施已经到位。