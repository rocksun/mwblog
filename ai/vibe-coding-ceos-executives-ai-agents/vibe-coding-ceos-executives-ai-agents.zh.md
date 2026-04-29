虽然软件开发人员似乎已经全面采用了 AI 编程助手，但组织的业务端——C 级高管和职权链上的其他高级管理人员——也正在采用这些工具来“[氛围编程](https://thenewstack.io/beginners-guide-to-vibe-coding/)”各种智能体和生产力应用。

这种趋势涵盖了从简单的流程自动化到服务数百名用户的完整生产系统。所使用的工具包括 [Claude](https://thenewstack.io/anthropics-claude-interactive-visualizations/)、[Cursor](https://thenewstack.io/cursor-3-demotes-ide/)，以及这些高管已在使用的平台中日益增加的 AI 功能。其动机从对 IT 排队的失去耐心到对技术潜力的真正好奇不等。而结果比这些热情所暗示的更加多样化。

## 14万行代码，仅手动修改10行

[Moshe Bar](https://www.linkedin.com/in/moshebar/) 是 [Codenotary](https://thenewstack.io/codenotary-adds-background-vulnerability-scanning/) 的 CEO 兼联合创始人，他从 2025 年 3 月开始为 IBM 3270 大型机终端用户构建了一个电子公告板系统 (BBS)。他并不是一名程序员。他指定了数据库结构——包括用户、消息、主题、帖子、聊天的表格——然后将其余工作交给了 Claude。该系统目前运行着 14 万行代码。Bar 亲自编辑了其中大约 10 行。

“在如此短的时间内完成这样一个规模、可靠性和实用性的项目，在仅仅两年前是不可想象的，”Bar 说道。

该系统运行在 moshix.tech:3270，拥有 500 名用户，数千个活跃讨论，并且从未宕机，他告诉 *The New Stack*。Bar 每八周通过 Claude 进行一次安全审计。他开源了代码，并表示其他人此后已经据此创建了自己的 BBS 实例。

Bar 亲自编辑的那 10 行代码是什么？那是他在一次跨大西洋飞行中，由于 Cursor 达到速率限制超时，他手动更改的菜单文本。自从完全转向使用 Claude 后，他就再也没动过源代码。

3270 协议——一种来自 1970 年代初期的晦涩、位精确的 IBM 标准——一直是唯一的持续挑战。Claude 偶尔仍会退回到 Unicode 或放错光标位置，这些问题 Bar 已经纠正了数百次。“你就像是在面对一个拥有博士学位的幼儿园小朋友，”他说道。但该应用程序仅运行在 23 MB 的内存上，一年多来从未发生过安全事故。据 Bar 估计，按照传统方式构建该系统将耗资巨大：需要三到四名资深开发人员，每人年薪 40 万至 50 万美元。

## 两次构建应用的 CEO

[OutSystems](https://thenewstack.io/ai-agents-need-more/) 的 CEO [Woodson Martin](https://www.linkedin.com/in/woodsonmartin/) 对他的氛围编程实验采取了更结构化的方法。他在团队创建的 [MCP 服务](https://thenewstack.io/mcp-maintainers-enterprise-roadmap/)之上构建了一个个人移动应用包装器——他并行构建了两次，一次使用 OutSystems 自家的 AI 编程工具 [Mentor](https://www.outsystems.com/low-code-platform/mentor-ai-app-generation/)，另一次使用 Claude，两次都连接到同一个后端。

“我受够了向那些本该替我开发的人解释需求，”Martin 说道。“我当时想，‘我自己来吧。’”

这个应用是一个个人幕僚系统，它将客户账户情报——购买信号、网站活动、内部数据——整合到一份会前简报中，他可以通过手机调取。它取代了以往长达 45 分钟的 PowerPoint 会议以及销售团队的多次准备会议。

Martin 还利用一个名为 [V2MOM](https://www.salesforce.com/blog/how-to-create-alignment-within-your-company/) 的目标设定框架来运营公司（借鉴自他曾工作过的 Salesforce），他的团队后来将其产品化为一项 MCP 服务。在进行高管一对一面谈之前，他会查询该服务以发现个人目标与公司目标之间的对齐差距。围绕该框架构建的智能体层现在有助于在全公司范围内推广组织变革。

在 Codenotary，Bar 对其工程部门的任务源于他使用 AI 辅助编程的经验；他告诉 *The New Stack*，三四个月前，他宣布公司未来的所有开发将仅限使用大语言模型（LLM）。他的理由很简单——云计算将产品上市时间从三年缩短到一年；而大语言模型再次将其缩短到三个月。

“如果你不能在三个月内从零开始推出一个新的应用程序，你可能已经错失了市场，”他说道。

当被问及在成功“氛围编程”出一个 BBS 后是否觉得自己像个程序员时，Bar 说：“不，我不这么认为。遗憾的是，我不这么认为，因为当我看到代码以及它实现的某些功能时，我完全不知道是怎么回事，一点都不知道。”

## 亲身实践

其他高管正在较小规模上进行尝试，但意图相似。AI 编排平台 Zapier 的联合创始人兼 CEO [Wade Foster](https://www.linkedin.com/in/wadefoster/) 描述了如何在 Cursor 中利用 Zapier SDK 构建个人 AI 幕僚。“SDK 处理我在工作中使用的每种工具的身份验证，”Foster [在 LinkedIn 上写道](https://www.linkedin.com/pulse/how-i-built-my-ai-chief-staff-zapier-sdk-wade-foster-rudbc/)。“编程智能体处理其他一切。我只需要描述我想要什么。”

Anaconda 的外部沟通经理 [Jessica Stefanowicz](https://www.linkedin.com/in/jstefanowicz/) 在 Claude 中“氛围编程”了一个奖项追踪仪表板——这是她的第一个此类项目。该工具每周自动更新，监控申请截止日期和提交要求，并根据具体的业务更新和产品推荐适合的奖项计划。它取代了每周约一小时的手动工作。

为客户服务和运营提供平台的 [Front](https://front.com/) 公司的首席营销官 [David Slater](https://www.linkedin.com/in/slaterdavid/) 表示，他利用 Claude 构建了一个双智能体系统，用于管理 90 天周期内的 50 到 70 个目标与关键结果 (OKR) 项目。一个智能体负责为每两周一次的沟通做准备，标出需要注意的领域并在会议前为负责人生成问题；第二个智能体在评审完成后，生成针对三个不同受众（产品、销售和高管团队）的定制状态报告。过程中没有编写任何代码。

“我不是技术用户。我不是通过写代码来构建这些智能体的，”Slater 告诉 *The New Stack*。“但这个系统从根本上改变了我管理部门核心运营节奏的方式。”

## 怀疑论者自有其道理

关注这一趋势的分析师们并非一致看好。

Forrester 分析师 [Andrew Cornwall](https://www.linkedin.com/in/acornwall/) 证实，非技术高管确实正在构建重要的 Web 应用，但也列举了风险：氛围编程的应用通常没有经过抗攻击加固，往往缺乏满足审计要求的控制措施，并且经常在没有预算或维护计划的情况下被丢给 CIO 或 CTO。在最糟糕的情况下，高管使用了未经批准的 AI 服务商并泄露了公司数据。

“如果氛围编程者及其用户了解其应用的局限性，它们并不比他们过去构建的电子表格风险更高。”他指出，更难的问题在于，一个看起来很专业的应用可能会掩盖它是经过专业支持的，还是仅靠提示词维持的。

他的 Forrester 同事 [Ken Parmelee](https://www.linkedin.com/in/kparmelee/) 补充了两个质疑点。首先，高管们通常并非独自构建——通常会有 IT 人员参与，尽管高管在内部沟通中揽下了功劳。其次，更根本的是，大多数非开发人员会遇到瓶颈。“非开发人员不是系统思考者，”Parmelee 告诉 *The New Stack*。一旦项目需要数据库、持久化内存或后端集成，大多数人就无法独立推进。

“他们可以做非常简单的应用或流程，”他说道，“但很多时候这并不等同于真正的价值。”

Constellation Research 分析师 [Holger Mueller](https://www.linkedin.com/in/holgermueller/) 表示，他看到了怀疑者忽视的一个重要优势：高管构建自己的自动化工具不会占用开发预算或工程能力。“企业其他部分的‘项目仍按计划进行’，”他说道。

与此同时，Futurum Group 分析师 [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/) 表示，他的公司观察到智能体编程（如氛围编程）正在迅速向外扩张。

根据他们近期对 818 名数据专业人士进行的决策者调查，75% 的人已经在使用生成式和智能体 AI 工具，将更多时间花在业务问题上，而非编程流水线上。

Shimmin 指出，他们并不孤单。

“从轶闻来看，我们在非 IT 专业人士中也看到了同样的加速和扩张，尤其是高管，”他告诉 *The New Stack*。“不，这些人并不是在传统意义上编写软件。在光谱的一端，他们正在自动化各种任务以释放时间和精力。在另一端，他们正在利用这些工具推动变革并探索新机会。高管们不再是召开会议讨论新想法（例如新产品或修订后的工作流），而是正在构建自己的工作原型来压力测试他们的想法，如果成功，通过将这些早期资产交给 IT 进行完善和实施，从而缩短上市时间。”

## 新的门槛，还是特例？

Bar 对自己在分布中的位置有着清醒的认识。“考虑到应用的范围，我认为自己有点像个特例，”他说道。据他观察，大多数氛围编程者都是在解决特定的痛点——即一个小型、定义明确的应用。服务于数百名用户的完整系统还是很少见的。

但可能性的门槛正在不断移动。Bar 表示，他正在重新审视几年前的一次谈话，当时他自信地告诉邻居，对开发人员的需求将永远强劲。

“我开始觉得也许那是个错误，”他说道，“因为我开始认为，我们或许正在慢慢走向这种对开发人员过度需求局面的终结。”

[Gene Kim](https://www.linkedin.com/in/realgenekim/) 在他的书 *[Vibe Coding](https://www.amazon.com/Vibe-Coding-Building-Production-Grade-Software/dp/B0FPGHVGD8/ref=sr_1_2?adgrpid=186412553677&dib=eyJ2IjoiMSJ9.v9_Oe2RCDcAJ1OxHYNXt94yT_JuJdsvdiFMM0rbLvkbqNj9dVfQ-ebhVYgSKtPpYuJ4PAczgdFU6FJx-NuIQAXT5rplixZ3cuZIzrp5fYA2ht8tnEHeLh96-yZeo9zeGb3DpIKNndinCre3IUqz-fLTnVVpiwJa-zwIpYu9RwgKAsji1QNdMcDtB4SiegYLlC-dYBgO-LyEKUtbXiAZuTw.D-HcSIfeZ1PqfnRNle99tLFaI4X4TrlpzXYYsZPTln0&dib_tag=se&hvadid=779657810078&hvdev=c&hvexpln=0&hvlocphy=9007907&hvnetw=g&hvocijid=15607065160011506336--&hvqmt=e&hvrand=15607065160011506336&hvtargid=kwd-2435698919933&hydadcr=16400_13457160_8572&keywords=gene+kim+vibe+coding&mcid=a6a8db8d14f13713be7831ec62db55c6&qid=1777292464&sr=8-2)* 中对这个[时刻](https://www.linkedin.com/in/realgenekim/)进行了宏观的描绘：“我们正在见证一场软件革命，它可能会让 1990 年代的互联网繁荣看起来像是一场热身赛。”

在去年接受 *The New Stack* 采访时，Kim 表示 AI 编程代表了一场“[比 DevOps 大 10 到 100 倍](https://thenewstack.io/devops-pioneer-vibe-coding-100x-bigger-than-devops-revolution/)”的变革——他正赌上自己的名声，押注于“[氛围编程的潜力](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/)”。

那些在业余时间进行氛围编程的高管们，可能正是这场浪潮的最前沿。