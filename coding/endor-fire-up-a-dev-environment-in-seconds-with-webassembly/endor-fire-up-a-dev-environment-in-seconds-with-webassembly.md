
<!--
title: Endor：借助WebAssembly技术，秒建开发环境
cover: https://cdn.thenewstack.io/media/2025/08/0657579d-joe-eitzen-mdk6dgeihk4-unsplash.jpg
summary: Endor利用WebAssembly技术，允许开发者在浏览器和命令行中快速创建隔离的测试环境，无需远程服务器，代码安全且便于共享。它通过极速启动时间和沙箱环境，简化了开发流程，适用于人工智能和代理编码等场景。
-->

Endor利用WebAssembly技术，允许开发者在浏览器和命令行中快速创建隔离的测试环境，无需远程服务器，代码安全且便于共享。它通过极速启动时间和沙箱环境，简化了开发流程，适用于人工智能和代理编码等场景。

> 译自：[Endor: Fire up a Dev Environment in Seconds With WebAssembly](https://thenewstack.io/endor-fire-up-a-dev-environment-in-seconds-with-webassembly/)
> 
> 作者：B. Cameron Gain

新推出的 [Endor](https://thenewstack.io/endor-webassembly-based-server-in-the-browser/) 允许开发者在几秒钟内创建可重现、隔离的测试环境，而不是花费数小时或数天，这得益于 [WebAssembly](https://thenewstack.io/webassembly/) 的闪电般速度。

Endor 的开发者表示，这种能力在向 [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) 提问、运行代理和进行 [氛围编程](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) 的时代尤为重要，它允许开发者快速且安全地测试代码。Endor 提供了在浏览器和命令行中执行此操作的方法。

WebAssembly 是实现这一切的底层技术，尽管大多数开发者可能不会关心细节。WebAssembly 提供了平台启动和运行的闪电般速度，使得在 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 上创建 [Linux shell](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 只需几秒钟，而不是像为开发目的设置测试环境那样需要数小时。

Endor 的一些优势包括跨平台的一致性和无状态、可重现的环境。这意味着无论操作系统如何，环境都将以相同的方式运行（尽管 ReveCom 仅在 MacOS 中为此文章进行了测试），并且不依赖于系统上存在的特定库。

当然，WebAssembly 著名的沙箱环境可以在运行这些小型或大型程序时保护系统，您可以根据需要进行调整。环境不会干扰或与您正在使用的主机上的现有依赖项和配置文件冲突，因为默认情况下文件系统访问和网络已禁用。

这扩展了 Endor 的用途，允许运行有风险甚至是不安全的代码——或破坏性的混沌测试——而无需担心干扰或导致主机出现问题。这也意味着当您作为开发者在一个项目上协作时，每个人都拥有完全相同的测试环境。

基于 Endor WebAssembly 的环境完全在本地运行，无论是在浏览器中还是在命令行中。这意味着没有远程服务器，您的代码和脚本永远不会离开您的机器。但是，这也意味着性能将受到本地 CPU 和内存的限制。

## 设置和运行

开发者开始使用 Endor 只需访问 Endor 服务器并安装 shell 即可。至少在 Mac 上，建议首先使用 Homebrew 安装 Endor：

[![](https://cdn.thenewstack.io/media/2025/07/6640ce68-screenshot-2025-07-31-at-9.11.23%E2%80%AFam.png)](https://cdn.thenewstack.io/media/2025/07/6640ce68-screenshot-2025-07-31-at-9.11.23%E2%80%AFam.png)
然后访问您喜欢的控制台——无论您是在 Mac、PC 还是 Linux 机器上——现在您就在本地机器上运行了一个可用的 [Alpine Linux](https://thenewstack.io/wizos-a-new-enterprise-linux-built-on-alpines-secure-foundation/) 副本。

[![](https://cdn.thenewstack.io/media/2025/07/be839b25-screenshot-2025-07-31-at-9.16.36%E2%80%AFam-1024x409.png)](https://cdn.thenewstack.io/media/2025/07/be839b25-screenshot-2025-07-31-at-9.16.36%E2%80%AFam-1024x409.png)

添加您的程序或代码：

[![](https://cdn.thenewstack.io/media/2025/07/cf09abf4-screenshot-2025-07-30-at-10.07.18%E2%80%AFpm-1024x362.png)](https://cdn.thenewstack.io/media/2025/07/cf09abf4-screenshot-2025-07-30-at-10.07.18%E2%80%AFpm-1024x362.png)

这是我在看一个极客版的“星球大战”：

[![](https://cdn.thenewstack.io/media/2025/07/4c78822f-screenshot-2025-07-31-at-9.17.55%E2%80%AFam-1024x405.png)](https://cdn.thenewstack.io/media/2025/07/4c78822f-screenshot-2025-07-31-at-9.17.55%E2%80%AFam-1024x405.png)

[![](https://cdn.thenewstack.io/media/2025/07/e8dc6755-screenshot-2025-07-31-at-9.18.11%E2%80%AFam-1024x524.png)](https://cdn.thenewstack.io/media/2025/07/e8dc6755-screenshot-2025-07-31-at-9.18.11%E2%80%AFam-1024x524.png)

Endor 由前 Bitnami 联合创始人和开发负责人独立开发，其联合创始人兼首席执行官 Daniel Lopez Ridruejo 和首席技术官 Angel de Miguel 代表了 WebAssembly 的实用性和可访问性的一个重要里程碑或步骤，因为它现在已准备好供最终用户运行。

它与 WebAssembly 的后端和服务器方面尤其相关，开发者可以亲身使用，而不是像过去几年那样在浏览器中使用（最初就是为此目的而创建的），以及用于云基础设施应用程序，例如使用 microVM 降低延迟和使用 Azure 的 Hyperlite 提高隔离性。

## Wasm Days

WebAssembly 已经通过极快的启动时间、安全优势和其他功能证明了其强大之处。最初专为浏览器设计，现在随着 WASI 组件标准的形成，它正在扩展到服务器和边缘。

在今年早些时候在巴塞罗那举行的 [Wasm I/O conference](https://2025.wasm.io/) 上，Endor 在此首次亮相，它展示了 Endor 如何利用 WebAssembly 的各种功能和各个服务组合成一个完全在浏览器或远程服务器中启用的结构化环境。无需下载任何内容——然而，一个完整的服务器和开发环境功能可以直接在浏览器中使用。这些服务器功能可以借助 Wasm 在几毫秒内启动和管理，包括利用浏览器在存储、网络和计算能力方面的改进的数据库、Web 服务器和语言运行时。

在 Wasm I/O 上，Lopez Ridreujo 和 de Miguel 展示了一个演示并讨论了 Endor，它是建立在 [Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) 和其他开源技术之上的。两者都强调了他们致力于为开源社区做出贡献，作为这项计划的一部分。

Lopez Ridreujo 说：“随着人工智能和代理编码系统的使用，越来越需要按需提供开发环境。Endor 可以轻松地在命令行和浏览器中执行此操作。”

## 连接的力量

WebAssembly 最初是为了在浏览器中运行应用程序而创建的，现在作为一个强大的编译器，它以极快的速度和极低的延迟规范将应用程序扩展到跨网络、设备、服务器和其他环境运行。借助 Endor，运行服务器应用程序和开发平台所需的组件都在浏览器中。

“连接的力量意味着如果有人需要访问某些东西，您只需向他们发送一个网址即可。这使得共享变得容易。” Lopez Ridruejo 在 Wasm I/O 期间说。“我们希望用 Endor 捕捉这种魔力，只需访问一个网址或在终端中输入这一行代码，您就可以启动并运行一个开发环境。”

Lopez Ridruejo 说，[Python](https://thenewstack.io/what-is-python/)、[Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) 和 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) 等各种技术已经在使用 WebAssembly 进行分发。“WebAssembly 正在逐渐但肯定地在开发的许多方面取得进展，对于越来越多的用例而言，它是 Docker 和其他技术的可行替代方案，” de Miguel 说。“Endor 只是这种趋势的一个例子。”

此外，与传统服务器不同，Endor 的浏览器功能不依赖于专用服务器。相反，沙箱环境集成到浏览器本身中。

## 一切都在浏览器上运行

对于开发者而言，Endor 的方法不依赖于传统的虚拟机 (VM)。相反，一切都在浏览器上运行，或者对于命令行版本，则在 Node 内部运行。某些组件（如 [PHP](https://thenewstack.io/the-herd-is-strong-php-and-its-developer-ecosystem-at-30/)）直接编译为 Wasm 代码，而其他组件（如 [MySQL](https://thenewstack.io/linux-back-up-a-mysql-database-from-the-command-line/)）可能作为 Linux 容器在基于 Wasm 的硬件模拟器中运行。然后使用浏览器内的虚拟 TCP/IP 网络将不同的部分连接起来。然后可以在其上部署 [phpMyAdmin](https://www.phpmyadmin.net/) 等应用程序，方法是从本地文件系统挂载文件夹或克隆 GitHub 存储库。

Lopez Ridruejo 说，通过利用这项技术，传统上在运行 VirtualBox 的 Linux VM、[Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 或类似工具上执行的任务可以在浏览器或 Node 环境中执行。用户不再需要手动安装 MySQL 或配置 Docker 容器。相反，他们只需单击一个按钮即可立即启动 MySQL。Lopez Ridruejo 说，与传统的开发工作流程相比，这种方法更加方便和易于访问。