<!--
title: 超越氛围编程：MCP迈向生产的重重挑战
cover: https://cdn.thenewstack.io/media/2026/02/708f059c-vackground-com-up8ooq1pm2s-unsplash-scaled.jpg
summary: MCP面临上线挑战，主要体现在安全性、上下文窗口限制及工具集成。需加强安全、优化上下文管理，以实现广泛应用。
-->

MCP面临上线挑战，主要体现在安全性、上下文窗口限制及工具集成。需加强安全、优化上下文管理，以实现广泛应用。

> 译自：[Beyond the vibe code: The steep mountain MCP must climb to reach production](https://thenewstack.io/model-context-protocol-evolution/)
> 
> 作者：David Eastman

去年我没做的一件事就是参加任何 [模型上下文协议](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)（MCP）会议，很大程度上是因为我看不出为什么一个非常年轻的协议能够代表广阔的LLM世界。但随着人工智能发展的速度，MCP现在正在寻找健身房会员资格并检查其养老金计划。

上周参加在伦敦举行的 [MCP大会](https://www.mcp-conference.com/)（它们现在已遍布全球）让我深入了解了开发者在LLM和工具连接领域遇到的问题——以及工具供应商可能如何应对这些问题。显然，一些公司正在为他们的企业客户推销“安全MCP网关”或“受管MCP基础设施”，自然地，一些参观者正在寻找这些解决方案。

尽管MCP尚未完全确立自身地位，但它已经经历了一次“濒死体验”。

![](https://cdn.thenewstack.io/media/2026/02/53efb9a1-image-1024x377.png)

[Teo Borschberg (agment.ai) 的幻灯片](https://www.linkedin.com/in/teo-borschberg-94a44945/)

OpenClaw从未被直接提及，但它绝对是盛宴上的幽灵。MCP可能把门开得太大了——在我们完全理解安全隐患之前。（这里有些讽刺：OpenClaw实际上是一个MCP客户端应用程序——只是一个对调用原生MCP没有看法的应用程序。）

### MCP仍在自我探索

也许在这样一个快速发展的环境中，没有哪项单一技术有足够的时间或空间来妥善确立自身，这并不令人惊讶。在实施方面，MCP服务器仍主要是“内部的”，即在公司防火墙后使用。从快速的氛围编程解决方案到投入生产仍然是一个问题。该协议本应使现有服务的访问民主化，而且它也做到了。许多公司已尝试通过电子邮件连接传入的错误报告，并在Salesforce或JIRA中创建问题。然而，在那之后，事情就不那么清楚了。

我注意到“工具”和“技能”有时可以互换使用。从技术上讲，工具是单一用途的指令，而创建Claude代理技能只是创建一个包含 `SKILL.md` 文件的文件夹。该技能还可以包含资源和工具。但我正在想，这两个术语现在是否代表了“更多MCP”。

“A2A”在许多幻灯片上出现，但没有评论。提及Google的Agent-to-Agent协议可能是一种随意的方式，让演讲听起来更通用。我几乎没有看到提及Agent Communication Protocol (AGP)。

### “关于安全，某些方面”

不可避免地，关于安全的问题一直在困扰（或侵蚀）MCP服务器。尽管MCP旨在使从代理到数据之间的路径尽可能无摩擦，并将安全作为可选功能，但安全仍然存在。[Duncan Doyle](https://www.linkedin.com/in/duncan-doyle-9601642/) 就MCP与OAuth 2.1的安全性做了一个精彩实用的演讲；其核心原则（与其他许多演讲者一样）是“请实施安全”。

像往常一样，核心问题是信任。虽然MCP可以定义可以做什么，但OAuth面临着更艰巨的任务，即在工作流程中确定哪个实体被允许访问什么。Duncan引入了**安全诱导**的概念，这源于服务器在交互过程中通过客户端向用户请求额外信息时出现的问题。

你想得越多，情况就越糟。MCP服务器如何安全地向客户端请求你的GitHub凭据？你很快就会意识到MCP客户端必须支持用户的审批流程，并明确识别预期接收者。演讲中的演示展示了许多MCP授权步骤，并证明了正确实现的服务器并非一项快速任务。结束语“从未如此容易被劫持”既是时代的标志，也是对该技术的直接批评。

### 打开窗口

另一个重要的收获是，工具会占用上下文窗口的空间，所以返回100个“有用”的工具通常不是一个好主意。

简单地减少LLM在查询时被告知的工具数量可以节省空间。这引出了**渐进式披露**的概念，它最初听起来像是来自红磨坊的东西，但实际上是只用接下来需要的工具响应工具请求的想法。同样，查询返回过多的数据也会有助于填满长时间对话的窗口。我还听到了对“情景记忆”的提及。

几次演讲宣布“**代码模式**”是一种胜利——当你连接到MCP服务器时，Agents SDK会获取MCP服务器的模式，然后将其转换为TypeScript API，并附带基于模式的文档注释。

但正如我们在 [GSD](https://thenewstack.io/beating-the-rot-and-getting-stuff-done/) 中看到的，如果LLM能够编写足够的笔记供其他子代理拾取和阅读，上下文窗口大小问题就可以持续避免。

### 聊天中的买卖

“ChatGPT是现在最重要的平台”这句话并没有启发我的开发者思维，但它应该会引起一些关注。ChatGPT应用是我 [去年年底谈到的](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/) OpenAI技术的确定名称，它们显然旨在取代网络。其理念是MCP服务器实际上是品牌或企业服务。在这里，发现是驱动力，一次工具调用可能会带来购买披萨的机会。处理支付存在一个固有的困境：如何在减少摩擦的同时确保安全？这里我们又回到了安全问题。

![](https://cdn.thenewstack.io/media/2026/02/8b19f4f2-image-1-1024x454.png)

*[Aaron Koivunen，柏林MCP社区](https://www.linkedin.com/in/aaron-koivunen/)*

但毫无疑问，当用户在ChatGPT上对话时，没有上下文切换，而且大多数任务的学习曲线都非常短。

### 结论

无论你如何做，构建服务并以代理友好的方式公开它仍然是开发者的工作。但是，在上下文窗口大小有限且安全考量并非总是完全实施的情况下，MCP显然有几条可以成功发展的道路。也许通过一些严格的锻炼，这种“中年发福”可以被阻止。

最后，引用 [**Teo Borschberg**](https://www.linkedin.com/in/teo-borschberg-94a44945/) 的宝贵建议，以下是启动你的第一个内部MCP实施的一些提示：

*   选择一个人们经常提问的内部系统
*   构建一个具有只读访问权限的MCP服务器
*   将其交给五位非工程师人员