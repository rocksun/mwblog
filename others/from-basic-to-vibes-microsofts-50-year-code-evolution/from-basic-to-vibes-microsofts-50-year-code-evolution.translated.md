# 从 BASIC 到 Vibes：微软 50 年的代码进化

![Featured image for: From BASIC to Vibes: Microsoft’s 50-Year Code Evolution](https://cdn.thenewstack.io/media/2025/04/ffb2ddc3-frank-albrecht-lkgwaktioyq-unsplash-1-1024x683.jpg)

为了纪念其成立 50 周年，微软发布了其独有的 [vibe coding](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) 套件——GitHub Copilot 代理模式和 [模型上下文协议 (MCP) 支持](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)。

GitHub 首席执行官 [Thomas Dohmke](https://www.linkedin.com/in/ashtom/) 在一篇介绍新解决方案的博文中 [模仿 Jay-Z](https://www.youtube.com/watch?v=9XEWVM1IhGY) 的口吻写道：“[请允许我们重新介绍一下自己](https://genius.com/Jay-z-public-service-announcement-lyrics)：[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 正在变得更加具有代理性，它能更好地理解你的工具和服务，这得益于世界领先的模型，从今天开始。”

或许是乘着这股嘻哈潮流，微软 CEO [Satya Nadella](https://www.linkedin.com/in/satyanadella/) 提供了一段自己在微软 50 周年纪念活动上进行 vibe coding 并使用该技术的视频片段。你不会找到很多 CEO 敢于登上舞台进行 vibe code。Nadella *确实* 很酷。他可以像其他人一样 [轻松驾驭连帽衫](https://seasonedgaming.com/2021/06/10/microsoft-ceo-satya-nadella-wears-halo-infinite-hoodie-in-latest-xbox-update/)（而且我听说他也能让派对气氛嗨起来，开玩笑的）。

微软向所有用户推出了 [Visual Studio Code 中的代理模式](https://github.com/features/copilot?utm_source=Blog&utm_medium=GitHub&utm_campaign=proplus&utm_notesblogtop)，现在已完整支持 MCP。它还发布了一个新的开源和本地 [GitHub MCP 服务器](https://github.com/github/github-mcp-server?utm_source=Blog&utm_medium=GitHub&utm_campaign=proplus&utm_notesblogtop)，使开发人员能够将 GitHub 功能添加到任何支持 [MCP](https://modelcontextprotocol.io/introduction) 的 LLM 工具中，MCP 是一种旨在简化 AI 模型与 API 交互方式的开源标准。

## 采取行动的 AI

与此同时，关于 Nadella 参加派对（所有玩笑都放在一边），微软对 vibe coding 非常认真。代理模式的革命性在于它能够超越单纯的建议。虽然最初的 Copilot 会在你键入时提供代码补全，但代理模式采取了一种更积极主动的方法。

Dohmke 在 GitHub 的公告中写道：“代理模式从根本上能够采取行动将你的想法转化为代码。” 这意味着 AI 可以建议终端命令、生成整个文件，甚至自动诊断和修复运行时错误。

微软在 [2 月份与 VS Code Insiders 分享了代理模式](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/)，“使开发人员能够执行各种任务：从 [自动修复代码生成错误](https://x.com/d4m1n/status/1898759539303809436)，到 [构建 Web 应用程序](https://x.com/jorisroovers/status/1898647091469025301)，到 [删除提交](https://x.com/Will479242/status/1900306201906188341)——无论那意味着什么，”Dohmke 写道。

一位早期用户 (@xthree) 在 X 上分享了他的经验：“我向它提出了我认为会是一项艰巨的任务，它扫描了 4-5 个不同的文件，弄清楚了它是如何工作的，并在所有这些文件中进行了修改，以完全按照我想要的方式工作。第一次就成功了。”

该技术目前正在向所有 VS Code 用户推广，GitHub 的目标是在未来几周内实现全面可用。手动启用也可用。

## 智能的 USB 端口

GitHub 将 MCP 描述为“智能的 USB 端口”。

公告称：“MCP 允许你为代理模式配备它需要的上下文和功能来帮助你，就像智能的 USB 端口一样。” 这意味着开发人员可以将代理模式连接到其开发堆栈中的各种工具和服务，从而将其功能扩展到 VS Code 内置的功能之外。

为了加速采用，GitHub 的开源本地 MCP 服务器将 GitHub 功能添加到任何支持该协议的 LLM 工具中。这允许代理搜索存储库、管理问题，甚至创建拉取请求——本质上将其变成 GitHub 平台本身的高级用户。

## 引擎盖下的多模型能力

GitHub 不会将用户限制为单一 AI 模型。代理模式将由 Claude 3.5 和 3.7 Sonnet、3.7 Sonnet Thinking、Google Gemini 2.0 Flash、OpenAI o3-mini 和 OpenAI GPT-4o 提供支持。
访问这些高级模型需要采用新的定价结构。GitHub 正在推出高级请求，Copilot Pro 用户从 5 月 5 日起每月可获得 300 个高级请求，而企业版客户将从 5 月 12 日至 19 日期间开始分别获得 300 个和 1,000 个高级请求。

新的 Pro+ 层级，定价为每月 39 美元，将为个人提供 1,500 个每月高级请求，并可以访问 GPT-4.5 等高级模型。

## 从 BASIC 到十亿开发者

此次发布的时间——恰逢微软成立 50 周年——颇具象征意义。在公司庆祝成立半个世纪之际，此次发布既是对其过去的思考，也是对其未来的大胆宣言。

Dohmke 写道：“从 BASIC 或 MS-DOS 的创建，到 .NET Framework 和 VS Code，再到收购 GitHub——微软始终是一家以开发者为核心的公司。半个世纪的开发者之爱绝非易事。”

此外，“现在，有了 GitHub Copilot——最初是一家开发者平台公司，现在已成为任何人都可以成为开发者的平台。GitHub 和微软都完全打算实现一个拥有 10 亿开发者的世界。”

为了说明这一点，在 Nadella 的一个精彩瞬间，他进行了一场精心设计的演示，展示了他如何使用 Agent Mode 来编写代码，并“一次性”重现微软的第一个 BASIC 程序——这是对公司起源的恰当致敬，也展示了开发者工具的发展历程。

Blue Badge Insights 的首席执行官 Andrew Brust 告诉 The New Stack：“Satya 的视频，他在其中创建了一个 Altair BASIC 模拟器，这很有趣，并且对微软成立 50 周年来说也很有怀旧意义，但对我来说，这似乎有点花哨，没有展示太多细节。因此，这激发了我内心的 AI 怀疑论者。”

他补充说：“但是 GitHub Copilot 在 VS Code 的 agent 模式下的演示是另一回事。是的，它处理的是一项更平凡的应用程序维护任务，但平凡的事情在软件世界中是现实的，这里就是这种情况。提示是合理的，任务是有界限的但又是不平凡的，结果是引人注目的。”

## Vibe Coding 很有趣

Microsoft MVP 和区域总监 [Richard Campbell](https://www.linkedin.com/in/richjcampbell/?originalSubdomain=ca) 告诉 The New Stack：“Vibe coding 很有趣——但请注意，你需要了解多少才能编写有用的提示。更不用说当它不起作用时该怎么办了。”

他补充说：“然后还有所有其他的考虑因素，比如部署、安全性、基础设施等等……没有什么是像看起来那么简单的。当 Andrej [Karpathy] 创造了这个术语时，他尝试了几次——在称其为 vibe coding 之前，他称其为用英语编码，他实际上是在谈论开发者进行实验。”

的确，任何愚蠢到部署以这种方式生成的代码的人，很可能是不了解这样做的后果的人。

Campbell 说，这“只是提醒人们，开发者的工作不是编写代码——而是充分理解问题，以便能够向计算机描述它们，从而更有效地执行”。“高效可能更快，可能成本更低……取决于具体情况。而且，还要在安全和适当的范围内。让专家来做这些事情才是正确的。”

## Agent 觉醒

GitHub 将此次发布称为“agent 觉醒”，这表明它认为这仅仅是 AI 辅助开发者方式发生更大转变的开始。

Dohmke 说：“Agent 觉醒不会止步于此。”他还宣布了 Copilot 代码审查代理的全面上市——在预览期间已被超过 100 万开发者使用——并发布了“下一个编辑建议”，允许开发者“通过 tab 键逐步实现编码的辉煌”。

对于许多开发者来说，agent 模式的引入代表了他们与 AI 辅助编码关系的一个重大演变。最初是一个有争议但有用的自动完成工具，现在已经转变为更接近于协作编码伙伴的东西，能够理解上下文，在文件中建立联系，并采取独立行动来解决问题。

Brust 说：“对我来说，这就是 AI 驱动的编码应该有的样子：用户提供技术上精明的需求，AI 完成繁重的工作，展示其工作成果，并让用户确认其有效性并批准其部署。”“只有当生成提示的人知道他们在说什么时，这才能奏效，但它可以减轻很多工作量。这与 AI 不会取代人，而是让人更有效率的观点完美契合。”

随着 vibe coding 进入主流，有一点是明确的：人类和 AI 对软件开发的贡献之间的界限继续模糊。在微软和 GitHub 等公司的带领下，未来 50 年的编程将与过去大不相同。

[
YOUTUBE.COM/THENEWSTACK
](https://www.youtube.com/THENEWSTACK)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
channel 来播放我们所有的播客、访谈、演示等内容。[The New Stack 的 YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1)