
<!--
title: Docker替代品Flox有Kubernetes的库
cover: https://cdn.thenewstack.io/media/2025/01/c7fe7be5-capture-decran-2025-01-10-201516-1.png
-->

Flox 简化了企业使用的 Nix，提供了一种无容器的 Docker 替代方案，承诺更好的依赖管理和跨平台兼容性。

> 译自 [Docker Replacement Flox Has Libraries for Kubernetes](https://thenewstack.io/docker-replacement-flox-has-libraries-for-kubernetes/)，作者 B Cameron Gain。

[初创公司 Flox](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/)已经展示了其对[Nix](https://thenewstack.io/flox-gears-up-nix-for-the-enterprise/)的改进如何作为[Docker](https://thenewstack.io/when-webassembly-replaces-docker/)的可行替代方案，值得仔细研究。虽然 Nix 已经存在多年，并且以其复杂性而闻名，但 Flox 简化了其使用和采用。最近，Flox 将其版本的 Nix 定位为[Kubernetes](https://thenewstack.io/kubernetes/)上 Docker 容器的潜在替代品。

[Flox](https://flox.dev/)被描述为面向开发人员和运维团队的环境和平台，以跨平台的方式提供可重复性和应用程序部署。但是，它实现了跨不同环境的一致性，并且可以利用 Flox，Flox 集成了 Nix 的最佳功能，使其更易于访问并简化了 Nix 环境的使用。

[Nix 存储库](https://nixos.org/)的工作方式与传统的 OCI 注册表不同。虽然 OCI 注册表运行有效，但它们的[容器](https://thenewstack.io/containers/)层依赖于分层文件系统。在这样的系统中，更改一层会使所有后续层失效。相比之下，Nix 存储库在 Nix 存储库中提供了许多派生版本——Flox 称之为“Nixpkgs 包”的超过 120,000 个。它们可能由单个文件或 shell 脚本组成，这有助于避免不必要的失效。

例如，在为 .sh 设置依赖树时，只需要少量相关的文件。然后，这些文件可以在各种项目中重复使用，与基于容器的系统相比，在依赖项管理方面提供了更高的分辨率。

## 云原生 Nix

正如 Flox 的高级 DevRel 工程师和 Kubernetes 贡献者[Leigh Capili](https://www.linkedin.com/in/leighcs/)在 11 月的 Cloud Native Rejekts 上的“云原生 Nix！”演讲中解释的那样，云原生人员——那些已经受益于容器镜像和运行时的人——会对以确保其仅访问所需内容的方式打包软件感兴趣。让我阐述这种方法的重要性。

这种环境使列出我正在使用的 Nix 包生态系统中的软件变得容易。Flox 是我们构建的一个开源项目，旨在更轻松地理解如何使用这些包。例如，我可以列出我主目录中的软件，显示我想在我的系统上安装的包。您将看到诸如[zsh](https://www.zsh.org/)（我最喜欢的文本编辑器）和用于终端任务的实用程序之类的工具。

通常，软件的开发是为了使其能够运行、通过测试并打包到可以上传到注册表的容器镜像中。

然而，Capili 说，当使用 MacBook 时，重新考虑打包的一个令人信服的原因出现了。MacBooks 配备高级内核，例如 Darwin 内核，该内核也用于 iPhone。虽然 Darwin 内核提供了令人印象深刻的隔离功能，但它目前无法以所需的方式运行 OCI 容器。尽管有一个有趣的 Darwin 容器项目可能会在未来支持这一点，但 Capili 解释说，它尚未被广泛采用。

![](https://cdn.thenewstack.io/media/2025/01/097ce3c3-img_20241110_163428664_hdr-1024x771.jpg)

为了打包和使用云原生专业人员所需的软件，Capili 说用户通常依赖于 Docker、[Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/) 或 [nerdctl](https://thenewstack.io/containers/how-to-deploy-containers-with-nerdctl/) 等工具来访问在 Linux 环境中运行的守护程序。有趣的是，现代 Nixpkgs 包中的绝大多数软件都是跨构建在公共构建农场上的。然后将其存储在托管在 1.5 PB 实例上的二进制缓存中。Capili 说，这种设置使软件可用于 macOS 原生环境，从而减少了频繁运行虚拟机的需要，这是一个显著的优势。

在他的演示中，Capili 解释了为什么已经受益于容器镜像和运行时的云原生用户会对以确保其仅访问所需内容的方式打包软件感兴趣。“目标是阐明这种方法的重要性，”Capili 说。

正如Capili解释的那样，通常情况下，软件的开发是为了使其能够运行，通过测试，并打包成一个可以上传到注册表的容器镜像。Capili说，采用这种方法，似乎没有理由重新考虑习惯。现代工具允许创建可无限期存储的工作制品，并部署在诸如Functions as a Service、Kubernetes集群甚至Docker Desktop等平台上。Capili说，这种工作流程似乎足以满足大多数需求。

“假设我们要添加更多与基础设施相关的工具。我可以轻松安装这些软件包，尽管我可能需要拉取新版本，”Capili说。“最终，我们要查看运行时目录，我的配置文件、二进制文件和其他系统组件都指向我的Nix存储中的符号链接。”

为了完成这些任务，Nix存储中存在许多不同类型的软件。每次构建都在一个沙盒环境中进行，网络访问被锁定。系统时钟被固定以确保输出在不同构建之间完全一致。“这使得我们可以相信配方会产生一致的结果，从而使我们能够有效地缓存二进制文件，”Capili说。
