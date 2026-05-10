AI 编程公司显然都认同自主代理正在成为软件开发的核心，但这些系统应如何运行——以及开发者在协作环路中处于什么位置——仍存在争议。

[Amp](https://ampcode.com/) 是一家在 2025 年底[从 Sourcegraph 剥离](https://sourcegraph.com/blog/why-sourcegraph-and-amp-are-becoming-independent-companies)出来的 AI 编程初创公司，本周揭晓了其重新构建的 CLI 版本，名为 [**Neo**](https://ampcode.com/news/neo)。该版本经过重新设计，支持远程控制、插件驱动，并能更好地适应运行时间较长的代理工作流。

与此同时，该公司还一直在主张“[编程代理已死](https://ampcode.com/news/the-coding-agent-is-dead)”。更准确地说，Amp 认为目前的 AI 编程代理模式——即紧密绑定于单一编辑器、单一终端和单一用户会话的系统——正开始让位于能够跨环境运行、更具自主性且需要更少直接监督的代理。

> Amp 认为，目前的 AI 编程代理模式——即紧密绑定于单一编辑器、单一终端和单一用户会话的系统——正开始让位于能够跨环境运行的代理。

这产生了一个明显的矛盾：如果代理正在超越终端，那为什么还要重构终端呢？Amp 的观点是，终端正在变成一个“控制面”——它是开发者与代理交互的众多场所之一。

“终端依然重要，而且将一直重要，”该公司写道。“总会有一些时刻，你会希望代理就在你身边。”

## 重构 CLI

![Neo](https://cdn.thenewstack.io/media/2026/05/6c2e1900-gif1.gif)

*Neo*

全新 Neo 的核心部分是远程控制。当开发者在本地启动 Amp CLI 线程时，他们现在可以通过 Amp 的 Web 界面远程连接并管理该会话。系统会将终端会话的实时更新流式传输到浏览器中，同时允许用户从命令行之外发送后续提示、排队消息、中断任务或彻底取消代理。

![Remote control](https://cdn.thenewstack.io/media/2026/05/98bf79b3-gif2-remote-contorl.gif)

*远程控制*

Amp 表示，实现这种远程交互的底层架构是其从头开始重构 CLI 的主要原因之一。

Amp 联合创始人兼 CEO [Quinn Slack](https://www.linkedin.com/in/quinnslack) 在 [X 上的帖子](https://x.com/sqs/status/2052129216007971230?s=20)中指出了这一架构变化，并提到他甚至能在飞机的 Wi-Fi 环境下交付功能，因为新架构往返服务器的数据量减少了“约 95%”。

根据 Slack 的说法，这种减少源于将代理循环（agent loop）本身移至云端，而不是直接在终端会话内部运行。

值得注意的是，Amp 并不是唯一一家将编程代理扩展到本地终端会话之外的公司。

[GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-remote-control?utm_source=chatgpt.com) 和 [Claude Code](https://code.claude.com/docs/en/remote-control?utm_source=chatgpt.com) 最近都推出了远程控制功能，允许开发者从终端外部监控并与长时间运行的编程会话进行交互。

在其他方面，Neo 还引入了一个[插件系统](https://ampcode.com/manual/plugin-api)，用于通过额外的工具和集成来扩展 CLI，以及一种全新的“压缩优先（compaction-first）”架构，旨在更好地管理长时间运行的代理会话和庞大的对话历史。更新后的 CLI 还可以在执行过程中展示代理的中间推理过程，而 Token 和成本追踪现在也会在长时间运行的会话中直接显示在界面上。

## 超越 IDE

Amp 表示将在未来几天逐步推出 Neo，用户可以直接向公司申请早期访问权限。

> 新的 CLI 诞生于 AI 编程公司对软件开发演变方式日益增长的分歧之中。

新的 CLI 诞生于 AI 编程公司对软件开发演变方式日益增长的分歧之中。虽然大多数公司都认同自主代理将承担更大的角色，但在什么将成为其主要交互界面上，大家的共识较少。

今年 4 月，开源 AI 编程初创公司 [Roo Code 宣布](https://thenewstack.io/roo-code-cloud-ides-ai-coding/)将停止其 VS Code 扩展和更广泛的以 IDE 为中心的工具开发，转而支持 [Roomote](https://roomote.dev/)。Roomote 是一款基于云的自主编程代理，旨在跨 Slack、GitHub 和 Linear 等工具端到端地执行任务。

[Matt Rubens](https://www.linkedin.com/in/mattrubens/)，Roo Code 的 CEO 兼联合创始人，[在 X 上写道](https://x.com/mattrubens/status/2046636598859559114)，他的团队已经转向在并行的云环境中远程运行代理，系统可以在那里开启修复并验证自己的输出。

“如果代理只需一个提示词就能创建一个高质量的 PR（拉取请求），交互模式就会完全改变——你会脱离 IDE，专注于端到端地推动事务，”Rubens 写道。

顺便提一句，[Atlassian 本周扩展了](https://thenewstack.io/atlassian-teamwork-graph-agents/)对其 Teamwork Graph 的访问权限——这是该公司跨越 Jira、Confluence、Bitbucket、Jira Service Management 和其他连接工具的索引型企业图谱——通过一个新的 CLI，该工具明确**不是**为开发者设计的，而是为他们的代理设计的。

![Teamwork Graph CLI](https://cdn.thenewstack.io/media/2026/05/81eeb1c0-gif3.gif)

*Teamwork Graph CLI*

Atlassian [将其描述为](https://developer.atlassian.com/platform/teamwork-graph/twg-cli/)“AI 编程代理的技能层”：安装一次，Claude Code、Codex、Gemini 或 Cursor 就可以代表你查询并操作整个 Atlassian 技术栈。人类进行设置，代理负责驾驶。这是一个虽小但具有指标意义的信号，表明老牌厂商正开始默认构建“代理可读”的工具，而不是在为人类设计的界面上强行添加代理访问权限。

> 势头正从“编程代理存在于单一编辑器或紧密受限的本地会话中”这一想法中转移。

总的来说，这些努力表明，势头正从“编程代理存在于单一编辑器或紧密受限的本地会话中”这一想法中转移。然而与此同时，命令行本身似乎正在作为这些系统的运行时、协调层和控制面，找到新的角色。

Amp 实际上是在试图跨越这两个领域——它押注即使代理变得更加自主，开发者仍然会希望有一个可以“握住方向盘”的地方。而那个地方很可能就是终端。