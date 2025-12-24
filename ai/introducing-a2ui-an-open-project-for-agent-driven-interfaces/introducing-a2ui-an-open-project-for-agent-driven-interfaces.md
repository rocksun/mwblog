<!--
title: A2UI重磅发布：打造智能体驱动界面的开放项目
cover: https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/train-gpt2-model-with-jax-on-tpu-.2e16d0ba.fill-1200x600.png
summary: A2UI是开源项目，使代理能安全生成跨平台、原生风格的UI，解决文本交互低效及跨信任边界渲染难题，提升用户体验。
-->

A2UI是开源项目，使代理能安全生成跨平台、原生风格的UI，解决文本交互低效及跨信任边界渲染难题，提升用户体验。

> 译自：[Introducing A2UI: An open project for agent-driven interfaces](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/)
> 
> 作者：Google A2UI Team

生成式AI在生成文本、图像和代码方面表现出色。现在，是时候将其用于生成上下文相关的**界面**了。今天，我们公开了[A2UI](https://github.com/google/A2UI/)项目，以便我们能在这个早期阶段的*格式*和*实现*上与他人协作。A2UI旨在解决代理生成的可互操作、跨平台、生成式或基于模板的UI响应所面临的特定挑战。A2UI允许代理生成最适合当前与代理对话的界面，并将其发送到前端应用程序。我们一直在为我们的一些产品构建A2UI，我们希望与社区互动，帮助完善A2UI规范，添加更多传输方式，并添加更多客户端渲染器和集成。

**A2UI**是一个开源项目，包含一种针对表示可更新、代理生成的UI而优化的格式，以及一套初始的渲染器，它允许代理生成或填充丰富的用户界面，以便它们可以在不同的宿主应用程序中显示，并由Lit、Angular或Flutter等一系列UI框架（未来还将支持更多）渲染。渲染器支持一组通用组件和/或客户端声明的一组自定义组件，这些组件被组合成布局。客户端拥有渲染权，可以将其无缝集成到自己的品牌用户体验中。编排器代理和远程A2A子代理都可以生成UI布局，这些布局以消息而非可执行代码的形式安全传递。

下面是A2UI渲染卡片的示例，展示了A2UI可以实现各种UI组合。

![a2ui-blog-1-component-gallery (2)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-1-component-gallery_2.original.png)

## **问题：代理需要“说”UI**

想象一个旨在帮助您预订餐厅餐桌的代理。仅文本的交互可能涉及笨拙的来回对话：

**用户：**（输入）“预订一张两人桌。”

**代理：**“好的，哪一天？”

**用户：**（输入）“明天。”

**代理：**“什么时间？”

**用户：**（输入）“也许晚上7点”

**代理：**“我们那时没有预订空位，还有其他时间吗？”

**用户：**（输入）“你们什么时候有空位？”

**代理：**“我们5:00、5:30、6:00、8:30、9:00、9:30和10:00有空位，这些时间对您合适吗？”

这可能缓慢且低效。更好的体验是**代理快速生成或使用**一个带有日期选择器、时间选择器和提交按钮的简单表单。借助A2UI，大型语言模型（LLM）可以从组件库中组合定制的UI，为手头的特定任务提供图形化、美观、易用的界面。

例如，您可以使用A2UI来组合这个预订UI，而不是上面基于文本的聊天来回对话。下面是餐厅预订的A2UI表示的一种可能渲染，由于A2UI的设计赋予了前端宿主应用程序对样式的很多控制权，因此还有许多其他可能性。

![a2ui-blog-2-reserve-table](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-2-reserve-table.original.png)

## **挑战：跨信任边界渲染**

我们正在进入多代理网络时代。来自Google的代理正在与来自Cisco、IBM、SAP和Salesforce的代理对话，以解决复杂的任务。这就是为什么我们共同创建了[代理间（A2A）协议](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)并将其捐赠给Linux基金会：以使代理即使不共享内存、工具或上下文也能协作。

然而，这种去中心化带来了用户界面问题。

如果您的代理存在于您的应用程序内部，它可以直接操作视图层（例如DOM）。但在多代理世界中，执行工作的代理通常是远程的——在后台、不同的服务器上运行，或者由不同的组织拥有。它不能直接触及您的UI；它必须发送消息。

历史上，从远程、不受信任的源渲染UI意味着发送HTML或JavaScript并将其在**iframe**中沙盒化。这种方法很重，可能会在视觉上脱节（它很少与您应用程序的原生样式匹配），并且在安全边界方面引入了复杂性。

我们需要一种传输UI的方法，这种方法**像数据一样安全，但像代码一样富有表现力**。

## **解决方案：将UI规范作为消息序列**

A2UI提供了一种标准格式，可以作为结构化输出即时生成，或用作模板并用值填充。生成此响应的代理可能是远程A2A代理或用户正在交互的编排器。JSON负载可以通过A2A、AG UI以及可能其他传输方式发送到客户端。客户端应用程序使用其自己的原生UI组件进行渲染。这意味着**客户端保留对样式和安全性的完全控制**，有助于确保代理的输出始终与您的应用程序原生集成。

[视频](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/landscape-architect-demo.mp4)


在此示例中，用户上传了一张照片，远程代理使用Gemini理解它，并为景观客户的特定需求制作了一个定制表单。

[视频](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/a2ui-custom-compnent.mp4)


在此示例中，代理决定用一个包含交互式图表的自定义组件和一个包含Google地图的自定义组件进行响应。

## **核心理念：安全、可更新、解耦**

我们围绕几个关键原则设计了A2UI：

*   **安全至上：** 运行LLM生成的任意代码可能会带来重大的安全风险。A2UI是一种*声明式*数据格式，而非可执行代码。您的客户端应用程序维护一个受信任、预批准的UI组件（例如，`Card`、`Button`、`TextField`）“目录”，代理只能请求渲染该目录中的组件。这有助于您降低UI注入和其他漏洞的风险。
*   **对LLM友好且可增量更新：** UI表示为带有ID引用的组件扁平列表，这使得LLM可以轻松地增量生成，从而实现渐进式渲染和响应式用户体验。代理可以根据对话进展中新的用户请求，高效地对UI进行增量更改。
*   **与框架无关且可移植：** A2UI将UI*结构*与UI*实现*分离。代理发送组件树及其相关数据模型的描述。您的客户端应用程序负责将这些抽象描述映射到其原生小部件——无论是Web组件、Flutter小部件、React组件、SwiftUI视图还是其他任何东西。来自代理的相同A2UI JSON负载可以在基于不同框架构建的多个不同客户端上渲染。

![a2ui-blog-3-end-to-end-data-flow](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-3-end-to-end-data-flow.original.png)

## **探索代理UI生态系统**

代理UI领域发展迅速，优秀的工具不断涌现以解决技术栈的不同部分。我们认为A2UI并非这些框架的替代品，而是一种专用协议，旨在解决**可互操作、跨平台、生成式或基于模板的响应**这一特定问题。

为了帮助您选择合适的工具或工具组合，以下是我们对当前格局的概述：

**1. 构建“宿主”应用程序UI**

如果您正在构建一个全栈应用程序（用户交互的“宿主”UI），除了实际构建UI之外，您还可以利用一个框架（**AG UI、Vercel AI SDK、已经在使用A2UI的Flutter版GenUI SDK**）来处理“管道”：状态同步、聊天历史和输入处理。

*   **A2UI的适用之处：** A2UI是互补的。如果您使用AG UI连接您的宿主应用程序，它可以将A2UI作为数据格式来渲染来自宿主代理以及第三方或远程代理的响应。这为您提供了两全其美：一个功能丰富、有状态的宿主应用程序，可以安全地渲染来自其不控制的外部代理的内容。
*   **A2UI与A2A：** 您可以直接通过A2A发送到客户端前端。
*   **A2UI与AG UI：** AG UI提供脚手架，可轻松构建和部署支持A2UI的应用程序。
*   **A2UI与REST**及其他传输方式是可行的，但尚未提供。

**2. UI作为“资源”（MCP应用程序）**

**模型上下文协议（MCP）**[最近引入了**MCP应用程序**](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)，这是一项整合了MCP-UI和OpenAI工作的新标准，旨在使服务器能够提供交互式界面。这种方法将UI视为一种资源（通过`ui:// URI`访问），工具可以返回该资源，通常在沙盒化`iframe`中渲染预构建的HTML内容，以确保隔离和安全。

**A2UI的不同之处：** A2UI采用“原生优先”方法，这与MCP应用程序的资源获取模型截然不同。A2UI代理发送的是原生组件的蓝图，而不是检索要在沙盒中显示的不透明负载。这使得UI能够完美继承宿主应用程序的样式和可访问性功能。在多代理系统中，编排器代理可以轻松理解子代理发出的轻量级A2UI消息内容，从而实现代理之间更流畅的协作。

**3. 平台特定生态系统（OpenAI ChatKit）**

像**ChatKit**这样的工具为专门在OpenAI生态系统内部署代理提供了高度集成、优化的体验。

**A2UI的不同之处：** A2UI专为在Web、Flutter和原生移动设备上构建自己的代理界面，或为代理需要在信任边界之间通信的企业网络（如**A2A**）的开发者而设计。A2UI以代理为代价，赋予客户端对样式更多的控制权，以实现与宿主客户端应用程序更高程度的视觉一致性。

## **为真实世界而生**

从第一天起，A2UI就与Google内部和外部的多个团队合作开发，以解决实际问题。我们很高兴能得到以下关键合作者的支持：

**AG UI / CopilotKit：强大组合**

我们相信协作生态系统。[AG UI](https://ag-ui.com/) / [CopilotKit](https://www.copilotkit.ai/)背后的团队与我们合作，确保了零日兼容性，为开发者提供了强大的“强强联合”故事。

> *“代理-用户交互协议（AG-UI）连接代理后端和代理前端。它为开发者提供了构建丰富全栈代理应用程序的实用构建块。AG-UI完全支持A2UI规范，用于代理动态生成的丰富声明式生成UI。AG-UI还实现了与A2A协议的完整握手，以实现与任何A2A系统的无缝全功能集成。我们很高兴能提供AG-UI和A2UI之间的零日兼容性。”* — Atai Barkai，CopilotKit和AG UI的创始人

**Opal：为实验性AI小程序提供动力**

[Opal](http://opal.google/)让数十万人可以使用自然语言构建、编辑和共享AI小程序。Google的Opal团队是A2UI的核心贡献者。除了帮助构建A2UI，该团队还一直在使用它来**快速原型设计**并将其集成到核心应用构建流程中。Opal中的A2UI将使任何人都能构建具有动态、生成式UI的AI小程序，为每个用例定制。在接下来的几周里，您将能够在Opal中看到并体验A2UI的实际应用。

> *“A2UI是我们工作的基础。它赋予我们灵活性，让AI以新颖的方式驱动用户体验，而不受固定前端的限制。其声明性本质和对安全性的关注使我们能够快速安全地进行实验。”* — Dimitri Glazkov，Opal团队首席工程师

**Gemini Enterprise：企业代理的自定义UI**

Gemini Enterprise使企业能够构建强大的自定义AI代理。A2UI正在被集成，以允许这些企业代理在其宿主应用程序中渲染丰富、交互式的UI。

> *“我们的客户需要他们的代理不仅仅是回答问题；他们需要代理引导员工完成复杂的工作流程。A2UI将允许在Gemini Enterprise上进行开发的开发者让他们的代理生成任何任务所需的动态、自定义UI，从数据录入表单到审批仪表板，极大地加速工作流自动化。”* — Fred Jabbour，Gemini Enterprise产品经理

**Flutter：多平台生成式UI应用体验**

[Flutter](http://flutter.dev/)及其[GenUI SDK](https://github.com/flutter/genui)帮助您使用Gemini（或其他LLM）生成动态、个性化的UI，显著提升您的生成式AI和基于代理的用户体验的可用性和满意度。这些生成式UI遵循您既定的品牌准则并使用您自己的小部件目录。GenUI SDK使用A2UI作为远程服务器端代理与应用之间的UI声明格式。

> *“我们的开发者选择Flutter是因为它让他们能够快速创建富有表现力、品牌丰富、自定义的设计系统，这些系统在每个平台上都感觉很棒。A2UI非常适合Flutter的GenUI SDK，因为它确保了每个用户，在每个平台上，都能获得高质量的原生体验。”* — Vijay Menon，Dart工程总监

**AI Powered Google：标准化代理UI**

随着Google在公司范围内采用AI，A2UI为团队提供了一种标准化方式，使AI代理能够交换用户界面，而不仅仅是文本。这种互操作性允许代理在任何前端渲染，支持涉及每个界面多个代理或每个代理多个界面的工作流程，并使内部构建的代理可以轻松地对外公开，例如在Gemini Enterprise中。

> *“就像A2A允许任何代理与另一个代理对话，无论平台如何，A2UI标准化了用户界面层，并通过编排器支持远程代理用例。这对内部团队来说非常强大，使他们能够快速开发以丰富用户界面为常态而非例外情况的代理。随着Google在生成式UI领域的进一步推进，A2UI为在任何客户端渲染的服务器驱动UI提供了一个完美的平台。”* — James Wren，AI Powered Google高级工程师

## **开始使用：尝试A2UI**

了解A2UI的最佳方式是亲眼看看它的实际应用。

*   首先访问[a2ui.org](http://a2ui.org/)并阅读快速入门指南和文档。
*   接下来进入`samples`文件夹，尝试一个客户端UI和一些后台示例代理，也许是餐厅查找器。

以下是启动餐厅查找器的方法：

```
git clone https://github.com/google/A2UI.git
export GEMINI_API_KEY="your_gemini_api_key"


cd A2UI/samples/agent/adk/restaurant_finder
uv run .


cd A2UI/samples/client/lit/shell
npm install
npm run dev
```

Shell

另一种查看A2UI实际应用的方法是尝试Flutter的GenUI SDK。

GenUI SDK for Flutter在与远程或服务器端代理通信时，底层使用A2UI。它很容易上手，请访问<https://docs.flutter.dev/ai/genui>或观看[GenUI入门视频](https://www.youtube.com/watch?v=nWr6eZKM6no)。在GitHub上的GenUI SDK仓库中，您还可以找到一个[使用A2UI的客户端-服务器示例](https://github.com/flutter/genui/tree/main/examples/verdure)。

CopilotKit还有一个公共的[A2UI小部件构建器](https://go.copilotkit.ai/A2UI-widget-builder)供您尝试。

## **支持的集成**

以下是该项目目前拥有的一些关键集成，以及我们希望项目未来能支持的一些集成。我们欢迎社区在这些领域做出贡献。

![a2ui-blog-4-checklist](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/a2ui-blog-4-checklist.original.png)

## **未来是开放的：加入我们！**

今天标志着A2UI的第一个公开里程碑。我们的格式目前是`v0.8`，因为我们已经针对初始用例进行了多轮的实战强化和测试，未来还有更多内容需要发展和发现。我们为**Flutter**、**Web Components**和**Angular**提供了早期但可用的客户端库。

随着项目现已开源，我们很高兴能与生态系统合作，共同：

*   完善和发展格式
*   将A2UI连接到您喜欢的客户端库中
*   未来构建更强大和有用的工具
*   为开发者入职培训做贡献并提供示例

A2UI是一个Apache 2许可项目，我们相信它的成功取决于社区。我们邀请您探索代码，尝试演示，尤其是做出贡献。无论您是想为自己喜欢的UI框架构建客户端，为代理构建库添加支持，还是构建一个出色的演示，我们都期待您的声音并与您合作。

查看我们的[公共路线图](https://github.com/google/A2UI/blob/main/ROADMAP.md)以了解我们的发展方向，并找出您如何参与其中。让我们共同构建代理用户体验的未来。