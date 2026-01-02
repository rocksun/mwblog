<!--
title: 2025前端AI巨变：颠覆浪潮来袭
cover: https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1.png
summary: 2025年前端AI发展迅猛，从代码生成到系统感知组件。Figma鸿沟缩小，LLM更专业，AX成关键。MCP标准化代理与UI通信，自组装界面兴起。
-->

2025年前端AI发展迅猛，从代码生成到系统感知组件。Figma鸿沟缩小，LLM更专业，AX成关键。MCP标准化代理与UI通信，自组装界面兴起。

> 译自：[2025’s Radical Frontend AI Shift](https://thenewstack.io/2025s-radical-frontend-ai-shift/)
> 
> 作者：Loraine Lawson

当我们回顾 2024 年时，人工智能既引人担忧又备受炒作——但那时，前端的功能还不多。这种情况在 2025 年迅速改变，人工智能在网络开发中的应用从代码生成演变为系统感知组件和插件的创建。这一年也见证了[开发者们超越了通用聊天机器人](https://thenewstack.io/move-beyond-chatbots-plus-5-other-lessons-for-ai-developers/)时代，通过一类更好地理解 UI/UX 的新型生成工具，将人工智能直接融入前端架构。

## “Figma 鸿沟”的终结与代码优先原型的兴起

年初，TNS 重点介绍了 [WebCrumbs 的前端人工智能项目](https://thenewstack.io/genai-helps-frontend-developers-create-components/)，这是一个为开发者创建插件或模板的生成式人工智能模型，可以将代码导出为 CSS/Tailwind、HTML、React、Angular、Svelte 或 Next.js。这使其与 Vercel 的 v0 区分开来，v0 最初将 Next.js 和 Tailwind 紧密耦合。（v0 现在提供更灵活的 React、[Svelte、Vue 和 Remix](https://v0.app/docs/faqs) 导出，以及标准的 CSS 代码。）WebCrumbs Frontend AI 还集成了代码编辑器和 Visual Studio。

根据其网站显示，[WebCrumbs 及其 Frontend AI](https://www.webcrumbs.ai/) 现已关闭。但这预示着年末即将发生的一切，因为开发转向了组件的创建以及与前端开发工作的更多集成。

> 我们看到“Figma 鸿沟”正在缩小，新工具可以同时生成代码和设计。

我们还看到“Figma 鸿沟”正在缩小，因为新工具同时生成代码和设计，确保开发者在视觉编辑器中看到的内容与浏览器中渲染的内容一致。

但一些人，包括 [Bolt（一个基于人工智能的在线网络应用构建器）](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/)的首席执行官 Eric Simons，预见到更大的转变即将到来，这可能会让同时创建和设计变得更容易。Simons 认为这可能会让 Figma 鸿沟变得无关紧要。

Simons 当时在一条推文中表示：“我们进入了一个新时代，现在用代码制作工作原型比在 Figma 中设计它们更快。”

值得注意的是，[Bolt](https://bolt.new/) 仍然包含上传 Figma 文件的方式，这表明我们尚未完全达到代码与设计融合的阶段。

尽管如此，新的界面允许进行视觉调整——间距、颜色、字体——而不是要求人工智能为一个小改动重写整个文件，这些调整可以即时与代码同步。

## LLM 推理革命

实现这一目标的一个因素是大型语言模型（LLM）的转变。随着人工智能公司创建了针对开发以及专业人工智能开发工具进行优化的模型，LLM 不再是通用模型。

2024 年年中，[Claude Artifacts 发布](https://thenewstack.io/is-react-now-a-full-stack-framework-and-other-dev-news/)，预示了 2025 年将发生什么。它提供了一个人工智能驱动的 UI 功能，带有一个侧面板，允许开发人员在模型编写代码时实时查看或与 React 或 HTML 代码交互。

接着在 2025 年 4 月，我们看到了 [OpenAI 的 GPT-4.1 发布](https://thenewstack.io/openai-releases-new-models-trained-for-developers/)，它专门为编码和指令遵循进行了调整，拥有 100 万个 token 的上下文窗口。OpenAI 还发布了带有 o3 和 o4 模型的推理版本，引入了使用图像的能力。开发者突然可以将白板草图或 UI 截图直接转换为逻辑推理链。

2025 年初，Anthropic 发布了 [Claude 3.7 Sonnet](https://thenewstack.io/making-the-fediverse-more-accessible-with-claude-3-7-sonnet/)。其突出特点是双重思维模式，允许开发者在标准快速响应和“扩展思维”模式之间切换。这对前端至关重要，因为它允许处理复杂的 UI 逻辑或状态管理问题。

谷歌还在 5 月推出了实验性的 [Google Stitch](https://developers.googleblog.com/stitch-a-new-way-to-design-uis/)。它由 Gemini 3 提供支持，直接与 Figma 集成，可以读取设计文件并生成遵循特定设计系统规则（例如 Material Design）的高保真前端代码。

## AX 优于 DX：使用 MCP 标准化代理与 UI 的通信

1 月份，Netlify 首席执行官 Matt Biilmann 与 TNS 谈论了 [AX（代理体验）](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/)，他认为我们现在设计网站既要为人类用户服务，也要为人工智能代理服务。这一警告我们在这一年里反复听到，不仅是关于网站，[甚至关于 API](https://thenewstack.io/its-time-to-start-preparing-apis-for-the-ai-agent-era/)。到 6 月，我们听到 PayPal 等公司重复这一观点，他们已经开始努力使其 [PayPal API 更加代理友好](https://thenewstack.io/paypal-on-how-to-prepare-apis-for-agentic-ai-future/)。

公司实现这一目标的一种方式是使用[模型上下文协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)。MCP 服务器迅速出现，成为人工智能代理[如何与应用数据通信的行业标准](https://thenewstack.io/agent-ui-standards-multiply-mcp-apps-and-googles-a2ui/)。MCP-UI 等扩展允许这些代理不仅获取数据，还可以从服务器“拉取”丰富的、品牌化的 UI 组件，并在聊天界面中显示它们（例如，航班选择器直接出现在 Claude 或 ChatGPT 窗口中）。

> MCP 服务器迅速出现，成为人工智能代理如何与应用数据通信的行业标准。

MCP 服务器很快成为那些希望与开发者分享文档最佳实践的公司和 JavaScript 框架的必备条件。今年，[Angular 和 React 都推出了 MCP 服务器](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)，我们听说其他框架也纷纷效仿。

这一年也看到了“自愈 UI”的出现，它们使用嵌入在仪表板中的代理——例如 [Netlify 的 Agent Runners](https://thenewstack.io/new-netlify-agents-offer-ai-workflows-for-developers/)——可以扫描损坏的链接，识别可访问性违规，或修复移动设备上的响应式设计错误并自动提交拉取请求（Pull Request）。

## 生成式 UI：迈向自组装界面

所有这一切很快导致了 2025 年前端领域最根本性的转变：生成式 UI 的演进，即界面由人工智能根据用户的提示组装而成。虽然 LLM 从一开始就能够创建界面，但这些解决方案变得更加复杂和对开发者友好，从而允许更复杂的创建。

其中一个工具是我们在 12 月重点介绍的 [Hashbrown Framework](https://thenewstack.io/run-ai-agents-in-the-browser-with-the-hashbrown-framework/)。这个开源框架使人工智能代理能够完全在浏览器中运行。使用 Hashbrown 的应用程序可以部署一个 LLM，根据实时用户行为即时决定渲染哪些 UI 组件——填写表单、创建自定义图表或建议快捷方式。

它还通过 Skillet 库支持流式传输，解决了 LLM 在提示方面的速度问题。这使得 UI 能够在人工智能开始“思考”的瞬间开始渲染和动画组件，让体验感觉即时。通过利用 Chrome 和 Edge 中的实验性浏览器 API，这些工具还能够在设备上运行轻量级模型。这实现了“私有 AI”，无需将敏感用户数据发送到云服务器即可提供智能体验。

2025 年让我们预见到了人工智能在前端领域的可能性。我们期待在 2026 年发现哪些会留下，哪些会被淘汰。