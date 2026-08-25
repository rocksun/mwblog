<!--
title: Spline重构整个3D编辑器，并将控制权交给了Claude Code
cover: https://cdn.thenewstack.io/media/2026/05/30be87ed-daniel-lee-zhpam5xxvwk-unsplash-scaled.jpg
summary: Spline发布V2版本，重构了3D编辑器并集成MCP服务器。开发者现在可以通过Claude Code、Cursor等AI代理直接在实时场景中进行编辑，实现了设计与代码的无缝交互，极大提升了开发与设计的协作效率。
-->

Spline发布V2版本，重构了3D编辑器并集成MCP服务器。开发者现在可以通过Claude Code、Cursor等AI代理直接在实时场景中进行编辑，实现了设计与代码的无缝交互，极大提升了开发与设计的协作效率。

> 译自：[Spline rebuilt its entire 3D editor. Then it handed the keys to Claude Code.](https://thenewstack.io/spline-v2-mcp-agents/)
> 
> 作者：Amanda Caswell

Spline 在周四发布了 V2 版本，对其 3D 编辑器进行了彻底重构，使外部编码代理能够直接在实时、可编辑的场景上进行工作。

关键的新增功能是 Spline MCP 服务器，它向 Claude Code、Cursor、Codex、Google Antigravity 和 VS Code 开放了编辑器。通过随桌面应用程序捆绑的本地服务器，这些工具可以直接在实时的 Spline 项目中工作，在更改场景及其行为的同时，保持结果完全可编辑。

Spline V2 还包含其内置的 AI 代理，该代理可以根据提示构建和编辑场景。MCP 让开发人员能够从一个已经理解代码库和当前工作的编码代理中访问相同的环境，而无需在单独的 Spline 对话中重建该上下文。

> 通过随桌面应用程序捆绑的本地服务器，这些工具可以直接在实时的 Spline 项目中工作，在更改场景及其行为的同时，保持结果完全可编辑。

## MCP 调用直接作用于实时场景

MCP 服务器直接捆绑在 Spline 为 macOS 和 Windows 重构的桌面应用程序中；它不能在浏览器中工作，也没有可安装的独立服务器包。

当桌面应用程序打开时，它会查找受支持的客户端并在其配置文件中注册服务器。然后，开发人员重启 AI 客户端并正常发出提示词。例如，如果有人要求 Claude Code 创建一个浮岛，Claude 会将该请求转换为结构化的 MCP 工具调用。Spline 然后将这些调用路由到一个打开的 3D 编辑器选项卡，在那里它们针对实时文档运行。如果没有打开合适的文件，应用程序可以创建一个。

该模型在开始进行更改之前可以看到场景中已经发生的情况，这使它能够在视觉设计和在画布上运行的代码之间切换，在需要新模型或图像时使用 Spline 的 AI 工具，并继续处理周围的界面或游戏逻辑。

它所做的所有更改都保留在 Spline 项目中，因此设计师得到的是实时场景，而不是扁平化的图像或静态网格，并且可以在代理完成工作后立即继续编辑。

Spline 表示其内部 AI 代理遵循相同的方法，每次更改都被视为正常的编辑器操作，出现在撤销历史记录中，并同步给文件中的其他人。Spline 并不是唯一将 MCP 钥匙交给外部代理的创意平台。ElevenLabs 最近[将其语音代理基础设施通过 MCP 服务器向 Claude 开放](https://thenewstack.io/elevenlabs-mcp-voice-agents/) —— 让聊天窗口管理生产语音代理，正如 Spline 现在让编码代理管理 3D 场景一样。

> 它所做的所有更改都保留在 Spline 项目中，因此设计师得到的是实时场景，而不是扁平化的图像或静态网格，并且可以在代理完成工作后立即继续编辑。

## 代理跨越画布鸿沟

当代理需要在应用程序及其界面之间移动时，这种设置会变得更有用，因为 Spline V2 将 3D 编辑器和 Hana 置于同一个 MCP 连接之后，并自动处理切换，将场景工作导向 3D 编辑器，将界面更改导向 Hana。

在 Hana 中，代理可以将现有的组件转换为可编辑的框架，然后将任何视觉更改带回应用程序代码中，利用导出元素上的稳定引用在源代码中找到正确的位置。

这种往返是有局限性的，因为 Hana 只支持围绕 flexbox 构建的 HTML 和 CSS 的子集，因此复杂的标记和框架特定的组件可能需要与现有代码协调，而不是直接替换。

对于 3D 工作，开发人员可以通过 Claude Code 构建或更改场景，在 Spline 中进行视觉上的细化，并以从 Vanilla JavaScript 和 Three.js 到 React、Next.js 和 React Three Fiber 等多种格式导出到 Web。这些导出默认使用 WebGPU，并在必要时回退到 WebGL。

Spline 的运行时 API 可以控制已发布的场景，但该公司没有记录一种将对导出代码所做的更改流回原始 3D 文件的方法。如果代理需要修改该源代码，它必须通过 MCP 返回并在实时编辑器中工作。

Google Antigravity 最近才通过 [VS Code 和 JetBrains 的扩展](https://thenewstack.io/google-antigravity-ide-extensions/)扩展到其自己的 IDE 之外 —— Spline 现在给了它另一个可以工作的界面。OpenAI 的 Codex，另一个受支持的客户端，最近获得了[在等待开发人员回答时保持编码](https://thenewstack.io/codex-async-developer-messaging/)的能力。

## 导出前的编辑至关重要

Spline 已经提供了一个代码 API，允许 Web 应用程序在运行期间使用 JavaScript 来控制已发布场景的状态和行为。

MCP 服务器在场景仍在构建时发挥作用，使代理能够直接访问可编辑的文档，以便它可以在导出前了解其结构并进行更改。在这里，MCP 作为编辑器的控制界面，而 Spline 继续管理视觉项目并实时渲染更改。

## 本地服务器，作用域访问

连接保留在开发人员的计算机上，服务器绑定到 `127.0.0.1`，并由阻止任意网页的源白名单保护。开发人员可以通过 Spline 的 MCP 设置选择哪些客户端具有访问权限。

据 Spline 称，与其 MCP 服务器交换的提示词和场景数据保留在桌面应用程序和连接的客户端之间。但是，如果代理使用 Spline 的 AI 生成功能之一，那么该工作仍会在云端运行，就像手动从编辑器启动一样。

多个代理会话可以连接到同一个编辑器，但 Spline 的文档没有解释团队如何在发布共享文件之前归因或审查个人的 MCP 更改。

> 多个代理会话可以连接到同一个编辑器，但 Spline 的文档没有解释团队如何在发布共享文件之前归因或审查个人的 MCP 更改。