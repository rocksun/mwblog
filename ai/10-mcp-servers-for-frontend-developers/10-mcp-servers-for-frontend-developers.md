<!--
title: 前端开发者的十大 MCP 服务器
cover: https://cdn.thenewstack.io/media/2025/09/d0dccb4d-mcp_servers_for_frontend.jpg
summary: 本文介绍了十个 MCP 服务器以及一个实验性的 Angular MCP 服务器，它们可以支持和简化前端开发工作。这些服务器涵盖了 Canva、Dart、DigitalOcean、Figma、GitHub、JetBrains、MongoDB、React、Shopify 和 Vercel 等平台， 提供了代码生成、UI 调整、数据库交互、云基础设施管理等功能。
-->

本文介绍了十个 MCP 服务器以及一个实验性的 Angular MCP 服务器，它们可以支持和简化前端开发工作。这些服务器涵盖了 Canva、Dart、DigitalOcean、Figma、GitHub、JetBrains、MongoDB、React、Shopify 和 Vercel 等平台， 提供了代码生成、UI 调整、数据库交互、云基础设施管理等功能。

> 译自：[10 MCP Servers for Frontend Developers](https://thenewstack.io/10-mcp-servers-for-frontend-developers/)
> 
> 作者：Loraine Lawson

如今，你几乎无法转身而不了解到某家公司创建了一个新的 MCP 服务器。

MCP 是 Anthropic 提出的一个新兴开放标准，它提供了一种 AI 模型与外部数据源和工具交互的方式。它就像一种通用语言和一组规则，允许[大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)与自身之外的系统进行通信。

[MCP 服务器](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/)的快速推出可能会让人难以跟上，但这些服务器对开发者来说是有益的，因为 MCP 可以与集成开发环境 (IDE) 中的 AI 一起使用，以提供文档和支持。

几乎每天都有新的 MCP 服务器发布，你如何判断哪些对你最有帮助？通过大量的研究和 Gemini 的一点帮助，我们确定了十个 MCP 服务器（外加一个实验性的 MCP），它们可以支持和简化前端开发工作。

### 1. Canva MCP 服务器

**它的用途：** 在 [Canva MCP 服务器](https://www.canva.dev/docs/apps/mcp-server/) 出现之前，构建 Canva 应用程序是一个漫长的过程。开发者必须与 Canva 来回沟通，Canva 会审查应用程序以确保它们符合 Canva 的外观和风格。[Canva 意识到它可以将使用其开发工具的工作转移](https://thenewstack.io/why-canva-chose-mcp-server-over-ai-agent-for-app-developers/)到 Canva 之外，并让开发者在 IDE 中访问这些工具。MCP 服务器：

* **通过单个提示生成 Canva 应用程序**。通过调用 Canva CLI 应用程序生成器，MCP 服务器可以创建一个完全结构化的应用程序，该应用程序遵循已建立的最佳实践。然后，一旦创建了你的应用程序，它就可以帮助你使用 Apps SDK 中的各种方法添加新功能；
* **调整应用程序 UI Kit**，允许开发者将现有的 UI 迁移到应用程序 UI Kit 组件，从而确保应用程序在功能和美观上的一致性；
* **更容易地符合** Canva 的设计指南；
* **生成一份报告，其中包含基于 Canva 设计指南的必须/应该/可以的建议**。它甚至为代码提供改进建议。
* **与 Claude 等 AI 聊天助手集成**，开发者可以在其中讨论 Canva Apps SDK 或 Connect API。
* **通过 Connect API 构建与 Canva 的集成**，通过生成 Canva Connect API 客户端代码来创建新设计或上传资源。

### 2. Dart MCP 服务器

**它的用途：** [Dart 的 MCP 服务器](https://www.postman.com/getmcp/public-mcp-servers/collection/6823c17166acdcf3d75b5048) 允许 AI 代理与 Dart 平台交互。这个 MCP 服务器允许 AI 助手以编程方式访问和管理 Dart 工作区中的数据；例如客户信息、项目、任务、时间跟踪和账单。主要功能包括：

* **工作区交互**，允许 [AI 代理](https://thenewstack.io/4-reasons-agentic-ai-is-failing/)连接到特定 Dart 工作区并在其中执行操作；
* **客户和项目管理**，可以查询并可能管理客户详细信息、项目和相关任务；
* **任务和时间跟踪访问**，允许开发者访问 Dart 中记录的任务信息、状态和时间条目；
* **账单和财务数据**，能够检索与 Dart 中管理的 invoices、retainers 和其他财务方面相关的信息；
* **协作和沟通**，包括支持与项目和任务相关的更新；以及
* **自定义字段和数据**，因此开发人员可以访问存储在 Dart 工作区中配置的自定义字段中的数据。

### 3. DigitalOcean MCP 服务器

**它的用途：** [DigitalOcean MCP 服务器](https://www.digitalocean.com/community/tutorials/control-apps-using-mcp-server) 允许 AI 与云基础设施交互，为前端开发者提供一个简单、自然的语言界面来访问他们的后端。MCP 服务器：

* **允许开发者从头开始构建一个应用程序**并将其部署到 [DigitalOcean](https://thenewstack.io/tutorial-a-gitops-deployment-with-flux-on-digitalocean-kubernetes/)，而无需离开 IDE；
* **直接从 GitHub 存储库部署一个新的**应用程序；
* **更改代码并使用单个提示重新部署它**；
* **创建所有应用程序的列表**，检查它们、重新启动它们或从编辑器中删除它们。
* **强制重建或删除应用程序**；
* **检查哪些区域可用**并相应地计划部署。

### 4. Figma 的开发模式 MCP 服务器

**它的用途：** [开发模式 MCP 服务器](https://www.postman.com/getmcp/public-mcp-servers/collection/6866ec3e48ab75becd41a29a) 向从 [Figma 设计文件](https://thenewstack.io/new-figma-plug-in-converts-design-to-angular-react-native/)生成代码的 AI 代理提供设计信息和上下文。本地服务器允许 AI 助手以编程方式获取有关当前 Figma 文件、项目和选定设计元素（节点）的详细信息，并将 AI 功能集成到设计到开发的流程中。它支持：

* **从选定的框架或节点生成代码**。Figma 用户可以选择 Figma 中的一个框架或提供一个节点 URL，以便让 AI 代理将设计转换为代码。
* **从图层中提取设计上下文**，通过从设计中提取变量、组件和布局，以确保构建符合设计模式。
* **代码连接**。MCP 服务器会告知 AI 代理有关从代码连接信息派生的现有组件，从而支持重用。

### 5. GitHub MCP 服务器

**它的用途：** [GitHub MCP 服务器](https://github.com/github/github-mcp-server) 是为开发者构建的，允许 AI 代理直接与代码库、拉取请求和问题交互。GitHub MCP 服务器将 AI 工具直接连接到 GitHub 的平台，使 AI 代理、助手和聊天机器人能够读取存储库和代码文件、管理问题和 PR、分析代码并自动化工作流程。所有这些都通过自然语言交互实现。MCP 服务器提供：

* **存储库管理：** 开发者可以浏览和查询代码、搜索文件、分析提交并了解他们有权访问的任何存储库中的项目结构；
* **问题和拉取请求自动化：** 创建、更新和管理问题和拉取请求。AI 可以帮助分类错误、审查代码更改并维护项目看板。
* **为 CI/CD 和工作流程添加** 智能。它可以 [监控 GitHub Actions 工作流程](https://thenewstack.io/the-missing-part-of-github-actions-workflows-monitoring/) 运行、分析构建失败、管理发布并深入了解开发管道；
* **分析代码**、检查安全发现、审查 Dependabot 警报、了解代码模式并全面了解你的代码库。
* **团队协作**，通过提供对讨论的访问、管理通知、分析团队活动并简化团队流程。

### 6. JetBrains MCP 代理服务器

**它的用途：** JetBrains 提供 IDE，包括用于 Java 和 Kotlin 的 IntelliJ IDEA；用于 Python 的 PyCharm，用于 JavaScript 的 WebStorm，用于 .NET 的 Rider 和用于 C/C++ 的 CLion。它为其 [MCP 代理服务器提供了一个插件](https://www.postman.com/getmcp/public-mcp-servers/collection/681e63aecb58000ecfc0317f)，该插件允许 AI 工具利用 IDE 的代码理解能力、执行重构、生成代码并直接在运行 AI 助手的开发环境中访问项目上下文。它支持：

* **IDE 集成**，为外部 AI 代理提供了一个桥梁，以便与在 JetBrains IDE 中运行的 AI 助手插件进行通信；
* **代码理解和分析**，允许 AI 代理访问 IDE 对代码库的理解，包括语法、语义和项目结构；
* **代码生成和修改**，这有助于 AI 驱动的代码生成、自动完成、重构和其他代码操作任务，这些任务由 IDE 执行。
* **项目上下文访问**，使 AI 代理能够获取有关当前项目、打开的文件和光标位置的信息，以提供上下文相关的帮助；以及
* **本地执行**，这意味着代理在本地运行，从而有助于本地 AI 代理或开发工具与本地 JetBrains IDE 实例之间的通信。

### 7. MongoDB MCP 服务器

**它的用途：** [MongoDB MCP 服务器](https://www.mongodb.com/company/blog/announcing-mongodb-mcp-server) 允许 AI 与其数据库交互。前端开发者可以使用 AI 代理来：

* **查询数据库** 以获取特定的信息。
* **管理数据**，通过使用自然语言将新用户添加到数据库。
* **管理集合**，通过为数据库创建新集合。
* **获取数据库的 schema**；以及
* **创建上下文感知代码生成**，这意味着开发者可以描述所需的数据，并让 AI 生成 MongoDB 查询，甚至生成与之交互的代码。

### 8. React MCP 服务器（第三方）

Meta 尚未宣布发布 React 的 MCP 服务器的任何计划，但 Drishya AI Labs 的前端开发者 Kalivaraprasad Gonapa 创建了一个。根据 GitHub 存储库，[React MCP 服务器](https://github.com/kalivaraprasad-gonapa/react-mcp) 与 Claude Desktop 集成，从而能够根据用户提示创建和修改 React 应用程序。它支持：

* **创建新的 React 应用程序**；
* **运行 React 开发服务器**；
* **管理文件和目录**；
* **安装 npm 包**；
* **执行终端命令**；以及
* **跟踪和管理长时间运行的进程。**

### 9. Shopify Dev MCP 服务器

**它的用途：** 这个 [MCP 服务器](https://shopify.dev/docs/apps/build/devmcp) 将开发者的 AI 助手连接到 [Shopify](https://thenewstack.io/how-mcp-ui-powers-shopifys-new-commerce-widgets-in-agents/) 的开发资源，使 AI 助手能够搜索 Shopify 文档、探索 API schema、构建函数并获取有关 Shopify API 和最佳实践的最新答案。MCP 服务器支持：

* **查询你的 AI 助手** 以了解如何使用 Shopify 进行开发；
* **支持 Shopify 的 API**，其中包括 Admin GraphQL API、函数、Polaris Web 组件（可选）和 Liquid（可选）；以及
* **与 AI 开发工具集成**，例如 Cursor 和 Claude Desktop。

### 10. Vercel MCP 服务器

**它的用途：** [Vercel MCP 服务器](https://vercel.com/docs/mcp/vercel-mcp) 允许 AI 与前端开发和托管平台交互。它与 Gemini CLI、[Gemini Code Assist](https://thenewstack.io/google-vaunts-new-gemini-code-assist-tool-at-cloud-next-2024/)、Windsurf、Goose、Raycast、Devin、带有 Copilot 的 VS Code、Cursor、Claude 和 Claude Code 以及 ChatGPT 一起使用。它支持：

* **部署应用程序的新版本**；
* **获取有关应用程序的反馈**，包括新功能；
* **管理应用程序设置**，通过检查应用程序的环境变量；以及
* **处理新应用程序的配置**。

## 即将推出

### **Angular MCP 服务器** （实验性）

**它的用途：** [Angular 有一个 CLI MCP 服务器](https://angular.dev/ai/mcp) 处于实验阶段，它将提供工具来帮助开发者完成他们的工作流程。它支持：

* **最佳实践支持**，通过允许开发者访问 Angular 最佳实践指南，以确保所有代码都符合现代标准。
* **列出 Angular 工作区中定义的所有应用程序和库**，通过读取 angular.json 配置文件；以及
* **搜索 Angular 的官方文档**。