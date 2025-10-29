<!--
title: GitHub携Agent HQ入局，全面拥抱AI编程智能体大战
cover: https://cdn.thenewstack.io/media/2025/10/3fb0a441-img_2704-scaled.jpg
summary: GitHub 发布 Agent HQ，集成 Anthropic、Google 等第三方编程代理，通过任务控制中心管理。开发者可自定义代理，并支持 Slack/Linear 集成，同时推出代码质量功能，提升协作效率。
-->

GitHub 发布 Agent HQ，集成 Anthropic、Google 等第三方编程代理，通过任务控制中心管理。开发者可自定义代理，并支持 Slack/Linear 集成，同时推出代码质量功能，提升协作效率。

> 译自：[GitHub Embraces the Coding Agent Competition With Agent HQ](https://thenewstack.io/github-embraces-the-coding-agent-competition-with-agent-hq/)
> 
> 作者：Frederic Lardinois

**披露：** GitHub 承担了作者参加 GitHub Universe 的机票和住宿费用。

旧金山 — 在其 [Universe 2025 大会上](https://githubuniverse.com/)，[GitHub](https://github.com/) 今天[发布](https://github.blog/news-insights/company-news/welcome-home-agents/)了一系列更新，将把第三方编程代理直接引入 GitHub。

因此，开发者将能够在一个地方看到他们的代理工作，了解其思考过程，根据需要引导它们，并批准它们生成的代码。今年晚些时候，这项新功能将支持 [Anthropic 的 Claude Code](https://thenewstack.io/anthropics-claude-code-comes-to-web-and-mobile/)、[谷歌的](https://cloud.google.com/?utm_content=inline+mention) [Jules](https://thenewstack.io/agentic-coding-how-googles-jules-comparestoclaudecode/) 和 [OpenAI 的 Codex](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/)，以及来自 [Cognition](https://cognition.ai/) 和 [xAI](https://x.ai/) 的编程代理，当然还有 GitHub 自己的 Copilot 代理——所有这些都将作为 GitHub 付费订阅的一部分。

Copilot Pro+ 用户现在还可以在 VS Code 的 Insider 版本中与 OpenAI 的 Codex 协同工作（由 OpenAI [最近推出的 Codex SDK](https://thenewstack.io/openai-launches-a-new-gpt-5-model-for-its-codex-coding-agent/) 提供支持），使其成为首批将代理直接引入编辑器的合作伙伴（VS Code 本身也正在获得更新，旨在使其“完全围绕与代理协同工作”）。

对于那些希望对这些代理拥有更多控制权的用户，GitHub 现在还将允许开发者在 VS Code 中创建自定义代理。这意味着他们可以创建包含自定义指令和防护措施的 AGENTS.md 文件。

这套名为 Agent HQ 的新代理工具将使这些编程代理能够访问与 GitHub 自己的 Copilot 代理相同的工具和 API。GitHub 表示，其理念是使代理成为 GitHub 工作流的原生部分，并为开发者提供工具来管理一组专门的代理，以并行执行任务。

## GitHub 的 Agent HQ

Agent HQ 也将扩展到 VS Code，GitHub 将首先在编辑器中直接集成 OpenAI 的 Codex，其他代理也将很快跟进。

正如 GitHub 首席运营官 Kyle Daigle 在今天发布会前[接受采访时](https://youtu.be/5oZAm5fHziA?si=7IO6yYXoC9afY5AO)告诉我的那样，GitHub 希望给开发者提供选择——即使这意味着他们可能会选择非 Copilot 的编程代理、非 GitHub 的问题跟踪器或非 VS Code 的 IDE。

[![](https://cdn.thenewstack.io/media/2025/10/527549ea-c7f5cae8-11c9-44f3-842a-a5fde3f4d5b7-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/527549ea-c7f5cae8-11c9-44f3-842a-a5fde3f4d5b7-scaled.jpg)

*GitHub 宣布 Agent HQ 支持第三方编程代理（图片来源：The New Stack）。*

借助 Copilot，GitHub 提供了首批 AI 编程工具之一。但如今，开发者在选择上有了更多余地。Anthropic 的 Claude Code、谷歌的 Jules 和 Gemini CLI、OpenAI 的 Codex 以及 Copilot 本身等编程代理，当然，[已成为大多数开发者的标准工具箱的一部分](https://thenewstack.io/ai-has-won-googles-dora-study-shows-universal-dev-adoption/)。

[![](https://cdn.thenewstack.io/media/2025/10/077324cd-3rd-party-agent-ui-1-1024x560.jpg)](https://cdn.thenewstack.io/media/2025/10/077324cd-3rd-party-agent-ui-1-1024x560.jpg)

*GitHub 的 Agent HQ 允许开发者选择他们偏好的编程助手。（来源：GitHub）*

Daigle 表示：“我们 Agent HQ 的目标是，提供一个单一平台，你可以在其中使用基本上任何想要集成的编程代理，并拥有一个统一的视图——一个任务控制中心界面，我可以在其中查看所有任务、它们正在做什么、它们处于何种代码状态——考虑创建、代码审查等，并将使我们能够构建 GitHub Copilot 编程代理的底层原语提供给所有其他编程代理。”

几乎所有编程代理都已与 GitHub 集成，开发者通常通过在 GitHub 中标记他们最喜欢的编程代理来启动后台代理任务。但正如 Daigle 所指出的，直到现在，你还无法在 GitHub 中看到它们实际执行这些任务或引导它们。

Anthropic 首席产品官 Mike Krieger 表示：“我们正与 GitHub 合作，让 Claude 更紧密地融入团队构建软件的方式。通过 Agent HQ，Claude 可以处理问题、创建分支、提交代码并响应拉取请求，像任何其他协作者一样与你的团队协作。我们认为这就是未来开发的工作方式：代理和开发者在您已信任的基础设施上共同构建。”

## 任务控制中心（Mission Control）

Agent HQ 的核心是任务控制中心（Mission Control），它将成为 GitHub 所称的“中央指挥中心”，用于与这些代理协同工作。它将在 GitHub 网页界面、VS Code、GitHub 移动应用程序和 CLI 中提供。

GitHub 设想的一个常见工作流程是，开发者首先在 GitHub 网页界面中将工作分配给一个代理，然后在任务控制中心（Mission Control）监控进度。然后，如果他们想修改该代码，他们将转到他们的 IDE，完成后，提交代码并继续处理其他任务。

[![](https://cdn.thenewstack.io/media/2025/10/bc83de4d-ezgif-504f7f231e73af.gif)](https://cdn.thenewstack.io/media/2025/10/bc83de4d-ezgif-504f7f231e73af.gif)

*在任务控制中心（Mission Control）分配和监控工作的示例。（来源：GitHub）*

由于这些代理将原生访问这些原语，GitHub 也能够扩展对许多企业一直要求的功能的支持。例如，这些代理的新控制平面将允许组织设置审计日志、创建安全策略，并管理开发者可以访问哪些代理和模型。

具体而言，这意味着增加分支控制，使组织能够控制何时运行持续集成工作流和其他检查，以及代理的访问控制、一键合并冲突解决和更好的文件导航功能。

## Slack 和 Linear 集成

GitHub 还将推出与 Slack 和 Linear 的新集成。

Daigle 告诉我：“无论你在哪里遇到需要用代码解决的问题，我们都应该在那里。因此，我们最近推出了一个 Teams 集成来实现这一点。我们正在添加 Slack 集成来实现这一点，当你与同事交谈时，只需说‘@GitHub，开始吧’，然后基本上就实现了这个功能。它会向你显示它已经开始，我可以在 Agent HQ 中查看它以继续这项工作。”

与 Linear 的集成也将以类似方式工作。正如 Daigle 所强调的，GitHub 希望存在于“灵感迸发”的时刻，并让开发者能够向代理发送一个注释，让它制定计划并将这个新想法通过代码实现。

## GitHub 代码质量

伴随此次发布，GitHub 还推出了 GitHub 代码质量的公开预览版。正如该公司所指出的，代码——无论是代理还是人工编写——可能通过了合并所需的测试，但仍可能降低代码库的整体质量。

该公司表示，新的代码质量功能旨在提供“组织范围内的可见性、治理和报告，以系统地提高每个存储库的代码可维护性、可靠性和测试覆盖率。”

特别是对于代理，GitHub 现在增加了一个代码审查步骤，它会对代码进行初步审查并检查是否存在任何问题。

[![](https://cdn.thenewstack.io/media/2025/10/69d4e408-code-quality.png)](https://cdn.thenewstack.io/media/2025/10/69d4e408-code-quality.png)

*新的 GitHub 代码质量功能现已进入公开预览版。（来源：GitHub）*

## 拥抱所有代理

所有这些都意味着 GitHub 正在直接邀请竞争对手进入其平台——但 Daigle 认为，这对开发者来说是正确的举措。

他告诉我：“所有这些技术都没有改变一个核心事实，那就是开发者会选择他们想选择的工具，而且他们很少百分之百地单独工作。这是一项团队运动，所以我们需要让他们能够作为团队的一部分来协作，而不是感觉‘好吧，因为我选择了这个工具，或者因为我选择了这个编程代理，我需要每天花八小时独自工作，然后再把它带回 GitHub，在那里我们才能协作。’”

[![](https://cdn.thenewstack.io/media/2025/10/38377782-914a8511-b234-474d-92b4-255935e13dab-scaled.jpg)](https://cdn.thenewstack.io/media/2025/10/38377782-914a8511-b234-474d-92b4-255935e13dab-scaled.jpg)

*GitHub 首席运营官 Kyle Daigle 介绍了 GitHub 作为所有开发者和代理之家的全新愿景（图片来源：The New Stack）。*

“所以明年、下个月、下周，我们将继续寻找这样的时刻：哦，我们可以让开发者选择这个，你可以成为 GitHub 的一部分，而不是非此即彼。”

该公司还推出了与 [Slack](https://api.slack.com/?utm_content=inline+mention) 和 [Linear](https://linear.app/) 的新集成，Linear 是一款流行的事务跟踪和项目管理工具，常与 GitHub 协同使用。

该公司表示，2025年每秒钟都有新的开发者加入 GitHub。目前，这个[微软](https://news.microsoft.com/?utm_content=inline+mention)旗下的开发者平台上有超过1.8亿开发者。随着 AI 编程代理越来越受欢迎，生成的代码量——以及能够编写代码的人数——将只增不减。