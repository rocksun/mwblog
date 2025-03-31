<!--
title: Endor：基于WebAssembly的浏览器内服务器
cover: https://cdn.thenewstack.io/media/2025/03/aa6767f2-getty-images-6dnmfeeaht0-unsplash.jpg
summary: 颠覆认知！Endor横空出世：基于 WebAssembly，数据库、Web服务器、语言运行时毫秒级启动！无需Docker，浏览器秒变云原生开发环境，PHP、MySQL、Linux全栈支持，Emscripten功不可没！
-->

颠覆认知！Endor横空出世：基于 WebAssembly，数据库、Web服务器、语言运行时毫秒级启动！无需Docker，浏览器秒变云原生开发环境，PHP、MySQL、Linux全栈支持，Emscripten功不可没！

> 译自：[Endor: WebAssembly-Based Server in the Browser](https://thenewstack.io/endor-webassembly-based-server-in-the-browser/)
> 
> 作者：B Cameron Gain

巴塞罗那 – [WebAssembly](https://thenewstack.io/webassembly/) 已经展示了其在极快的启动时间、安全优势和其他能力方面的强大功能。最初是为浏览器设计的，但随着 [WASI](https://thenewstack.io/why-wasi-preview-2-makes-webassembly-production-ready/) 组件标准的形成，它现在正在扩展到服务器和边缘。

在本周于此举行的 [Wasm I/O conference](https://2025.wasm.io/) 期间，展示了如何将 WebAssembly 的各种功能和单个服务组合到一个完全在浏览器中启用的结构化环境中。无需下载任何内容——但完整的服务器和开发环境功能可直接在浏览器中使用。这些服务器功能可以毫秒级启动和管理，这要归功于 [Wasm](https://thenewstack.io/wasm-spin-and-spinkubes-rocky-road-to-cncf-sandbox-status/)，其中包括数据库、Web 服务器和语言运行时，它们利用了浏览器在存储、网络和计算能力方面的改进。

> 它被称为 Endor，并且主要基于开源构建。Angel de Miguel 和 [@vomkriege] 在 [@wasm_io] 上解释了如何利用 Wasm 和浏览器来构建一个“梦想编程环境”。浏览器变成了一台计算机，克服了许多资源限制。
>
> [@thenewstack](pic.twitter.com/4Tan3x3h69)
>
> — BC Gain (@bcamerongain),March 27, 2025

在 Wasm I/O 上，Endor 首席执行官 Daniel Lopez 和首席技术官 Angel de Miguel，该项目的联合创始人，展示了他们的工作。他们展示了一个演示并讨论了他们的项目 Endor，该项目建立在 [Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/) 和其他开源技术之上。两者都强调了他们致力于为开源社区做出贡献，作为这项计划的一部分。

“如今，开始使用服务器软件最困难的部分是正确设置和配置所有内容。我们构建 Endor 的目的是让开发人员可以轻松启动并运行他们喜欢的堆栈，”Lopez 告诉我。“你只需要一个浏览器——没有比这更容易的了。”

## 连接的力量

WebAssembly 最初是为了在浏览器中运行应用程序而创建的，现在作为一个类固醇编译器，它扩展了应用程序，使其能够在网络、设备、服务器和其他环境中以非常快的速度和非常低的延迟规范运行。借助 Endor，运行服务器应用程序和开发平台所需的组件都在浏览器中。

“连接的力量意味着如果有人需要访问某些东西，他们不需要安装任何东西。他们只需访问网址即可，这使得它对共享极具吸引力，”Lopez 在 Wasm I/O 期间说。“现在，只需一个链接，用户就可以运行数据库、执行 PHP 代码并执行各种任务。这种便利既神奇又实用。”

Lopez 说，Python、Ruby 和 PostgreSQL 等各种技术已经在使用 WebAssembly 进行使用和分发。

“服务器最重要的方面是您可以在其上运行的软件。如果必要的应用程序不可用，那么构建访问文件系统或网络的解决方案的能力是无关紧要的。在 2025 年，服务器软件开发主要涉及 Docker 容器、Linux 和软件包管理系统，”De Miguel 说。“我们对 Endor 的演示展示了一种集成多个开源组件以创建无缝体验的方法，从克隆 GitHub 存储库到部署该应用程序，所有这些都在不离开浏览器的情况下完成。”

此外，与传统服务器不同，Endor 的浏览器功能不依赖于专用服务器。相反，沙盒环境集成在浏览器本身中。

## 一切都在浏览器上运行

对于开发人员来说，Endor 的方法不依赖于传统的虚拟机 (VM)。相反，一切都在浏览器上运行。某些组件（如 PHP）直接编译为 Wasm 代码，而其他组件（如 [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/)）可能作为基于 Wasm 的硬件仿真器中的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 容器运行。然后使用浏览器内的虚拟 TCP/IP 网络将不同的部分连接起来。然后可以将 phpMyAdmin 等应用程序部署在它之上，可以通过从本地文件系统挂载文件夹或克隆 GitHub 存储库来实现。
通过利用这项技术，传统上在运行 [VirtualBox](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/)、[Docker Desktop](https://thenewstack.io/create-a-development-environment-in-docker-desktop/) 或类似工具的 Linux 虚拟机上执行的任务可以在浏览器中执行，Lopez 说。用户不再需要手动安装 MySQL 或配置 Docker 容器。相反，他们只需单击一个按钮即可立即启动 MySQL。Lopez 说，与传统的开发工作流程相比，这种方法更方便、更容易访问。