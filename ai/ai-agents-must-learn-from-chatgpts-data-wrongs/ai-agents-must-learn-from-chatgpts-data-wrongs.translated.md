# AI Agent 必须从 ChatGPT 的数据错误中吸取教训

![Featued image for: AI Agents Must Learn From ChatGPT’s Data Wrongs](https://cdn.thenewstack.io/media/2025/03/e35b1022-gustas-brazaitis-xnky-cu20d4-unsplash-1024x683.jpg)

[Gustas Brazaitis](https://unsplash.com/@gustasbrazaitis?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/turned-on-macbook-pro-xNKy-Cu20d4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 发布

大型语言模型 (LLM) 树立了一个危险的数据先例，进入了人工智能 (AI) 时代。ChatGPT 和其他生成式平台在未经用户同意或补偿的情况下训练信息，从而造成了重大的版权和所有权问题。输出是“新的”，但输入是从未公开的来源复制和粘贴的。

这是一个数据权利问题，我们必须在 AI Agent 时代来临之际解决。尽管 Agent 有望成为个人和专业任务中的超人助手，但如果我们继续创建对知识产权漠不关心的黑盒，它们将不值得信任。

相反，尤其是在早期阶段，我们[必须首选能够跟踪信息、识别输入并奖励贡献者的基础设施](https://thenewstack.io/why-infrastructure-must-be-serverless-in-the-ai-age/)。这就是我们如何从 ChatGPT 的数据错误中吸取教训，并使新一波的 Agent 能够在验证、许可和隐私为核心的情况下运行。

**LLM 树立了一个危险的数据先例**

即使 Claude、ChatGPT 或 Gemini 生成的内容感觉是原创的，但实际上也是从数十亿个数据点中抓取的，没有明确的许可或对所有者的后续补偿。这些平台本质上是获取受版权保护的材料，在未经同意的情况下继续前进，并且未能注明来源。

更糟糕的是，我们通常不知道这些模型是如何做出决定的。它们是封闭[源代码，数据](https://thenewstack.io/decoding-kafka-why-its-worth-the-complexity/)进入，命令输出，并且对中间发生的事情没有任何透明度。这种黑盒[方法会产生道德和实践](https://thenewstack.io/microsoft-takes-practical-approach-to-kubernetes-management/)问题。

我之前将模型比作人类，因为它们吃什么就是什么。如果我们只吃垃圾食品，我们就会变得迟缓。如果 Agent 只消耗版权和二手材料，它们就会不准确、不可靠，并且是通用的而不是特定的。它们的[数据“饮食”](https://crypto.news/ai-agents-need-better-data-diets-opinion/)决定了性能，我们不能期望从建立在有问题输入之上的系统中获得高质量的输出。

一个新时代[需要一种新方法](https://thenewstack.io/why-you-need-a-centralized-approach-to-monitoring/)。[AI Agent 有机会从一开始就将数据](https://thenewstack.io/agentic-ai-for-enterprises-4-key-benefits-driving-innovation/)权利融入其中，通过利用区块链来跟踪信息，并利用强大的数据基础设施来决定其使用。通过[将数据来源和尊重构建到基础中](https://thenewstack.io/distributed-data-not-apps-build-the-foundation-for-web3/)，我们可以为 Agent 提供经过同意的信息，并让用户参与到它产生的价值中。

**使用基础设施构建数据防护栏**

好消息是，现在改变数据现状还为时不晚。正在出现三个技术防护栏，以确保 Agent 行为朝着透明的基础设施和改进的数据权利方向发展。

首先，我们需要清晰的管道来跟踪归属。区块链是另一项备受炒作但又被误解的技术，它在这方面有所帮助。基于区块链的[数据框架创建了 Agent 访问的信息的不可变记录](https://thenewstack.io/a-look-at-datastaxs-ai-and-push-cache-for-data-access-at-scale/)。与当今不透明的采购不同，我们可以使用可验证的凭证系统和去中心化标识符[将问责制构建到基础设施中](https://thenewstack.io/building-an-integrated-infrastructure-for-real-time-business/)。例如，[Kite AI](https://gokite.ai/) 正在构建一个模块化的第 1 层区块链，用于跟踪归属智能的证明。这样，开发人员可以配置激励措施，协调跨子网的协作，并[跨自定义数据](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/)、模型和 Agent 构建理想的 AI 技术堆栈。

其次，隐私保护计算技术允许在不暴露数据的情况下进行数据处理。零知识证明、同态加密和[安全多方计算创建了同意的基础，并保持数据](https://thenewstack.io/container-security-a-troubling-tale-but-hope-on-the-horizon/)安全。这些技术在各种区块链系统和可信执行环境 (TEE) 计算平台中实施，可以在不泄露敏感数据的情况下对其进行计算。
第三，我们需要通过适当的信用[让这些系统重拾信心](https://thenewstack.io/devs-need-system-design-tools-not-diagramming-tools/)。如果使用了用户信息或受版权保护的材料，代理及其各自的模型必须奖励署名，而不是忽略署名。[Story Protocol](https://learn.story.foundation/intellectual-property-101) 是另一个 web3 项目，旨在推进这一概念——使用区块链让创作者能够确立对其作品的所有权，设定作品的使用规则，并确保他们在内容被使用时获得报酬。[CARV ID](https://eips.ethereum.org/EIPS/eip-7231) 实现了类似的目标——将在线身份与单一的事实来源联系起来，用户可以在这里决定他们的信息是否可以用于模型训练以及是否需要付费。这不仅让用户参与到人工智能革命中来，还在一定程度上恢复了对整个系统的信任。

**信任是代理能否被采用的关键**

如果代理[不能赢得信任](https://thenewstack.io/dont-trust-security-in-ai-generated-code/)，它们将在第一个障碍前止步。请记住，这些平台承诺在各种情况下提供自主的、智能的帮助。如果我们的行业继续窃取数据，那么在家庭或工作中，主流的接受是不太可能的。

我们已经看到了这样做的危险，三星的会议记录和源代码在 ChatGPT 中[使用后泄露](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/)。这种[数据处理方式对于](https://thenewstack.io/if-your-data-isnt-answering-why-it-isnt-working-hard-enough/)公司专有数据以及受 GDPR 或 HIPAA 约束的组织来说是不够好的。用户和企业都需要知道，他们的信息不仅在这些模型中是安全的，而且还使用了顶级的隐私标准和后端防护措施。

[正确使用数据也有运营上的好处](https://thenewstack.io/fermyon-cloud-save-your-webassembly-serverless-data-locally/)。构建在数据主权基础设施上的 AI 代理通过访问更高质量、适当署名的信息，可以产生更[可靠的结果](https://thenewstack.io/developers-guide-to-the-built-in-tools-of-openai-agents-sdk/)。它们还可以被审计，以发现偏差和不准确之处。也许最重要的是，它们通过透明地运作而不是作为难以理解的黑盒来赢得信任。

代理的成功取决于创建一个系统，在这个系统中，数据不仅丰富且经过认证，而且还通过可操作的指标进行丰富，并通过无需信任的共识进行验证。当代理访问高质量、经过验证的信息——并且仅在获得明确的用户同意和署名机制的情况下——它们才能实现其崇高的目标。现在是从 ChatGPT 的数据错误中吸取教训，并开辟一条通往安全且经过验证的代理基础设施的新道路的时候了。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。