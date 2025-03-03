
<!--
title: 10款开源工具助你提升编码技能
cover: https://cdn.thenewstack.io/media/2025/02/599ac749-alexander-mils-qxp2nsc6ilm-unsplash-1-1.jpg
-->

> 译自：[10 Open Source Tools to Supercharge Your Coding Game](https://thenewstack.io/10-open-source-tools-to-supercharge-your-coding-game/)
> 
> 作者：Jack Wallen

从 VS Code 到 Tauri，这些开源开发工具简化了工作流程，自动化了重复性任务，并提高了各个技能水平开发人员的编码效率。

如果你想提高生产力，有很多应用程序可供选择。对于那些更喜欢使用开源软件的人来说，选择范围并没有减少多少。事实上，有很多开源工具都致力于提高编码效率。

当然，任何这样的列表都会包含你可能使用也可能不使用的工具。你的工作流程可能已经基本设定好了，并且知道你只需要一个额外的工具就能将你的生产力提升到一个新的水平。这个工作流程可能包括诸如编辑器、[IDE](https://thenewstack.io/best-open-source-ides/)、代码审查和分析、协作和文档、[CI/CD](https://thenewstack.io/ci-cd/)、监控、[调试](https://thenewstack.io/how-generative-ai-is-revolutionizing-debugging/)、自动化以及介于两者之间的一切。

这里的关键是提高你的生产力，并且仍然有很多工具可以为你服务。

让我们深入了解一下，看看你可以添加到工作流程中的哪些开源工具。

## Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) 是市场上最流行的 IDE 之一。VS Code 由微软开发，其源代码可以在 [GitHub](https://github.com/microsoft/vscode) 上查看。这个 IDE 免费、轻量级、灵活且可扩展。VS Code 非常适合编码、调试和测试。

但是这个 IDE 如何提高你的生产力呢？考虑一下它的特性，例如庞大的扩展库、智能代码补全、版本控制集成、代码分析和诊断以及跨平台兼容性，你就会明白这个 IDE 如何帮助改进你的工作流程。无需使用多个工具，你就可以在一个应用程序中处理许多任务。VS Code 还支持最流行的语言，例如 HTML/CSS、JavaScript、C/C++、C#、Objective-C、Python、PHP 和 Java。

## Git

[Git](https://git-scm.com/) 是一个版本控制系统，它帮助开发者管理代码库随时间的变化。使用 Git 可以极大地提高你的生产力，因为你不仅可以跟踪代码的更改，还可以与团队实时协作项目，而无需担心一个开发者会覆盖另一个开发者所做的更改。

Git 包括跟踪更改、版本管理、协作、提交、分支、合并等功能。

Git 通过一个非常易于遵循和可重复的工作流程来帮助你提高生产力，这个工作流程如下所示：

- 创建本地仓库：在你的工作目录中初始化一个 Git 仓库。你可以将这个仓库提供给局域网上的团队成员，也可以将其迁移到 GitHub。
- 进行更改并提交：在更改代码后，你可以使用 `git add` 和 `git commit` 来创建文件的新的版本。
- 推送到远程仓库：通过将更改（提交）推送到共享位置（例如 GitHub）来与团队成员共享你的更改。
- 从远程仓库拉取：然后，你可以从共享位置检索最新的代码更改，并将它们合并到你的本地副本中以进行进一步的工作。

## Docker/Podman

容器是软件开发的一个重要方面。任何对容器感兴趣的人都应该查看 [Docker](https://www.docker.com/) 或 [Podman](https://podman.io/)，因为这两个工具是开发和部署容器最有效率的方法。

但是为什么是容器呢？

容器使得跨环境一致地开发成为可能，因此你无需担心为多个平台开发。容器还具有更快的开发周期、简化的依赖项管理、更快的构建时间、更轻松的测试/调试、改进的可扩展性和降低的成本。并且由于容器是可移植的，你可以在你选择的 OS 上进行开发，并轻松地将容器迁移到另一个 OS，并确保它能够正常工作。

## Jenkins

[Jenkins](https://www.jenkins.io/) 是一个自动化服务器，它使开发人员能够以可重复且可靠的方式构建、测试和部署应用程序。Jenkins 包括自动化构建、CI/CD 支持、作业调度、监控和报告、代码审查、部署脚本等等。

但是为什么自动化平台可以帮助提高你的编码效率呢？Jenkins 为你做的最重要的事情是自动化重复性任务，这样你就可以专注于更重要的活动。Jenkins 还帮助减少错误，改进协作，并加快新版本和功能的上市时间。Jenkins 支持 Docker 和 Kubernetes，并具有 GitHub Actions、JIRA 和 Docker 容器构建等插件。

Jenkins 免费使用，你可以在 [GitHub](https://github.com/jenkinsci/jenkins) 上查看其源代码。

## GPT-Engineer

[GPT-工程师](https://github.com/AntonOsika/gpt-engineer) 是一款基于文本的工具，用于以更结构化和引导的方式与大型语言模型 (LLM) 交互。GPT-工程师允许你使用自然语言指定软件，使用 AI 编写和执行代码，以及/或者要求 AI 建议改进你的代码。

我知道你在想什么……使用 AI 编写代码基本上是作弊，我不会争论这一点。但是，你可以使用此类工具来学习特定语言或理解复杂的代码概念或代码行。你可以将 GPT-工程师与本地文件夹中的代码一起使用，在文件夹内创建一个提示文件并填写所需的指令，然后运行 `gpte DIRECTORY` 命令（其中 DIRECTORY 是包含代码的文件夹）。

GPT-工程师可免费使用，并可以使用 Python 或 Poetry 安装。

## Eclipse IDE

[Eclipse](https://eclipseide.org/) 是一款免费的开源 IDE，面向 Java 项目。Eclipse 可用于 Linux、macOS 和 Windows，包含广泛的插件生态系统，使用模块化架构，包括代码完成和检查以及高级调试功能。

Eclipse 非常灵活，你可以使用插件和自定义设置来完美满足你的需求。有适用于 Java Builder、代码完成、Git 集成的插件等等。

但是 IDE 如何帮助你提高生产力呢？借助大量的插件库和令人印象深刻的功能集，可以通过减少错误和提高代码的整体质量来简化你的工作流程（从而简化和缩短调试过程）。

## Continu

[Continu](https://www.continue.dev/) 是 GitHub Copilot 的开源替代方案，并为 VS Code 和 JetBrains IDE 提供 AI 驱动的代码完成和内联帮助。使用 Continu，你可以连接任何你想要的 LLM，然后将其与 Chat 一起使用，从而简化向 AI 寻求帮助的过程，而无需离开你的 IDE。

Continu 的自动完成功能在你键入时提供内联代码建议（类似于 Gmail 等中的自动建议）。还有编辑（一种无需离开当前打开的文件即可修改代码的方法）和操作（常用用例的快捷方式）。

Continu 具有用户友好的 UI，可以从你的 IDE 插件市场免费安装。

## Tabby

[Tabby](https://github.com/TabbyML/tabby) 是一款自托管的 AI 编码助手，可以作为 GitHub Copilot 的另一种替代方案。使用 Tabby，你可以在本地安装和使用它，因此无需依赖第三方（这意味着更高的隐私），并支持消费级 GPU。

你可以使用以下命令在一分钟内将 Tabby 部署为 Docker 容器：

`docker run -it –gpus all -p 8080:8080 -v $HOME/.tabby:/data tabbyml/tabby serve –model StarCoder-1B –device cuda –chat-model Qwen2-1.5B-Instruct`

Tabby 的功能包括代码完成、上下文理解、AI 驱动的建议和代码分析，以减少开发时间，提高代码质量并提高生产力。

## Configu

[Configu](https://configu.com/) 是一个开源的配置即代码平台，用于自动化配置管理、防止错误配置以及通过配置和自动化不同环境中软件应用程序的部署来消除繁琐的重复性任务。

使用 Configu，你的工程团队可以无缝地管理和协作处理任何环境中的环境变量、密钥和功能标志。此工具可以轻松集成到现有系统和工作流程中，并且可以从小到大、从简单到复杂以及从临时到重复的任务进行扩展。

Configu 用于环境管理、配置自动化和基础设施编排。将 Configu 添加到你的工作流程中，你将享受到更高的速度和效率、改进的一致性和简化的配置管理。

Configu 可以使用以下命令轻松安装：

`curl https://files.configu.com/cli/install.sh | sh`

## Tauri 2.0

[Tauri](https://tauri.app/) 是一款开源工具，使开发人员可以使用现代基于 Web 的技术（例如 React、Angular 或 Vue.js）创建桌面应用程序。Tauri 提供类似 Electron 的环境，其中包括窗口、菜单和文件对话框等功能。使用 Tauri，你可以为 Linux、macOS 和 Linux 创建外观和感觉都很自然的应用程序。因为 Tauri 使用流行的基于 Web 的框架和库，所以它有助于减少构建桌面应用程序所需的时间。

使用 Tauri，你的开发人员将享受到更快的开发时间、更轻松的应用程序维护和改进的跨平台兼容性，这要归功于预构建的 UI 组件、基于 Web 的配置文件和本机应用程序性能优化。

典型的 Tauri 工作流程如下所示：

1. 使用 React、Angular 或 Vue.js 构建 Web 应用程序。
2. 将网络应用程序转换为具有原生行为的桌面应用程序。
3. 在不同平台上测试和改进桌面应用程序，然后再发布。

任何一个应用程序都能帮助提高您的编码效率。更好的是……总有更多开源应用程序可以帮助提高效率。
