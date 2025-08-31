<!--
title: Flutter 3.5：开发者体验再升级
cover: https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2.png
summary: Flutter 3.35发布，重点提升开发者效率，包括Web端有状态热重载、Dart和Flutter MCP Server以及Widget Previews。Google修改Android应用安装规则，2026年3月起需验证开发者。DigitalOcean推出MCP Server，通过AI工具用自然语言提示管理云资源。
-->

Flutter 3.35发布，重点提升开发者效率，包括Web端有状态热重载、Dart和Flutter MCP Server以及Widget Previews。Google修改Android应用安装规则，2026年3月起需验证开发者。DigitalOcean推出MCP Server，通过AI工具用自然语言提示管理云资源。

> 译自：[Flutter 3.5 Offers New Developer Experience Features](https://thenewstack.io/flutter-3-5-offers-new-developer-experience-features/)
> 
> 作者：Loraine Lawson

Flutter 3.35于8月16日发布，更新包括Web端有状态热重载的稳定版本和[Dart and Flutter MCP Server](https://dart.dev/tools/mcp-server)。它还包括Widget Previews的实验性版本。

根据Google Dart和Flutter的技术项目经理[Kevin Chisholm](https://www.linkedin.com/in/kevin-chisholm/)在[Flutter 博客文章](https://medium.com/flutter/whats-new-in-flutter-3-35-c58ef72e3766)中的说法，开发者效率是此版本的一个关键方面。

Chisholm写道，Web端有状态热重载现在默认启用。该功能意味着开发者可以编辑其Web应用程序的代码，并在浏览器中即时看到更改，而不会丢失应用程序的当前状态。

热重载是一个过程，使开发服务器能够在保存文件后自动将新代码注入到正在运行的应用程序中，从而避免了完整的页面刷新。“有状态”部分意味着应用程序的当前状态（例如表单中的数据、用户在游戏中的位置或已翻转的切换）在热重载期间得以保留。

“我们的目标是在所有平台上提供无缝且一致的热重载体验，”Chisholm写道。“虽然您仍然可以使用标志禁用此功能，但我们计划在未来的版本中删除该功能。”

此外，Dart和Flutter [MCP Server](https://thenewstack.io/remote-mcp-servers-inevitable-not-easy/)现在可以在Dart SDK的稳定通道中使用。

“Dart和Flutter MCP Server充当桥梁，使[AI 编码助手](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/)可以通过Dart和Flutter工具链访问您的项目的更多上下文，”Chisholm写道。“您的AI助手不仅可以建议代码，还可以深入了解您的项目并代表您采取行动。这使您可以专注于您的目标，而AI处理这些机制。”

该版本还包括Widget Previews，这是一项新的实验性功能，使开发人员可以直接在其IDE中查看和迭代单个widget，而无需运行整个应用程序。

Chisholm说，它补充了有状态的热重载。

“Widget Previews通过允许您在沙盒环境中可视化和测试您的widget来补充这一点，该环境完全独立于完整的应用程序，”他写道。“在构建设计系统或跨各种不同配置（例如各种屏幕尺寸、主题和文本比例）同时并排测试组件时，这非常宝贵。”

它通过允许开发人员专注于特定的UI组件来微调widget的设计和行为，但无需构建和运行完整的应用程序，从而加快了开发过程。

此版本中同样值得注意的是[WebAssembly](https://thenewstack.io/what-debugging-javascript-on-webassembly-looks-like/) dry runs。

“为了预见到启用WebAssembly (Wasm) 作为默认的Web构建目标，现在每个JS构建都对Wasm执行“dry run”编译，”Chisholm写道。“一系列检查确定您的应用程序的Wasm准备情况，并且任何发现都会作为警告输出到控制台。”

## Google 更改了 Android 应用程序安装

Google更改了[Android](https://thenewstack.io/code-anywhere-turn-your-android-tablet-into-a-dev-machine/)应用程序安装过程：从2026年3月开始，经过认证的设备上的应用程序安装将需要经过验证的开发者。

根据[Techgig 的一份报告](https://content.techgig.com/technology-guide/google-android-app-installation-rules-developer-verification-2026/articleshow/123522363.cms)，这意味着无论开发者如何分发他们的应用程序，甚至通过第三方应用程序来源，都需要注册并证明他们的身份。

[![绿色 Android 机器人头](https://cdn.thenewstack.io/media/2025/08/b76c67db-android-head_flat.png)](https://cdn.thenewstack.io/media/2025/08/b76c67db-android-head_flat.png)

*图片来自 Google*

Google表示，这项新要求提供了一个额外的安全层。

“继最近的攻击（包括针对人们手机上的金融数据的攻击）之后，我们一直在努力提高开发者的责任感，以防止滥用，”Android产品、信任和增长副总裁Suzanne Frey在[Android 博客](https://android-developers.googleblog.com/2025/08/elevating-android-security.html)上写道。“我们已经看到恶意行为者如何隐藏在匿名背后，通过冒充开发者并使用他们的品牌形象来创建令人信服的虚假应用程序来伤害用户。”

她补充说，这是一个严重的问题。Google最近的分析发现，来自互联网侧载来源的恶意软件比通过Google Play提供的应用程序多50倍以上，她指出。

一个[新的开发者控制台](https://support.google.com/android-developer-console/answer/16450960)将支持这项工作。Android还发布了[关于Android开发者验证的指南](https://developer.android.com/developer-verification/guides)。公开试点测试将于10月开始。

## DigitalOcean 推出 MCP Server

云基础设施开发商[DigitalOcean现在提供一个MCP](https://www.digitalocean.com/blog/mcp-server-public-release)（模型上下文协议）服务器，该服务器允许开发者通过支持AI的工具使用自然语言提示来管理云资源。

[MCP是一个开源协议](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/)，它将AI系统连接到外部工具、系统和数据源。[开发者可以使用Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)、Cursor、VS Code、Windsurf和任何其他与MCP兼容的客户端来访问服务器。

该服务器目前可以访问九项服务：Accounts、App Platform、Databases、DOKS、Droplets、Insights、Marketplace、Networking和Spaces Storage。

“您无需使用多个仪表板或工具，而是可以在您最喜欢的与MCP兼容的工具中管理常见的云操作，”该团队写道。

它还允许开发者“将纯英语转化为真正的[API](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/) 操作”。这意味着开发者可以：

* **部署和管理应用程序：** 运行命令，例如从[GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/)存储库部署[Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/)应用程序，或者检查开发者帐户上有哪些应用程序。
* **创建和管理数据库：** 预置一个新的PostgreSQL数据库或创建一个新的数据库。
* **处理文件：** 将文件从本地目录上传到Spaces存储桶，创建临时访问密钥，并获取文件的公共URL。
* **检查证书和监控。**
* **检查SSL证书的状态。**
* **优化和了解成本：** 获取云成本的可视性，深入了解每月应用程序支出，或查看过去12个月的账单历史记录，以了解特定月份账单较高的原因。