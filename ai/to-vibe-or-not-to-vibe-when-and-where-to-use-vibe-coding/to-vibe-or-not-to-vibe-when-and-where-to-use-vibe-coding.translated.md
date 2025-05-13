# Vibe Coding：何时以及在何处使用 Vibe Coding

![Featued image for: To Vibe or Not to Vibe? When and Where To Use Vibe Coding](https://cdn.thenewstack.io/media/2025/05/c2a4c0e7-andrej-lisakov-f5tv-e6v7-0-unsplashb-1024x576.jpg)

Vibe coding，这个术语由 [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383?) 在 2025 年 2 月创造，指的是通过自然语言提示来引导 AI 模型生成可用的代码，从而将开发人员的角色从打字转变为指导和改进 AI 输出。这种方法大大减少了对深入编码知识的需求，并允许快速原型设计。

听起来很棒，对吧？软件工程师不再需要花费数小时来完善代码！相反，他们可以成为指挥家，引导 AI 工具的交响乐来创建他们梦想中的项目。但这个想法到底有多真实呢？

在本文中，我将介绍 vibe coding 的最佳用例，并检查可能不是最佳方法的场景，以便您了解是否要使用 vibe coding。

## 什么是 Vibe Coding？

Vibe coding 是一种[编程过程](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)，开发人员无需为项目编写代码，而是用简单的语言描述他们希望实现的目标，然后由专门的大型语言模型 (LLM) 生成相应的代码。

与传统的逐行编码不同，vibe coding 将工程师和开发人员的角色从工匠或构建者转变为架构师：您告诉 LLM 您想要什么，测试它生成的内容，然后进一步改进它，无论是您自己还是通过进一步提示 LLM。

常用工具包括 [Cursor](https://dolthub.com/blog/2025-03-29-vibin/)、[Windsurf](https://www.analyticsvidhya.com/blog/2025/03/vibe-coding-with-windsurf/)、[Claude Code](https://www.infoworld.com/article/3853805/vibe-coding-with-claude-code.html)、[Replit](https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/) 和 [ChatGPT](https://medium.com/@niall.mcnulty/how-i-vibe-coded-a-micro-app-in-10-minutes-with-chatgpt-87db79fe5b4a)。

## 寻找那些美妙的 Vibes：Vibe Coding 的适用场景

Vibe coding 正在许多不同的场景中进行测试。到目前为止，以下似乎是该过程的最佳用例：

### 快速原型设计和想法验证

对于争分夺秒进入市场的创始人和工程师来说，[vibe coding 提供了一种无摩擦的方式](https://www.businessinsider.com/developers-redefined-builders-ai-windsurf-ceo-varun-mohan-2025-5)来启动最小可行产品 (MVP) 并在数小时（而不是数周）内验证概念。您可以生成主要由 AI 生成的代码库，这些代码库围绕提示构建，允许您即时迭代功能。这种方法与[敏捷业务和开发原则](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/)完美契合：随意提示、修补和快速调整。它对于黑客日演示、内部原型和投资者推介非常有效，在这些场景中，速度比完美更重要。

### 小型项目和低风险应用程序

当您只需要一个个人网站、浏览器游戏或一次性自动化脚本时，vibe coding 通过[消除样板文件的繁琐工作](https://spectrum.ieee.org/vibe-coding)来提供价值。生成小型游戏、制作实用程序以自动化繁琐的工作流程或创建需要最少监督的内部仪表板等任务非常适合，尤其是在最坏的结果只是花费额外的几分钟手动调试时。

### 学习和探索

编码初学者经常面临[陡峭的学习曲线](https://lifemichael.com/corporate/the-journey-through-the-learning-curve-of-programming/)。Vibe coding 通过允许学习者快速了解工作代码的影响来拉平曲线。对于[经验丰富的工程师](https://simonwillison.net/2025/Mar/19/vibe-coding/)也有好处：vibe coding 可以探测不熟悉的语言或框架、搭建 UI 或生成示例算法，以便他们可以通过探索加深理解。

### 工作流程简化和重复性任务

在成熟的代码库中，存在大量耗时的重复性任务：重构命名约定、添加日志记录、更新许可证标头等。Vibe coding 可以[自动化这些琐事](https://dev.to/erikch/what-i-learned-vibe-coding-30em)，从而节省数小时的单调乏味，并将工程师解放出来以从事具有高影响力的工作。

### 处理设计和 UI 调整

产品经理和设计师可以利用 vibe coding 来应用快速的 UI 调整，例如调整填充、交换配色方案或生成多个布局变体，而无需搜索 CSS 文件。这种“[提示驱动开发](https://andrewships.substack.com/p/prompt-driven-development)”支持直接实验和快速反馈循环。

### 修复 Bug 和小故障（某种程度上……）
将错误消息粘贴到 LLM 中通常会立即得到修复，但[这些修复可能很表面](https://blankslatedigital.co.uk/blog/artificial-intelligence/what-is-vibe-coding/)。虽然感觉编程可以迅速解决常见的语法错误，但更深层次的逻辑错误仍然需要人类的洞察力。

## 真实世界的例子和成功案例

有很多人正在探索感觉编程的用例和应用。这里仅举几个例子：

### Fly Pieter

荷兰企业家 Pieter Levels 使用 Cursor 和 Claude 3.7 Sonnet 在不到三个小时内构建了一个[基于 3D 浏览器的飞行模拟器](https://avgeekery.com/new-flight-simulator-made-with-ai-earns-creator-5000-per-month/)，其中包含摩天大楼，据报道通过 Stripe 小额交易每月产生超过 67,000 美元的收入。

### 语音转应用

工程师 Riley Brown 通过使用感觉编程结合不同的 AI 工具来创建多模态输入（语音和图像识别），在几分钟内[创建了一个主页和登录页面](https://www.youtube.com/watch?v=08TcHAeTJeU)。

### 十分​​钟内的 Airbnb 克隆

Cognosys 的 CEO Sully Omar 现场演示了 [Cursor 的新代理和 Whisper 语音转文本](https://x.com/SullyOmarr/status/1893757471799308321) 如何完全通过提示和语音在十分钟内构建一个可用的 Airbnb 克隆（包括后端、UI 和数据库）。

还有很多其他值得探索的例子！

## 当感觉不对时：感觉编程的不足之处

但在你匆忙决定编码现在只是感觉之前，让我们停下来讨论一下经验丰富的开发人员进行传统的逐行编码仍然是最佳选择的情况。

### 安全敏感型应用

处理用户凭据、支付信息或个人数据需要严格的[应用安全措施](https://www.imperva.com/learn/application-security/application-security/)。 AI 生成的代码通常[忽略最佳实践](https://qwiet.ai/appsec-resources/risks-in-ai-generated-code-a-security-and-reliability-perspective/)，例如正确的加密、API 密钥的安全存储或正确的 CORS 配置。盲目部署感觉编码的身份验证或支付流程可能会使组织面临违规和监管罚款的风险。

### 大型生产软件

企业系统和分布式微服务需要精心设计的解决方案、强大的 CI/CD 管道和详尽的测试。[幻觉和上下文窗口限制](https://devops.com/ai-generated-code-packages-can-lead-to-slopsquatting-threat/)使得在广泛的代码库中进行深度调试变得不切实际。对于正常运行时间和可靠性至关重要的关键任务基础设施，感觉编程绝不应取代人为驱动的设计。

### 合规性高的领域

金融、医疗保健和政府等行业在严格的法规（HIPAA、GDPR 等）下运作。 AI 模型可能缺乏对细微法律要求的认识，因此不适合为任何需要符合严格法规的内容[生成合规代码](https://www.jit.io/resources/devsecops/ai-generated-code-the-security-blind-spot-your-team-cant-ignore)。

### 当需要原创性或深刻理解时

LLM 生成现有模式的衍生物；它们不是发明家。复杂的算法，例如新颖的优化例程或专有的数据处理管道，[需要人类的独创性](https://conspicuous.com/conspicuous-blog/ai-vs-human-coders-comparative-analysis/)。如果你的开发项目正在创造全新的东西，而不是复制现有的东西，那么感觉编程可能会不足。

### 专有或敏感代码

你[永远不应将私有或专有资源](https://www.securityjourney.com/post/5-types-of-data-you-should-never-share-with-ai)提供给未沙盒化的 AI 助手。尤其是代码，因为它可能成为 LLM 训练数据的一部分。如果你无法访问具有[严格数据隔离保证](https://www.regie.ai/blog/generative-ai-data-privacy)的工具，那么无纪律的感觉编程可能会成为你知识产权的负担。

## 有效的感觉编程的最佳实践（在适当的时候）

值得注意的是，感觉编程实验的许多成功案例都来自经验丰富的程序员。他们不仅知道他们想要创建什么以及代码可以实现什么，而且他们还能够检查代码中的不一致和幻觉。如果你从未编写过代码或缺乏经验，你不能期望立即看到结果。

无论你是编码新手还是编码大师，以下是一些关于如何充分利用感觉编程实验的快速建议：
**制定计划：** 确保你对想要生成的内容有一个概念，包括所需的功能，而不是盲目地进行。随性编码并不是一个真正的沙箱；它是一条可以带你走向结果的道路。在提示你的 AI 之前，先在一个规范文件中概述功能。

**提供上下文：** 如果你能提供配置和规则文件来指导模型，你将降低 AI 模型偏离方向和产生幻觉的风险。

**迭代工作：** 一次处理一个功能，保持你的提示范围狭窄和具体。

**彻底测试：** 你可以使用 AI 自动生成的测试，以及人工/人工验证关键路径的组合。

**选择流行的技术栈：** 在网上有很多关于使用流行工具进行随性编码的指南。在获得更多经验之前，最好坚持使用这些工具，直到你对自己有信心。

**审查和重构：** 始终逐行审核 AI 输出，然后重构结构。

**监控兔子洞：** AI 可能会陷入生成无效代码的循环中。不要害怕回滚并尝试不同的提示方法。

**尝试多模态输入：** 屏幕截图可以增强提示的清晰度，而使用语音可能是一个有趣的实验，一旦你更有经验。

**检查氛围：** 在原型之外分享你的代码之前，让一位经验丰富的工程师审查所有内容。

## 随性编码的未来

在未来几年，随性编码有望从简单的文本提示演变为更直观的拖放式 [“随性设计”界面](https://andrewchen.substack.com/p/predictionsthoughts-on-vibe-coding)：可视化工作流程，你可以在其中绘制 UI 或映射数据流，而 AI 会在幕后填充代码。

随着 AI 模型变得更加专业化并与业务领域紧密集成，我们可以看到端到端的管道，将高级需求转化为可用于生产的应用程序。

对于开发人员来说，这意味着 [一个根本性的角色转变](https://www.nucamp.co/blog/vibe-coding-the-future-of-vibe-coding-how-aidriven-development-could-transform-programming-by-2030)：他们将不再键入每一行代码，而是精心制作精确的提示，管理生成的输出，并嵌入领域专业知识以保持系统的一致性。据预测，到 2030 年，AI 将自动化高达 80% 的日常编码任务，因此工程师将专注于架构、道德监督和跨团队集成。

我们还可以看到“随性”的进一步应用，例如 [事件随性](https://thenewstack.io/vibe-coding-is-here-but-are-you-ready-for-incident-vibing/)。

## 结论

随性编码降低了软件创建的门槛。它对于快速原型设计、个人项目和学习来说是一个改变游戏规则的工具。然而，它不是万能的：在安全关键、大规模或合规驱动的环境中部署 AI 生成的代码会带来重大风险。

未来需要一种平衡的方法，即在 AI 擅长的领域利用其速度，但在需要严格理解和问责制的领域应用传统的工程规范。知道何时拥抱随性，何时拿起你的 IDE，是在软件开发的下一阶段蓬勃发展的关键。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。