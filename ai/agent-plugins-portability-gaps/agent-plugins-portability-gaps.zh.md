**本月初**，Vercel 发布了 [Agent Plugins 1.0.0](https://agent-plugins.org/specification)，核心维护者来自 AWS、Cursor、Microsoft 和 OpenAI。同一天，[Google 宣布](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/)加入该行列。这一格式解决了开发者真正头疼的问题：一个原本可以独立运行的技能（Skill）和一个 MCP 服务器，在发布到第二个客户端时，往往不得不进行分叉（fork）并分别维护。

尽管这六家公司就组件的存放位置达成了一致，但对于组件的具体行为尚未实现标准化。规范的 7.1 节将技能格式交给了 [Agent Skills 规范](https://agentskills.io/specification)，7.2 节将通信行为和生命周期交给了 [MCP](https://modelcontextprotocol.io/specification)。这两者均源自 Anthropic，虽已公开发布，但 Anthropic 并未进入该项目的指导委员会。

项目方对此表现得很坦诚。其文档将这一成果称为一个微小的互操作性底线，Google 的博文也将 v1 版本仅描述为一种包格式。明显的差异并不在于宣传辞令与技术事实之间，而在于像“兼容”、“可移植”和“插件”这样的术语，在日常使用中暗示的含义远超这一狭窄协议所实际提供的范畴。

## Anthropic 发布了什么，以及向谁发布

2025 年 12 月 9 日，Anthropic 将 MCP 捐赠给了由 Linux 基金会领导的 Agentic AI Foundation。九天后，Agent Skills 作为一种开放标准发布，目前在 [agentskills.io](https://agentskills.io/) 上进行公开开发。两者的治理模式不同：MCP 归属一个独立的基金会，而 Agent Skills 是一个开放开发的规范，缺乏类似的法律监管者。

Agent Plugins 项目对这两项标准均缺乏权威。这一细节决定了该生态系统中每一个后续的发展。

Agent Plugins 技术指导委员会成员包括：亚马逊的 Clare Liguori、Cursor 的 Roshan Sadanani、微软的 Harald Kirschner、OpenAI 的 Gav Verma，以及担任核心维护者负责人的 Vercel 的 Jonathan Hefner。[技术章程](https://github.com/agentplugins/agent-plugins-spec/blob/main/GOVERNANCE.md)措辞谨慎，指出治理角色由个人而非组织担任，不为特定公司预留席位，且没有任何单一供应商可以控制多数核心维护者席位。

Google 的文章称其“正以核心维护者身份加入该组织，由 Kevin Hou 代表”。截至本文撰写之时，章程中指定的记录名册 [MAINTAINERS 文件](https://github.com/agentplugins/agent-plugins-spec/blob/main/MAINTAINERS.md) 仍只列出了五人，未包含 Google。加入流程正在进行中而非完成，如果你在关注谁拥有投票权，该文件是值得关注的对象。

没有任何一手资料解释 Anthropic 的缺席，所以我不会凭空猜测。

## 规范只管位置，不管行为

一个插件就是一个在根目录下包含 plugin.json 文件的目录。技能存放在 skills/ 中，每个技能一个子目录。MCP 服务器存放在 mcp.json 中。这些位置是固定的，清单文件不允许移动它们或内联声明组件，这消除了原本每个客户端都会独立发明一套发现机制和优先级规则的可能。

```
reports-plugin/
├── plugin.json          # Agent Plugins 管理此文件
├── skills/
│   └── summarize/
│       └── SKILL.md     # Agent Skills 管理此文件
├── mcp.json             # Agent Plugins 管理配置结构
└── com.vendor.client/   # 无人管理此目录

```

清单文件仅要求两个字段：`$schema` 和 `name`。其余均为可选元数据。

```
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "reports-plugin"
}

```

关于组件本身，规范明确表示由他人定义。第 7.1 节明确指出 Agent Skills 规范是“SKILL.md 格式、frontmatter 字段和目录布局的事实来源”，而 Agent Plugins 仅管理如何在插件内发现技能。第 7.2 节对 MCP 做了同样的处理。

没有什么强迫必须这样做。规范完全可以通过定义配置档、强制要求子集或禁止可选功能来约束其他规范的实现。但 Agent Plugins 选择了拒绝。因为它将 Agent Skills 和 MCP 视为单独管理的合同，所以它主要标准化了地址，避免了在它们之上叠加行为要求。

## 这就是为什么“兼容”是一个范围，而不是一种状态

第 11.1 节列出了兼容客户端的最低要求，最后一点需要强调。客户端必须至少支持一种组件类型：技能或 MCP 服务器。第 11.2 节阐明了后果：仅支持技能的客户端无需支持 MCP 即可达成兼容。

传输支持也采取了类似方法。支持 MCP 的客户端必须至少实现 stdio 或 Streamable HTTP 中的一种，并应支持两者，而传统的 HTTP+SSE 保持可选。第 7.2.2 节要求客户端跳过其未实现传输方式的服务器条目，并继续加载其他内容。

将这些组合起来，合规声明所代表的含义范围就变得非常广泛。

| 客户端 | 技能 | MCP | stdio | Streamable HTTP | 合规 |
| --- | --- | --- | --- | --- | --- |
| A | 是 | 否 | n/a | n/a | 是 |
| B | 否 | 是 | 是 | 否 | 是 |
| C | 是 | 是 | 否 | 是 | 是 |

客户端 A 和客户端 B 没有共同点，但两者都通过了合规认证。一个包含技能和捆绑 stdio 服务器的插件在两者上都无法完整运行，因为 A 只加载技能，B 只加载服务器，而在每种情况下，客户端的行为都完全符合规范要求。

公平地说，目前并不存在这样的客户端。[兼容客户端页面](https://agent-plugins.org/compatible-clients) 列出了 VS Code、Cursor、GitHub Copilot、ChatGPT、Codex、Kiro、Hermes Agent、OpenClaw 和 Grok Bot，它们都支持 Agent Skills 和 MCP，并逐项列出了传输方式。这份名单也已远远超过了发布周时的六家，这是一个真正的采用信号。

虽然其脆弱性比矩阵暗示的更具体，但这仍然是一个值得注意的细节。仅仅宣称符合 Agent Plugins 标准并不能预测互操作性。能预测互操作性的是每个客户端的能力矩阵，而该矩阵是文档，本身并非合规声明的一部分。没有任何东西能阻止未来的客户端发布规范所允许的“仅技能”配置，并以与当前八个客户端完全相同的方式进行自我描述。

## 那个与自身架构相矛盾的清单规则

大多数解释性报道对 plugin.json 的描述如出一辙：架构是封闭的，任何多余的顶层字段都会使清单无效。从 package.json 复制一个字段，插件就会崩溃。

规范却另有说法。第 5.2 节列出了 10 个允许的顶层字段，并继续说明如果清单包含任何其他顶层字段，“客户端必须报告并忽略每个未知字段，并且如果清单在其他方面满足本节要求，则必须继续加载插件。” 未知顶层字段在设计上是非致命的。任何其他架构违规都是致命的。

再看看 [已发布的架构](https://github.com/agentplugins/agent-plugins-spec/blob/main/schemas/1.0.0/plugin.schema.json)，它在顶层设置了 “additionalProperties”: false。如果使用标准的 JSON Schema 验证器运行一个带有额外字段的清单，它会失败。但将同样的清单交给合规的客户端，它却必须能够加载。

第 5.2 节预见到了这一点，称当规范文本与架构冲突时，以规范文本为准。虽然这可以作为裁决依据，但也意味着机器可读的工件与规范性文本在处理一个必然会反复出现的问题上存在分歧，而机器可读工件正是你的 CI 系统会调用的东西。如果你正在编写一个插件检查工具（linter），千万不要仅仅从架构文件生成它。

## 两个都叫 plugin.json 的文件

Claude Code 已经使用 .claude-plugin/plugin.json 作为其插件系统。Agent Plugins 则在包根目录使用 plugin.json。文件名相同，位置不同，架构不同，两者毫无关系。

这确实造成了困惑。编辑器中的搜索结果显示了两个完全相同的文件名。文档中提到的“插件清单”并未具体说明是哪一个。除非迁移指南每次都给出完整路径，否则它就是含糊不清的。

澄清 Anthropic 缺席的含义及其不包含的含义非常重要。Claude Code 并不是该格式的首发客户端，但 npx plugins add CLI 将其列为支持的安装目标，并将便携式包转换为 Claude 的原生插件系统。准确的表述应该是插件通过 CLI 安装到 Claude Code 中，而不是 Claude Code 实现了 Agent Plugins。那个转换步骤正是行为可能产生偏差的地方，而规范中没有任何内容对此进行管理。

## 客户端命名空间是如何夺回可移植性的

第 8 节定义了客户端扩展，这是为便携核心之外的任何内容准备的反向域名命名空间。客户端可以在 extensions[“com.vendor.client”] 下声明清单数据，或者使用顶层 com.vendor.client/ 目录，或两者并用。

看看规范将什么分配给了该命名空间：“Agent Plugins 不为客户端扩展数据或文件分配任何可移植的发现、验证、加载或失败语义。每个客户端定义其自身命名空间的内容和行为。”

命令、钩子、代理、规则和 LSP 服务器都存在于 v1 之外，理由是它们的格式尚未统一。每一个都是开发者实际为之构建插件的功能。当 [EmpirioLabs 的 Adam Dalloul 警告称](https://thenewstack.io/agent-plugins-open-standard/)，有用的行为最终落入供应商命名空间，会导致标准在纸面上开放，而碎片化却转移到了其他地方时，他描述的就是第 8 节记录的这种“逃生舱”。

这是否重要，取决于你的插件价值中有多少是在钩子中实现的。如果绝大部分都在这里，那么便携部分仅仅是一个外壳，而你试图避免的分叉依然存在，只是换了一个目录名。

## 你的插件是便携的，直到它需要密码或二进制文件

两个较小的发现将耗费开发者的宝贵时间。

第 7.2.1 节指出，标头值是“可见的包数据，而非便携的秘密机制”，插件不得在标头或环境变量中嵌入凭据，并且 v1 未定义任何 OAuth 配置和便携式凭据引用字段。授权发现、用户交互和凭据存储均由客户端管理。因此，任何与经过身份验证的服务通信的插件，在打包上是便携的，但在设置上是特定于客户端的，而设置正是用户最容易被卡住的地方。

第二点更为隐蔽。对于 stdio 服务器，命令必须是裸的可执行文件名或相对于插件的路径。配置的 PATH 值是否参与解析裸文件名是“客户端定义”的，规范称声称合规的插件不得依赖该行为。客户端还可以随心所欲地继承、省略或清理环境环境变量。两个合规客户端可以使用不同的环境和不同的解析结果启动同一个服务器。如果你的插件包含可执行文件，请使用相对于插件的命令，不要依赖宿主环境。

## v1.1 需要修复什么

项目方对这些差距表现得很坦诚。其 [未来考量文档](https://github.com/agentplugins/agent-plugins-spec/blob/main/FUTURE_CONSIDERATIONS.md) 列出了权限声明、密码签名验证、证明链、秘密机制、组织允许列表、审计事件架构、依赖解析和合规测试套件。

其中两个正在做不同的工作，值得一提。合规测试套件将使实现声明变得可测试，确立客户端是否正确执行了其声称的功能。机器可读的能力配置文件将使剩余的可选表面变得可预测，从而将今天的兼容客户端页面变成构建系统可以检查的内容。两者你都需要，而且后者是成本更低、收益更高的赢家。

签名和权限比上述两者更重要。权限模型迫使每个客户端就插件可以触及的内容达成一致，而当今的 IDE、CLI 和托管企业平台对此的答案各不相同。章程没有给任何供应商足够的票数来打破僵局。我应该说明这是我的推断，因为项目方并未明确提及。

Agent Plugins 做了其作者们设定要做的狭窄事情，这种克制是故意的，而不是疏忽。只要把兼容性页面看作能力列表，而不是承诺即可，因为定义其两种便携组件类型语义的规范，是在别处管理的。