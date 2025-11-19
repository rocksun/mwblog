[Google](https://cloud.google.com/?utm_content=inline+mention) 今日[发布](https://antigravity.google/blog/introducing-google-antigravity) 了其最新的代理式开发平台实验—— [Antigravity](https://antigravity.google)。Antigravity 搭载了[新的 Gemini 3 模型](https://blog.google/products/gemini/gemini-3/)，结合了目前相当主流的以 AI 为中心的 IDE 和一些创新，Google 表示这些创新将 IDE “朝着以代理为先的未来发展”。

Antigravity 今天起可免费公测，支持 Mac、Windows 和 Linux，并为 Gemini 3 Pro 的使用提供了 Google 所称的“慷慨的速率限制”。

[![Google Antigravity 开发工具的演示。](https://cdn.thenewstack.io/media/2025/11/fe306be4-google-antigracity-demo.gif)](https://cdn.thenewstack.io/media/2025/11/fe306be4-google-antigracity-demo.gif)

Google 新的 Antigravity 代理式开发工具演示。（图片来源：Google）

## 模型选择：Gemini、Claude 和 GPT-OSS

一个有趣的方面是，Gemini 3 并非开发者唯一可选择的模型。他们还可以使用 Anthropic 的 Claude Sonnet 4.5 和 OpenAI 的开源 GPT-OSS 模型来驱动代理。

Google 解释说：“我们将根据我们的能力提供模型访问权限，并设置速率限制以防止滥用，这些限制每五小时刷新一次。”

Google 和 Anthropic 最近宣布了[一项价值数十亿美元的重大云合作](https://www.cnbc.com/2025/10/23/anthropic-google-cloud-deal-tpu.html)。这也许是交易的一部分。

## 下一代代理式编码

IDE 本身将为开发者提供对其编辑器视图中的代码的访问权限，以及任何现代开发环境的常用功能，包括标签补全和行内命令。

DeepMind 的 CTO 和 Google 的首席 AI 架构师 [Koray Kavukcuoglu](https://www.linkedin.com/in/koray-kavukcuoglu-0439a720/) 在今天发布前的新闻发布会上表示：“我们意识到，LLM（语言模型）已经从根本上改变了人们编码的方式，以及我们构建软件、实现创意的方式。因此，今天，为了推动模型和 IDE 协同工作的边界，我们推出了 Google Antigravity。这是我们的新代理式开发平台。我认为，思考如何通过专用的代理界面来开发软件是一个重要的概念，这个界面能够让开发者在这些更高层次、面向任务的水平上进行操作。”

代理式编码显然已经不再新鲜，也远未达到炒作周期的顶峰。但我们现在看到的是围绕这个概念的持续创新流。虽然无法判断 Google 的新模型在这个环境中的表现如何，但 Google 正在拓展整体开发者体验的边界。

[![Google Antigravity 代理式编码工具的 Logo（来源：Google）。](https://cdn.thenewstack.io/media/2025/11/9fa23e7d-googleantigravitylogo-whitebackground.png)](https://cdn.thenewstack.io/media/2025/11/9fa23e7d-googleantigravitylogo-whitebackground.png)

图片来源：Google。

## 信任但验证

例如，该公司认为，同类工具通常要么向用户展示编码代理所做的每一次操作和工具调用，要么只在没有上下文的情况下显示最终代码。“这两种方式都无法让用户信任代理所进行的工作，”Antigravity 团队在今天的公告中写道。

在 Antigravity 中，代理会生成 Google 所称的“产物”（artifacts），它将其定义为“用户比原始工具调用更容易验证的交付物格式”，包括任务列表、实施计划、屏幕截图和浏览器录屏。该公司表示，这样做的目的是确保用户可以信任代理已经验证了它的工作。

Kavukcuoglu 解释说：“你可以查看代理是如何执行的，以及沿途完成了哪些状态。代理将通过在 Chrome 浏览器中运行应用程序来验证其工作，并在完成后，展示最终产品工作方式的演练。”

## 代理管理器

Antigravity 试图弥合现有代理式编码范式与新想法之间差距的另一个例子是，它专注于所谓的“以代理为先的管理器界面”（agent-first Manager surface），团队将其描述为一种“任务控制中心”，用于在代理异步处理任务时生成、编排和观察它们。

偏好更传统模式的用户，即带有编辑器视图和侧边代理面板的用户，可以选择这样做，但 Antigravity 团队认为，“我们正在迈向一个新时代，随着 Gemini 3 等模型的出现，代理可以同时在所有这些界面上自主运行。”

团队写道：“除了 IDE 式的编辑器界面，我们还引入了一个以代理为先的管理器界面，它颠覆了代理嵌入界面的范式，转变为界面嵌入代理的模式。”

## 引导代理

要引导代理，开发者可以在代理创建的产物上写类似 Google Docs 的评论，或对其显示的屏幕截图提供反馈。随着时间的推移，代理会通过维护一个基于先前工作的内部知识库来学习这些反馈。这可能包括代码片段或它如何成功完成先前任务的任务列表。

## Gemini CLI 和 Jules 呢？

这个新工具加入了 Google 平台上现有的代理式编码工具，例如 [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/)、[Jules 编码代理](https://jules.google/) 以及 Google AI Studio 中[最近推出的](https://blog.google/technology/developers/introducing-vibe-coding-in-google-ai-studio/) 氛围编程（vibe coding）模式。它们都从不同的角度处理这项技术，其中一些（如 Jules 和现在的 Antigravity）明确是实验性的。目前看来，Gemini CLI 是最受欢迎的服务。其他这些工具能否长期存在，仍有待观察。