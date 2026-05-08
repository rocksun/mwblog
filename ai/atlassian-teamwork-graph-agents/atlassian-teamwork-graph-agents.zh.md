[Atlassian](https://www.atlassian.com) 希望开发者在 Claude Code 等工具中使用的自主且长时间运行的智能体能为每位用户提供服务。

在周三于阿纳海姆举行的 Team ’26 大会上，该公司推出了 Max，这是 Rovo Chat 中的一种新模式。Atlassian 的 AI 产品负责人 [Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 将其描述为“运行在云端、内置 Teamwork Graph 上下文的‘微型 Claude Code’”。

对于 Atlassian 而言——正如其许多竞争对手一样——它拥有的数据以及它能为智能体提供的上下文，正变得越来越重要，成为新兴智能体层的核心，而这一层目前仍处于剧烈的变动之中。

![](https://cdn.thenewstack.io/media/2026/05/7e02cc03-twg-mcp-vignette-final.gif)

对于 Atlassian 来说，这具体意味着将其 Teamwork Graph（这张涵盖了 Jira、Confluence、Jira Service Management 以及数十个关联 SaaS 工具中超过 1500 亿个对象和关系的图谱）开放给任何符合 MCP 协议的智能体。此外，还有一套全新的 Teamwork Graph 命令行工具和一组 MCP 服务器（均处于公开测试阶段），允许 Claude Code、IDE 编程助手（copilots）和其他第三方智能体查询支撑 Atlassian 自家 Rovo 平台的同一套上下文底层。

> Atlassian 的赌注是：智能体在客户数据架构中能访问的上下文，决定了它在企业中是否有用。

Atlassian 的赌注是：智能体在客户数据架构中能访问的上下文，决定了它在企业中是否有用。该公司愿意以此下注，甚至不惜让外部智能体进入其自身的图谱。

## 图谱如何运作

[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 在发布前的简报中告诉 *The New Stack*，Teamwork Graph 已经开发多年。他称其为“记录系统级别的质量”，并认为这是区分竞争对手的关键（尽管那些竞争对手通常也采取了非常类似的策略，将内部图谱视为在这个智能体时代的护城河）。

对于一家企业来说，这个图谱包含了多年的 Jira 工单历史、Confluence 页面和 Jira Service Management 事件，以及来自关联 SaaS 工具的信号。这些随后都通过人、项目、决策和文档之间的关系进行映射。

[](https://cdn.thenewstack.io/media/2026/05/9e1a79a2-twg-mcp-vignette-final.mp4)

Atlassian 通过一种名为 Cipher 的内部查询语言向智能体公开该图谱。在 Team ’26 上发布的工具允许智能体执行这些 Cipher 查询，以实现 [Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 所描述的“多跳遍历（multi-hop traversal）”，即跨图谱遍历各种关系。

相比于标准的检索增强生成（RAG），这种方案的卖点在于：能够基于关系进行推理的智能体可以找到所需内容，而无需将原始文本塞进上下文窗口。“上下文窗口不再拥挤了，”[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 说道。“你可以将推理能力用在真正需要的地方，而不仅仅是用于筛选一堆数据。”

一个新的公共网站 teamworkgraph.com 现已上线，首次允许客户将其自身的图谱可视化。

Atlassian 进行了一项内部基准测试，对比了具有 Teamwork Graph CLI 访问权限的 Claude Code 与没有该权限的同一智能体。Atlassian 表示，拥有图谱访问权限的版本减少了 48% 的 Token 消耗，并产生了准确率高出 44% 的结果，[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 将此归功于智能体遍历关系的能力，而非通过检索重建上下文。

![](https://cdn.thenewstack.io/media/2026/05/7c4a152b-img_3822-1024x768.jpg)

Atlassian 联合创始人 Mike Cannon-Brookes 在 Atlassian Team ’26 大会上。图片来源：*The New Stack*

## 开放护城河

Team ’26 的另一个新动态是 Teamwork Graph CLI 现已进入公开测试阶段，它为开发者、管理员和编程智能体提供了一个访问图谱的终端界面（谁能想到命令行工具会突然再次变得有趣？）。与此同时，符合 MCP 的 Teamwork Graph 工具也处于公开测试阶段，允许任何符合协议的智能体像 Rovo 一样查询图谱。

在会议前的媒体简报中，Atlassian 联合创始人兼 CEO [Mike Cannon-Brookes](https://www.linkedin.com/in/mcannonbrookes/) 表示，他相信“Teamwork Graph CLI 可能会成为最受客户欢迎的东西，我猜是因为它是免费的，这总是对他们有帮助，而且它以各种全新的方式释放了他们现有的图谱。”

> “我们从第一天起就是一家开放平台公司，所以我们从未想过限制某人只能使用一种东西。”
> ——[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/)，Atlassian

Atlassian 描述的一个实际用例是：一名开发者在 IDE 中运行 Claude Code，希望智能体知道哪些 Jira 工单和 Confluence 决策与他们正在编辑的文件相关联。如果没有这些新工具，开发者必须编写自定义的胶水代码来检索这些数据。但现在，智能体可以直接通过 MCP 查询图谱，并获得与 Rovo 相同的关联上下文。

“我们从第一天起就是一家开放平台公司，所以我们从未想过限制某人只能使用一种东西，”[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 说道。他指出，这允许高级用户在 Teamwork Graph 之上使用他们选择的智能体进行构建，而知识工作者则可以留在 Rovo 中，因为这里的上下文一直是默认配置。

通过代码智能功能，开发者可以要求 Rovo 查找代码库中尚未采用新按钮样式的所有位置。[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 说，Rovo 会搜索“超过 10 亿行代码”，并在几分钟内返回不符合规范的存储库。从那里，可以通过 Jira 中的智能体工作流（agents-in-Jira workflow）分配智能体来实施更改。

## 定价

目前，Rovo 操作是按席位授权的。客户根据其 Atlassian 计划获得一定数量的 Rovo 积分。超额费用尚未开启。

Max 正在转向一种不同的模式。Atlassian 计划根据变量和价值对 Max 的使用进行计费，费率表和超额计时将“相对很快”发布，[Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/) 说道。“你可能会要求一个 5 分钟的任务或一个 20 分钟的任务，”他认为定价必须随之调整。

当 *The New Stack* 问及在如此多公司转向按使用量计费模式的背景下，Atlassian 的整体定价策略时，[Mike Cannon-Brookes](https://www.linkedin.com/in/mcannonbrookes/) 指出，该公司希望“在定价上由客户主导”。他相信混合模式，即公司目前提供的产品，将按席位收费与 AI 使用积分相结合。

“以 AI 领域为例，我们的席位模式附带了慷慨的 Rovo 积分限制；在存储方面，附带了慷慨的索引对象和存储限制，还有一系列 Forge 限制等等。对于绝大多数客户，我们希望他们的使用量在他们支付的‘包络线’之内，”[Mike Cannon-Brookes](https://www.linkedin.com/in/mcannonbrookes/) 说道。

当然，他也承认，有些用户会达到这些限制，但如果一个用户向 TeamWork Graph 推送了数百万个对象，他们可能也愿意为从中获得的价值付费。

## 上下文层之战已经打响

当然，Atlassian 并不是唯一一家声称上下文图谱是差异化因素的公司。微软正在通过 Microsoft Graph 加上 Copilot Studio 讲述同样的故事，Salesforce 拥有 Data Cloud 和 Agentforce，而 ServiceNow 也在本周自己的活动中发布了一系列工具。