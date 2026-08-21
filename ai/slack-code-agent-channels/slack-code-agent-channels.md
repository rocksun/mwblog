<!--
title: Slack推出全新代码频道：仅限智能体创建使用
cover: https://cdn.thenewstack.io/media/2026/08/975597e3-mariia-berezovsky-kttrmzhprjs-unsplash-scaled.jpg
summary: Slack推出Slack Code，旨在为开发者智能体提供专属协同频道。该功能由智能体自动创建并管理，支持实时代码预览、计划展示及评审。此举旨在将编程智能体从单一终端模式引入多人协作环境，并有效避免频道信息过载。目前该功能已向部分合作伙伴开放。
-->

Slack推出Slack Code，旨在为开发者智能体提供专属协同频道。该功能由智能体自动创建并管理，支持实时代码预览、计划展示及评审。此举旨在将编程智能体从单一终端模式引入多人协作环境，并有效避免频道信息过载。目前该功能已向部分合作伙伴开放。

> 译自：[Slack has a new channel type -- but only agents can create one](https://thenewstack.io/slack-code-agent-channels/)
> 
> 作者：Frederic Lardinois

Slack于周四推出了 [Slack Code](https://slack.com/blog/news/slack-code-channels-for-agents)，这是一种专为编码智能体及其主管开发者打造的新型 Slack 频道。

现在，只要你在 Slack 中的任何位置提到受支持的智能体，如果它判断该请求适合处理，它就会启动一个代码频道。该频道将承载其计划、正在处理的仓库和分支、代码差异（code diffs）、拉取请求信息以及输出的实时 HTML 预览。

频道中的成员可以请求更改或停止智能体。一旦工作完成，智能体将归档该频道，尽管它仍然可被搜索，并且 [Slack 表示](https://www.salesforce.com/introducing-slack-code/)，它可以作为审计日志使用。

有趣的是，至少目前为止，人类还无法自行创建代码频道。

![](https://cdn.thenewstack.io/media/2026/08/4c05bf1b-slack-code-1024x701.gif)

图片来源：Slack。

Slack Code 现已面向使用 Anthropic 的 Claude、Cognition 的 Devin、GitHub Copilot 和 Vercel 的团队开放，OpenAI 的 ChatGPT 支持稍后推出。Slack 产品副总裁 Katie Steigman 告诉 *The New Stack*，该功能适用于所有 Slack 计划，包括免费工作区，且不收取额外费用。

总的来说，这对 Slack 来说是一个合乎逻辑的举动。如今，大多数编码智能体在终端、IDE、桌面应用或浏览器会话中大多是“单机”体验，尽管行业几个月来一直 [推动它们向团队基础设施发展](https://thenewstack.io/coding-agents-team-infrastructure/)。

Steigman 表示：“我们需要从那种孤立的、单机的 AI 工作方式（比如我在终端工作，用某种智能体处理我的事情）转变为将其带入多人协作环境中。”

## 为什么智能体需要一种不同类型的频道

Slack 已经有了线程（提醒一下大家记得使用它们！）。但 Steigman 说，线程适用于智能体在一条或两条消息中回答的情况，而不适用于运行时间较长且随着进展引入更多人的编码会话。

“你想把人拉进来，如果是在线程中这样做，你实际上是在炸毁整个频道，”她说。“你正在摧毁那个线程，对吧？”

![](https://cdn.thenewstack.io/media/2026/08/64dfa707-slack-code-1024x667.png)

图片来源：Slack。

Steigman 认为，传统的频道存在相反的问题。Slack 将其设计为持久的团队空间，而智能体的编码会话通常会结束。

“它们有点太永久了，”Steigman 说。“它们对于智能体来说不够灵活。”

因此，Slack 增加了一种新型频道，它具有定义的生命周期，且没有人类创建者（尽管 Steigman 表示这可能会改变）。目前，每个代码频道都继承了其来源对话的可见性，因此根据智能体被提及的位置，它是公开或私有的。

## 引入智能体

Slack Code 不是编码模型、工具包或智能体运行时。Slack 构建了一个 [API](https://docs.slack.dev/ai/developing-agents/)，允许合作伙伴智能体创建和管理这种新频道类型，仅此而已。Steigman 表示，该集成并不在 [模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-mcp/) 或 [Agent2Agent (A2A)](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) 上运行，尽管 Slack 确实为了其他目的发布了 MCP 服务器。代码频道 API 的访问权限目前仅限于发布合作伙伴，计划稍后向更多编码智能体开放。

Slack 由 Salesforce 拥有，Salesforce 销售 Agentforce，而 Slack Code 免费托管 Anthropic、OpenAI、GitHub 和 Cognition 的智能体。Slack 押注于无论使用谁的智能体，它都能成为智能体工作审查的场所。GitHub 在向 Claude 和 Codex 以及其自己的 Copilot [开放 Agent HQ](https://thenewstack.io/github-agent-hq/) 时，也做了同样的押注。

## 上下文与控制

Steigman 说：“我认为这是因为你所有的上下文都在那里。”项目的错误报告、截图、决策和之前的讨论已经存在于其频道中（不过，GitHub、Atlassian 和几乎所有其他 SaaS 公司在谈论他们拥有的上下文时也会这样说）。

太多的上下文也不是好事，所以智能体的覆盖范围取决于其配置。她说，Slack 的内部智能体 Spec 可以看到她能看到的一切，而客户可以更狭窄地限定他们的智能体权限。

Slack 表示，智能体继承了其现有的权限和管理控制，并且高风险操作仍需人类签字批准。在演示中，Steigman 指出，在她的示例更改发布之前，有人会在 GitHub 中批准拉取请求。

## 围绕智能体的热潮

当然，Slack 并不是唯一一家考虑如何将智能体引入开发者对话的公司，而且它也不是走得最远的。

Anthropic 在 6 月推出了 [Claude Tag](https://thenewstack.io/anthropic-claude-tag-slack/)，这是一个为 Claude Team 和 Enterprise 客户提供的测试版共享智能体，它以自己的工作区身份运行，而不是借用召唤者的权限。Anthropic 正在采取一种不同的方法来解决同一个问题，即让一个 Claude 与频道中的每个人合作。

[Block 的 Buzz](https://thenewstack.io/block-buzz-agent-workspace/) 是一款采用 Apache 2.0 许可的协作产品，感觉非常像 Slack，它进一步推动了这种模式。Buzz 项目绑定到任意数量的频道，并在单一身份系统下承载仓库、带有内联差异和注释的拉取请求、问题、持续集成结果和合并决策，因此最初的请求和最终的结果保持连接。Buzz 也可以自托管，而 Slack Code 则不行。它没有的是安装基础，因为大多数公司无论如何都已经在使用 Slack（包括 Block 本身）。

## 避免变成“疯狂的机器人乐园”

编码可能只是第一个拥有自己智能体频道的用例。Steigman 说，Slack 已经看到代码频道被用于文档、演示和事件响应，即使界面仍然围绕仓库、分支、拉取请求、差异和预览构建。

“我认为现在低估用户体验 (UX) 是很容易的，因为每个人都沉迷于模型，”Steigman 说。

她说，Slack 的核心产品团队正在观察智能体生成的消息如何改变人类的行为，目标是添加更多智能体，而不让 Slack “因噪音而爆炸，变成这个疯狂的机器人乐园”。