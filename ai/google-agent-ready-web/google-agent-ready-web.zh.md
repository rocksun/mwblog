在周二举行的 I/O 开发者大会上，谷歌发布了多项新功能和技术规范，计划将其 Chrome 浏览器及整个 Web 平台带入全新的智能体 AI（agentic AI）时代。

正如谷歌开发者倡导者 [Paul Kinlan](https://uk.linkedin.com/in/paulkinlan) 在公告中指出的，“智能体正在改变各处的开发方式，而这种变革在 Web 领域发生得最为迅速。它正在重新定义我们构建的内容、构建的方式以及构建者。随着我们进入智能体 Web 时代，我们看到了一种转变，它弥补了复杂的开发者工作流、底层平台能力与日常用户体验之间的差距。”

谷歌认为，Web 需要适应 AI 智能体的需求，让它们更容易与网站互动，而浏览器则需要更多地成为用户的专业助手。与此同时，开发者将寻找能够充分利用 Web 平台优势的工具，并在需要时由 AI 提供辅助。

## Chrome 中的 WebMCP

谷歌计划让智能体访问网站及其工具的核心是 WebMCP，这是一个新兴的开放标准，用于向智能体公开 JavaScript 函数和 HTML 表单等。

“WebMCP 的核心意义在于，我们希望 Web 体验能成为智能体工作流中的一等公民。WebMCP 允许网页此时向这些智能体公开具体的函数和能力，”Paul Kinlan 在发布前的媒体简报中表示。

理想情况下，WebMCP 允许智能体使用网站开发者为其启用的工具与站点进行交互。这比智能体尝试通过屏幕截图或遍历 DOM 来浏览站点要容易得多，而且速度也快得多。

不出所料，不少品牌对此也表现出了浓厚兴趣，包括 Booking.com、Expedia、Instacart、Intuit、Shopify 和 Redfin。

目前的计划是让 Chrome 很快支持 WebMCP API。谷歌正从 Chrome 149（目前处于测试版）中的 WebMCP Origin Trial（来源试用）开始。

对于开发者，谷歌现在允许他们[将自己的智能体引入 Chrome DevTools](https://developer.chrome.com/docs/devtools/agents)。智能体现在可以直接访问 DevTools 的功能，如控制台日志、网络流量和辅助功能树。你告诉智能体自己在控制台中看到了什么的时代已经一去不返了，它们现在可以直接看到正在发生的事情并做出相应反应。

这一能力已经存在了一段时间，但谷歌现在将其视为 1.0 版本，并已准备好投入日常使用。它已在谷歌自家的 Antigravity 应用以及 20 多个编码智能体中可用。该工具使用了 Chrome 内置的 MCP 服务器或 Chrome DevTools CLI（因为命令行界面现在又变酷了）。

![](https://cdn.thenewstack.io/media/2026/05/9d8c565e-3_-ai_assistance_devtools.gif)

Chrome DevTools 中的 AI 辅助。来源：Google。

## 编码智能体构建 Web 应用的蓝图

随着 AI 工具加快编码速度，Web 的变化速度也将比以前更快。通过 [Web Platform Baseline](https://web.dev/baseline)，谷歌和其他浏览器厂商定义了一套任何 Web 开发者都可以在现代浏览器中找到的核心能力。谷歌现在通过其全新的 [Modern Web Guidance（现代 Web 指南）](https://developer.chrome.com/docs/modern-web-guidance)更进一步。

该指南目前处于早期预览阶段，本质上是为 AI 编码智能体提供的一套技能，教导它们了解特定 Baseline 目标的能力。

“我们希望开发者能够确信，他们的编码智能体所使用的功能是大多数用户都能使用的，”Paul Kinlan 说。“如果他们的浏览器支持矩阵超出了 Baseline 的要求——也许他们稍微领先一点——我们也会提供回退策略，以应对用户使用的浏览器不支持某些功能的情况。”

对于想知道应该关注哪个 Baseline 目标的开发者，谷歌让他们能够轻松连接到 Google Analytics API，以查看用户正在使用哪些浏览器以及这些浏览器支持哪些现代 Web 功能。

## 更丰富的 Web UI

谷歌在 I/O 大会上宣布的一项重大更新虽然与智能体关系不大，但非常有下一代特性：HTML-in-Canvas API（结合元素级视图过渡）。如果你读到这里感到困惑，你并不孤单，但事实证明，这完全是为了视觉上的提升。

正如谷歌所言，HTML-in-Canvas API 将允许开发者“通过 WebGL 和 WebGPU 将真实的 DOM 元素直接集成到 Canvas 中，从而构建[沉浸式 3D 体验](https://github.com/GoogleChromeLabs/css-web-ui-demos/blob/main/html-in-canvas/awesome-html-in-canvas.md)，这些体验是可搜索、可访问、原生可翻译的，并且可以与内置浏览器功能无缝交互。”

这一切都是为了实现以前在 Web 上无法实现的丰富图形用户界面。`<canvas>` 元素已经存在[很长时间了](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)，它允许 Web 开发者使用 JavaScript 在页面上绘制图形。但在 `<canvas>` 元素内部，浏览器布局引擎是不可用的，这意味着没有文本折行、焦点管理、`<input>` 字段，也不支持复制粘贴等功能。

HTML-in-Canvas 将这两个世界结合在一起。来自布局引擎的实时 DOM 元素现在可以在 `<canvas>` 元素内部渲染，最重要的是，它们可以像网页上的任何其他元素一样在该 `<canvas>` 区域中进行操作。

截至目前，HTML-in-Canvas 是一项提议标准，Firefox 和 Safari 尚未采用。

“它改变了 Web 的感觉，”Paul Kinlan 解释道。“它将赋予我们改变单个元素并以从未有过的方式为其设计样式的能力，甚至能带来结合了 Web 和 HTML 的新型 3D 图形或 3D 体验。”

这是一种你需要在演示中亲眼目睹的功能（见下文）。它也可能会驱动许多关于 Web 新 UI 形式的疯狂实验——伴随着随之而来的惯常过度设计。但一年后再来看，许多 Web 应用可能会看起来更像现代移动端体验，而不是 2005 年的 Web 2.0 应用。

![](https://cdn.thenewstack.io/media/2026/05/8ca929bb-5_-html_in_canvas_3d_in-car_demo.gif)

HTML-in-Canvas 演示。来源：Google。