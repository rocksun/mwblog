
<!--
title: 谷歌AI创业“路线图”：坦途还是荒野？
cover: https://cdn.thenewstack.io/media/2025/11/6c1a87bd-getty-images-e3gjtedeeoi-unsplashb.jpg
summary: Google 在 Web AI 峰会上强调浏览器端 AI 的发展，推出 WebMCP、WebGPU 等技术，旨在普及 AI。Parisa Tabriz 将此视为“Web 的文艺复兴”。Google 致力于开放 Web，并预测浏览器将成为生产力平台。Kenji Baheux 介绍了两种开发模式：便捷的“铺好的道路”和灵活的“开放领域”。
-->

Google 在 Web AI 峰会上强调浏览器端 AI 的发展，推出 WebMCP、WebGPU 等技术，旨在普及 AI。Parisa Tabriz 将此视为“Web 的文艺复兴”。Google 致力于开放 Web，并预测浏览器将成为生产力平台。Kenji Baheux 介绍了两种开发模式：便捷的“铺好的道路”和灵活的“开放领域”。

> 译自：[Google’s Web AI Playbook: The Paved Road vs. the Open Field](https://thenewstack.io/googles-web-ai-playbook-the-paved-road-vs-the-open-field/)
> 
> 作者：Richard MacManus

在本月于 [Google](https://cloud.google.com/?utm_content=inline+mention) 举办的 [Web AI 峰会](https://rsvp.withgoogle.com/events/web-ai-summit-2025) 上，主要焦点是 [浏览器中的客户端 AI](https://thenewstack.io/how-google-is-shifting-ai-from-the-cloud-to-your-browser/) — 但我们也听到了很多关于模型上下文协议（MCP）及其 Web 变体 [WebMCP](https://thenewstack.io/how-webmcp-lets-developers-control-ai-agents-with-javascript/)、代理（agents）以及像 WebGPU 和 WebNN 这样的“计算抽象”如何使 Web 开发人员能够访问设备硬件。

在 Google Web AI 负责人 [Jason Mayes](https://www.linkedin.com/in/webai/) 致开场白后，本次活动以 Google Chrome 和 Web 生态系统副总裁兼总经理 [Parisa Tabriz](https://www.linkedin.com/in/parisatabriz/) 的主题演讲拉开帷幕。Tabriz 将当前这个时刻描述为“Web 的文艺复兴”，并补充说“许多开发工具和技术正在发生根本性变化，无论你称之为氛围编程还是 AI 辅助。”

鉴于目前 Web 开发人员和在线创作者面临的就业压力，我不确定“文艺复兴”是否是这里的正确词语。但我理解 Tabriz 的观点，即由于 AI 技术，Web 的构建和使用方式正在发生根本性变化。

[![Parisa Tabriz 在 Web AI 峰会上](https://cdn.thenewstack.io/media/2025/11/2a2de3c0-webai-tabriz2.jpg)](https://cdn.thenewstack.io/media/2025/11/2a2de3c0-webai-tabriz2.jpg)

*Parisa Tabriz，Chrome 副总裁/总经理，在 Web AI 峰会上。*

Web 行业中的许多人曾 [质疑 Google 在 AI 时代对开放 Web 的承诺](https://thenewstack.io/is-ai-the-ultimate-version-of-google-as-larry-page-wanted/)。但据 Tabriz 称，Google 仍致力于投资开放 Web。

“在 Chrome Web 生态系统组织中，需要了解并记住的一点是，我们非常致力于继续投资于开放、可互操作的 Web，”她说。

> Google “非常致力于继续投资于开放、可互操作的 Web。”
> 
> **— Parisa Tabriz，Google Chrome 副总裁/总经理**

她引用了 WebAssembly — “这一切都是为了将桌面级功能带入浏览器” — 和 WebGPU 作为她团队近期一直在改进的技术示例。

她还提到了去年 8 月添加到 Chrome 的内置 AI API，以及 Gemini Nano — Google 的主要设备端模型 — 于去年 6 月作为 Chrome 的内置功能发布。所有这些功能都概述在 Google 的“[AI with Chrome](https://developer.chrome.com/docs/ai)”网页上。

## 通过浏览器实现 AI 开发的民主化

Tabriz 将 Web AI 运动视为一种 AI 的民主化。

“它 [Web AI] 实际上是关于我们如何实现 AI 的民主化，以确保新的功能更易于访问和高效，目标是让 AI 在任何设备、任何浏览器、任何地方都可用。”

有趣的是，这种语言与 Google 首席执行官 [Sundar Pichai](https://www.linkedin.com/in/sundarpichai/) 于 2017 年 5 月发表的题为“让 AI 为每个人服务”的博客文章 [相呼应](https://blog.google/technology/ai/making-ai-work-for-everyone/)。正如 Pichai 当时所写，“我们越能努力实现 AI 技术的民主化 — 无论是在人们可以使用的工具方面，还是在我们应用它的方式方面 — 每个人就越早受益。”请注意，这比现在著名的由多名 Google 员工撰写的“[Attention Is All You Need](https://arxiv.org/abs/1706.03762)”学术论文发表早了一个月，这篇论文启发了 OpenAI 开始构建成为 ChatGPT 的东西。

我的观点是，虽然我们有时可能在 Google 的 AI 技术执行方面有所诟病（只需谷歌搜索“AI Overviews glue pizza”），但你无法诟病该公司对 AI 的一贯愿景 — 直到 Tabriz 说 Web AI 旨在让 AI 在任何设备和任何浏览器上可用。

## AI 时代浏览器的未来

Tabriz 接着谈了谈 AI 时代浏览器的未来。她说，浏览器正从“渲染像素的 Web 窗口”转变为“生产力的...合作伙伴平台”。她指出，“浏览器已成为 Chrome 企业客户的‘新终端’，因为现在有这么多人每天都在浏览器中工作（‘至少在桌面端’，她补充道）。”

> 浏览器正从“渲染像素的 Web 窗口”转变为“生产力的...合作伙伴平台”。
> 
> **— Parisa Tabriz，Google Chrome 副总裁/总经理**

对于开发人员而言，Tabriz 认为“对设备端 AI 和混合解决方案存在‘浓厚兴趣’”。

她最后对 Web 的未来做出了三个预测：

1.  **更具主动性：** “它将不仅仅是对用户查询做出反应，它将理解用户意图。”当然，这也是 [AI 代理](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/) 发挥作用的地方。
2.  **更个性化、动态的体验：** 特别是，Tabriz 谈到了“[AI] 生成的动态用户界面，并且能够真正适应最适合个人的内容”，这暗示了按需网站，或者至少是为每个用户定制的 Web UI 层。
3.  **人机协作的新形式：** 在这里，她提到了“[Gemini 最近集成到 Chrome 中](https://thenewstack.io/chrome-switches-on-ai-the-future-of-browsing-begins-now/)”，并将其用作“浏览助手”。

[![Parisa Tabriz 在 Web AI 峰会上](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)](https://cdn.thenewstack.io/media/2025/11/e857e98d-webai-tabriz1.png)

Parisa Tabriz 在 Web AI 峰会上。

## Web AI 开发人员指南

在 Web AI 峰会晚些时候，我们听到了更多关于开发人员如何着手构建基于浏览器的 AI 应用程序的信息。[Kenji Baheux](https://www.linkedin.com/in/baheux/)，一位负责 Web AI 计划的 Chrome 产品经理，做了一次[非常有用的演示](https://docs.google.com/presentation/d/1wTRhaujJnJDxhhuG7KNhHfBl_2wQ0yqIX1V7xs4OesI/edit)，概述了他对 Web AI 指南的看法 — 换句话说，就是一份开发人员的指南。

Baheux 谈到了 Web AI 开发的两种主要方法。第一种，“铺好的道路”，是关于使用现有框架（包括可能由 Google 本周发布的“代理开发平台”[Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)）和 Chrome 的内置 AI API。通过这种方法，开发人员无需担心 GPU — 或 WebGPU。

“这显然是简单快捷的道路，它是为那些希望交付有价值的 AI 功能而无需担心 AI 基础设施或技术栈的构建者设计的，”Baheux 告诉 Web AI 峰会听众。

[![Web AI 铺好的道路](https://cdn.thenewstack.io/media/2025/11/47b78531-webai-paved-road.png)](https://cdn.thenewstack.io/media/2025/11/47b78531-webai-paved-road.png)

*Web AI 铺好的道路。（来源：Kenji Baheux）*

然后，他提出了另一种方法，这实际上是这个隐喻中的一个*领域*。“开放领域”使开发人员能够访问设备硬件，这意味着要深入研究 Wasm、WebGPU 或 WebNN 的“低级 API”。

“这是最大灵活性和控制力的途径，”Baheux 解释说，“它本质上是为两个关键群体设计的。它适用于需要部署自己定制模型的构建者，或者一些想要完全控制整个 AI 技术栈的人。其次，这也是...那些构建框架[或]工具的人的工作室，以便他们通过提供易于使用的解决方案来扩展铺好的道路的范围。”

[![Web AI 开放领域](https://cdn.thenewstack.io/media/2025/11/64171b87-webai-open-field.png)](https://cdn.thenewstack.io/media/2025/11/64171b87-webai-open-field.png)

*Web AI 开放领域。（来源：Kenji Baheux）*

在他演讲的稍后部分，Baheux 指出，我们还需要针对 AI 驱动的 Web 应用程序设计新的模式。他说，通过客户端 AI，“你可以更主动。”他说，到目前为止，开发人员在 AI 方面犯的最大错误是给他们的网站添加了一个“AI 功能陷阱” — 例如，一个侵扰性的聊天机器人，中断了用户的流程。

“我认为更好的方法是微妙而有帮助的，”他说。“目标确实是增强用户已有的工作流程，以便 AI 能够融入背景中。”

[![Kenji Baheux 在 Web AI 峰会上](https://cdn.thenewstack.io/media/2025/11/17f97596-webai-summit-kenji.jpg)](https://cdn.thenewstack.io/media/2025/11/17f97596-webai-summit-kenji.jpg)

*Google 产品经理 Kenji Baheux 在 Web AI 峰会上。*

## 结论

Web AI 作为一种特定类型的 AI 应用程序开发，显然发挥了 Google 的优势 — 其在 Web 浏览器市场的统治地位（OpenAI 和其他 AI 公司正以[他们的新浏览器](https://webtechnology.news/a-new-web-browser-from-openai-initial-reactions-to-atlas/)觊觎），其根据自身愿景塑造新兴 Web 标准（如 WebGPU 和 Wasm）的能力，其 Web 工程能力以及其日益复杂的 AI 模型和工具（Gemini 和 Antigravity 等工具）。

反过来看，许多开发人员可能仍然更愿意依赖云计算 — 服务器端 AI — 来为其 AI 应用提供支持。但就我个人而言，我认为设备端 AI 潜力巨大，这在很大程度上是因为它完美地契合了 Web 平台本身的优势 — 可部署性、用户隐私以及（最重要的是）开放性。