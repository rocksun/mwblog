<!--
title: Anthropic为你的Slack频道赋予了Claude的常驻席位
cover: https://cdn.thenewstack.io/media/2026/06/d843691f-mohamed-nohassi-v_uh3nbuide-unsplash-scaled.jpg
summary: Anthropic推出Claude Tag，将Claude从单次响应的助手升级为Slack中的常驻团队成员。它支持异步办公、积累团队背景知识，并利用“代理身份”机制实现多人实时协作，标志着AI办公从单机向团队协作模式的重大演进。
-->

Anthropic推出Claude Tag，将Claude从单次响应的助手升级为Slack中的常驻团队成员。它支持异步办公、积累团队背景知识，并利用“代理身份”机制实现多人实时协作，标志着AI办公从单机向团队协作模式的重大演进。

> 译自：[Anthropic gives @Claude a permanent seat in your Slack channels](https://thenewstack.io/anthropic-claude-tag-slack/)
> 
> 作者：Paul Sawers, Frederic Lardinois

Anthropic [宣布推出 Claude Tag](https://www.anthropic.com/news/introducing-claude-tag)，这是一项新产品，将 Claude 直接嵌入到 Slack 中，作为一个持久的、共享的团队成员——它能够随着时间的推移积累机构知识，进行异步工作，并可以在无需提示的情况下采取行动。

该产品目前为 Enterprise 和 Team 计划客户提供测试版，取代了 Anthropic 现有的 Slack 版 Claude 应用，后者于 [2025 年 10 月首次亮相](https://claude.com/blog/claude-and-slack)。最初的集成允许用户通过私信 @Claude、通过 AI 助手面板调用它，或在对话串中 @它以获取按需帮助——这很有用，但更偏向于事务性。后来在 [12 月](https://claude.com/blog/claude-code-and-slack)，Anthropic 将 Claude Code 添加到 Slack 中，允许开发者在对话中 @Claude，并让它在 Web 上启动一个完整的编码会话，完成后将拉取请求（pull request）发布回对话串中。

从这个意义上说，Claude Tag 对 Slack 的作用大致相当于 Cowork 对知识工作者的作用：它将源于 Claude Code 的代理循环扩展到了一个新的界面和更广泛的任务集，而不是局限于工程工作流。

在许多方面，Claude Tag 是下一步的演进：Claude 不再是应要求加入对话然后静默，它现在全职驻留在频道中。任务可以安排在数小时或数天内运行，Claude 独立完成这些任务——积累上下文、学习工作词汇，并拾起那些原本会被淹没的未解决议题。

这种上下文也不一定局限于单个频道：在管理员授予访问权限的情况下，Claude 可以利用来自其他频道的信息来为其面前的工作提供依据。

![Claude Tag](https://cdn.thenewstack.io/media/2026/06/bf5c26ec-claudegif.gif)

*Claude Tag 运行中*

## 身份认同

Claude Tag 有效地赋予了 Claude 在工作空间中独立的身份——它为每个连接的工具拥有自己的账户，以 Claude 应用的身份发布到 Slack，以其自己的 GitHub 应用身份打开拉取请求，或由管理员设置的专用服务账户查询数据仓库。如果启用了“环境感知”（ambient）行为，根本不需要 @Claude——它会监控对话，标记它认为团队需要知道的事情，并跟进那些已经沉寂的对话串，这与 Claude Code 用户已经熟悉的“自动”模式非常相似。

> 除了划定工具和数据访问范围外，管理员还可以为每个频道的 Claude 设置令牌（token）消耗上限；这是防止自主代理在无人值守时产生高额费用的护栏。

每个频道都有一个 Claude，由频道内的所有人共享，因此任何团队成员都可以看到正在处理的内容，并接手同事未完成的工作。这种多人协作的动态变化可以说是迄今为止 AI 助手工作方式中最重大的转变之一。

例如，一个人分配给 @Claude 的任务，可以由团队的其他成员实时引导、纠正和建立。

![多人协作引导中](https://cdn.thenewstack.io/media/2026/06/de0e6587-gif3claude.gif)

*多人协作引导中*

支撑这一切的是 Anthropic 所称的“代理身份”（agent identity）——这种访问结构使得在不造成安全混乱的情况下实现多人 AI 成为可能。[Noah Zweben](https://www.linkedin.com/in/noahzweben/) 是 Claude Code 团队的成员，他在[一篇配套博客文章中指出](https://claude.com/blog/agent-identity-access-model)，该模型是 Claude Tag 设计处理的那种自主、团队级工作所需的必要基础。

> “在 Claude Tag 等产品中，从单人 AI 到多人 AI 的转变，使得长期、基于团队的工作成为可能。”

“在 Claude Tag 等产品中，从单人 AI 到多人 AI 的转变，使得长期、基于团队的工作成为可能，”Zweben 写道。“代理身份确保 Claude 对工具的访问范围既足以有用，又能在企业规模下保持安全。”

在工作原理方面，Zweben 解释了为什么传统模型——即 AI 助手借用调用者的权限——需要重新思考。代理现在在提问者下线很久之后依然会安排任务并响应事件，而在有多个参与者引导的共享频道中，没有单一用户的凭据适合继承。

相反，管理员在工作空间级别定义 Claude 可以访问的内容，每个频道继承一组基准权限，这些权限可以根据在该频道完成的工作进行收紧或扩展。

> “代理身份将‘这个用户能做什么？’的问题替换为‘这个代理在这个分区能做什么？’”

工程频道可能获得 GitHub 和数据仓库的读写权限；通用频道可能仅获得只读权限。至关重要的是，由于 Claude 是在自己的账户下而不是任何人的个人凭据下操作，共享频道永远不会成为进入他人私人文档的后门。

“代理身份将‘这个用户能做什么？’的问题替换为‘这个代理在这个分区能做什么？’，”Zweben 写道。

## Slack 层的竞争

团队通讯平台正迅速成为企业中 AI 代理的主要控制层——任务分配、监控和汇报都在这里进行。例如，GitHub 已经 [将 Copilot 引入了 Microsoft Teams](https://github.blog/changelog/2025-09-19-work-with-copilot-coding-agent-in-microsoft-teams/)，而 OpenAI 的 [Codex 则包含](https://openai.com/index/codex-now-generally-available/) 原生 Slack 集成，允许团队直接从对话串中委派任务。而 Cognition 的 [Devin 从一开始就是围绕 Slack 构建的](https://cognition.com/blog/devin-generally-available)。

由 Jack Dorsey 领导、拥有 Square 和 Cash App 的 Block 公司，[也花了一些时间从头开始构建类似的东西](https://thenewstack.io/how-block-manages-its-fleet-of-ai-coding-agents-from-slack/)，使用其开源的 Goose 框架开发了一个代理编排系统，工程师完全可以在单个 Slack 对话串中进行管理。

无论哪种 AI 最终成为工作协调频道的默认存在，它都将获得分发优势和复合数据优势，使其越来越难以被取代。对于一家已经在工程组织中运行 Claude Code 的公司来说，将 Claude Tag 添加到其 Slack 频道是自然的下一步——这也大大加深了这种依赖性。