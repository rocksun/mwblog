<!--
title: EngFlow使C++构建速度提高21倍，软件安全性大大提高
cover: https://cdn.thenewstack.io/media/2025/04/b0fb4788-skyler-h-xalujbpfbsi-unsplash.jpg
summary: C++福音！EngFlow收购tipi.build，推出CMake RE公测，集成HermeticFetchContent，构建速度飙升21倍！基于Bazel远程执行，加速C/C++构建，提升软件安全性，解决SBOM依赖管理难题，AI时代必备！
-->

C++福音！EngFlow收购tipi.build，推出CMake RE公测，集成HermeticFetchContent，构建速度飙升21倍！基于Bazel远程执行，加速C/C++构建，提升软件安全性，解决SBOM依赖管理难题，AI时代必备！

> 译自：[EngFlow Makes C++ Builds 21x Faster and Software a Lot Safer](https://thenewstack.io/engflow-makes-c-builds-21x-faster-and-software-a-lot-safer/)
> 
> 作者：Darryl K Taft

[EngFlow](https://www.engflow.com/) 是一家构建加速公司，由前 [Google](https://cloud.google.com/?utm_content=inline+mention) 工程师创建，他们负责为开发者提供远程构建执行的开源 [Bazel](https://bazel.build/) 项目。最近，EngFlow 推出了 [CMake RE](https://www.engflow.com/product/cmakere) 的公开测试版，这是一种为 [CMake](https://cmake.org/) 软件 [构建系统](https://thenewstack.io/engflow-bazel-and-more-for-faster-builds/) 用户提供的远程执行服务。
EngFlow 最近还收购了一家名为 [tipi.build](https://tipi.build/) 的公司，以加强其构建加速产品线。

## Tipi

tipi.build 提供快速的远程 [C](https://thenewstack.io/the-obfuscated-c-code-competition-returns/)、[C++](https://thenewstack.io/out-with-c-and-c-in-with-memory-safety/) 和 [Rust](https://thenewstack.io/rust-programming-language-guide/) 构建，其缓存技术基于 CMake 和 [Git](https://thenewstack.io/need-to-know-git-start-here/)。Tipi 使开发人员能够立即测试和构建跨平台，并在需要时添加云 CPU 核心，从而使持续集成触手可及。

Tipi 总部位于瑞士苏黎世，由 CMake 爱好者和 C++ 开发人员创立，他们希望在不牺牲性能或安全性的前提下提高开发人员的灵活性。Tipi 产品用于开发物联网 (IoT)、金融交易、医疗设备、汽车等行业的关键软件。

Engflow 和 Tipi 之前曾在 CMake 远程构建执行服务方面进行过合作，此次收购为 EngFlow 客户提供了更深入的构建系统现代化和缓存方面的专业知识。

## CMake RE 和 HermeticFetchContent

CMake RE 的测试版为 CMake 软件构建系统用户提供远程执行服务。它还为 C 和 C++ 开发人员提供构建加速、缓存和远程执行。此外，其功能还包括本地 hermetic CMake 构建、构建和依赖项缓存以及云构建分发。

新的开源项目 [HermeticFetchContent](https://tipi.build/blog/20250225-hfc-launch) 为 C 和 C++ 开发人员带来了更现代的构建系统功能。它解决了软件安全和持续交付方面的挑战，并提供了依赖项管理和溯源机制，包括 [软件物料清单 (SBOM)](https://thenewstack.io/a-good-sbom-is-hard-to-find/)。

当与 CMake RE 结合使用时，HermeticFetchContent 可以显着加快构建速度——在某些情况下 [速度提高高达 21 倍](https://github.com/tipi-build/hfc-bench/blob/main/README.md)。

“我们与 CMake RE 和 HermeticFetchContent 的创建者 tipi.build 合作，以优化我们针对数百种配置的 CMake 构建，”高频交易领域的 C++ 工程师兼 ISO C++ 标准委员会成员 [Jody Hagins](https://cplusplusonline.com/) 在一份声明中表示。“他们基于源代码的缓存构建方法不仅加快了我们的构建速度，还通过允许我们在整个依赖链中启用 sanitizers 来提高了安全性。”

## 代码库呈指数级增长，C++ 开发也是如此

EngFlow 首席执行官 [Helen Altshuler](https://www.linkedin.com/in/helen-altshuler/) 告诉 The New Stack，随着代码库越来越大，这些工具变得越来越重要，尤其是在人工智能呈指数级增长地增加代码行数的情况下。该技术有助于将构建时间从数小时缩短到数分钟，并支持估计超过 700 万开发人员的 C 和 C++ 开发人员社区。

Tipi 联合创始人 [Damien Buhl](https://www.linkedin.com/in/damien-buhl/) 表示，C++ 开发仍在增长，尤其是在金融、嵌入式系统、物联网和人工智能领域。据报道，像 Google 这样的公司正在将 Python 代码库迁移到 C++ 以提高效率，因为所需的服务器数量减少了 7 倍。

“所有人工智能公司都在使用 C++，因为……如果你用 C++ 构建软件，你需要的服务器数量比用 PHP 或 Python 构建的少 7 倍，”Buhl 说。

组合平台 (CMake RE) 提供了一个两层远程执行系统：

- 第 1 层 (tipi.build)：本地构建加速，但受到机器大小的限制。
- 第 2 层 (EngFlow)：分布式构建系统，可以跨数千个核心进行扩展。
它们共同创造了一种比使用大型独立机器更具成本效益的“超级计算机”体验。

“[可观测性]我们正在将 20,000 个核心或 40,000 个核心（分布在许多计算机上）变成一个核心，”Altshuler 告诉 The New Stack。“因此，从使用远程执行的客户的角度来看，他们拥有这个集群，所以本质上，他们拥有一台超级计算机。”
的确，人工智能已经在生成大量的代码。人工智能也在生成大量的劣质代码，“这会显著降低速度。我们与一些客户交谈过，他们现在有大量的构建在排队，”她说。

Altshuler补充说：“在代码更多、测试迭代次数更多的时代，尤其是在代码质量不高的情况下……拥有最强大和可扩展的系统来处理构建和测试工作流程非常重要。”

## 基于 Bazel

近年来，谷歌的 Bazel 项目已成为当今复杂的多语言代码库的最佳构建系统之一，并且其内在设计旨在克服这些问题。然而，EngFlow 的 Bazel 集群技术为大型开发团队提供了增强的构建系统性能。

此外，Buhl 表示，两家公司及其各自的技术（tipi.build 和 EngFlow）的结合，将 Bazel 远程执行和缓存的所有优势带给 CMake，而无需进行破坏性的构建系统迁移。

## 满足安全要求

同时，HermeticFetchContent 解决了软件安全和持续交付的挑战，以满足监管要求。

使用 C 和 C++ 的工程平台团队在安全和持续软件交付方面面临着新的挑战，特别是当联邦政府呼吁[从关键系统中消除 C 和 C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)时。

Buhl 指出，Rust、C 和 C++ 代码的编译和自动化测试是计算密集型的，常见的代码库可能需要数小时才能编译，从而生成非常大的构建树。当团队将静态分析器和清理器工具添加到他们的构建和测试中，以处理美国国家安全局、白宫和欧盟最近定义的安全要求时，这些问题会更加严重。

Buhl 说，HermeticFetchContent 使开发人员能够在整个依赖链上运行内存安全检查（清理器）。