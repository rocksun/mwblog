<!--
title: 微软全新 Copilot 框架让智能体开发变得轻松——直到你想切换它
cover: https://cdn.thenewstack.io/media/2026/10/1d1484de-ian-taylor-h7b1suempis-unsplash-scaled.jpg
summary: 微软通过 Foundry 推出全新的 GitHub Copilot 智能体编排框架，大幅简化了自主智能体的构建与部署。尽管它提供了内置沙箱、MCP 集成及子智能体支持等强大功能，但创建后无法更改框架的限制以及对自带模型的不支持，也引发了开发者对平台锁定和运行环境控制权的担忧。
-->

微软通过 Foundry 推出全新的 GitHub Copilot 智能体编排框架，大幅简化了自主智能体的构建与部署。尽管它提供了内置沙箱、MCP 集成及子智能体支持等强大功能，但创建后无法更改框架的限制以及对自带模型的不支持，也引发了开发者对平台锁定和运行环境控制权的担忧。

> 译自：[Microsoft’s new Copilot harness makes agents easy — until you want to switch](https://thenewstack.io/microsoft-copilot-harness-foundry/)
> 
> 作者：Amanda Caswell

**微软正在通过 Microsoft Foundry 向外部开发者开放 GitHub Copilot 智能体框架**，将贯穿其 Copilot 产品的相同编排基础设施转化为托管服务，用于构建和部署自主智能体。

[在周三宣布](https://devblogs.microsoft.com/foundry/microsoft-copilot-harness-in-foundry/)之后，Microsoft Copilot 框架现已通过 Foundry Agent Service 提供公开预览版。它内置了沙箱、可复用技能、MCP 集成以及对子智能体的支持。微软负责运行智能体并管理其执行环境，开发者只需选择受支持的 model（模型）并为其应用配置 instructions（指令）和 tools（工具）。

> 这一相同的框架现已支持 Copilot Code、Copilot Studio、GitHub Copilot、CLI 以及 VS Code。

该公司还在其更多的 Copilot 产品中使用了 GitHub 的智能体基础设施。这是 Build 2026 上概述的 [Foundry 战略](https://thenewstack.io/microsoft-foundry-build-2026-ai-agents/)的延续，该战略专注于让企业更容易运行、管理和控制 AI 智能体。这一相同的框架现已支持 Copilot Code、Copilot Studio、GitHub Copilot、CLI 以及 VS Code。

## 深入托管的 Copilot 框架

微软的框架负责管理 model（模型）和 tool（工具）调用、跟踪 context（上下文），并使智能体保持在配置的策略内。技能可以将 instructions（指令）、脚本和支持资源打包，而 MCP 集成则需要 authentication（身份验证）和 approval（批准）。智能体还可以处理文件、运行代码并将任务委派给子智能体，由主智能体协调结果。

> 微软的框架负责管理 model（模型）和 tool（工具）调用、跟踪 context（上下文），并使智能体保持在配置的策略内。

## 开发者如何部署智能体

该公司的技术演练展示了这如何与研究智能体一起工作。基于 Markdown 的技能列出了收集证据、分析数据和编写报告的步骤，而 `azure.yaml` 文件则定义了 model（模型）部署、tools（工具）、instructions（指令）和框架。

开发者选择 `microsoft_copilot_preview` 作为框架类型，使用 `azd deploy --all` 部署智能体，并通过 Azure Developer CLI 调用它。他们可以将智能体配置和支持文件保留在源码管理中，从而更容易与应用程序代码一起跟踪更改。

## 运行时限制与平台锁定

在创建 prompt（提示词）智能体时必须选择 Copilot 框架，并且一旦选定便无法更改，即使在新的版本中也是如此。微软还控制着智能体获得的 CPU 和内存量以及它可以空闲多长时间。开发者可以决定他们的智能体做什么，但对它们运行的环境控制较少。

> 开发者可以决定他们的智能体做什么，但对它们运行的环境控制较少。

微软将其更广泛的框架战略定位为多模型，尽管存在一些限制。开发者可以从通过 Foundry 部署的兼容 model（模型）中进行选择，但在托管的 Copilot 框架中[不支持自带 model（模型）](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/ai-gateway)。

希望获得更多控制权的团队可以改用 Foundry 的托管智能体。团队可以使用自己的框架构建和运行智能体，并自定义其运行方式，而微软则负责托管。该公司还在周三宣布了托管智能体长时间运行弹性功能的全面可用性，帮助它们在需要数小时甚至数天才能完成的任务中从中断中恢复。

## Foundry 智能体定价解析

Foundry Agent Service 中的 Copilot 框架在 2026 年 12 月 1 日之前免费，不过 model inference（模型推理）以及某些 tools（工具）和连接的服务仍然需要单独收费。

在此之后，微软将对计算收取每 vCPU 小时 0.0994 美元的费用，对内存收取每 GiB 小时 0.0118 美元的费用。这些费率可能会因地区和客户协议而异。