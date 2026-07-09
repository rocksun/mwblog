<!--
title: Anthropic 的 Claude Cowork 现在支持合上笔记本电脑后继续工作
cover: https://cdn.thenewstack.io/media/2026/07/5e42581e-david-palma-v8xagix2nxi-unsplash-scaled.png
summary: Anthropic 宣布 Claude Cowork 现已支持 Web 和移动端，并将任务处理移至云端。这意味着即便用户离线或合上电脑，AI 代理也能持续运行预定任务。此举旨在提升知识工作者的日常办公效率，缩小了与微软 Copilot 等竞品的差距。
-->

Anthropic 宣布 Claude Cowork 现已支持 Web 和移动端，并将任务处理移至云端。这意味着即便用户离线或合上电脑，AI 代理也能持续运行预定任务。此举旨在提升知识工作者的日常办公效率，缩小了与微软 Copilot 等竞品的差距。

> 译自：[Anthropic's Claude Cowork now keeps working when you close your laptop](https://thenewstack.io/claude-cowork-cloud-mobile/)
> 
> 作者：Frederic Lardinois

自发布以来，[Claude Cowork](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/) —— Anthropic 专为知识工作者打造的代理工具，一直只能在桌面上运行。这意味着它必须依赖一台保持开启并处于运行状态的电脑，才能完成任务，包括执行预定任务。Anthropic 在周二做出了改变，将 [Cowork 推向了 Web 和移动端](https://claude.com/blog/cowork-web-mobile/)，并将其所有工作负载迁移到云端。这样即使设备离线，任务也能持续运行，且用户可以随意切换设备。

订阅 Anthropic Max 计划的用户（每月 100 美元起）现已获得 Beta 测试权限，公司预计在未来几周内将更新后的 Cowork 推向更多计划。

此次更新还拉近了 Claude Chat 与 Cowork 之间的距离。在 Web 和桌面端，聊天和 Cowork 现在共享一个界面，项目和产出物（Artifacts）可以在两者之间同步。用户可以通过模态框在 Chat 和 Cowork 之间切换，而无需进入 Claude UI 的不同区域。在移动端，Cowork 将在应用程序中拥有独立的版块。

![](https://cdn.thenewstack.io/media/2026/07/bc9a9ee7-unified-home-ui-1024x576.png)

*图片来源：Anthropic*

Anthropic 表示，将 Chat 和 Cowork 紧密结合意味着“委派任务现在变得像提问一样简单”。

不过，该公司仍需确保向用户解释清楚这两项功能的区别。当 Cowork 首次推出时，围绕它出现了一个完整的[讲解者产业](https://www.youtube.com/results?search_query=cowork+explained)，部分原因是基本的交互式聊天功能仍是大多数用户与 AI 工具互动的主流方式。毕竟，AI 代理对于绝大多数知识工作者来说仍然是新鲜事物。但另一方面，这也许会促使更多用户尝试使用 Cowork 来自动化更多的流程——并安排更多的任务。

## 从 Claude Code 到聊天窗口

从核心层面来看，Cowork 采用了 Anthropic 编码代理 Claude Code 的代理能力，并将其提供给那些从不打开终端的用户。它于 1 月份推出，允许非开发者向 Claude 下达任务，并让其在文件、日历、电子邮件、消息应用、Web 和其他连接的工具中进行协作，直到任务完成。

> “此举为 Anthropic 带来了许多用户渴望的‘全天候运行’代理，而无需忍受必须始终保持电脑开启的不便。”

4 月份，Anthropic [将 Cowork 从预览版转为正式商用](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/)，并面向付费计划添加了企业所需的基于角色的访问控制和治理功能。

然而，在周二之前，所有这些功能都在笔记本电脑上运行，一旦合上盖子就会停止。

## 工作持续进行

这正是此次最大更新的意义所在。工作仍在继续，更关键的是，[即使你的 Mac mini 离线，预定任务也能照常运行](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)。在预定时间运行任务，正是许多用户使用 OpenClaw 或像 [Tasklet](https://thenewstack.io/tasklet-is-ifttt-for-the-agentic-age/) 这样的托管服务所做的事情。

此举为 Anthropic 提供了许多用户渴望的“全天候运行”代理，而无需忍受必须始终保持电脑开启的不便。对于大多数知识工作者来说，这让他们在实现 OpenClaw 的愿景（及其所带来的用例）方面迈进了 90%，且没有任何相关的风险。

需要注意的一点：如果你有现有的预定任务，它们不会自动迁移。“现有的预定任务会继续在本地运行，并且需要你的设备保持开启，”Anthropic 的一位发言人告诉 *The New Stack*。“新的预定任务会自动在云端运行，你将能够从‘预定任务’页面迁移现有的任务。”

当然，这并不意味着 Cowork 在桌面端没有用武之地。目前，Anthropic 指出 Claude 桌面应用仍然是“深度工作场所”，因为它可以访问用户的本地文件和浏览器（Claude 何时才能在云端获得一个临时浏览器？）。

## “工作之外的工作”

Anthropic 还发布了一份关于 Cowork 使用情况的新报告，并指出目前超过 90% 的 Cowork 使用并非软件开发（基于 5 月份 120 万次匿名会话）。

最大的类别是业务运营，占所有会话的三分之一：整理电子表格、将分散的更新汇总成报告、建立入职清单。内容创作和文案写作占了 16.4%。

![](https://cdn.thenewstack.io/media/2026/07/9a0c9247-screenshot-2026-07-07-at-7.56.52-am-1024x847.png)

*图片来源：Anthropic*

两者合计约占 Cowork 使用量的一半。Anthropic 将其称为“日常知识工作”，并指出这“几乎不在任何人的职位描述中，却是每个人每周工作的重要组成部分”。Anthropic 和其他人长期以来一直认为，AI 和 AI 代理将使知识工作者从整理电子表格和演示文稿等繁琐工作中解放出来。

软件开发占 8.7%，考虑到 Claude Code 在桌面应用中仅处于一个标签页之隔，这个比例依然显得很高。

正如 Anthropic 在报告中所述：“虽然编程仍然——可以理解地——是 AI 最受关注的用途之一，但 AI 在日常业务工作中的使用正在增加，人们发现它在哪些类型的任务中最有帮助，也正变得越来越清晰。”

## 追赶微软

将 Cowork 引入云端也缩小了与微软的差距，微软在 3 月份推出了 [Copilot Cowork](https://thenewstack.io/ai-agents-knowledge-workers/)。它基于 Anthropic 的 Claude 引擎和代理框架，但从一开始就在云端（以及客户的 Microsoft 365 租户内部）运行。

Google 的 [Gemini Agent Mode](https://thenewstack.io/google-gemini-agent-platform/) 和 OpenAI 的 Operator 也在追逐同样的非开发者自动化领域。

为了庆祝此次发布，Anthropic 将 [Cowork 的使用限额翻倍](https://thenewstack.io/anthropic-claude-cowork-promotion/)，有效期至 8 月 5 日。现在，既然工作已经在云端运行，Cowork “无需你参与即可持续进行”的承诺终于可以经受考验了。

![](https://cdn.thenewstack.io/media/2026/07/28a769c3-cowork-web-mobile-press-no-logo-1920x1080-1-1024x576.png)

*图片来源：Anthropic*