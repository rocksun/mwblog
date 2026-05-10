随着 AI 智能体接管了更多的应用程序逻辑，例如读取文件、获取网页和处理队列消息，围绕 HTTP 边界构建的安全工具不再有效。[Arcjet](https://arcjet.com/) 希望通过其最新产品来解决这一问题。

这家总部位于旧金山的运行时安全公司最近宣布推出了 [Guards](https://docs.arcjet.com/guards)，这项功能可以在 [AI 智能体工具处理程序](https://thenewstack.io/how-to-choose-the-right-tool-for-your-google-adk-agent/)、队列消费者和工作流步骤中[执行安全策略](https://thenewstack.io/the-impact-of-regular-training-and-timely-security-policy-changes-on-dev-teams/)。由于这些代码路径从不涉及 HTTP 请求，因此对传统的 Web 应用程序防火墙 (WAF)、代理和中间件来说是不可见的，公司 CEO [David Mytton](https://www.linkedin.com/in/davidmytton/) 告诉 *The New Stack*。

## Guards 针对的缺口

其前提非常简单。传统的应用程序安全（如 WAF、AI 网关和代理）假设存在请求边界。一个 HTTP 请求进入，到达中间件，经过检查，然后到达应用程序代码。当应用程序有一个“前门”时，这种模式是有效的。

但代理化系统（Agentic systems）并非如此。Mytton 在随发布公告一同发表的[博客文章](https://blog.arcjet.com/introducing-arcjet-guards-security-inside-the-agent-loop/)中写道：“智能体工具处理程序接收非受信输入作为函数参数，而不是请求体。队列消费者从经纪人（broker）那里获取消息，从不触及路由器。一个[多智能体流水线](https://thenewstack.io/vs-code-becomes-multi-agent-command-center-for-developers/)通过共享内存或工作流引擎将状态从一个步骤传递到下一个步骤。” 这些都不会跨越代理能够看到的网络边界。

其后果是非常具体的。

事实上，Mytton 引用了一个真实案例：一个智能体下载了一个恶意设计的网站，该网站指示它将内容发送给外部攻击者，而保护上游聊天界面的 WAF 从未发现这一情况。

他在接受 *The New Stack* 采访时表示：“你在聊天界面上设置了正确的所有权限，但通过在幕后直接对智能体进行提示词注入，你可以让它执行超出预期的操作。” 隐藏在智能体加载的图像中的文本指令是他指出的另一个攻击矢量。

除了可见性之外，还存在上下文问题。Mytton 在博客文章中写道：“位于应用程序前端的代理可以看到请求，但它无法看到身份、会话、业务逻辑或预算。” Guards 运行在应用程序内部，也就是这些上下文存在的地方。他指出，在代理化系统中，信息的丢失更为严重——代理根本无法看到工具调用，因为工具调用不是一个请求。

## Guards 的功能

Guards 集成到了 [Arcjet 现有的 SDK 模型](https://thenewstack.io/arcjet-reaches-v10-promises-stable-security-for-javascript-apps/)中，开发人员在与功能相同的代码库中定义规则，因此保护措施随代码一同交付，并在同一个拉取请求（Pull Request）中进行审查。执行点移动到了任何非受信输入到达的地方。

Mytton 在关于该消息的[新闻稿](https://www.prnewswire.com/news-releases/arcjet-introduces-guards-bringing-application-security-inside-ai-agent-workflows-302758796.html)中表示：“安全必须存在于代码存在的地方。对于[代理化系统](https://thenewstack.io/why-agentic-llm-systems-fail-control-cost-and-reliability/)来说，这意味着在非受信输入实际到达的工具调用和工作流步骤内部，而不是在一个已不复存在的周界。Guards 为开发人员提供了一种在智能体日常使用的代码路径中执行策略的方法——这正是威胁模型现在所处的位置。”

初始用例涵盖了 Arcjet 认为在生产代理化系统中最迫切的三个场景：工具结果上的提示词注入检测——在获取的内容重新进入模型上下文之前捕获其中嵌入的恶意指令；在数据到达第三方模型之前，对工具输入和队列消息进行 PII（个人身份信息）屏蔽；以及在智能体循环内部执行每个用户的 Token 预算。

关于最后一点，Mytton 在简报中直言不讳：失控的智能体循环会迅速耗尽预算。他说，“控制预算”意味着它“不会去读取成千上万个页面并耗费大量资金”。

Guards 还能处理多智能体场景。它不是孤立地检查单个工具调用，而是在整个流水线中携带会话上下文。Mytton 告诉 *The New Stack*：“如果你有多个智能体在做不同的事情，其核心理念是你将工具调用包裹起来，保护输入内容，然后它会分析输出内容——这样你就有两次分析的机会。”

## 智能体优先，而不只是对智能体友好

Arcjet 的宣传超出了技术能力的范畴。Mytton 将“对智能体友好”的产品与围绕智能体实际工作方式构建的产品划清了界限。

他在博客文章中写道：“对智能体友好并不等同于智能体优先。在现有的控制平面或仪表盘之上交付 [CLI](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) 或 [MCP 服务器](https://thenewstack.io/build-mcp-server-tutorial/)可以使该控制平面可供智能体访问，但这只是工作的一半。”

在 Arcjet 的定位中，另一半工作是在智能体运行的地方与其交汇——即在代码仓库内部，编写代码并生成差异（diff）。

Mytton 在文章中写道：“当保护代码就在同一文件的上方三行时，编写聊天处理程序的智能体可以看到保护它的提示词注入规则。代码审查涵盖了这两者。添加功能的拉取请求同时也添加了保护。”

Arcjet 为 Guards 提供了一种基于提示词的安装路径：安装命令不是引导开发人员进行手动的 SDK 集成，而是直接提供指令，让 Claude Code、Codex 或 Gemini Code Assist 等编程智能体直接执行。正如 Mytton 在简报中所说，与其告诉开发人员安装 SDK 并让他们自己摸索，“我们只是给你一个提示词，该提示词会告诉你的编程智能体如何使用 Arcjet Guards。”

## 竞争格局

传统的 Web 方法已经得到了充分的覆盖。Cloudflare 的 AI Gateway 和 Salesforce 的 AI Gateway 处理速率限制、计费和请求检查，但两者都基于正在进行 Web 请求的假设运行。

“这些都是代理，它们总是假设 Web 请求正在发生，”Mytton 告诉 *The New Stack*。

Arcjet 的论点是，当智能体调用函数而不是发起请求时，代理模型会撞上结构性的墙。

“就像你在终端运行某些东西一样——它不会先经过代理。这就是 Arcjet 的切入点，”他说。

Mytton 从周界转移的角度看待这种转变。

Mytton 在博客中写道：“代理和 WAF 之所以存在，是因为在很长一段时间里，它们是在不涉及开发人员的情况下，在互联网和应用程序之间设置执行点的唯一方法。这在以前行得通，是因为周界是真实存在的。而现在，周界正在消融。”

Guards 现在可通过 Arcjet 的 JavaScript 和 [Python SDK](https://thenewstack.io/arcjets-python-sdk-embeds-security-in-code/) 使用。