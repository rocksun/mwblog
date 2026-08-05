<!--
title: 现在的Codex到秋天就会显得“原始”——OpenAI团队的路线图印证了这一点
cover: https://cdn.thenewstack.io/media/2018/03/8fa2e419-laptop.jpg
summary: OpenAI核心产品负责人Thibault Sottiaux指出，受限于本地环境的Codex即将迎来重大演变。通过收购Ona构建持久化云端工作空间，AI Agent将实现脱离笔记本的自主运行，这意味着当前开发模式即将面临颠覆。
-->

OpenAI核心产品负责人Thibault Sottiaux指出，受限于本地环境的Codex即将迎来重大演变。通过收购Ona构建持久化云端工作空间，AI Agent将实现脱离笔记本的自主运行，这意味着当前开发模式即将面临颠覆。

> 译自：[Today's Codex will feel "primitive" by fall — and its own team's roadmap backs it up](https://thenewstack.io/openai-codex-cloud-evolution/)
> 
> 作者：Amanda Caswell

Thibault Sottiaux，OpenAI的核心产品负责人，认为目前的Codex版本在今年结束前就会显得过时。

[Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/) 在周一晚间通过X平台发文称：“鉴于我最近看到的一些结果，很明显Codex是一个很好的工具。” 他继续写道：“但它在2-3个月内就会显得原始，我们即将经历AI在最前沿使用方式的另一次重大进化。” 他还表示：“下一代模型需要的不仅仅是你的笔记本电脑。”

> “它在2-3个月内就会显得原始，我们即将经历AI在最前沿使用方式的另一次重大进化。”

Sottiaux并未透露OpenAI未来几个月计划的细节。然而，他的评论非常及时，因为该公司已经在努力将Codex的应用范围扩展到开发者计算机之外。自7月初[为Codex推出新的GPT-5模型](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/)并随后[突破800万用户](https://thenewstack.io/gpt-5-6-codex-user-surge/)以来，该产品一直在快速演进。

## Ona填补了基础设施的空白

6月，OpenAI[表示计划收购Ona](https://openai.com/index/openai-to-acquire-ona/)，这是一家创建安全云开发环境的公司。OpenAI称此次收购是“Codex下一阶段”的一部分，届时Agent即使在发起任务的笔记本电脑关闭后，也能在客户的云端持续工作。

> “下一代模型需要的不仅仅是你的笔记本电脑。”

目前Codex使用云基础设施，但仍可能需要开发者的笔记本电脑来访问项目和运行工具。如果笔记本电脑断开连接，Agent可能会丢失继续工作所需的内容。

OpenAI已经测试了这种方法。在[2月份发布的一项实验中](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)，Codex在从零构建设计工具时连续工作了约25小时，使用了约1300万个token，并生成了约30,000行代码。阿里巴巴更进一步——其Qwen3.8-Max Agent最近[自主编码了16天](https://thenewstack.io/qwen-autonomous-coding-audit/)，在无人帮助的情况下提交了265次代码。Ona可以帮助解决这个问题。

该公司（以前称为Gitpod）创建的云环境可以根据每个项目所需的工具和依赖项进行设置。OpenAI表示，Ona已经帮助200万开发者使用了这些环境。

## Agent需要持久的工作区

如果收购完成，Ona的技术将使Codex能够在客户的云端拥有一个永久的工作区。Agent无需依赖本地机器上的活动会话，即可获得任务所需的上下文和工具。

OpenAI表示，企业仍将决定Codex在其云环境中的工作方式，包括它能访问哪些敏感系统。该交易尚未最终确定，因此OpenAI和Ona目前仍是独立的公司。

目前尚不清楚Sottiaux的预测是否真的与Ona有关。尽管此次收购表明OpenAI的眼光已不仅局限于模型本身，因为要让Codex独立工作，它需要一个即使在开发者的笔记本电脑关闭时也能保持在线的环境。

遗憾的是，将执行环境迁移到云端解决了一个问题，但也带来了许多新问题。

## 安全风险随访问权限增加

让编码Agent拥有对公司网络或开发者凭据的完全访问权限无疑是有风险的。OpenAI表示，Ona的客户控制模型将允许Agent在组织自己的云内工作，而OpenAI则提供模型和编排。即使模型变得更强大并能处理更复杂的任务，它仍然需要一个安全的地方来运行命令、保存进度并与其他系统进行交互。

开发者可以将重构、升级依赖项或调查Bug等任务分配给Agent，并让其远程工作。他们可以跟踪进度、检查终端输出，并在需要人工决策时介入。当Agent完成任务时，用户可以查看合并请求并检查运行了哪些测试。

OpenAI已经在朝这个方向发展。Codex[已被整合进ChatGPT桌面应用中](https://thenewstack.io/openai-codex-work-atlas/)，并能处理并行任务。其[桌面应用正日益围绕管理Agent进行构建](https://thenewstack.io/openais-codex-desktop-app-is-all-about-managing-agents/)，其移动功能让开发者能够监控和引导在笔记本电脑、开发机或远程环境中运行的任务。它还通过[新的插件](https://thenewstack.io/openais-codex-gets-plugins/)和[针对知识工作者的工具](https://thenewstack.io/openai-codex-knowledge-workers/)进行了扩展，不仅仅服务于开发者。

> Agent环境将结合计算资源与CI/CD系统。

## 管理新的Agent层

这种变化意味着出现了一种需要管理的新型基础设施。Anthropic已经在这一领域采取行动——其[收购Mendral](https://thenewstack.io/anthropic-mendral-cicd-acquihire/)旨在直接在其平台内自动化CI/CD任务，如不稳定的测试和依赖项审查。Agent将需要自己的身份和访问规则，它们的行为也需要像人类开发者和当前的自动化流程一样被记录、审查并追溯。

Sottiaux的预测无疑引发了好奇。两到三个月对于一个产品变得“原始”来说，是一个非常短的时间。