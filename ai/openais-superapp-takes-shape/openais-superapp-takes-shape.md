<!--
title: OpenAI 超级应用初具规模：Codex 正在突破编程界限
cover: https://cdn.thenewstack.io/media/2025/11/2ade5193-img_2600-scaled.jpg
summary: OpenAI 正将 Codex 演进为集成浏览器、自动化工具及图像生成的超级应用。通过支持后台电脑操作、引入心跳自动化机制和插件生态，Codex 正在从单一编程工具转型为全能的 AI 助手。
-->

OpenAI 正将 Codex 演进为集成浏览器、自动化工具及图像生成的超级应用。通过支持后台电脑操作、引入心跳自动化机制和插件生态，Codex 正在从单一编程工具转型为全能的 AI 助手。

> 译自：[OpenAI's superapp is taking shape as Codex goes beyond coding](https://thenewstack.io/openais-superapp-takes-shape/)
> 
> 作者：Frederic Lardinois

OpenAI 已经[公开](https://openai.com/index/next-phase-of-enterprise-ai/)谈论过其构建统一 AI 超级应用的计划，该应用将结合 ChatGPT、Codex 编程代理、Atlas 浏览器以及面向企业的新型代理式 AI 工具。我们现在正看到这一愿景的首批组件通过 [Codex 桌面端应用的重大更新](https://openai.com/index/codex-for-almost-everything/)汇聚在一起，这将构成这一新超级应用的基础。

该公司最初于 2025 年 5 月推出 Codex 作为其软件工程代理。起初反响平平，但在 2026 年成为 OpenAI 的热门产品，特别是在 2 月份发布了公司的[专用 Codex 模型](https://thenewstack.io/openai-releases-new-models-trained-for-developers/)之后。

OpenAI 的 Codex 负责人 Thibault Sottiaux 在周三发布前的简报中指出，Codex 目前拥有 300 万周活跃用户，且每月新增 100 万用户，这一增长势头仍在加速。

“我们实际上是在玩一个‘暗度陈仓’的把戏，在公开透明地构建超级应用——并从 Codex 演进而来，”Sottiaux 说道。

Codex 桌面应用是该公司构建此超级应用的逻辑起点，虽然 OpenAI 将周三的更新定位在编程和开发者用例上，但其中许多功能同样可供商业和个人用户使用。

## 后台运行的电脑使用功能

Codex 现在可以使用你的电脑——或者至少是你的 Mac，因为该功能目前尚未在其他平台上推出。凭借此功能，Codex 可以操作桌面应用程序，无论是为了测试你使用编程代理构建的东西，还是为了自动化任何其他任务。

这里有趣的一点是，Codex 实际上可以在后台完成所有这些工作，而不会妨碍你使用电脑。其他电脑使用（computer use）代理通常会接管桌面，考虑到这些代理目前往往反应较慢，这更容易拖慢你的速度而不是提高效率。

“你开始觉得 Codex 能做的事情没有限制了，”Sottiaux 说。“它变得非常、非常具有创造力。它让你保持在状态（flow）中。它能理解你的目标、你的语境，具备跨所有应用和浏览器工作的能力，并保持步调一致。而且它还能定期在后台执行所有这些工作，在你日常关心的每一件事上提供帮助，而不仅仅是在你构建和开发软件的时候。”

> “这简直是 Codex 在构建它自己。” —— OpenAI 的 Thibault Sottiaux

OpenAI 正在利用这一功能对 Codex 进行质量保证，让代理验证应用中的每个功能是否已实现。“这简直是 Codex 在构建它自己，”他说。

值得注意的一点是，要开始使用电脑使用功能，你需要进入 Codex 设置并下载插件。

![](https://cdn.thenewstack.io/media/2026/04/217c7d05-computer-use-tic-tac-toe.gif)

*来源：OpenAI*

## Codex 内置浏览器

通过 Atlas，OpenAI 构建了自己的浏览器，目前也正缓慢地将其引入 Codex。目前推出速度较慢，但已经有一些明显的用例超出了当前正在构建的应用预览范围。在这个新版本的 Codex 中，你实际上可以对浏览器中看到的任何内容发表评论。OpenAI 指出，这对于向代理提供前端工作的反馈特别有用。

不久之后，Codex 将获得该浏览器的完整使用权，以打开页面、逐步执行用户流程并分析其自身工作。届时，内置浏览器的潜力对于开发者来说将变得更加明显，同时也将为那些必须填写表格或在不同 Web 应用之间复制粘贴数据的商业用户开启更多用例。

Sottiaux 谨慎地将其描述为 Atlas 和 Codex 未来走向的预览。“这还不是它的全部实力。这算是对未来趋势的一次窥探，”他说。

![](https://cdn.thenewstack.io/media/2026/04/6afba678-in-app-browser.gif)

*来源：OpenAI*

## Codex 内置图像生成

关于前端工作，Codex 现在还可以访问 OpenAI 的 gpt-image-1.5 图像生成模型。如果你想在 Codex 生成的网站中添加任何视觉资产（或者仅仅作为占位符），这非常有用。但 OpenAI 团队也指出，这对于构建原型（mockups）或为游戏生成资产等也很有用。

OpenAI 表示，生成图像将不收取额外费用。

![](https://cdn.thenewstack.io/media/2026/04/9a978c7b-imagegen-burger.gif)

*来源：OpenAI*

## 丰富的插件生态

此版本还新增了对另外 90 个插件的支持，这些插件是 OpenAI 精选的技能、集成和 MCP 服务器包。一些新插件包括用于管理 JIRA 的 Atlassian Rovo，以及 CircleCI、CodeRabbit、GitLab Issues、Microsoft 套件、Databricks 的 Neon、Remotion、Render 和 Superpowers。

正如领导 Codex 应用开发的 Andrew Ambrosio 所指出的，“目标是让 Codex 自然地融入人们的工作方式，而不是让他们改变工作方式。”

![](https://cdn.thenewstack.io/media/2026/04/4606b13b-automations-x-plugins-proactive-teammate.gif)

*来源：OpenAI*

虽然插件本身可能看起来并不起眼，但它们构成了将许多非编程用例引入 Codex 的骨干。目前，这已经远远超出了标准的办公效率和电子邮件服务，涵盖了 MyRegistry.com、United Rentals、FINN 汽车订阅、Readwise 以及来自 Pitchbook、Morningstar 和 Scite 等的各种研究工具。

正如 OpenAI 团队所指出的，当这些插件与 Codex 的自动化（Automations）功能结合时尤其有趣——即 OpenAI 能够按计划运行提示词（类似于 [Claude Code 中的 Routines](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)）。

## 心跳与自动化

这些自动化功能也迎来了重大的、受 OpenClaw 启发的更新，增加了“心跳”（heartbeats），允许你自动跟进某个线程。

“你可以设置一个专门用于每日简报的线程，或者一个用于分流 Slack 消息的线程，”Ambrosio 说。“或者你可以将其设置为个人助理，每五分钟运行一次心跳（类似于 Open Claw），然后去使用插件执行一堆任务。对于你需要完成的任务类型，尤其是那些持久性的任务，这是一个非常强大的个性化维度。”

![](https://cdn.thenewstack.io/media/2026/04/d7872c23-automations-1024x373.png)

*来源：OpenAI*

值得一提的是，这些心跳在同一个线程中运行。来自 OpenAI 竞争对手的类似工具通常会为每次运行创建新的工作树，这可能导致它们丢失之前迭代的上下文。

在 OpenAI 内部，心跳自动化已经成为部署近乎持续运行的代理的一种方式，这些代理负责监控 Slack 频道、分流收件箱或盯住 GitHub 和 Notion。Sottiaux 描述了同时运行多个代理的情况，它们本质上就像团队成员一样。

## 更多主动式帮助

Codex 现在还会更频繁地建议后续行动，包括安排自动化任务。“Codex 现在还会主动提议有用的工作，以继续你中断的地方。利用来自项目、连接插件和记忆的上下文，Codex 现在可以建议如何开始你的工作日，或者从之前的哪个项目继续，”该团队在今天的公告中写道。

例如，Codex 可能会建议你跟进 Google 文档中未回答的评论，并从 Slack 和 Notion 等其他应用中提取上下文来帮助你完成。

结合改进的记忆系统（现在允许 Codex 更好地记住你的偏好和以往互动的上下文），这可能是开发者工作流之外，Codex 日常使用中最具影响力的变化之一。它也展示了 OpenAI 长期以来对这款应用的规划方向。

虽然这里的重点大多在于超越编程，但至少在目前，开发者也能获得大量新功能和体验优化更新。

“我们继续在开发者已经投入时间的地方进行投资，”Ambrosio 说道。

例如，现在可以直接在 Codex 中处理 GitHub 评审评论。开发者可以打开多个终端标签页（太棒了！），通过 SSH 连接到远程开发机（目前处于 Alpha 阶段），并在侧边栏中打开文件以查看 PDF、电子表格、幻灯片或其他文档。新增的还有一个摘要面板，让你跟踪计划、来源和产出物。

“结合在一起，这些改进使得在编写代码、检查输出、评审更改以及在单一工作区中与代理协作等软件开发生命周期的各个阶段之间移动变得更快，”OpenAI 团队写道。

![](https://cdn.thenewstack.io/media/2026/04/4f6aff87-remote-ssh.gif)

*来源：OpenAI*

## 作为队友的 Codex

在 OpenAI 内部，Codex 已经远远超出了其编程起源。Codex 团队表示，公司 80% 以上的人都在使用它，而且不仅仅是工程师：用例包括撰写每周简报、综合反馈、起草产品需求、审查合同，甚至发送安全培训提醒。

## 可用性

更新后的 Codex 应用现在面向所有使用 ChatGPT 登录的 Codex 用户开放。某些功能，包括上下文感知建议和记忆等个性化功能，将在稍后阶段提供给 Enterprise、Edu 以及欧盟和英国的用户。电脑使用功能在发布时也不会向欧盟和英国用户开放，但将“很快”推出。

Sottiaux 指出，随着时间的推移，我们还将看到 Codex Web 应用和移动应用。