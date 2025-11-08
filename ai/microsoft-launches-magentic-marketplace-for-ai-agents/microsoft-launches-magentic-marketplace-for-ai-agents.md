<!--
title: 微软Magentic AI智能体市场重磅上线！
cover: https://cdn.thenewstack.io/media/2025/11/61978141-alex-shuper-rvrqqdweij0-unsplashb.jpg
summary: 微软研究院发布Magentic Marketplace，模拟AI智能体市场，测试协作、谈判与交易。旨在发现安全与偏见问题，强调人工监督，并改进LLM和协议。
-->

微软研究院发布Magentic Marketplace，模拟AI智能体市场，测试协作、谈判与交易。旨在发现安全与偏见问题，强调人工监督，并改进LLM和协议。

> 译自：[Microsoft Launches Magentic Marketplace for AI Agents](https://thenewstack.io/microsoft-launches-magentic-marketplace-for-ai-agents/)
> 
> 作者：Richard MacManus

微软研究院刚刚发布了一个用于研究智能体市场的开源环境，名为 [Magentic Marketplace](https://www.microsoft.com/en-us/research/blog/magentic-marketplace-an-open-source-simulation-environment-for-studying-agentic-markets/)。在该发布之前，我采访了微软研究院 AI 前沿实验室的董事总经理 [Ece Kamar](https://www.linkedin.com/in/ecekamar/)。

Kamar 的研究小组此前曾开发了 [AutoGen](https://microsoft.github.io/autogen/stable/)，这是一个智能体开发框架，已在 Python 开发者中广受欢迎——尤其是在 [构建多智能体 AI 系统](https://thenewstack.io/a-developers-guide-to-the-autogen-ai-agent-framework/) 方面。部分归因于这一成功，Magentic Marketplace 的开发受到了 AutoGen 的启发。

Kamar 告诉我：“AutoGen 是一个月前发布的微软智能体框架的一部分。因此，我们能够获得所有这些编程层并将其整合到微软产品中。现在，我们利用从 AutoGen 中获得的所有经验——人们使用 AutoGen 所做的事情——来思考智能体将如何发展。”

## 什么是 Magentic Marketplace？

Magentic Marketplace 的理念是允许研究人员模拟 AI 智能体的市场，以测试“智能体如何在真实世界市场动态下进行谈判、交易和协作。”该市场还将监测这些系统的安全性和公平性。

[![Magentic Marketplace 概述](https://cdn.thenewstack.io/media/2025/11/31cc8d96-magentic-marketplace1.jpg)](https://cdn.thenewstack.io/media/2025/11/31cc8d96-magentic-marketplace1.jpg)

*Magentic Marketplace 概述。*

尽管 Magentic Marketplace 是一个研究项目，但它日后很容易成为一个商业项目——类似于 AutoGen 如何演变为 [微软智能体框架](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/)（这是 AutoGen 与 Semantic Kernel 近期合并的结果，Semantic Kernel 是一个我曾在 [2023 年 4 月报道过](https://thenewstack.io/microsoft-semantic-kernel-for-ai-dev-a-chat-with-john-maeda/) 的 SDK）。

Kamar 说：“我们预计将会有公共市场出现。我们 [微软研究院] 作为研究部门，可能不会是构建这些市场的团队。但是……当你查看该领域的一些最新发布时，会发现它们都在为开始测试这些市场做准备。”

她补充道：“我个人认为，我们使用技术的许多方式都将以这些智能体为核心重新思考和设计。市场将是其中一个我预计将出现大量活动的领域。”

## “智能体社会”中的协议

像任何好的研究项目一样，对于 AI 智能体应该如何工作，存在一个工作理论。Kamar 在 2000 年代于哈佛大学攻读博士学位时，研究的正是 AI 智能体这一课题，她正在使用“智能体社会”一词来描述该项目的目标。

她说：“在这种‘智能体社会’的理念中，核心在于 AI 智能体汇聚一堂，互相交互、协作、谈判。此外，在人类监督下，真正揭示当我们拥有这些智能体时世界将是怎样的，以及身边有这些智能体如何能够解决我们在世界上存在的一些低效率问题。”

> “在这种‘智能体社会’的理念中，核心在于 AI 智能体汇聚一堂，互相交互、协作、谈判。”
> **– Ece Kamar，微软研究院**

研究的一个关键部分是测试通信协议，例如 [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP) 和 [Agent2Agent](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) (A2A)，以及新兴的支付协议。对于智能体商务来说，目前还没有一个默认协议——尽管 OpenAI 最近宣布了 [Agentic Commerce Protocol](https://openai.com/index/buy-it-in-chatgpt/) (ACP)，谷歌在九月份宣布了 [Agent Payments Protocol](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) (AP2)，而其他公司（如 Shopify）一直在使用 [MCP-UI](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/)。

Kamar 还预计将出现新的协议来帮助智能体协作，或者像 MCP 和 A2A 这样的协议将扩展到市场用例。例如，智能体以何种正确方式展示交易信息？

## AI 智能体模拟中的关键挑战和偏见

Kamar 表示，他们也认识到 AI 智能体带来的风险——例如安全性和偏见——她描述了他们迄今为止在市场模拟中遇到的一些挑战。

“我们正在看到的一件事是，尽管我们拥有这些通信协议 [MCP、A2A 等]，但驱动这些智能体的模型有时会陷入某种决策悖论。如果选择过多，它们在做出正确选择方面可能尚未那么有效。”

[![Magentic Marketplace 实际运行](https://cdn.thenewstack.io/media/2025/11/3a42a9b9-magentic-marketplace2.jpg)](https://cdn.thenewstack.io/media/2025/11/3a42a9b9-magentic-marketplace2.jpg)

Magentic Marketplace 实际运行。

该小组还观察到“出现了一些偏见”。

“例如，我们识别出的一种偏见称为‘提案偏见’。目前的模型倾向于快速出现的选项。就像，如果你是一个快速的智能体，无论你的提案是否最佳，你都会更受青睐。”

因此，尽管智能体能够在市场模拟中相互通信，但要使多智能体协作成为现实，还有大量工作要做。Kamar 指出，要从这些市场中获得最高水平的效用，“我们需要以不同的方式训练和构建这些智能体。”

她提到了他们迄今为止在模拟中遇到的一些技术问题。其中一个被她称为“工具空间干扰”，这基本上意味着智能体因 AI 工具的激增而感到困惑。她说：“目前，MCP 有如此多不同的工具，有时它们的命名方式相同，甚至命名约定尚未完善；我们发现，随着该协议的成熟，仍然存在问题。”

> Magentic Marketplace 已经揭示了“现有前沿模型在协作和谈判方面的局限性。”
> **– Kamar**

事实上，Kamar 的小组本身也构建了一个开源 MCP 工具，名为 [MCP Interviewer](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/)。她解释说，它“帮助开发者……对这些工具进行‘面试’，查看干扰问题，以便他们能更清楚地了解要引入哪些工具；并在实际系统中发生之前发现工具干扰等问题。”

第二个问题是技术栈的更深层——她指出“现有前沿模型在协作和谈判方面的局限性。”他们尝试让 LLM 相互协作以帮助智能体执行任务，结果发现模型的性能会随着这种协作而下降。

Kamar 说：“因此，作为一个团队，我们也在研究模型训练方式需要改变什么，以便这些模型能够在协作能力方面赋能更强大的智能体。”

## 平衡 AI 智能体自主性与人工监督

那些足够年长，还记得互联网“点com”时代的人会记得，人们花了数年时间才放心地在网页浏览器中输入信用卡信息进行在线购物。那么，要多久我们才能放心地将信用卡信息——甚至个人偏好——交给 AI 智能体呢？

Kamar 说：“我认为对于我们研究人员来说，最重要的是要尽可能地改进技术并清晰地阐释技术。当这些技术最终交到人们手中时，我们不是给予他们一个我们建造却不真正理解的东西；而是给予他们一个我们真正理解、经过测试、理解其不足并努力改进过的东西。”

她补充说，她的团队还考虑了在这些智能体系统中进行人工监督何时是适当的——在行业中更常被称为“人在环中”（human in the loop）。

> “如果我们要构建这些市场和生态系统，我们也可以投入时间去理解和构建这些层级，作为用户，我仍然拥有控制权……”
> 
> **– Kamar**

她说：“所以我认为也会有一个光谱，我们不会在第一天就实现完全的智能体自主性。你知道，没必要那样。如果我们要构建这些市场和生态系统，我们也可以投入时间去理解和构建这些层级，作为用户，我仍然拥有控制权——我仍在查看所有的交互，我仍在查看各种选项，我仍然可以询问智能体向我推荐的内容。”

在这次采访之前，我必须承认我不太确定微软为何要发布一个模拟市场而不是真实的市场。但 Kamar 说服了我，在公共市场上线之前充分测试智能体如何协作不仅是明智的，而且实际上，不先运行模拟是危险的！

此外，Magentic Marketplace 应该能帮助我们改进大型语言模型（LLM）、协议和 AI 工具，这些都是公司使公共智能体市场可行所必需的。