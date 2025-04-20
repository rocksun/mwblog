
<!--
title: 使用Atlassian Rovo Dev Agents为整个软件开发生命周期打造Agentic AI
cover: https://cdn.thenewstack.io/media/2025/04/001746cd-anu-bharadwaj-teams-25.jpg
summary: Atlassian Rovo推出Dev Agents，助力SLDC实现Agentic AI！聚焦外部循环，解决知识共享难题。Rovo集成LLM和Teamwork Graph，通过Search、Chat、Studio三大功能，提升团队效率。Code Planner、Code Reviewer等Dev Agents已上线，Pull Request周期缩短45%。自定义AI Agents和Agent Swarm工作流，解放开发者生产力！
-->

Atlassian Rovo推出Dev Agents，助力SLDC实现Agentic AI！聚焦外部循环，解决知识共享难题。Rovo集成LLM和Teamwork Graph，通过Search、Chat、Studio三大功能，提升团队效率。Code Planner、Code Reviewer等Dev Agents已上线，Pull Request周期缩短45%。自定义AI Agents和Agent Swarm工作流，解放开发者生产力！

> 译自：[Agentic AI for the Whole SLDC With Atlassian Rovo Dev Agents](https://thenewstack.io/agentic-ai-for-the-whole-sldc-with-atlassian-rovo-dev-agents/)
> 
> 作者：Jennifer Riggins

加利福尼亚州阿纳海姆 — 如此多的[面向工程师的生成式AI（GenAI）](https://thenewstack.io/ai-engineering/)都集中在内部循环上，尤其是AI生成的代码。尽管如此，[开发人员希望花更多时间编写代码](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/)——而AI在这方面并不完全擅长（至少目前是这样）。

真正[降低开发人员生产力](https://thenewstack.io/the-interrupt-tax-why-developer-productivity-is-measured-in-silences/)的是外部循环，这导致工程师们需要等待其他团队和系统。知识共享和发现尤其如此，因为糟糕或缺失的文档仍然是开发人员抱怨的首要问题。

[GenAI](https://thenewstack.io/ai/)的真正创新在于组织[衡量整个软件开发生命周期](https://thenewstack.io/a-guide-to-measuring-developer-productivity/)，然后将AI应用于主要瓶颈和[较小的痛点](https://thenewstack.io/boost-developer-productivity-by-reducing-their-paper-cuts/)。

六个月前，企业和开发人员生产力工具的制造商Atlassian，[发布了其GenAI产品套件，称为Rovo](https://thenewstack.io/atlassians-new-ai-product-gives-developers-access-to-agents/)。Rovo目前正逐步进入全面可用阶段，每月用户已超过100万，它专注于三个跨组织职能：

- 搜索：已有超过300,000个组织正在使用它，搜索可以解决[知识工作者花费25%的时间寻找答案](https://www.atlassian.com/blog/state-of-teams-2025)的普遍问题。
- 聊天：构建在所有主要大型语言模型（LLM）以及[Atlassian Teamwork Graph](https://thenewstack.io/atlassian-intelligence-saas-co-gets-generative-ai-makeover/)和第三方工具之上，具有零日保留功能。
- Studio：开箱即用和构建自己的[AI agents](https://thenewstack.io/ai-agents/)和agent swarm工作流程。

据Atlassian团队称，早期采用者使用Rovo应用程序的成功率比领先的开源同类产品高60%。对于公司自己的工程师来说，这包括仅实施一个AI开发agent就使pull request周期时间减少了45%。

在上周的[Atlassian Team](https://events.atlassian.com/team-digital/)活动中，Rovo之前每人每月收费20美元，现在宣布包含在任何Atlassian计划中，对于没有Jira、Confluence或Loom订阅的同事，费用为5美元。该公司表示，这将增加Rovo背后的“脑力”，即其Teamwork Graph，该图描绘了团队、数据、目标和知识的互连性。

The New Stack从Atlassian的领导层了解到Rovo对开发人员体验的影响，缩小了技术和业务之间的差距。

## 去你的开发人员所在的地方
Atlassian全力投入AI，坚信AI只有在易于采用时才有价值——并且早期采用者将具有优势。

正如Atlassian的AI产品负责人Jamil Valliani在Teams ’25的新闻发布会上所说，“所有那些作为世界重建为AI加人类合作者的早期参与者。”

在其核心产品中，Atlassian希望平衡开箱即用的常见用例与定制任何解决方案的能力，因为正如他所说，“AI不是一刀切的。没有哪个团队是相同的。”

根据[Atlassian State of Teams 2025 report](https://www.atlassian.com/blog/state-of-teams-2025)，71%的受访团队表示，他们没有最大限度地利用AI来帮助他们管理和发现信息。这部分是因为早期AI采用的重点是代码生成，即使在最好的情况下，也只占开发人员体验的30%。Valliani补充说，当推广缓慢且如此多的AI没有集成到工作流程中时，AI的采用就会动摇。

[GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/)起飞的原因之一是，它通过将其可搜索的GenAI直接放在代码库旁边来减少上下文切换。Atlassian呼应了这种观点，不仅将Rovo嵌入到其自身产品的工作流程中，而且还嵌入到GitHub中，“在正确的时间和正确的地点”，正如Valliani所说，“几乎无需他们主动考虑。”
Teamwork Graph 原生理解 Jira Issues 和 Confluence Pages 之间的关系。Rovo Search 集成到带有文件预览的 [Slack](https://api.slack.com/?utm_content=inline+mention) 中——无需下载或在单独的窗口中打开即可预览——以及集成到一系列应用程序中，如 [Google](https://cloud.google.com/?utm_content=inline+mention) Drive、[ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention)（可观测性）、Sharepoint、Workday 和 Outlook。

每个 Teamwork Graph 的结果对于每个用户都会有所不同。它基于所有集成工具进行训练并从中提取数据，并为每个工具提供基于角色的访问控制 (RBAC)，从而推动更加个性化的搜索体验。

Rovo Search 提供了一个包含相关时间线和参考资料的精选摘要，并通过语义搜索进行了增强，Valliani 认为这是“首批以这种规模为我们的客户提供开箱即用的语义搜索的公司之一”。

Rovo Chat 已经在 Atlassian 内部（同样，不仅仅是技术角色）以及其他早期采用客户中广受欢迎。Atlassian 与每个主要的 LLM 都有合作关系，他说，每个 LLM 都有自己的无数据保留协议。这不仅保护了用户数据，而且还允许 Rovo 拥有自己的 GenAI 组合，能够在发布新模型时“在幕后切换”。

Valliani 吹嘘 Rovo Chat 在执行所需操作方面的内部使用成功率高达 90%。对于更复杂的主题，Chat 用户很快还可以使用 Deep Research，它会执行一个研究计划，包括不同的相关同事、扩展搜索和来源列表，生成一份包含视频、图表、表格以及（可选）Web 结果的报告。

这些 Rovo 功能现在也可用于所有 Atlassian 产品，包括 Goals，它支持将工作与结果联系起来的对话式覆盖——这在使用 [OKRs](https://thenewstack.io/a-guide-to-okrs-and-overcoming-the-pain-of-them/) 时始终具有挑战性，并且可以帮助将组织目标与 Jira issues 联系起来。

## 专为开发者打造的 AI 代理

Team ’25 最大的公告之一是在 Rovo 中推出 Studio 应用程序，该应用程序使用自然语言来自动化 AI 代理的创建和代理群的组织。当然，The New Stack 关注的是 [Rovo dev agents](http://atlassian.com/rovo-dev)。

Valliani 说，这些代理的总体目标是“将人类从繁琐的工作中解救出来”。对于转化为构建在 [平台工程目标](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/) 之上的软件，旨在承担他所谓的“耗时但重要的任务”，或者说开发者体验中 80% 的时间都陷入了苦工。

上周发布了大约 20 个开箱即用的 dev agents。Code Planner 从 Teamwork Graph 中读取 Jira issue 以及所有相关信息，如需求、Confluence 文档和任何第三方信息，Atlassian 的 AI、敏捷和 DevOps 产品负责人说。

“然后，Code Planner 将在 Jira issue 上编写一个技术计划，以帮助开发人员提高工作效率，更快地直接进行个人或团队级别的实施，”他告诉 The New Stack。

“一个好的用例是对于一个代码仓库来说是新的开发人员，这在大型组织中经常发生。您可能必须去其他地方贡献代码。我们可以帮助您编写一个计划，‘这是我们认为您应该进行更改的地方，我们为您提供我们认为需要进行更改的文件和更改。’”

Code Planner dev agent 也是初级工程师在向高级工程师寻求帮助之前的一个很好的第一站。

![Jira 中 Rovo Code Planner dev agent 的工作流程。](https://cdn.thenewstack.io/media/2025/04/a5660a61-rovo-dashboard-2-1024x566.png)

Jira 中 Rovo Code Planner dev agent 的工作流程。

新的 Implementor Agent 然后可以采用该技术计划并为其编写代码。

Devenny 说：“开发人员可以选择一个代理来实施它将返回的代码，然后再提出 pull request。” dev agent 会通知开发人员，共享差异，并且“开发人员可以审查它并进行任何更改。” 这通常涉及开发人员和代理之间的对话。

## 自定义 Dev Agents 的用例

虽然有大约 20 个开箱即用的 AI 代理，但 Valliani 说，早期的采用者需要一个空白画布来构建自己的代理，每个代理都致力于一个单一的目的。

考虑到这一点，Atlassian 增加了无需代码即可构建自己的代理的功能，即使是 Atlassian 的非技术部门也使用了该功能。在内部，Atlassian 创建了自己的 Onboarding Buddy 代理，在第一个月内，该代理回答了 70% 的 Atlassian 新员工提出的 2,000 个问题。

一个 Atlassian 工程团队构建并在内部共享了其自己的 Pull Request Generator，团队成员表示该工具自动化了 80% 的开发者任务（例如添加功能标志和测试自动化），从而将平均 pull request 时间缩短至 30 分钟。

这种创建自定义开发代理的能力还允许客户执行组织和行业标准，通常从现有的 Confluence 文档中提取。

Valliani 说：“然后你可以定制这些代理，可以指定知识来源并约束代理，然后自动运行代理。”

面对越来越多的 AI 生成代码意味着对代码审查的需求增加，Atlassian 内部通过其 Code Reviewer 解决了第三个早期的 agentic AI 开发者用例。Devenny 说，它将 pull request 与 Jira issue 结合起来，“推断 Jira issue 中的验收标准，并展示代码是否真正符合该验收标准。”

Code Reviewer 还会检查语法错误和拼写错误。如果它是对更敏感或关键的代码库的代码更改，则可以标记为由两个审查者审查。

上周，Code Reviewer 建议 Devenny 降低此函数的复杂性，并提供了一个代码示例说明如何操作。考虑到这一点，在未来几个月内，Bitbucket 将推出一个“应用建议”按钮。

自从 10 月下旬采用此特定开发代理以来，Atlassian 工程部门在使用 Code Reviewer 时，任何 pull request 的 PR 周期时间都提高了 45%，而未使用时则没有。

Devenny 说：“之所以有如此大的跳跃式下降，是因为你无需等待数小时或数天才能让同行参与进来，你可以立即获得反馈。”

> “目前，我们为开发者执行的任务就像重复性任务，开发者一开始就不热衷于执行的任务。能够从他们必须做的事情中删除这些任务意味着他们可以花更多时间专注于他们喜欢实施的任务。”
>
> — Josh Devenny, Atlassian

Ops Guide 是另一个开发代理，可帮助处理 on-call 职责，旨在减少检测、响应和从事件中恢复的时间。

这些开发代理中的每一个都有助于缩短整体 issue 周期时间，但不会自动化掉循环中必不可少的人。

Devenny 还提到 Pipeline Fixer 和 Deployment Summarizer 开发代理即将推出。

Feedback Decoder AI 代理创建和分析来自 Loom 视频消息平台和其他来源的客户反馈的文字记录，然后可用于自动创建 Jira tickets。然后，Jira Product Discovery (JPD) AI 代理可以将 Jira tickets 与客户数据连接起来，而这些数据又与既定目标相关联。Feedback Decoder 还可以更新 Slack 中的团队，在 HubSpot 中记录活动等等。

Atlassian 总裁 [Anu Bharadwaj](https://www.linkedin.com/in/anutthara/) 在 Teams ‘25 主题演讲中说：“JPD 可以非常简单地了解你的产品创意如何推动重要目标和指标，因此你可以解释你的伟大产品创意如何影响你的业务，并且你可以决定谁有权访问你自己的地图。”“它可以是部门、团队或整个公司。”

Atlassian 甚至使用它与合作伙伴和客户分享产品路线图。Bharadwaj 还引用了早期采用者 Doodle 在线调度平台，以及它如何使用 JPD 来“构建一个将客户洞察转化为创意的系统，结果令人震惊——交付速度提高了 25%，计划时间减少了 93%。”

Devenny 说，这些开发代理在不保留数据的情况下完成了所有这些工作：“我们不会根据你的数据进行训练。我们只是在运行时向代理提供该上下文。”

## 编排 AI 代理队友群

然后，团队可以编排执行互连任务的 AI 代理群，从而搭建多个 AI 代理群。

Bharadwaj 说：“[AI 原生软件开发方法](https://thenewstack.io/what-is-an-ai-native-developer/) 真正改变了游戏规则。它打破了角色之间的传统孤岛，并消除了重复性任务。”“想象一下，每个团队成员都可以做比他们传统上分配的角色更多的事情。在我们的 Rovo 代理的支持下，这创造了一个由强大的通才组成的团队，为 AI 原生世界做好准备。”

Studio 还允许团队同时实施多个 issue，例如“为这四件事生成单元测试”，代理将创建四个实现，每个 issue 一个，并将其移至审查，甚至设置自动化。

最近，Atlassian 工程部门不得不更新 200 项服务中的 API。一个自定义开发代理在一个小时内提出了 200 个 pull requests。
“人们会有‘顿悟’或‘哇’的时刻，他们会想，‘哦，我以后不需要再做这类任务了。’这是一个巨大的思维转变。在每一种情况下，我都看到了积极的一面，因为随着LLM能力的提高，我们将能够完成越来越多的任务，”Devenny说。

“目前，我们为开发者所做的任务都是重复性的任务，开发者一开始就不热衷于做这些任务。能够从他们必须做的事情中移除这些任务，意味着他们可以花更多的时间专注于他们喜欢实现的任务。”

Rovo dev agents 现在在 GitHub 和 Bitbucket 上面向 Atlassian 客户开放公开测试版。在测试期间，客户无需支付任何费用。