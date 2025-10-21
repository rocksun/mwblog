<!--
title: Block狂飙！两月让1.2万员工变身AI高手
cover: https://cdn.thenewstack.io/media/2025/10/9dfa3b0a-alex-kotliarskyi-qbpzgqemskg-unsplash-1.jpg
summary: Block公司8周内为1.2万员工部署AI代理，通过易用性、安全性、多模型及社区支持，大幅提升效率，赋能全员。
-->

Block公司8周内为1.2万员工部署AI代理，通过易用性、安全性、多模型及社区支持，大幅提升效率，赋能全员。

> 译自：[How Block Got 12,000 Employees Using AI Agents in Two Months](https://thenewstack.io/how-block-got-12000-employees-using-ai-agents-in-two-months/)
> 
> 作者：Darryl K. Taft

RALEIGH, N.C. — 尽管大多数公司仍在探索如何让其开发者有效使用AI编码工具，[金融科技](https://thenewstack.io/the-staging-bottleneck-microservices-testing-in-fintech/)公司[Block](https://block.xyz/)在八周内就为其全部12,000名员工部署了[AI代理](https://thenewstack.io/ai-agents-and-their-life-cycle-what-you-should-know/)。

在上周于此地举行的[All Things Open 2025](https://2025.allthingsopen.org/)大会上，Block工程副总裁Angie Jones解释了公司是如何做到的。

[![](https://cdn.thenewstack.io/media/2025/10/f8a79e6a-pxl_20251014_143224926-1-1.jpg)](https://cdn.thenewstack.io/media/2025/10/f8a79e6a-pxl_20251014_143224926-1-1.jpg)

## 小处着手

和许多科技成功故事一样，这个故事始于一位沮丧的工程师。Jones在她的演讲中说，Block的首席[机器学习（ML）](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/)工程师Bradley表示，他厌倦了那些只能生成代码片段的AI工具。他说，他想要的是能真正做事的东西——自动化复杂的开发任务，而不仅仅是建议下一行代码。

当[OpenAI](https://openai.com/)推出[函数调用](https://thenewstack.io/getting-started-with-function-calling-in-llms/)功能时，Bradley和一个小团队开始尝试自动化他们开发工作流中的部分环节。实验成功了，但他们很快就遇到了扩展问题。由于没有标准，为不同的API构建集成变得令人头疼。每一个新工具都意味着定制代码和维护问题。

随后，[Anthropic](https://www.anthropic.com/)联系了Block，介绍了名为[模型上下文协议（MCP）](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/)的东西——这是一个用于将AI代理连接到工具和数据源的开放标准。Block很喜欢这个想法，成为了启动合作伙伴，并重写了他们的内部代理（“[Goose](https://github.com/block/goose)”），使其与MCP协同工作。

## 偶然的发现

然而，在为工程师构建Goose的过程中，团队意识到他们可以让它为公司里的每个人服务。

“我们开始思考，如果我们能让它为所有12,000名员工服务，那会怎么样？”Jones说。这听起来雄心勃勃。大多数员工从未见过命令行，更不用说管理[API密钥](https://thenewstack.io/why-your-api-keys-are-leaving-you-vulnerable-to-attack/)了。

最初的尝试都失败了。非技术员工不知道如何安装软件。那些设法安装了的人又卡在认证流程上。Jones表示，整个体验都是为开发者设计的。

## 让它为普通人工作

然而，团队停止了像工程师一样思考，开始像他们的用户一样思考。

首先，他们让软件易于安装。下载文件、解压缩并将其拖到“应用程序”文件夹的整个过程对许多员工来说都很陌生。因此，他们将Goose添加到了内部软件中心。现在，它会在每台公司笔记本电脑上自动安装和自动更新。

“所以，如果你有Block的笔记本电脑，你就有Goose。它就是能用，”Jones说。

接下来，他们解决了“我应该使用哪个模型”的问题。他们没有强迫每个人使用一个AI模型，而是让员工自己选择。市场营销人员倾向于选择[ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/)进行写作。工程师则坚持使用[Claude](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/)进行技术任务。这种灵活性使得不同团队的采用变得容易得多。

“我们允许员工从OpenAI、Anthropic、[Google](https://cloud.google.com/?utm_content=inline+mention)、Meta提供商中选择，”Jones说。“这赋予了人们选择的权力，使得在各个领域中的采用变得容易得多。”

也许最大的挑战是安全性。正如[Jones所指出的](https://thenewstack.io/whos-afraid-of-the-queen-of-devrel-angie-jones-of-block/)，“Block是一家金融科技公司，这意味着Square和Cash App，对吧？所以，我们处理很多法规。我们必须非常安全。”他们没有让人安装随机工具，而是“成立了一个小型任务团队来构建人们需要的内部服务器。”

团队忙碌起来。

“到那周结束时，我们有超过60个内部MCP服务器准备就绪，而今天，我们已经超过100个了。”

这些内部MCP服务器包括与Slack、Google Calendar、他们的数据仓库和内部系统等工具的连接。所有这些都经过预批准，并自动可用。

## 没人谈论的问题

然而，即使有了更好的软件，新问题也随之出现。Jones说，员工们开始启用所有可用的工具，“以防万一他们需要它”。随着数十个工具的激活，AI代理变得缓慢，有时甚至无法使用。

Block的解决方案是实现自动工具管理。如果用户询问日历日程安排和Asana任务，系统会自动启用Google Calendar和Asana，同时关闭其他所有工具。Jones说，用户无需为此操心。

他们还构建了对话摘要功能。当聊天内容过长时，系统会自动总结已发生的内容，并以全新的上下文继续。

## 建立支持系统

此外，Block投入巨资帮助人们使用这些工具。

他们创建了两个Slack频道：一个用于获取帮助，另一个用于分享人们构建的东西。这个灵感频道成为了他们最佳的采用驱动因素之一。员工会看到同事自动化了他们曾费力解决的问题，然后立即想自己尝试一下。

“一个[Slack频道]是人们可以提问、[报告bug](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/)、请求功能或实时解决问题的地方，每个人都在这里贡献，”Jones说。“我无法过分强调这对采用有多么关键，特别是对于我们的非技术用户而言。”

第二个频道成为了Block的秘密武器。

“这是一个员工可以分享他们的成功故事、酷炫工作流、巧妙提示或代理成功完成的奇妙任务的空间，”Jones说。“因此，这个频道很快成为最佳的有机采用驱动力之一。人们滚动浏览，看到别人在做什么，他们立即想自己尝试一下。”

Block还每周举办关于Goose的研讨会、办公时间和培训课程。这些不仅仅是“如何使用AI”的课程，而是针对特定团队的定向研讨会。销售运营团队获得了与客户支持团队不同的培训。

## 人们实际构建了什么

Jones指出，结果令人惊讶。她详细介绍道，公司各地的员工开始自动化以前不可想象的任务：

* 一位安全分析师现在通过用日常英语向他们的数据仓库提问来检测欺诈，而不是编写复杂的[SQL查询](https://thenewstack.io/how-to-write-sql-queries/)。
* 销售运营部门的一名员工分析了80,000份销售记录，并找出了如何在不同项目中重新分配它们。以前需要几天电子表格工作才能完成的任务，现在只需一小时。
* 一名工程师利用他们的事件管理集成来发现系统中断的模式，从而进行了修复，使他们的基础设施更加可靠。

Jones分享了她自己的经历：当她需要赞助一个活动但没有时间走常规采购流程时，她向Goose求助。“感觉Goose在我耳边低语，‘让我告诉你该和谁谈谈。你想让我帮你处理这件事吗？’”

Jones说，最能说明问题的故事是关于一位员工，她构建了自己的[MCP服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)，然后询问在哪里提交。当他们给她一个GitHub链接时，她说：“哦，我没有[GitHub帐户](https://thenewstack.io/git-push-how-to-use-the-cli-to-interact-with-github/)。我不是开发者。”Jones解释说，一个非工程师构建了一个解决她特定问题的工具。

## 更大的图景

Block的经验揭示了企业AI采用的一些重要信息：技术是存在的。缺失的是围绕它的一切——安装、认证、安全、培训和社区，Jones指出。

“这不再是一个副项目了，”她总结道。“我们正在大规模地将AI付诸实践，并弄清楚这对一家真正的公司意味着什么。”

Jones解释说，其他试图扩展AI的公司可以学习Block的方法。从标准开始（MCP帮助他们避免了集成混乱）。让事物易于使用，而不仅仅是技术上可行。从一开始就构建安全性和合规性。并投资于教育和社区支持。

最重要的是：让用户驱动创新。她表示，一些最具创造性的应用来自与技术无关的部门。

Block证明了企业AI的采用不必缓慢，不必局限于开发者，也不必专注于取代员工。当你让AI工具真正易于访问时，员工会找到更智能、更快速、更自主的工作方式。

工作的未来可能不是关于AI取代人类。它可能更多地是关于赋予每个人自己由AI驱动的能力。Block已经展示了这在大规模上是什么样子。