<!--
title: 五大AI巨头联合支持共享插件标准，这对开发者意味着什么？
cover: https://cdn.thenewstack.io/media/2026/08/357f1ef4-andrei-castanha-scaled.jpg
summary: OpenAI、微软等巨头共同支持Agent Plugins 1.0开源标准，旨在统一AI Agent技能与MCP服务器的打包格式，实现跨平台的互操作性，降低开发门槛。但专家提醒，在提升便利性的同时，仍需警惕权限管理与安全性风险。
-->

OpenAI、微软等巨头共同支持Agent Plugins 1.0开源标准，旨在统一AI Agent技能与MCP服务器的打包格式，实现跨平台的互操作性，降低开发门槛。但专家提醒，在提升便利性的同时，仍需警惕权限管理与安全性风险。

> 译自：[Five AI rivals just backed a shared plugin standard. Here's why it matters for developers.](https://thenewstack.io/agent-plugins-open-standard/)
> 
> 作者：Adrian Bridgwater

[OpenAI](https://thenewstack.io/openai-aims-to-make-chatgpt-the-operating-system-of-the-future/), [AWS](https://aws.amazon.com/blogs/opensource/aws-supports-agent-plugins-an-open-standard-for-portable-agent-extensions/), [Cursor](https://thenewstack.io/cursor-3-demotes-ide/), [GitHub](https://thenewstack.io/github-agent-hq/) 以及 [Microsoft](https://thenewstack.io/microsoft-scout-openclaw-runtime/) 已联合支持 [Agent Plugins](https://agent-plugins.org/#) 1.0.0。这是一个用于可重用组件的便携式包格式，旨在扩展 AI Agent。

代理基础设施公司 [Vercel](https://vercel.com/home?utm_source=google&utm_medium=cpc&utm_campaign=24015397389&utm_campaign_id=24015397389&utm_term=vercel&utm_content=198458702299_816334546963&utm_source=google&utm_medium=cpc&utm_campaign=gg_s_vercel_acq_emea_brand-exact&utm_campaign_id=24015397389&utm_content=brand_exact&utm_term=vercel&gad_source=1&gad_campaignid=24015397389&gbraid=0AAAAACXzHouXxZSdS4kiM34b0S4nqGVRm&gclid=CjwKCAjwhNbTBhB4EiwAsFSg-iJmUmPtFH3JSrcMQCP-qSjDKmY6K86gRJGGVwAtJlU0QWKyxeRqmBoCTrIQAvD_BwE) 发起了 Agent Plugins 提案及[项目的核心规范](https://vercel.com/blog/introducing-agent-plugins)，并于周四详细说明了其发布情况。

Agent Plugins 是一个开放且独立于厂商的插件标准，它将 AI Agent 技能（一种旨在使 Agent 能力具备可移植性、模块化和“[渐进式加载](https://www.mindstudio.ai/blog/progressive-disclosure-ai-agent-skill-design)”特性的开放标准目录格式）和 MCP 服务器打包成可分发的插件，以便将它们扩展到其他 AI Agent 客户端、运行时或其他自定义 AI 框架中。

尽管 Agent 技能和 MCP 服务器可以在不同的客户端之间重用（在此意义上，客户端指任何软件平台托管、执行或连接到 AI Agent 的应用程序、代码编辑器、软件工具或代码运行时），但这些客户端本身通常以不同的方式和格式来打包和发现 Agent 技能及 MCP 服务器。

Vercel 的技术员工 Jonathan Hefner 在[博客](https://vercel.com/blog)中解释了此举的重要性。

“Agent Plugins 为兼容的客户端提供了一种通用格式：一个包含 [plugin.json](https://docs.castopod.org/develop/en/plugins/reference/plugins-json/) 清单和组件固定位置的目录。该格式设计得非常小巧且易于实现，将安装、分发、策略、用户体验和特定于客户端的功能留给每个客户端去处理，”Hefner 写道。

他指出，Agent Plugins 是作为编写 Agent 扩展的开发者与加载这些扩展的客户端之间的一份契约，现在这份契约已对双方“明确且开放”，可由双方共同塑造。

Hefner 与同事 Eric Dodds、Andrew Qu 表示，Agent 技能为 AI Agent 提供了可重用的指令和资源，而 [MCP 服务器](https://modelcontextprotocol.io/docs/getting-started/intro) 则用于将 Agent 连接到工具和服务。那么，开发者为什么还需要插件呢？

## 开发者为什么需要让 Agent 接入插件？

在实际的现实用例中，软件开发者需要 Agent 和技能来连接实时数据库和各种数据馈送，以运行查询、交叉引用模式元数据并利用实时分析。插件操作的实现可以让 Agent 与 GitHub、Jira、Slack、Figma 或大型云超大规模平台建立关键连接。

Agent 还利用插件连接 USB 或硬件接口（可能跨越分布式边缘环境，也包括桌面设备），与本地开发环境和微服务交互，或者（例如）从地图或天气 API、支付网关或支付处理服务（如 [Stripe](https://stripe.com/)、[Adyen](https://www.adyen.com/en_GB) 或 PayPal 的企业服务 [Braintree](https://www.paypal.com/us/braintree)）中获取数据。

Hefner 强调了该项目的状态，确认它是开放许可的，且其维护者、贡献流程和技术决策都是公开的，因此没有任何单一公司的产品路线图能决定该格式的发展方向。

他表示，对于插件作者来说，Agent Plugins 1.0.0 意味着针对同一组件的特定于客户端的约定变少了。同样，对于客户端实现者来说，该规范定义了一个用于发现、验证和加载的小型确定性契约。

## 我们是赢了战斗，却输了战争吗？

工业用品公司 Grainger 的高级云平台工程师 Pavan Madduri 告诉 *The New Stack*，在他看来，Agent Plugins “解决的是简单问题，而不是困难问题”。

“在 ChatGPT、Cursor、Copilot 和 VS Code 中标准化 Agent 技能和 MCP 服务器的打包和发现确实是有用的基础设施——但与此同时，一个现在运行在六个不同客户端应用程序中的插件，也代表了权限管理的一个额外故障点，”Madduri 说道。

> “一旦某样东西变成 Agent 的‘一次编写，随处运行’，它就自动变成了‘一次妥协，处处被攻破’，而该规范明确将治理、安装策略和权限管理委托给了客户端应用程序。”

在他看来，该规范将治理和权限管理留给各方，可能会带来安全隐患。

“没有信任和权限管理的互操作性不是安全架构；它只是另一种传播漏洞和过度权限的方法，”Madduri 警告道。

## 朝着使 AI Agent 更具互操作性迈出的重要一步

上下文感知代码创建和理解工具集专家 [Adronite](https://www.adronite.com/) 的总裁兼 CTO Edward Rothschild 告诉 *The New Stack*，他认可治理和安全方面的责任，但总体上认为这具有价值，并称 Agent Plugins 1.0.0 是现代技术栈中“使 AI Agent 更具互操作性的重要一步”。

“真正的价值在于能够减少阻碍企业 AI 采用的摩擦，”Rothschild 说。“与其要求插件开发者为每一个 AI 客户端或 Agent 框架以不同的方式打包和维护集成，不如采用通用标准，使这些能力在不同环境中更具可移植性，同时仍然允许组织维持治理和安全性。”

随着开放标准的成熟，Rothschild 呼吁各方共同努力，让标准机构和商业组织继续将互操作性与强大的身份验证、访问控制和运营可观测性相结合，赋予开发者灵活编码的能力，同时不引入新的管理盲点。

AI 模型托管公司 [EmpirioLabs](https://empiriolabs.ai) 的创始人 Adam Dalloul 告诉 *The New Stack*，他的实践经验让他认为“当前的 Agent 基础设施距离云原生和 MLOps 还相去甚远”。

“我们亲身经历过开源 Agent 更新在平稳运行数周后破坏生产工作流程的情况，所以版本控制、测试和回滚不能是事后才考虑的事情，”Dalloul 说。“能够将技能和 MCP 服务器打包一次，并在 Codex、ChatGPT、Cursor、GitHub Copilot、Kiro 和 VS Code 中通用，这确实是一个真正的胜利，老实说，这种通用格式早该存在了。”

> “能够将技能和 MCP 服务器打包一次，并在 Codex、ChatGPT、Cursor、GitHub Copilot、Kiro 和 VS Code 中通用，这确实是一个真正的胜利，老实说，这种通用格式早该存在了。”

但他有一个担忧：特定于客户端的扩展。

“我之所以表达这种担忧，是因为如果所有有用的行为最终都进入了厂商的命名空间，那么该标准在纸面上看起来是开放的，而锁定和碎片化只会转移到其他地方，”Dalloul 补充道。

## 放眼未来：关注命令、钩子和 Agent 本身

如前所述，Agent Plugins 1.0.0 专注于两种组件类型：Agent 技能和 MCP 服务器。

Hefner 确认，其他组件（如命令、钩子和 Agent 本身）仍由各客户端负责。技术指导委员会可能会在未来的版本中考虑增加更多的组件类型，只要语义趋于统一且出现了明确的可移植性需求。