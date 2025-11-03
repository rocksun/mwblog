
<!--
title: Linux：微软WSL十年磨砺，终拥抱开源
cover: https://cdn.thenewstack.io/media/2025/11/a961a840-dave-kim-sltmudkal9m-unsplash.jpg
summary: WSL起源于Astoria，经WSL 1.0（兼容层）到WSL 2（虚拟机）发展。微软克服困难将其开源，获得巨大成功，并成为公司开源项目的典范。
-->

WSL起源于Astoria，经WSL 1.0（兼容层）到WSL 2（虚拟机）发展。微软克服困难将其开源，获得巨大成功，并成为公司开源项目的典范。

> 译自：[Linux: Microsoft WSL's Decade-Long Journey to Open Source](https://thenewstack.io/linux-microsoft-wsls-decade-long-journey-to-open-source/)
> 
> 作者：Steven J. Vaughan-Nichols

伦敦 — [Craig Loewen](https://www.linkedin.com/in/craig-loewen)，微软负责[适用于 Linux 的 Windows 子系统 (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) 的高级产品经理，和负责监管 WSL 的首席产品经理主管 Clint Rutkas，在 [Canonical](https://canonical.com/) 的 [Ubuntu 25.10 峰会](https://ubuntu.com/summit)上首次讲述了[WSL 最终开源](https://thenewstack.io/the-windows-subsystem-for-linux-is-now-open-source/)的故事。这是一段漫长而奇特的旅程。

## WSL 在 Astoria 项目中的起源

WSL 的故事始于 2010 年的 [Astoria 项目](https://trungnt2910.com/astoria-windows-android/)，也被称为 Windows Bridge for Android。这个胎死腹中的项目旨在通过 Windows 10 Mobile 内核中的一个翻译层，让人们能够在 Windows Phone 上运行 Android 应用。既然你口袋里不太可能有一部能正常工作的 Windows Phone，你就知道结果如何了。

最初的原型将 [Linux 系统调用](https://thenewstack.io/introduction-to-linux-operating-system/)转换为 Windows NT 内核调用，为 [Bash 和 Ubuntu 在 Windows 上于 2016 年发布](https://www.zdnet.com/article/ubuntu-not-linux-on-windows-how-it-works/)奠定了基础。这项最初的工作由 Canonical 协助构建，重新编译了 [Cygwin 的开源工具](https://www.cygwin.com/)，使其能在 Windows 上原生运行。当时 Canonical Ubuntu 产品和策略团队的成员 Dustin Kirkland 解释说：“我们谈论的是一模一样的，校验和也完全匹配的[直接在 Windows 中运行的 Ubuntu ELF 二进制文件](https://www.zdnet.com/article/ubuntu-not-linux-on-windows-how-it-works/)。”

## 首次迭代：WSL 1.0 兼容层

当时，Kirkland 说：“微软的一支精明开发团队一直努力工作，调整了一些微软研究院的技术，基本上实现了 Linux 系统调用到 Windows 操作系统系统调用的实时翻译。Linux 极客可以将其视为 [WINE](https://www.winehq.org/)（[这个开源程序能让人们在 Linux 上运行 Windows 程序](https://www.winehq.org/)）的某种反向操作——Ubuntu 二进制文件在 Windows 中原生运行。”

这就是 [WSL 1.0](https://www.zdnet.com/article/windows-subsystem-for-linux-graduates-in-windows-10-fall-creators-update/) 的前身。这是一个兼容层，通过使用一种称为“[pico 进程](https://learn.microsoft.com/en-us/archive/blogs/wsl/pico-process-overview)”的机制，将 Linux 系统调用转换为 Windows NT 内核调用，从而使人们能够运行 Ubuntu、openSUSE 和 Fedora 等 Linux 发行版。它于 2017 年作为 Windows 10 秋季创意者更新的一部分发布。

## 新方法：WSL 2 的崛起与普及

用户，主要是开发者，喜欢它，但他们都报告说 WSL 1.0 很慢。于是，微软退后一步，重新审视并尝试了一种运行 Linux 及其应用程序的新方法。团队决定[开发他们自己的 Linux 内核](https://www.zdnet.com/article/hell-freezing-over-microsoft-releases-its-own-linux-for-windows/)。因此，WSL 2 采取了根本不同的方法。WSL 2 不再使用仿真，而是使用轻量级托管虚拟机 (VM) 来运行微软 Linux 内核，该内核通过 Windows Update 进行更新。

这个版本在开发者中变得非常流行，尤其是在 2020 年 5 月稳定发布之后。[数百万用户采用它进行编程、系统管理和云工程工作流](https://ubuntu.com/blog/wsl-ubuntu-2022-year-in-review)。根据 [2022 年 Stack Overflow 开发者调查](https://survey.stackoverflow.co/2022)，其受欢迎程度在 2021 年至 2023 年间加速增长，使用 WSL 作为主要操作系统的开发者比例在一年内增长了近五倍，从 3% 增加到超过 14%。

## 微软内部推动 WSL 开源

在微软内部，WSL 的开发者开始推动 WSL 2.0 开源。正如 Loewen 所说，这完全合乎情理。毕竟，“Linux 是开源的，对吧？我们正在开发一款将 Linux 带到 Windows 操作系统的 Linux 产品。我们希望它能与社区融合，并在社区所在地。我们在那里是有意义的。这就是商业价值，拥抱社区。”

Loewen 补充说：“它不可能更早发生，因为 WSL 最初与 Windows 内核结合得太紧密，我们无法开源它。即使我们想，我们也不被允许。然后随着时间的推移，我们开始这么做，因为我们觉得，‘这需要开源！’所以我们开始移除所有私有调用，解耦一切，这就是我们能走到今天的原因。”

## 克服将 WSL 与 Windows 解耦的挑战

这花了很多时间。Loewen 说：“我们花费了数年时间来解耦私有 API 并重构长期存在的依赖关系，最终使微软能够发布负责 WSL 的完整代码。”

微软内部推动 WSL 开源涉及三个主要策略：庆祝社区参与、展示商业价值以及全面评估收益和成本。在内部，团队认为开源 WSL 与微软支持开发者工具用户的更广泛战略不谋而合。Linux 本身是开源的，需要在 Windows 环境中采取以社区为中心的方法，以赢得用户信任并实现有效演进。

有时这是一项艰苦的工作。Rutkas 承认，“开源是有益的，但它需要时间和精力。你必须说服你的利益相关者。”

## 开源 WSL 的即时成功

然而，一旦完成，它便取得了巨大的成功。Rutkas 说：“我们一开源，它在 GitHub 上的星标就从 15,000 涨到了 30,000 多。这很好——而且是在一天之内。它飙升了。它登上了 [Hacker News](https://news.ycombinator.com/)，而且我认为它在那里是第一帖子，持续了 24 小时，这简直是闻所未闻。所以，我们知道我们做出了正确的决定。”

这一转变再次证明并非所有技术都必须是专有的。是的，即使在微软也是如此。两人表示，WSL 的真正价值在于提高开发者的生产力，而非“秘密武器”的差异化。团队表示，这证明开源可以驱动任务价值，其重要性超过了竞争顾虑。通过采纳开源模式，微软赋能外部开发者以私有团队无法比拟的速度解锁解决方案和改进。

## 微软未来开源项目的蓝图

WSL 团队的开源工作现在指导着微软的最佳实践。它已成为其他主要微软面向程序员项目的蓝图，例如 Windows Terminal、PowerToys 和[微软的新 CLI 编辑器 Edit](https://devblogs.microsoft.com/commandline/edit-is-now-open-source/)。两人表示，优先考虑开源优先的结果已被证明是可衡量的、积极的，并且是微软未来开源转型的蓝图。

微软成为开源软件领导者？十年前谁能想到呢？