<!--
title: OpenAI的ChatGPT/Codex桌面应用现已登陆Linux
cover: https://cdn.thenewstack.io/media/2026/08/9e7a394a-screenshot-2026-08-11-at-10.42.00-am-1024x695.png
summary: OpenAI正式推出Linux版ChatGPT桌面应用，支持主流发行版并提供.deb和.rpm包。该应用整合了ChatGPT、ChatGPT Work和Codex功能，支持语音与浏览器扩展，但首发版本暂不支持原生计算机控制功能。
-->

OpenAI正式推出Linux版ChatGPT桌面应用，支持主流发行版并提供.deb和.rpm包。该应用整合了ChatGPT、ChatGPT Work和Codex功能，支持语音与浏览器扩展，但首发版本暂不支持原生计算机控制功能。

> 译自：[OpenAI's ChatGPT/Codex desktop app is now on Linux](https://thenewstack.io/openais-chatgpt-desktop-linux/)
> 
> 作者：Frederic Lardinois

周二，OpenAI 发布了用于 Linux 的 ChatGPT 桌面版。

目前该应用处于预览阶段，集成了 ChatGPT、ChatGPT Work 和 Codex，可运行在 Ubuntu 24.04 和 26.04 LTS、Debian 13 以及 Fedora 43 和 44 上，并为 [x64](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/x64-architecture) 和 ARM64 架构提供了原生的 .deb 和 .rpm 包。

[Mac 和 Windows 版 ChatGPT 桌面应用](https://thenewstack.io/openai-codex-work-atlas/)于 7 月份随 OpenAI 推出 ChatGPT Work 时发布。

一位 OpenAI 发言人告诉 *The New Stack*：“Linux 是桌面应用最受期待的平台之一，此次发布将 ChatGPT 和 Codex 扩展到了每一个主流桌面操作系统。”

> “Linux 是桌面应用最受期待的平台之一。”——OpenAI。

与 macOS 和 Windows 上的 ChatGPT 桌面应用一样，Linux 版本也将内置 OpenAI 的应用内浏览器，并支持 Chrome 扩展。

不过，OpenAI 发言人向我们证实，有一项功能在 Linux 上将不可用，即应用内浏览器之外的计算机使用（computer use）功能。

“Linux 应用支持核心的 ChatGPT 和 Codex 体验，包括语音功能，”这位发言人告诉我们。“主要区别在于原生的计算机使用功能——即 ChatGPT 与 OpenOffice 或 GIMP 等桌面应用程序进行交互的能力——在发布时暂不可用。这也影响了相关功能，包括 Appshots、录制与重放，以及涉及桌面应用和浏览器的语音请求。其他基于浏览器的工作流，包括 Chrome 扩展，均受支持。”

该应用在发布时将面向全球提供。

## 从 Codex 到 ChatGPT 应用

自新的 ChatGPT 应用推出以来，该公司对其进行了一些改进，因为最初的版本明显感觉像是贴了 ChatGPT Work 和常规 ChatGPT 聊天标签的 Codex 应用。在当前的迭代中，在 ChatGPT 和 Codex 之间切换变得更加容易，但对于普通用户来说，这可能仍然是一种令人困惑的体验。

公平地说，Anthropic 的 Claude 应用也存在许多相同的问题，为代理系统寻找最佳用户体验显然仍是一项正在进行的工作。

事实证明，当用户想要提出问题并获得答案时，聊天界面非常有效。但当一个代理运行了一个小时，同时协调多个子任务、等待批准、编辑文件和/或生成多个工件时，它们就会变得不那么自然。在这一点上，产品需要像项目仪表板一样，而不仅仅是一个消息应用。

## 不仅仅是 Codex 的图形用户界面

值得注意的是，Linux 用户并不缺乏对 OpenAI 编码代理的访问权限。

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) 已经在 Linux 上运行，该公司的 IDE 扩展也是如此，而 Codex 云端则提供了另一种无需安装桌面客户端即可委托编码工作的方式。

桌面应用所增加的是一个用于协调这些工作的可视化工作空间。用户可以将多个项目和长时间运行的任务保持在视野范围内，检查文件和生成的工件，审查代码更改，并在本地工作和云端工作之间切换。该应用还将 OpenAI 的浏览器、插件和更广泛的 ChatGPT 功能引入到同一个界面中。

对于那些生活在终端里的开发人员来说，新应用不一定会取代 CLI。对于检查存储库、运行命令、编写可重复任务脚本以及将 Codex 集成到 CI 中，CLI 仍然是更直接的选择。

桌面应用旨在作为围绕这些任务的协调层，特别是当涉及多个代理、存储库或不同种类的工作时。

不过，它还包括对用于知识工作的 ChatGPT Work 和 ChatGPT 聊天的支持，这是一个不错的额外福利。