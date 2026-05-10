<!--
title: OpenAI Codex 推出 Chrome 扩展程序，AI 代理实现浏览器原生操作
cover: https://cdn.thenewstack.io/media/2026/05/37c804dd-taufik-ramadhan-asfztr-k5bq-unsplash-scaled.jpg
summary: OpenAI 为 Codex 推出 Chrome 扩展程序，使 AI 代理能直接在浏览器会话中操作。该工具支持跨标签页处理已登录工作流，避开了传统的截图推理模式，大幅提升了操作效率。
-->

OpenAI 为 Codex 推出 Chrome 扩展程序，使 AI 代理能直接在浏览器会话中操作。该工具支持跨标签页处理已登录工作流，避开了传统的截图推理模式，大幅提升了操作效率。

> 译自：[OpenAI Codex arrives in the browser with new Chrome extension](https://thenewstack.io/openai-codex-chrome-extension/)
> 
> 作者：Paul Sawers

AI 公司一直致力于创建能像人类一样使用计算机的编码代理：点击按钮、滚动页面以及在桌面上移动光标。这一前景显而易见，但执行过程仍然显得笨拙。

其目标是使代理能够像人一样操作软件，特别是在缺乏清晰 API 或集成的 Web 应用和企业工具中。

然而，这些系统仍可能让人感到繁琐，通常会垄断浏览器会话，并且一次只能处理一个屏幕的任务。这就是 OpenAI 现在试图通过全新的 [Codex Chrome 扩展程序](https://developers.openai.com/codex/app/chrome-extension) 来解决的问题。

在[周四](https://x.com/openaidevs/status/2052481136971125158?s=46)推出的这款 Codex Chrome 扩展程序允许代理直接在用户的实时浏览器会话中运行，让它们能够访问已登录的网站、多个标签页和经过身份验证的工作流，而无需完全接管桌面。

该扩展程序将 Chrome 连接到 Windows 和 macOS 上的 Codex 应用，允许代理使用用户现有的浏览器状态、Cookie 和登录会话，与 Gmail、Salesforce、LinkedIn 以及内部 Web 应用等工具进行交互。

## 超越“截图并点击”的代理

此次发布基于 OpenAI 在 4 月份为 Codex 引入的“计算机使用”功能。该功能允许代理在后台运行桌面应用和浏览器，而用户可以继续在机器的其他地方工作。

然而，OpenAI 现在正在通用的计算机使用系统与更专注于浏览器的方法之间划定更清晰的界限。

> “OpenAI 正在通用的计算机使用系统与更专注于浏览器的方法之间划定更清晰的界限。”

此前，Codex 在与浏览器工作流交互时，很大程度上依赖于结构化插件或更广泛的计算机使用工具。插件仍然是首选路线，因为它们允许 Codex 直接与 Slack、Gmail 和 GitHub 等服务协作，而无需手动导航其界面。

![Codex 中的插件](https://cdn.thenewstack.io/media/2026/05/e39a5a81-gif1.gif)

*Codex 中的插件*

但许多工作流仍然存在于完整的 Web 应用程序、内部仪表板或经过身份验证的浏览器会话中，代理仅通过集成很难轻松访问这些内容。

在随发布附带的演示视频中，OpenAI 开发者体验负责人 Dominik Kundel 表示，新扩展程序避免了许多计算机使用系统中常见的传统“截图、推理、移动鼠标”循环，即代理在决定下一步点击哪里之前，需要反复分析屏幕上的可见内容。

虽然 Codex 已经可以通过 OpenAI 现有的计算机使用功能操作 Chrome，但它实际上将浏览器视为任何其他桌面应用程序，一次一步地进行视觉交互。而新的扩展程序则将 Codex 直接连接到 Chrome 本身，使其能够跨多个标签页、登录会话并行处理浏览器任务。

这种差异至关重要，因为越来越多的现代软件工作发生在基于浏览器的 SaaS 工具、内部仪表板和经过身份验证的企业应用中，而这些应用通常缺乏清晰的 API 或结构化集成。

“有时没有插件，或者虽然有插件，但你需要的东西仅在完整的 Web 应用中可用，”Dominik Kundel 说。“有时上下文其实就是现有的已登录 Chrome 会话。这就是 Chrome 扩展程序的用途。”

> “有时上下文其实就是现有的已登录 Chrome 会话。这就是 Chrome 扩展程序的用途。”

## Chrome 与 Codex 的结合

Chrome 扩展程序是通过 Codex 应用本身安装的。用户首先打开 Codex，导航到插件（Plugins）部分，然后添加 Chrome 插件，随后它将引导用户连接 Chrome 并批准所需的浏览器权限。

![在 Codex 中安装 Chrome 扩展程序](https://cdn.thenewstack.io/media/2026/05/233e6cca-gif2installingextension.gif)

*在 Codex 中安装 Chrome 扩展程序*

安装完成后，Codex 可以直接通过如下提示词调用 Chrome：“*@Chrome 打开 Salesforce 并根据这些通话记录更新账户*，”或者“*总结社区论坛评论中的反馈和情绪*。”

虽然 OpenAI 表示 Codex 现有的应用内浏览器仍然更适合本地主机测试和前端开发任务，但 Chrome 扩展程序是专为依赖于用户实时浏览器上下文和 Chrome 完整功能的工作流而设计的。在演示中，Dominik Kundel 展示了 Codex 如何同时在多个标签页中研究围绕产品发布的情绪，在将结果汇总到电子表格之前，识别重复的反馈和痛点。

![我们应该处理什么？](https://cdn.thenewstack.io/media/2026/05/bcbdf23d-gif3.gif)

*我们应该处理什么？*

该扩展程序旨在介于 Codex 的结构化插件及其更广泛的计算机使用工具之间。OpenAI 表示，Codex 可以根据工作流在集成、Chrome 及其自身应用内浏览器之间动态切换，在可能的情况下使用直接插件，当任务需要身份验证会话或完整 Web 界面时，则退而使用浏览器交互。

该扩展程序的关键点之一是它不会强占用户的活动浏览会话；相反，它将 Codex 的活动分组成独立的 Chrome 标签页。这允许代理在后台继续研究、导航和编译信息，而用户可以继续在浏览器的其他位置工作。

![隔离的 Chrome 标签页](https://cdn.thenewstack.io/media/2026/05/a5d75342-gif4.gif)

*隔离的 Chrome 标签页*

这种更深层次的浏览器集成也比典型的聊天机器人交互需要更多权限。

根据 [OpenAI 的文档](https://developers.openai.com/codex/app/chrome-extension)，该扩展程序可能会请求访问浏览历史记录、标签页组、下载内容、书签、网站数据、调试器功能以及与原生应用程序的通信。

该公司表示，除非用户明确禁用这些提示，否则 Codex 在与新网站交互前会请求确认。它还指出，浏览器任务可能会暴露敏感上下文，因为页面内容、经过身份验证的会话和浏览活动可能会成为 Codex 完成任务时使用的信息的一部分。

## 全域访问

此次发布正值整个 AI 行业推动浏览器原生代理之际——而且，浏览器会话本身正日益成为关键战场。

Anthropic 也一直在朝着同一方向迈进。其 [Claude Chrome 扩展程序](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)自 8 月份以来一直处于[测试阶段](https://claude.com/blog/claude-for-chrome)，它[赋予了 Claude Code 同样的能力](https://code.claude.com/docs/en/chrome)，使其能在用户现有的浏览器会话中运行——访问经过身份验证的应用、跨标签页工作，并处理缺乏清晰 API 集成的工作流。该公司今年早些时候还在 macOS 上[扩展了 Claude Code 和 Claude Cowork](https://thenewstack.io/claude-computer-use/)，使其具备更广泛的计算机使用能力。与此同时，法国 AI 初创公司 HCompany 最近[推出了 HoloTab](https://thenewstack.io/hugging-face-holotab/)，这是一款无需特定网站集成即可在 Chrome 中导航网站的浏览器代理。

因此，一个清晰的模式正在显现：代理正在向工作实际发生的地方靠拢。不是从外部操作系统，而是在应用程序内部、在会话中、在现代工作已经存在的上下文中运行。