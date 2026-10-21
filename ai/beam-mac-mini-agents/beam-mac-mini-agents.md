<!--
title: Beam将运行智能体的Mac Mini应用窗口完美拉到本地
cover: https://cdn.thenewstack.io/media/2026/10/49ed5cf2-beam-1024x576.png
summary: Beam是一款全新的Mac应用，旨在解决运行AI智能体的Mac Mini远程操控痛点。它允许用户将远程Mac上的单个应用窗口直接拉到本地显示，操作如同本地软件一般，告别了传统笨重的屏幕共享。
-->

Beam是一款全新的Mac应用，旨在解决运行AI智能体的Mac Mini远程操控痛点。它允许用户将远程Mac上的单个应用窗口直接拉到本地显示，操作如同本地软件一般，告别了传统笨重的屏幕共享。

> 译自：[Beam pulls single app windows off the Mac Mini running your agents](https://thenewstack.io/beam-mac-mini-agents/)
> 
> 作者：Matthew Burns

[Beam](https://beam.win) 是一款全新的 Mac 应用，它能将一台 Mac 上运行的窗口投射到另一台 Mac 上，使其表现得如同本地安装的应用一样。为什么？为了智能体。

连续创业者 [Hiten Shah](https://www.linkedin.com/in/hnshah/)（曾联合创立 Crazy Egg 和 KISSmetrics）与 Sam Asante 共同在一家名为 Noats 的公司开发了它。该应用周二在 Product Hunt 上线，主要面向放在衣橱里运行 AI 智能体的无头 Mac Mini。

这个创意非常棒：用户不再需要打开屏幕共享（Screen Sharing）来操作整个远程桌面，而是只需在另一台机器上选择一个单独的窗口（比如智能体正在工作的终端会话或浏览器窗口），它就会直接打开并显示在你面前的 Mac 上，与其他应用并排显示。它拥有自己的 Dock 图标，可以通过 `Command+Tab` 切换器调出。调整该窗口的大小会同步调整另一台 Mac 上的窗口大小。键盘快捷键可以正常使用，文件可以跨设备拖放，应用的音频也可以在本地播放。应用本身永远不会离开原始机器。当一个窗口不够用时，Beam 还可以拉取整个显示器或整台 Mac。

Shah 在他的 [Product Hunt 发布帖](https://www.producthunt.com/products/beam-win) 中围绕自己的设置展开了阐述，他描述了运行智能体和本地模型的 Mac，“即使在没有人坐在它们面前时，工作也在继续”。要访问其中一台机器通常意味着需要进行屏幕共享并浏览第二个桌面。Beam 旨在将其精简为那一个最重要的窗口。

**Beam 顺应了为 AI 系统提供动力的 Mac 生态系统的爆发趋势**，因此该应用仅在 macOS 上运行。并且两台 Mac 都需要配备 Apple Silicon、macOS Sonoma 或更高版本，并安装了 Beam。这两台机器可以在同一个 Wi-Fi 网络上互相发现，也可以通过 Tailscale 在任何地方连接。

该公司表示，窗口、按键、剪贴板和音频直接在 Mac 之间传输，经过加密，且绝不会经过其服务器。它还表示，隐藏窗口和密码管理器绝不会出现在窗口选择器中。

对于没有安装 Beam 的设备，共享链接可以在任何浏览器中打开一个单独的窗口，默认只读（除非授予控制权限），有效期从一小时到一周不等。

Asante 在 Product Hunt 上表示，原生的 iOS 和 Android 应用正在开发中。

定价取决于设置。托管 Mac 和加入共享链接是免费的。使用自己的 Mac 每天前 20 分钟免费，之后为每月 12 美元、每年 84 美元或终身许可 199 美元。

Beam 顺应了智能体硬件的发展趋势。在 OpenClaw 的最初推动下，Mac Mini 正在成为常驻智能体的默认家园，随后 Perplexity 等其他应用也加入了进来。苹果在 4 月份的财报电话会议上也提及了智能体工作负载。

*The New Stack* 的 Janakiram MSV 很早就捕捉到了这一趋势，并在 5 月份报道了这一转变，他写道：[“Mac mini 刚刚成为了基础设施。”](https://thenewstack.io/mac-mini-agent-infrastructure/)

Beam 并不是第一个解决这个问题的人。我使用 Astropad 的 Workbench 几周，它让我能够通过桌面和 iOS 应用远程访问智能体。Workbench 押注于移动设备，而 Beam 则押注于远程访问的单位应该是窗口，而不是整个屏幕。Jump Desktop、Screens 和苹果自己的屏幕共享也都涵盖了这些基础功能。

尽管如此，这个问题是真实存在的并且正在不断加剧。藏在衣橱里或机架上的 Mac 正在成为开发者标准配置的一部分。Beam 的解决方案是彻底不再把它当作第二个桌面。