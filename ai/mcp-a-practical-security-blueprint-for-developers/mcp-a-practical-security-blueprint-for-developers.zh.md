想象一下，你的编码环境不仅仅是一个工具，而是一个真正的伙伴。它能预测你的需求，与你的数据库和基础设施无缝连接，甚至能与你的命令行工具对话。这不仅仅是一个未来的梦想，也是 [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) 所承诺的。MCP 扩展了像 Cursor、Windsurf 或 Cline 这样的高级代理编码工具，通过将其连接到外部上下文和工具，使你的工作更快、更顺畅、更强大。

但能力越大，责任越大。这项先进的技术在解放开发者的同时，也可能使你的系统和数据暴露于新的危险之中。因此，真正的问题不是 MCP 是否改善了开发者体验，而是如何在不危及安全的情况下采用它？

## **真实世界的警报：来自实践的教训**

安全使用 MCP 的旅程不仅仅是理论，它还受到实际事件的“警钟”的指导。这些不仅仅是可怕的故事，对于任何拥抱这项颠覆性技术的开发者来说，都是至关重要的教训。

以 Anthropic 的 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 为例。这个旨在帮助调试 MCP 服务器的工具，存在一个 [严重缺陷](https://nvd.nist.gov/vuln/detail/CVE-2025-49596)。因为它在客户端和代理之间缺乏适当的安全性，[未经授权的请求可以启动 MCP 命令](https://thehackernews.com/2025/07/critical-vulnerability-in-anthropics.html)。这是一个明确的提醒：即使是为安全而设计的工具，也需要强大的安全性。

另一个警告来自 [@cyanheads/git-mcp-server](https://github.com/cyanheads/git-mcp-server)。在 2.1.5 版本之前，这个帮助处理 Git 项目的服务器容易受到 [命令注入](https://nvd.nist.gov/vuln/detail/CVE-2025-53107) 的攻击。这意味着，如果输入没有被正确清理，攻击者可以注入他们自己的系统命令，将一个有用的工具变成武器。

而且这不仅仅是开发者工具。[WordPress AI Engine 插件](https://wordpress.org/plugins/ai-engine/) 在 2.1.5 版本之前，存在一个 [安全漏洞](https://nvd.nist.gov/vuln/detail/CVE-2025-5071)，它没有正确检查用户权限。这可能导致未经授权的更改或数据丢失。这些事件突出了一个关键点：**AI 集成的便利性永远不应以牺牲强大的安全性为代价。**

## **你的安全蓝图：安全地使用 MCP**

那么，如何在不引来灾难的情况下利用 MCP 的巨大潜力呢？这首先要始终考虑安全性，并将其构建到开发和采用的每一步中。

### **隐藏的威胁：提示注入**

想象一下，你的 AI 助手，仔细地按照指令行事，突然将机密文件发送给攻击者。这就是 [提示注入](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/) 的危险。在这里，有害的命令隐藏在 AI 处理的看似正常的文本中。AI 没有意识到隐藏的命令，执行了你从未批准的操作。

**开发者如何解决它：**

* **始终显示工具操作以供用户批准：** 清晰是最好的防御。在任何操作发生之前，使其显而易见，并要求用户说“是”。
* **阻止或清理可疑模式：** 警惕隐藏的文本或旨在欺骗 AI 的棘手的 Unicode 字符。
* **使用强类型工具：** 使用强类型工具构建服务器可以大大降低远程代码执行的风险。通过清楚地显示每个操作并需要用户批准，你可以创建一个至关重要的安全检查，让人始终参与其中。[Salesforce DX MCP Server](https://github.com/salesforcecli/mcp) 就是使用 TypeScript 库来实现这一点的。

### **沉默的盗窃：令牌盗窃**

MCP 服务器通常存储 [OAuth 令牌](https://thenewstack.io/supply-chain-attacks-how-to-mitigate-oauth-token-theft/) 以连接到其他在线服务。如果这些令牌被盗，攻击者可以冒充用户，而且往往不会引起任何人的注意。这不仅仅是一个服务被黑客攻击，一次违规可能导致跨多个服务的攻击，使攻击者可以广泛访问你的数字世界。

**开发者如何解决它：**

* **使用有效期短且访问权限有限的令牌：** 令牌的有效期越短，它可以执行的操作越少，如果被盗造成的危害就越小。
* **加密存储令牌并定期更改它们：** 像对待贵重物品一样对待你的令牌 —— 好好保护它们并经常更新它们。
* **采用“零秘密”方法：** 例如，使用 Salesforce DX MCP Server 意味着开发者不需要将秘密信息放在他们的设置中，从而消除了明文秘密信息暴露的风险。此外，它专注于传递用户名而不是令牌，这大大降低了攻击的可能性。

### **过多的访问权限：过度宽泛的权限**

许多 MCP 服务器为了易于使用，即使只需要读取信息，也会要求完全访问你的系统。这种看似很小的过度请求可能会产生严重的后果。一个具有过多访问权限的受损工具可能会泄露你的整个电子邮件收件箱、你的整个驱动器 —— 甚至是你从未打算共享的文件。

**开发者如何解决它：**

* **遵循最小权限原则：** 只提供所需的精确权限。把它想象成只给客人他们需要进入的房间的钥匙，而不是你整栋房子的钥匙。
* **仔细审查访问权限：** 定期检查和修剪权限，以确保它们与实际需要的权限相符。
* **实施详细的访问控制：** Salesforce DX MCP Server 是一个很好的例子。它只能获取明确允许的组织的身份验证信息，并且用户在启动服务器时指定这些允许的组织。

### **隐藏的危险：恶意或未经检查的工具**

MCP 生态系统的开放性可能是一种喜忧参半的祝福。第三方 MCP 服务器虽然方便，但可能包含隐藏的或有害的行为。这带来了内部数据被盗和严重的 [供应链](https://www.cloudflare.com/learning/security/what-is-a-supply-chain-attack/) 攻击的风险，其中一个部分的问题可能会影响你的整个系统。

**开发者如何解决它：**

* **审查源代码的安全性：** 在允许开发者使用任何 MCP 服务器之前，对其源代码进行彻底的安全检查。
* **选择官方的、签名的软件：** 选择来自可信来源的、具有验证过的数字签名的 MCP 服务器。
* **维护一份批准的 MCP 服务器列表：** 创建一份经过检查的 MCP 服务器的精选列表，并避免在没有首先进行安全审查的情况下进行自动更新。
* **执行内部规则：** 例如，在 Salesforce，只允许开发者使用经过安全部门批准的 MCP 服务器。

### **敞开的大门：不安全的默认设置和网络暴露**

早期的 MCP 连接器，为了易于使用，通常在 `0.0.0.0` 上运行，没有任何身份验证或加密。这基本上留下了一扇敞开的大门，允许攻击者只需访问一个网页就可以利用这些工具。这种疏忽创建了一条通往 [远程代码执行](https://www.cloudflare.com/learning/security/what-is-remote-code-execution/) (RCE) 漏洞和立即数据盗窃的直接途径。

**开发者如何解决它：**

* **始终使用 HTTPS：** 加密所有通信以保护数据在传输过程中的安全。
* **使用基于 OAuth 的身份验证：** 安全地确认访问你的 MCP 服务器的用户和应用程序的身份。
* **使用安全的基于云的解决方案：** 例如，Salesforce 的 [Heroku Remote MCP Server](https://www.heroku.com/blog/heroku-remote-mcp-server/) 使用 OAuth 进行安全身份验证，以支持安全的默认设置和云集成。

## **超越基础：持续的警惕**

安全地采用 MCP 不是一项一次性的任务，而是一项持续的承诺，要保持警惕并始终改进。

* **审查你的代码和设计：** 定期检查你的 MCP 设置的安全性。
* **记录和监控每一个工具调用：** 详细的日志记录提供了记录，并有助于及早发现异常活动。
* **随时了解情况并更新：** 关注安全警告，并迅速将你的 MCP 服务器更新到最新的、最安全的版本。

## **结论：负责任地赋能开发者**

模型上下文协议确实是一个游戏规则改变者。它提供了先进的开发者体验，将人类意图与机器执行相结合。但这种力量带来了一个至关重要的要求：**安全性必须是其设计的首要任务。**

通过使用类型化工具、避免以明文形式存储秘密信息、仅提供必要的访问权限以及将安全性作为默认设置等方法，你可以将 MCP 从潜在的弱点变成你 AI 工具包中强大而安全的工具。

同样令人鼓舞的是，我们看到了企业界提出的许多 [提案](https://github.com/modelcontextprotocol/modelcontextprotocol/issues?q=is%3Aissue%20state%3Aopen%20security) ，旨在改进协议的安全设计。开发的未来是智能和互联的；让我们确保它也是安全的。