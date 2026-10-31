<!--
title: 为什么MCP服务器应该告诉智能体下一步做什么
cover: https://cdn.thenewstack.io/media/2026/10/47ca69a6-for-thumbnail-16.png
summary: AWS的James Ward认为MCP服务器不应仅被动返回数据，而应像对话中的参与者一样，主动为智能体提供下一步操作指南、追踪交互路径并进行评估优化，从而提升智能体的工作效率。
-->

AWS的James Ward认为MCP服务器不应仅被动返回数据，而应像对话中的参与者一样，主动为智能体提供下一步操作指南、追踪交互路径并进行评估优化，从而提升智能体的工作效率。

> 译自：[Why MCP servers should tell agents what to do next](https://thenewstack.io/aws-mcp-agent-observability/)
> 
> 作者：Matthew Burns

**许多 MCP 服务器只做一件事。** 智能体请求数据，服务器将数据返回。AWS 的 [James Ward](https://www.linkedin.com/in/jamesward/) 认为这留下了很大的提升空间。他告诉我，当服务器的运作方式不那么像数据库，而更像是对话中的另一个声音时，该协议的效果最好。

Ward 是 AWS 的首席开发者布道师，也是智能体 AI 基金会（Agentic AI Foundation）技术委员会的成员，该 Linux 基金会组织现在负责托管 MCP。上周在圣何塞举行的 AGNTCon + MCPCon 上，我和他进行了深入交谈，就在他和共同演讲者 Alexander Ioffe 准备发表关于将 MCP 从基础 API 转换为智能体集成接口的演讲前一天。

视频

“很多时候，我们的 MCP 服务器只是这些 API，比如‘获取我的客户’，这是一个好的开始，”Ward 说。“我将 MCP 想象成这场对话中的第三个人，或者第四、第五个人，这取决于你有多少个 MCP 服务器。”

在实践中，这意味着工具响应在传输数据的同时还携带了指导信息。它告诉智能体它刚刚做了什么、接下来可能想做什么，以及在哪里可以找到更多信息。

他阐述的另一半是可见性。Web 开发者可以追踪页面上的点击一直到数据库。“MCP 默认没有任何方法来实现追踪 ID，”Ward 说。

AWS 使用的变通方法相当低技术含量。在工具中添加一个会话 ID 参数，并告诉智能体在每次调用时传递它，这样就可以将各个调用串联成一个完整的旅程。第二个参数可以携带用户的提示词或其目标的摘要。然后，团队可以比较用户的意愿与智能体所走的路径，围绕它构建评估（eval），调整工具描述或参数，并衡量是否完成了更多任务。Ward 表示，AWS 为其自身开发者使用的 MCP 服务器构建了大部分这样的功能。

5 月份，AWS 向所有人开放了其 [MCP 服务器](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/)，并在 [9 月份添加了 Lambda 诊断功能](https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/)。在会议前发布的一篇[智能体 AI 基金会简介](https://aaif.io/blog/james-ward-thinks-your-mcp-server-could-use-some-work)中，Ward 描述了一个智能体一次获取一个客户记录的场景，因为服务器只提供了一个单记录工具。观察完整的旅程是团队发现该模式并构建批量工具来解决它的途径。

Ward 并未将 MCP 视为唯一的解决方案。他说，AWS 还提供 CLI 和 skills，部分原因是 MCP 的 OAuth 模型无法像 CLI 那样在 AWS 用户配置文件之间切换。哪种效果最好取决于模型、工具描述以及智能体如何发现工具，因此 AWS 会通过评估相互测试它们。

这些都不是什么稀奇的事情，Ward 心知肚明。“太阳底下无新事，”他说。观察旅程、复现它、衡量它并改进它。不同之处在于，现在的团队必须理解人类和智能体共同走过的路径，并测试对其工具的更改是否真正帮助他们完成了任务。