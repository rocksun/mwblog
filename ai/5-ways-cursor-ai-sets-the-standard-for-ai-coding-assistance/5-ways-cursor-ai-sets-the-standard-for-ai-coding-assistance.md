
<!--
title: Cursor AI 设置 AI 编码辅助标准的 5 种方式
cover: https://cdn.thenewstack.io/media/2024/09/0833a258-liam-briese-wb7v7mhufy4-unsplash.jpg
-->

凭借其集成的环境和多功能特性，Cursor AI 为 AI 驱动的编码辅助设定了新标准。

> 译自 [5 Ways Cursor AI Sets the Standard for AI Coding Assistance](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/)，作者 Janakiram MSV。

Cursor AI 是一个 [AI-first 集成开发环境](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/)，将 AI 编码助手提升到一个新的水平。大多数编码助手都将 IDE 作为附加组件或插件，但 [Cursor AI](https://www.cursor.com/)（最流行的开源开发者工具 [Visual Studio Code](https://code.visualstudio.com/) 的一个分支）将 AI 功能直接嵌入到开发环境中。

Cursor AI 已经面世一年多了，但它最近在收到 [Andreessen Horowitz 的 6000 万美元 A 轮融资](https://techcrunch.com/2024/08/09/anysphere-a-github-copilot-rival-has-raised-60m-series-a-at-400m-valuation-from-a16z-thrive-sources-say/) 后登上了新闻头条。Cursor AI 还获得了 [Andrej Karpathy](https://x.com/karpathy)（前特斯拉自动驾驶负责人和前 [OpenAI](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/) 研究员）等行业领导者的高度评价。

> “编程的变化如此之快……我正在尝试使用 VS Code Cursor + Sonnet 3.5 来代替 GitHub Copilot，我认为它现在已经获得了全面胜利。根据经验，在过去几天里，我的大部分“编程”工作现在都是用英语编写。”
>
> — Andrej Karpathy (@karpathy), Twitter,[8 月 24 日]

Cursor AI 的功能扩展到更专业的应用程序，例如 11 Labs 用于视频编辑中 AI 画外音的 [Helper 应用程序](https://www.chaindesk.ai/tools/youtube-summarizer/cursor-composer-building-apps-end-to-end-develop-a-full-stack-apps-with-no-code-QFg3zSdeTos)。收入仪表板和 [Duolingo 克隆](https://prototypr.io/post/cursor-composer-cmdi) 的开发进一步说明了 Cursor 在创建多样化、实用应用程序方面的潜力。从交互式游戏到 Chrome 扩展程序，Cursor AI Composer 正在彻底改变各个领域的软件开发。

我已经使用 Cursor AI 几周了，以下是我最喜欢的能够显著提高 [开发人员生产力](https://thenewstack.io/three-key-metrics-to-measure-developer-productivity/) 的功能。

## 1. Composer

Composer 功能是 Cursor AI 最强大的功能。它几乎就像将产品经理起草的规范文档变成一个完整的应用程序。在典型情况下，是工程团队帮助产品经理将规范转化为代码。

在 Cursor 中，Composer 通过生成构建应用程序所需的所有工件来完成繁重的工作。规范是用简单的英语编写的，甚至可能包括 UI 模型和线框图。

![](https://cdn.thenewstack.io/media/2024/09/f5ee1ac4-cusror-1-1024x523.jpg)

Cursor AI Composer 通过几个令人印象深刻的作品展示了其在应用程序开发中的多功能性和强大功能。著名的例子包括一个功能齐全的任务管理器网络应用程序和一个完整的身份验证系统，展示了其处理复杂软件结构的能力。一个 8 岁的孩子成功构建了一个聊天机器人，这突出了该平台的可访问性，证明了其用户友好的特性。

在创建提示时，可以参考文件（如屏幕截图、数据库模式，甚至是文本文件）以及分步说明，以便为 Composer 提供上下文。

可以通过按 Shift+Command+I 热键来调用 Composer，这将弹出一个全屏编辑器。

在我的测试中，我利用 Composer 将现有数据集导入 PostgreSQL 数据库，并通过 REST API 端点公开它。我可以毫不费力地将数据库和 API 层打包到 [Docker](https://www.docker.com/?utm_content=inline+mention) Compose 文件中，并在我的开发机器上运行它——所有这些都不需要离开开发环境。在测试 API 后，我可以轻松创建包含用于在 Kubernetes 中部署应用程序的清单的 YAML 文件。

## 2. 随时随地聊天

目前大多数 AI 编码助手都局限于两个功能：编辑器中的代码补全和一个单独的聊天窗口。聊天窗口提供类似于 ChatGPT 的对话界面。

![](https://cdn.thenewstack.io/media/2024/09/ef89dc77-cusror-3-1024x621.jpg)

我喜欢 Cursor 的地方在于它能够在任何地方调用聊天输入框——在代码编辑器中、侧边栏中，甚至在终端窗口中。这是一个非常强大的功能，可以让开发人员控制工作流程。

![](https://cdn.thenewstack.io/media/2024/09/b8eba31a-cusror-3a-1024x305.jpg)

您可以选择一段代码并按 Command+K 重写或重构它，或者按 Command+L 在侧边栏中甚至在终端窗口中显示它。聊天输入最好的地方在于它能够记住历史记录，这使得编辑提示以更好地调整它们变得很容易。

## 3. 模型选择

Cursor 提供了对各种模型的访问，包括流行的 [Claude 3.5 Sonnet](https://www.anthropic.com/news/claude-3-5-sonnet) 和 [GPT-4o](https://thenewstack.io/reviewing-code-with-gpt-4o-openais-new-omni-llm/)。但令人印象深刻的是该工具能够引入您自己的模型。

![](https://cdn.thenewstack.io/media/2024/09/2f78e912-cusror-2a-1024x339.jpg)

开发人员可以将 Cursor 指向 [他们现有的帐户和订阅](https://thenewstack.io/generative-ai-cloud-services-aws-azure-or-google-cloud/)，以使用来自 Anthropic、[微软](https://news.microsoft.com/?utm_content=inline+mention) Azure、OpenAI 和 [谷歌](https://cloud.google.com/?utm_content=inline+mention) 的模型。Azure OpenAI 使开发人员能够使用提供安全性和合规性的专用端点。

您还可以将 Cursor 指向托管自定义模型的任何与 OpenAI API 兼容的端点。此功能可以使用户能够在任何 [推理引擎](https://thenewstack.io/5-open-llm-inference-platforms-for-your-next-ai-application/)（例如您自己基础架构上的文本生成推理服务器或 vLLM，或在 Runpod 和 [Fireworks AI](https://thenewstack.io/why-latency-and-total-cost-of-ownership-matter-more-in-ai-apps/) 等第三方基础架构上）托管代码生成器模型，例如 [CodeGemma](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/)、[Code Llama](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) 或 [Codestral](https://thenewstack.io/codestral-a-step-closer-to-ai-driven-coding-for-the-masses/)。

![](https://cdn.thenewstack.io/media/2024/09/4c0679cb-cusror-2-1024x342.jpg)

还可以动态切换模型。例如，您可以使用一个模型在 shell 中运行命令，而使用另一个模型生成代码。

## 4. 使用 @ Moniker 增强上下文

Cursor 最棒的功能是能够引用文件、文件夹、网络、文档，甚至是整个代码库。这是一个杀手级功能，使 Cursor 从竞争对手中脱颖而出。

![](https://cdn.thenewstack.io/media/2024/09/e175df87-cusror-4-1024x499.jpg)

当您使用 `@Codebase` 询问有关代码库的问题时，Cursor 会搜索与您的查询相关的代码。使用 `@Files` 引用文件允许您将特定文件带入上下文。这类似于将 ChatGPT 与 [自定义 GPT](https://thenewstack.io/getting-started-with-openais-gpt-builder-and-how-it-uses-rag/) 结合使用，这意味着您可以随时使用有关您自己的代码和应用程序的知识。

通过 `@Web` 添加网络搜索的功能使 Cursor 变成了一个类似 [Perplexity 的工具](https://thenewstack.io/accessing-perplexity-online-llms-programmatically-via-api/)。它可以搜索网络并从 StackOverflow 或与您的查询相关的其他来源获取答案。

最后，包含任何外部工具文档的功能是一个救星。Cursor 将抓取文档并将其转换为 [嵌入](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)，这些嵌入将用于代码生成和查询响应。

![](https://cdn.thenewstack.io/media/2024/09/a1dcb1fb-cusror-4a-1024x411.jpg)

我添加了 [Chroma DB](https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/) 文档，Cursor 指导我完成了索引、创建和查询集合的过程。

## 5. DevOps 工作流程自动化

我对 Cursor 最满意的是它能够处理端到端的应用程序生命周期，而无需离开开发环境。虽然 Composer 和 Tab 等功能可以解决代码生成问题，但终端内的聊天窗口是一个真正的游戏规则改变者。它可以生成和运行 shell 脚本、Docker 和 Kubernetes 命令，以及任何其他与 CLI 相关的工具。

虽然其他 AI 编码助手也有一个聊天窗口来响应与操作相关的查询，但它们需要复制和粘贴。但 Cursor 将需要执行的实际命令直接放在命令提示符处，从而显着加快了工作流程。

![](https://cdn.thenewstack.io/media/2024/09/f4ee4609-cusror-5-1024x370.jpg)

在我的测试用例中，我可以直接在编辑器窗口中生成 [Dockerfile](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，构建它们，标记它们，并通过用简单的英语提示 Cursor 将它们推送到 Docker Hub。在 Docker Compose 环境中生成和测试容器后，我可以将应用程序部署在云中运行的 Kubernetes 集群中。

![](https://cdn.thenewstack.io/media/2024/09/979f45a7-cusror-5a-1024x312.jpg)

Cursor 能够帮助我以无缝的方式从开发过渡到生产，而无需离开开发环境，这给我留下了深刻的印象。

Cursor AI 凭借其集成的环境、多功能的功能和无缝的工作流程自动化，正在改变开发方式。从强大的 Composer 工具到灵活的聊天功能和全面的模型选项，Cursor AI 提高了生产力并简化了开发流程。其整体方法为 AI 驱动的编码辅助设定了新标准。
