<!--
title: Claude Code 与个人软件的兴起
cover: https://cdn.thenewstack.io/media/2026/04/44de4ae7-adri-ansyah-qlrxiy534ny-unsplash-1.jpg
summary: 本文介绍了 Claude Code 催生的“个人软件”浪潮。通过 AI 赋能，非技术人员也能低成本开发定制化工具，替代传统 SaaS 解决特定业务痛点，实现了软件开发的民主化。
-->

本文介绍了 Claude Code 催生的“个人软件”浪潮。通过 AI 赋能，非技术人员也能低成本开发定制化工具，替代传统 SaaS 解决特定业务痛点，实现了软件开发的民主化。

> 译自：[Claude Code and the rise of personal software](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/)
> 
> 作者：Jessica Wachtel

说 [Claude Code](https://thenewstack.io/claude-code-desktop-redesign/) 正在积极改变软件的构建方式已不是新闻。但真正的新闻是**谁**在构建软件。[软件开发](https://thenewstack.io/innovating-software-development-with-ai-and-ml-pros-and-cons/)正从专业软件开发者转向每一个人。Anthropic 的智能体编程工具 Claude Code 让软件开发变得像描述你想要什么一样简单。其易用性已是公开的秘密。在 2025 年 5 月推出后，Claude Code 的[年化收入在 11 月达到了 10 亿美元](https://aibusinessweekly.net/p/claude-ai-statistics)。到 2026 年 2 月，这一数字翻了一倍多，达到 [25 亿美元](https://aibusinessweekly.net/p/claude-ai-statistics)。

Claude Code 正在彻底改变企业工程团队的运作方式。更具趣味性的是，它如何使软件开发民主化，并将这些相同的功能带给以前依赖 SaaS 和工程团队的部门。现在，营销、财务和销售等领域的人员也可以构建软件。一个围绕着“任何人都可以创建所需软件”这一新颖想法的完整生态系统正在兴起。

Claude Code 并非特例。其他非技术应用构建平台也随之迅速增长。[Lovable 在一年内增长了 2,800%](https://getmocha.com/blog/ai-app-builder-statistics)，[Replit 增长了 15 倍](https://getmocha.com/blog/ai-app-builder-statistics)。构建软件的渴望已经远远超出了专业开发者的范畴。

欢迎来到个人软件的兴起时代。但不要被“个人软件”这个词所迷惑。个人软件是指为满足个人、系统或团队的独特需求而开发的任何软件。这包括惠及个人和企业的软件。Retool 最近的一项调查发现，35% 的公司已经用自建工具替换了至少一个 SaaS 工具，78% 的公司预计在 2026 年会构建更多工具。Retool 的 CEO David Hsu 简单地总结道：董事会的默认问题正在从“我们该买什么？”转变为“我们能直接造一个吗？”

## 那么用 Claude Code 编写的个人软件是什么样的？

它就像 PointFive 的云与 AI 效率负责人 Taylor Houck 告诉 *The New Stack* 的那样，他使用 Claude Code 在不到一周的时间内构建了一个解决方案。这是一个解决他每天都会遇到、且现有软件无法解决的问题，而且这个问题还没大到值得花钱聘请工程师团队来构建定制工具的程度。

Houck 的团队运行着一个依赖于人工的内容工作流：有人填写表单；一名团队成员获取这些详细信息，进行验证并起草内容；该草稿被粘贴到共享的 Google 文档中，并发送电子邮件给贡献者审阅；贡献者反馈意见；团队进行修改；获得批准后，有人手动将其上传到 CMS。虽然流程简单明了，但每一步都是瓶颈和潜在的故障点。工作流虽然可行，但无法同步高效运作。

如果 Houck 没有使用 Claude Code 将流程自动化，这个工作流原本会一直保持现状。但他做到了，现在流程已完全自动化。一旦有人填写表单，Webhook 就会触发一个托管在 AWS Lambda 上、由 DynamoDB 数据库支持的智能体系统。该系统验证提交内容、起草内容、生成审阅链接并自动发送邮件给贡献者。贡献者进行审阅、提出修改建议或直接批准。每个操作都会自动触发工作流中的下一步，没有人需要等待他人。一旦获得完全批准，只需点击一下，即可通过直接的 CMS 集成将其发布到网站上。

整个解决方案的构建时间不到一周，包含 130 个文件和 85,000 行代码，100% 由 Claude Code 构建。

这个软件很简单，甚至有些枯燥。但与此同时，它在以前绝不可能存在。不是因为想法太复杂，而是因为为仅一个团队构建如此定制化的东西在经济上从未可行过。传统的软件开发需要数月的工程时间、工资和基础设施成本。对于这样一个利基问题，账算不过来。“以前这在经济上根本不可行，” Houck 说道，“这原本需要一个工程师团队花费大量时间来构建。现在，它的运行成本每月不到 5 美元，而我是在每月 200 美元的 Claude 订阅费内完成构建的。”

Houck 并不是开发者。他形容自己是一个在云基础设施背景下“懂点皮毛但足以搞出名堂”的人，而非软件工程出身。他并不具备编写代码的专业知识，但在 Claude Code 的帮助下，他指导了应用的开发。在写下第一行代码之前，他与 Claude 在规划模式下花了几个小时定义需求、讨论架构并对决策进行压力测试。Claude 甚至部署了应用程序。对于这次经历，Houck 说：“我给了 Claude AWS 凭证，它就帮我完成了所有部署。我不需要进行任何点击操作，也不需要手动在 AWS 中做任何事情。”

即使已经构建了这么多东西，Claude Code 仍将为 Houck 和他的团队带来更多益处。该应用程序目前依赖于两个第三方 SaaS 工具：用于表单的 Typeform 和用于网站的 Webflow。他已经使用 Claude Code 亲自重构了这两个工具，并准备将其推向生产环境。他现在正围绕他的个人软件重建 SaaS 技术栈。

在谈到如何开始使用 Claude Code 时，Houck 说：“总会有我从未想到的用例。我们每个人都有自己的经验和技能组合。利用你独特的视角，将这些工具视为力量倍增器。”

这种影响超出了个人生产力的范畴。Houck 认为 Claude Code 提升了整个劳动力队伍的水平。“使用这些工具的个人贡献者现在成了经理，有团队的经理现在成了总监。几乎每个人都可以使用所有这些工具。”

## 个人软件中正在出现的模式

Houck 并不孤单。Livesport 的产品负责人 Ondrej Machart 在六个月内使用 Claude Code 构建了 13 个项目。他在 Medium 文章[《13 个改变了我产品经理角色的 Claude Code 项目经验教训》](https://medium.com/@ondrej.machart/13-claude-code-projects-that-changed-my-product-manager-role-over-the-last-6-months-7057b9045d51)中，写到了如何完全使用 Claude Code 构建一个原生 iOS 应用、一个帮助公司高层做出重大产品整合决策的工具，以及一个个人任务追踪器。

Machart 的应用起初并非始于 Claude Code。他曾尝试过 Replit、Lovable 和其他氛围编程工具，但没有一个能提供他所需的功能。在同事的建议下，他开始在终端中使用 Claude Code。他利用晚上和深夜的时间花了两个月学习窍门，驱动力并非一夜致富，而是构建一些人们可能真正会用的东西。

他的第一个项目是一个帮助家长寻找附近游乐场的原生 iOS 应用，最终成功上线 App Store，并集成了订阅模式和第三方 API。他写道：“我没有变成工程师，也不打算成为工程师。但在理解其他领域和范畴方面，我变得更加‘T型化’。这很有价值，因为它带来了同理心。”

与 Houck 一样，Machart 也不是软件工程师。这两个人都没打算构建独角兽（至少目前还没）。他们都需要无法获得的软件，因此他们使用 Claude Code 解决了问题。Claude Code 取得了成功。以前那些解决起来没有意义的问题，现在都变得可以解决了。Claude Code 不仅让软件开发变得更快，还让它变得个人化。