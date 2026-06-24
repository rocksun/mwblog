AI开发者工具的整合正加速进行，最新消息显示，Cursor 已将开源编码助手 [Continue](https://www.continue.dev/) 收入麾下——这是其在过去繁忙的 18 个月中完成的最新一笔收购。

这笔交易似乎与 SpaceX 确认 [斥资 600 亿美元收购 Cursor](https://thenewstack.io/spacex-cursor-ai-coding/) 的时间大致相同，这意味着 Elon Musk 的火箭帝国现在也成为了 Continue 的拥有者。

交易条款尚未披露，事实上，双方几乎没有进行任何公开宣布。大约在 6 月 16 日左右，Continue 更新了其主页，发布了一则简短消息，声明已被 Cursor 收购，并附带了一份常见问题解答，解释称现有用户需在 7 月 15 日前导出数据，否则数据将被删除，且循环计费功能已被禁用。

看起来，Continue 已经被终止运营了。

![Cursor 已收购 Continue](https://cdn.thenewstack.io/media/2026/06/732deb7f-acquiredzz-1024x701.png)

*Cursor 已收购 Continue*

确认消息也通过开发者的在线报告传来，[这些开发者收到了来自 Continue 的关于其账户的电子邮件](https://news.ycombinator.com/item?id=48580219)，并通过 LinkedIn 得到证实。Matthaus Krzykowski——通过 Angel Invest 投资了 Continue 的天使投资人，也是其数据管道公司 [dltHub](https://dlthub.com/) 的长期合作者——发表了一篇感言，向包括 Ty Dunn 和 Nate Sesti 在内的创始团队致敬。

Krzykowski 表示，他从 2019 年起就一直关注 Ty Dunn 的职业生涯，当时他是总部位于柏林的 [对话式 AI 公司 Rasa](https://techcrunch.com/2024/02/14/rasa-an-enterprise-focused-dev-platform-for-conversational-genai-raises-30m/) 的首位产品经理。Ty Dunn 后来于 2022 年成为 dltHub 的创始工程师，次年离开并与 Nate Sesti 共同创立了 Continue。对 Krzykowski 而言，当时认为 [GitHub Copilot](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/) 已经垄断市场的传统观点是错误的——开发者的体验仍然存在巨大缺陷。

> “2023 年仍处于编码智能体的早期阶段——然而大多数投资者认为 GitHub Copilot 已经胜出。”

“2023 年仍处于编码智能体的早期阶段——然而大多数投资者认为 GitHub Copilot 已经胜出，” Krzykowski [写道](https://www.linkedin.com/posts/matthauskrzykowski_continue-acquired-by-cursor-has-been-acquired-share-7474561438162829312-7oig/)。“当时，开发者只能困在从 ChatGPT 复制粘贴内容，并猜测 Copilot 使用什么上下文来给出建议。显而易见，必须有一种更好的方式。支持 Ty 和 Nate 很容易——我通常会押注于我曾近距离观察其构建过程的人。”

## 开源替代方案

作为 [Y Combinator 2023 年夏季孵化班](https://www.ycombinator.com/companies/continue) 的毕业生，Continue [将自己定位为](https://www.ycombinator.com/launches/J6f-continue-the-easiest-way-to-code-with-any-llm) 充斥市场的专有编码助手的开源替代品。它作为 VS Code 扩展、JetBrains 插件和 CLI 提供，允许开发者连接他们选择的任何 AI 模型，并从他们自己的工具（如 Jira、Confluence 等）中提取上下文，以构建针对其特定环境定制的编码助手。

数据控制角度是其推销的核心——在一个由开发者几乎无法获得可见性的闭源工具主导的市场中，Continue 将自己定位为透明的替代方案。在 [2025 年初](https://techcrunch.com/2025/02/26/continue-wants-to-help-developers-create-and-share-custom-ai-coding-assistants/) 为庆祝该初创公司完成 300 万美元种子轮融资而接受 TechCrunch 采访时，Ty Dunn 详细阐述了其含义。

“当你使用 Continue 时，你可以保留你的数据，” Ty Dunn 当时说道。“作为一个组织，你可以将所有开发者的所有数据汇集在一个地方。这在那些一刀切的‘黑盒’编码助手中是不可能的，因为它们的 SaaS 产品和策略是获取你的数据并用它来为所有人改进产品。”

快进 16 个月，这家初创公司现在已被 AI 编码领域最知名的专有厂商之一吸收。在被收购时，[Continue 已经积累了](https://github.com/continuedev/continue) 34,300 个 GitHub 星标和 4,800 个 Fork，并筹集了约 500 万美元的资金。团队在关闭业务前推送了最后一个 2.0.0 版本——移除了遥测数据并清理了代码，作为对社区刻意交接的一部分。在 Apache 2.0 许可下，代码库仍然公开可用，任何人都可以 Fork 并基于其构建。

## Cursor 的低调整合

Continue 的收购是 Cursor 相关两则故事之一，它们似乎都被 SpaceX 的重磅新闻所掩盖。与此同时，Cursor 在其 Compile 开发者大会上发布了 [Cursor Origin](https://thenewstack.io/cursor-origin-github-disruption/)——一个针对代码托管和协作、挑战 GitHub 的智能体原生工具，同样未受广泛关注。

此外，这是 Cursor 在过去 18 个月里形成的一系列稳定收购动作的最新一步，[包括 AI 编码助手 Supermaven](https://cursor.com/blog/supermaven) 和 [代码审查初创公司 Graphite](https://cursor.com/blog/graphite)。与 Graphite 不同的是，后者继续作为独立产品运营，而 Continue 的交易带有典型的“收购招募（acqui-hire）”特征——该产品似乎已被关闭，且关于 Continue 团队中谁将转投 Cursor 的公开信息很少。

据 Krzykowski 称，联合创始人 Nate Sesti 正在加入 Cursor。与此同时，[Ty Dunn 的 LinkedIn 资料](https://www.linkedin.com/in/tylerjdunn/) 显示他在收购公开前几周的 5 月份离开了 Continue，目前尚不清楚他是否会加入 Cursor。Chad Metcalf（[于 2025 年 4 月](https://www.linkedin.com/posts/chadmetcalf_im-excited-to-join-continue-as-ceo-after-activity-7330627587196575746-a1gY/) 接替 Ty Dunn 担任 CEO）尚未对其下一步行动发表任何公开声明。Continue 的两名创始工程师 Dallin Romney 和 Patrick Erichsen 已加入 [OpenClaw](https://openclaw.ai/)——这是一个今年早些时候走红的开源 AI 智能体，其 [创始人加入了 OpenAI](https://steipete.me/posts/2026/openclaw)——担任技术人员。

*The New Stack* 已联系 Cursor 和 Continue 请求置评，若有回应，我们将更新本文。