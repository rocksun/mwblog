AI 需要治理。在预测性、生成式和代理式人工智能呈指数级增长的同时，人们一再追问：“它安全吗？我们还能控制它吗？”

随着 AI 如今演进并集成到实时生产软件系统中，安全和治理平台公司 [SurePath AI](https://www.surepath.ai/) 周四推出了一项新服务。该公司表示，这项服务将弥补智能自动化的可见性差距，并确保每一次 AI 交互的安全。[SurePath MCP 策略控制](https://www.surepath.ai/) 提供实时防护，控制特定代码库允许使用哪些 [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 服务器和工具。

但 [Anthropic 推出了 MCP](https://www.anthropic.com/news/model-context-protocol)，受到了广泛欢迎，这项技术被誉为 [代理式 AI 的 USB-C](https://medium.com/@priyasrivastava18official/why-mcp-is-called-the-usb-c-of-agentic-ai-f9bcd256968d)。那么，为什么开发者需要关注他们将哪种 MCP 作为自己的 USB 使用呢？

## 为什么 MCP 并非总是那么简单？

[网络安全专家](https://www.securityweek.com/anthropic-mcp-server-flaws-lead-to-code-execution-data-exposure/) 指出，通过 MCP 服务器的读/写访问存在潜在的供应链攻击风险；还存在数据外泄和泄漏路径风险，即 API 密钥、安全凭证或用户身份可能被泄露；专有逻辑可能泄漏给第三方，尤其是在 MCP 连接由未经部门批准和监督的所谓“影子 AI”元素建立时；我们还应记住，流氓 MCP 行为可以连接到旨在应用破坏性代码修改（且没有可见回滚路径）的代理服务，而开发者对此可能一无所知。

但简单地阻止 MCP 是不切实际的；需要采用超越传统防火墙和身份与访问管理 (IAM) 策略的技术进行安全管理。虽然基于云的 MCP 提供了一些防护措施，但它们也增加了攻击面。例如，连接到本地和远程 MCP 服务器混合环境的多个代理会为数据蔓延和横向移动创建错综复杂的路径。

SurePath AI 的首席产品官兼联合创始人是 Randy Birdsall。Birdsall 惋惜 MCP 的兴起与 [ChatGPT 首次面世](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/) 时所见的狂热如出一辙，他告诉 *The New Stack*，他看到的是快速采用、缺乏监管以及对风险的肤浅理解。

“我们看到 MCP 在每个组织中都在使用——不仅仅是开发者，还有商业领袖和 AI 高级用户，他们点击连接 AI 客户端和代理到关键企业系统。在我们一个较大的企业客户中，启用 MCP 策略控制的最初几个小时内，我们就识别出了一千多个正在使用的有风险或恶意的 MCP 工具，”Birdsall 说。

## MCP 的“热线电话”

Birdsall 表示，MCP 可以充当生成式 AI 客户端与支持企业运营的系统之间的“直接线路”。这些轻量级 MCP 工具可以在用户的笔记本电脑上本地运行，并且通常由 AI 桌面应用程序（如 ChatGPT、Claude 和 Cursor）静默启动。它们还链接到内部工具，如 Google Drive、Salesforce 和 AWS 管理 API。

> “如果缺乏对 MCP 负载的可见性和控制，组织只能寄希望于用户自行遵守最佳实践。‘YOLO 模式’并非有效的安全策略。”

他说，这带来了新的安全挑战，即 AI 现在正以终端用户的身份发出真实的指令。

“组织在管理 MCP 方面面临的最大挑战之一，不仅是建立批准的资源，还在于尝试监控和保护已启用 MCP 的各种系统的使用——从本地 MCP 服务器生态系统中的供应链攻击，到现有 SaaS 产品远程 MCP 端点上验证不佳的身份验证流程。”

“如果缺乏对客户端与 AI 模型之间 MCP 负载的可见性与控制，组织只能寄希望于用户自行应用最佳实践。正如我们所见，‘YOLO 模式’并非一种[有效的安全策略](https://thenewstack.io/how-threat-research-can-inform-your-cloud-security-strategy/)，”Birdsall 告诉 *The New Stack*。

## 剖析破坏性决策

SurePath AI 专门旨在解决这些挑战，通过在任何执行发生之前，对允许使用哪些 MCP 服务器和工具实施基于策略的控制。该技术本身具有足够的模式感知能力来转换这些请求，因此 SurePath AI 通过控制本地 MCP 主机及其连接来强制执行组织关于允许使用哪些 MCP 服务器和工具的策略。这些策略可以使用内置的工具破坏性分类，也可以根据每个组织的安全要求进行明确定制。

为了减轻远程侧的风险，SurePath AI 维护了一个已知 MCP 服务器和端点的目录。所有受保护的 MCP 流量都通过其平台路由，在那里实时应用访问控制，细化到特定工具级别。

SurePath AI 的新功能还能通过检测“从未见过”的 MCP 工具来发现供应链威胁，这些工具可能冒充其他工具或试图将数据泄露到批准的安全边界之外。

## 完善 MCP 负载

更具体地说，在该工具集中，该公司构建了一个 MCP 工具发现功能，使团队能够通过监控整个员工队伍中 AI 工具的 MCP 使用情况来发现 MCP 工具。它的工作原理是拦截 MCP 负载，并删除那些被策略阻止或违反能力要求（例如非只读工具）的工具。当某个工具违反策略时，它会在发送到后端服务之前从 MCP 负载中移除，这意味着该服务将无法利用该工具。

SurePath MCP 策略控制还包括一个 MCP 工具黑名单、一个 MCP 工具白名单、一个允许只读功能和一项全方位捕获操作，以控制系统如何处理超出已定义黑白名单的工具。

至于 MCP 的使用是否变得更安全或更强大，答案可能兼而有之。行业告诉我们，更多的开发者正在陷入 MCP 的便利陷阱，但同时，更多的治理和控制工具集（如 SurePath 的产品）也正在涌现。